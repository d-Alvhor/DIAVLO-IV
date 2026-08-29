#!/usr/bin/env python3
"""El capturador, ejecutado de verdad, a varias resoluciones.

Existe porque el capturador se publicó usando T.Image.LANCZOS —un atributo que
no existe, porque tracker.py importa PIL dentro de las funciones— y reventaba
con AttributeError en el primer ciclo, antes de guardar un solo panel.
Compilaba perfectamente. Solo lo pilla ejecutarlo.

El OCR se sustituye por un doble que devuelve las líneas REALES de una captura
del corpus, reescaladas al tamaño que se le pida.
"""
import sys
import json
import types
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent))

FIX = json.loads((AQUI / "fixtures.json").read_text(encoding="utf-8"))
CAP = next(c for c in FIX if any("Yelmo legendario" in l["t"] for l in c["l"]))
BASE = 4072.0          # las cajas del fixture viven en 2036 px escalado x2

RESOLUCIONES = [(2036, 1145), (2560, 1440), (3840, 2160), (1920, 1080)]


def doble_de_ocr(im, idioma):
    k = im.width / BASE
    return {"lines": [{"text": l["t"], "words": [{"bounding_rect": {
                "x": l["x"] * k, "y": l["y"] * k,
                "width": (l["x2"] - l["x"]) * k,
                "height": (l["y2"] - l["y"]) * k}}]}
            for l in CAP["l"]]}


def main():
    w = types.ModuleType("winocr")
    w.recognize_pil_sync = doble_de_ocr
    sys.modules["winocr"] = w
    import capturador as C
    from PIL import Image

    fallos = []
    for ancho, alto in RESOLUCIONES:
        pans = C.paneles_interesantes(Image.new("RGB", (ancho, alto), (20, 18, 16)))
        casco = [p for p in pans if p["hueco"] == "Casco"]
        if not casco:
            fallos.append(f"{ancho}x{alto}: no encuentra el tooltip del casco")
            continue
        x1, y1, x2, y2 = casco[0]["caja"]
        if not (0 <= x1 < x2 <= ancho and 0 <= y1 < y2 <= alto):
            fallos.append(f"{ancho}x{alto}: recorte fuera de la imagen {casco[0]['caja']}")
        print(f"  ok  {ancho}x{alto:<5} recorte {x2-x1}x{y2-y1} px  "
              f"{casco[0]['nombre'][:32]}")

    w.recognize_pil_sync = lambda im, i: (_ for _ in ()).throw(RuntimeError("boom"))
    if C.paneles_interesantes(Image.new("RGB", (2560, 1440))) != []:
        fallos.append("un OCR que revienta debería devolver [] , no propagar")
    else:
        print("  ok  un fallo del OCR no tumba el bucle")

    for f in fallos:
        print(f"  MAL  {f}")
    print(f"\n  {'PASA' if not fallos else 'FALLA'}")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
