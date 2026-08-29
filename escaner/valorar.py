#!/usr/bin/env python3
"""
Valorador de afijos — Diablo IV

La regla que gobierna todo, y que un humano calcula mal siempre:

  Un afijo que SUMA entra en un grupo compartido, y su valor real depende de
  cuánto tienes YA en ese grupo:
      +50 sobre un grupo de 4.047  ->  +1,2%
      +40 sobre un grupo de   11,5 ->  +347%

  Un afijo que MULTIPLICA (los que llevan "x") se aplica entero sobre todo lo
  demás y no se diluye nunca.

  => Templa en el grupo más VACÍO, no en el más grande.

Los nombres de afijo se normalizan contra el catálogo canónico (catalogo.py),
que es lo que corrige el ruido del OCR.
"""

import re
import json
import difflib
import unicodedata
from pathlib import Path

PERFIL_STATS = Path(__file__).with_name("mis_stats.json")
EN_COMBATE = Path(__file__).with_name("en_combate.json")

# ---------------------------------------------------------------- tu ficha
# Grupos aditivos, leídos de la ficha de personaje. Son la BASE de todo el
# cálculo: si están desfasados, las respuestas también.
# Se pueden sobrescribir con mis_stats.json sin tocar el código.
GRUPOS_DEF = {
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
# Cantidades planas: el marginal es sobre el total, no sobre 100+total.
PLANOS = {"espinas", "vida máxima", "vida por golpe", "armadura", "fuerza",
          "resolución máxima", "inteligencia", "voluntad", "destreza", "dureza",
          "daño base de arma", "máximo de fe", "resistencia física",
          "resistencia al fuego", "resistencia a los rayos", "resistencia al frío",
          "resistencia al veneno", "resistencia a la sombra"}

# La hoja de personaje del juego, tal cual la escribe (es-ES). Es vocabulario
# CERRADO: por eso una lectura sucia empareja sola con la buena, igual que con
# los 891 afijos. Sacado de la ficha real de un Paladín a nivel 70.
FICHA = (
    "Nivel", "Fuerza", "Inteligencia", "Voluntad", "Destreza",
    "Dureza", "Armadura", "Resistencia física", "Resistencia al fuego",
    "Resistencia a los rayos", "Resistencia al frío", "Resistencia al veneno",
    "Resistencia a la sombra",
    "Daño base de arma", "Velocidad de arma", "Probabilidad de golpe crítico",
    "Daño de golpe crítico", "Daño por vulnerabilidad", "Todo el daño",
    "Daño físico", "Daño con fuego", "Daño con rayos", "Daño con frío",
    "Daño sagrado", "Daño con veneno", "Daño con sombra",
    "Daño contra enemigos cercanos", "Daño contra enemigos de élite",
    "Espinas", "Probabilidad de Castigo",
    "Vida máxima", "Capacidad de pociones", "Curación recibida", "Vida por golpe",
    "Probabilidad de bloqueo", "Reducción de bloqueo", "Reducción de todo el daño",
    "Bonus de barrera", "Probabilidad de esquivar",
    "Máximo de Fe", "Regeneración de fe", "Velocidad de movimiento",
    "Reducción de tiempo de reutilización", "Bonus de probabilidad de golpe de suerte",
    "Ralentización por golpe de suerte", "Aturdimiento por golpe de suerte",
    "Bonus de experiencia", "Resolución máxima", "Reducción de daño",
)

# La hoja y los afijos NO llaman igual a lo mismo: la ficha dice "Daño contra
# enemigos cercanos" y el objeto dice "daño a enemigos cercanos". Sin esto, el
# valor de la ficha no alimentaba su propio grupo.
ALIAS_FICHA = {
    "dano contra enemigos cercanos": "daño a enemigos cercanos",
}   # las claves van SIN tildes: se consultan con norm(), que las quita

# Filas de la ficha que no son un grupo donde nada se diluya.
NO_GRUPO = {"nivel", "capacidad de pociones", "bonus de experiencia",
            "velocidad de arma", "regeneración de fe", "reducción de daño",
            "bonus de probabilidad de golpe de suerte"}

# Afijos que no aportan NADA a una build de espinas físicas directas.
MUERTOS = {
    "daño en el tiempo": "tu daño de espinas es directo, no periódico",
    "daño de frío": "eres físico", "daño con frío": "eres físico",
    "daño de fuego": "eres físico", "daño con fuego": "eres físico",
    "daño sagrado": "eres físico", "daño de veneno": "eres físico",
    "daño de sombra": "eres físico",
    "daño a enemigos lejanos": "eres cuerpo a cuerpo, siempre estás pegado",
}


def norm(s):
    s = unicodedata.normalize("NFD", str(s))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", s).strip().lower()


def cargar_grupos():
    if PERFIL_STATS.exists():
        try:
            d = json.loads(PERFIL_STATS.read_text(encoding="utf-8"))
            g = dict(GRUPOS_DEF)
            g.update({k: float(v) for k, v in d.items()})
            return g
        except Exception:
            pass
    return dict(GRUPOS_DEF)


def cargar_combate():
    """Valores que la ficha da MAL porque los mide fuera de combate.

    La hoja de personaje enseña el estado en reposo. Una build que acumula
    —Resolución, bloqueo por acumulación, fortificación— vale en combate algo
    muy distinto: la ficha decía 17 de Resolución máxima cuando en el juego son
    29, y 77,5% de bloqueo cuando en combate topa. Como los grupos son el
    divisor de todo el cálculo, usar el número en reposo lo falsea entero.

    Este fichero lo escribe el jugador y la lectura de ficha NUNCA lo pisa."""
    try:
        crudo = json.loads(EN_COMBATE.read_text(encoding="utf-8"))
    except Exception:
        return {}
    out, sueltas = {}, []
    conocidas = list(GRUPOS_DEF) + [f.lower() for f in FICHA]
    for k, v in crudo.items():
        if str(k).startswith("_"):
            continue
        try:
            v = float(v)
        except (TypeError, ValueError):
            sueltas.append(k)
            continue
        # Lo escribe una persona a mano: un acento o una letra de más no puede
        # hacer que la línea se ignore en silencio.
        n = norm(k)
        casa = next((c for c in conocidas if norm(c) == n), None)
        if casa is None:
            cerca = difflib.get_close_matches(n, [norm(c) for c in conocidas],
                                              n=1, cutoff=0.82)
            casa = next((c for c in conocidas if norm(c) == cerca[0]), None) if cerca else None
        if casa is None:
            sueltas.append(k)
            continue
        out[ALIAS_FICHA.get(norm(casa), casa)] = v
    if sueltas:
        print(f"  ⚠ en_combate.json: no reconozco {sueltas}. "
              f"Se ignoran. Mira los nombres en valorar.py (FICHA).")
    return out


COMBATE = cargar_combate()
GRUPOS = {k: v for k, v in cargar_grupos().items()
          if re.sub(r"\s+", " ", str(k)).strip().lower() not in
          {"nivel", "capacidad de pociones", "bonus de experiencia",
           "velocidad de arma", "regeneración de fe", "reducción de daño",
           "bonus de probabilidad de golpe de suerte"}}
GRUPOS.update(COMBATE)                    # lo de combate manda sobre la ficha



def num(s):
    """OCR real trae ruido: puntos sueltos, comas huérfanas, cifras partidas."""
    t = str(s).strip()
    if not re.search(r"\d", t):
        return None
    # "30,5 %" tiene que dar 30.5. Antes solo llegaban aquí números ya pelados
    # por la regex de turno; leyendo la ficha por cajas llega la celda entera.
    t = t.rstrip("% \t").rstrip(".,")
    if "," in t:
        ent, _, dec = t.rpartition(",")
        t = ent.replace(".", "") + "." + dec
    else:
        t = t.replace(".", "")
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


# ---------------------------------------------------------------- parseo
def parsear(texto, cat=None):
    """Tooltip -> [{grupo, valor, mult}]. Si se pasa el catálogo, los nombres
    de afijo se corrigen contra los 891 canónicos (arregla el ruido del OCR)."""
    out = []
    for linea in str(texto).splitlines():
        linea = linea.strip()
        if not linea:
            continue

        m = re.search(r"multiplicador de (.+?)\s*x\s*(\d[\d.,]*)\s*%?", linea, re.I)
        if m:
            v, g = num(m.group(2)), limpiar(m.group(1))
            if v is not None and len(g) > 2:
                out.append({"grupo": g, "valor": v, "mult": True, "crudo": linea})
            continue

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

    if cat:                                   # corregir contra el catálogo
        for a in out:
            canon = cat.afijo("de " + a["grupo"]) or cat.afijo(a["grupo"])
            if canon and _compatible(a["grupo"], canon) and _mismo_afijo(a["grupo"], canon):
                a["canonico"] = canon
                a["grupo"] = limpiar(canon)
    return out


def _mismo_afijo(grupo, canonico):
    """¿El canónico corrige ESTE afijo, o es otro que venía pegado detrás?

    El emparejamiento difuso existe para arreglar el ruido del OCR
    ('velocidd de ataqe' -> 'velocidad de ataque'). Pero con dos afijos pegados
    —'3.506 de armadura de fuerza'— casaba con el segundo y le daba el valor
    del primero. Se acepta si se parecen ENTEROS, o si el canónico está al
    principio; no si aparece al final."""
    g = norm(grupo)
    c = norm(re.sub(r"^de\s+", "", canonico))
    if difflib.SequenceMatcher(None, g, c).ratio() >= 0.70:
        return True
    return c in g and g.index(c) <= 3


def _compatible(original, canonico):
    """El emparejamiento difuso puede invertir el sentido: 'daño de Físico'
    casa con 'daño NO físico', que es el afijo contrario. Se rechaza cualquier
    candidato que introduzca una negación que el original no tenía."""
    o, c = norm(original), norm(canonico)
    # OJO: con subcadenas, "dano fisico" contiene "no " -> hay que usar palabras.
    for neg in ("no", "sin", "excepto", "salvo"):
        pat = rf"\b{neg}\b"
        if re.search(pat, c) and not re.search(pat, o):
            return False
    return True


# ---------------------------------------------------------------- valoración
def casar(grupo, con_pos=False):
    """Grupo leído -> clave de GRUPOS. Si dos afijos se pegaron por un fallo de
    lectura ("3.506 de armadura de fuerza"), el valor es del que va PEGADO al
    número: o sea el que aparece antes en el texto."""
    g = norm(grupo)
    if not g:
        return (None, 99) if con_pos else None
    for k in GRUPOS:
        if norm(k) == g:
            return (k, 0) if con_pos else k
    mejor = None
    for k in GRUPOS:
        nk = norm(k)
        if nk and nk in g:
            pos = g.index(nk)
            if mejor is None or (pos, -len(nk)) < (mejor[1], -len(norm(mejor[0]))):
                mejor = (k, pos)
        elif g in nk and mejor is None:
            mejor = (k, 0)
    if mejor is None:
        return (None, 99) if con_pos else None
    return mejor if con_pos else mejor[0]


def muerto(grupo):
    g = norm(grupo)
    for pat, motivo in MUERTOS.items():
        if norm(pat) in g:
            return motivo
    return None


def valorar(a):
    mu = muerto(a["grupo"])
    if mu:
        return {**a, "pct": 0.0, "muerto": mu, "tipo": "muerto"}
    if a.get("mult"):
        return {**a, "grupo_real": casar(a["grupo"]) or a["grupo"],
                "pct": a["valor"], "tipo": "multiplica"}
    k, pos = casar(a["grupo"], con_pos=True)
    if not k:
        return {**a, "pct": None, "tipo": "desconocido"}
    if pos > 3:
        # El afijo casa, pero lejos del número: delante hay otra cosa, así que
        # ese número no es suyo. "216 a todas las resistencias de probabilidad
        # de golpe crítico" daba un 216% de crítico que no existe.
        return {**a, "pct": None, "tipo": "pegado a otro afijo"}
    base = GRUPOS[k]
    if k in PLANOS:
        pct = (a["valor"] / base) * 100 if base else 0.0
        tipo = "suma (plano)"
    else:
        pct = (a["valor"] / (100 + base)) * 100
        tipo = "suma"
    return {**a, "grupo_real": k, "base": base, "pct": pct, "tipo": tipo}


def aporte(afijos):
    """Aporte compuesto de una pieza, en % sobre el total."""
    g = 1.0
    for a in afijos:
        if a.get("pct"):
            g *= 1 + a["pct"] / 100
    return (g - 1) * 100


def analizar(texto, cat=None):
    afijos = [valorar(a) for a in parsear(texto, cat)]
    return afijos, aporte(afijos)


def comparar(texto_nuevo, texto_viejo, cat=None):
    """Devuelve (dif%, aporte_nuevo, aporte_viejo, afijos_nuevos)."""
    an, tn = analizar(texto_nuevo, cat)
    _, tv = analizar(texto_viejo, cat)
    dif = ((1 + tn / 100) / (1 + tv / 100) - 1) * 100
    return dif, tn, tv, an


def veredicto(dif):
    if dif > 3:
        return "GANA", "#4a9d68"
    if dif < -3:
        return "PIERDE", "#c14a4a"
    return "EMPATA", "#d0a63c"


def resumen_linea(afijos, total):
    """Una línea corta para el log del tracker."""
    mejor = max((a for a in afijos if (a.get("pct") or 0) > 0),
                key=lambda a: a["pct"], default=None)
    trozos = [f"+{total:.0f}%"]
    if mejor:
        trozos.append(f"lo mejor: {mejor.get('grupo_real') or mejor['grupo']} "
                      f"+{mejor['pct']:.0f}%")
    mu = [a for a in afijos if a.get("muerto")]
    if mu:
        trozos.append(f"⚠ {len(mu)} afijo(s) inútiles")
    return " · ".join(trozos)


# ---------------------------------------------------------------- ficha
def _canon_ficha(etiqueta):
    """Etiqueta leída por OCR -> nombre canónico de la ficha, o None.
    Lista cerrada de ~49 filas: 'Reducciön de blogueo' empareja sola."""
    e = norm(etiqueta)
    if not e or len(e) < 4:
        return None
    for f in FICHA:
        if norm(f) == e:
            return f
    cerca = difflib.get_close_matches(e, [norm(f) for f in FICHA], n=1, cutoff=0.80)
    if not cerca:
        return None
    return next(f for f in FICHA if norm(f) == cerca[0])


# Rango plausible de cada fila. Un valor fuera de aquí no es una estadística
# rara: es que se emparejó la etiqueta con el número de otra columna. Sin esto
# se guardó "velocidad de arma: 543.046" y "máximo de fe: 4.728".
RANGOS = {
    "nivel": (1, 100), "velocidad de arma": (0.5, 5.0),
    "capacidad de pociones": (1, 12), "máximo de fe": (30, 400),
    "regeneración de fe": (0.1, 50), "resolución máxima": (1, 60),
    "probabilidad de golpe crítico": (0, 100), "probabilidad de bloqueo": (0, 100),
    "probabilidad de esquivar": (0, 100), "reducción de bloqueo": (0, 100),
    "reducción de todo el daño": (0, 100), "curación recibida": (0, 500),
    "velocidad de movimiento": (0, 400), "capacidad": (1, 12),
    "reducción de tiempo de reutilización": (0, 90),
    "bonus de barrera": (0, 500), "vida máxima": (1000, 200000),
    "armadura": (100, 500000), "dureza": (1000, 100000000),
}


def _plausible(clave, valor):
    r = RANGOS.get(norm(clave)) or RANGOS.get(clave)
    return not r or (r[0] <= valor <= r[1])


# El OCR de Windows escribe el símbolo % como "0/0" o "9/0": "3.166,1 9/0" es
# 3.166,1 %. Sin esto NINGUNA fila porcentual se reconocía como número, y las
# ofensivas de la ficha son todas porcentuales.
PCT_OCR = re.compile(r"\s*[09]\s*[/|]\s*0\s*$")


def pct_ocr(t):
    return PCT_OCR.sub("%", str(t).strip())


def _es_valor(t):
    return bool(re.fullmatch(r"[+\-]?\s*[\d][\d.,]*\s*%?", pct_ocr(t)))


def leer_ficha_cajas(lineas):
    """Ficha de personaje -> {stat: valor}, emparejando por ALTURA.

    En la hoja, la etiqueta va pegada al borde izquierdo de la fila y el número
    al derecho: medio panel de distancia. Juntarlos por cercanía horizontal no
    funciona —era por lo que solo salían las cuatro de la columna estrecha—,
    pero por altura sí: el número está a la misma altura que su etiqueta, y
    cuando la etiqueta ocupa dos renglones ('Daño por' / 'vulnerabilidad') el
    número queda centrado entre los dos.
    """
    ls = [l for l in lineas if l.get("texto", "").strip()]
    valores = [l for l in ls if _es_valor(l["texto"])]
    etiquetas = [l for l in ls if not _es_valor(l["texto"])]
    out = {}
    for v in valores:
        cy = (v["y"] + v["y2"]) / 2
        alto = max(v["y2"] - v["y"], 1)
        n = num(pct_ocr(v["texto"]))
        if n is None:
            continue
        # A la izquierda, a su altura, y CERCA: sin el tope de distancia se
        # emparejaba con la etiqueta de otra columna de la pantalla (así salió
        # "reducción de todo el daño: 757", que es el valor de Destreza).
        cerca = [e for e in etiquetas
                 if e["x2"] <= v["x"] + alto
                 and v["x"] - e["x2"] < alto * 14
                 and abs((e["y"] + e["y2"]) / 2 - cy) < alto * 1.15]
        if not cerca:
            continue
        # solo la etiqueta más pegada, y su continuación en el renglón de abajo
        borde = max(e["x2"] for e in cerca)
        cerca = [e for e in cerca if borde - e["x2"] < alto * 12]
        cerca.sort(key=lambda e: (e["y"], e["x"]))
        candidatos = [" ".join(e["texto"] for e in cerca)]
        candidatos += [e["texto"] for e in
                       sorted(cerca, key=lambda e: abs((e["y"] + e["y2"]) / 2 - cy))]
        for c in candidatos:
            canon = _canon_ficha(c)
            if not canon:
                continue
            clave = ALIAS_FICHA.get(norm(canon), canon.lower())
            if _plausible(clave, n):
                out[clave] = n
            break
    return out


def leer_ficha(texto):
    """Ficha de personaje -> {stat canónico: valor}. TODAS las filas, no solo
    las que ya conocíamos: son la base del cálculo, y cuantas más haya, más
    afijos encuentran su grupo en vez de quedarse en 'desconocido'.

    El texto se pasa por reflujo() antes: la ficha parte las etiquetas largas
    en dos renglones ('Daño por' / 'vulnerabilidad 321,6 %') y sueltas no
    casan con nada."""
    out = {}
    for linea in str(texto).splitlines():
        l = linea.strip().replace("|", " ")
        if not l:
            continue
        m = re.match(r"^(.+?)\s+([\d][\d.,]*)\s*%?\s*$", l)
        if not m:
            continue
        v = num(m.group(2))
        if v is None:
            continue
        canon = _canon_ficha(m.group(1))
        if canon:
            out[ALIAS_FICHA.get(norm(canon), canon.lower())] = v
    return out


def guardar_ficha(valores):
    actual = {}
    if PERFIL_STATS.exists():
        try:
            actual = json.loads(PERFIL_STATS.read_text(encoding="utf-8"))
        except Exception:
            pass
    actual.update(valores)
    PERFIL_STATS.write_text(json.dumps(actual, ensure_ascii=False, indent=2),
                            encoding="utf-8")
    # Nivel o capacidad de pociones no son grupos donde nada se diluya: se
    # guardan, pero no entran en el reparto.
    GRUPOS.update({k: v for k, v in valores.items() if norm(k) not in NO_GRUPO})
    GRUPOS.update(COMBATE)                # la ficha no pisa lo de combate
    return len(valores)


# ---------------------------------------------------------------- informe
def informe(perfil):
    """Resumen legible de una build completa: qué aporta cada pieza, cuál es la
    más floja y en qué grupo conviene templar (el más vacío, no el más grande)."""
    objetos = perfil.get("objetos") or {}
    lineas = []
    piezas = sorted(((h, d) for h, d in objetos.items() if d.get("aporte") is not None),
                    key=lambda kv: -kv[1]["aporte"])
    if piezas:
        lineas.append("APORTE POR PIEZA")
        for h, d in piezas:
            lineas.append(f"  {d['aporte']:>7.0f}%   {h:<11} {d['nombre'][:34]}")
        floja = piezas[-1]
        lineas.append(f"\n  La más floja: {floja[0]} ({floja[1]['nombre'][:30]}, "
                      f"+{floja[1]['aporte']:.0f}%). Ahí es donde más margen tienes.")

    muertos = [(h, a["grupo"]) for h, d in objetos.items()
               for a in (d.get("afijos") or []) if a.get("muerto")]
    if muertos:
        lineas.append("\nAFIJOS QUE NO TE SIRVEN")
        for h, g in muertos:
            lineas.append(f"  {h:<11} {g}")

    if COMBATE:
        lineas.append("\nVALORES DE COMBATE (la ficha los da en reposo)")
        for k, v in sorted(COMBATE.items()):
            lineas.append(f"  {v:>8.1f}   {k}")

    # Solo grupos que esta build USA de verdad. Antes miraba todos los de la
    # ficha y recomendaba "probabilidad de esquivar" o "daño con fuego" a una
    # build física de espinas: grupos vacíos, sí, pero vacíos porque no pintan
    # nada aquí.
    usados = {casar(a.get("grupo_real") or a["grupo"])
              for d in objetos.values() for a in (d.get("afijos") or [])
              if not a.get("muerto")}
    usados.discard(None)
    candidatos = {k: v for k, v in GRUPOS.items()
                  if k in usados and k not in PLANOS and not muerto(k)}
    if candidatos:
        vacios = sorted(candidatos.items(), key=lambda kv: kv[1])[:3]
        lineas.append("\nDÓNDE TEMPLAR (de los grupos que esta build usa, "
                      "los más vacíos)")
        for k, v in vacios:
            lineas.append(f"  {v:>8.1f}%   {k}")
        lineas.append("  Un afijo que suma rinde el triple en un grupo vacío "
                      "que en uno lleno.")
    return "\n".join(lineas)


# ---------------------------------------------------------------- pruebas
def autotest():
    try:
        from catalogo import Catalogo
        cat = Catalogo()
    except Exception as e:
        cat = None
        print(f"  (sin catálogo: {e})")

    PUNOS = """+243 de fuerza +[150 - 180]
+2.970 de vida máxima [1.831 - 2.200]
Multiplicador de daño por vulnerabilidad x52% [16 - 28]%
Multiplicador de daño de Físico x32% [14 - 24]%
+64,0% de daño a enemigos cercanos
Tus ataques infligen del 1% al 390% [325 - 390]% de su daño normal
+[30 - 50]% de daño en el tiempo"""

    afijos, total = analizar(PUNOS, cat)
    print("  --- Puños del Destino ---")
    for a in sorted(afijos, key=lambda x: -(x.get("pct") or 0)):
        nom = a.get("grupo_real") or a["grupo"]
        pct = "—" if a.get("pct") is None else f"{a['pct']:+.1f}%"
        print(f"    {pct:>9}  {nom:<32} {a['tipo']}")
    print(f"\n    TOTAL: +{total:.1f}%")
    print(f"    log:   {resumen_linea(afijos, total)}")

    PEOR = """+180 de fuerza
+1.500 de vida máxima
Multiplicador de daño de golpe crítico x25% [26 - 50]%"""
    dif, tn, tv, _ = comparar(PEOR, PUNOS, cat)
    v, _ = veredicto(dif)
    print(f"\n  --- un guante peor contra los Puños ---")
    print(f"    {v}  {dif:+.1f}%   (nuevo +{tn:.0f}% · viejo +{tv:.0f}%)")

    dif2, _, _, _ = comparar(PUNOS, PUNOS, cat)
    v2, _ = veredicto(dif2)
    print(f"\n  --- el mismo objeto contra sí mismo (control) ---")
    print(f"    {v2}  {dif2:+.1f}%   {'ok' if abs(dif2) < 0.01 else 'MAL'}")

    print("\n  --- ruido del OCR ---")
    RUIDO = """.
+ . de fuerza
- 28]9'0
•
+2.970 de vida máxima
+64,0% de daño a enemigos cercanos"""
    a2, t2 = analizar(RUIDO, cat)
    print(f"    de 6 líneas mugrientas saca {len(a2)} afijos, total +{t2:.1f}% "
          f"{'ok' if len(a2) == 2 else 'revisar'}")


if __name__ == "__main__":
    autotest()
