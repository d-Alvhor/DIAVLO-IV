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
import unicodedata
from pathlib import Path

PERFIL_STATS = Path(__file__).with_name("mis_stats.json")

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
          "resolución máxima"}

# Afijos que no aportan NADA a una build de espinas físicas directas.
MUERTOS = {
    "daño en el tiempo": "tu daño de espinas es directo, no periódico",
    "daño de frío": "eres físico", "daño con frío": "eres físico",
    "daño de fuego": "eres físico", "daño con fuego": "eres físico",
    "daño sagrado": "eres físico", "daño de veneno": "eres físico",
    "daño de sombra": "eres físico",
    "daño a enemigos lejanos": "eres cuerpo a cuerpo, siempre estás pegado",
}


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


GRUPOS = cargar_grupos()


def norm(s):
    s = unicodedata.normalize("NFD", str(s))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", s).strip().lower()


def num(s):
    """OCR real trae ruido: puntos sueltos, comas huérfanas, cifras partidas."""
    t = str(s).strip()
    if not re.search(r"\d", t):
        return None
    t = t.rstrip(".,")
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

        m = re.search(r"multiplicador de (.+?)\s*x\s*(\d[\d.,]*)\s*%", linea, re.I)
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
            if canon and _compatible(a["grupo"], canon):
                a["canonico"] = canon
                a["grupo"] = limpiar(canon)
    return out


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
    mu = muerto(a["grupo"])
    if mu:
        return {**a, "pct": 0.0, "muerto": mu, "tipo": "muerto"}
    if a.get("mult"):
        return {**a, "grupo_real": casar(a["grupo"]) or a["grupo"],
                "pct": a["valor"], "tipo": "multiplica"}
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
def leer_ficha(texto):
    """Ficha de personaje -> {grupo: valor}. Así los grupos se mantienen al día
    sin editar código: son la base del cálculo y desfasados mienten."""
    out = {}
    for linea in str(texto).splitlines():
        l = linea.strip()
        if not l:
            continue
        m = re.match(r"^(.+?)\s+([\d.,]+)\s*%?\s*$", l)
        if not m:
            continue
        etiqueta, bruto = limpiar(m.group(1)), num(m.group(2))
        if bruto is None or len(etiqueta) < 4:
            continue
        # limpiar() quita el "de" tras "daño", así que hay que aplicarlo a las
        # dos partes o "daño de golpe crítico" nunca casa con su propia clave.
        e = limpiar(etiqueta)
        for k in GRUPOS_DEF:
            kk = limpiar(k)
            if kk == e or kk in e or e in kk:
                out[k] = bruto
                break
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
    GRUPOS.update(valores)
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

    porcentuales = {k: v for k, v in GRUPOS.items() if k not in PLANOS}
    vacios = sorted(porcentuales.items(), key=lambda kv: kv[1])[:3]
    lineas.append("\nDÓNDE TEMPLAR (grupos más vacíos)")
    for k, v in vacios:
        lineas.append(f"  {v:>8.1f}%   {k}")
    lineas.append("  Un afijo que suma rinde el triple en un grupo vacío que en uno lleno.")
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
