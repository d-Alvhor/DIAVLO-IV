---
name: d4-recon
description: Reinvestiga Diablo IV de cero y regenera la guía completa. Úsalo cuando cambie la temporada, cuando llegue un parche grande, o cuando la guía muestre el aviso de caducidad. Ancla al parche vivo, investiga por dominios, refuta de forma adversarial, reescribe solo las capas afectadas y regenera el HTML. Fail-closed.
---

# Reinvestigar y regenerar la guía

## Lo primero: tu conocimiento está caducado

Diablo IV cambia cada temporada. **Da por caducado todo lo que "sabes" del juego** y averígualo por web antes de escribir nada. Este proyecto nació precisamente porque las guías públicas presentan datos de hace tres temporadas como si fueran de hoy.

## Fase 1 — Anclaje temporal

Antes que nada, averigua por búsqueda web:

1. Qué **temporada** está viva, con su fecha de inicio y su fecha estimada de fin.
2. Qué **parche** está vivo, con su número de build y su fecha.
3. Si hay **PTR** corriendo, qué trae y **cuándo llega** (un PTR vivo significa que la temporada actual se acaba).

Actualiza `manifiesto.json` con `parche_actual` y `temporada_actual`. Todo lo demás cuelga de esto.

## Fase 2 — Investigación en abanico

Lanza un subagente por dominio, cada uno escribiendo a `investigacion/crudo/<dominio>.md`.
Los dominios están en los ficheros ya existentes de ese directorio: úsalos como plantilla.

**Declara de antemano qué dominios son obligatorios y cuáles opcionales.** Si falla cualquier obligatorio, se aborta la ejecución entera. Nada de umbrales tipo "3 de 13".

Instrucciones que todo investigador debe llevar:

- Cargar `WebSearch` y `WebFetch` vía `ToolSearch` antes de nada.
- **Fuentes vetadas para efectos y números:** fextralife, primagames, beebom, gamespot, segmentnext, studioloot, gamerguides, pcgamesn, mythicdrop. Publican datos de lanzamiento **sin fecha**, años después. Sirven para nomenclatura, nunca para valores.
- **Fuentes preferentes:** las notas oficiales de Blizzard, maxroll.gg/d4 e icy-veins.com/d4 — y solo sus páginas con fecha de actualización **dentro del parche vivo**. Ni Maxroll se salva: se ha detectado alguna página suya con sello de temporada actual sirviendo datos viejos.
- **La vía más fiable descubierta hasta ahora** es el fichero de datos que sirve el planificador de Maxroll (`assets-ng.maxroll.gg/d4-tools/game/data.min.json`). Es datamining, no una fuente primaria de Blizzard, y hay que declararlo como tal — pero contiene los campos reales del juego y ha resuelto contradicciones que ninguna web resolvía.
- Cada número debe llevar su URL al lado. Si no se ha visto escrito, se declara "no encontrado". **Un hueco declarado vale más que un número con buena pinta.**
- **Verificar el modelo, no solo los valores.** Si todas las fuentes usan el mismo marco conceptual, eso no lo valida: puede ser que todas lo hayan heredado de una versión muerta. Sospecha especialmente cuando las fuentes discrepan en las cifras pero coinciden en el marco.

## Fase 3 — Refutación adversarial

Por cada dominio crítico, un segundo agente intenta **refutar** al primero.

**Escribe en `investigacion/refutacion/<dominio>.md`, en fichero aparte. No edita el informe original.** El desacuerdo entre dos agentes es el dato más valioso del expediente; borrarlo es destruir evidencia.

El refutador comprueba: que ninguna fuente sea anterior al parche vigente, que no se haya colado ninguna fuente vetada respaldando un número, y que los nombres propios y los pares valor→efecto salgan de una cita literal.

## Fase 4 — Verificación de campo

**La pantalla del jugador gana a cualquier web.** Cuando una contradicción se pueda resolver mirando el juego, **pídeselo** en vez de buscar diez minutos más. Guarda su respuesta en `investigacion/campo/` con nivel de evidencia `oficial`.

Cierra cada ciclo con una lista corta de comprobaciones de un minuto que el jugador pueda hacer.

## Fase 5 — Redacción por capas

Reescribe **solo las capas afectadas**:

- `contenido/nucleo/` — ajustes, mando, conceptos, cross-play. Un hotfix **no** la toca. Siempre `parche: todas` y `temporada: todas`.
- `contenido/version/` — dificultad, builds, itemización, paragón, endgame. La toca un parche.
- `contenido/temporada/` — mecánica y ruta estacional. Muere con la temporada.

El dialecto markdown está descrito en el `README.md` y lo impone `construir.mjs`.

**Al cambiar de temporada:** actualiza el manifiesto, mueve `temporada/` a `archivo/`, y marca `estado: archivado` en **todo** documento con la temporada vieja, **esté en la carpeta que esté** — un capítulo de builds puede estar atado al parche *y* a la mecánica estacional a la vez, y la carpeta no lo salva.

## Fase 6 — Gate

```
node construir.mjs
```

**Si falla, no hay build, no hay commit y no hay publicación.** No se rellena un hueco con el contenido anterior fingiendo que sigue vigente: ese es exactamente el fallo que este proyecto existe para no cometer.

## Fase 7 — Publicación

Commit y `push` explícito. **Un commit local no es publicar.**

## La regla que gobierna todo lo demás

**No publiques lo incierto en formato de certeza.** Una tabla limpia se lee como un hecho aunque lleve una advertencia debajo; la advertencia al final no anula la tabla del principio. El nivel de confianza va **en la misma línea que el dato**, o no va.
