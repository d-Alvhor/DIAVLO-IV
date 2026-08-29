#!/usr/bin/env python3
"""
Tracker de builds — Diablo IV (Windows)

Le das a Trackear, dices si es TU personaje o un RIVAL, y empieza a mirar la
pantalla. Tú vas pasando el ratón por encima de tus objetos y habilidades; él
va rellenando la checklist solo. No termina hasta haberlo visto todo.

NO es un overlay: no dibuja sobre el juego, no lee su memoria, no automatiza
nada. Hace capturas de pantalla y las lee. La ventana es una ventana normal.

Instalación (una vez):
    pip install winocr mss pillow

Uso:
    python tracker.py
"""

import re
import sys
import json
import time
import unicodedata
import threading
from pathlib import Path
from datetime import datetime

try:
    import tkinter as tk
    from tkinter import ttk, simpledialog
except ImportError:
    tk = ttk = simpledialog = None

AQUI = Path(__file__).parent
PERFILES = AQUI / "perfiles"
CONFIG = AQUI / "config.json"
CORPUS = AQUI / "corpus"
SUFICIENTE = 6      # líneas útiles a partir de las cuales no se prueban más variantes

from catalogo import Catalogo
import valorar as V

CAT = Catalogo()   # 432 tipos, 891 afijos, 524 aspectos — de Diablo4Companion (MIT)

# ---------------------------------------------------------------- qué hay que ver
# Ya no adivinamos con palabras clave: la línea de tipo del tooltip es literalmente
# una entrada del catálogo, así que emparejamos contra los 432 nombres reales.
# Eso corrige de paso los errores del OCR ("Yelrno" -> Casco).
HUECOS = ["Casco", "Peto", "Guantes", "Pantalones", "Botas",
          "Arma", "Escudo", "Amuleto", "Anillo 1", "Anillo 2"]

N_HABILIDADES = 6

# Cómo se reconoce un tooltip de HABILIDAD, visto en capturas reales del juego:
#   Punición
#   RANGO 1/15                      <- firma inequívoca, ningún objeto la tiene
#   Tiempo de reutilización: 0,5 s
#   MODIFICADORES
# Nada de listas de nombres a mano: el nombre se toma de la primera línea, así
# funciona con cualquier habilidad de cualquier clase sin mantener nada.
RANGO = re.compile(r"\brango\s*\d+\s*/\s*\d+", re.I)
MARCAS_HABILIDAD = [
    "tiempo de reutilizacion", "modificadores", "probabilidad de golpe de suerte",
    "coste:", "de fe", "genera", "canalizada", "definitiva", "dano sagrado",
]

# ---------------------------------------------------------------- texto
def norm(s):
    s = unicodedata.normalize("NFD", str(s))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", s).strip().lower()


def identificar(texto):
    """Del texto de un tooltip saca (clase, hueco_o_nombre, nombre, texto).
    clase: 'objeto' | 'habilidad' | None."""
    lineas = [l.strip() for l in texto.splitlines() if l.strip()]
    if len(lineas) < 3:          # un tooltip real nunca son dos líneas sueltas
        return None
    n = norm(texto)

    # ¿objeto? La línea de tipo suele ser la 2ª. Contra el catálogo, no a ojo.
    for linea in lineas[:4]:
        hueco = CAT.hueco(linea)
        if hueco:                       # None = tipo conocido pero no es equipo
            return ("objeto", hueco, lineas[0].strip(), texto)

    # ¿habilidad? EXIGIMOS "RANGO n/15". La red de seguridad anterior ("dos
    # marcadores sueltos") metía basura de la interfaz —nombres de mercenario,
    # cabeceras de panel— como si fueran habilidades. Un falso positivo es peor
    # que no detectar: llena la checklist de mentiras y la da por completa.
    if RANGO.search(n) and len(lineas) >= 3:
        nombre = lineas[0].strip()
        # la 1ª línea puede ser basura del icono; nos quedamos con la primera
        # que parezca un nombre de verdad y no un dato
        for l in lineas[:3]:
            if 3 <= len(l) <= 40 and not re.search(r"\d", l) and not RANGO.search(norm(l)):
                nombre = l.strip()
                break
        return ("habilidad", norm(nombre), nombre, texto)
    return None


# ---------------------------------------------------------------- captura + OCR
def capturar(region=None):
    import mss
    from PIL import Image
    MSS = mss.MSS if hasattr(mss, "MSS") else mss.mss
    with MSS() as sct:
        mon = region if isinstance(region, dict) else (
            {"left": region[0], "top": region[1], "width": region[2], "height": region[3]}
            if region else sct.monitors[1])
        shot = sct.grab(mon)
        return Image.frombytes("RGB", shot.size, shot.bgra, "raw", "BGRX")


def _lineas_con_caja(res):
    """winocr devuelve cada línea con las cajas de sus palabras. Sacamos la caja
    de la línea entera para poder agrupar por cercanía."""
    out = []
    ls = res.get("lines") if isinstance(res, dict) else getattr(res, "lines", None)
    for l in (ls or []):
        txt = (l.get("text") if isinstance(l, dict) else getattr(l, "text", "")) or ""
        if not txt.strip():
            continue
        palabras = (l.get("words") if isinstance(l, dict) else getattr(l, "words", None)) or []
        cajas = []
        for w in palabras:
            r = w.get("bounding_rect") if isinstance(w, dict) else getattr(w, "bounding_rect", None)
            if not r:
                continue
            g = (lambda k: r.get(k) if isinstance(r, dict) else getattr(r, k, 0))
            cajas.append((g("x"), g("y"), g("width"), g("height")))
        if cajas:
            x = min(c[0] for c in cajas)
            y = min(c[1] for c in cajas)
            x2 = max(c[0] + c[2] for c in cajas)
            y2 = max(c[1] + c[3] for c in cajas)
            out.append({"texto": txt, "x": x, "y": y, "x2": x2, "y2": y2, "h": y2 - y})
        else:
            out.append({"texto": txt, "x": 0, "y": 0, "x2": 0, "y2": 0, "h": 0})
    return out


def agrupar(lineas):
    """Agrupa líneas en bloques por cercanía vertical y solape horizontal.
    Un tooltip es un bloque; el resto de la interfaz, otros. Así se puede leer
    la pantalla ENTERA sin que el ruido de alrededor estropee la lectura."""
    con_caja = [l for l in lineas if l["h"] > 0]
    if not con_caja:
        return ["\n".join(l["texto"] for l in lineas)] if lineas else []
    con_caja.sort(key=lambda l: (l["y"], l["x"]))
    bloques, actual = [], [con_caja[0]]
    for l in con_caja[1:]:
        prev = actual[-1]
        hueco = l["y"] - prev["y2"]
        alto = max(prev["h"], l["h"], 1)
        solapa = min(l["x2"], prev["x2"]) - max(l["x"], prev["x"])
        ancho = min(l["x2"] - l["x"], prev["x2"] - prev["x"]) or 1
        if hueco < alto * 1.6 and solapa > ancho * 0.25:
            actual.append(l)
        else:
            bloques.append(actual)
            actual = [l]
    bloques.append(actual)
    return ["\n".join(x["texto"] for x in b) for b in bloques]


def _lineas(res):
    if isinstance(res, dict):
        ls = res.get("lines") or []
        return [l.get("text", "") if isinstance(l, dict) else getattr(l, "text", "") for l in ls]
    ls = getattr(res, "lines", None)
    if ls:
        return [getattr(l, "text", "") for l in ls]
    return [getattr(res, "text", "") or ""]


def preparar(img, escala=2):
    """Los tooltips son texto claro sobre fondo oscuro SEMITRANSPARENTE, que es
    justo lo que peor lee un OCR. Escalar, subir contraste y binarizar ayuda
    bastante. Devuelve varias versiones: se prueban por orden."""
    from PIL import Image, ImageOps, ImageEnhance
    g = img.convert("L")
    g = g.resize((g.width * escala, g.height * escala), Image.LANCZOS)
    versiones = [("escalada", g)]
    alto = ImageEnhance.Contrast(g).enhance(2.2)
    versiones.append(("contraste", alto))
    versiones.append(("binaria", alto.point(lambda v: 255 if v > 140 else 0)))
    versiones.append(("binaria-inv", ImageOps.invert(alto.point(lambda v: 255 if v > 140 else 0))))
    return versiones


def ocr(img, guardar=None):
    """Lee el tooltip. Prueba la imagen cruda y varias preparaciones, y se queda
    con la que más líneas útiles saque. Si se pasa 'guardar', deja la captura y
    lo leído en corpus/ para poder medir la precisión más tarde."""
    import winocr

    def leer(im):
        try:
            return "\n".join(x for x in _lineas(
                winocr.recognize_pil_sync(im, "es-ES")) if x.strip())
        except Exception:
            return ""

    # El orden importa: primero las que mejor rinden en la medición, y solo se
    # corta cuando el resultado es COMPLETO (un tooltip tiene ~6 líneas útiles).
    # Cortar antes hacía que se quedara con la peor lectura, que es lo que pasaba.
    intentos = [("cruda", img)]
    try:
        intentos += preparar(img)
    except Exception:
        pass

    mejor, mejor_txt, mejor_n = "cruda", "", -1
    for nombre, im in intentos:
        t = leer(im)
        n = _utiles(t)
        if n > mejor_n:
            mejor, mejor_txt, mejor_n = nombre, t, n
        if mejor_n >= SUFICIENTE:
            break

    if guardar:
        _al_corpus(img, mejor_txt, mejor)
    return mejor_txt


def ocr_bloques(img, guardar=None):
    """Lee la pantalla ENTERA y devuelve bloques de texto separados.
    Cada tooltip acaba en su propio bloque, así no hace falta fijar zona."""
    import winocr
    try:
        versiones = [("escalada", preparar(img, escala=2)[0][1]), ("cruda", img)]
    except Exception:
        versiones = [("cruda", img)]
    mejor, mejor_bloques, mejor_n = "cruda", [], -1
    for nombre, im in versiones:
        try:
            res = winocr.recognize_pil_sync(im, "es-ES")
        except Exception:
            continue
        bloques = agrupar(_lineas_con_caja(res))
        n = sum(1 for b in bloques if identificar(b))
        if n > mejor_n:
            mejor, mejor_bloques, mejor_n = nombre, bloques, n
        if n:
            break
    if guardar:
        _al_corpus(img, "\n---\n".join(mejor_bloques), f"{mejor}/bloques")
    return mejor_bloques


def _utiles(texto):
    """Cuántas líneas parecen de verdad un afijo o un tipo de objeto."""
    n = 0
    for l in texto.splitlines():
        l = l.strip()
        if len(l) < 4:
            continue
        if re.search(r"\d", l) or CAT.hueco(l):
            n += 1
    return n


def _al_corpus(img, texto, variante):
    """Cada captura, con lo que leyó. Así el corpus de prueba se construye solo."""
    try:
        CORPUS.mkdir(exist_ok=True)
        marca = datetime.now().strftime("%Y%m%d-%H%M%S-%f")[:-3]
        img.save(CORPUS / f"{marca}.png")
        (CORPUS / f"{marca}.txt").write_text(
            f"# variante: {variante}\n{texto}", encoding="utf-8")
    except Exception:
        pass


# ---------------------------------------------------------------- perfil
class Perfil:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo               # "yo" | "rival"
        self.objetos = {}              # hueco -> {nombre, texto}
        self.habilidades = {}          # clave -> {nombre, texto}
        self.inicio = datetime.now().isoformat(timespec="seconds")

    def anadir(self, clase, clave, nombre, texto):
        """Devuelve True si es algo NUEVO."""
        if clase == "objeto":
            if clave == "Anillo":                      # dos anillos: por nombre
                ya = [k for k in self.objetos if k.startswith("Anillo")]
                if any(self.objetos[k]["nombre"] == nombre for k in ya):
                    return False
                if len(ya) >= 2:
                    return False
                clave = f"Anillo {len(ya) + 1}"
            if clave in self.objetos and self.objetos[clave]["nombre"] == nombre:
                return False
            nuevo = clave not in self.objetos
            afijos, total = V.analizar(texto, CAT)
            self.objetos[clave] = {
                "nombre": nombre, "texto": texto, "aporte": round(total, 1),
                "afijos": [{"grupo": a.get("grupo_real") or a["grupo"],
                            "valor": a["valor"], "mult": bool(a.get("mult")),
                            "pct": round(a["pct"], 1) if a.get("pct") is not None else None,
                            "tipo": a.get("tipo"), "muerto": a.get("muerto")}
                           for a in afijos]}
            return nuevo
        else:
            if clave in self.habilidades:
                return False
            if len(self.habilidades) >= N_HABILIDADES:
                return False
            self.habilidades[clave] = {"nombre": nombre, "texto": texto}
            return True

    def faltan(self):
        f = [h for h in HUECOS if h not in self.objetos]
        n = N_HABILIDADES - len(self.habilidades)
        return f, max(0, n)

    def completo(self):
        f, n = self.faltan()
        return not f and n == 0

    def guardar(self):
        PERFILES.mkdir(exist_ok=True)
        seguro = re.sub(r"[^\w\-. ]", "_", self.nombre).strip() or "sin_nombre"
        ruta = PERFILES / f"{self.tipo}_{seguro}.json"
        ruta.write_text(json.dumps({
            "nombre": self.nombre, "tipo": self.tipo, "inicio": self.inicio,
            "objetos": self.objetos, "habilidades": self.habilidades,
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        return ruta


# ---------------------------------------------------------------- ventana
class App(tk.Tk if tk else object):
    INTERVALO = 0.7          # segundos entre capturas

    def __init__(self):
        super().__init__()
        self.title("Tracker de builds — Diablo IV")
        self.geometry("640x760+40+40")
        self.configure(bg="#141210")
        self.attributes("-topmost", True)
        self.perfil = None
        self.grabando = False
        self.region = self._cfg().get("region")
        self.vistos_txt = set()
        self.ciclos = 0
        self.sin_nada = 0

        cab = tk.Frame(self, bg="#1c1917")
        cab.pack(fill="x")
        tk.Label(cab, text="TRACKER", bg="#1c1917", fg="#c14a4a",
                 font=("Georgia", 12, "bold")).pack(side="left", padx=10, pady=9)
        self.btn = tk.Button(cab, text="▶  Trackear", command=self.alternar,
                             bg="#c14a4a", fg="white", relief="flat", padx=14, pady=3,
                             font=("Segoe UI", 10, "bold"))
        self.btn.pack(side="left", padx=6)
        tk.Button(cab, text="Zona", command=self.elegir_region, bg="#232019",
                  fg="#e8e2da", relief="flat", padx=10).pack(side="left")
        tk.Button(cab, text="Ficha", command=self.leer_ficha, bg="#232019",
                  fg="#e8e2da", relief="flat", padx=10).pack(side="left", padx=4)
        self.estado = tk.Label(cab, text="parado", bg="#1c1917", fg="#9a9088",
                               font=("Segoe UI", 9))
        self.estado.pack(side="right", padx=12)

        self.lista = tk.Frame(self, bg="#141210")
        self.lista.pack(fill="both", expand=True, padx=14, pady=10)
        self.filas = {}
        self._construir_checklist()

        self.log = tk.Text(self, height=7, bg="#0f0d0c", fg="#9a9088", relief="flat",
                           font=("Consolas", 9), padx=10, pady=6, wrap="word")
        self.log.pack(fill="x", padx=14, pady=(0, 12))
        self._log("Dale a Trackear. Luego pasa el ratón por cada objeto y cada "
                  "habilidad; la checklist se va marcando sola.")

    def _cfg(self):
        try:
            return json.loads(CONFIG.read_text())
        except Exception:
            return {}

    def _construir_checklist(self):
        for w in self.lista.winfo_children():
            w.destroy()
        self.filas = {}
        tk.Label(self.lista, text="EQUIPO", bg="#141210", fg="#c14a4a",
                 font=("Georgia", 10, "bold"), anchor="w").pack(fill="x", pady=(0, 4))
        for h in HUECOS:
            self.filas[h] = self._fila(h)
        tk.Label(self.lista, text="HABILIDADES", bg="#141210", fg="#c14a4a",
                 font=("Georgia", 10, "bold"), anchor="w").pack(fill="x", pady=(12, 4))
        for i in range(N_HABILIDADES):
            self.filas[f"hab{i}"] = self._fila(f"Habilidad {i + 1}")

    def _fila(self, etiqueta):
        f = tk.Frame(self.lista, bg="#141210")
        f.pack(fill="x", pady=1)
        marca = tk.Label(f, text="○", bg="#141210", fg="#3a352f", font=("Segoe UI", 12), width=2)
        marca.pack(side="left")
        nom = tk.Label(f, text=etiqueta, bg="#141210", fg="#6b625a",
                       font=("Segoe UI", 10), anchor="w", width=14)
        nom.pack(side="left")
        val = tk.Label(f, text="—", bg="#141210", fg="#3a352f",
                       font=("Segoe UI", 10), anchor="w")
        val.pack(side="left", fill="x", expand=True)
        fila = {"marca": marca, "nombre": nom, "valor": val, "etiqueta": etiqueta}
        # clic derecho sobre una fila = borrarla, por si el OCR mete algo raro
        for w in (f, marca, nom, val):
            w.bind("<Button-3>", lambda e, et=etiqueta: self._borrar_fila(et))
        return fila

    def _borrar_fila(self, etiqueta):
        for clave, fila in self.filas.items():
            if fila["etiqueta"] != etiqueta:
                continue
            fila["marca"].config(text="○", fg="#3a352f")
            fila["nombre"].config(fg="#6b625a")
            fila["valor"].config(text="—", fg="#3a352f")
            if self.perfil:
                self.perfil.objetos.pop(clave, None)
                if clave.startswith("hab"):
                    i = int(clave[3:])
                    claves = list(self.perfil.habilidades)
                    if i < len(claves):
                        self.perfil.habilidades.pop(claves[i], None)
            self._log(f"  ✗ borrado: {etiqueta}")
            return

    def _log(self, s):
        self.log.insert("end", s + "\n")
        self.log.see("end")

    # ---------------------------------------------------------------- control
    def alternar(self):
        if self.grabando:
            self.parar("parado a mano")
            return
        if simpledialog is None:
            return
        d = Dialogo(self)
        self.wait_window(d)
        if not d.resultado:
            return
        tipo, nombre = d.resultado
        self.perfil = Perfil(nombre, tipo)
        self.vistos_txt = set()
        self.ciclos = 0
        self.sin_nada = 0
        self._construir_checklist()
        self.grabando = True
        self.btn.config(text="■  Parar", bg="#8a3030")
        etq = "TU personaje" if tipo == "yo" else f"RIVAL: {nombre}"
        self._log(f"\n▶ Trackeando {etq}. Pasa el ratón por cada pieza…")
        threading.Thread(target=self._bucle, daemon=True).start()

    def parar(self, motivo):
        self.grabando = False
        self.btn.config(text="▶  Trackear", bg="#c14a4a")
        self.estado.config(text=motivo)
        if self.perfil:
            ruta = self.perfil.guardar()
            self._log(f"■ {motivo}. Guardado en {ruta.name}")
            if motivo != "completo" and self.perfil.objetos:
                self._informe()

    def _bucle(self):
        fallos = 0
        while self.grabando:
            try:
                img = capturar(self.region)
                if self.region:
                    trozos = [ocr(img, guardar=True)]
                else:
                    trozos = ocr_bloques(img, guardar=True)
                fallos = 0
            except Exception as e:
                fallos += 1
                if fallos >= 3:
                    self.after(0, self._log, f"✗ No puedo capturar: {e}")
                    self.after(0, self.parar, "error de captura")
                    return
                time.sleep(1)
                continue
            reconocidos = 0
            for txt in trozos:
                if not txt or txt in self.vistos_txt:
                    continue
                self.vistos_txt.add(txt)
                r = identificar(txt)
                if r:
                    reconocidos += 1
                    self.after(0, self._visto, *r)
            # Sin esto no se distingue "no captura" de "captura pero no reconoce".
            self.ciclos += 1
            if reconocidos:
                self.sin_nada = 0
            else:
                self.sin_nada += 1
                if self.sin_nada in (8, 25, 60):
                    self.after(0, self._log,
                               f"  … {self.ciclos} lecturas, {len(trozos)} bloques en la "
                               f"última. Ninguno es un tooltip: pon el ratón ENCIMA de "
                               f"un objeto y espera 2 s.")
            time.sleep(self.INTERVALO)

    def _visto(self, clase, clave, nombre, texto):
        if not self.perfil or not self.perfil.anadir(clase, clave, nombre, texto):
            return
        if clase == "objeto":
            k = clave if clave in self.filas else next(
                (h for h in HUECOS if h.startswith("Anillo") and h in self.perfil.objetos), None)
            for h, d in self.perfil.objetos.items():
                if d["nombre"] == nombre:
                    k = h
                    break
            self._marcar(k, nombre)
        else:
            i = len(self.perfil.habilidades) - 1
            self._marcar(f"hab{i}", nombre)
        d = self.perfil.objetos.get(k) if clase == "objeto" else None
        if d and d.get("afijos") is not None:
            afijos = [{"grupo": x["grupo"], "valor": x["valor"], "mult": x["mult"],
                       "pct": x["pct"], "tipo": x["tipo"], "muerto": x["muerto"]}
                      for x in d["afijos"]]
            self._log(f"  ✓ {nombre}  —  {V.resumen_linea(afijos, d['aporte'])}")
            self._contra_referencia(k, d)
        else:
            self._log(f"  ✓ {nombre}")
        f, n = self.perfil.faltan()
        self.estado.config(text=f"faltan {len(f)} objetos · {n} habilidades")
        if self.perfil.completo():
            self._log("\n★ COMPLETO. Build entera capturada.")
            self._informe()
            self.parar("completo")

    def _contra_referencia(self, hueco, dato):
        """Si hay un perfil guardado del otro lado, compara ese hueco al vuelo."""
        otro = "rival" if self.perfil.tipo == "yo" else "yo"
        for ruta in sorted(PERFILES.glob(f"{otro}_*.json")) if PERFILES.exists() else []:
            try:
                p = json.loads(ruta.read_text(encoding="utf-8"))
            except Exception:
                continue
            ref = (p.get("objetos") or {}).get(hueco)
            if not ref or not ref.get("texto"):
                continue
            dif, tn, tv, _ = V.comparar(dato["texto"], ref["texto"], CAT)
            v, _ = V.veredicto(dif)
            self._log(f"      vs {p.get('nombre', ruta.stem)}: {v} {dif:+.0f}%")
            return

    def _marcar(self, clave, texto):
        fila = self.filas.get(clave)
        if not fila:
            return
        fila["marca"].config(text="●", fg="#4a9d68")
        fila["nombre"].config(fg="#e8e2da")
        extra = ""
        if self.perfil:
            d = self.perfil.objetos.get(clave)
            if d and d.get("aporte") is not None:
                extra = f"   +{d['aporte']:.0f}%"
        fila["valor"].config(text=(texto[:38] + extra), fg="#c9c0b4")

    def leer_ficha(self):
        """Captura la hoja de personaje y actualiza los grupos del valorador.
        Son la base de todo el cálculo: desfasados, las respuestas mienten."""
        self._log("\nLeyendo la ficha de personaje…")
        self.update()
        try:
            self.withdraw()
            time.sleep(0.25)
            img = capturar(self.region)
            self.deiconify()
            txt = ocr(img, guardar=True)
        except Exception as e:
            self.deiconify()
            self._log(f"✗ {e}")
            return
        vals = V.leer_ficha(txt)
        if not vals:
            self._log("  No he reconocido ninguna estadística. Abre la hoja de "
                      "personaje y marca la Zona sobre la lista de estadísticas.")
            return
        V.guardar_ficha(vals)
        self._log(f"  ✓ {len(vals)} estadísticas actualizadas:")
        for k, v in sorted(vals.items()):
            self._log(f"      {k}: {v:g}")

    def _informe(self):
        if not self.perfil:
            return
        p = {"objetos": self.perfil.objetos}
        self._log("\n" + "─" * 46)
        for l in V.informe(p).splitlines():
            self._log(l)
        self._log("─" * 46)

    # ---------------------------------------------------------------- zona
    def elegir_region(self):
        self.withdraw()
        time.sleep(0.25)
        sel = tk.Toplevel()
        sel.attributes("-fullscreen", True, "-alpha", 0.25)
        sel.configure(bg="black")
        cv = tk.Canvas(sel, cursor="cross", bg="black", highlightthickness=0)
        cv.pack(fill="both", expand=True)
        est = {}

        def down(e):
            est["x"], est["y"] = e.x, e.y
            est["r"] = cv.create_rectangle(e.x, e.y, e.x, e.y, outline="#c14a4a", width=2)

        def move(e):
            if "r" in est:
                cv.coords(est["r"], est["x"], est["y"], e.x, e.y)

        def up(e):
            self.region = [min(est["x"], e.x), min(est["y"], e.y),
                           abs(e.x - est["x"]), abs(e.y - est["y"])]
            CONFIG.write_text(json.dumps({"region": self.region}))
            sel.destroy()
            self.deiconify()
            self._log(f"Zona fijada: {self.region[2]}×{self.region[3]} px")

        cv.bind("<ButtonPress-1>", down)
        cv.bind("<B1-Motion>", move)
        cv.bind("<ButtonRelease-1>", up)


class Dialogo(tk.Toplevel if tk else object):
    def __init__(self, padre):
        super().__init__(padre)
        self.title("¿De quién?")
        self.configure(bg="#1c1917")
        self.resultado = None
        self.transient(padre)
        self.grab_set()
        tk.Label(self, text="¿De quién es esta build?", bg="#1c1917", fg="#e8e2da",
                 font=("Segoe UI", 11)).pack(padx=24, pady=(18, 12))
        f = tk.Frame(self, bg="#1c1917")
        f.pack(padx=24)
        tk.Button(f, text="Soy yo", width=12, bg="#c14a4a", fg="white", relief="flat",
                  pady=6, command=self._yo).pack(side="left", padx=5)
        tk.Button(f, text="Un rival", width=12, bg="#232019", fg="#e8e2da", relief="flat",
                  pady=6, command=self._rival).pack(side="left", padx=5)
        self.entrada = tk.Entry(self, bg="#141210", fg="#e8e2da", relief="flat",
                                insertbackground="#e8e2da", justify="center")
        self.entrada.pack(fill="x", padx=24, pady=(14, 20))
        self.entrada.insert(0, "")
        tk.Label(self, text="(nombre del rival, si es un rival)", bg="#1c1917",
                 fg="#6b625a", font=("Segoe UI", 8)).pack(pady=(0, 14))

    def _yo(self):
        self.resultado = ("yo", "mi build")
        self.destroy()

    def _rival(self):
        n = self.entrada.get().strip() or "rival"
        self.resultado = ("rival", n)
        self.destroy()


# ---------------------------------------------------------------- pruebas
def autotest():
    casos = [
        ("YELMO EXCEPCIONAL DEL YUNQUE DE GLYNN\nYelmo legendario ancestral\n900 de poder de objeto", "Casco"),
        ("MANTO DE LOS GRISES\nPeto único ancestral\n900 de poder", "Peto"),
        ("PUÑOS DEL DESTINO\nGuantes únicos ancestrales\n900", "Guantes"),
        ("VOLUNTAD DE TIBAULT\nPantalones únicos ancestrales\n900", "Pantalones"),
        ("BORCEGUÍ DE SKOVOS DE INTERDICCIÓN\nBotas legendarias ancestrales\n900", "Botas"),
        ("EFIGIE PÚTRIDA APLASTANTE\nMangual legendario ancestral\n900", "Arma"),
        ("HERALDO DE ZAKARUM\nEscudo único ancestral\n900", "Escudo"),
        ("ÍDOLO SEDIENTO DE SANGRE\nAmuleto único ancestral\n900", "Amuleto"),
        ("CÍRCULO DE ECOS DE ESCRITURA DE LAPA\nAnillo legendario ancestral\n900", "Anillo"),
        ("LÍMITE LÍMBICO DE FUERZA REDIRIGIDA\nAnillo legendario ancestral\n900", "Anillo"),
        ("TALISMÁN DE LOCRAN\nAmuleto único ancestral\n900", "Amuleto"),
    ]
    ok = 0
    for texto, esperado in casos:
        r = identificar(texto)
        got = r[1] if r else None
        marca = "ok " if got == esperado else "MAL"
        if got == esperado:
            ok += 1
        print(f"  {marca}  {texto.splitlines()[0][:38]:<40} -> {got}")
    print(f"\n  objetos: {ok}/{len(casos)}")

    # Tooltips REALES de habilidad, sacados de capturas del juego
    hab = [
        "Punición\nRANGO 1/15\nJusticia Discípulo\n"
        "Tiempo de reutilización: 0,5 s\nProbabilidad de golpe de suerte: 26%\nMODIFICADORES",
        "Carga con escudo\nRANGO 15/15\nTiempo de reutilización: 8 s\nCanalizada",
        "Aura de fanatismo\nRANGO 12/15\nCoste: 0 de Fe\nMODIFICADORES",
        "Fortaleza\nRANGO 5/15\nTiempo de reutilización: 45 s\nDefinitiva",
    ]
    ok2 = 0
    for texto in hab:
        r = identificar(texto)
        bien = bool(r) and r[0] == "habilidad"
        ok2 += bien
        print(f"  {'ok ' if bien else 'MAL'}  {texto.splitlines()[0]:<40} -> "
              f"{r[2] if r else None}")
    print(f"  habilidades: {ok2}/{len(hab)}")

    p = Perfil("prueba", "yo")
    p.anadir("objeto", "Anillo", "ANILLO A", "x")
    p.anadir("objeto", "Anillo", "ANILLO B", "x")
    p.anadir("objeto", "Anillo", "ANILLO C", "x")
    print(f"\n  dos anillos como máximo: {list(p.objetos)} "
          f"{'ok' if len(p.objetos) == 2 else 'MAL'}")


def simulacion():
    """Sesión completa simulada con tooltips reales del jugador."""
    TOOLTIPS = {
        "Casco": """YELMO EXCEPCIONAL DEL YUNQUE DE GLYNN
Yelmo legendario ancestral
+182 de fuerza
+1.728 de vida máxima [1.226 - 1.450]
+1.635 de espinas [1.221 - 1.526]
+6 acumulaciones máximas de Resolución""",
        "Guantes": """PUÑOS DEL DESTINO
Guantes únicos ancestrales
+243 de fuerza +[150 - 180]
+2.970 de vida máxima [1.831 - 2.200]
Multiplicador de daño por vulnerabilidad x52% [16 - 28]%
Multiplicador de daño de Físico x32% [14 - 24]%
+64,0% de daño a enemigos cercanos""",
        "Escudo": """HERALDO DE ZAKARUM
Escudo único ancestral
+225 de fuerza +[150 - 180]
+790 de vida por golpe [526 - 632]
+1.908 de espinas [1.221 - 1.526]
18,8% de reducción de daño [11,0 - 15,0]%""",
        "Anillo": """CÍRCULO DE ECOS DE ESCRITURA DE LAPA
Anillo legendario ancestral
+6,4% de probabilidad de golpe crítico [3,5 - 5,0]%
Multiplicador de daño de golpe crítico x27% [13 - 25]%
+336 de vida por golpe [263 - 316]""",
    }
    p = Perfil("simulacion", "yo")
    print("  --- sesión simulada ---")
    for _, txt in TOOLTIPS.items():
        r = identificar(txt)
        if not r:
            print(f"    MAL  no identificado: {txt.splitlines()[0]}")
            continue
        clase, clave, nombre, texto = r
        if p.anadir(clase, clave, nombre, texto):
            hueco = next((k for k, v in p.objetos.items() if v["nombre"] == nombre), clave)
            d = p.objetos[hueco]
            print(f"    ok   {hueco:<11} {nombre[:30]:<32} +{d['aporte']:.0f}%")
    f, n = p.faltan()
    print(f"\n    capturado: {len(p.objetos)} objetos · faltan {len(f)}: {', '.join(f)}")
    print(f"    habilidades: faltan {n}")
    print(f"    completo: {p.completo()}  (correcto: False, faltan piezas)")
    peor = TOOLTIPS["Guantes"].replace("x52%", "x20%").replace("+64,0%", "+10,0%")
    dif, tn, tv, _ = V.comparar(peor, TOOLTIPS["Guantes"], CAT)
    v, _ = V.veredicto(dif)
    print(f"\n    guantes recortados vs los tuyos: {v} {dif:+.1f}%")


if __name__ == "__main__":
    if "--test" in sys.argv:
        autotest()
        print()
        simulacion()
    else:
        App().mainloop()
