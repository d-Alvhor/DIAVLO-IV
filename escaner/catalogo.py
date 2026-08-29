#!/usr/bin/env python3
"""
Catálogo canónico de Diablo IV en español.

Los datos NO son míos: vienen de josdemmers/Diablo4Companion (MIT), que publica
el catálogo extraído del juego en 14 idiomas. Aquí solo se cargan y se indexan.

    datos/ItemTypes.esES.json   432 tipos de objeto -> hueco canónico
    datos/Affixes.esES.json     891 afijos con DescriptionClean ya limpio
    datos/Aspects.esES.json     524 aspectos legendarios con su descripción

Por qué importa: la línea de tipo de un tooltip ("Escudo único ancestral") es
literalmente una entrada del catálogo. Emparejar contra una lista cerrada de
nombres reales es mucho más robusto que adivinar con palabras clave, y corrige
solo los errores del OCR.

Actualizar (cuando cambie el parche):
    python catalogo.py --actualizar
"""

import re
import sys
import json
import difflib
import unicodedata
from pathlib import Path

DATOS = Path(__file__).with_name("datos")
IDIOMA = "esES"
BASE_URL = ("https://raw.githubusercontent.com/josdemmers/Diablo4Companion"
            "/master/D4Companion/Data")
FICHEROS = ["ItemTypes", "Affixes", "Aspects"]

# Tipo canónico del catálogo -> hueco de nuestra ficha
HUECO_DE_TIPO = {
    "helm": "Casco", "chest": "Peto", "gloves": "Guantes", "pants": "Pantalones",
    "boots": "Botas", "weapon": "Arma", "ranged": "Arma", "offhand": "Escudo",
    "amulet": "Amuleto", "ring": "Anillo",
}
# Los que existen pero no ocupan hueco de equipo en nuestra checklist
IGNORAR = {"charm", "rune", "horadricseal", "sigil", "witchersigil",
           "dungeonescalation", "horadricjewel", "bloodiedlair"}


def norm(s):
    s = unicodedata.normalize("NFD", str(s))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", s).strip().lower()


class Catalogo:
    def __init__(self, carpeta=DATOS):
        self.carpeta = Path(carpeta)
        self.tipos = {}      # nombre normalizado -> hueco
        self.afijos = {}     # descripcion normalizada -> texto original
        self.aspectos = {}   # nombre normalizado -> {nombre, descripcion}
        self._cargar()

    # ------------------------------------------------------------ carga
    def _leer(self, nombre):
        ruta = self.carpeta / f"{nombre}.{IDIOMA}.json"
        if not ruta.exists():
            raise FileNotFoundError(
                f"Falta {ruta.name}. Ejecuta:  python catalogo.py --actualizar")
        return json.loads(ruta.read_text(encoding="utf-8"))

    def _cargar(self):
        for x in self._leer("ItemTypes"):
            t = x.get("Type")
            if t in HUECO_DE_TIPO:
                self.tipos[norm(x["Name"])] = HUECO_DE_TIPO[t]
            elif t in IGNORAR:
                self.tipos[norm(x["Name"])] = None      # conocido, pero no es equipo

        for x in self._leer("Affixes"):
            d = (x.get("DescriptionClean") or "").strip()
            if d:
                self.afijos.setdefault(norm(d), d)

        for x in self._leer("Aspects"):
            n = (x.get("Name") or "").strip()
            if n:
                self.aspectos[norm(n)] = {"nombre": n,
                                          "descripcion": (x.get("Description") or "").strip()}

        self._tipos_k = list(self.tipos)
        self._afijos_k = list(self.afijos)
        self._aspectos_k = list(self.aspectos)

    # ------------------------------------------------------------ consultas
    def hueco(self, linea, umbral=0.86):
        """Línea de tipo de un tooltip -> hueco ('Casco', 'Arma'…) o None.
        Tolera el ruido del OCR emparejando contra los nombres reales."""
        n = norm(linea)
        if n in self.tipos:
            return self.tipos[n]
        # la línea puede traer cola ("Escudo único ancestral  900 de poder")
        for k, v in self.tipos.items():
            if n.startswith(k) or k in n:
                return v
        cerca = difflib.get_close_matches(n, self._tipos_k, n=1, cutoff=umbral)
        return self.tipos[cerca[0]] if cerca else None

    def afijo(self, texto, umbral=0.78):
        """Trozo de línea de afijo -> nombre canónico del catálogo, o None.
        Esto es lo que corrige los errores del OCR: 'de velocidd de ataqe'
        empareja con 'de velocidad de ataque' porque solo hay 891 posibles."""
        n = norm(texto)
        if not n:
            return None
        if n in self.afijos:
            return self.afijos[n]
        for k, v in self.afijos.items():
            if len(k) > 8 and (k in n or n in k):
                return v
        cerca = difflib.get_close_matches(n, self._afijos_k, n=1, cutoff=umbral)
        return self.afijos[cerca[0]] if cerca else None

    def aspecto(self, texto, umbral=0.8):
        """Detecta un aspecto legendario por su nombre."""
        n = norm(texto)
        for k, v in self.aspectos.items():
            if len(k) > 6 and k in n:
                return v
        cerca = difflib.get_close_matches(n, self._aspectos_k, n=1, cutoff=umbral)
        return self.aspectos[cerca[0]] if cerca else None

    def resumen(self):
        equipo = sum(1 for v in self.tipos.values() if v)
        return (f"{len(self.tipos)} tipos ({equipo} de equipo) · "
                f"{len(self.afijos)} afijos · {len(self.aspectos)} aspectos")


# ---------------------------------------------------------------- actualizar
def actualizar():
    import urllib.request
    DATOS.mkdir(exist_ok=True)
    for f in FICHEROS:
        nombre = f"{f}.{IDIOMA}.json"
        url = f"{BASE_URL}/{nombre}"
        print(f"  bajando {nombre}…", end=" ", flush=True)
        with urllib.request.urlopen(url, timeout=30) as r:
            (DATOS / nombre).write_bytes(r.read())
        print(f"{(DATOS / nombre).stat().st_size // 1024} KB")
    print("\n" + Catalogo().resumen())


# ---------------------------------------------------------------- pruebas
def autotest():
    c = Catalogo()
    print(" ", c.resumen(), "\n")

    # Lineas de tipo REALES de las capturas del jugador
    casos = [
        ("Yelmo legendario ancestral", "Casco"),
        ("Peto único ancestral", "Peto"),
        ("Guantes únicos ancestrales", "Guantes"),
        ("Guantes legendarios", "Guantes"),
        ("Pantalones únicos ancestrales", "Pantalones"),
        ("Botas legendarias ancestrales", "Botas"),
        ("Mangual legendario ancestral", "Arma"),
        ("Espada legendaria ancestral", "Arma"),
        ("Escudo único ancestral", "Escudo"),
        ("Amuleto único ancestral", "Amuleto"),
        ("Anillo legendario ancestral", "Anillo"),
        # con ruido del OCR
        ("Yelrno legendario ancestral", "Casco"),
        ("Escudo unico ancestral", "Escudo"),
        ("Anillo legendari0 ancestral", "Anillo"),
    ]
    ok = 0
    for linea, esp in casos:
        got = c.hueco(linea)
        marca = "ok " if got == esp else "MAL"
        ok += got == esp
        print(f"  {marca}  {linea:<34} -> {got}")
    print(f"\n  tipos: {ok}/{len(casos)}\n")

    # Afijos: incluidos errores tipicos de OCR
    afx = ["de velocidad de ataque", "de armadura total", "de vida maxima",
           "de velocidd de ataqe", "de dano de golpe critico", "de espinas",
           "de probabilidad de golpe critico"]
    ok2 = 0
    for a in afx:
        r = c.afijo(a)
        ok2 += bool(r)
        print(f"  {'ok ' if r else 'MAL'}  {a:<34} -> {r}")
    print(f"\n  afijos: {ok2}/{len(afx)}")

    asp = c.aspecto("Imprimido: Aspecto de Interdicción")
    print(f"\n  aspecto de ejemplo: {asp['nombre'] if asp else 'no encontrado'}")


if __name__ == "__main__":
    if "--actualizar" in sys.argv:
        actualizar()
    else:
        autotest()
