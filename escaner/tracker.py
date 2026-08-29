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
import difflib
import unicodedata
import threading
import ctypes.wintypes
from pathlib import Path
from datetime import datetime

def _dpi_consciente():
    """Windows MIENTE sobre el tamaño de la pantalla a los procesos que no se
    declaran conscientes del DPI. A 125% de escalado, un monitor de 2560x1440
    se reporta como 2048x1152: la captura sale más pequeña y borrosa, y las
    coordenadas de tk dejan de coincidir con las de la captura.

    Hay que llamarlo ANTES de crear ninguna ventana y antes de capturar nada,
    por eso vive aquí arriba y no dentro de la clase. Devuelve el escalado
    declarado en Windows, para agrandar la interfaz en consecuencia."""
    if sys.platform != "win32":
        return 1.0
    import ctypes
    for llamada in (lambda: ctypes.windll.shcore.SetProcessDpiAwareness(2),
                    lambda: ctypes.windll.user32.SetProcessDPIAware()):
        try:
            llamada()
            break
        except Exception:
            continue
    try:
        return max(1.0, ctypes.windll.user32.GetDpiForSystem() / 96.0)
    except Exception:
        return 1.0


ESCALADO = _dpi_consciente()

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
# Sello y dijes salen en el visor de configuraciones del leaderboard. Se leen y
# se valoran, pero NO cuentan para dar la build por completa: no todo el mundo
# los lleva, y si no, la sesión no terminaría nunca.
N_DIJES = 6
HUECOS_EXTRA = ["Sello"] + [f"Dije {i}" for i in range(1, N_DIJES + 1)]

# Cómo se reconoce un tooltip de HABILIDAD, visto en capturas reales del juego:
#   Punición
#   RANGO 1/15                      <- firma inequívoca, ningún objeto la tiene
#   Tiempo de reutilización: 0,5 s
#   MODIFICADORES
# Nada de listas de nombres a mano: el nombre se toma de la primera línea, así
# funciona con cualquier habilidad de cualquier clase sin mantener nada.
RANGO = re.compile(r"\brango\s*\d+\s*/\s*\d+", re.I)
# En el visor de configuraciones del leaderboard las habilidades NO llevan
# "RANGO n/15": llevan "Enfrentamiento : Castigo" y debajo MODIFICADORES con la
# lista de mejoras elegidas. Es más útil que el rango: dice qué eligió.
ELECCION = re.compile(r"^\s*(.{3,40}?)\s+[:：]\s+(.{3,40})\s*$")
MARCAS_HABILIDAD = [
    "tiempo de reutilizacion", "modificadores", "probabilidad de golpe de suerte",
    "coste:", "de fe", "genera", "canalizada", "definitiva", "dano sagrado",
]

# ---------------------------------------------------------------- texto
def norm(s):
    s = unicodedata.normalize("NFD", str(s))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", s).strip().lower()


# Palabras que solo salen en NUESTRA ventana. Si aparecen, el bloque es la
# propia interfaz del tracker: se descarta. (Cinturón, además del borrado del
# rectángulo: 564 capturas de una sesión real eran todas de sí mismo.)
PROPIAS = ("tracker de builds", "habilidad 1", "habilidad 2", "faltan",
           "trackear", "equipo\nhabilidades")


# Chrome de la interfaz del juego que se cuela dentro del recuadro del tooltip.
# No es parte del objeto: ni es su nombre ni es un afijo.
CHROME = ("EQUIPADO", "Casilla de", "Quitar", "Desmarcar objeto", "Marcar objeto",
          "Desplazar hacia abajo", "Desplazar hacia arriba", "Requiere nivel",
          "Comparar", "Soltar", "Equipación de la armería", "Guardar en el alijo",
          "Mejorar", "Bloqueado", "Estadísticas y materiales", "Transfigurado")
# Etiquetas de una sola palabra: SOLO si la línea es exactamente eso. Como
# subcadena se comerían nombres de objeto ("Mano" está dentro de un montón).
CHROME_EXACTO = ("mano", "mayus", "alt", "ctrl", "transfigurado", "equipado",
                 "cuello", "mano izquierda", "mano derecha", "mano izquierda,",
                 "vinculado a cuenta", "enlazar", "pado", "anillo", "amuleto")
# El OCR parte EQUIPADO en trozos ("EQUI PADO", "PADO"): se reconoce con hueco
# opcional entre letras, y también pegado a la etiqueta del hueco.
EQUIPADO = __import__("re").compile(r"^\s*(?:mano\s*\w*,?\s*|cuello\s*)?e?\s*q?\s*u?\s*i?\s*pado\s*$", __import__("re").I)
CHROME_N = tuple(sorted({__import__("re").sub(r"\s+", " ", c).strip().lower()
                         for c in CHROME}))


def es_chrome(linea):
    n = norm(linea)
    if n in CHROME_EXACTO or EQUIPADO.match(n):
        return True
    # el OCR pega un icono delante ("-L Desplazar hacia arriba"): se tolera
    # basura corta al principio, pero solo en líneas cortas de interfaz
    if any(n == c or n.startswith(c) or (len(n) < 46 and c in n) for c in CHROME_N):
        return True
    # el OCR destroza las etiquetas de interfaz ("Estadísticas" -> "Estacusúcas"):
    # con lista cerrada y línea corta, el parecido basta
    return bool(len(n) < 30 and difflib.get_close_matches(n, CHROME_N, n=1, cutoff=0.78))


def es_propia(texto):
    n = norm(texto)
    return sum(1 for p in PROPIAS if p in n) >= 2


# El tooltip parte un afijo largo en dos renglones: "Multiplicador de daño de
# golpe" / "crítico x30% [13-25]%". Cada mitad por separado no parsea, así que
# el valorador se comía los multiplicadores enteros y daba +5% a un arma con
# x30% de crítico. Se vuelven a juntar antes de valorar.
CORTADA = re.compile(r"(?:\b[a-záéíóúñ]{2,}|\bx)\s*$", re.I)
SIGUE = re.compile(r"^\s*(?:[a-záéíóúñ]|x\s*\d)")
# el OCR escribe el símbolo % como '0/0' o '9/0': x300/0 es x30%
PORCIENTO = re.compile(r"(\d+)[09]\s*/\s*0")


def reflujo(texto):
    """Vuelve a unir los afijos que el tooltip partió en dos renglones."""
    out = []
    for l in texto.splitlines():
        l = PORCIENTO.sub(r"\1%", l.strip())
        if not l:
            continue
        if out and CORTADA.search(out[-1]) and SIGUE.match(l):
            out[-1] = f"{out[-1]} {l}"
        else:
            out.append(l)
    return "\n".join(out)


def _nombre(previas):
    """El nombre de un objeto son las líneas que hay ENCIMA de la de tipo.
    El juego lo parte en varios renglones y el OCR los da sueltos:
    'YELMO EXCEPCIONAL DEL' / 'YUNQUE DE' / 'GLYNN'. Quedarse con el primero
    daba nombres a medias ('mANT0 DE. LOS', 'Escudo únic')."""
    partes = []
    for l in previas:
        l = re.sub(r"[*·•~^]+\s*$", "", l).strip()
        if not l or re.fullmatch(r"[\W\d_]+", l):   # adornos e iconos sueltos
            continue
        partes.append(l)
    return re.sub(r"\s{2,}", " ", " ".join(partes)).strip()[:70]


def calidad_nombre(n):
    """Cuánto fiarse de un nombre leído por OCR, para quedarse con la mejor de
    varias lecturas. Coger la más LARGA elegía justo la más sucia
    ('PUÑOS DEt DES f INO' por encima de 'PUÑOS DEL DESTINO')."""
    if not n:
        return 0.0
    if norm(n) in CAT.unicos:
        return 2.0                       # corregido contra el catálogo: seguro
    if CAT.hueco(n):
        return 0.1                       # es la línea de TIPO, no un nombre
    return sum(1 for c in n if c.isalpha() or c.isspace()) / len(n)


def identificar(texto):
    """Del texto de un panel saca (clase, hueco_o_nombre, nombre, texto).
    clase: 'objeto' | 'habilidad' | None."""
    if es_propia(texto):
        return None
    lineas = [l.strip() for l in texto.splitlines() if l.strip()]
    utiles = [l for l in lineas if not es_chrome(l)]
    if len(utiles) < 3:          # un tooltip real nunca son dos líneas sueltas
        return None
    limpio = reflujo("\n".join(utiles))
    n = norm(limpio)

    # ¿objeto? Se busca la línea de TIPO contra el catálogo, no a ojo. Puede
    # estar hasta la 10ª: por encima va el nombre, que ocupa varios renglones.
    for i, linea in enumerate(utiles[:10]):
        hueco = CAT.hueco(linea)
        if hueco:                       # None = tipo conocido pero no es equipo
            nombre = _nombre(utiles[:i]) or linea
            # los únicos tienen nombre canónico: el catálogo corrige el OCR
            return ("objeto", hueco, CAT.unico(nombre) or nombre, limpio)

    # ¿habilidad? EXIGIMOS "RANGO n/15". La red de seguridad anterior ("dos
    # marcadores sueltos") metía basura de la interfaz —nombres de mercenario,
    # cabeceras de panel— como si fueran habilidades. Un falso positivo es peor
    # que no detectar: llena la checklist de mentiras y la da por completa.
    if "modificadores" in n and not RANGO.search(n):
        for l in utiles[:3]:
            m = ELECCION.match(l)
            if m and "modificador" not in norm(l):
                nombre = f"{m.group(1).strip()} : {m.group(2).strip()}"
                return ("habilidad", norm(m.group(1)), nombre, limpio)

    if RANGO.search(n):
        nombre = utiles[0]
        for l in utiles[:3]:
            if 3 <= len(l) <= 40 and not re.search(r"\d", l) and not RANGO.search(norm(l)):
                nombre = l
                break
        return ("habilidad", norm(nombre), nombre, limpio)
    return None


# ---------------------------------------------------------------- captura + OCR
def monitores():
    try:
        import mss
        with mss.mss() as sct:
            return [dict(m) for m in sct.monitors]
    except Exception:
        return []


def monitor_activo():
    """El monitor donde está el RATÓN.

    Antes se capturaba `monitors[1]`, el primario. Pero el primario no tiene por
    qué ser donde juegas: aquí era un monitor vertical de 1200x1920 con la
    consola abierta, así que la app estaba leyendo una terminal de PowerShell
    mientras el juego corría en el 2K de al lado. El ratón sí está donde juegas,
    porque es con el ratón con lo que enseñas los objetos."""
    mons = monitores()[1:]
    if not mons:
        return None
    if len(mons) == 1:
        return mons[0]
    try:
        import ctypes
        pt = ctypes.wintypes.POINT()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
        for m in mons:
            if (m["left"] <= pt.x < m["left"] + m["width"]
                    and m["top"] <= pt.y < m["top"] + m["height"]):
                return m
    except Exception:
        pass
    return max(mons, key=lambda m: m["width"] * m["height"])


def pantalla():
    """Tamaño del área que se captura ahora mismo, en píxeles físicos."""
    m = monitor_activo()
    return (m["width"], m["height"]) if m else (0, 0)


def capturar(region=None, con_origen=False):
    from PIL import Image
    import mss
    with mss.mss() as sct:
        if isinstance(region, dict):
            mon = region
        elif region:
            mon = {"left": region[0], "top": region[1],
                   "width": region[2], "height": region[3]}
        else:
            mon = monitor_activo() or sct.monitors[1]
        shot = sct.grab(mon)
        img = Image.frombytes("RGB", shot.size, shot.bgra, "raw", "BGRX")
        return (img, (mon["left"], mon["top"])) if con_origen else img


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


def _fusionar_renglon(ls):
    """El OCR parte un mismo renglón en dos cuando hay mucho espacio: '+ 182' y
    'de fuerza' llegan como líneas distintas. Se vuelven a unir por altura."""
    ls = sorted(ls, key=lambda l: (l["y"], l["x"]))
    out = []
    for l in ls:
        if out:
            p = out[-1]
            alto = max(p["h"], l["h"], 1)
            # El hueco tolerado era alto*6: a 200% de escalado eso son ~300 px,
            # suficiente para saltar de un panel al de al lado. Así se pegó
            # "543.046" (la Dureza de la hoja) a un afijo del tooltip, y el
            # amuleto salió valorado en +474.179%. Un renglón partido de verdad
            # deja un hueco de pocos caracteres.
            if abs(l["y"] - p["y"]) < alto * 0.5 and 0 <= l["x"] - p["x2"] < alto * 1.6:
                p["texto"] = f"{p['texto']} {l['texto']}"
                p["x2"] = max(p["x2"], l["x2"])
                p["y2"] = max(p["y2"], l["y2"])
                p["h"] = p["y2"] - p["y"]
                continue
        out.append(dict(l))
    return out


def agrupar(lineas, hueco_max=2.4, solape_min=0.30, cajas=False):
    """Agrupa las líneas en paneles: un tooltip es un panel, y cada panel es una
    COLUMNA en la pantalla.

    La versión anterior encadenaba cada línea con la ANTERIOR en orden de altura.
    Con dos paneles a distinta altura eso los entrelaza: en una captura real el
    tooltip del casco quedó partido en seis trozos, con 'Raheir' y 'Aldkin' (el
    panel de mercenarios, a 2.500 px de distancia) metidos entre medias. El
    bloque que tenía el tipo de objeto se quedaba sin un solo afijo -> +0%.

    Ahora cada línea busca un panel ABIERTO cuya columna solape con la suya. El
    del mercenario abre el suyo y no rompe el del tooltip.
    """
    con_caja = [l for l in lineas if l["h"] > 0]
    if not con_caja:
        if not lineas or cajas:
            return []
        return ["\n".join(l["texto"] for l in lineas)]
    abiertos = []
    for l in _fusionar_renglon(con_caja):
        mejor, mejor_s = None, solape_min
        for b in abiertos:
            if l["y"] - b["y2"] > max(b["alto"], l["h"], 1) * hueco_max:
                continue                       # ese panel ya quedó atrás
            solapa = min(l["x2"], b["x2"]) - max(l["x"], b["x"])
            ancho = min(l["x2"] - l["x"], b["x2"] - b["x"]) or 1
            s = solapa / ancho
            if s > mejor_s:
                mejor, mejor_s = b, s
        if mejor is None:
            abiertos.append({"x": l["x"], "x2": l["x2"], "y2": l["y2"],
                             "alto": l["h"], "lineas": [l]})
        else:
            mejor["lineas"].append(l)
            mejor["x"] = min(mejor["x"], l["x"])
            mejor["x2"] = max(mejor["x2"], l["x2"])
            mejor["y2"] = max(mejor["y2"], l["y2"])
            mejor["alto"] = max(mejor["alto"], l["h"])
    for b in abiertos:
        b["texto"] = "\n".join(x["texto"] for x in b["lineas"])
        b["y"] = min(x["y"] for x in b["lineas"])
    return abiertos if cajas else [b["texto"] for b in abiertos]


def _lineas(res):
    if isinstance(res, dict):
        ls = res.get("lines") or []
        return [l.get("text", "") if isinstance(l, dict) else getattr(l, "text", "") for l in ls]
    ls = getattr(res, "lines", None)
    if ls:
        return [getattr(l, "text", "") for l in ls]
    return [getattr(res, "text", "") or ""]


ANCHO_OCR = 4000    # ancho al que se lleva la imagen para leerla


def escalar_para_ocr(img):
    """Sube la imagen a un ancho fijo en vez de multiplicar por 2 a ciegas.

    El x2 fijo estaba calibrado sobre capturas de 2036 px (-> 4072). En una
    pantalla de 2560 daba 5120x2880: el triple de píxeles que procesar cada
    0,7 s, sin leer mejor. Con un ancho objetivo el texto queda del mismo
    tamaño en píxeles vengas de la resolución que vengas."""
    from PIL import Image
    g = img.convert("L")
    k = ANCHO_OCR / max(g.width, 1)
    if k <= 1.02:
        return g
    return g.resize((int(g.width * k), int(g.height * k)), Image.LANCZOS)


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
        # solo la que se usa: preparar() construía cuatro y tiraba tres
        versiones = [("escalada", escalar_para_ocr(img)), ("cruda", img)]
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
        """Devuelve True si es nuevo, "mejor" si mejora lo que ya había."""
        if clase != "objeto":
            if clave in self.habilidades or len(self.habilidades) >= N_HABILIDADES:
                return False
            self.habilidades[clave] = {"nombre": nombre, "texto": texto}
            return True

        # huecos repetidos: dos anillos, seis dijes
        for base, tope in (("Anillo", 2), ("Dije", N_DIJES)):
            if clave != base:
                continue
            ya = [k for k in self.objetos if k.startswith(base)]
            igual = next((k for k in ya if self.objetos[k]["nombre"] == nombre), None)
            if igual:
                clave = igual
            elif len(ya) >= tope:
                return False
            else:
                clave = f"{base} {len(ya) + 1}"

        afijos, total = V.analizar(texto, CAT)
        # Menos de 3 afijos en una pieza de nivel 70 no es una pieza pobre: es
        # una LECTURA pobre (tapada por otro panel, o a medio desplazar). Se
        # marca, porque dar un +0% por bueno es peor que decir que no lo sabes.
        dato = {"nombre": nombre, "texto": texto, "aporte": round(total, 1),
                "parcial": len(afijos) < 3,
                "afijos": [{"grupo": a.get("grupo_real") or a["grupo"],
                            "valor": a["valor"], "mult": bool(a.get("mult")),
                            "pct": round(a["pct"], 1) if a.get("pct") is not None else None,
                            "tipo": a.get("tipo"), "muerto": a.get("muerto")}
                           for a in afijos]}
        # La misma pieza se lee muchas veces mientras pasas el ratón, y algunas
        # salen tapadas por otro panel o a medio desplazar. Nos quedamos con la
        # lectura MÁS COMPLETA, no con la primera ni con la última.
        ya = self.objetos.get(clave)
        if ya is not None:
            # El nombre se elige APARTE de los afijos: la lectura más completa
            # no tiene por qué ser la que leyó mejor el nombre, ni al revés.
            mejor_n = max((nombre, ya.get("nombre") or ""), key=calidad_nombre)
            ya["nombre"] = mejor_n
            if len(afijos) <= len(ya.get("afijos") or []):
                return False
            dato["nombre"] = mejor_n
            self.objetos[clave] = dato
            return "mejor"
        self.objetos[clave] = dato
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
        self._pendiente = None
        self._geom = None
        self._aviso_borrado = False
        self._factor = None
        self.region = self._zona_valida()
        if ESCALADO > 1.05:
            # con DPI awareness la ventana sale a tamaño físico, o sea diminuta
            # en una pantalla escalada. Se compensa aquí.
            self.tk.call("tk", "scaling", 1.3333 * ESCALADO)
            self.geometry(f"{int(640 * ESCALADO)}x{int(760 * ESCALADO)}+40+40")
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
        tk.Button(cab, text="Zona ✕", command=self.quitar_region, bg="#232019",
                  fg="#9a9088", relief="flat", padx=8).pack(side="left", padx=3)
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
        a, b = pantalla()
        try:
            self._factor = a / max(self.winfo_screenwidth(), 1) if a else 1.0
        except Exception:
            self._factor = 1.0
        self._vigilar_geometria()
        self._log(f"Capturando {a}×{b} px"
                  + (f" · escalado de Windows {ESCALADO:.0%}" if ESCALADO > 1.05 else "")
                  + (f" · ZONA {self.region[2]}×{self.region[3]}" if self.region else ""))
        ms = monitores()[1:]
        if len(ms) > 1:
            self._log(f"  Tienes {len(ms)} monitores: "
                      + ", ".join(f"{m['width']}×{m['height']}" for m in ms)
                      + ". Miro donde esté el ratón, así que ten el ratón "
                      "en la pantalla del juego.")
        if self._pendiente:
            self._log(self._pendiente)
        self._log("Dale a Trackear. Luego pasa el ratón por cada objeto y cada "
                  "habilidad; la checklist se va marcando sola.")

    def _vigilar_geometria(self):
        """Guarda dónde está esta ventana, DESDE EL HILO PRINCIPAL.

        _captura_limpia corre en el hilo de captura, y tkinter no es seguro
        fuera del suyo: winfo_rootx() allí lanza excepción. Como iba dentro de
        un try/except mudo, el borrado de la propia ventana no llegó a
        ejecutarse NUNCA y el tracker se seguía leyendo a sí mismo."""
        try:
            self._geom = (self.winfo_rootx(), self.winfo_rooty(),
                          self.winfo_width(), self.winfo_height())
        except Exception:
            pass
        self.after(250, self._vigilar_geometria)

    def _captura_limpia(self):
        """Captura y BORRA de la imagen el rectángulo de esta misma ventana.
        Se pinta encima en vez de ocultar la ventana para no dar tirones cada
        0,7 s."""
        img, (ox, oy) = capturar(self.region, con_origen=True)
        g = self._geom
        if not g:
            return img
        try:
            from PIL import ImageDraw
            wx, wy, ww, wh = g
            k = self._factor or 1.0            # tk -> píxeles de la captura
            x1, y1 = (wx - ox) * k, (wy - oy) * k
            barra = 34 * ESCALADO * k          # la barra de título va por encima
            caja = [int(max(0, min(x1 - 4 * k, img.width))),
                    int(max(0, min(y1 - barra, img.height))),
                    int(max(0, min(x1 + (ww + 4) * k, img.width))),
                    int(max(0, min(y1 + (wh + 4) * k, img.height)))]
            if caja[2] > caja[0] and caja[3] > caja[1]:
                ImageDraw.Draw(img).rectangle(caja, fill=(0, 0, 0))
        except Exception as e:
            if not self._aviso_borrado:
                self._aviso_borrado = True
                self.after(0, self._log, f"  (no puedo taparme a mí mismo: {e})")
        return img

    def _zona_valida(self):
        """Una zona dibujada en otra pantalla (u otro escalado) recorta mal: sus
        números son píxeles de una pantalla que ya no existe. Se descarta en vez
        de aplicarse a ciegas — era la causa de 'no coge toda la pantalla'."""
        cfg = self._cfg()
        z = cfg.get("region")
        if not z:
            return None
        ancho, alto = pantalla()
        antes = cfg.get("pantalla")
        if antes and list(antes) != [ancho, alto]:
            self._pendiente = (f"Ignoro la zona guardada: se dibujó en una "
                               f"pantalla de {antes[0]}×{antes[1]} y ahora tienes "
                               f"{ancho}×{alto}.")
            return None
        if z[2] * z[3] < ancho * alto * 0.92:
            self._pendiente = (f"⚠ Tienes una ZONA fijada de {z[2]}×{z[3]}: solo "
                               f"el {z[2]*z[3]/(ancho*alto):.0%} de la pantalla. "
                               f"Todo lo de fuera es invisible. Pulsa «Zona ✕» "
                               f"para quitarla.")
        return z

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
        tk.Label(self.lista, text="SELLO Y DIJES  (opcional)", bg="#141210",
                 fg="#6b625a", font=("Georgia", 9, "bold"), anchor="w"
                 ).pack(fill="x", pady=(10, 2))
        for h in HUECOS_EXTRA:
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
                img = self._captura_limpia()
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
                    mayor = max(trozos, key=len) if trozos else ""
                    muestra = " / ".join(mayor.splitlines()[:3])[:80]
                    self.after(0, self._log,
                               f"  … {self.ciclos} lecturas · {len(trozos)} bloques · "
                               f"el mayor tiene {len(mayor.splitlines())} líneas\n"
                               f"     lo que leo ahí: {muestra}")
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
            if d.get("parcial"):
                self._log(f"  ◐ {nombre}  —  solo he leído {len(afijos)} afijo(s); "
                          "el tooltip estaba tapado. Vuelve a pasar el ratón.")
            else:
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
        d = self.perfil.objetos.get(clave) if self.perfil else None
        parcial = bool(d and d.get("parcial"))
        fila["marca"].config(text="◐" if parcial else "●",
                             fg="#c9a227" if parcial else "#4a9d68")
        fila["nombre"].config(fg="#e8e2da")
        extra = ""
        if d and d.get("aporte") is not None:
            extra = ("   lectura a medias — vuelve a pasar el ratón"
                     if parcial else f"   +{d['aporte']:.0f}%")
        fila["valor"].config(text=(texto[:34] + extra),
                             fg="#c9a227" if parcial else "#c9c0b4")

    def leer_ficha(self):
        """Lee la hoja de personaje mientras la desplazas.

        No cabe en una sola captura: son ~49 filas en cuatro secciones. Lee
        durante unos segundos y va acumulando, así que basta con abrir la ficha
        (tecla C) y bajar despacio."""
        if self.grabando:
            self._log("Para el trackeo antes de leer la ficha.")
            return
        if getattr(self, "_leyendo_ficha", False):
            self._log("Ya estoy leyendo la ficha, espera a que acabe.")
            return
        self._leyendo_ficha = True
        self._log("\nLeyendo la ficha 15 s. Abre la hoja de personaje (C), entra "
                  "en «Estadísticas y materiales» —no vale el resumen— y baja "
                  "despacio por la lista.")
        self.update()
        threading.Thread(target=self._bucle_ficha, daemon=True).start()

    def _bucle_ficha(self, segundos=15.0):
        vistas, fin, ciclos = {}, time.time() + segundos, 0
        while time.time() < fin:
            try:
                img = self._captura_limpia()
                import winocr
                res = winocr.recognize_pil_sync(escalar_para_ocr(img), "es-ES")
                lineas = _lineas_con_caja(res)
                # Por CAJAS, no por texto: en la hoja la etiqueta va pegada a la
                # izquierda y el número al borde derecho, medio panel de por
                # medio. Unidos por texto nunca se emparejan.
                nuevas = V.leer_ficha_cajas(lineas)
                nuevas.update(V.leer_ficha(reflujo("\n".join(
                    l["texto"] for l in lineas))))
                _al_corpus(img, "\n".join(l["texto"] for l in lineas), "ficha")
                for k, v in nuevas.items():
                    if k not in vistas:
                        self.after(0, self._log, f"      {k}: {v:g}")
                    vistas[k] = v
                ciclos += 1
            except Exception as e:
                self.after(0, self._log, f"  (lectura saltada: {type(e).__name__}: {e})")
            self.after(0, self.estado.config,
                       {"text": f"ficha: {len(vistas)} estadísticas"})
            time.sleep(0.6)
        self.after(0, self._fin_ficha, vistas, ciclos)

    def _fin_ficha(self, vistas, ciclos):
        self._leyendo_ficha = False
        if not vistas:
            self._log("  No he reconocido ninguna estadística. Abre la hoja de "
                      "personaje con C y vuelve a darle a Ficha.")
            self.estado.config(text="ficha vacía")
            return
        V.guardar_ficha(vistas)
        # Contra lo ACUMULADO en disco, no contra esta pasada: si no, decía que
        # faltaban 33 cuando ya estaban guardadas de la vez anterior.
        todo = dict(V.GRUPOS)
        try:
            todo.update(json.loads(V.PERFIL_STATS.read_text(encoding="utf-8")))
        except Exception:
            pass
        tengo = {V.norm(k) for k in todo}
        faltan = [f for f in V.FICHA
                  if V.norm(f) not in tengo
                  and V.norm(V.ALIAS_FICHA.get(V.norm(f), f)) not in tengo
                  and V.norm(f) not in V.NO_GRUPO]   # no insistir con las que no pintan
        self._log(f"  ✓ {len(vistas)} nuevas en {ciclos} lecturas · "
                  f"{len(todo)} acumuladas en total.")
        if faltan:
            self._log(f"  Aún sin ver ({len(faltan)}): {', '.join(faltan[:6])}"
                      + ("…" if len(faltan) > 6 else "")
                      + "\n  Vuelve a darle a Ficha sobre esa parte de la lista.")
        else:
            self._log("  ★ La ficha entera. Ya puedes darle a Trackear.")
        self.estado.config(text=f"ficha: {len(todo)} estadísticas")

    def _informe(self):
        if not self.perfil:
            return
        p = {"objetos": self.perfil.objetos}
        self._log("\n" + "─" * 46)
        for l in V.informe(p).splitlines():
            self._log(l)
        self._log("─" * 46)

    # ---------------------------------------------------------------- zona
    def quitar_region(self):
        """Sin esto no había forma de volver a mirar la pantalla entera."""
        self.region = None
        try:
            CONFIG.unlink()
        except FileNotFoundError:
            pass
        a, b = pantalla()
        self._log(f"Zona quitada. Vuelvo a mirar la pantalla entera ({a}×{b}).")

    def elegir_region(self):
        """Marca a mano el recuadro donde salen los tooltips.

        Casi nunca hace falta: agrupar() separa los paneles de una pantalla
        entera. Sirve para pantallas muy grandes, donde limitar el área acelera
        cada ciclo."""
        if self.grabando:
            self._log("Para el trackeo antes de marcar la zona.")
            return
        self.withdraw()
        self.update()
        time.sleep(0.25)
        sel = tk.Toplevel()
        sel.attributes("-fullscreen", True, "-alpha", 0.25)
        sel.configure(bg="black")
        cv = tk.Canvas(sel, cursor="cross", bg="black", highlightthickness=0)
        cv.pack(fill="both", expand=True)
        tk.Label(sel, text="Arrastra sobre la zona de los tooltips  ·  Esc para cancelar",
                 bg="#c14a4a", fg="white", font=("Segoe UI", 11, "bold"),
                 padx=14, pady=6).place(relx=0.5, y=30, anchor="n")
        est = {}

        def cerrar(msg=None):
            try:
                sel.destroy()
            except Exception:
                pass
            self.deiconify()
            if msg:
                self._log(msg)

        def down(e):
            # x_root/y_root son coordenadas del ESCRITORIO VIRTUAL, que es lo
            # que entiende mss. e.x/e.y son del canvas: en multimonitor apuntan
            # a otro sitio.
            est["x"], est["y"] = e.x_root, e.y_root
            est["cx"], est["cy"] = e.x, e.y
            est["r"] = cv.create_rectangle(e.x, e.y, e.x, e.y,
                                           outline="#c14a4a", width=2)

        def move(e):
            if "r" in est:
                cv.coords(est["r"], est["cx"], est["cy"], e.x, e.y)

        def up(e):
            if "x" not in est:
                return
            an, al = abs(e.x_root - est["x"]), abs(e.y_root - est["y"])
            # Un clic sin arrastrar guardaba una zona de 0x0 y dejaba la app
            # inservible para siempre, sin forma de deshacerlo.
            if an < 80 or al < 80:
                cerrar(f"Zona descartada: {an}×{al} px es demasiado pequeño. "
                       "Sigo mirando la pantalla entera.")
                return
            self.region = [min(est["x"], e.x_root), min(est["y"], e.y_root), an, al]
            CONFIG.write_text(json.dumps({"region": self.region,
                                          "pantalla": list(pantalla())}))
            a, b = pantalla()
            pct = an * al / max(a * b, 1)
            cerrar(f"Zona fijada: {an}×{al} px ({pct:.0%} de la pantalla). "
                   "«Zona ✕» para volver a la pantalla entera.")

        cv.bind("<ButtonPress-1>", down)
        cv.bind("<B1-Motion>", move)
        cv.bind("<ButtonRelease-1>", up)
        sel.bind("<Escape>", lambda e: cerrar("Zona sin cambios."))
        sel.focus_force()


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
