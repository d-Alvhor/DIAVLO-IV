# Tracker de builds — perfiles de clase y captura anclada al cursor

Fecha: 15 de septiembre de 2026 · Parche 3.2.1 · Temporada 15

## Por qué

El tracker funciona, pero está calibrado para un Paladín de espinas de la
Season 14. Para un Brujo de fuego tiene dos problemas, y el primero es grave.

**Miente.** `valorar.py` lleva dentro una lista de afijos muertos escrita a
mano para esa build:

    MUERTOS = {
        "daño de fuego": "eres físico",
        "daño con fuego": "eres físico",
        ...
    }

Un Brujo es una clase de fuego. Tal cual está, el tracker le diría que sus
mejores afijos no le sirven. Lo mismo con `mis_stats.json` (5.165 de Fuerza de
otro personaje, que falsea todos los porcentajes) y con `en_combate.json`
(Resolución 29 y bloqueo 100, que el Brujo ni tiene).

**Lee el sitio equivocado.** Cada 0,7 s captura la pantalla entera —3456×2168—
y la escala a 4000 px para buscar un tooltip que está a 300 px del cursor.

## Qué se construye

### 1. Perfiles de clase

Una carpeta `clases/` con un fichero por clase:

    clases/paladin.json     los datos actuales, migrados tal cual
    clases/brujo.json       nuevo, con los grupos vacíos

Cada perfil lleva:

| Campo | Qué es | De dónde sale |
|---|---|---|
| `grupos` | las estadísticas de la hoja de personaje | botón Ficha |
| `combate` | lo que la ficha mide en reposo y en combate vale otra cosa | el jugador |
| `muertos` | afijos que no aportan nada a ESTA build | evidencia, no suposición |
| `huecos` | cifras conocidas como desconocidas, que el tracker pide | investigación |

`valorar.py` deja de tener constantes de clase: carga el perfil activo. Los
perfiles capturados se separan por clase (`perfiles/brujo/yo_*.json`), así que
el Paladín queda intacto y se puede comparar una build contra otra.

**`brujo.json` nace con `muertos` vacío.** No se ha jugado un Brujo todavía.
Marcar un afijo como muerto es una afirmación, y afirmar sin evidencia es el
fallo que este proyecto existe para no cometer.

Lo que sí lleva de salida son los **huecos** que dejó la investigación, porque
saber qué no sabes vale más que rellenarlo a ojo:

    "huecos": {
      "maximo de ira":        "la variante Pecado lo sube un 50%, ¿sobre qué base?",
      "maximo de dominio":    "igual",
      "enfriamiento de metamorfosis":
                              "DISPUTA: Icy Veins dice 5 s, Wowhead dice 15 s",
      "drenaje de dominio en forma demonica":
                              "1/s por Demonio Mayor cercano, sin verificar en 3.2.1"
    }

El botón **Ficha** los rellena. Mientras estén vacíos, el tracker lo dice en vez
de calcular sobre un número inventado.

### 2. Captura anclada al cursor

El tooltip sale siempre pegado al cursor. El bucle pasa de sondear a reaccionar:

    vigila la posición del ratón (GetCursorPos, barato)
    cuando lleva ~250 ms quieto Y está en un sitio nuevo:
        captura un recuadro centrado en el cursor
        OCR solo de ese recuadro
    mientras el ratón se mueve: no lee nada

El recuadro se recorta contra los bordes del monitor activo. Si N ciclos
seguidos no encuentran nada, vuelve a pantalla completa como red de seguridad.

Esto no es un intercambio entre velocidad y coste: es las dos cosas. Menos
píxeles por lectura permite leer más a menudo, y el texto queda más grande para
el mismo coste de OCR, así que **además lee mejor**.

Se conserva lo que ya funciona: el borrado del rectángulo de la propia ventana,
la detección del monitor donde está el ratón, el agrupado por columnas, y el
reflujo de líneas partidas.

### 3. Catálogo al parche vivo

`python catalogo.py --actualizar` para traer los objetos del 3.2.1, incluidos
los nueve únicos legado nuevos. Sin esto no reconoce lo que caiga.

## Qué NO se hace

- **No se inventan los afijos muertos del Brujo** a partir de las notas del
  parche. Se rellenan cuando haya evidencia.
- **No se arrastran las estadísticas del Paladín** al perfil nuevo.
- No se toca la lógica de agrupado ni de valoración, que están probadas contra
  162 capturas reales.

## Cómo se comprueba

Las siete pruebas actuales tienen que seguir pasando. Se añaden dos:

| Prueba | Qué comprueba |
|---|---|
| `test_clases.py` | que cargar el perfil del Brujo NO trae afijos muertos del Paladín, que los grupos vacíos no rompen el cálculo, y que un afijo de fuego puntúa positivo para el Brujo y cero para el Paladín |
| `test_cursor.py` | que el recuadro se recorta bien contra los bordes en las cuatro esquinas, que el disparo por ratón parado no se pierde eventos, y que la red de pantalla completa entra cuando N ciclos fallan |

Y la de siempre: **ejecutarlo, no compilarlo.** El capturador se publicó una vez
usando un atributo que no existía; compilaba y reventaba en el primer ciclo.
