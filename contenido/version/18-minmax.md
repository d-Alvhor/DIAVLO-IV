---
titulo: Min-max de verdad
capa: version
parche: "3.1.3"
temporada: 14
estado: vivo
entitlement: base
verificado: 2026-08-19
revisar_despues: 2026-10-15
---

## Vuestro techo, dicho sin adornos

Pedisteis nivel de clasificación (*leaderboard*). La respuesta honesta es que con juego base llegáis a la **parte media-alta** de las tablas, no al top-100. Y no es opinión: es aritmética de capas multiplicativas que os faltan, en una tabla que **no separa por expansión**.

::: evidencia nivel=corroborado fuentes=icyveins-runewords,maxroll-minion-guide,blizzard-loh-oficial
Las cuatro capas de potencia que no tenéis y que sí lleva vuestro rival de tabla:

| Capa | Expansión | Cifra documentada |
|---|---|---|
| *Runewords* — runa `Gar` | 🔒 Vessel of Hatred | apila **2,5 % de probabilidad de crítico por acumulación, hasta 25 %** en 5 s |
| Mercenario (*Mercenary*) — Subo | 🔒 Vessel of Hatred | **+25 %** de multiplicador de daño crítico |
| Talismán + *Charms* de 6 huecos, con bonus de set | 🔒 Lord of Hatred | multiplicador; magnitud exacta no publicada |
| Cubo Horadrim (*Horadric Cube*) → Míticos crafteados | 🔒 Lord of Hatred | **+30 %** de Poder de Único, afijos al máximo, Ancestral siempre |
:::

::: aviso tipo=ojo
**Nadie ha publicado cuánto DPS exacto cuesta esto.** Las cifras que circulan por foros («te pierdes el 60-80 % del endgame») son opinión sin respaldo y no las vais a ver aquí. Está documentado *qué* falta, no *cuánto* pesa.
:::

Lo que perdéis y duele más que el daño es el **determinismo**. Sin Cubo no fabricáis Míticos, los recibís: vuestro min-max depende de RNG donde el del otro depende de una receta. Contrapartida irónica: como no crafteáis, el límite de «un solo Mítico crafteado equipado» no os afecta y podéis equipar todos los que os caigan.

**El muro está reportado en la transición Tormento VII → VIII, en torno a Pozo 60.** Antes de ahí el juego base es completo. Después, cada piso que la gente sube lo sube con multiplicadores que vosotros no tenéis.

::: evidencia nivel=unica fuentes=icyveins-tower
El criterio de la Torre (*The Tower*) es el **piso más alto completado**; el tiempo solo desempata. Hay tramos de recompensa **top 1000 / 500 / 100 / 10 / 1**, y el **top 1000 reparte recompensa material**, no solo cosmética. Existe tabla propia para **grupos de 2**.
:::

Ese top 1000 en la categoría de dúo es vuestro objetivo realista de primera temporada. Es digno y es alcanzable. El top-100 no lo es sin las cuatro capas.

## Objetivos de estadística, build por build

Lo más accionable del capítulo. Son los objetivos que **publican las guías**, no medidas propias: aquí no se ha probado nada en el juego. Varias guías usan `>`, o sea son **mínimos**, no valores exactos.

::: evidencia nivel=corroborado fuentes=maxroll-minion-guide,maxroll-blood-surge,maxroll-blood-wave,maxroll-bone-spear
| Build | Vel. ataque | Crítico | Regen. Esencia | RCR | Vida |
|---|---|---|---|---|---|
| **Esbirros (Minion)** | 100 % | 100 % | — | — | 30.000 mín. |
| **Blood Surge** | >70 % con *Ferocity* | >85 % con *Bone Storm* | >10 | >15 % | — |
| **Blood Wave** | 50 %+ con *Ferocity* | 70 %+ | 15+ | 15 %+ | — |
| **Bone Spear** | 100 % con *Frenzy* + *Bone Storm* | 100 % con *Bone Storm* + *Decrepify* | — | **no bajar** (ver trucos) | 30.000+ |
:::

::: evidencia nivel=unica fuentes=maxroll-bone-spirit,maxroll-golem,maxroll-sever,maxroll-blight
Las builds vetadas para juego base, por si acabáis pivotando: **Bone Spirit** y **Golem** piden 100 % de velocidad de ataque, 100 % de crítico y 30.000+ de vida. **Sever** pide ~100 % y ~100 % con buffs, más **14–28 de regeneración de Esencia**. **Blight** pide 10–15 de regeneración, >90 % de velocidad con *Ferocity*, ~100 % de crítico con *Bone Storm* y >10 % de RCR.
:::

::: evidencia nivel=unica fuentes=maxroll-necro-builds
Patrón que conviene interiorizar: **casi todo el catálogo converge en 100 % de velocidad de ataque y 100 % de crítico**, y esos 100 % no salen de stats planos — salen *dentro de la ventana de un enfriamiento activo* (*Bone Storm*, acumulaciones de *Ferocity*, *Frenzy*). Vuestro problema no es llegar al 100 %; es **llegar al 100 % durante la ventana en la que disparáis**.
:::

::: aviso tipo=peligro
Vuestro objetivo de crítico es más difícil que el de la guía, porque la guía cuenta con `Gar` (hasta 25 %) y con Subo (+25 % de daño crítico), y vosotros no. **Compensadlo en joyería, gemas y rangos de *Bone Storm*.** Si copiáis una lista de templados de guía tal cual, os quedaréis cortos de crítico y no sabréis por qué.
:::

## Breakpoints: los que deciden y los que están en disputa

Un breakpoint es un umbral donde el rendimiento salta de golpe. En vuestro caso hay cuatro que mandan sobre todo lo demás.

**1 · El radio del glifo.** Es el multiplicador más barato del juego, y está en disputa entre fuentes vivas.

::: evidencia nivel=disputa fuentes=icyveins-glyphs,skycoach-glifos,maxroll-paragon
Dos versiones incompatibles, ambas de fuentes vivas de la S14:
- **Icy Veins y Skycoach:** radio 3 en niveles 1–14 → **radio 4 al nivel 15** → **radio 5 al nivel 50**; Raro pasa a Legendario al **51**; tope **150**.
- **Maxroll:** radio 4 al **25**, radio 5 al **51**; tope 150.

Coinciden en el tope (150) y en que el salto a Legendario está en el entorno del 50-51. No coinciden en el primer salto de radio. **Se cierra mirando el tooltip en vuestra pantalla.**
:::

**2 · El requisito de atributo del glifo.** Cada glifo tiene dos capas: un escalado lineal («por cada 5 de [atributo] comprado dentro del radio») y un **bonus multiplicativo bloqueado** detrás de un umbral.

::: evidencia nivel=unica fuentes=game8-paragon
Ejemplo verificado, glifo **Control**: escala a **+2,0 % de daño a objetivos con Control de Masas por cada 5 de Inteligencia** comprada en radio, y requiere **+40 de Inteligencia** en radio para activar el bonus adicional de **20 %[x]** para ti y tus esbirros. No está confirmado si el umbral de 40 es universal o varía por glifo.
:::

El multiplicativo vale muchísimo más que el escalado lineal. Orden de prioridad: **cumplir el umbral de atributo primero, subir el glifo a 50/51 después, y solo entonces rellenar atributo para el escalado lineal.** Rellenar antes de tener radio 5 es tirar puntos.

**3 · El piso del Pozo del Artífice (*The Pit*) que garantiza subida.**

::: evidencia nivel=corroborado fuentes=maxroll-pit-guide,icyveins-glyphs
Completar un Pozo **10 pisos por encima del nivel del glifo garantiza la subida** (100 %). Por cada **20 pisos** que el Pozo esté por encima del glifo, **cada intento da un nivel adicional**. Ejemplo trabajado publicado: Pozo **50** completado sin morir sobre un glifo de nivel **10** reparte **+3, +2, +2, +2** en los cuatro intentos.
:::

::: evidencia nivel=disputa fuentes=maxroll-pit-guide,maxroll-endgame-progression
Intentos por incursión: la versión mayoritaria dice **3 intentos, +1 si terminas sin morir = 4**. Una fuente dice **4 + 1 = 5**. Sin resolver. Lo que no está en disputa: **morir cuesta un intento**.
:::

**4 · El rango de habilidad.** Este es el breakpoint que cambia toda la planificación y que casi ninguna guía en castellano menciona.

::: evidencia nivel=corroborado fuentes=maxroll-skill-trees,datos-juego-3-1-0
Cada habilidad activa admite **15 rangos**, no 5 (el fichero de datos del juego, versión 3.1.0.72698, marca `ranks: 15` en las 23 habilidades del Nigromante). Y la regla de rendimiento publicada por Maxroll: *«cada punto extra hace la habilidad un 10 % más potente de lo que era a rango 1… el primer punto que metes en una habilidad activa es diez veces más potente que los cuatro siguientes»*.
:::

Traducción operativa: **amplitud primero, profundidad al final**. Subir *Skeleton Mage* a 5/15 antes de tener Gólem, *Coven* y *Master of Puppets* es la forma más común y más cara de tirar puntos.

## Topes y presupuestos

Min-maxear es repartir presupuestos finitos. Estos son los vuestros.

::: evidencia nivel=disputa fuentes=maxroll-skill-trees,blizzard-loh-oficial,foro-blizzard
**Presupuesto de puntos de habilidad.** Maxroll: **80** = 68 por subir de nivel (uno por nivel del 2 al 69) + **12** del Rango de Temporada. Blizzard, en su blog: *«up to 83 available Skill Points»*. Un usuario del foro oficial: **81**, porque 2 de esos puntos vienen del Renombre de Skovos 🔒. **Planificad con 80.** Si os sobran, mejor.
:::

Con **80 puntos y 15 rangos por habilidad**, el árbol da para llevar al máximo **cinco habilidades como mucho** —y eso sin gastar un solo punto en modificadores ni variantes—. Ese es el techo duro que gobierna vuestro reparto.

::: evidencia nivel=unica fuentes=icyveins-summoner
Los puntos del Rango de Temporada **no abren clústeres**: *«los puntos de habilidad del Rango de Temporada o del Renombre no afectan al progreso del árbol y se pueden asignar a rangos de habilidad ya desbloqueados»*. Son munición pura de profundidad.
:::

::: evidencia nivel=corroborado fuentes=maxroll-paragon,maxroll-paragon-experience
**Presupuesto de Paragón:** 300 niveles (1 punto cada uno) + **42** del Rango de Temporada = **342 puntos**, repartidos entre **5 tableros** (el inicial + 4 acoplados) de 70–180 nodos cada uno. No podéis coger ni de lejos todos los nodos: **cada nodo común que cogéis de paso es un multiplicador que no cogéis**.
:::

::: evidencia nivel=unica fuentes=datos-juego-3-1-0
**Topes de ejército** (fichero de datos del juego, 3.1.0.72698): Guerreros base **4**, **+3** con *Master of Puppets* ✅, **+2** con la mejora A de Escaramuzadores. Magos base **3**, **+2** con *Coven* ✅. Cada Sacrificio multiplica la cantidad por **0,5**.
:::

::: aviso tipo=peligro
El «tope de 28 esbirros» que circula por internet **no es una cifra oficial**: procede de un periodista escribiendo *«lo que parecen 28»*. No planifiquéis con ella.
:::

## Rotaciones

Una rotación no es una lista de teclas: es el orden que hace coincidir la ventana de daño con la de buffs. Estas son las publicadas.

::: build nombre="Ancla — Esbirros" estado=intermedia entitlement=base
Abrir con **Zarcillos de Cadáver** (*Corpse Tendrils*) para agrupar → **Gólem preventivo** antes de élites peligrosas, que activa Imparable (*Unstoppable*) y acumula *Ferocity* → **Comando de Guerreros** sobre el objetivo prioritario (el multiplicador del 25 % es manual, no se aplica solo) → **Sever** en bucle para generar cadáveres → los Magos los consumen solos. Vuestro trabajo es moveros y **mantener la maldición**; los esbirros pegan.
:::

::: build nombre="Martillo — Blood Surge" estado=intermedia entitlement=base
**Bone Storm** al entrar en el pack (es vuestra ventana de crítico) → **Corpse Tendrils** para juntarlo → **Bone Prison** por el bonus de velocidad de ataque → **spam de Blood Surge** → **Sever** para saltar al siguiente grupo → **Decrepify a mano** cuando toque élite o jefe, porque no tenéis la runa `Wat` que lo automatiza.
:::

::: evidencia nivel=unica fuentes=maxroll-blood-wave,maxroll-bone-spear
**Blood Wave:** *Sever* para cerrar distancia y hacer cadáveres → *Corpse Tendrils* para Vulnerable → *Bone Prison* → **spam de Blood Wave pegado al pack** (la guía insiste en quedarse cerca) → *Blood Mist* para teletransportar y consumir cadáveres → *Blood Lance* solo para mantener Sobrepoder (*Overpower*). **Bone Spear:** lanzas *Bone Storm* y luego spameas *Bone Spear*; **cada 4 lanzamientos recortas segundos del enfriamiento de Bone Storm** vía *Aspect of Rapid Ossification*.
:::

**La capa de dúo que ninguna guía escribe, porque todas asumen expansión.** Sin runas `Teb` ni `Wat`, cubrir Decrepitud (*Decrepify*) **e** Doncella de Hierro (*Iron Maiden*) cuesta dos huecos de barra. **Llevad una cada uno**: os devuelve un hueco por cabeza y es la mejor compensación disponible por no tener *runewords*. El ancla sostiene además Vulnerable, que sube el daño de **todas** las fuentes, las del compañero incluidas.

## Los trucos contraintuitivos

Aquí es donde se separa el que ha leído una guía del que ha entendido el sistema.

::: evidencia nivel=unica fuentes=maxroll-necro-builds
**1 · En Bone Spear, NO reduzcáis el coste de Esencia.** Es lo contrario de lo que hacen Blood Surge y Blood Wave, que persiguen 15 % de RCR.
:::

::: evidencia nivel=unica fuentes=maxroll-bone-spear
Cuanta más Esencia gastáis por lanzamiento, más procs de *Aspect of Rapid Ossification* y más reinicios de *Bone Storm*. La guía reporta además que los **Magos Esqueléticos aportan una regeneración de Esencia enorme**, que es la razón de que la build «dependa de la utilidad de esbirros». La reducción de coste os quita procs.
:::

**2 · Los Sacrificios esconden una línea que ninguna guía web publica.**

::: evidencia nivel=unica fuentes=datos-juego-3-1-0
Los **nueve** Sacrificios de Guerreros y de Magos del Libro de los Muertos incluyen una segunda línea: **«Tu Gólem gana 60 %[x] de daño»**. Los Sacrificios de Gólem **no** la tienen. Mismo patrón en los nueve tooltips del fichero de datos. Si sacrificáis guerreros o magos, **vuestro Gólem pasa a ser el pilar de daño de la build**, lo sepáis o no.
:::

**3 · Guardar puntos sin gastar no retrasa nada.** Los clústeres se abren por **nivel de personaje** (`requiredLevel` en el fichero del juego), no por puntos gastados: podéis subir tres niveles sin tocar el árbol y se abren igual. Cualquier guía que hable de «23 puntos para Definitivas» describe el árbol de 2024 y está muerta.

**4 · No construyáis alrededor de un socket de glifo demasiado pronto.**

::: evidencia nivel=unica fuentes=maxroll-paragon
Cita de Maxroll: *«construir alrededor de un socket pronto probablemente reduce tu poder… normalmente es mejor esperar a invertir fuerte en sockets hasta que estén suficientemente subidos de nivel»*. Con radio 3 y sin bonus legendario, gastar 15 puntos rodeando un glifo bajo de Inteligencia es pérdida neta.
:::

**5 · Saltaos los clústeres de Resistencia al principio.** Instrucción explícita de las dos guías de invocador de Icy Veins: anotad dónde están y volved sobre Paragón ~250, cuando ya tengáis el daño aditivo cogido. La resistencia tiene rendimiento decreciente y en el Paragón temprano necesitáis el multiplicador.

**6 · Acoplad pronto los tableros cuyos nodos raros queráis activar barato.** El umbral del tercer bonus de un nodo raro **sube con cada tablero que acopláis**, y se mide contra vuestro atributo **total** —equipo y aspectos incluidos—, no solo contra lo gastado en el tablero. Un nodo raro que hoy parece muerto se enciende cambiando de amuleto.

::: evidencia nivel=unica fuentes=maxroll-necro-builds
**7 · Imprimid vuestro mejor aspecto ofensivo en el AMULETO.** Es la pieza que menos se reemplaza y **multiplica el efecto del aspecto un 150 %**. Lo repiten todas las guías y casi nadie lo hace.
:::

**8 · El Pozo es la peor fuente de XP por minuto y la única fuente de nivel de glifo.**

::: evidencia nivel=unica fuentes=maxroll-paragon-experience
XP publicada por actividad: **Hellwyrm** en Marea Infernal **~30,9 M**, Rupturas con Writhe/Rot **~21 M**, Rupturas Surgentes **~10,7 M**, Rupturas normales **~6,2 M**, **Pozo piso 100 ~3,6 M**. Coste total hasta Paragón 300: **~58.200 millones de XP**.
:::

Conclusión operativa: **Paragón en Marea Infernal y Rupturas; al Pozo solo a subir glifos.** Y dentro del Pozo, corred el piso más alto que limpiéis **rápido y sin morir**, no el más alto que sobreviváis.

::: evidencia nivel=unica fuentes=datos-juego-3-1-0
**9 · *Pile the Bodies* es un cebo.** Su «300 %[x]» es el número más grande de la pantalla y escala una Definitiva con enfriamiento largo. *Unyielding Commander* ✅ está activa casi siempre. Elegid la segunda.
:::

**10 · Tres trucos que son avisos.** El tablero *Wither* pasó a **daño de Frío** en 3.1.0: si lo cogéis, vuestro escalado tiene que ir a Frío. *Blood Mist* fue reclasificada como habilidad de **Movilidad**, lo que cambia qué aspectos la tocan. Y el glifo *Dominate* fue nerfeado pese a aparecer en media docena de listas de subida: **comprobad su tooltip antes de invertir 100 niveles en él**.

**11 · Reparto antes que crafteo.** En dúo, si un objeto le sirve al otro, **pasádselo antes** de encantarlo o masterworkearlo: el primer clic lo deja pegado a esa cuenta para siempre.

## Lo que nadie ha publicado y os afecta

Huecos declarados. Ninguno relleno con conjetura.

- **El texto exacto de los glifos más usados de la clase** —*Essence*, *Warrior*, *Mage*, *Exploit*, *Gravekeeper*, *Imbiber*, *Abyssal*— no está en ninguna fuente accesible, y son justo los de vuestras listas de subida. Máxima prioridad de verificación en pantalla.
- **El nodo legendario del tablero *Cult Leader* tiene dos versiones incompatibles** en las fuentes: una escala con la velocidad de ataque de los esbirros, otra con el número de tipos de esbirro activos. **Son mecánicas distintas y cambian el itemizado entero.** Sin resolver.
- **Qué significa exactamente `ranks: 3`** en los nodos de modificador y variante del fichero de datos. Si admiten tres puntos cada uno, maximizar una habilidad costaría 15 + 3×3 = **24 puntos** en vez de 15 + 3. Afecta directamente a vuestro presupuesto. **Se cierra pulsando dos veces un nodo de modificador.**
- **No existe ninguna tabla de DPS comparable publicada** para las builds del Nigromante en la S14. Las columnas de «techo de daño» de cualquier guía, incluida esta, son ordinales, no numéricas.
- **El Gólem de Hueso puede estar bugueado**: un jugador del foro **oficial** reporta que no aplica Vulnerable como promete su tooltip, sin respuesta de Blizzard. No construyáis asumiendo esa Vulnerabilidad sin comprobarla.

## Las comprobaciones que valen puntos

Cinco minutos de vuestro tiempo cierran huecos que ninguna web ha cerrado en tres pasadas de investigación.

::: paso n=1 obligatorio=si entitlement=base
Pulsad **dos veces** un nodo de modificador del árbol. Si admite un segundo y un tercer punto, cada habilidad maximizada os cuesta 24 puntos en vez de 18, y toda la planificación cambia.
:::

::: paso n=2 obligatorio=si entitlement=base
Pasad el ratón (o el cursor del mando) por el **tooltip de un glifo** y anotad a qué nivel salta el radio. Cierra la disputa 15/50 contra 25/51 y evita cientos de incursiones al Pozo malgastadas.
:::

::: paso n=3 obligatorio=si entitlement=base
Comprobad cuántos **intentos de mejora** os da una incursión al Pozo terminada sin morir. Si son 4 y no 5, vuestro calendario de glifos se alarga un 25 %.
:::

::: paso n=4 obligatorio=no entitlement=base
Mirad el **requisito de atributo** de tres glifos distintos. Si los tres piden 40, el 40 es universal y planificáis el reparto de Inteligencia de una vez.
:::

::: aviso tipo=truco
El min-max más rentable que tenéis disponible hoy no es un objeto: es **no morir en el Pozo**. Un intento extra por incursión, repetido durante una temporada, es la única fuente de poder del juego que **no depende de RNG ni de expansión**. Los que van por delante en la tabla tienen mejores multiplicadores; no tienen mejores glifos si vosotros corréis limpio.
:::
