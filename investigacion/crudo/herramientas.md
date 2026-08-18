# Ecosistema de herramientas externas de Diablo IV — Season 14 (agosto 2026)

> **Investigación fechada el 18 de agosto de 2026.**
> Estado del juego asumido: **Season 14 "Season of Death Awakening"** (viva desde el 30 de junio de 2026), parche vivo **3.1.3 (build 73224, 12 de agosto de 2026)**. PTR 3.2.0 de la Season 15 corrió del 4 al 11 de agosto de 2026.
>
> **Jugador objetivo:** principiante absoluto, **Nigromante (Necromancer)**, **SOLO JUEGO BASE** (sin *Vessel of Hatred*, sin *Lord of Hatred*), en **dúo con pareja** (también nigro principiante), **uno en PC y otro en consola** (cross-play). Objetivo: min-max nivel leaderboard.
>
> **Leyenda:** ✅ = funciona con el juego base · 🔒 = requiere expansión · ⚠️ = riesgo o aviso importante

---

## 0. TL;DR — el veredicto en diez líneas

1. **Las webs (Maxroll, Mobalytics, D4Builds, Icy Veins, Wowhead, helltides.com) son 100 % seguras** ✅. Son páginas web: no tocan el juego, no hay riesgo de baneo, y funcionan igual para el de consola porque se abren en el móvil o el navegador.
2. **Lo que instalas en el PC y se dibuja encima del juego (overlays) es zona gris/roja** ⚠️. La EULA de Blizzard prohíbe software no autorizado expresamente por Blizzard, y Blizzard **no autoriza nada expresamente**. Ver sección 2.
3. **El filtro de botín (Loot Filter) ya es una función OFICIAL dentro del juego** y —según la mayoría de fuentes— **está disponible para todo el mundo, también con el juego base** ✅. Esto mata la necesidad de la mayoría de overlays de terceros. Ver sección 6 (hay una contradicción entre fuentes, la reporto).
4. **Para el de consola hay una pega concreta y muy dolorosa: no se pueden pegar códigos de importación de filtros de botín en PS5/Xbox** según dos de tres fuentes. Hay solución (sección 11).
5. **Mejor planificador para min-max serio: Maxroll D4Planner.** Mejor para buscar builds raras/creativas: D4Builds. Mejor para "dime rápido qué está roto": Mobalytics.
6. **La trampa nº1 para vosotros:** ningún planificador ni guía filtra por "poseo la expansión o no". Las builds top de nigromante usan mercenarios, runewords y sistemas de expansión. Sección 12.
7. **Calculadora de daño real:** el port web de la hoja de Avarilyn (`jlian.github.io/d4-damage-calc/`) ✅ — gratis, navegador, sin instalación.
8. **Leaderboard real de la comunidad:** `helltides.com/pit`, crowdsourced con vídeo, actualizado el 18/08/2026 ✅.
9. **Herramientas muertas o dudosas que NO debéis usar como referencia:** `d4armory.io` (ya redirige a la web oficial de Blizzard), la app móvil D4Planner de iOS (última actualización nov. 2023), `d4planner.io` (contenido con referencias a Season 2).
10. **Comunidad:** Discord oficial *Sanctuary* + Discord de wudijo (canales por clase) + r/Diablo4Necromancer.

---

## 1. Cómo he clasificado el riesgo

He separado el ecosistema en tres cajones, porque para vosotros la diferencia es "me divierto" vs "pierdo la cuenta":

| Cajón | Qué es | Riesgo de baneo | Sirve al de consola |
|---|---|---|---|
| **A — Web pura** | Abres el navegador, lees, planificas, copias un código a mano | **Ninguno** | Sí, en móvil/tablet/navegador de la consola |
| **B — App móvil separada** | App en el teléfono, no toca el PC ni la consola | **Ninguno** | Sí |
| **C — Software en el PC que lee/dibuja sobre el juego** | Overlays, OCR de items, lectura de memoria | **Real, no nulo** ⚠️ | No (solo PC) |

**Recomendación de partida: vivid en A y B.** El cajón C es donde está el riesgo y, desde que existe el filtro de botín oficial, ha perdido gran parte de su razón de ser.

---

## 2. ⚠️ Política oficial de Blizzard sobre addons, overlays y software de terceros

Esto es lo primero que había que verificar antes de recomendar nada. Lo que he podido confirmar:

### 2.1 Lo que dice literalmente la EULA

La **End User License Agreement de Blizzard** (versión revisada por última vez el **21 de marzo de 2024**, según la propia página legal) prohíbe en su sección 1.C.ii:

- **Cheats (trampas):** métodos "no autorizados expresamente por Blizzard" (por hardware, software o combinación) que influyan y/o faciliten el gameplay.
- **Bots:** cualquier código y/o software, no autorizado expresamente por Blizzard, que permita el control automatizado del juego.
- **Hacks:** acceder o modificar el software de la plataforma de cualquier manera no autorizada expresamente por Blizzard.
- **Software no autorizado:** cualquier código y/o software, no autorizado expresamente por Blizzard, que pueda usarse en conexión con la plataforma y "que cambie y/o facilite el gameplay".

La sección 1.C.vi contiene una coletilla importante: Blizzard "puede, a su sola y absoluta discreción, permitir el uso de ciertas interfaces de usuario de terceros" — es decir, **existe la posibilidad teórica de excepciones, pero es discrecional y no automática**. **No hay exención explícita para overlays informativos.**

### 2.2 Postura práctica: Blizzard NO aprueba herramientas una por una

El hilo oficial del foro de Diablo IV "Third Party App: Diablo IV overlay is permitted? #ModCheck" (foros US de Blizzard) es el hilo de referencia de la comunidad sobre este tema. Conclusión del hilo:

- **No hay respuesta oficial de un empleado de Blizzard** que apruebe ni prohíba explícitamente overlays concretos.
- La postura resumida por la comunidad veterana (post de MissCheetah, 10 de junio de 2023): *"Blizzard no aprobará ningún software de terceros. No lo hacen ni lo controlan, así que no te van a decir que está bien."* Y: cualquier cosa que aporte funcionalidad que el juego base no ofrece, que automatice cualquier parte del juego/rotación, o que cambie archivos del juego, **no está permitida**.
- Blizzard considera que **la EULA es el aviso**. No hay lista blanca. No hay proceso de aprobación previa.
- Aviso adicional del hilo: los overlays "tienden a causar conflictos con los juegos de Blizzard: caídas, pantallas grises y zonas de pantalla que no responden".

### 2.3 Precedente histórico documentado

Blizzard ha advertido públicamente contra software de terceros modificador del juego en Diablo IV, señalando en particular **TurboHUD4**, con riesgo de acción disciplinaria que puede incluir **suspensión permanente** en casos graves. La justificación pública es que la naturaleza always-online/live-service obliga a Blizzard a mantener el control del código.

### 2.4 Traducción para vosotros dos

- **Todo lo que sea una web → cero riesgo.** Punto.
- **Overlays tipo Diablo4Companion, d4lf, Overwolf → riesgo real aunque no haya oleada de baneos documentada específicamente contra ellos.** No he encontrado ninguna evidencia de baneos masivos por estas herramientas concretas, pero tampoco ninguna autorización. Que llevéis meses sin problema no es garantía; las oleadas son retroactivas.
- **Consejo:** siendo principiantes y con el filtro de botín oficial ya en el juego, **el beneficio marginal de un overlay no compensa el riesgo**. Reevaluad dentro de 200 horas si de verdad os falta algo.

> ⚠️ **Incertidumbre importante:** no he podido confirmar ninguna declaración de Blizzard de 2026 (posterior a *Lord of Hatred*) que actualice o suavice esta política. Todo lo documentado que he podido leer es de 2023–2024 más la EULA de marzo de 2024. Se me agotó el presupuesto de búsquedas web antes de poder cerrar ese punto. **Trátalo como "política vigente salvo prueba en contrario", no como "verificado en 2026"**.

---

## 3. Planificadores de builds — comparativa

### 3.1 Tabla comparativa

| Herramienta | URL | Precio | Qué hace mejor | Cuenta obligatoria | Consola | Estado S14 |
|---|---|---|---|---|---|---|
| **Maxroll D4Planner** | maxroll.gg/d4/planner | Gratis | Planificación exhaustiva: equipo, aspectos legendarios, afijos, árbol de habilidades, paragon, renombre. Cálculos en vivo | No para leer; sí para guardar en cuenta | Sí (web) | ✅ Guías etiquetadas "Season 14 Death Awakening" |
| **D4Builds** | d4builds.gg | Gratis | Volumen y diversidad de builds off-meta creadas por jugadores; tierlist propia; base de datos con loot tables y mapas | No aparente | Sí (web) | ✅ Indica "Season 14"; ya muestra "Season 15 PTR data is live" |
| **Mobalytics** | mobalytics.gg/diablo-4 | Gratis | Tier list rápida, tarjetas visuales compactas, "loot filters" integrados en las guías, planner propio | Recomendable | Sí (web) | ✅ Planner con actualización visible del 17/08/2026 |
| **InfinityBuilds / InfinityTools** | infinitybuilds.gg · tools.infinitybuilds.gg | Gratis (aparente) | Planner + paragon + base de datos (uniques, aspectos, manuales de tempering, catálogo de afijos) + sección de loot filters | Desconocido | Sí (web) | ✅ Se declara "tested and updated for the current season (Season 14)" |
| **D4Planner.io** | d4planner.io | No indicado | Calculadora de habilidades + trackers con push | No | Sí (web/PWA) | ⚠️ Contenido con referencias a Season 2 — **sospechoso de estar desactualizado** |

### 3.2 Cuál usar y por qué (recomendación razonada)

**Para vuestro objetivo (min-max, nivel leaderboard): Maxroll D4Planner como herramienta principal.**

Razones concretas y verificables:

- El D4Planner **integra el árbol de habilidades y el tablero de paragon con los cálculos**, de modo que ves el impacto de cada cambio sin salir a hojas de Excel externas. La propia Maxroll lo vende así: en lugar de abrir otras hojas de cálculo o documentos, asignas items, habilidades y paragon y ves si el daño es suficiente.
- Incluye **equipo, aspectos legendarios, afijos, habilidades, paragon y progreso de renombre** en un solo perfil.
- Puedes **guardar perfiles y compartirlos** en la base de datos pública, donde además la comunidad los puntúa (sistema de ranking de builds).
- Sus autores incluyen creadores de referencia con página propia en Maxroll (`maxroll.gg/@wudijo`, `maxroll.gg/@macrobioboi`), lo que da trazabilidad de quién firma cada build.
- **Es gratis.** Sin muro de pago detectado.

**Cuándo usar D4Builds en su lugar:** cuando ya tengáis clara la meta y queráis **explorar variantes creativas** que Maxroll no cubre. D4Builds tiene builds de nigromante de sobra publicadas (Blood Wave, Minion, Bone Spirit, Blood Lance, entre otras) y una tierlist propia.

**Cuándo usar Mobalytics:** para el vistazo rápido de "¿qué está roto esta semana?". Es más veloz y visual, pero menos profundo.

> ⚠️ **Aviso metodológico crítico:** Maxroll y Mobalytics **rankean por separado y llegan a discrepar hasta en tres tiers sobre la misma build**. No promediéis sus tier lists. Elegid una fuente y sed coherentes, o mejor: fiaos del leaderboard real de Pit (sección 8) por encima de cualquier tier list editorial.

### 3.3 Lo que NINGÚN planificador hace bien (y os afecta directísimamente)

**Ningún planificador ni página de guías tiene un filtro "solo juego base".** Lo he comprobado explícitamente en la página de guías de builds de Maxroll: todas las guías de nigromante (Blood Surge, Army of the Dead, Bone Spear, Bone Spirit, Sever, Blood Wave, Minion, Blood Lance, Golem, Blight) aparecen etiquetadas únicamente como "Season 14 Death Awakening", **sin ninguna indicación de si requieren expansión y sin filtro para separarlas**.

Esto significa que **vosotros tenéis que hacer ese filtrado a mano**. Ver sección 12 con la checklist.

---

## 4. Calculadoras de daño y hojas de cálculo de la comunidad

### 4.1 La calculadora de daño de referencia ✅

**`https://jlian.github.io/d4-damage-calc/`** — gratis, web, sin instalación, sin cuenta.

- Es **un port web de la hoja de cálculo de "damage buckets" de Avarilyn**, la hoja de referencia histórica de la comunidad. La página afirma explícitamente que mantiene "las mismas matemáticas que la hoja de Avarilyn, en tu navegador".
- **Entradas:** clase, habilidad (skill), stats base sin equipo, afijos del equipo, asignación de puntos de paragon.
- **Salidas:** daño en vivo, desglose por los cinco "cubos" de daño (aditivo, vulnerable, crítico, daño de arma, multiplicadores) y —lo más útil— **ranking de qué mejora de stat te da más rendimiento ahora mismo**.
- ✅ **Funciona para el de consola** porque es una web.

> ⚠️ **Incertidumbre:** la página **no indica para qué parche/temporada está actualizada** ni menciona soporte específico de Nigromante. Tampoco declara caveats de precisión. Dado que las matemáticas de cubos son estructurales y no cambian cada temporada, sigue siendo útil, pero **verificad los números contra el juego real antes de tomar decisiones caras** (masterworking, tempering).

### 4.2 La referencia teórica que hay que leerse sí o sí

**`maxroll.gg/d4/resources/in-depth-damage-guide`** — **última actualización: 12 de junio de 2026** (por tanto, vigente para Season 14). Gratis, web.

Contenido clave verificado:

- **Multiplicadores globales (multiplicativos)**: marcados en el juego con `[x]%`. Multiplican todo el daño que cumpla su condición. Son "en gran medida independientes de tus stats de items y paragon". Ejemplos citados: The Grandfather con 150 %[x], y el 20 %[x] base contra enemigos vulnerables.
- **Daño aditivo**: marcado con `[+]%`. Todo se suma en un único cubo antes de multiplicar. Incluye daño cercano, daño a distancia, daño a vulnerables, daño de golpe crítico.
- La guía incluye una **fórmula general de daño** en formato gráfico, que incorpora: daño medio de arma × porcentaje de habilidad × multiplicador aditivo × multiplicadores globales × escalado de stat principal ÷ reducción de daño enemiga.

**Por qué importa para min-max:** la diferencia entre `[+]` y `[x]` es la diferencia entre "he subido un 5 % mi daño" y "he doblado mi daño". Es el concepto más rentable que podéis interiorizar como principiantes.

> ⚠️ **Nota:** esta guía **no menciona ninguna calculadora ni hoja de cálculo**. La conexión entre la guía y la calculadora de Avarilyn la hago yo; no es una recomendación de Maxroll.

---

## 5. Bases de datos de items y aspectos

| Herramienta | Qué ofrece | Precio | Consola |
|---|---|---|---|
| **Maxroll — Items / Resources** | Base de datos de items, tablas de botín de jefes (Boss Loot Table Cheat Sheet), cheat sheet de crafteo, guía de farmeo óptimo, guía de speed leveling | Gratis ✅ | Sí (web) |
| **D4Builds — Database** | Base de datos con loot tables y herramientas de mapa | Gratis ✅ | Sí (web) |
| **InfinityTools** | Uniques, aspectos, manuales de tempering, catálogo completo de afijos, planner de skills y rutas de paragon | Gratis (aparente) ✅ | Sí (web) |
| **Wowhead — Diablo 4** | Sección D4 con event timers, event map y event guides | Gratis ✅ | Sí (web) |

Para nigromante, la combinación práctica es: **Maxroll para las tablas de botín de jefes** (saber a qué jefe farmear para qué unique) + **InfinityTools o D4Builds para consultar afijos y aspectos** mientras planificáis.

> ⚠️ No pude abrir `tools.infinitybuilds.gg` ni `infinitybuilds.gg` directamente (HTTP 403 al fetcher). La información sobre InfinityBuilds procede de resultados de búsqueda y de las notas de versión de Diablo4Companion (que añadió soporte de importación desde InfinityBuilds.gg en julio de 2026, lo que **confirma que el sitio existe y está activo**).

---

## 6. Filtro de botín (Loot Filter) — el capítulo más importante

### 6.1 Ahora es una función OFICIAL del juego ✅

Esta es la novedad que cambia todo el ecosistema de herramientas: **Diablo IV tiene filtro de botín nativo**, introducido con la salida de la expansión *Lord of Hatred* (abril de 2026).

**Cómo funciona (verificado en la wiki de Fextralife y en la guía de Maxroll):**

- Acceso: **Opciones → Jugabilidad → Abrir Filtro de Botín** (Options → Gameplay → Open Loot Filter).
- Pulsas **"Nuevo filtro"** (New Filter) y eliges entre construir reglas propias o **"Importar filtro"** (Import Loot Filter) pegando un código de importación.
- También puedes **exportar** tu filtro para compartirlo.
- **Límite: 25 reglas por filtro.**
- Puedes tener **varios filtros guardados pero solo uno activo a la vez**.
- Las reglas **se priorizan de arriba abajo**: las de arriba sobrescriben a las de abajo.
- Las reglas individuales se pueden **activar/desactivar sin borrarlas**.
- Controla la visibilidad de items en **el suelo, el inventario, los contenedores de botín y los mercaderes**: ocultar, resaltar o priorizar.
- Parches relacionados documentados: **3.0.1a** arregló problemas de filtrado del Codex of Power; **3.0.2** arregló problemas de edición con mando.

### 6.2 🔴 CONTRADICCIÓN ENTRE FUENTES — ¿requiere expansión?

Esto es crítico para vosotros y las fuentes **no se ponen de acuerdo**:

| Fuente | Qué dice |
|---|---|
| **Icy Veins** (news, cita a Blizzard) | "Disponible para **todos los jugadores, independientemente de la posesión de la expansión**" |
| **Fextralife wiki** | "Aunque se introdujo con la expansión *Lord of Hatred*, es **parte del juego base y no requiere poseer la expansión**" |
| **Maxroll** (resources/loot-filter) | "**Requiere la expansión Lord of Hatred y no está disponible en el juego base**" |

**Mi lectura:** 2 de 3 fuentes dicen que es gratis para todos, y **una de ellas (Icy Veins) cita directamente el anuncio de Blizzard**. Además, encaja con el patrón habitual de Blizzard: los sistemas de calidad de vida se reparten a todos y lo que se vende son clases, zonas y campaña. **Probabilidad alta de que sea ✅ juego base.**

**Verificación de 30 segundos por vuestra parte:** abrid Opciones → Jugabilidad y mirad si aparece la entrada del filtro de botín. Es una comprobación que hacéis vosotros mismos y cierra la duda de forma definitiva.

### 6.3 🔴 SEGUNDA CONTRADICCIÓN — ¿puede la consola importar códigos?

Esto os afecta directamente porque uno de vosotros juega en consola:

| Fuente | Qué dice |
|---|---|
| **Maxroll** | "Los jugadores de consola **no pueden importar códigos de filtro** de las guías directamente; deben configurar los filtros a mano desde cero" |
| **d4lootfilter.com** (guía, act. mayo 2026) | "La función de importar/exportar está **actualmente solo disponible en PC**. PS5 y Xbox pueden crear y editar reglas manualmente en el menú del juego, pero **no hay forma de pegar un código de importación directamente**" |
| **D4 Filter Forge** | "El formato de filtro funciona multiplataforma. **Un filtro creado en PC puede importarse en consola y viceversa, siempre que estés logueado en la misma cuenta de Battle.net**" |

**Mi lectura:** las dos primeras fuentes hablan de **pegar un código de texto** (imposible sin teclado y sin campo de texto en consola). La tercera habla de que **el filtro viaja con la cuenta de Battle.net**. Son afirmaciones compatibles: no puedes *pegar el código* en la consola, pero si **importas el código en el PC estando en la misma cuenta, el filtro puede aparecer en la consola**.

**⚠️ Esto es una inferencia mía, no está confirmado por ninguna fuente de forma explícita.** Ver sección 11 para el plan de acción.

### 6.4 Herramientas web para filtros de botín (cajón A, cero riesgo) ✅

| Herramienta | URL | Qué hace | Precio |
|---|---|---|---|
| **D4 Filter Forge** | d4filterforge.com | **Editor visual de filtros en el navegador.** Construyes, editas y compartes filtros y **genera los códigos Base64 oficiales que el juego acepta**. Declara explícitamente: no lee ni escribe memoria del juego, no inyecta código, no corre junto al juego | Gratis (donación opcional) |
| **D4 Loot Filter Viewer** | d4lootfilter.com | **Descodificador de códigos.** Pegas un código de importación y te muestra el nombre del filtro, la clase para la que se diseñó y **la lista completa de cada regla** (visibilidad, colores, afijos requeridos, tipos de item). Pensado explícitamente para consoleros que deben recrear el filtro a mano | Sin coste indicado |
| **DiabloFilter** | diablofilter.com | Repositorio de filtros de la comunidad para D4 y D2R, con un "Filter Reader" para descodificar cualquier filtro | No verificado (403) |
| **diablo4lootfilter.com** | diablo4lootfilter.com | Buscador de códigos de importación | ⚠️ Su portada anuncia "**códigos de Season 13**" — posiblemente desactualizado |

**D4 Filter Forge es la joya de esta sección** y merece destacarse: es la única herramienta que he encontrado que **declara explícitamente por qué NO es software de terceros en el sentido de la EULA** ("no lee ni escribe en memoria del juego, no inyecta código, no corre junto al juego; solo pegas texto en los ajustes del juego"). Eso es exactamente el tipo de herramienta que podéis usar sin ninguna preocupación.

> ⚠️ D4 Filter Forge afirma que el soporte nativo de filtros llegó **"con el parche 2.1"**, lo que contradice a Icy Veins, Fextralife y Maxroll, que lo sitúan en *Lord of Hatred* (parche 3.0.x, abril de 2026). No he podido resolver esta discrepancia. Puede ser un error de la página o puede que hubiera una versión previa más limitada.

---

## 7. Overlays y software de escritorio — el cajón de riesgo ⚠️

Los documento porque existen y son populares, **no porque os los recomiende**.

### 7.1 Diablo4Companion (josdemmers/Diablo4Companion)

- **Qué es:** aplicación acompañante para Windows que muestra **un overlay dentro del juego resaltando los afijos, aspectos, runas y sigilos que buscas**. Usa **OCR y reconocimiento de imagen** para detectar los afijos del item en pantalla.
- **Funciones:** filtrado de botín por valor de afijo y poder del item; lista de comercio; **overlay del tablero de paragon**; multi-idioma.
- **Importación de builds:** desde **D2Core** (`d2core.com/d4/builds`), **D4Builds** (`d4builds.gg`), **Maxroll** (`maxroll.gg/d4/build-guides`, copiando el build ID tipo `dqih026y` de `maxroll.gg/d4/planner/dqih026y`), **Mobalytics** (`mobalytics.gg/diablo-4`, dos formatos de URL; en el formato simple hay que añadir antes la página de perfil) y desde julio de 2026 también **InfinityBuilds.gg**.
- **Licencia:** MIT, código abierto, gratis.
- **Estado de mantenimiento: MUY activo.** 808 commits. **Última versión v5.3.7.0 del 28 de julio de 2026.** Historial reciente: v5.3.6.0 (27 jul), v5.3.5.0 (24 jul, con actualización de datos para **v3.1.1.72903** — confirma que sigue el parche 3.1.1 de Season 14), v5.3.4.0 (1 jul), v5.3.3.0 (29 jun), v5.3.2.0 (20 jun, añadió soporte de community builds de Mobalytics).
- ⚠️ **La documentación NO contiene ninguna declaración sobre la TOS de Blizzard ni sobre riesgo de baneo.** Silencio absoluto sobre el tema.
- ❌ **Solo Windows (.exe). No sirve al de consola.**

### 7.2 D4LF (d4lfteam/d4lf)

- **Qué es:** filtro de botín que analiza tu inventario y alijo y filtra por tipo de item, poder, valores de afijo, rareza y número de greater affixes. Soporta uniques, seals, charms, sigils y tributes. Incluye overlays de tablero de paragon y de eventos del mundo.
- **Qué NO hace (según su propia documentación):** no auto-desmantela ni descarta automáticamente. Presenta las decisiones al jugador, que gestiona los items a mano. Usa lectura vía TTS en lugar de manipulación directa del juego.
- **Estado:** 722 commits. **Última versión v10.0.2 del 7 de agosto** (probablemente 2026, aunque el fetch no lo confirmó con año).
- ⚠️ **Ninguna advertencia sobre TOS ni riesgo de baneo en su documentación.**
- ❌ **Windows (funcionalidad completa requiere Windows por la integración TTS). No sirve al de consola.**

### 7.3 Overwolf — plataforma de apps con overlay

`overwolf.com/browse-by-game/diablo-iv` lista estas apps para Diablo IV, **todas gratuitas**:

| App | Qué hace |
|---|---|
| **Mobalytics Desktop** | Companion todo-en-uno con overlays, builds y perfiles |
| **D4 Interactive Map** | Mapa interactivo con **posición del jugador en vivo** |
| **Diablo 4 Map** | Seguimiento de posición en tiempo real para actividades |
| **dIVa** | "Interfaz dinámica con analíticas visuales": estadísticas en tiempo real y overlays inteligentes |
| **PureDiablo** | Mapas interactivos y **seguimiento de XP** |
| **DIABLO SNAPS** | Identificación y compartición de items para coleccionistas |
| **Traderie** | Marketplace |
| **Play With Purpose** | Raiding y trading multi-juego |
| **Game Maps** | Mapas interactivos multi-juego |

⚠️ **La página de Overwolf NO contiene ningún descargo de responsabilidad sobre aprobación de Blizzard, seguridad ni riesgo de baneo.** Las apps de "posición del jugador en vivo" son precisamente el tipo de funcionalidad que la interpretación estricta de la EULA describe como *"funcionalidad no proporcionada por el juego base"*.

**Mi recomendación explícita: no instaléis nada de este cajón.** Especialmente estando en dúo: si uno pierde la cuenta, se acabó el proyecto de min-max para los dos.

---

## 8. Trackers de eventos, temporada y progreso

### 8.1 helltides.com ✅ — el más completo y el más actual

- **Rastrea:** Helltides, Cofres Misteriosos (Tortured Gifts of Mysteries), ubicaciones de Rituales, **Jefes del Mundo (World Bosses)**, **Eventos Legión**, y **Realmwalkers / Hatred Rising**.
- **Notificaciones:** sí — icono de campana + control deslizante de audio para activar notificaciones de audio y de navegador.
- **Precio:** gratis, con opción "Ad Free" de pago para quitar publicidad.
- **Consola:** ✅ es web, se abre en el móvil.
- **Leaderboard del Pit:** `helltides.com/pit` — ver 8.2.
- ⚠️ **Contradicción interna:** al abrir la portada, parte del texto hace referencia a "Season 6" y menciona Nahantu como zona activa, con versión de sitio "v5.2.6". Pero **la sección del Pit está actualizada al 18/08/2026 con datos de Season 14**. Interpretación: el sitio está vivo y actualizado, pero tiene **texto estático viejo sin limpiar** en la portada. No lo descartéis por eso.

### 8.2 helltides.com/pit ✅ — el leaderboard real de la comunidad

Esto es lo que os interesa como objetivo declarado de "nivel leaderboard":

- **Naturaleza: crowdsourced de la comunidad, NO oficial de Blizzard.**
- **Cómo se envía una run:** grabas la run, la subes a YouTube u otra plataforma de vídeo, pulsas "Submit run" arriba de la página y metes la URL del vídeo. Pasa por **revisión** antes de publicarse.
- **Requisitos del vídeo:** debe mostrar **la run estacional completa**, buena calidad, **sin edición**.
- **Umbral de elegibilidad:** las speedruns elegibles deben ser de **Tier 100 o superior**.
- **Estado a 18/08/2026 12:55:** 432 envíos totales, 3 pendientes de revisión.
- **Realidad para nigromante (dato duro que os conviene interiorizar):** de las 15 mejores clears, **14 son Rogue**; en los 11 primeros puestos, **solo hay Rogues**. El mejor nigromante registrado está en el **puesto #8 con Tier 139 y 12:40** (jugador "[INF]秋葉@黑巫师-血潮").
- ⚠️ Los dos datos anteriores parecen provenir de instantáneas distintas del ranking (un snapshot dice "los 11 primeros son Rogue" y otro sitúa un nigro en el #8) — el leaderboard cambia a diario. Consultadlo en vivo.
- **Precio:** gratis. **Consola:** ✅ es web.

### 8.3 Wowhead — Diablo 4 Event Timers ✅

`wowhead.com/diablo-4/event-timers` — timers de **Helltides**, **Eventos Legión** y **Jefes del Mundo**. Incluye "Event Timers", "Event Map" y "Event Guides". **Todos los tiempos se muestran en tu hora local.** Gratis, web, funciona para consola.
⚠️ La página no menciona Season 14 ni el parche 3.1 explícitamente.

### 8.4 Maxroll — Mapa interactivo con trackers ✅

- Timers automáticos de **Helltides, Legiones y Jefes del Mundo**.
- **El tracker de Helltide coloca automáticamente los Cofres Misteriosos en sus ubicaciones correctas.**
- Muestra objetivos de **Renombre por región**: misiones secundarias, mazmorras, bastiones (strongholds) y **aspectos legendarios**.
- **Guardado de progreso:** si estás logueado en una cuenta Maxroll, se guarda en la cuenta; si no, se guarda en el almacenamiento del navegador.
- El marcado de progreso es **manual** (clicas los elementos del mapa para marcarlos como completados).
- ⚠️ El artículo de anuncio es del **17 de octubre de 2023** y **no dice nada sobre cobertura de Nahantu/Kurast** (zona de *Vessel of Hatred* 🔒). Para vosotros esto es irrelevante: **como no tenéis VoH, no vais a ir a Nahantu de todas formas.**

### 8.5 Trackers que NO recomiendo

| Herramienta | Problema |
|---|---|
| **d4planner.io** | Los trackers funcionan y tiene push (en iOS hay que añadirlo a la pantalla de inicio), pero **el contenido hace referencia a Season 2** (farmeo de Uber Duriel). **Fuertemente sospechoso de estar desactualizado.** No indica si es gratis |
| **d4armory.io** | ❌ **MUERTO.** El dominio ahora hace **redirect 301 a diablo4.com, que a su vez redirige a diablo4.blizzard.com**. Ha dejado de existir como herramienta independiente. Muchas guías viejas todavía lo citan — ignoradlas |
| **App móvil "D4Planner" (iOS)** | ❌ **Última versión 1.9.0 del 13 de noviembre de 2023.** Valoración 3,8/5 con 40 votos. Es gratis pero está **abandonada hace casi tres años**. No la instaléis |

---

## 9. Mapas interactivos (Altares de Lilith y zonas)

| Herramienta | Qué cubre | Sync | Precio | Consola |
|---|---|---|---|---|
| **Maxroll World Map** | Altares de Lilith, waypoints, mazmorras, bastiones, aspectos legendarios, objetivos de renombre por región, + timers de eventos | Cuenta Maxroll o localStorage del navegador; marcado **manual** | Gratis ✅ | Sí (web) |
| **D4Builds — Map tools** | Herramientas de mapa integradas en su base de datos | No verificado | Gratis ✅ | Sí (web) |
| **App "Map and Timers for Diablo 4" (iOS)** | Mapa interactivo de Santuario, timers de Helltide con notificaciones, lista de guilds | No verificado | Gratis (aparente) | Sí (app móvil) ⚠️ actualidad no verificada |
| **D4 Interactive Map / Diablo 4 Map (Overwolf)** | Mapa con **posición del jugador en vivo** | Automática | Gratis | ❌ Solo PC · ⚠️ overlay, ver sección 7 |

**Para el dúo, la jugada correcta:** el mapa de Maxroll abierto en el móvil o en una segunda pantalla mientras el otro juega. **Cero riesgo, funciona para ambos, y el marcado manual de altares os obliga a coordinaros** (que además es lo que queréis, porque los Altares de Lilith dan bonos permanentes de cuenta que hay que recoger una sola vez).

⚠️ La versión con posición del jugador en vivo de Overwolf es más cómoda, pero es exactamente el tipo de "funcionalidad no proporcionada por el juego base" que la EULA describe. No la uséis.

---

## 10. Comercio, precios y economía

### 10.1 Reglas de comercio del juego (verificado en Maxroll)

**Qué SÍ se puede intercambiar:**
- Items comunes, mágicos, raros, legendarios y **uniques**
- Oro
- Gemas, elixires, incienso
- **Materiales de invocación de jefes**

**Qué NO se puede intercambiar (account-bound):**
- 🔴 **Mythic Uniques**
- 🔴 **Cualquier equipo que haya sido encantado (enchanted), templado (tempered) o masterworked** — esto es enorme para min-max: en cuanto tocas una pieza, deja de ser comerciable
- 🔴 Todas las monedas excepto el oro
- 🔴 Items de misión y Pergaminos de Huida (Scrolls of Escape)

**Mecánica:** el comercio se hace **directamente entre jugadores en Kyovashad**. Ambos deben estar en la misma instancia de mundo, se inicia con la rueda de acción, y **ambas partes deben bloquear su oferta antes de aceptar**.

**No hay casa de subastas dentro del juego.** Ninguna fuente consultada menciona una.

**Aviso de seguridad de la propia guía:** *"comprueba siempre dos veces los items que tu compañero de comercio ha puesto en la ventana de comercio"* — para evitar la estafa clásica del cambiazo de última hora.

### 10.2 Sitios de comercio de terceros

⚠️ **Aviso primero: la guía de comercio de Maxroll NO nombra ni referencia ningún sitio web de terceros.** Los siguientes aparecieron en búsquedas pero **no he podido abrir ni verificar ninguno**, y varios son sitios de dinero real (RMT), que es un vector clásico de baneo y de estafa:

- **Odealo** (odealo.com) — marketplace con listados de Season 14
- **The Crimson Market** (thecrimsonmarket.com) — trading de items, gear y oro; ofrece price check
- **PlayerAuctions**, **Easy Item Trading** (easyitemtrading.com, con price check y detección de items por captura de pantalla)

Dato de precios que apareció en búsquedas y que **NO puedo verificar**: los Mythics comunes empiezan en 20–50 $, y los Mythics definitorios de build con rolls perfectos llegan a 100–500 $+, con máximos al principio de la temporada.

> 🔴 **Recomendación tajante para principiantes:** **no toquéis los sitios de dinero real.** La compra de items por dinero real es terreno de baneo y de estafas, y además vuestros Mythic Uniques serían intransferibles de todas formas (son account-bound). Para vosotros dos, el "comercio" útil es **entre vosotros**: pasaros uniques y materiales de jefe **antes de tocarlos con tempering/masterworking**.

**Vosotros dos podéis comerciar entre PC y consola sin problema**, ya que el cross-play permite estar en la misma instancia de mundo. ⚠️ No he encontrado fuente que confirme explícitamente que el comercio directo funcione entre plataformas distintas; el requisito documentado es "estar en la misma instancia de mundo", que el cross-play permite. **Verificadlo en vuestra primera sesión.**

---

## 11. Guía específica para el dúo PC + consola

Esta sección es la que os resuelve problemas prácticos concretos.

### 11.1 Lo que funciona igual para los dos ✅

Todo lo del cajón A y B: Maxroll (guías, planner, mapa, damage guide, tablas de botín), D4Builds, Mobalytics, Icy Veins, Wowhead, helltides.com, la calculadora de daño, D4 Filter Forge, el descodificador de filtros. **El de consola abre estas webs en el móvil, la tablet o el navegador y tiene exactamente la misma información.**

### 11.2 Lo que NO funciona en consola ❌

- **Diablo4Companion, d4lf, todas las apps de Overwolf** — son ejecutables de Windows.
- **Pegar códigos de importación de filtros de botín** — dos de tres fuentes dicen que la importación/exportación de códigos es exclusiva de PC.

### 11.3 Plan de acción para el filtro de botín en el dúo

**Orden de intentos, del mejor al peor:**

1. **Primero probad esto:** que el de PC importe el código del filtro y comprobéis si aparece en la cuenta del de consola. D4 Filter Forge afirma que **el formato es multiplataforma y viaja con la cuenta de Battle.net**. Si cada uno tiene su propia cuenta esto no sirve, pero **merece los 2 minutos de comprobación**. ⚠️ Inferencia mía, no confirmada.
2. **Si no funciona (lo más probable):** el de consola usa **`d4lootfilter.com`** en el móvil. Pega ahí el código del filtro que use el de PC y **la web le descompone el filtro en la lista completa de reglas legibles** (nombre, clase de destino, visibilidad, colores, afijos requeridos, tipos de item). Después las teclea a mano en el menú del juego. Con el límite de **25 reglas por filtro**, es tedioso pero perfectamente factible: media hora una vez por temporada.
3. **Alternativa:** el de consola construye su filtro desde cero con **D4 Filter Forge** en el navegador para *visualizar* qué reglas quiere, y luego las teclea. Menos eficiente que la opción 2.

### 11.4 Herramienta del juego que os conviene dominar ya: la Armería (Armory)

No es una herramienta externa, pero es la que más os va a rentar como dúo de min-maxers:

- **Qué hace:** crear **múltiples builds y cambiar entre ellas rápidamente**, guardando **equipo, habilidades, puntos de paragon y glifos**.
- **Coste: completamente gratis** (no cuesta oro).
- **Dónde:** en las ciudades principales, la **Ciudadela Oscura** (Dark Citadel), el **Árbol de los Susurros** (Tree of Whispers) y los **Campos de Entrenamiento** (Training Grounds) — normalmente al lado del alijo.
- **Cuándo llegó:** publicada para el inicio de la **Season 7** (19 de enero de 2025). Página de Maxroll actualizada por última vez el **26 de junio de 2026**.
- ⚠️ **La página de Maxroll no indica si requiere expansión ni si funciona en consola, ni especifica el límite de loadouts.** Otra fuente menciona "hasta cinco builds", pero **no lo he podido verificar directamente**. Como se añadió en la Season 7, más de un año antes de *Lord of Hatred*, y en un parche estacional normal, **casi con seguridad es ✅ juego base** — pero marcadlo como no verificado al 100 %.

**Por qué os importa:** con la Armería, cada uno puede tener una build de empuje de Pit y otra de farmeo rápido sin rehacer el paragon a mano cada vez. Es la diferencia entre jugar y pelearse con el menú.

---

## 12. ⚠️ La trampa nº1 para vosotros: guías que asumen expansiones

**Ninguna de las webs recomendadas os avisa de que una build necesita expansión.** Lo he verificado explícitamente: la página de guías de builds de Maxroll lista las diez builds de nigromante etiquetadas solo como "Season 14 Death Awakening", **sin marcar requisitos de expansión y sin filtro para separar juego base de expansión**.

Peor aún: la **guía de subida de nivel de Nigromante de Icy Veins** (act. 26 de junio de 2026, Season 14; actualizada previamente para *Lord of Hatred* el 26 de abril de 2026) **menciona expresamente contenido de ambas expansiones**:

- 🔒 **Mercenarios (Mercenaries)** durante la campaña — *Vessel of Hatred*
- 🔒 **Kurast Undercity** (desbloqueo a nivel 20) — *Vessel of Hatred*
- 🔒 **Cambios del Árbol de Habilidades y del Libro de los Malditos (Book of the Damned)** + sistema de **War Plans** — atribuidos a *Lord of Hatred*

### 12.1 Checklist para filtrar una guía antes de seguirla

Cuando abráis cualquier guía de nigromante, buscad con Ctrl+F estas palabras. **Si aparecen como requisito, esa build no es para vosotros:**

| Palabra clave (EN / ES) | Expansión | Estado |
|---|---|---|
| Mercenary / Mercenario, Raheir, Subo, Aldkin, Varyana | Vessel of Hatred | 🔒 |
| Runeword, Rune of Ritual, Rune of Invocation / Palabra rúnica, runas | Vessel of Hatred | 🔒 |
| Kurast, Nahantu, Undercity, Dark Citadel | Vessel of Hatred | 🔒 |
| Spiritborn | Vessel of Hatred | 🔒 |
| Warlock, Paladin | Lord of Hatred | 🔒 |
| War Plans | Lord of Hatred (probable) | 🔒 ⚠️ no verificado |

⚠️ **Incertidumbre importante:** los cambios del **Árbol de Habilidades** y del **Book of the Damned** son ambiguos. Icy Veins los atribuye a *Lord of Hatred*, pero **los reworks de sistemas base suelen aplicarse a todos los jugadores vía parche**, mientras que lo que se vende es contenido nuevo. **No he podido confirmar si el rework del Book of the Damned llega al juego base.** Es una de las cosas más importantes que os queda por verificar, porque el Book of the Damned es el sistema central del Nigromante.

### 12.2 Sistemas de Season 14 y el juego base

⚠️ **Fuera de mi dominio de investigación, pero conviene decirlo:** la mecánica estacional (Pandemonium Ruptures), el rework Mythic Unique 3.0, el modo Solo Self-Found, el lair boss Corrupted Reaper y el crossover con Overwatch **no los he verificado respecto a requisitos de expansión** en esta investigación. Históricamente las mecánicas estacionales son para todos los propietarios del juego base, pero **hay que confirmarlo**. La "prueba gratuita de Warlock" implica precisamente que Warlock normalmente 🔒 requiere *Lord of Hatred*.

---

## 13. Comunidades: dónde preguntar

### 13.1 Discords

⚠️ **La fuente que enumera estos servidores es del 4 de julio de 2023.** Los enlaces de invitación y los recuentos de miembros pueden haber cambiado. Verificad antes de fiaros de los números.

| Servidor | Invitación | Miembros (2023) | Para qué |
|---|---|---|---|
| **Sanctuary (oficial de Blizzard)** | discord.gg/diablo4 | 424.274 | Anuncios oficiales, discusión general. **El único oficial** |
| **wudijo** | discord.gg/x8kT6U7Q | 99.532 | **El de expertos.** Canales dedicados por clase (incl. Necromancer), trading, LFG, discusión de builds |
| **The Chaos Sanctuary** | discord.gg/diablo | 66.370 | Uno de los Discords de Diablo más antiguos; canales por clase, comunidad, trading |
| **r/Diablo** | discord.gg/rdiablo | 61.528 | Ligado al subreddit; canales por clase + hardcore, PvP, LFG |
| **Diablo 4 Underground** | discord.gg/diablo4underground | 14.435 | Canales por clase, LFG hardcore/softcore, trading, PvP, world tracker |
| **Diablo 4 Community** | discord.com/invite/diablo4community | ~12.000 | "Chill", moderación buena, discusiones diarias |

**No existe ningún Discord exclusivo de Nigromante** entre los grandes; todos los servidores importantes tienen **canal `#d4-necromancer` o equivalente**.

**Mi recomendación para vosotros:** entrad al **de wudijo** para teorycrafting serio (es donde está la gente que sabe de números) y al **oficial Sanctuary** para noticias. Los demás sobran al principio.

### 13.2 Subreddits

- **r/Diablo4Necromancer** — el subreddit específico de vuestra clase. ⚠️ **No pude abrirlo** (el fetcher no puede acceder a reddit.com), así que **no he verificado su actividad ni su número de miembros en 2026**. Aparece referenciado en búsquedas sobre Season 14, lo que sugiere que sigue vivo.
- **r/diablo4** — el subreddit general grande.
- **r/Diablo** — el subreddit histórico de la saga, con Discord asociado.
- ⚠️ No pude verificar ninguno directamente. Tratad esta sección como "existen y son las referencias habituales", no como verificada.

### 13.3 Creadores de contenido activos en Season 14

**Verificado que tienen contenido de Season 14 vivo:**

- **wudijo** — tiene **página de autor propia en Maxroll** (`maxroll.gg/@wudijo`) con build guides, planners y estrategias. Es la referencia de rigor numérico de la comunidad y tiene el Discord de teorycrafting más serio. **Sigue activo en S14.**
- **MacroBioBoi** — **página de autor propia en Maxroll** (`maxroll.gg/@macrobioboi`). Referencia de matemáticas de daño.
- **p4wnyhof** — tiene perfil en Mobalytics con un "Season 14 Necro Hub" y una build "Trillion Burst Army of the Dead Necro". **Activo en S14 y específicamente centrado en nigromante.**

**Contenido de Nigromante S14 verificado en YouTube** (títulos localizados en búsqueda, canales no identificados individualmente):
- "BROKEN Army of the Dead Necromancer Build (Season 14)"
- "Cold Necro is Finally Viable! Frozen Reaper Necromancer"
- "This Minion Necromancer DESTROYS Torment 12!"
- "Big D Spirit Necromancer Endgame Guide" (DoT meta)
- "One Necro Build to Rule them All — Tanky + T12 Mephisto"
- "S14 BEST Summon Necro Endgame Build (PIT 114 SHOWCASE)" ⚠️ etiquetado como "Lord of Hatred Necromancer Guide" → **probablemente requiere expansión**

⚠️ **No pude confirmar actividad en S14 de Rob2628 ni de Lurkin.** No aparecieron en los resultados de búsqueda de nigromante S14. **No significa que estén inactivos**, solo que no lo he verificado.

---

## 14. Stack recomendado para vosotros dos

**Fase 1 — Subir de nivel (ahora mismo):**
1. **Icy Veins → guía de subida de nivel de Nigromante** (act. 26/06/2026, S14). Aplicad la checklist de la sección 12.1 mientras la leéis.
2. **Maxroll World Map** en el móvil para los Altares de Lilith y el renombre. Uno de los dos lleva el tracking por los dos.
3. **helltides.com** en el móvil con notificaciones activadas, para no perderos jefes del mundo ni Helltides.

**Fase 2 — Primer endgame:**
4. **Filtro de botín oficial en el juego**: el de PC importa un filtro de Maxroll/Mobalytics; el de consola lo descodifica en **d4lootfilter.com** y lo teclea (25 reglas máx.).
5. **Armería del juego** para tener build de farmeo y build de push.
6. **Maxroll → tablas de botín de jefes** para saber a quién farmear cada unique.

**Fase 3 — Min-max de verdad:**
7. **Maxroll → In-Depth Damage Guide** (act. 12/06/2026). Entender `[+]` vs `[x]` antes que nada.
8. **Maxroll D4Planner** para planificar cada pieza antes de gastar materiales.
9. **jlian.github.io/d4-damage-calc/** para saber qué stat concreto os da más rendimiento ahora.
10. **helltides.com/pit** para ver qué está haciendo la gente que empuja de verdad, y con qué builds.
11. **Discord de wudijo, canal de nigromante**, para preguntar las dudas finas.

**Lo que NO instaláis:** nada. Ni Overwolf, ni Diablo4Companion, ni d4lf. ⚠️

---

## 15. Incertidumbres y contradicciones

### 15.1 Contradicciones directas entre fuentes (reportadas, no promediadas)

1. **🔴 ¿El filtro de botín oficial requiere *Lord of Hatred*?**
   - **Icy Veins** (citando a Blizzard) y la **wiki de Fextralife**: **NO**, es para todos, parte del juego base.
   - **Maxroll**: **SÍ**, requiere la expansión y no está en el juego base.
   - *Sin resolver.* Mi apuesta: es juego base ✅. **Comprobadlo vosotros en Opciones → Jugabilidad.**

2. **🔴 ¿En qué parche llegó el filtro de botín?**
   - **Icy Veins / Fextralife / Maxroll**: con *Lord of Hatred* (parches 3.0.1a y 3.0.2 citados como correctivos).
   - **D4 Filter Forge**: "desde el parche 2.1, cuando D4 añadió soporte nativo de filtros".
   - *Sin resolver.*

3. **🔴 ¿Puede la consola importar códigos de filtro?**
   - **Maxroll** y **d4lootfilter.com**: **NO**, solo PC; en consola hay que hacerlo a mano.
   - **D4 Filter Forge**: el formato es multiplataforma y viaja con la cuenta de Battle.net.
   - *Probablemente compatibles* (no puedes *pegar* un código en consola, pero el filtro puede sincronizar por cuenta), **pero es una inferencia mía sin fuente que lo confirme**.

4. **🔴 Estado de actualización de helltides.com**
   - Su portada muestra texto de "Season 6" y versión de sitio v5.2.6.
   - Su sección Pit está actualizada al 18/08/2026 con datos de Season 14.
   - *Interpretación: sitio vivo con texto viejo sin limpiar.*

5. **🟡 Fecha de la página de filtro de botín de Maxroll**
   - El extractor devolvió "actualizada el 21 de julio de 2026, lo que corresponde a Season 4 (Season of Loot Reborn)". La fecha y la temporada son **incoherentes entre sí** (julio 2026 es Season 14, no Season 4). Probable error del extractor, pero lo señalo.

6. **🟡 Composición del leaderboard de Pit**
   - Un snapshot dice que los 11 primeros puestos son todos Rogue; otro sitúa un Nigromante en el puesto #8 (Tier 139). Son instantáneas de momentos distintos de un ranking que cambia a diario.

### 15.2 Cosas que NO he podido verificar

- **Ninguna declaración de Blizzard de 2026 sobre software de terceros.** Toda la política documentada es de 2023–2024 + EULA de 21/03/2024. **No he podido confirmar que no haya cambiado tras *Lord of Hatred*.**
- **Ninguna oleada de baneos documentada** específicamente por Diablo4Companion, d4lf u Overwolf. Ausencia de evidencia ≠ evidencia de ausencia.
- **Mobalytics: todos mis intentos de abrir sus páginas devolvieron HTTP 403.** Todo lo que digo de Mobalytics viene de fragmentos de búsqueda, no de lectura directa de la página.
- **InfinityBuilds / InfinityTools: HTTP 403.** Su existencia y actividad quedan confirmadas indirectamente (Diablo4Companion añadió soporte de importación en julio de 2026), pero no he leído su web.
- **PureDiablo, DiabloFilter, DiabloBytes: HTTP 403.** Sin verificar.
- **Reddit: el fetcher no puede acceder a reddit.com.** Toda la sección de subreddits está sin verificar.
- **Si la Armería del juego requiere expansión** y **cuántos loadouts permite** exactamente. La cifra de "cinco" aparece en una fuente secundaria sin verificar.
- **Si el rework del Book of the Damned / Árbol de Habilidades de *Lord of Hatred* llega al juego base.** Crítico para vosotros y sin resolver.
- **Si el comercio directo funciona entre PC y consola.** Documentado el requisito de "misma instancia de mundo"; el cross-play debería bastar, pero sin confirmación explícita.
- **Precios de mercado de Mythics.** Cifras vistas en búsqueda, no verificadas, y de sitios RMT que no recomiendo.
- **Actividad en S14 de Rob2628 y Lurkin.** No aparecieron en las búsquedas de nigromante S14.
- **Para qué parche está actualizada la calculadora de daño de jlian.** La página no lo indica.
- **Si "Guide for D4", "Map and Timers for Diablo 4" y "D4Tools" (apps móviles) siguen actualizadas en 2026.** Solo verifiqué D4Planner iOS, que está muerta desde noviembre de 2023.
- **El presupuesto de búsquedas web de esta sesión se agotó** (200/200) antes de poder cerrar los puntos de política de Blizzard 2026 y de verificar varias apps móviles. Varias páginas devolvieron 403 al fetcher. Esta investigación es sólida en lo verificado, pero **hay huecos reales y están todos listados aquí**.

---

## Fuentes

Páginas realmente abiertas y leídas con WebFetch (18 de agosto de 2026):

- https://maxroll.gg/d4
- https://maxroll.gg/d4/build-guides
- https://maxroll.gg/d4/planner
- https://maxroll.gg/d4/resources/loot-filter
- https://maxroll.gg/d4/resources/trading
- https://maxroll.gg/d4/resources/armory
- https://maxroll.gg/d4/resources/in-depth-damage-guide
- https://maxroll.gg/d4/news/diablo-4-map-tool-is-live
- https://d4builds.gg/
- https://www.icy-veins.com/d4/guides/necromancer-leveling-guide/
- https://www.icy-veins.com/d4/news/after-years-of-requests-diablo-4-will-finally-get-a-loot-filter/
- https://diablo4.wiki.fextralife.com/Loot+Filters
- https://www.wowhead.com/diablo-4/event-timers
- https://helltides.com/
- https://helltides.com/pit
- https://d4planner.io/trackers
- https://d4filterforge.com/
- https://www.d4lootfilter.com/guide
- https://jlian.github.io/d4-damage-calc/
- https://github.com/josdemmers/Diablo4Companion
- https://github.com/josdemmers/Diablo4Companion/releases
- https://github.com/josdemmers/Diablo4Companion/wiki/How-to-import-and-export-builds
- https://github.com/d4lfteam/d4lf
- https://github.com/d4lfteam/d4lf/releases
- https://www.overwolf.com/browse-by-game/diablo-iv
- https://us.forums.blizzard.com/en/d4/t/third-party-app-diablo-iv-overlay-is-permitted-modcheck/41715
- https://us.forums.blizzard.com/en/d4/t/third-party-app-diablo-iv-overlay-is-permitted-modcheck/41715/2
- https://www.blizzard.com/en-us/legal/08b946df-660a-40e4-a072-1fbde65173b1/blizzard-end-user-license-agreement
- https://mythicdrop.com/guide/diablo-4-discord-servers
- https://apps.apple.com/us/app/d4planner-diablo-4-planner/id6447534049
- https://d4armory.io/ (comprobado: redirect 301 → diablo4.com → diablo4.blizzard.com; herramienta desaparecida)

**Páginas que devolvieron HTTP 403 y NO pude leer** (menciones en el informe basadas solo en fragmentos de búsqueda):
- https://mobalytics.gg/diablo-4 y todas sus subpáginas
- https://infinitybuilds.gg/en · https://tools.infinitybuilds.gg/en
- https://www.purediablo.com/diablo-4-helltide-boss-timer
- https://diablofilter.com/
- https://diablobytes.com/diablo-iv/lord-of-hatred/loot-filter/

**Inaccesible para el fetcher:** https://www.reddit.com/r/Diablo4Necromancer/
