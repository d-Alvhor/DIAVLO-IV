#!/usr/bin/env python3
"""La hoja de personaje con la GEOMETRÍA REAL de una partida.

40 capturas de la ficha de un Paladín 70 a 3456x2168 con Windows al 200%, con
las cajas tal como las devolvió el OCR. Es lo único que dice si el emparejado
etiqueta-valor funciona de verdad.

Existe porque el OCR escribe el símbolo % como "9/0" o "0/0" —"3.166,1 9/0"—
y por eso NINGUNA fila porcentual se reconocía como número. Se leían las planas
(Fuerza, Dureza, Espinas) y ninguna de las ofensivas.
"""
import sys
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent))
import valorar as V

FIX = json.loads((AQUI / "ficha_cajas.json").read_text(encoding="utf-8"))

# Tienen que salir sí o sí: son las que mandan en el cálculo.
OBLIGATORIAS = ("daño de golpe crítico", "daño por vulnerabilidad",
                "todo el daño", "daño físico", "espinas", "vida máxima",
                "armadura", "dureza", "fuerza", "probabilidad de bloqueo",
                "daño contra enemigos de élite", "resolución máxima")
# Rango en el que tiene que caer el valor, para que no cuele un cruce.
CORDURA = {"daño de golpe crítico": (500, 20000), "todo el daño": (50, 2000),
           "daño por vulnerabilidad": (50, 2000), "daño físico": (50, 2000),
           "espinas": (1000, 100000), "fuerza": (1000, 20000),
           "probabilidad de bloqueo": (10, 100), "vida máxima": (5000, 100000)}


def main():
    acumulado = {}
    for cap in FIX:
        ls = [{"texto": l["t"], "x": l["x"], "y": l["y"], "x2": l["x2"],
               "y2": l["y2"], "h": l["y2"] - l["y"]} for l in cap["l"]]
        acumulado.update(V.leer_ficha_cajas(ls))

    fallos = []
    for k in OBLIGATORIAS:
        if k not in acumulado:
            fallos.append(f"no lee «{k}»")
    for k, (lo, hi) in CORDURA.items():
        v = acumulado.get(k)
        if v is not None and not (lo <= v <= hi):
            fallos.append(f"«{k}» = {v}, fuera de [{lo}, {hi}]")

    print(f"  {len(acumulado)} estadísticas de {len(FIX)} capturas reales")
    for k in sorted(acumulado):
        marca = "**" if k in OBLIGATORIAS else "  "
        print(f"   {marca} {k:<40} {acumulado[k]:g}")
    for f in fallos:
        print(f"  MAL  {f}")
    print(f"\n  {'PASA' if not fallos else 'FALLA'}")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
