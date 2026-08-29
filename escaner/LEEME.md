# Tracker de builds — Diablo IV

Le das a **Trackear**, dices si es tu personaje o un rival, y va mirando la pantalla.
Tú pasas el ratón por cada objeto; la checklist se rellena sola y **te dice cuánto
aporta cada pieza y si gana a la del otro perfil**.

## Lo que NO hace

No dibuja sobre el juego. No lee su memoria. No automatiza teclado ni ratón.
Hace capturas de pantalla y las lee. La ventana es una ventana normal, aparte.

> ⚠️ Blizzard no autoriza herramientas de terceros ni tiene lista blanca: la EULA
> es deliberadamente amplia y prohíbe software que "lea información generada por
> la Plataforma". No hay ningún caso documentado y sostenido de baneo por
> captura + OCR en Diablo IV, pero **nadie puede garantizarte nada**. Riesgo asumido.

## Instalación (una vez, en el PC de Windows)

1. [Python](https://www.python.org/downloads/) — marca *"Add Python to PATH"*
2. En una consola:

```
pip install winocr mss pillow
```

`winocr` usa el **motor de OCR que ya trae Windows**. Sin Tesseract, sin binarios,
y lee español de fábrica.

## Uso

```
python tracker.py
```

1. **▶ Trackear** → eliges **Soy yo** o **Un rival** (con su nombre)
2. Pasas el ratón por cada objeto y cada habilidad
3. La checklist se marca sola: `○` → `●` con el nombre y **cuánto aporta**
4. Si ya tienes guardado el otro perfil, te compara **hueco a hueco al vuelo**
5. Termina cuando lo ha visto todo (10 huecos + 6 habilidades) y guarda el perfil

**Botón Zona:** casi nunca hace falta — la app separa los paneles de una
pantalla entera ella sola. Solo sirve para acelerar en pantallas muy grandes, y
**una zona mal puesta hace que no vea media pantalla**. «Zona ✕» la quita.

Si algo va raro, lo primero:

```
python revisar.py
```

Mide la pantalla dos veces, antes y después de declararse consciente del DPI.
Si los dos números no coinciden, Windows está escalando (125%, 150%…) y la
diferencia es exactamente lo que se estaba perdiendo.

Los perfiles se guardan en `perfiles/yo_*.json` y `perfiles/rival_*.json`, con el
texto completo de cada pieza.

## Las tres piezas

| Fichero | Qué hace |
|---|---|
| `catalogo.py` | Carga el catálogo canónico en español |
| `valorar.py` | Calcula el aporte real de cada afijo y compara piezas |
| `tracker.py` | Captura, checklist en vivo y perfiles |
| `capturador.py` | Recorta los tooltips para que los lea Claude |
| `revisar.py` | Diagnóstico de pantalla, DPI y zona |

### El catálogo no es mío

Viene de [josdemmers/Diablo4Companion](https://github.com/josdemmers/Diablo4Companion) (MIT),
que publica el catálogo extraído del juego en 14 idiomas:

```
432 tipos de objeto  ·  891 afijos  ·  524 aspectos
```

**Y eso es lo que corrige el OCR.** Como solo hay 432 tipos y 891 afijos posibles,
una lectura sucia empareja sola con la buena:

| El OCR lee | Se resuelve como |
|---|---|
| `Yelrno legendario ancestral` | **Casco** |
| `Anillo legendari0 ancestral` | **Anillo** |
| `de velocidd de ataqe` | *de velocidad de ataque* |

Actualizarlo cuando cambie el parche:

```
python catalogo.py --actualizar
```

### La regla que aplica el valorador

Un afijo que **suma** entra en un grupo compartido, y su valor real depende de
cuánto tienes ya ahí:

```
+50 sobre un grupo de 4.047  ->    +1,2%
+40 sobre un grupo de    11,5 ->  +347%
```

Un afijo que **multiplica** (los que llevan `x`) se aplica entero y no se diluye.

> **Templa en el grupo más vacío, no en el más grande.**

## Mantener tus datos al día

**`mis_stats.json`** (créalo al lado de `valorar.py`) sobrescribe los grupos sin
tocar el código. Son **la base de todo el cálculo**: si están desfasados, las
respuestas también.

```json
{
  "daño de golpe crítico": 4047.5,
  "daño a enemigos cercanos": 75.5,
  "vida máxima": 13100
}
```

En `valorar.py` está además `MUERTOS`: afijos que no aportan nada a esta build
(daño en el tiempo, elemental, a enemigos lejanos). El tracker los marca.

## Comprobar que funciona sin abrir el juego

```
python catalogo.py               # 14/14 tipos y 7/7 afijos, con ruido metido a mano
python valorar.py                # valoración, comparación y control contra sí mismo
python tracker.py --test         # identificación + sesión simulada
python pruebas/test_bloques.py   # 162 capturas REALES de una partida
python pruebas/test_capturador.py  # el capturador, ejecutado, a cuatro resoluciones
```

Las dos últimas son las que valen. `test_bloques` corre sobre capturas de verdad
—con el panel de mercenarios estorbando y tooltips tapados a medias— y exige
0 nombres basura y ≥3 líneas de afijo por objeto. `test_capturador` lo **ejecuta**
con el OCR simulado: el capturador se publicó una vez usando un atributo que no
existía, compilaba de maravilla y reventaba en el primer ciclo.

## Lo que NO está verificado

**El OCR contra un tooltip real del juego.** Todo lo medido usa texto escrito a
mano o imágenes generadas. El listón para fiarse sería: **20-30 capturas reales
variadas, ≥95% de líneas aceptadas y cero afijos o números erróneos aceptados en
silencio.** Está sin intentar.
