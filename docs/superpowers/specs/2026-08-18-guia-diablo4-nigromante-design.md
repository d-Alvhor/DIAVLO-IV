# Diseño — Guía y agente de Diablo IV para nigromante (Season 14)

**Fecha:** 2026-08-18
**Estado:** propuesto, pendiente de revisión del usuario

## 1. Problema

Un jugador principiante de Diablo IV quiere jugar **nigromante** en la **Season 14
("Season of Death Awakening", viva desde el 30/06/2026, parche 3.1.3)** y optimizar al
máximo, con ambición de leaderboard. Juega **en dúo** con su pareja, también principiante
y también nigromante. Él en **PC**, ella/él en **PS5** (cross-play).

**Restricción dominante: sólo tiene el juego base.** No posee *Vessel of Hatred* ni
*Lord of Hatred*. Casi todas las guías públicas asumen las expansiones sin decirlo.

**El problema real no es la falta de información, es que la información pública está
podrida de contenido caducado.** Diablo IV cambia cada temporada; las guías de Google
mezclan la Season 11 con la 14 sin fecharse. Un principiante no tiene forma de distinguirlas.

## 2. Qué se construye

Dos artefactos en un repo público, `github.com/d-Alvhor/DIAVLO-IV`:

1. **La guía** — un único `index.html` autocontenido, en español, navegable desde el móvil.
2. **El agente** — una skill de Claude Code que reinvestiga y regenera la guía cuando el
   juego cambie (parche, temporada nueva), sin depender de CI ni de API keys de pago.

## 3. Arquitectura

```
DIAVLO-IV/
├─ index.html            # artefacto final. Autocontenido, offline, sin red.
├─ contenido/            # FUENTE DE VERDAD del texto. Un .md por capítulo.
│   ├─ 00-empezar-aqui.md
│   ├─ 01-ajustes-pc.md
│   ├─ 02-ajustes-ps5.md
│   ├─ 03-dificultad.md
│   ├─ 04-leveling.md
│   ├─ 05-builds.md
│   ├─ 06-itemizacion.md
│   ├─ 07-paragon.md
│   ├─ 08-endgame.md
│   ├─ 09-duo.md
│   ├─ 10-minmax.md
│   ├─ 11-errores-y-mitos.md
│   └─ 12-muro-de-expansion.md
├─ construir.mjs         # generador: contenido/*.md -> index.html
├─ investigacion/
│   ├─ DOSSIER.md        # síntesis + contradicciones + huecos
│   └─ crudo/*.md        # 13 informes por dominio, con fuentes y fechas
└─ .claude/
    ├─ skills/d4-recon/  # /d4-recon  -> reinvestiga todo y regenera
    └─ skills/d4-parche/ # /d4-parche -> chequeo rápido tras un hotfix
```

**Separación de responsabilidades.** `contenido/` no sabe nada de HTML; `construir.mjs`
no sabe nada de Diablo; el agente escribe markdown y llama al generador. Cada pieza es
sustituible sin tocar las otras.

### 3.1 El generador (`construir.mjs`)

Node puro, **cero dependencias** (Node v26 disponible). Lee `contenido/*.md` en orden
alfabético, convierte a HTML e inyecta en una plantilla. Salida: **un solo fichero**.

Requisitos del HTML resultante:
- **Autocontenido**: CSS y JS inline, sin CDN, sin fuentes externas. Abre sin internet.
- **Buscador instantáneo** sobre todo el texto. Es el modo de uso real: el móvil al lado
  del teclado, buscar "glifo" a mitad de partida.
- **Navegación lateral** con las secciones, colapsable en móvil.
- **Responsive** de verdad: se lee con una mano en un móvil.
- **Modo oscuro por defecto** (se juega de noche y con el monitor en oscuro).
- Marcadores visuales `✅ juego base` / `🔒 requiere expansión` **renderizados como
  distintivos**, no como texto suelto. Es la información más importante para este usuario.
- Tablas con scroll horizontal propio; la página nunca hace scroll lateral.
- Cada sección muestra su **fecha de última verificación y el parche** contra el que se validó.

### 3.2 El agente (`.claude/skills/d4-recon/`)

Invocación: `/d4-recon` (completo) o `/d4-parche` (rápido).

Fases:
1. **Anclaje temporal** — averigua por web el parche y la temporada vivos *hoy*. Nada se
   asume de memoria; el conocimiento del modelo se considera caducado por defecto.
2. **Investigación en abanico** — un subagente por dominio, escribiendo a `investigacion/crudo/`.
3. **Verificación adversarial** — sobre los dominios críticos (dificultad, leveling, builds,
   itemización, expansiones), un segundo agente intenta *refutar* al primero y corrige el
   fichero. Esta fase es el corazón del diseño: es lo que separa esta guía de un blog.
4. **Redacción** — reescribe `contenido/*.md` desde el dossier verificado.
5. **Regeneración** — ejecuta `node construir.mjs` y commitea.

**Invariante del agente:** ningún dato entra en la guía sin fuente citada y fecha. Si un
dato no se puede fechar, se marca como incierto en lugar de presentarse como hecho.

### 3.3 Publicación

GitHub Pages con *deploy desde rama* (`main`, raíz). No consume minutos de Actions.
URL resultante: `https://d-alvhor.github.io/DIAVLO-IV/`.

## 4. Contenido de la guía

Ordenado por el momento en que el jugador lo necesita, no por categoría teórica:

| # | Capítulo | Qué responde |
|---|----------|--------------|
| 00 | Empezar aquí | Ruta de 5 minutos. Qué leer según dónde estés. |
| 01 | Ajustes PC | Gráficos, rendimiento con muchos esbirros, UI, keybinds, accesibilidad. |
| 02 | Ajustes PS5 | Rendimiento vs calidad, mando, qué builds son cómodas con mando. |
| 03 | Dificultad | Nombres y orden reales, a qué dificultad jugar en cada franja, la señal de "ya puedo subir". |
| 04 | Leveling 1-60 | Orden **exacto** de puntos de habilidad, Libro de los Muertos, campaña sí/no, horas reales. |
| 05 | Builds | Tier list completa + las 3 viables **sin expansión** al detalle (barra, aspectos, stats, rotación). |
| 06 | Itemización | Greater Affixes, Mythic Unique 3.0, temple, maestría. Regla de 3 segundos: qué recojo, qué tiro. |
| 07 | Paragon y glifos | Tableros en orden, glifos por build, breakpoints. |
| 08 | Endgame | Pit, Hordas, mazmorras de pesadilla, jefes invocables. Tabla "qué actividad según lo que necesites". |
| 09 | Dúo | Escalado con 2 jugadores, XP, cross-play PC↔PS5, y **combos de dos nigromantes que se potencian**. |
| 10 | Min-max | Breakpoints, topes de stats, rotaciones, empuje de Pit. El capítulo friki. |
| 11 | Errores y mitos | Trampas de novato + **mitos que eran verdad en temporadas viejas y ya no**. |
| 12 | Muro de expansión | El nivel exacto donde se nota la falta de VoH, si se nota, y si compensa comprarla. |

**Idioma:** español de España, con el término **en inglés entre paréntesis** la primera vez
que aparece. El juego se juega en español; las guías y los planners están en inglés. El
jugador necesita poder cruzar ambos.

## 5. Decisiones tomadas y descartadas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| Markdown como fuente, HTML generado | HTML escrito a mano | El agente rompe HTML; el markdown lo reescribe limpio cada temporada. |
| Un solo fichero HTML | Sitio multipágina | El buscador global es el caso de uso real (móvil en la mano). |
| Skill de Claude Code | GitHub Action | Una Action no puede investigar sin API key de pago. La skill usa la suscripción existente. |
| Cero dependencias en el generador | Astro / 11ty / marked | Un `npm install` roto dentro de seis meses mata la regeneración. |
| Verificación adversarial obligatoria | Investigar y ya | Es la única defensa contra la plaga de guías caducadas. |

## 6. Criterios de aceptación

1. `node construir.mjs` produce un `index.html` que abre **sin conexión** y sin errores en consola.
2. El buscador encuentra un término presente en cualquier capítulo.
3. La guía se lee de una pasada en un móvil, sin scroll horizontal.
4. **Todo** sistema mencionado está marcado ✅ base o 🔒 expansión.
5. Cada capítulo declara parche y fecha de verificación.
6. El capítulo de builds distingue explícitamente builds viables sin expansión de las que no.
7. Ningún dato numérico aparece sin fuente en `investigacion/`.
8. `/d4-recon` regenera la guía de punta a punta sin intervención manual.
9. La guía es navegable en `https://d-alvhor.github.io/DIAVLO-IV/`.

## 7. Riesgos

- **Que la Season 14 muera pronto.** La PTR 3.2.0 de la S15 corrió del 4 al 11/08/2026; la
  temporada acaba en semanas. *Mitigación:* el capítulo 00 declara la fecha de caducidad
  estimada y el agente existe precisamente para el relevo.
- **Que las fuentes públicas asuman expansiones en silencio.** Es el riesgo central.
  *Mitigación:* la verificación adversarial pregunta explícitamente por esto en cada dominio.
- **Que ciertas herramientas externas violen la política de Blizzard.** *Mitigación:* no se
  recomienda ninguna sin verificar antes la postura oficial; el riesgo de baneo se declara.
- **Que el dúo de dos nigromantes tenga menos sinergia de la esperada.** *Mitigación:* si la
  investigación lo confirma, se dice claramente en lugar de forzar un combo que no existe.

## 8. Fuera de alcance

- Otras clases más allá de lo necesario para contextualizar el nigromante.
- Modo Hardcore.
- PvP / Campos del Odio.
- Traducción de la guía a inglés.
