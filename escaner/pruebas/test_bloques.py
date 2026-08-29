#!/usr/bin/env python3
"""Banco de pruebas con capturas REALES del juego.

fixtures.json son 162 capturas de una sesión de verdad, con cada línea que leyó
el OCR y su caja. Es lo único que dice si el agrupado funciona: el texto ya
lo lee bien: lo que fallaba era juntarlo.
"""
import sys, json, re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import tracker as T

FIX = json.load(open(Path(__file__).with_name("fixtures.json"), encoding="utf-8"))
AFIJO = re.compile(r"^\s*[+\-]?\s*[\d.,]+\s*%?\s+de\s+|x\d+%|^\s*\+", re.I)


def bloques_de(cap):
    ls = [{"texto": l["t"], "x": l["x"], "y": l["y"], "x2": l["x2"],
           "y2": l["y2"], "h": l["y2"] - l["y"]} for l in cap["l"]]
    return T.agrupar(ls)


def medir():
    con_objeto = afijos_por_objeto = objetos = 0
    basura, sin_afijos, ejemplos = [], 0, {}
    for cap in FIX:
        vistos = []
        for b in bloques_de(cap):
            r = T.identificar(b)
            if not r or r[0] != "objeto":
                continue
            _, hueco, nombre, texto = r
            objetos += 1
            n = sum(1 for l in texto.splitlines() if AFIJO.search(l))
            afijos_por_objeto += n
            if n == 0:
                sin_afijos += 1
            if T.norm(nombre) in T.CHROME_N or len(nombre) < 5:
                basura.append((cap["f"], nombre))
            vistos.append(hueco)
            ejemplos.setdefault(hueco, (nombre, n, texto))
        if vistos:
            con_objeto += 1
    return {"capturas": len(FIX), "con_objeto": con_objeto, "objetos": objetos,
            "afijos_medios": afijos_por_objeto / max(objetos, 1),
            "sin_afijos": sin_afijos, "basura": basura, "ejemplos": ejemplos}


def caso_yelmo():
    """El caso concreto que falla: el casco sale a +0% porque sus afijos
    acaban en otro bloque."""
    for cap in FIX:
        ts = [l["t"] for l in cap["l"]]
        if not (any("Yelmo legendario" in t for t in ts)
                and any("espinas" in t for t in ts)):
            continue
        for b in bloques_de(cap):
            r = T.identificar(b)
            if r and r[1] == "Casco":
                t = r[3]
                return {"captura": cap["f"], "nombre": r[2],
                        "vida": "vida máxima" in t, "espinas": "espinas" in t,
                        "resolucion": "Resolución" in t,
                        "lineas": len(t.splitlines())}
        return {"captura": cap["f"], "nombre": None}
    return None


if __name__ == "__main__":
    m = medir()
    print(f"  capturas con algún objeto : {m['con_objeto']}/{m['capturas']}")
    print(f"  objetos identificados     : {m['objetos']}")
    print(f"  líneas de afijo por objeto: {m['afijos_medios']:.1f}")
    print(f"  objetos SIN ningún afijo  : {m['sin_afijos']}  <- deben ser pocos")
    print(f"  nombres basura            : {len(m['basura'])}  <- debe ser 0")
    for f, n in m["basura"][:5]:
        print(f"      {n!r}")
    print("\n  un ejemplo por hueco:")
    for h, (n, na, _) in sorted(m["ejemplos"].items()):
        print(f"      {h:<11} {n[:44]:<46} {na} afijos")
    y = caso_yelmo()
    print(f"\n  CASO YELMO: {y}")
    ok = (y and y.get("vida") and y.get("espinas")
          and not m["basura"] and m["afijos_medios"] >= 3)
    print(f"\n  {'PASA' if ok else 'FALLA'}")
    sys.exit(0 if ok else 1)
