# Diseño — Guía y agente de Diablo IV para nigromante

**Fecha:** 2026-08-18 · **Revisión:** v2 (tras revisión adversarial de Sol/GPT-5.2)
**Estado:** propuesto

## 1. Problema

Un jugador principiante quiere jugar **nigromante** en Diablo IV, hoy **Season 14
("Season of Death Awakening", desde el 30/06/2026, parche 3.1.3)**, y optimizar al máximo.
Juega **en dúo** con su pareja, también principiante y también nigromante. Él en **PC**,
ella/él en **PS5** (cross-play).

**Restricción dominante: sólo posee el juego base.** Ni *Vessel of Hatred* ni *Lord of Hatred*.

Hay dos fallos del ecosistema público que este proyecto existe para corregir:

1. **Las guías no se fechan.** Mezclan parches y temporadas sin declararlo. Un principiante
   no puede distinguir un consejo vivo de uno muerto hace tres temporadas.
2. **Las guías asumen las expansiones en silencio.** Recomiendan runas, mercenarios y
   actividades que este jugador no puede tocar, sin advertirlo nunca.

## 2. Qué se construye

Repo público `github.com/d-Alvhor/DIAVLO-IV`:

1. **La guía** — un `index.html` autocontenido, en español, usable desde el móvil.
2. **El agente** — skill de Claude Code que reinvestiga y regenera cuando el juego cambie.
   Sin CI y sin API keys de pago: corre sobre la suscripción existente.

## 3. La decisión estructural: contenido por capas

**El contenido se separa por velocidad de caducidad, no por tema.** Es la decisión que
gobierna todo lo demás.

| Capa | Caduca cuando | Ejemplos |
|---|---|---|
| `nucleo/` | Casi nunca | Ajustes gráficos, mando, controles, cross-play, cómo se lee un objeto, glosario ES↔EN |
| `version/` | Cambia el parche | Tiers de dificultad, itemización, paragon, builds, endgame, muro de expansión |
| `temporada/` | Muere con la temporada | Mecánica de la S14, ruta estacional, cierre de temporada |
| `archivo/` | Ya caducó | Temporadas pasadas, conservadas y marcadas como históricas |

**Invariante de capas:** `nucleo/` **no puede enlazar** a `temporada/`. Lo valida el
generador y falla la build si se incumple. Consecuencia práctica: cuando llegue la Season 15,
archivar la S14 es mover una carpeta, no reescribir la guía. Sin esta regla, el proyecto
nace caducado.

```
DIAVLO-IV/
├─ index.html
├─ contenido/
│   ├─ nucleo/      00-empezar · 01-ajustes-pc · 02-ajustes-ps5
│   │               03-como-funciona · 04-duo-cross-play · 05-glosario
│   ├─ version/     10-dificultad · 11-itemizacion · 12-paragon
│   │               13-builds · 14-endgame · 15-muro-expansion · 16-minmax
│   ├─ temporada/   20-s14-mecanica · 21-s14-ruta · 22-s14-cierre
│   └─ archivo/
├─ construir.mjs    # markdown -> index.html
├─ validar.mjs      # gates. Falla => no hay build ni commit.
├─ investigacion/
│   ├─ DOSSIER.md
│   ├─ crudo/       # informe original de cada dominio
│   └─ refutacion/  # la refutación, EN FICHERO APARTE
└─ .claude/skills/  # d4-recon · d4-parche
```

### 3.1 Frontmatter obligatorio

Cada `.md` empieza con:

```yaml
---
titulo: Dificultades y cuándo subir
capa: version
parche: "3.1.3"
temporada: 14
estado: vivo          # vivo | ptr | caducado | archivado
entitlement: base     # base | voh | loh  (mínimo requerido)
verificado: 2026-08-18
revisar_despues: 2026-10-01
---
```

`validar.mjs` rechaza cualquier fichero sin frontmatter completo o con `revisar_despues`
vencido sin que nadie lo haya renovado. **La guía caduca sola y lo dice**, en vez de mentir
en silencio.

### 3.2 Evidencia: qué significa "verificado"

Sol acertó en que trece agentes leyendo webs no es verificación. No se puede probar una
build en el juego, así que **no se fingirá que se ha hecho**. En su lugar, cada afirmación
consecuente lleva un nivel de evidencia visible:

| Nivel | Significa |
|---|---|
| **Oficial** | Parche o post de Blizzard. |
| **Corroborado** | Dos o más fuentes independientes de referencia coinciden. |
| **Fuente única** | Una sola fuente lo dice. |
| **En disputa** | Las fuentes se contradicen. Se muestran **ambas versiones**. |
| **Sin confirmar** | No se pudo fechar ni contrastar. Se marca; no se presenta como hecho. |

**Prohibición explícita:** ninguna afirmación numérica puede publicarse en nivel
"sin confirmar" sin llevar el aviso visible al lado. Nada de números huérfanos.

**La refutación se conserva.** El verificador adversarial **no edita** el informe original:
escribe `investigacion/refutacion/<dominio>.md`. Cuando dos agentes discrepan, el desacuerdo
es el dato más valioso que hay; borrarlo es destruir evidencia.

### 3.3 Builds por estado de progresión, no por "BiS"

Un principiante no tiene los objetos de la build final, así que la build final no le sirve.
**Cada build recomendada se publica en tres presupuestos**, y cada uno declara cómo se llega
al siguiente:

| Estado | Qué asume | Debe declarar |
|---|---|---|
| **Arranque** | Nivel 60 recién hecho, sin únicos, aspectos del códice | Con qué se juega mientras cae lo bueno |
| **Intermedia** | Aspectos clave y algún único conseguidos | Qué objeto concreto desbloquea el salto y **dónde se farmea** |
| **Aspiracional** | Equipo optimizado | Coste real en horas y si es alcanzable sin expansión |

**Nada de listas de objetos sin ruta de adquisición.**

### 3.4 Sesgos de investigación prohibidos

El propio spec v1 introdujo preguntas que presuponían su respuesta ("las 3 builds viables",
"el nivel exacto del muro"). Queda prohibido. La redacción debe admitir estos resultados:

- que sólo **una** build de nigromante sea competitiva sin expansión — o **ninguna**;
- que **no exista** un nivel exacto de muro, sino una degradación progresiva;
- que el mejor dúo de dos nigromantes consista en **no pisarse**, y no en una sinergia positiva.

Si la realidad es decepcionante, se publica decepcionante.

### 3.5 "Leaderboard": qué se promete de verdad

El objetivo declarado es min-max de nivel leaderboard. **Sin expansiones eso puede ser
literalmente inalcanzable**, y el capítulo de min-max debe abrir diciéndolo si la
investigación lo confirma. Lo que sí se promete y se puede medir: **el tier de Pit más alto
alcanzable con juego base**, con la build, el equipo y el parche declarados.

## 4. El generador (`construir.mjs`)

Node puro, **cero dependencias de runtime**. La objeción de Sol —un parser casero de
markdown es un riesgo— se acepta y se neutraliza con sus propias tres condiciones:

1. **Dialecto cerrado.** Sólo: encabezados, párrafos, listas, tablas, énfasis, código,
   enlaces, citas al pie y bloques de aviso. Nada más.
2. **Sintaxis desconocida = build rota.** No se renderiza "como se pueda": falla y lo dice.
3. **Escapado por defecto y fixtures hostiles.** Todo texto se escapa antes de insertarse.
   **HTML crudo en el markdown está prohibido**, no sanitizado: prohibido. Hay fixtures con
   `<script>`, `javascript:`, `onerror=` y URLs malformadas, y la build falla si alguno se
   cuela. El contenido lo redacta un agente desde texto copiado de internet y se publica en
   una URL pública: tratarlo como no confiable no es paranoia, es lo correcto.

**Salida:** un solo `index.html`, CSS y JS inline, sin CDN ni fuentes externas.

**Determinismo:** mismo `contenido/` ⇒ mismo `index.html` byte a byte. Sin marcas de tiempo
de build ni orden de iteración inestable. Un diff sucio delata un fallo del generador.

### 4.1 Búsqueda

Es el modo de uso real: el móvil al lado del teclado, buscando a mitad de partida.

- **Índice precomputado** en build (no escanear el DOM en cada tecla).
- **Normalización de tildes y mayúsculas**: "glifo" encuentra "Glifo", "critico" encuentra "crítico".
- **Bidireccional ES↔EN** vía alias del glosario: buscar "esbirros" encuentra "minions" y al revés.
  Sin esto la guía es inútil, porque el juego está en español y los planners en inglés.
- **Resultados con contexto**: fragmento + capítulo + capa + enlace de ancla estable.
  Nunca "ocultar todo salvo coincidencias", que en móvil desorienta.

### 4.2 Lectura

- Modo oscuro por defecto, con conmutador.
- Responsive real: se lee con una mano.
- Distintivos **✅ juego base** / **🔒 requiere expansión** renderizados como etiquetas.
- Cada capítulo muestra capa, parche y fecha de verificación.
- Tablas con scroll propio; la página **nunca** hace scroll horizontal.
- **Dos modos de recorrido**: "Haz esto ahora" (ruta lineal, decisiones mínimas) y
  "Referencia" (todo el detalle). El mismo documento sirve al que empieza y al que min-maxea.

## 5. El agente

`/d4-recon` (completo) · `/d4-parche` (rápido tras hotfix)

1. **Anclaje temporal** — averigua por web parche y temporada vivos hoy. El conocimiento del
   modelo se considera caducado por defecto.
2. **Abanico de investigación** — un subagente por dominio → `investigacion/crudo/`.
3. **Refutación adversarial** — en los dominios críticos, un segundo agente intenta refutar
   al primero y escribe **fichero aparte**.
4. **Resolución** — las discrepancias se resuelven por calidad de fuente, o se publican como
   "en disputa". Nunca se promedian.
5. **Redacción por capas** — reescribe sólo las capas afectadas. Un hotfix no toca `nucleo/`.
6. **Gate** — `node validar.mjs`. Si falla, **no hay build, no hay commit, no hay publicación**.
7. **Publicación** — build, commit y `push` explícito. Commit local no es publicar.

**Fail-closed.** Si 3 de 13 investigaciones fallan, el agente lo dice y no publica los
capítulos afectados; no rellena el hueco con lo que había antes fingiendo que está vigente.
**Reanudable:** una ejecución interrumpida se retoma sin repetir lo ya hecho.

**Sobre la periodicidad:** una skill local sólo actúa cuando se la invoca. No se promete
detección automática de cambios. Lo que sí hace la guía es **declarar su propia caducidad**
(`revisar_despues`) y mostrarla en pantalla, para que el humano sepa cuándo toca.

## 6. Contenido

| Capa | # | Capítulo | Qué responde |
|---|---|---|---|
| núcleo | 00 | Empezar aquí | Ruta de 5 minutos. Qué leer según dónde estés. |
| núcleo | 01 | Ajustes PC | Gráficos, rendimiento con muchos esbirros, UI, keybinds, accesibilidad. |
| núcleo | 02 | Ajustes PS5 | Rendimiento vs calidad, mando, qué builds son cómodas con mando. |
| núcleo | 03 | Cómo funciona el juego | Conceptos, lectura de objetos en 3 segundos, economía de materiales. |
| núcleo | 04 | Dúo y cross-play | Battle.net, invitaciones, campaña desincronizada, loot, reparto de roles. |
| núcleo | 05 | Glosario ES↔EN | Tabla buscable. Alimenta el buscador bidireccional. |
| versión | 10 | Dificultad | Tiers reales, a cuál jugar en cada franja, la señal de "ya puedo subir". |
| versión | 11 | Itemización | Afijos mayores, Mythic 3.0, temple, maestría. En qué orden gastar materiales. |
| versión | 12 | Paragon y glifos | Tableros en orden, glifos por build, breakpoints. |
| versión | 13 | Builds | Tier list + las viables sin expansión, en tres presupuestos cada una. |
| versión | 14 | Endgame | Pit, Hordas, jefes. Tabla "qué actividad según lo que necesites". |
| versión | 15 | Muro de expansión | Qué se degrada sin VoH, dónde, y si compensa comprarla. |
| versión | 16 | Min-max | Techo real de Pit con juego base. Breakpoints, topes, rotaciones. |
| temporada | 20 | Mecánica S14 | Pandemonium Ruptures, journey, pase, Corrupted Reaper. |
| temporada | 21 | Ruta S14 | Qué hacer y en qué orden esta temporada. |
| temporada | 22 | Cierre de temporada | Qué merece la pena en las semanas que quedan, qué sobrevive al pasar a Eterno. |

**Idioma:** español de España, con el término **en inglés entre paréntesis** la primera vez.
El glosario lo indexa en ambos sentidos.

## 7. Decisiones y descartes

| Decisión | Descartado | Por qué |
|---|---|---|
| Contenido por capas de caducidad | Capítulos por tema | Sin esto, la Season 15 obliga a reescribir todo. |
| Markdown como fuente | HTML a mano | El agente rompe HTML; reescribe markdown limpio. |
| Un `index.html` | Sitio multipágina | El buscador global es el caso de uso real. |
| Conversor propio de dialecto cerrado | `marked` / Astro / 11ty | Aceptando dialecto cerrado + fallo ruidoso + fixtures hostiles, el riesgo queda acotado y la regeneración sobrevive a seis meses sin tocar nada. |
| Un solo spec | Tres specs (propuesta de Sol) | Es una guía para dos personas, no una plataforma. Las capas caben aquí; tres ciclos de aprobación matan el proyecto. |
| Niveles de evidencia | "Verificado" binario | No se puede probar en el juego. Fingirlo sería peor que declararlo. |
| Skill local | GitHub Action | Una Action no puede investigar sin API key de pago. |
| Frontmatter + lint | Registro inmutable de afirmaciones con IDs | Sobreingeniería para este tamaño. El lint da el 90% del valor. |

## 8. Criterios de aceptación (ejecutables)

Todos son comprobaciones que corren en `validar.mjs` o a mano de forma inequívoca.

| # | Gate | Cómo se comprueba |
|---|---|---|
| 1 | Build determinista | Dos builds seguidas ⇒ ficheros idénticos byte a byte. |
| 2 | Sintaxis desconocida rompe la build | Fixture con sintaxis no soportada ⇒ salida distinta de cero. |
| 3 | Sin XSS | Fixtures con `<script>`, `javascript:`, `onerror=` ⇒ build falla o escapa; comprobado en la salida. |
| 4 | Frontmatter completo | Todo `.md` con los 8 campos válidos, si no falla. |
| 5 | Invariante de capas | Ningún enlace de `nucleo/` apunta a `temporada/`. |
| 6 | Citas resolubles | Toda cita al pie resuelve a una URL presente en `investigacion/`. |
| 7 | Sin anclas rotas | Todo enlace interno apunta a un ancla existente. |
| 8 | Entitlement declarado | Todo capítulo y toda build llevan `base`/`voh`/`loh`. |
| 9 | Sin números huérfanos | Ninguna cifra en nivel "sin confirmar" sin aviso visible al lado. |
| 10 | Caducidad visible | Capítulo con `revisar_despues` vencido ⇒ aviso en pantalla. |
| 11 | Offline por `file://` | Se abre el fichero local con la red cortada: sin errores de consola ni peticiones salientes. |
| 12 | Búsqueda con tildes y bidireccional | "critico"→"crítico" y "esbirros"→"minions" devuelven resultados con capítulo y ancla. |
| 13 | Móvil sin scroll horizontal | 360 px de ancho: el `body` no desborda. |
| 14 | `/d4-recon` es fail-closed | Con una investigación forzada a fallar, no se produce commit ni publicación. |

## 9. Riesgos

- **La Season 14 muere en semanas.** *Mitigación:* las capas. El trabajo de `nucleo/` y buena
  parte de `version/` sobrevive; sólo `temporada/` se archiva. El capítulo 22 convierte el
  final de temporada en contenido útil en vez de en un problema.
- **Las fuentes asumen expansiones en silencio.** Riesgo central. *Mitigación:* la refutación
  adversarial pregunta explícitamente por ello en cada dominio, y el gate 8 lo exige por escrito.
- **El objetivo "leaderboard" puede ser inalcanzable sin expansión.** *Mitigación:* §3.5 obliga
  a decirlo en la primera línea del capítulo, no a esconderlo.
- **Herramientas externas que violen la política de Blizzard.** *Mitigación:* no se recomienda
  ninguna sin verificar la postura oficial; el riesgo de baneo se declara explícito.
- **El agente publica contenido caduco con apariencia de autoridad.** El riesgo que más pesa.
  *Mitigación:* gates 4, 9 y 10 más los niveles de evidencia. La guía prefiere decir "no lo sé"
  antes que decir algo bonito.

## 10. Fuera de alcance

- Otras clases más allá de lo necesario para contextualizar el nigromante.
- Modo Hardcore. PvP / Campos del Odio.
- Traducción al inglés.
- Detección automática de parches sin intervención humana.
