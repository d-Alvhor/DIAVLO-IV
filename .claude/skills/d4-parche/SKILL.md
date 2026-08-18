---
name: d4-parche
description: Chequeo rápido tras un hotfix de Diablo IV. Responde a "¿me han roto la build?" en minutos, sin reinvestigar nada. Compara el parche vivo contra el manifiesto, lee solo las notas oficiales y toca únicamente los capítulos afectados.
---

# ¿Me han roto la build?

Esto **no** es una reinvestigación. Es el chequeo de cinco minutos que se hace cuando cae un parche y quieres saber si algo de la guía ha dejado de ser cierto. Para el trabajo completo, `d4-recon`.

## 1 · Qué parche hay hoy

Busca el número de build vivo y compáralo con `parche_actual` de `manifiesto.json`.

Si coinciden, **no hay nada que hacer**. Dilo y termina; no inventes trabajo.

## 2 · Lee solo las notas oficiales

Las **notas de parche de Blizzard**, y nada más. Ninguna guía, ningún agregador, ningún vídeo. En un chequeo de parche solo cuenta la fuente primaria.

Si hay varios parches entre el manifiesto y hoy, **léelos todos**: es fácil saltarse uno intermedio, y ha pasado.

## 3 · Clasifica cada cambio

| Toca | Ejemplos | Capa afectada |
|---|---|---|
| Nada de la guía | Cosméticos, arreglos de audio, otras clases | ninguna |
| Un capítulo concreto | Un aspecto del nigromante, un jefe, un material | `version/` |
| La temporada | Mecánica estacional, journey, recompensas | `temporada/` |
| Los cimientos | Árbol de habilidades, sistema de dificultad, itemización | `version/` entera, y revisa `nucleo/` |

**`nucleo/` casi nunca se toca.** Si crees que sí, párate y comprueba: normalmente es que el cambio va a `version/`.

## 4 · Presta atención especial al nigromante y al dúo

El lector es un nigromante que juega en dúo con juego base. Busca explícitamente en las notas:

- cambios de **nigromante**, esbirros, Libro de los Muertos, Esencia y cadáveres;
- cambios de **grupo, comercio, escalado por número de jugadores** o cross-play;
- cambios que **muevan la frontera entre juego base y expansión** en cualquier dirección.

## 5 · Toca lo justo

Actualiza solo los capítulos afectados. En cada uno que toques, sube `verificado` a hoy y `parche` al nuevo. Actualiza `manifiesto.json`.

**No subas la fecha de verificación de un capítulo que no has revisado de verdad.** Esa fecha es una promesa al lector.

## 6 · Gate y publicación

```
node construir.mjs
```

Si falla, no hay commit ni publicación. Luego commit y `push` explícito.

## 7 · Informa en una línea

Al terminar, dile al jugador **si le han roto la build o no**, en una frase, y qué capítulos se han movido. Es la pregunta que ha venido a hacer.

Si el parche cambia algo de su build activa, **dilo lo primero**, antes que cualquier otro cambio.
