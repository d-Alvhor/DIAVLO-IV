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

from catalogo import Catalogo

CAT = Catalogo()   # 432 tipos, 891 afijos, 524 aspectos — de Diablo4Companion (MIT)

# ---------------------------------------------------------------- qué hay que ver
# Ya no adivinamos con palabras clave: la línea de tipo del tooltip es literalmente
# una entrada del catálogo, así que emparejamos contra los 432 nombres reales.
# Eso corrige de paso los errores del OCR ("Yelrno" -> Casco).
HUECOS = ["Casco", "Peto", "Guantes", "Pantalones", "Botas",
          "Arma", "Escudo", "Amuleto", "Anillo 1", "Anillo 2"]

# Habilidades del Paladín que pueden ir en la barra (6 huecos).
HABILIDADES = [
    "carga con escudo", "shield charge", "choque", "clash", "fortaleza", "fortress",
    "condena", "condemn", "aura de desafío", "aura de desafio", "defiance aura",
    "aura de fanatismo", "fanaticism aura", "aegis", "égida", "egida",
    "golpe bendito", "blessed hammer", "martillo bendito", "juicio", "judgement",
    "zelote", "zeal", "castigo", "punish", "escudo bendito", "blessed shield",
    "avance", "advance", "arbitro", "árbitro", "arbiter", "blandir", "brandish",
]
N_HABILIDADES = 6

# Marcadores de que un tooltip es de habilidad y no de objeto.
MARCAS_HABILIDAD = ["enfriamiento", "coste:", "de fe", "genera", "habilidad de",
                    "canalizada", "definitiva", "cuerpo a cuerpo"]


# ---------------------------------------------------------------- texto
def norm(s):
    s = unicodedata.normalize("NFD", str(s))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", s).strip().lower()


def identificar(texto):
    """Del texto de un tooltip saca (clase, hueco_o_nombre, nombre, texto).
    clase: 'objeto' | 'habilidad' | None."""
    lineas = [l.strip() for l in texto.splitlines() if l.strip()]
    if len(lineas) < 2:
        return None
    n = norm(texto)

    # ¿objeto? La línea de tipo suele ser la 2ª. Contra el catálogo, no a ojo.
    for linea in lineas[:4]:
        hueco = CAT.hueco(linea)
        if hueco:                       # None = tipo conocido pero no es equipo
            return ("objeto", hueco, lineas[0].strip(), texto)

    # ¿habilidad? nombre conocido + algún marcador de tooltip de habilidad
    for h in HABILIDADES:
        if h in n and any(m in n for m in MARCAS_HABILIDAD):
            return ("habilidad", h, lineas[0].strip(), texto)
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


def _lineas(res):
    if isinstance(res, dict):
        ls = res.get("lines") or []
        return [l.get("text", "") if isinstance(l, dict) else getattr(l, "text", "") for l in ls]
    ls = getattr(res, "lines", None)
    if ls:
        return [getattr(l, "text", "") for l in ls]
    return [getattr(res, "text", "") or ""]


def ocr(img):
    import winocr
    res = winocr.recognize_pil_sync(img, "es-ES")
    return "\n".join(x for x in _lineas(res) if x.strip())


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
            self.objetos[clave] = {"nombre": nombre, "texto": texto}
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
        self.ultimo = ""

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
        return {"marca": marca, "nombre": nom, "valor": val, "etiqueta": etiqueta}

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

    def _bucle(self):
        fallos = 0
        while self.grabando:
            try:
                txt = ocr(capturar(self.region))
                fallos = 0
            except Exception as e:
                fallos += 1
                if fallos >= 3:
                    self.after(0, self._log, f"✗ No puedo capturar: {e}")
                    self.after(0, self.parar, "error de captura")
                    return
                time.sleep(1)
                continue
            if txt and txt != self.ultimo:
                self.ultimo = txt
                r = identificar(txt)
                if r:
                    self.after(0, self._visto, *r)
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
        self._log(f"  ✓ {nombre}")
        f, n = self.perfil.faltan()
        self.estado.config(text=f"faltan {len(f)} objetos · {n} habilidades")
        if self.perfil.completo():
            self._log("\n★ COMPLETO. Build entera capturada.")
            self.parar("completo")

    def _marcar(self, clave, texto):
        fila = self.filas.get(clave)
        if not fila:
            return
        fila["marca"].config(text="●", fg="#4a9d68")
        fila["nombre"].config(fg="#e8e2da")
        fila["valor"].config(text=texto[:46], fg="#c9c0b4")

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

    hab = [("CARGA CON ESCUDO\nHabilidad de Juggernaut\nCoste: 20 de Fe\nCanalizada", "carga con escudo"),
           ("FORTALEZA\nDefinitiva\nEnfriamiento: 45 s", "fortaleza"),
           ("AURA DE FANATISMO\nAura\nCoste: 0 de Fe", "aura de fanatismo")]
    ok2 = 0
    for texto, esperado in hab:
        r = identificar(texto)
        if r and r[0] == "habilidad" and r[1] == esperado:
            ok2 += 1
            print(f"  ok   {texto.splitlines()[0]:<40} -> habilidad")
        else:
            print(f"  MAL  {texto.splitlines()[0]:<40} -> {r}")
    print(f"  habilidades: {ok2}/{len(hab)}")

    p = Perfil("prueba", "yo")
    p.anadir("objeto", "Anillo", "ANILLO A", "x")
    p.anadir("objeto", "Anillo", "ANILLO B", "x")
    p.anadir("objeto", "Anillo", "ANILLO C", "x")
    print(f"\n  dos anillos como máximo: {list(p.objetos)} "
          f"{'ok' if len(p.objetos) == 2 else 'MAL'}")


if __name__ == "__main__":
    if "--test" in sys.argv:
        autotest()
    else:
        App().mainloop()
