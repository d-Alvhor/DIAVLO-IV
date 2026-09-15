#!/usr/bin/env python3
"""Captura anclada al cursor.

El tooltip sale pegado al ratón, así que leer la pantalla entera cada 0,7 s era
leer el sitio equivocado y además leer cuando no había nada que leer.

La forma del recuadro no es arbitraria: medido sobre las capturas reales del
jugador, el tooltip más grande ocupa el 23% del ancho de pantalla y el 94% del
ALTO. Por eso se recorta en horizontal y NUNCA en vertical — un recuadro
cuadrado alrededor del cursor cortaría el tooltip por la mitad.
"""
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent))
import tracker as T

# Proporciones reales medidas en pruebas/fixtures.json
TOOLTIP_ANCHO = 0.23        # del ancho de la pantalla
TOOLTIP_ALTO = 0.94         # del alto

MONITORES = [
    ("principal 3456x2168", {"left": 0, "top": 0, "width": 3456, "height": 2168}),
    ("2K a la derecha",     {"left": 3456, "top": 0, "width": 2560, "height": 1440}),
    ("vertical a la izq",   {"left": -1200, "top": 0, "width": 1200, "height": 1920}),
]


def main():
    fallos = []
    for etiqueta, mon in MONITORES:
        esquinas = [
            ("centro",      (mon["left"] + mon["width"] // 2, mon["top"] + mon["height"] // 2)),
            ("sup-izq",     (mon["left"] + 5, mon["top"] + 5)),
            ("sup-der",     (mon["left"] + mon["width"] - 5, mon["top"] + 5)),
            ("inf-izq",     (mon["left"] + 5, mon["top"] + mon["height"] - 5)),
            ("inf-der",     (mon["left"] + mon["width"] - 5, mon["top"] + mon["height"] - 5)),
        ]
        for nombre, pos in esquinas:
            c = T.caja_cursor(pos, mon)
            if not c:
                fallos.append(f"{etiqueta}/{nombre}: no devuelve recuadro")
                continue
            x, y, an, al = c
            if x < mon["left"] or x + an > mon["left"] + mon["width"]:
                fallos.append(f"{etiqueta}/{nombre}: se sale a lo ancho ({c})")
            if y != mon["top"] or al != mon["height"]:
                fallos.append(f"{etiqueta}/{nombre}: no coge el alto entero ({c})")
            # ancho suficiente para un tooltip que salga a IZQUIERDA o DERECHA
            if an < mon["width"] * TOOLTIP_ANCHO * 2:
                fallos.append(f"{etiqueta}/{nombre}: demasiado estrecho para un "
                              f"tooltip a cualquier lado ({an} px)")
        c = T.caja_cursor(esquinas[0][1], mon)
        ahorro = 1 - (c[2] * c[3]) / (mon["width"] * mon["height"])
        print(f"  {etiqueta:<22} recuadro {c[2]}x{c[3]}  ahorro {ahorro:.0%}")
        if ahorro <= 0:
            fallos.append(f"{etiqueta}: el recuadro no ahorra nada")

    # sin ratón (o fuera de Windows) no puede reventar: devuelve None y el
    # bucle cae al modo de pantalla entera
    if T.caja_cursor(None, MONITORES[0][1]) is not None:
        fallos.append("sin posición de ratón debería devolver None")
    elif T.caja_cursor((100, 100), None) is not None:
        fallos.append("sin monitor debería devolver None")
    else:
        print("  ok  sin ratón o sin monitor devuelve None, no revienta")

    # posicion_raton no revienta fuera de Windows
    try:
        T.posicion_raton()
        print("  ok  posicion_raton() no revienta en esta plataforma")
    except Exception as e:
        fallos.append(f"posicion_raton revienta: {type(e).__name__}: {e}")

    # las constantes del bucle tienen que ser sanas
    if not (0 < T.QUIETO < 1):
        fallos.append(f"QUIETO={T.QUIETO} fuera de rango razonable")
    if not (T.REPASO > T.QUIETO):
        fallos.append(f"REPASO={T.REPASO} debe ser mayor que QUIETO={T.QUIETO}")
    if T.FALLOS_PANTALLA < 3:
        fallos.append(f"FALLOS_PANTALLA={T.FALLOS_PANTALLA}: la red de seguridad "
                      f"saltaría demasiado pronto")

    for f in fallos:
        print(f"  MAL  {f}")
    print(f"\n  {'PASA' if not fallos else 'FALLA'}")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
