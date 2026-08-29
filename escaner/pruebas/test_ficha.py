#!/usr/bin/env python3
"""La hoja de personaje, leída entera.

Antes solo se quedaba con 14 filas —las que ya estaban escritas a mano en el
código— y tiraba el resto. Los grupos son la base de todo el cálculo: cuantos
más haya, menos afijos se quedan en "desconocido".

El texto de abajo es la ficha REAL de un Paladín nivel 70, con las etiquetas
partidas en dos renglones tal como las parte el juego, y con ruido de OCR
metido a mano en cuatro filas.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import tracker as T
import valorar as V

# Tal como llega del OCR: etiquetas partidas, tildes comidas, letras cambiadas.
FICHA = """Nivel 70
Fuerza 4.896
Inteligencia 838
Voluntad 872
Destreza 665
Dureza 359.674
Armadura 43.943
Resistencia física 4.387
Resistencia al fuego 8.280
Resistencia a los rayos 6.757
Resistencia al frío 3.371
Resistencia al veneno 4.317
Resistencia a la sombra 3.371
Daño base de arma 3.940
Velocidad de arma 1,20
Probabilidad de golpe
crítico 49,4 %
Daño de golpe crítico 4.047,5 %
Daño por
vulnerabilidad 321,6 %
Todo el daño 176,5 %
Daño físico 266,9 %
Daño con fuego 25,0 %
Daño con rayos 25,0 %
Daño con frío 25,0 %
Daño sagrado 25,0 %
Daño con veneno 25,0 %
Daño con sombra 25,0 %
Daño contra enemigos
cercanos 11,5 %
Daño contra enemigos
de élite 159,0 %
Espinas 8.035
Probabilidad de Castigo 65,0 %
Vida máxima 10.124
Capacidad de pociones 4
Curación recibida 30,5 %
Vida por golpe 369
Probabilidad de
bloqueo 66,5 %
Reducciön de blogueo 27,7 %
Reducción de todo el
daño 43,1 %
Bonus de barrera 0,0 %
Probabilidad de
esquivar 4,0 %
Máximo de Fe 110
Regeneración de fe 1,50
Velocidad de
movimiento 110,0 %
Reducción de tiempo
de reutilización 33,4 %
Ralentización por
golpe de suerte 3,5 %
Aturdimiento por
golpe de suerte 3,0 %
Bonus de experiencia 1.400,0 %
Resoluciön maxima 17"""

# Lo que tiene que salir sí o sí, con su valor exacto.
CLAVE = {
    "fuerza": 4896, "dureza": 359674, "armadura": 43943,
    "daño de golpe crítico": 4047.5, "daño por vulnerabilidad": 321.6,
    "todo el daño": 176.5, "daño físico": 266.9,
    "daño a enemigos cercanos": 11.5,          # la ficha lo llama "contra"
    "daño contra enemigos de élite": 159.0,
    "espinas": 8035, "vida máxima": 10124,
    "probabilidad de bloqueo": 66.5,
    "reducción de bloqueo": 27.7,              # leído como "Reducciön de blogueo"
    "reducción de todo el daño": 43.1,
    "reducción de tiempo de reutilización": 33.4,
    "resolución máxima": 17,                   # leído como "Resoluciön maxima"
    "probabilidad de golpe crítico": 49.4,
    "máximo de fe": 110,
}


def main():
    leidas = V.leer_ficha(T.reflujo(FICHA))
    filas = len([l for l in FICHA.splitlines() if l.strip()])
    fallos = []
    for k, esperado in CLAVE.items():
        got = leidas.get(k)
        if got is None:
            fallos.append(f"no lee «{k}»")
        elif abs(got - esperado) > 0.05:
            fallos.append(f"«{k}»: {got} en vez de {esperado}")

    print(f"  {len(leidas)} estadísticas de {filas} renglones "
          f"({len(CLAVE)} obligatorias comprobadas)")
    if len(leidas) < 40:
        fallos.append(f"solo {len(leidas)} estadísticas; deberían ser 40+")
    for f in fallos:
        print(f"  MAL  {f}")
    if not fallos:
        for k in ("daño a enemigos cercanos", "reducción de bloqueo",
                  "resolución máxima"):
            print(f"  ok   {k:<38} {leidas[k]:g}")
    print(f"\n  {'PASA' if not fallos else 'FALLA'}")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
