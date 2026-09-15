#!/usr/bin/env python3
"""Perfiles de clase: que el valorador no arrastre la build de otro personaje.

Existe por un fallo concreto. valorar.py llevaba escrita a mano la lista de
afijos que no sirven, sacada de un Paladín de espinas:

    MUERTOS = { "daño de fuego": "eres físico", ... }

Un Brujo es una clase de FUEGO. Tal cual, el tracker le habría dicho que sus
mejores afijos eran inútiles — y el jugador se los habría quitado.
"""
import sys
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent))
import valorar as V
from catalogo import Catalogo

CAT = Catalogo()
AFIJO_FUEGO = "+45,0% de daño con fuego"
AFIJO_ESPINAS = "+1.908 de espinas [1.221 - 1.526]"


def main():
    fallos = []
    original = V.CLASE

    disponibles = V.clases_disponibles()
    if "paladin" not in disponibles or "brujo" not in disponibles:
        print(f"  MAL  faltan perfiles: {disponibles}")
        return 1
    print(f"  clases: {', '.join(disponibles)}")

    # 1. El Brujo NO hereda los afijos muertos del Paladín
    V.cargar_clase("brujo")
    if V.MUERTOS:
        fallos.append(f"el Brujo hereda {len(V.MUERTOS)} afijos muertos: {list(V.MUERTOS)[:3]}")
    else:
        print("  ok   el Brujo no hereda afijos muertos")

    # 2. El mismo afijo de fuego: muerto para el Paladín, vivo para el Brujo
    a_brujo = V.analizar(AFIJO_FUEGO, CAT)[0]
    muerto_brujo = bool(a_brujo and a_brujo[0].get("muerto"))
    V.cargar_clase("paladin")
    a_pala = V.analizar(AFIJO_FUEGO, CAT)[0]
    muerto_pala = bool(a_pala and a_pala[0].get("muerto"))
    if muerto_brujo:
        fallos.append("el daño de fuego sale MUERTO para el Brujo")
    if not muerto_pala:
        fallos.append("el daño de fuego NO sale muerto para el Paladín (build física)")
    if not muerto_brujo and muerto_pala:
        print("  ok   el daño de fuego: muerto para el Paladín, vivo para el Brujo")

    # 3. Las estadísticas de un personaje no contaminan al otro
    V.cargar_clase("brujo")
    if V.GRUPOS:
        fallos.append(f"el Brujo arrastra {len(V.GRUPOS)} grupos de otro personaje: "
                      f"{list(V.GRUPOS)[:3]}")
    else:
        print("  ok   el Brujo arranca sin grupos de otro personaje")

    # 4. Con los grupos vacíos el cálculo no revienta: devuelve 'desconocido'
    try:
        afx, total = V.analizar(AFIJO_ESPINAS, CAT)
        if afx and afx[0].get("pct") is not None:
            fallos.append("con grupos vacíos inventa un porcentaje en vez de "
                          "declarar que no lo sabe")
        else:
            print("  ok   sin grupos, dice 'no lo sé' en vez de inventarse un %")
    except Exception as e:
        fallos.append(f"con grupos vacíos revienta: {type(e).__name__}: {e}")

    # 5. Los huecos declarados llegan hasta el valorador
    if len(V.HUECOS) < 4:
        fallos.append(f"el Brujo declara {len(V.HUECOS)} huecos, deberían ser 4+")
    else:
        print(f"  ok   el Brujo declara {len(V.HUECOS)} huecos conocidos")

    # 6. Volver al Paladín lo deja como estaba
    V.cargar_clase("paladin")
    if not V.GRUPOS.get("fuerza") or len(V.MUERTOS) < 5:
        fallos.append("volver al Paladín no restaura sus grupos y muertos")
    else:
        print(f"  ok   volver al Paladín restaura {len(V.GRUPOS)} grupos y "
              f"{len(V.MUERTOS)} muertos")

    # 7. Los valores de combate del Paladín no se cuelan en el Brujo
    V.cargar_clase("brujo")
    if V.GRUPOS.get("probabilidad de bloqueo") or V.GRUPOS.get("resolución máxima"):
        fallos.append("el Brujo hereda bloqueo o Resolución del Paladín")
    else:
        print("  ok   el Brujo no hereda bloqueo ni Resolución")

    V.cargar_clase(original or "paladin")
    # cargar_clase no debe tocar el disco si no se le pide: si lo hiciera, esta
    # misma prueba dejaria al tracker arrancando como Brujo.
    activa = (V.CLASES / "activa").read_text(encoding="utf-8").strip()
    if activa != (original or "paladin"):
        fallos.append(f"la prueba ha dejado clases/activa en {activa!r}")
    else:
        print(f"  ok   la prueba no ha cambiado la clase activa ({activa})")

    for f in fallos:
        print(f"  MAL  {f}")
    print(f"\n  {'PASA' if not fallos else 'FALLA'}")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
