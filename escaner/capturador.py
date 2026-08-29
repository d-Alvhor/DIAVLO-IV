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
VALOR = re.compile(r"[+\-]?\s*[\d][\d.,]*\s*%?")
# Una fila de la hoja de personaje: etiqueta y número, sin '+' delante y sin
# corchetes de rango. Es lo que la distingue de un afijo de objeto.
FILA_FICHA = re.compile(r"^[A-Za-zÁÉÍÓÚÑáéíóúñ][\w áéíóúñÁÉÍÓÚÑ]{3,42}"
                        r"\s+[\d][\d.,]*\s*%?$")
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
        clase = r[0] if r else None
        # La hoja de personaje: muchas filas que son SOLO un número. No es un
        # objeto ni una habilidad, pero es justo lo que hay que leer, y leerlo
        # como imagen evita todo el problema de emparejar etiqueta con valor.
        filas = sum(1 for l in lineas
                    if VALOR.fullmatch(l.strip()) or FILA_FICHA.match(l.strip()))
        if not r and filas >= 6:
            clase = "ficha"
        elif not r:
            numericas = sum(1 for l in lineas if re.search(r"\d", l))
            if numericas < 4:
                continue
            clase = "?"
        caja = [max(0, b["x"] / escala - MARGEN), max(0, b["y"] / escala - MARGEN),
                min(img.width, b["x2"] / escala + MARGEN),
                min(img.height, b["y2"] / escala + MARGEN)]
        if caja[2] - caja[0] < 120 or caja[3] - caja[1] < 120:
            continue
        out.append({"caja": [int(c) for c in caja], "texto": texto,
                    "clase": clase, "hueco": r[1] if r else None,
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
    aviso = f" · escalado de Windows {T.ESCALADO:.0%}" if T.ESCALADO > 1.05 else ""
    print(f"Pantalla donde está el ratón: {a}×{b} px{aviso}")
    ms = T.monitores()[1:]
    if len(ms) > 1:
        print("  " + str(len(ms)) + " monitores: "
              + ", ".join(f"{m['width']}×{m['height']}" for m in ms)
              + " — capturo donde esté el ratón, así que déjalo en el del juego.")
    print(f"""
Capturando cada {cada:g} s. Haz esto, sin prisa:

  1. Abre la hoja de personaje (C) y entra en «Estadísticas y materiales».
     Baja despacio por toda la lista.
  2. Vuelve al equipo y pasa el ratón por las 10 piezas.
     Lo que no quepa: scroll y espera un segundo.
  3. Pasa el ratón por las 6 habilidades.

No tienes que hacer ni una captura: esto recorta solo lo que hace falta.
Ctrl+C para parar.
""")
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
