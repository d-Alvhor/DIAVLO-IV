#!/usr/bin/env python3
"""Diagnóstico de la captura. Se ejecuta EN TU SESIÓN, no por SSH.

Una sesión SSH de Windows está aislada del escritorio y reporta 1024x768, así
que desde fuera no se puede ver tu pantalla de verdad. Esto sí.

Mide DOS veces a propósito: antes y después de declararse consciente del DPI.
La diferencia entre las dos ES el problema — si Windows está a 125%, el «antes»
es lo que veía la app rota y el «después» lo que ve ahora.

    python revisar.py                 diagnóstico
    python revisar.py --borrar-zona   vuelve a mirar la pantalla entera
"""
import sys
import json
import ctypes
import ctypes.wintypes                    # lo necesita GetDpiForMonitor
from pathlib import Path

CONFIG = Path(__file__).with_name("config.json")


def medir():
    """Lo que el sistema dice AHORA MISMO sobre la pantalla."""
    gm = ctypes.windll.user32.GetSystemMetrics
    d = {"win": (gm(0), gm(1)), "virtual": (gm(78), gm(79)), "mss": None,
         "tk": None, "monitores": []}
    try:
        import mss
        with mss.mss() as s:
            d["monitores"] = [(m["width"], m["height"], m["left"], m["top"])
                              for m in s.monitors]
            shot = s.grab(s.monitors[1])
            d["mss"] = (shot.size.width, shot.size.height)
    except Exception as e:
        d["mss"] = f"ERROR {e}"
    return d


def consciente():
    for llamada in (lambda: ctypes.windll.shcore.SetProcessDpiAwareness(2),
                    lambda: ctypes.windll.user32.SetProcessDPIAware()):
        try:
            llamada()
            return True
        except Exception:
            continue
    return False


def fila(etiqueta, a, b):
    igual = "" if a != b else "   (igual)"
    print(f"  {etiqueta:<26} {str(a):<16} -> {str(b)}{igual}")


def main():
    print("Diagnóstico de captura — Diablo IV\n" + "=" * 62)
    antes = medir()
    ok = consciente()
    despues = medir()

    print(f"  se declara consciente del DPI: {'sí' if ok else 'NO (mala señal)'}\n")
    print(f"  {'':<26} {'sin DPI (roto)':<16} -> con DPI (bueno)")
    fila("pantalla según Windows", f"{antes['win'][0]}x{antes['win'][1]}",
         f"{despues['win'][0]}x{despues['win'][1]}")
    fila("captura real de mss",
         f"{antes['mss'][0]}x{antes['mss'][1]}" if isinstance(antes["mss"], tuple) else antes["mss"],
         f"{despues['mss'][0]}x{despues['mss'][1]}" if isinstance(despues["mss"], tuple) else despues["mss"])
    fila("escritorio virtual", f"{antes['virtual'][0]}x{antes['virtual'][1]}",
         f"{despues['virtual'][0]}x{despues['virtual'][1]}")

    try:
        h = ctypes.windll.user32.MonitorFromPoint(ctypes.wintypes.POINT(0, 0), 1)
        x, y = ctypes.c_uint(), ctypes.c_uint()
        ctypes.windll.shcore.GetDpiForMonitor(h, 0, ctypes.byref(x), ctypes.byref(y))
        print(f"\n  escalado de Windows        : {x.value / 96:.0%}")
    except Exception:
        pass

    if len(despues["monitores"]) > 2:
        print(f"\n  tienes {len(despues['monitores']) - 1} monitores:")
        for i, (w, h_, l, t) in enumerate(despues["monitores"][1:], 1):
            print(f"      monitor {i}: {w}x{h_} en ({l}, {t})")
        print("      La app captura el PRIMARIO. Juega en él, o marca Zona.")

    print()
    z = None
    if CONFIG.exists():
        try:
            z = json.loads(CONFIG.read_text()).get("region")
        except Exception:
            pass
    if z and isinstance(despues["mss"], tuple):
        area = z[2] * z[3] / max(despues["mss"][0] * despues["mss"][1], 1)
        print(f"  ⚠ ZONA GUARDADA            : {z[2]}x{z[3]} px en ({z[0]}, {z[1]})")
        print(f"    Cubre el {area:.0%} de la pantalla; lo de fuera es invisible.")
        print(f"    Quítala con:  python revisar.py --borrar-zona")
    else:
        print("  zona guardada              : ninguna (bien, mira toda la pantalla)")


if __name__ == "__main__":
    if "--borrar-zona" in sys.argv:
        if CONFIG.exists():
            CONFIG.unlink()
            print("Zona borrada. La app vuelve a mirar la pantalla entera.")
        else:
            print("No había zona guardada.")
    else:
        main()
