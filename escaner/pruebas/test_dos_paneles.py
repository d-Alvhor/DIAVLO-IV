#!/usr/bin/env python3
"""Dos paneles en pantalla a la vez: el fallo que dio +474.179%.

En la pantalla de personaje conviven el resumen de la izquierda (Fuerza,
Voluntad, Destreza, Dureza) y el panel de la derecha. Están a la MISMA ALTURA,
así que todo lo que empareje por altura sin mirar la distancia cruza de un
panel al otro. Pasó dos veces en una sesión real:

  · "543.046" (la Dureza) se pegó a un afijo del tooltip y el amuleto se
    valoró en +474.179%.
  · "reducción de todo el daño" se emparejó con 757, que es Destreza.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import tracker as T
import valorar as V

H = 44                      # altura de línea a 200% de escalado
IZQ_ET, IZQ_VAL = 120, 640          # panel de resumen
DER_ET, DER_VAL = 1900, 2500        # panel de detalle, muy a la derecha

RESUMEN = [("Fuerza", "5.165"), ("Inteligencia", "930"), ("Voluntad", "964"),
           ("Destreza", "757"), ("Dureza", "543.046")]
DETALLE = [("Vida máxima", "15.246"), ("Armadura", "45.360"),
           ("Probabilidad de bloqueo", "77,5 %"),
           ("Reducción de todo el daño", "43,1 %"),
           ("Velocidad de arma", "1,20"), ("Máximo de Fe", "110"),
           ("Capacidad de pociones", "4"), ("Espinas", "8.035")]


def montar():
    ls, y = [], 0
    for (e1, v1), (e2, v2) in zip(RESUMEN + [("", "")] * 9, DETALLE + [("", "")] * 9):
        if e1:
            ls.append({"texto": e1, "x": IZQ_ET, "x2": IZQ_ET + len(e1) * 14,
                       "y": y, "y2": y + H, "h": H})
            ls.append({"texto": v1, "x": IZQ_VAL, "x2": IZQ_VAL + 130,
                       "y": y, "y2": y + H, "h": H})
        if e2:
            ls.append({"texto": e2, "x": DER_ET, "x2": DER_ET + len(e2) * 14,
                       "y": y, "y2": y + H, "h": H})
            ls.append({"texto": v2, "x": DER_VAL, "x2": DER_VAL + 130,
                       "y": y, "y2": y + H, "h": H})
        y += H + 22
    return ls


def main():
    ls = montar()
    fallos = []

    # 1. el emparejado no puede cruzar de panel
    r = V.leer_ficha_cajas(ls)
    esperado = {"fuerza": 5165, "inteligencia": 930, "voluntad": 964,
                "destreza": 757, "dureza": 543046, "vida máxima": 15246,
                "armadura": 45360, "probabilidad de bloqueo": 77.5,
                "reducción de todo el daño": 43.1, "velocidad de arma": 1.2,
                "máximo de fe": 110, "capacidad de pociones": 4, "espinas": 8035}
    for k, v in esperado.items():
        got = r.get(k)
        if got is None:
            fallos.append(f"no lee «{k}»")
        elif abs(got - v) > 0.05:
            fallos.append(f"«{k}» = {got}, debería ser {v}")
    print(f"  {len(r)} estadísticas, {len(esperado)} comprobadas")

    # 2. la fusión de renglones no puede saltar de panel
    for b in T.agrupar(ls):
        for linea in b.splitlines():
            if "543.046" in linea and len(linea) > 12:
                fallos.append(f"la Dureza se pegó a otra cosa: {linea!r}")

    # 3. un valor imposible se rechaza en vez de guardarse
    absurdo = [{"texto": "Velocidad de arma", "x": DER_ET, "x2": DER_ET + 240,
                "y": 0, "y2": H, "h": H},
               {"texto": "543.046", "x": DER_VAL, "x2": DER_VAL + 130,
                "y": 0, "y2": H, "h": H}]
    if "velocidad de arma" in V.leer_ficha_cajas(absurdo):
        fallos.append("acepta velocidad de arma = 543.046")
    else:
        print("  ok  rechaza «velocidad de arma: 543.046» por imposible")

    for f in fallos:
        print(f"  MAL  {f}")
    print(f"\n  {'PASA' if not fallos else 'FALLA'}")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
