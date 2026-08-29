#!/usr/bin/env python3
"""El visor de configuraciones del leaderboard.

Es la pantalla donde se ve la build de un rival del top. Sus tooltips NO son
como los del juego normal:

  · Las habilidades no llevan "RANGO n/15". Llevan "Enfrentamiento : Castigo"
    y debajo MODIFICADORES con las mejoras elegidas — que es más útil que el
    rango, porque dice QUÉ eligió.
  · Salen sellos horádricos y dijes, que estaban en la lista de ignorados desde
    el principio. El sello mítico de un rival daba 19%[x] de daño y +7%[x] a las
    habilidades de juggernaut: no es adorno.

Sello y dijes se leen y se valoran, pero NO cuentan para dar la build por
completa: no todo el mundo los lleva.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import tracker as T

HABILIDAD_VISOR = """Enfrentamiento : Castigo
MODIFICADORES
Resolución
Efectividad de Marcha del cruzado"""

HABILIDAD_JUEGO = """Punición
RANGO 15/15
Tiempo de reutilización: 0,5 s
MODIFICADORES"""

SELLO = """SELLO DE LA MENTE DIAMANTINA
Sello horádrico Mítico
900 de poder de objeto
Equipación de la armería
Desbloquea 6 huecos de dije
19,0%[x] de daño [12,0 - 20,0]%[x]
Voluntad justiciera de Cathan:
+7%[x] [7 - 10]% de daño de las habilidades de juggernaut
Conviccion férrea de Cathan:
+4 [3 - 4] de regeneración de fe por segundo"""

DIJE = """CORAZÓN DEL BALUARTE
Dije legendario
900 de poder de objeto
+2.004 de espinas [1.221 - 1.526]
+6,4% de probabilidad de golpe crítico [3,5 - 5,0]%"""


def main():
    fallos = []

    for texto, clase, pista in [
            (HABILIDAD_VISOR, "habilidad", "Enfrentamiento : Castigo"),
            (HABILIDAD_JUEGO, "habilidad", "Punición"),
            (SELLO, "objeto", "Sello"),
            (DIJE, "objeto", "Dije")]:
        r = T.identificar(texto)
        if not r:
            fallos.append(f"no reconoce: {texto.splitlines()[0]}")
            continue
        if r[0] != clase:
            fallos.append(f"{texto.splitlines()[0]}: clase {r[0]}, esperaba {clase}")
        elif pista not in (r[1] if clase == "objeto" else r[2]):
            fallos.append(f"{texto.splitlines()[0]}: falta «{pista}» en {r[1:3]}")
        else:
            print(f"  ok  {texto.splitlines()[0][:34]:<36} {r[0]:<10} "
                  f"{r[1] if r[0]=='objeto' else r[2]}")

    # sello y dijes NO pueden bloquear el "completo"
    p = T.Perfil("prueba", "rival")
    for h in T.HUECOS:
        p.anadir("objeto", h.rstrip(" 12") if h.startswith("Anillo") else h,
                 f"pieza {h}", "+100 de fuerza")
    for i in range(T.N_HABILIDADES):
        p.anadir("habilidad", f"hab{i}", f"Habilidad {i}", "x")
    if not p.completo():
        f, n = p.faltan()
        fallos.append(f"sin sello ni dijes NO da completo: faltan {f}, {n} habilidades")
    else:
        print("  ok  completo sin sello ni dijes")

    # pero si aparecen, se guardan
    p.anadir("objeto", "Sello", "SELLO DE LA MENTE DIAMANTINA", SELLO)
    for i in range(8):                       # más de 6: los de sobra se caen
        p.anadir("objeto", "Dije", f"DIJE {i}", DIJE)
    dijes = [k for k in p.objetos if k.startswith("Dije")]
    if "Sello" not in p.objetos:
        fallos.append("no guarda el sello")
    elif len(dijes) != T.N_DIJES:
        fallos.append(f"{len(dijes)} dijes, tope {T.N_DIJES}")
    else:
        print(f"  ok  guarda sello y {len(dijes)} dijes (tope respetado)")

    for f in fallos:
        print(f"  MAL  {f}")
    print(f"\n  {'PASA' if not fallos else 'FALLA'}")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
