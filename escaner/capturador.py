#!/usr/bin/env python3
"""Capturador para leer la build con Claude.

Cambio de reparto respecto al tracker: aquí el OCR NO decide nada. Solo sirve
para ENCONTRAR el recuadro del tooltip en la pantalla. Quien lee lo que pone
dentro es Claude, mirando el recorte. Así deja de importar que el OCR se coma
letras, y funciona con objetos que necesitan scroll: si pasas dos veces, se
guardan los dos trozos y se juntan al leerlos.

    python capturador.py            cada 5 s, hasta Ctrl+C
    python capturador.py --cada 3   otro intervalo

Guarda en  sesion/  solo lo NUEVO: si el panel ya se guardó, se salta.
"""
import re
import sys
import time
import json
import hashlib
from pathlib import Path
from datetime import datetime

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tracker as T

SESION = Path(__file__).with_name("sesion")
MARGEN = 14         # píxeles de aire alrededor del recorte
ANCHO_MAX = 1150    # se reduce el recorte a esto: de sobra para leerlo


def paneles_interesantes(img):
    """Devuelve los recortes que parecen un tooltip de objeto o de habilidad."""
    import winocr
    g = T.escalar_para_ocr(img)
    escala = g.width / max(img.width, 1)      # el factor REAL, no una constante
    try:
        res = winocr.recognize_pil_sync(g, "es-ES")
    except Exception as e:
        # una lectura fallida no puede tumbar la sesión entera
        print(f"  (lectura saltada: {type(e).__name__})")
        return []
    out = []
    for b in T.agrupar(T._lineas_con_caja(res), cajas=True):
        texto = b["texto"]
        if T.es_propia(texto):
            continue
        lineas = [l for l in texto.splitlines() if l.strip()]
        if len(lineas) < 5:
            continue
        r = T.identificar(texto)
        # también valen los que el OCR no supo clasificar pero tienen pinta:
        # si hay varias líneas con números, es una ficha de algo
        numericas = sum(1 for l in lineas if re.search(r"\d", l))
        if not r and numericas < 4:
            continue
        caja = [max(0, b["x"] / escala - MARGEN), max(0, b["y"] / escala - MARGEN),
                min(img.width, b["x2"] / escala + MARGEN),
                min(img.height, b["y2"] / escala + MARGEN)]
        if caja[2] - caja[0] < 120 or caja[3] - caja[1] < 120:
            continue
        out.append({"caja": [int(c) for c in caja], "texto": texto,
                    "clase": r[0] if r else "?", "hueco": r[1] if r else None,
                    "nombre": r[2] if r else None})
    return out


def firma(texto):
    """Dos lecturas del mismo panel no son idénticas (el OCR baila). Se firma
    con las letras que sobreviven, para que casen igual."""
    n = re.sub(r"[^a-záéíóúñ]", "", T.norm(texto))
    return hashlib.sha1(n[:220].encode()).hexdigest()[:12]


def main():
    cada = 5.0
    if "--cada" in sys.argv:
        cada = float(sys.argv[sys.argv.index("--cada") + 1])
    SESION.mkdir(exist_ok=True)
    for viejo in SESION.glob("*"):
        viejo.unlink()
    vistas, n, manifiesto = set(), 0, []
    a, b = T.pantalla()
    aviso = ""
    if T.ESCALADO > 1.05:
        aviso = f" · escalado de Windows {T.ESCALADO:.0%}"
    print(f"Pantalla: {a}×{b} px{aviso}")
    if a and a < 2000:
        print("  ⚠ Eso parece poco para tu monitor. Ejecuta  python revisar.py")
    print(f"Capturando cada {cada:g} s. Pasa el ratón por cada objeto y cada "
          f"habilidad.\nSi un objeto no cabe, hazle scroll y espera un momento: "
          f"se guardan los dos trozos.\nCtrl+C para parar.\n")
    try:
        while True:
            try:
                img = T.capturar()
                encontrados = paneles_interesantes(img)
            except KeyboardInterrupt:
                raise
            except Exception as e:
                print(f"  (ciclo saltado: {type(e).__name__}: {e})")
                time.sleep(cada)
                continue
            for pan in encontrados:
                f = firma(pan["texto"])
                if f in vistas:
                    continue
                vistas.add(f)
                n += 1
                rec = img.crop(pan["caja"])
                if rec.width > ANCHO_MAX:
                    alto = int(rec.height * ANCHO_MAX / rec.width)
                    rec = rec.resize((ANCHO_MAX, alto), Image.LANCZOS)
                nom = f"{n:03d}-{pan['hueco'] or pan['clase']}.png"
                nom = re.sub(r"[^\w\-.]", "_", nom)
                rec.save(SESION / nom)
                manifiesto.append({"fichero": nom, "clase": pan["clase"],
                                   "hueco": pan["hueco"], "ocr": pan["nombre"],
                                   "px": [rec.width, rec.height]})
                (SESION / "manifiesto.json").write_text(
                    json.dumps(manifiesto, ensure_ascii=False, indent=1),
                    encoding="utf-8")
                print(f"  [{n:3d}] {nom:<28} {pan['nombre'] or '(sin clasificar)'}")
            time.sleep(cada)
    except KeyboardInterrupt:
        print(f"\nParado. {n} paneles guardados en {SESION}\\")
        print("Dile a Claude: «ya está» y los leo.")


if __name__ == "__main__":
    main()
