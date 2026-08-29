#!/usr/bin/env python3
"""
Escáner de objetos de Diablo IV — para Windows.

Captura la pantalla, lee el tooltip y te dice si el objeto gana al que llevas.

NO es un overlay: no dibuja nada sobre el juego, no lee su memoria, no automatiza
nada. Hace una captura de pantalla (como la tecla Impr Pant) y la lee. La ventana
de resultados es una ventana normal, aparte.

Instalación (una vez, en el PC de Windows):
    pip install winocr mss pillow

Uso:
    python escaner.py
    -> ventana con el resultado
    -> pon el ratón sobre el objeto en el juego y pulsa F8
    -> F9 para fijar la zona de captura (una vez, si quieres afinar)
"""

import re
import sys
import json
import time
import unicodedata
import threading
from pathlib import Path

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:  # sin Tk (p. ej. macOS de desarrollo): solo --test
    tk = ttk = None

CONFIG = Path(__file__).with_name("config.json")

# ---------------------------------------------------------------- tu personaje
# Grupos aditivos actuales, de la ficha de personaje.
# Actualízalos cuando cambies equipo: son la base de todo el cálculo.
GRUPOS = {
    "daño de golpe crítico": 4047.5,
    "daño por vulnerabilidad": 321.6,
    "todo el daño": 176.5,
    "daño físico": 266.9,
    "daño contra enemigos de élite": 159.0,
    "daño a enemigos cercanos": 75.5,
    "probabilidad de golpe crítico": 49.4,
    "espinas": 8035,
    "vida máxima": 13100,
    "vida por golpe": 1495,
    "armadura": 43943,
    "fuerza": 4896,
    "reducción de tiempo de reutilización": 23.4,
    "resolución máxima": 19,
}

# Grupos que son cantidades planas, no porcentajes acumulados.
PLANOS = {"espinas", "vida máxima", "vida por golpe", "armadura", "fuerza", "resolución máxima"}

# Lo que llevas puesto, por hueco: (grupo, valor, multiplicativo?)
EQUIPADO = {
    "Casco": [("fuerza", 182, 0), ("vida máxima", 1728, 0), ("espinas", 1635, 0),
              ("reducción de tiempo de reutilización", 7.5, 0), ("resolución máxima", 6, 0)],
    "Peto": [("fuerza", 157, 0), ("vida máxima", 1885, 0), ("espinas", 1984, 0),
             ("resolución máxima", 5, 0)],
    "Guantes": [("fuerza", 243, 0), ("vida máxima", 2970, 0), ("daño por vulnerabilidad", 52, 1),
                ("daño físico", 32, 1), ("daño a enemigos cercanos", 64, 0),
                ("aleatorio 1%-390%", 95.5, 1)],
    "Pantalones": [("fuerza", 151, 0), ("vida máxima", 1813, 0), ("espinas", 1908, 0),
                   ("resolución máxima", 6, 0)],
    "Botas": [("fuerza", 182, 0), ("vida máxima", 1629, 0), ("armadura", 1837, 0)],
    "Arma": [("fuerza", 223, 0), ("vida por golpe", 369, 0), ("daño de golpe crítico", 30, 1),
             ("daño físico", 13, 1), ("probabilidad de golpe crítico", 7.5, 0)],
    "Escudo": [("fuerza", 225, 0), ("vida por golpe", 790, 0), ("espinas", 1908, 0),
               ("probabilidad de golpe crítico", 8.8, 0)],
    "Amuleto": [("fuerza", 225, 0), ("todo el daño", 25, 1), ("probabilidad de golpe crítico", 10.6, 0),
                ("daño de golpe crítico", 88, 1), ("daño de golpe crítico", 63, 0)],
    "Anillo 1": [("probabilidad de golpe crítico", 6.4, 0), ("daño de golpe crítico", 27, 1),
                 ("daño por vulnerabilidad", 23, 1), ("daño físico", 13, 1), ("vida por golpe", 336, 0)],
    "Anillo 2": [("daño de golpe crítico", 28, 1), ("daño por vulnerabilidad", 23, 1),
                 ("daño físico", 11, 1), ("daño por vulnerabilidad", 50, 0)],
}

# Afijos que no aportan nada a Shield Charge (espinas físicas directas).
MUERTOS = {
    "daño en el tiempo": "tu daño de espinas es directo, no periódico",
    "daño de frío": "eres físico",
    "daño de fuego": "eres físico",
    "daño sagrado": "eres físico",
    "daño de veneno": "eres físico",
    "daño de sombra": "eres físico",
    "daño con frío": "eres físico",
    "daño con fuego": "eres físico",
    "daño a enemigos lejanos": "eres cuerpo a cuerpo, siempre estás pegado",
}


# ---------------------------------------------------------------- parseo
def norm(s):
    s = unicodedata.normalize("NFD", str(s))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", s).strip().lower()


def num(s):
    """OCR real trae ruido: puntos sueltos, comas huerfanas, cifras partidas.
    Devuelve None en vez de reventar; quien llama descarta la linea."""
    t = str(s).strip()
    if not re.search(r"\d", t):
        return None
    t = t.rstrip(".,")                 # "2.970." -> "2.970"
    if "," in t:                       # coma decimal espanola
        ent, _, dec = t.rpartition(",")
        t = ent.replace(".", "") + "." + dec
    else:
        t = t.replace(".", "")         # punto de millares
    try:
        return float(t)
    except ValueError:
        return None


def limpiar(s):
    s = norm(s)
    s = re.sub(r"^de\s+", "", s)
    s = re.sub(r"^(dano|daño) de ", r"\1 ", s)
    s = re.sub(r"\s*[\[(].*$", "", s)
    return s.strip(" .%")


def parsear(texto):
    """Tooltip crudo -> lista de afijos {grupo, valor, mult}."""
    out = []
    for linea in texto.splitlines():
        linea = linea.strip()
        if not linea:
            continue

        m = re.search(r"multiplicador de (.+?)\s*x\s*(\d[\d.,]*)\s*%", linea, re.I)
        if m:
            v, g = num(m.group(2)), limpiar(m.group(1))
            if v is not None and len(g) > 2:
                out.append({"grupo": g, "valor": v, "mult": True, "crudo": linea})
            continue

        # "Tus ataques infligen del 1% al 390%" -> se valora por su media
        m = re.search(r"del\s*1\s*%\s*al\s*(\d[\d.,]*)\s*%", linea, re.I)
        if m:
            mx = num(m.group(1))
            if mx is not None:
                out.append({"grupo": f"aleatorio 1%-{mx:g}%", "valor": (1 + mx) / 2 - 100,
                            "mult": True, "nota": f"media {(1 + mx) / 2:.1f}%", "crudo": linea})
            continue

        m = re.match(r"^\+?\s*(\d[\d.,]*)\s*%\s*(?:de\s+)?(.+?)(?:\s*\[|$)", linea, re.I)
        if m and not re.match(r"^[\d.,\s]+$", m.group(2)):
            v, g = num(m.group(1)), limpiar(m.group(2))
            if v is not None and len(g) > 2:
                out.append({"grupo": g, "valor": v, "mult": False, "crudo": linea})
            continue

        m = re.match(r"^\+?\s*(\d[\d.,]*)\s+(?:de\s+)?(.+?)(?:\s*\+?\[|$)", linea, re.I)
        if m:
            v, g = num(m.group(1)), limpiar(m.group(2))
            if v is not None and len(g) > 2:
                out.append({"grupo": g, "valor": v, "mult": False, "crudo": linea})
    return out


def casar(grupo):
    g = norm(grupo)
    for k in GRUPOS:
        if norm(k) == g:
            return k
    for k in GRUPOS:
        if g in norm(k) or norm(k) in g:
            return k
    return None


def muerto(grupo):
    g = norm(grupo)
    for pat, motivo in MUERTOS.items():
        if norm(pat) in g:
            return motivo
    return None


def valorar(a):
    """Aporte real del afijo, en % sobre el total. La regla que gobierna todo:
    lo que SUMA se diluye en el grupo que ya tienes; lo que MULTIPLICA no."""
    mu = muerto(a["grupo"])
    if mu:
        return {**a, "pct": 0.0, "muerto": mu, "tipo": "muerto"}
    if a["mult"]:
        return {**a, "grupo_real": casar(a["grupo"]) or a["grupo"], "pct": a["valor"], "tipo": "multiplica"}
    k = casar(a["grupo"])
    if not k:
        return {**a, "pct": None, "tipo": "desconocido"}
    base = GRUPOS[k]
    if k in PLANOS:
        pct = (a["valor"] / base) * 100 if base else 0.0
        tipo = "suma (plano)"
    else:
        pct = (a["valor"] / (100 + base)) * 100
        tipo = "suma"
    return {**a, "grupo_real": k, "base": base, "pct": pct, "tipo": tipo}


def aporte(afijos):
    g = 1.0
    for a in afijos:
        if a.get("pct"):
            g *= 1 + a["pct"] / 100
    return (g - 1) * 100


def analizar(texto, hueco=None):
    afijos = [valorar(a) for a in parsear(texto)]
    total = aporte(afijos)
    comp = None
    if hueco and hueco in EQUIPADO:
        eq = [valorar({"grupo": gr, "valor": v, "mult": bool(m)}) for gr, v, m in EQUIPADO[hueco]]
        base = aporte(eq)
        comp = {"hueco": hueco, "equipado": base,
                "dif": ((1 + total / 100) / (1 + base / 100) - 1) * 100}
    return afijos, total, comp


# ---------------------------------------------------------------- captura + OCR
def capturar(region=None):
    import mss
    from PIL import Image
    with (mss.MSS() if hasattr(mss, 'MSS') else mss.mss()) as sct:
        mon = region or sct.monitors[1]
        if isinstance(mon, dict):
            shot = sct.grab(mon)
        else:
            shot = sct.grab({"left": mon[0], "top": mon[1], "width": mon[2], "height": mon[3]})
        return Image.frombytes("RGB", shot.size, shot.bgra, "raw", "BGRX")


def ocr(img):
    """OCR con el motor nativo de Windows. Sin Tesseract, sin binarios."""
    import winocr
    from PIL import ImageOps

    def _lineas(res):
        """winocr devuelve un objeto/dict con 'lines'; cada una trae su 'text'.
        Hay que extraerlas: str(res) vuelca el diccionario entero y duplica afijos."""
        if isinstance(res, dict):
            ls = res.get("lines") or []
            return [l.get("text", "") if isinstance(l, dict) else getattr(l, "text", "") for l in ls]
        ls = getattr(res, "lines", None)
        if ls:
            return [getattr(l, "text", "") for l in ls]
        return [getattr(res, "text", "") or ""]

    txt = "\n".join(x for x in _lineas(winocr.recognize_pil_sync(img, "es-ES")) if x.strip())
    if len(txt.strip()) < 20:  # tooltip claro sobre oscuro: a veces invertir ayuda
        alt = "\n".join(x for x in _lineas(
            winocr.recognize_pil_sync(ImageOps.invert(img.convert("RGB")), "es-ES")) if x.strip())
        if len(alt) > len(txt):
            txt = alt
    return txt


# ---------------------------------------------------------------- atajos globales
# RegisterHotKey es la via oficial de Windows: le pides al sistema que te avise
# con una combinacion concreta. NO instala un hook de teclado, no lee otras teclas,
# y no interactua con ningun proceso. Es lo que usa cualquier app normal.
MOD_ALT, MOD_CONTROL, MOD_SHIFT, MOD_NOREPEAT, WM_HOTKEY = 0x0001, 0x0002, 0x0004, 0x4000, 0x0312
VK_D, VK_Z, VK_F8, VK_F9 = 0x44, 0x5A, 0x77, 0x78


# Combinaciones candidatas por accion, en orden de preferencia. Se usa la primera
# que Windows acepte: asi no hay que configurar nada si alguna esta ocupada.
CANDIDATAS = {
    "escanear": [(MOD_CONTROL | MOD_ALT, VK_D, "Ctrl+Alt+D"),
                 (MOD_CONTROL | MOD_SHIFT, VK_D, "Ctrl+Mayus+D"),
                 (MOD_ALT | MOD_SHIFT, VK_D, "Alt+Mayus+D"),
                 (MOD_CONTROL | MOD_ALT, VK_F8, "Ctrl+Alt+F8")],
    "zona": [(MOD_CONTROL | MOD_ALT, VK_Z, "Ctrl+Alt+Z"),
             (MOD_CONTROL | MOD_SHIFT, VK_Z, "Ctrl+Mayus+Z"),
             (MOD_ALT | MOD_SHIFT, VK_Z, "Alt+Mayus+Z"),
             (MOD_CONTROL | MOD_ALT, VK_F9, "Ctrl+Alt+F9")],
}


def atajos_globales(acciones, aviso):
    """acciones = {'escanear': cb, 'zona': cb}. Bloquea: llamar en un hilo aparte.
    Prueba las combinaciones candidatas y se queda con la primera libre."""
    import ctypes
    from ctypes import wintypes
    u32 = ctypes.windll.user32
    mapa, activos, idx = {}, {}, 1
    for accion, cb in acciones.items():
        for mods, vk, nombre in CANDIDATAS.get(accion, []):
            if u32.RegisterHotKey(None, idx, mods | MOD_NOREPEAT, vk):
                mapa[idx] = cb
                activos[accion] = nombre
                idx += 1
                break
        else:
            activos[accion] = None
    aviso(activos)
    if not mapa:
        return
    msg = wintypes.MSG()
    while u32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
        if msg.message == WM_HOTKEY and msg.wParam in mapa:
            mapa[msg.wParam]()
        u32.TranslateMessage(ctypes.byref(msg))
        u32.DispatchMessageW(ctypes.byref(msg))


# ---------------------------------------------------------------- ventana
class App(tk.Tk if tk else object):
    def __init__(self):
        super().__init__()
        self.title("Escáner — Diablo IV")
        self.geometry("560x620+40+40")
        self.configure(bg="#141210")
        self.attributes("-topmost", True)
        self.region = self._cargar_region()

        cab = tk.Frame(self, bg="#1c1917")
        cab.pack(fill="x")
        tk.Label(cab, text="ESCÁNER", bg="#1c1917", fg="#c14a4a",
                 font=("Georgia", 12, "bold")).pack(side="left", padx=10, pady=8)
        self.hueco = ttk.Combobox(cab, values=["(sin comparar)"] + list(EQUIPADO), state="readonly", width=16)
        self.hueco.current(0)
        self.hueco.pack(side="left", padx=6)
        tk.Button(cab, text="Escanear (Ctrl+Alt+D)", command=self.escanear,
                  bg="#c14a4a", fg="white", relief="flat", padx=10).pack(side="left", padx=6)
        tk.Button(cab, text="Zona (Ctrl+Alt+Z)", command=self.elegir_region,
                  bg="#232019", fg="#e8e2da", relief="flat", padx=8).pack(side="left")

        self.txt = tk.Text(self, bg="#141210", fg="#e8e2da", insertbackground="#e8e2da",
                           font=("Consolas", 10), relief="flat", padx=12, pady=10, wrap="word")
        self.txt.pack(fill="both", expand=True)
        self.txt.tag_config("t", foreground="#c14a4a", font=("Georgia", 14, "bold"))
        self.txt.tag_config("ok", foreground="#4a9d68", font=("Georgia", 14, "bold"))
        self.txt.tag_config("no", foreground="#c14a4a", font=("Georgia", 14, "bold"))
        self.txt.tag_config("mut", foreground="#9a9088")
        self.txt.tag_config("az", foreground="#7aa8cc")
        self.txt.tag_config("am", foreground="#d0a63c")

        self._msg("CON EL JUEGO DELANTE:\n"
                  "   Ctrl+Alt+D   escanear\n"
                  "   Ctrl+Alt+Z   marcar la zona del tooltip\n\n"
                  "Con esta ventana enfocada valen también F8 y F9.\n\n"
                  "Marca la zona una vez con Ctrl+Alt+Z: leer solo el recuadro del "
                  "tooltip en vez de la pantalla entera es mucho más rápido y preciso.")
        # con la ventana enfocada
        self.bind_all("<F8>", lambda e: self.escanear())
        self.bind_all("<F9>", lambda e: self.elegir_region())
        # y con el JUEGO enfocado: atajos globales del sistema
        self._arrancar_atajos()

    def _arrancar_atajos(self):
        if sys.platform != "win32":
            return
        acciones = {"escanear": lambda: self.after(0, self.escanear),
                    "zona": lambda: self.after(0, self.elegir_region)}
        threading.Thread(target=atajos_globales,
                         args=(acciones, lambda a: self.after(0, self._atajos_listos, a)),
                         daemon=True).start()

    def _atajos_listos(self, activos):
        esc, zon = activos.get("escanear"), activos.get("zona")
        if esc and zon:
            txt = (f"CON EL JUEGO DELANTE:\n"
                   f"   {esc}   escanear\n"
                   f"   {zon}   marcar la zona del tooltip\n\n"
                   f"Con esta ventana enfocada valen también F8 y F9.\n\n"
                   f"Marca la zona una vez: leer solo el recuadro del tooltip en vez "
                   f"de la pantalla entera es mucho más rápido y preciso.")
        else:
            txt = ("⚠ Windows no me ha dejado registrar los atajos globales.\n\n"
                   "Todas las combinaciones que probé están ocupadas por otra app.\n"
                   "Puedes seguir usando los botones de arriba, o F8/F9 con esta "
                   "ventana enfocada.\n\n"
                   "Para añadir otra combinación, edita CANDIDATAS en escaner.py.")
        self._msg(txt)

    def _cargar_region(self):
        if CONFIG.exists():
            try:
                return json.loads(CONFIG.read_text()).get("region")
            except Exception:
                pass
        return None

    def _msg(self, s, tag="mut"):
        self.txt.delete("1.0", "end")
        self.txt.insert("end", s, tag)

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
            x1, y1 = min(est["x"], e.x), min(est["y"], e.y)
            self.region = [x1, y1, abs(e.x - est["x"]), abs(e.y - est["y"])]
            CONFIG.write_text(json.dumps({"region": self.region}))
            sel.destroy()
            self.deiconify()
            self._msg(f"Zona fijada: {self.region[2]}×{self.region[3]} px.\nAhora pulsa F8 con el tooltip a la vista.")

        cv.bind("<ButtonPress-1>", down)
        cv.bind("<B1-Motion>", move)
        cv.bind("<ButtonRelease-1>", up)

    def escanear(self):
        self._msg("Leyendo…")
        self.update()
        threading.Thread(target=self._trabajo, daemon=True).start()

    def _trabajo(self):
        try:
            self.withdraw()
            time.sleep(0.2)
            img = capturar(self.region)
            self.deiconify()
            texto = ocr(img)
        except ImportError as e:
            self.deiconify()
            self.after(0, self._msg, f"Falta una librería: {e}\n\nEn el PC:\n  pip install winocr mss pillow")
            return
        except Exception as e:
            self.deiconify()
            self.after(0, self._msg, f"Error al capturar/leer:\n{e}")
            return
        hueco = self.hueco.get()
        hueco = hueco if hueco in EQUIPADO else None
        self.after(0, self._pintar, texto, hueco)

    def _pintar(self, texto, hueco):
        try:
            self._pintar_real(texto, hueco)
        except Exception:
            import traceback
            self.txt.delete("1.0", "end")
            self.txt.insert("end", "Fallo al analizar (no pasa nada, sigue funcionando)\n\n", "no")
            self.txt.insert("end", traceback.format_exc(), "mut")
            self.txt.insert("end", "\n--- texto leido ---\n" + (texto or "(vacio)")[:800], "mut")

    def _pintar_real(self, texto, hueco):
        afijos, total, comp = analizar(texto, hueco)
        t = self.txt
        t.delete("1.0", "end")

        if not afijos:
            t.insert("end", "No he leído ningún afijo.\n\n", "no")
            t.insert("end", "Prueba a fijar la zona con F9 sobre el tooltip.\n\nTexto crudo leído:\n", "mut")
            t.insert("end", texto[:900] or "(vacío)", "mut")
            return

        if comp:
            d = comp["dif"]
            tag = "ok" if d > 3 else "no" if d < -3 else "am"
            verbo = "GANA a tu" if d > 3 else "PIERDE contra tu" if d < -3 else "EMPATA con tu"
            t.insert("end", f"{verbo} {comp['hueco']}\n", tag)
            t.insert("end", f"{d:+.1f}% frente a lo que llevas puesto\n", tag)
            t.insert("end", f"nuevo +{total:.1f}%  ·  equipado +{comp['equipado']:.1f}%\n\n", "mut")
        else:
            t.insert("end", f"Aporte de la pieza: +{total:.1f}%\n\n", "t")

        for a in sorted(afijos, key=lambda x: -(x.get("pct") or 0)):
            nom = a.get("grupo_real") or a["grupo"]
            pct = "—" if a.get("pct") is None else f"{a['pct']:+.1f}%"
            t.insert("end", f"  {pct:>9}  ", "az" if a["mult"] else "am")
            t.insert("end", f"{nom}\n")
            det = a.get("muerto") or a.get("nota") or (
                f"tu grupo ya está en {a['base']:g}" if "base" in a else "grupo no mapeado")
            t.insert("end", f"             {a['tipo']} · {det}\n", "mut")

        mu = [a for a in afijos if a.get("muerto")]
        if mu:
            t.insert("end", f"\n⚠ {len(mu)} afijo(s) no te sirven de nada: "
                            f"{', '.join(a['grupo'] for a in mu)}\n", "no")
        mejor = max((a for a in afijos if (a.get("pct") or 0) > 0),
                    key=lambda a: a["pct"], default=None)
        if mejor:
            t.insert("end", f"\nLo que más aporta: {mejor.get('grupo_real') or mejor['grupo']} "
                            f"(+{mejor['pct']:.1f}%)\n", "mut")


# ---------------------------------------------------------------- pruebas
def autotest():
    T = """+243 de fuerza +[150 - 180]
+2.970 de vida máxima [1.831 - 2.200]
Multiplicador de daño por vulnerabilidad x52% [16 - 28]%
Multiplicador de daño de Físico x32% [14 - 24]%
+64,0% de daño a enemigos cercanos
Tus ataques infligen del 1% al 390% [325 - 390]% de su daño normal
+[30 - 50]% de daño en el tiempo"""
    afijos, total, comp = analizar(T, "Guantes")
    for a in sorted(afijos, key=lambda x: -(x.get("pct") or 0)):
        nom = a.get("grupo_real") or a["grupo"]
        pct = "—" if a.get("pct") is None else f"{a['pct']:+.1f}%"
        print(f"  {pct:>9}  {nom:<32} {a['tipo']}")
    print(f"\n  TOTAL pieza: +{total:.1f}%")
    if comp:
        print(f"  vs {comp['hueco']}: {comp['dif']:+.1f}%")


if __name__ == "__main__":
    if "--test" in sys.argv:
        autotest()
    else:
        App().mainloop()
