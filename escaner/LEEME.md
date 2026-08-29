# Escáner de objetos — Diablo IV

Capturas con **F8** y te dice si el objeto que tienes delante **gana o pierde**
contra el que llevas puesto, y **por qué**.

## Lo que NO hace

No dibuja nada sobre el juego. No lee su memoria. No automatiza nada.
Hace **una captura de pantalla** —como la tecla Impr Pant— y la lee.
La ventana de resultados es una ventana normal, aparte.

## Instalación (una sola vez, en el PC de Windows)

1. Instala **Python** desde [python.org](https://www.python.org/downloads/) si no lo tienes.
   Marca **"Add Python to PATH"** en el instalador.
2. Abre una consola y ejecuta:

```
pip install winocr mss pillow
```

`winocr` usa el **motor de OCR que ya trae Windows**. No hace falta Tesseract
ni ningún binario externo, y lee español de fábrica.

## Uso

```
python escaner.py
```

| Tecla | Qué hace |
|---|---|
| **F9** | Marcas **una vez** la zona de pantalla donde salen los tooltips (arrastras un rectángulo). Se guarda en `config.json`; no hay que repetirlo. |
| **F8** | Con el objeto a la vista, escanea y analiza. |

El desplegable de arriba elige **contra qué hueco** comparar.

> **Marca la zona con F9 el primer día.** Leer solo el recuadro del tooltip en vez
> de la pantalla entera es mucho más rápido y mucho más preciso.

## La regla que aplica

Los afijos que **suman** entran en un grupo compartido, y su valor real depende
de **cuánto tienes ya en ese grupo**:

- Sumar 50 a un grupo de 4.047 → **+1,2%**
- Sumar 40 a un grupo de 11,5 → **+347%**

Los que **multiplican** (los que llevan `x`) se aplican enteros y no se diluyen.

> **Templa en el grupo más vacío, no en el más grande.**

## Mantener tus datos al día

Abre `escaner.py` y edita, arriba del todo:

- **`GRUPOS`** — los números de tu ficha de personaje. **Son la base de todo el
  cálculo.** Si están desfasados, las respuestas también.
- **`EQUIPADO`** — lo que llevas puesto por hueco, para la comparación.
- **`MUERTOS`** — afijos que no te aportan nada con esta build (daño en el tiempo,
  daño elemental, daño a lejanos…). El escáner los marca en rojo.

## Comprobar que funciona sin abrir el juego

```
python escaner.py --test
```

Analiza unos Puños del Destino de ejemplo y saca el desglose por consola.
Si eso funciona, la lógica está bien y cualquier problema es del OCR o de la zona.
