# Diseño — Guía y agente de Diablo IV para nigromante

**Fecha:** 2026-08-18 · **Revisión:** v3 (tras dos rondas de revisión adversarial de Sol/GPT-5.2)
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
│   ├─ version/     10-dificultad · 11-nigromante · 12-leveling · 13-itemizacion
│   │               14-paragon · 15-builds · 16-endgame · 17-muro · 18-minmax
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
temporada: 14          # número | todas   <- gobierna la caducidad, no la carpeta
estado: vivo          # vivo | ptr | caducado | archivado
entitlement: base     # base | voh | loh  (mínimo requerido)
verificado: 2026-08-18
revisar_despues: 2026-10-01
---
```

**`temporada` manda sobre la carpeta.** Las dimensiones parche y temporada son combinables,
no excluyentes: una build del parche 3.1.3 puede depender además de la mecánica de la S14.
Vivir en `version/` no la hace sobrevivir a la S15. Cualquier fichero con `temporada: 14`
caduca con la S14 **esté donde esté**; `temporada: todas` es lo único neutral.

**Manifiesto de publicación** en `manifiesto.json`:

```json
{ "parche_actual": "3.1.3", "temporada_actual": 14 }
```

El generador publica sólo contenido compatible con el manifiesto. Si no hay cobertura para la
temporada actual, escribe **"sin cobertura vigente"**; **nunca** rescata en silencio la
temporada anterior haciéndola pasar por actual.

**Matriz de enlaces** (la valida la build):

| Desde | No puede enlazar a |
|---|---|
| `nucleo/` | `temporada/` |
| Contenido vivo | `archivo/` |
| Contenido con `temporada: todas` | Cualquier temporada concreta |
| Navegación y buscador vivos | Contenido en estado `ptr` o `archivado` |

Los enlaces a "la temporada actual" apuntan a un **alias lógico estable**, nunca a `s14-*`.

### 3.1.1 Caducidad: dos comportamientos distintos

Aquí la v2 se contradecía. Son dos cosas separadas y ambas hacen falta:

- **En publicación:** `validar.mjs` **falla** si se intenta publicar un fichero con
  `revisar_despues` vencido. No se publica contenido caduco.
- **En pantalla:** el HTML ya publicado compara `revisar_despues` con el **reloj del
  navegador** y muestra el aviso de caducidad por sí solo. La guía envejece en manos del
  lector y lo confiesa sin que nadie la regenere.

El reloj es inyectable para poder probar ambos comportamientos.

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

**Para que esto sea lintable y no prosa piadosa**, el nivel de evidencia es un bloque del
dialecto, no una convención de redacción:

```markdown
::: evidencia nivel=corroborado fuentes=maxroll-necro-s14,icyveins-necro-s14
El glifo X alcanza su umbral relevante a nivel 46.
:::
```

Así el validador puede comprobar de verdad que el número tiene detrás el nivel declarado y las
fuentes que dice tener. **Ninguna cifra consecuente puede vivir fuera de un bloque `evidencia`.**

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

Igual que la evidencia, la build es un **bloque estructurado** con su entitlement declarado,
para que el validador pueda auditarla sin adivinar dónde empieza y acaba:

```markdown
::: build nombre="Esbirros" estado=arranque entitlement=base evidencia=corroborado
...
:::
```

### 3.3.1 Invariante de la ruta base-only

Más importante para este jugador que cualquier etiqueta de capítulo:

> **Todo paso obligatorio del recorrido "Haz esto ahora" debe apuntar a contenido, objeto y
> actividad con `entitlement: base`. Lo bloqueado sólo puede aparecer como alternativa
> opcional y marcada como tal.**

Etiquetar honestamente cada paso no impide mandar al jugador por cinco pasos que no puede
hacer. El invariante sí. Lo valida la build recorriendo la ruta entera.

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
investigación lo confirma. Y como no se prueba nada en el juego, **el lenguaje no puede fingir que sí**: se dice
"el mayor tier de Pit **documentado** con juego base por fuentes fechadas", no "el techo real";
"horas **reportadas**", no "coste real en horas"; "techo **estimado**", no "techo real".
Queda prohibido en toda la guía el vocabulario de medición propia.

## 4. El generador (`construir.mjs`)

Node puro, **cero dependencias de runtime**. La objeción de Sol —un parser casero de
markdown es un riesgo— se acepta y se neutraliza con sus propias tres condiciones:

1. **Dialecto cerrado.** Sólo: encabezados, párrafos, listas, tablas, énfasis, código,
   enlaces, citas al pie, bloques de aviso y los bloques estructurados `::: evidencia :::`
   y `::: build :::`. Nada más.
2. **Sintaxis desconocida = build rota.** No se renderiza "como se pueda": falla y lo dice.
3. **Escapado por defecto, HTML crudo siempre fatal, y protocolos en lista blanca.**
   Todo texto se escapa antes de insertarse. **HTML crudo está prohibido**, no sanitizado:
   encontrarlo **falla la build siempre** — nunca "falla o escapa", que era la ambigüedad de
   la v2. Y escapar texto **no** neutraliza `[pincha aquí](javascript:...)`: el destino de
   todo enlace se valida contra una lista blanca de protocolos (`https:`, `http:`, anclas `#`
   y rutas relativas); cualquier otro rompe la build. Los fixtures hostiles son
   **contextuales** —el payload dentro de un enlace, de una tabla, de un atributo, de una cita—
   no cadenas sueltas buscadas en la salida.

   El contenido lo redacta un agente a partir de texto copiado de internet y se publica en una
   URL pública. Tratarlo como no confiable no es paranoia: es la única postura defendible.

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

**Fail-closed, sin umbrales arbitrarios.** La v2 decía tres cosas incompatibles. La regla es
una: **cada dominio se declara de antemano obligatorio u opcional**. Si falla **cualquier
dominio obligatorio**, se aborta la ejecución entera — sin build, sin commit, sin push, sin
publicación parcial. Nada de "3 de 13". Y jamás se rellena un hueco con el contenido anterior
fingiendo que sigue vigente: eso es exactamente el fallo del ecosistema que este proyecto
existe para no cometer.

**Sobre la reanudación:** sería cómodo retomar una ejecución interrumpida, pero **no se promete**
porque no se va a probar. Queda como aspiración declarada, no como garantía.

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
| versión | 11 | **Nigromante de cero** | Esencia, cadáveres, esbirros, Libro de los Muertos. Cómo funciona la clase. |
| versión | 12 | **Subida 1 → 60** | Personaje estacional vs Eterno, campaña o salto, **orden exacto de habilidades**, cuándo cambiar de dificultad, cómo mantener sincronizado al dúo, y el enganche exacto con la build de arranque. |
| versión | 13 | Itemización | Afijos mayores, Mythic 3.0, temple, maestría. En qué orden gastar materiales. |
| versión | 14 | Paragon y glifos | Tableros en orden, glifos por build, breakpoints. |
| versión | 15 | Builds | Tier list + las viables sin expansión, en tres presupuestos cada una. |
| versión | 16 | Endgame | Pit, Hordas, jefes. Tabla "qué actividad según lo que necesites". |
| versión | 17 | Muro de expansión | Qué se degrada sin VoH, dónde, y si compensa comprarla. |
| versión | 18 | Min-max | Mayor tier de Pit documentado con juego base. Breakpoints, topes, rotaciones. |
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

Todos corren en `validar.mjs` o son comprobaciones manuales inequívocas. Ninguno admite
interpretación: o pasa o rompe la build.

| # | Gate | Cómo se comprueba |
|---|---|---|
| 1 | Build determinista | Dos builds seguidas ⇒ ficheros idénticos byte a byte. |
| 2 | Sintaxis desconocida rompe la build | Fixture con sintaxis no soportada ⇒ salida distinta de cero. |
| 3 | HTML crudo **siempre** fatal | Fixture con `<script>` en cualquier contexto ⇒ build falla. Nunca escapa y continúa. |
| 4 | Protocolos en lista blanca | `[x](javascript:...)`, `data:`, `vbscript:` ⇒ build falla. Sólo `https:`, `http:`, `#`, rutas relativas. |
| 5 | Payloads contextuales | Payload dentro de enlace, tabla, cita y bloque estructurado ⇒ ninguno alcanza la salida ejecutable. |
| 6 | Frontmatter completo y válido | Todo `.md` con los 8 campos; `temporada` es número o `todas`. |
| 7 | Matriz de enlaces | Se comprueban las 4 reglas de §3.1, no sólo núcleo↛temporada. |
| 8 | Sin contaminación del buscador | Ningún documento `ptr` o `archivado` aparece en el índice de búsqueda vivo. |
| 9 | Citas ligadas a su afirmación | Toda `fuentes=` de un bloque `evidencia` resuelve a una fuente registrada en `investigacion/`, y el recuento cumple el mínimo del nivel declarado (`corroborado` ⇒ ≥2 independientes). |
| 10 | Sin anclas rotas | Todo enlace interno apunta a un ancla existente. |
| 11 | Entitlement estructurado | Todo bloque `build` y todo capítulo declaran `base`/`voh`/`loh`. |
| 12 | **Ruta base-only íntegra** | Se recorre "Haz esto ahora" entera: ningún paso obligatorio toca contenido, objeto o actividad con entitlement ≠ `base`. |
| 13 | Sin cifras huérfanas | Ninguna cifra consecuente fuera de un bloque `evidencia`; las de nivel `sin confirmar` llevan aviso renderizado. |
| 14 | Caducidad, dos comportamientos | (a) Publicar con `revisar_despues` vencido ⇒ falla. (b) Con reloj inyectado al futuro, el HTML publicado muestra el aviso. |
| 15 | Offline por `file://` | Se abre el fichero local con la red cortada: cero errores de consola y cero peticiones salientes. |
| 16 | Búsqueda: tildes, bidireccional y rápida | "critico"→"crítico", "esbirros"→"minions", con capítulo y ancla, y la función de búsqueda responde en **< 100 ms** sobre la guía real. |
| 17 | Móvil sin scroll horizontal | 360 px de ancho: el `body` no desborda. |
| 18 | `/d4-recon` fail-closed de verdad | En repo temporal con `push` simulado: con un dominio **obligatorio** forzado a fallar, `HEAD` queda inalterado y hay cero intentos de publicación. |
| 19 | **Ensayo de relevo de temporada** | Se mueve la S14 a `archivo/`, se regenera y se comprueba: cero resultados de S14 en la búsqueda viva, cero enlaces rotos, cero documentos `temporada: 14` fuera del archivo. |

**El gate 19 es el que decide si el diseño de capas funciona o es decorativo.** Se ejecuta antes
de dar el proyecto por bueno, no cuando llegue la Season 15 y ya sea tarde.

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
