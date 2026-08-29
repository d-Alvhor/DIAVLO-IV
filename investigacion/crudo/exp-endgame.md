# Endgame exclusivo de expansión — Temporada 14 "Death Awakening", parche 3.1.3

**Fecha del informe:** 20 de agosto de 2026
**Parche vivo declarado por el jugador:** 3.1.3 (build 73224, 12/08/2026)
**Fin de temporada:** martes 15 de septiembre de 2026 → quedan **~26 días**
([blizzardwatch.com](https://blizzardwatch.com/2026/07/17/diablo-4-season-15-start-september-15/) — ojo: la fecha viene del temporizador del Relicario in-game, **Blizzard no la ha anunciado oficialmente**)

**Perfil:** Nigromante de esbirros, nivel 70 (máximo), Paragón 0, acaba de comprar **Vessel of Hatred** y **Lord of Hatred**. Juega en dúo (PC + PS5).

---

## 0. Aviso de método — léelo antes que la tabla

Tres cosas que este informe hace distinto y que conviene que sepas:

1. **Todo número lleva su URL en la misma línea.** Lo que no aparezca escrito en una fuente fechada dentro de 3.1.x va a la sección `## No encontrado`, no se reconstruye.
2. **Hay una fuente de datamining.** El planificador de Maxroll sirve el fichero de datos del juego en `https://assets-ng.maxroll.gg/d4-tools/game/data.min.json`. Lo he descargado hoy: `last-modified: Tue, 18 Aug 2026 15:42:02 GMT`, 11.606.376 bytes. **Pero su campo `version` dice `3.1.0.72698`**, no 3.1.3/73224. O sea: el fichero se re-sirvió ayer pero el contenido corresponde a la build 72698. Es la fuente más literal que existe para nombres y textos de nodos e ítems, y a la vez **puede ir por detrás del parche vivo en un par de builds**. Todo lo marcado `[datamining]` viene de ahí y hereda ese asterisco.
3. **He encontrado dos modelos muertos circulando** en mi dominio. Están en la sección 6. Uno de ellos (el renombre) te haría perder horas esta temporada para nada.

**Leyenda:** 🆕 = contenido que el jugador **acaba de desbloquear hoy** al comprar las dos expansiones.

---

## 1. Veredicto de prioridad para las 4 semanas que quedan

| # | Sistema | ¿Nuevo hoy? | Requisito | Prioridad para Paragón+equipo en 4 semanas | Por qué |
|---|---|---|---|---|---|
| 1 | **Planes de Guerra** (War Plans) | 🆕 LoH | Campaña de Lord of Hatred completada | **MÁXIMA — es la llave de todo lo demás** | Es el sistema que *modifica* el resto de actividades. Sin él, la Undercity y las Mareas Infernales rinden en modo base. Maxroll lo llama "incredibly important for character progression" ([maxroll](https://maxroll.gg/d4/meta/endgame-progression), act. 09/07/2026) |
| 2 | **Ciudad Subterránea de Kurast** (Undercity) | 🆕 VoH | VoH + campaña VoH hasta la misión prioritaria | **MUY ALTA** | Única actividad del juego donde **eliges el botín antes de entrar** vía Tributo ([maxroll](https://maxroll.gg/d4/resources/kurast-undercity), act. 16/07/2026). Es literalmente un grifo dirigible |
| 3 | **Skovos / Temis** | 🆕 LoH | Lord of Hatred | **ALTA, pero solo como camino** | Temis es el hub del endgame: ahí está la mesa de mando de los Planes de Guerra ([Blizzard](https://news.blizzard.com/en-us/article/24267729/prepare-for-the-reckoning-lord-of-hatred-draws-near)) |
| 4 | **Ciudadela Oscura** (Dark Citadel) | 🆕 VoH | VoH + nivel 60 + Tormento + misión con la Sacerdotisa Cualli | **BAJA-MEDIA, semanal** | Una pasada semanal por el cofre y por Prismas Dispersos. No es un motor de farmeo (ver §4) |
| 5 | **Nahantu (zona)** | 🆕 VoH | VoH | **BAJA** salvo como puerta a la Undercity | La zona en sí es contenido de campaña |
| 6 | **Renombre / Tenets of Akarat / Chronicles of Creation** | 🆕 (ambas) | — | **CERO ESTA TEMPORADA** | El renombre **solo funciona en el reino Eterno** desde el parche 2.5.0. Ver §6.1. Esto es el error caro |

---

## 2. 🆕 CIUDAD SUBTERRÁNEA DE KURAST (Kurast Undercity)

### 2.1 Cómo se desbloquea

| Dato | Valor | Fuente |
|---|---|---|
| Expansión | **Vessel of Hatred** (obligatoria) | [icy-veins.com/d4/guides/kurast-undercity-guide](https://www.icy-veins.com/d4/guides/kurast-undercity-guide/) |
| Requisito de nivel | **Nivel 20** | [icy-veins](https://www.icy-veins.com/d4/guides/kurast-undercity-guide/) |
| Requisito de nivel (contradicción) | **Nivel 25** | [icy-veins.com/d4/news/fastest-diablo-4-season-14-leveling-route](https://www.icy-veins.com/d4/news/fastest-diablo-4-season-14-leveling-route/) — *dos páginas de la misma casa se contradicen; ver `No encontrado`* |
| Acción de desbloqueo | Avanzar la campaña de VoH hasta recibir una misión prioritaria de explorar las profundidades de la Undercity; completarla desbloquea permanentemente el **Brasero de Espíritus** (Spirit Brazier) | [maxroll](https://maxroll.gg/d4/resources/kurast-undercity) |
| Acción de desbloqueo (variante) | "Invocar la Llama de Espíritus" (Invoke the Spirit Flame) en la región de Nahantu | [icy-veins](https://www.icy-veins.com/d4/guides/kurast-undercity-guide/) |
| Personajes alternos | Tras el desbloqueo inicial, **todos tus alts tienen acceso desde nivel 1** | [icy-veins](https://www.icy-veins.com/d4/guides/kurast-undercity-guide/) |

**Para ti, hoy:** ya tienes VoH. Si no habías tocado la campaña de VoH, esa misión prioritaria es tu primer trámite. Es un trámite, no un proyecto.

### 2.2 El modelo real: **Tiempo** + **Sintonía**, dos relojes distintos

Aquí está la primera corrección de modelo. Guías antiguas describen la Undercity como "un temporizador que alargas encendiendo braseros de Fuego Sagrado". El modelo vigente en 3.1.x tiene **dos** variables separadas:

**(a) Tiempo (Time)** — el temporizador de la carrera.

| Tributo ofrecido | Tiempo inicial | Fuente |
|---|---|---|
| Ninguno | **120 segundos** | [maxroll](https://maxroll.gg/d4/resources/kurast-undercity) |
| Raro | **75 segundos** | [maxroll](https://maxroll.gg/d4/resources/kurast-undercity) |
| Legendario | **60 segundos** | [maxroll](https://maxroll.gg/d4/resources/kurast-undercity) |

Matar enemigos afligidos añade **entre 1 y 30 segundos** según el tipo de enemigo, "pero este bono se reduce según el nivel del Tributo" ([maxroll](https://maxroll.gg/d4/resources/kurast-undercity)). Lee eso dos veces: **cuanto mejor el tributo, menos tiempo tienes y menos tiempo recuperas**. La dificultad del tributo no es solo el enemigo, es el reloj.

**(b) Sintonía (Attunement)** — lo que decide **cuánto** botín sale.

> "Attunement is the main mechanic of the Undercity, which dictates how many rewards you receive at the end of the run." — [maxroll](https://maxroll.gg/d4/resources/kurast-undercity)

- Se muestra como **una barra de cuatro etapas** bajo el minimapa ([maxroll](https://maxroll.gg/d4/resources/kurast-undercity)).
- Sube por: matar monstruos (poco por muerte), **encender Braseros** (invocan enemigos; el premio solo se entrega tras matarlos a todos) y matar **Duendes del Tesoro** ([maxroll](https://maxroll.gg/d4/resources/kurast-undercity)).
- **Rango 1 de Sintonía es el mínimo** para cobrar la recompensa base de cualquier tributo — todas las descripciones de tributo lo repiten literalmente: *"at Attunement Rank 1"* `[datamining]`.
- El botín **solo se entrega al final**, tras matar al Jefe de Distrito ([icy-veins](https://www.icy-veins.com/d4/guides/kurast-undercity-guide/)).

**El "Fuego Sagrado" / "Aether" no aparece en ninguna fuente fechada en 2026.** Ni Maxroll (16/07/2026) ni Icy Veins lo mencionan. Si una guía te habla de Aether en la Undercity, está mirando otra versión del juego. (Aether sí existe, pero en las **Hordas Infernales** — ahí sí sale, ver §3.5.)

### 2.3 Tabla completa de Tributos `[datamining]`

Esto es texto literal del fichero de datos, no reconstrucción. Ordenado por para qué te sirve **a ti**.

| Tributo | Qué da (texto literal) | ¿Fuera de Tormento? |
|---|---|---|
| **Tribute of Heritage** | "Completing the dungeon with at least Attunement Rank 1 will reward **Uniques specific to your class**" | ✅ Todas las dificultades |
| **Tribute of Growth** | "Earn **Experience** at Attunement Rank 1" | ✅ Todas las dificultades |
| **Tribute of Armaments** | "chance to earn **Legendary** equipment" | ✅ Todas las dificultades |
| **Lesser Tribute of Harmony** | "Earn **Runes**" | ✅ Todas las dificultades |
| **Lesser Tribute of the Horadrim** | "Earn **Horadric Charms** and a chance for a **Horadric Seal**" | ✅ Todas las dificultades |
| **Minor Tribute of Andariel** | "Earn powerful gear rewards... **Guarantees Andariel will spawn** at the end of the run" | ✅ Todas las dificultades |
| **Greater Tribute of Armaments** | "chance to earn **Ancestral Legendary** equipment" | ❌ Solo Tormento |
| **Ancestral Tribute of Armaments** | "Ancestral Legendary equipment. **Enhanced Bargains that allow specific item type rewards** are available" | ❌ Solo Tormento |
| **Mythic Tribute of Armaments** | "chance to earn **Uniques** equipment, with **increased chances of a Mythic Unique**" | ❌ Solo Tormento |
| **Tribute of Ascendance (Resolute)** | "**Resolute Tributes reward only the Player who offers the Tribute.** Earn Uniques... with increased chances of a Mythic Unique" | ❌ Solo Tormento |
| **Tribute of Radiance (Resolute)** | "**Resolute...only the Player who offers.** Earn **Ancestral Legendaries**" | ❌ Solo Tormento |
| **Tribute of Titans** | "Earn **Lair Boss Hoard Keys**" (llaves de jefes de guarida) | ❌ Solo Tormento |
| **Tribute of Refinement** | "Earn **Obducite**" | ❌ Solo Tormento |
| **Greater Tribute of Refinement** | "Earn **Neathiron, Obducite, and Scrolls of Restoration**" | ❌ Solo Tormento |
| **Tribute of Harmony** | "Earn **Runes**" | ❌ Solo Tormento |
| **Greater Tribute of Harmony** | "Earn **Legendary Runes**" | ❌ Solo Tormento |
| **Tribute of Ingenuity** / **Greater** | "Earn **Horadric Cube Materials**" | ❌ Solo Tormento |
| **Lesser Tribute of Ingenuity** | "Earn Horadric Cube Materials" | ❌ Solo Tormento |
| **Tribute of the Horadrim** / **Greater** | "Horadric Charms and a Horadric Seal" | ❌ Solo Tormento |
| **Tribute of Andariel** / **Major Tribute of Andariel** | "Additional Legendaries and (a / moderate chance de) **Unique from Andariel's Hoard**. Guarantees Andariel will spawn" | Major: ❌ solo Tormento |

Fuente de toda la tabla: `assets-ng.maxroll.gg/d4-tools/game/data.min.json` (descargado 20/08/2026, `last-modified` 18/08/2026, `version` 3.1.0.72698). Datamining.

**Los tres tributos que te importan como Nigromante de esbirros:**

1. **Tribute of Heritage** — únicos **de tu clase**. Con esto la Undercity deja de ser una tragaperras y pasa a ser una máquina de fabricar tus Pact of Bone / The Undercrown / Bloodless Scream. La build guide de Maxroll para Nigromante de Esbirros (act. **22/07/2026**) lista como prioridad Mythic: **Warriors** → Pact of Bone, The Undercrown, Deathgrip, Blood Moon Breeches; **Mages** → Bloodless Scream, Pact of Bone, The Undercrown, The Hand of Naz, Blood Moon Breeches ([maxroll](https://maxroll.gg/d4/build-guides/minion-necromancer-guide)).
2. **Tribute of Titans** — llaves de jefes de guarida. Maxroll lo describe como "the fastest key farm in the game" ([maxroll, resultado de búsqueda](https://maxroll.gg/d4/resources/kurast-undercity)).
3. **Tribute of Growth** — XP directa para Paragón.

⚠️ **Nota de honestidad sobre "Tribute of Radiance":** la ficha de resultados de Maxroll lo describe como *"Aspects — Legendary Aspect imprints"*. El fichero de datos del juego dice literalmente *"Earn **Ancestral Legendaries**"*. **No coinciden.** Me inclino por el fichero de datos, pero está declarado como discrepancia en `## No encontrado`.

⚠️ **Nombres de tributo que YA NO EXISTEN** — si los ves en una guía, esa guía es de 2024: *Tribute of Mystique*, *Tribute of Equipment*, *Tribute of Gold*. Aparecen en resúmenes de búsqueda actuales pero **no están en el fichero de datos de 3.1.0**. Es el rastro de la versión de lanzamiento de VoH.

### 2.4 Jefes de Distrito

| Jefe | Mecánica | Fuente |
|---|---|---|
| **Yoche, the Golden** | AoE que cubre la sala; zonas seguras basadas en pilares | [maxroll](https://maxroll.gg/d4/resources/kurast-undercity) |
| **Longtooth, the Wretched** | Arena de tormenta con círculos de debuff amarillos | [maxroll](https://maxroll.gg/d4/resources/kurast-undercity) |
| **Alia, Kurast's End** | Escudo rojo/verde que determina las zonas seguras | [maxroll](https://maxroll.gg/d4/resources/kurast-undercity) |
| **Andariel** | No es de distrito: la fuerzas con cualquier Tributo de Andariel `[datamining]` | datamining |

### 2.5 Por qué se la llama "motor de farmeo"

No es marketing. Son tres propiedades que ninguna otra actividad tiene juntas:

1. **Botín dirigido a priori.** Eliges la categoría *antes* de entrar. Todo lo demás en D4 es aleatorio y luego filtras.
2. **Carrera corta y con techo de tiempo.** 60–120 s de base ([maxroll](https://maxroll.gg/d4/resources/kurast-undercity)) → el ciclo entrar/cobrar/repetir es el más rápido del juego.
3. **Es un nodo de Planes de Guerra.** Con el árbol invertido, la propia actividad cambia de reglas (§3.3). Ahí es donde el motor pasa de primera a quinta.

Además es la fuente listada de varios materiales que necesitas sí o sí:
- **Prismas de Sintonización** (Tuning Prisms, todos los tipos: Aggressive/Protector's/Resourceful/Pragmatic/Chromatic/Adept's) — "Collected from: **Cube Spoils in War Plans**, Cache Rewards from The Tree of Whispers, Elite monsters, **Undercity of Kurast**" `[datamining]`. Son los que dirigen los afijos en las Transmutaciones del Cubo Horádrico.
- El nodo **Finely Tuned** del árbol da **Prismas de Sintonización adicionales al completar la Undercity a Sintonía máxima** `[datamining]`.

---

## 3. 🆕 PLANES DE GUERRA (War Plans) — el sistema que hay que desbloquear HOY

### 3.1 Qué es y cómo se desbloquea

| Dato | Valor | Fuente |
|---|---|---|
| Expansión | **Lord of Hatred** (obligatoria) | [icy-veins.com/d4/guides/war-plans-overview](https://www.icy-veins.com/d4/guides/war-plans-overview/) |
| Requisito | **Completar la campaña de Lord of Hatred al menos una vez en un personaje** | [icy-veins](https://www.icy-veins.com/d4/guides/war-plans-overview/) |
| Dónde | **Mesa de mando (command table) en Temis**, capital de Skovos. Tyrael está al lado | [Blizzard](https://news.blizzard.com/en-us/article/24267729/prepare-for-the-reckoning-lord-of-hatred-draws-near) / [maxroll](https://maxroll.gg/d4/resources/war-plans) |
| Requisito de nivel | **No encontrado** en fuente fechada | — |

Descripción oficial de Blizzard:

> "Forge a chain of activities that you want to play, with the rewards you want to hunt for. Once you finish the first activity, you can seamlessly teleport to the next activity in the chain." — [news.blizzard.com](https://news.blizzard.com/en-us/article/24267729/prepare-for-the-reckoning-lord-of-hatred-draws-near)

> "Executing your War Plans levels up the Command Table, unlocking deeper progression and more choices." — [ídem](https://news.blizzard.com/en-us/article/24267729/prepare-for-the-reckoning-lord-of-hatred-draws-near)

Y la utilidad práctica que añadió el 3.0: existe un **teletransporte a un Plan de Guerra activo**; si no hay ninguno activo, te lleva a Temis ([Blizzard, notas 3.0, 10/06/2026](https://news.blizzard.com/en-us/article/24271857/diablo-iv-patch-notes-3-0)).

### 3.2 Las 7 actividades soportadas `[datamining]` + Maxroll

El fichero de datos lista exactamente siete árboles:

| # | Actividad | Clave interna |
|---|---|---|
| 1 | Tree of Whispers (Árbol de los Susurros) | `Warplans_Whispers` |
| 2 | Nightmare Dungeons (Mazmorras de Pesadilla) | `Warplans_NightmareDungeons` |
| 3 | Helltide (Marea Infernal) | `Warplans_Helltide` |
| 4 | **The Undercity** | `Warplans_Undercity` |
| 5 | Lair Bosses (Jefes de Guarida) | `Warplans_BossLair` |
| 6 | Infernal Hordes (Hordas Infernales) | `Warplans_InfernalHordes` |
| 7 | The Pit (El Foso) | `Warplans_Pit` |

Coincide con Maxroll (act. 05/08/2026): "Tree of Whispers, Nightmare Dungeons, Helltides, Kurast Undercity, Lair Bosses, Infernal Hordes, and The Pit" ([maxroll](https://maxroll.gg/d4/resources/war-plans)).

⚠️ El artículo oficial de Blizzard lista **seis** (omite el Árbol de los Susurros del listado principal) y luego aclara aparte: *"Whispers can double up with any activity selected! They still earn activity progression just like any other modes."* ([Blizzard](https://news.blizzard.com/en-us/article/24267729/prepare-for-the-reckoning-lord-of-hatred-draws-near)). O sea: los Susurros **se solapan** con lo que estés haciendo. Eso es XP de árbol gratis mientras farmeas otra cosa.

### 3.3 Cómo se sube un árbol — la tabla de Experiencia de Actividad

> "Each skill tree has **7 levels**, and you gain **1 skill point** to use in a tree **per level**." — [maxroll](https://maxroll.gg/d4/resources/war-plans) (act. 05/08/2026)

**Experiencia de Actividad por completar una actividad** ([maxroll](https://maxroll.gg/d4/resources/war-plans)):

| Dificultad | Actividades estándar | Hordas Infernales | Marea Infernal Mayor | Mazmorra de Pesadilla de Escalada |
|---|---|---|---|---|
| Normal | **25** | 50 | 75 | 85 |
| Difícil (Hard) | 31 | 62 | 94 | 106 |
| Experto (Expert) | 37 | 75 | 113 | 128 |
| Penitente (Penitent) | 43 | 87 | 131 | 149 |
| **Tormento 1–12** | **50–150** | **100–300** | **150–450** | **170–510** |

**Lectura práctica:** subir de dificultad multiplica por 6 la velocidad a la que desbloqueas nodos. Y la Mazmorra de Pesadilla de Escalada da **3,4×** lo que una actividad estándar. Si quieres los nodos rápido, tus Planes de Guerra deberían ir cargados de Escalada y Marea Infernal, no de actividades "normales".

⚠️ **Discrepancia declarada:** una fuente no preferente sostiene "hasta 125 en Tormento 12" en lugar de 150. Me quedo con Maxroll (150). Anotado en `## No encontrado`.

**Experiencia exacta necesaria para cada nivel de árbol (1→7): NO ENCONTRADA.** Ninguna fuente fechada la publica.

### 3.4 🎯 EL ÁRBOL DE LA UNDERCITY, NODO POR NODO `[datamining]`

Los 11 nodos con su texto literal. **Tienes 7 puntos** (uno por nivel de árbol) para 11 nodos → hay que elegir rama.

| Nodo | Rama | Texto literal (datamining) | Traducción operativa |
|---|---|---|---|
| **(raíz)** | — | — | Punto de entrada |
| **Last Gasp** | Centro | "Time collected from slain enemies with **5 seconds or less remaining** in the Undercity **doubles** the Time earned." | Seguro anti-fracaso. Cuando el reloj está en rojo, el tiempo que recuperas se dobla |
| **Bauble Day** | Centro | "If you slay a Portal Prankster within the Undercity, the **Cabochon Merchant** will appear after killing the District Boss. The Cabochon Merchant will sell you **Runes and Gems for Gold**." | Convierte oro en runas/gemas |
| **Idols of War** | Centro | "**Greater Tributes of Armament** more frequently drop throughout Sanctuary and have an **additional Bargain** choices." | Más tributos legendarios en todo el mundo |
| **Endless Swarm** | Izquierda | "**Invasion Portals** now appear in the Undercity. The enemies that emerge **grant Attunement** when slain." | Fuente extra de Sintonía |
| **Unfortunate Souls** | Izquierda | "Invasion Portals can now summon **Wisps** that attach to you and vanish if you die. Each Wisp you save will reward you with **Forgotten Souls** and other Crafting Materials at the end of the run." | Almas Olvidadas |
| **Gutter Filth** | Izquierda | "When you activate any Beacon within the Undercity, there is a small chance to summon a **Portal Prankster**. Invasion Portals will sometimes summon **Rats** of varying amounts." | Habilita toda la línea de duendes |
| **Trials and Tributes** | Izquierda | "For each **Portal Prankster** you slay within the Undercity, a **Tribute Chest** appears after killing the District Boss. Tribute Chests are unlocked by offering a Tribute." | **Cofres de tributo extra**. Ésta es la rama de botín |
| **Jade Epiphany** | Derecha | "When you gain an Attunement level in the Undercity, **Experience Orbs** appear around you. All enemies within the Undercity have **+1 Monster Power**." | **La rama de XP/Paragón** |
| **Finely Tuned** | Derecha | "Gain **additional Tuning Prisms** when completing the Undercity at **maximum Attunement**. All enemies within the Undercity have +1 Monster Power." | Materiales del Cubo Horádrico |
| **Pathfinder** | Derecha | "When you reach **maximum Attunement**, a **portal to the final floor** of the Undercity appears. All enemies within the Undercity have +1 Monster Power." | **Velocidad pura**: al llegar a Sintonía máxima saltas directo al jefe |
| **Initiative** | Derecha | "When you find the District Boss you gain the **Initiative** buff, with duration equal to your remaining Time. **Initiative is lost upon death.** If you slay the District Boss with Initiative active, you receive Tribute rewards **as if your Attunement was 2 higher (max 6)**." | Sintonía efectiva +2 |

**Topología del árbol** (reconstruida de las conexiones del fichero de datos, `[datamining]`):

```
                    (RAÍZ)
                   /   |   \
      Endless Swarm  Last Gasp  Jade Epiphany
            |          |            |
  Unfortunate Souls  Bauble Day  Finely Tuned
            |          |            |
      Gutter Filth  Idols of War  Pathfinder
            |                       |
   Trials and Tributes          Initiative
```

Izquierda = 4 nodos · Centro = 3 nodos · Derecha = 4 nodos. Con 7 puntos entra **una rama larga + el centro**, o casi.

**Qué recomienda Maxroll (act. 16/07/2026):**
- Los 7 nodos que lista como recomendados: Endless Swarm, Unfortunate Souls, Gutter Filth, Jade Epiphany, Finely Tuned, Pathfinder, Initiative ([maxroll](https://maxroll.gg/d4/resources/kurast-undercity)).
- "left path emphasizes **Gutter Filth** for increased chests" → rama de **botín**.
- "the right path from **Jade Epiphany to Initiative** will make Undercity runs finish **far more quickly** than doing the game mode normally" → rama de **velocidad + XP**.
- ⚠️ Honestidad de Maxroll, y la reproduzco: el valor de **Initiative** *"has not been verified from data collection"* ([maxroll](https://maxroll.gg/d4/resources/kurast-undercity)). Es decir: ni Maxroll ha comprobado que el +2 de Sintonía compense.

**Mi lectura para tu caso (Paragón desde 0, 4 semanas):** rama **derecha** (Jade Epiphany → Finely Tuned → Pathfinder → Initiative) y luego centro. Estás a Paragón 0 con 26 días; tu cuello de botella es XP y ciclos por hora, no cofres. Icy Veins coincide para el tramo de subida: desbloquear **Jade Epiphany**, que "grants experience orbs as you gain Attunement levels throughout the Undercity, for bonus XP" ([icy-veins](https://www.icy-veins.com/d4/news/fastest-diablo-4-season-14-leveling-route/)).

⚠️ **Ojo al coste oculto:** cuatro de los nodos de la rama derecha (Jade Epiphany, Finely Tuned, Pathfinder, Initiative) llevan pegado **"+1 Monster Power"** a *todos* los enemigos de la Undercity. Con la rama entera son **+4 de Poder de Monstruo acumulado**. Como Nigromante de esbirros recién llegado a 70 y sin Paragón, ese escalón lo pagas tú. Si notas que las carreras se te caen por tiempo, es esto.

### 3.5 Dónde vive de verdad "Writhe and Rot" — **corrección**

El brief mencionaba *'Writhe and Rot'* y *'Jade Epiphany'* como si fueran del mismo árbol. **No lo son.**

- **Jade Epiphany** → árbol de **The Undercity** `[datamining]`
- **Writhe and Rot** → árbol de **Helltide** (Marea Infernal) `[datamining]`

Texto literal de Writhe and Rot: *"Hellwyrms will always spew **Maggots** that gain +1 Monster Power. Sometimes, a **Pang of Duriel** will also crawl forth. **Lair Keys** often burst out of Pangs of Duriel."* `[datamining]`

Y esto importa mucho, porque Maxroll señala como fuente de XP de Paragón más rápida:

> "Whatever Pit Level you can complete efficiently (sub 3 min), **Helltide with the Writhe and Rot War Plan upgrade**" — [maxroll, Endgame Progression](https://maxroll.gg/d4/meta/endgame-progression) (act. 09/07/2026)

Nodos de Marea Infernal relevantes para ti `[datamining]`:

| Nodo | Texto literal | Para qué |
|---|---|---|
| **Hellmouth** | "When a Hellwyrm emerges, it unleashes one of the following: A **Chaos Rift**...; **Maggots**, which **burst out Experience Orbs** when slain; **Bloodseekers**, which are more likely to drop Ancestral items" | Puerta de entrada. Icy Veins lo pide primero |
| **Writhe and Rot** | (arriba) | Fija la salida en Maggots (XP) + Llaves de Guarida |
| **Planar Tremors** | "Hellwyrms will **always open a Chaos Rift**... The first time a Chaos Rift opens, there is a chance that **another will open**" | Alternativa a Writhe and Rot |
| **Crimson Scent** | "Hellwyrms will always call forth **Bloodseekers** that gain +1 Monster Power. **Greater Bloodseekers** may also emerge, which have a high chance to drop **Legendary** items" | La tercera vía: botín |
| **Bursting Brood** | "Maggots and Pangs of Duriel **explode when killed** and will often drop **Boss Trophies**" | Sinergia directa con Writhe and Rot |
| **Undying Embers** | "You lose **no Aberrant Cinders on death**" | Red de seguridad |
| **Ashes to Ashes** | "On death, **lose all** your Aberrant Cinders. For every 100 Aberrant Cinders you pick up, you gain an additional 10" | +10% cenizas a cambio de riesgo |
| **Hell's Prize** | "**Hell's Prize chests** will now appear in Helltide. These chests offer a massive torrent of items for **666 Aberrant Cinders**" | Sumidero de cenizas |
| **Meat Brothers** | "Instead of Hellborne, **two Butchers** connected with flaming chains ambush you. These Butchers each have a high chance to drop a **Profane Mindcage**" | Fuente de Jaulamentes Profanas |

**Ruta que recomienda Icy Veins para subir en S14:** meter "as many Helltide activities as possible in our War Plans" y subir el árbol de Marea Infernal para desbloquear **Hellmouth** y luego **Writhe and Rot**. Los Hellwyrms aparecen a **Nivel de Amenaza 2** (Threat Level 2) ([icy-veins](https://www.icy-veins.com/d4/news/fastest-diablo-4-season-14-leveling-route/)). Y avisa: **evita las Hordas Infernales** en el plan, "they take much longer to complete compared to other activities" ([ídem](https://www.icy-veins.com/d4/news/fastest-diablo-4-season-14-leveling-route/)).

### 3.6 Cambio de S14 que te afecta directamente: el progreso de Marea Infernal

En S14 el progreso de la actividad de Marea Infernal en el Plan de Guerra **dejó de contarse por abrir cofres y pasa a contarse por recoger cenizas**:

- **75 Cenizas** en Normal → Penitente
- **300 Cenizas** en Tormento 1+

([icy-veins](https://www.icy-veins.com/d4/news/diablo-4-season-14-ptr-changes-how-parties-use-war-plans/))

Además en S14: "War Plan activity XP scaling has been increased for **Torment 8 and higher**" y "War Plan base activity XP has been increased for the **Infernal Hordes**" ([ídem](https://www.icy-veins.com/d4/news/diablo-4-season-14-ptr-changes-how-parties-use-war-plans/)). **Las cifras exactas de esos aumentos no se publican.**

### 3.7 Los otros cinco árboles — resumen de lo que te sirve

**El Foso (The Pit)** `[datamining]` — es donde subes glifos, así que estos nodos son inversión directa:

| Nodo | Texto literal |
|---|---|
| **Choron's Blessing** | "Gain **+1 Glyph Upgrade Chance** for completing The Pit." |
| **Choron's Haste** | "The Pit gains the Haste Mastery objective. When you kill the Guardian gain **+1 Glyph Upgrade Chance for every 5 minutes** left on the Timer." |
| **Heart of Stone** | "Begin The Pit carrying the Heart of Stone... **breaks after dropping 10 times**... Deposit the Heart of Stone within to gain **+1 Glyph Upgrade Chance**." |
| **Choron's Soul** | "Choron's Soul now spawns with the Awakened Glyphstone... **All Progress Orbs in The Pit now grant Experience**." |
| **Choron's Flesh** | "...allow you to get valuable Equipment by **consuming one of your Glyph Upgrade Chances**." |
| **Pit Butcher** | "The Butcher is a Guardian and **killing him will complete the run**. However, you **fail the run if he kills any player**." ⚠️ **En dúo esto es el doble de peligroso** |
| **Damned Thieves** | "**Orb Thieves**... drop an immense amount of Progress Orbs when killed, but leave a **trail of Traps**" |

**Jefes de Guarida (Lair Bosses)** `[datamining]` — la forma de sacar tus Míticos sin farmear llaves aparte:

| Nodo | Texto literal |
|---|---|
| **Lair of Plenty** | "Lair Bosses have +1 Monster Power. **Gain +1 Hoard Chest** when you slay a Lair Boss (excluding Belial)." |
| **Exotic Armory** | "Hoard Chests drop **one additional Unique Item**, but it can be for **any Class**." |
| **Ultimate Nemesis** | "...the Call Of Evil... accepts **3 Superior Lair Keys**... all enemies gain **+5 Monster Power**. Defeating the Boss Encounter will award you with **10 Hoard Chests worth of Items**." |
| **Duriel's Invasion** | "When summoning the Blood Maiden in Helltides, there is a chance **Duriel** can be summoned instead." |
| **Golden Hoard** | "All equipment that would drop from Hoard Chests are **converted to Gold**, except for Unique and Mythic items." |
| **Lair of Runes** | "Lair Bosses have +1 Monster Power. Lair Bosses have a higher chances of dropping **specific Runes**." |
| **Two by Two** / **Greater Nemesis** | Portales a **Nemesis Lair** (2 jefes iniciados a la vez) y **Greater Nemesis Lair** (2 jefes mayores) |

**Mazmorras de Pesadilla** `[datamining]` — destacan **Fearless Conviction** ("A **Conviction Chest** appears at the end... higher than normal chance to award **Attuned Primordial Dust**"), **Greed is Good** (portal al **Goblin's Retreat**), **Recurring Nightmare** (jefes sueltan **Escalation Sigils**, solo en Tormento+) y **Waking Spoils** (**War's Bounty Chest** al terminar).

**Susurros** `[datamining]` — **Wisdom of Whispers**: "Gain **50% more Experience Orbs** in Whisper Caches." Y **Resplendent Favor**: "Each Whisper Cache has a chance to drop a **Resplendent Spark**" (chispas → míticos). Como los Susurros se solapan con cualquier otra actividad, esto es de lo más barato del sistema.

**Hordas Infernales** `[datamining]` — el eje Orden↔Caos: **Reign in Hell** ("An additional Infernal Offering appears each wave. However, you **suppress Chaos Waves**"), **Total Chaos** ("Chaos Waves appear more frequently. However, **one less Infernal Offering** each wave"), **Bedlam** ("+50 Aether" al entrar en oleada de Caos), **Pulse of Aether** ("+50 Aether" al suprimirla), **Devil's Deal** ("Completing the Infernal Challenge will grant **+200 Aether**"), **Forged in Flame** ("**Obducite** drops instead of Gem Fragments"). *(Aquí es donde vive el Aether — no en la Undercity.)*

### 3.8 Marcas de El'Druin y el tablero compartido — **la parte del dúo**

`[datamining]`: **"Marks of El'Druin :: Currency to support your journey through War Plans."**

| Dato | Valor | Fuente |
|---|---|---|
| Cómo se ganan | **1 por Plan de Guerra completado** | [Icy Veins, vía cobertura S14](https://www.icy-veins.com/d4/news/diablo-4-season-14-ptr-changes-how-parties-use-war-plans/) — cantidad exacta y tope: ver aviso ⚠️ abajo |
| Tope acumulable | **3** | ⚠️ Solo en fuentes NO preferentes. Ver `No encontrado` |
| Coste: rehacer tu tablero en solitario | **1 Marca** | ⚠️ Solo en fuentes NO preferentes |
| **Coste: sincronizar el tablero con todo el grupo** | **2 Marcas de El'Druin** | ✅ [icy-veins](https://www.icy-veins.com/d4/news/diablo-4-season-14-ptr-changes-how-parties-use-war-plans/) |

**Cómo funciona la sincronización en grupo** (novedad de S14):

> "When all party members are in Temis, a **New Plan** prompt will appear, costing **2 Marks of El'Druin**." El tablero del que inicia se reinicia y "the new board will be pushed to everyone else in the party" tras aceptar todos la votación. — [icy-veins](https://www.icy-veins.com/d4/news/diablo-4-season-14-ptr-changes-how-parties-use-war-plans/)

Y un detalle que sí importa: *"Plans are synced regardless of War Plan Level or other States (Torment Level, Campaign Completion etc.)"*. **Pero** el prerrequisito no se salta: **todo el grupo tiene que estar físicamente en Temis**, y Temis está en Skovos, y Skovos es Lord of Hatred. Ver §7.

---

## 4. 🆕 CIUDADELA OSCURA (Dark Citadel)

### 4.1 Desbloqueo y forma

| Dato | Valor | Fuente |
|---|---|---|
| Expansión | **Vessel of Hatred** | [icy-veins](https://www.icy-veins.com/d4/guides/dark-citadel-guide/) |
| Nivel | **60** | [icy-veins](https://www.icy-veins.com/d4/guides/dark-citadel-guide/) — ⚠️ escrito cuando el máximo era 60; ver `No encontrado` |
| Dificultad | **Tormento** | [icy-veins](https://www.icy-veins.com/d4/guides/dark-citadel-guide/) |
| Misión de desbloqueo | Una vez, con la **Sacerdotisa Cualli** en la ciudad de Kurast | [icy-veins](https://www.icy-veins.com/d4/guides/dark-citadel-guide/) |
| Acceso | Punto de referencia **Rise of Khazra** en Nahantu | [icy-veins](https://www.icy-veins.com/d4/guides/dark-citadel-guide/) |
| **Jugadores mínimos** | **2** (recomendado 4) — **NO se puede en solitario** | [icy-veins](https://www.icy-veins.com/d4/guides/dark-citadel-guide/) |
| Escalado | **"The difficulty level does not scale in function of the number of players"** | [icy-veins](https://www.icy-veins.com/d4/guides/dark-citadel-guide/) |
| Estructura | **3 alas × 2 jefes**: Labyrinth of Souls, Enclave of Strife, Dominion of Zagraal | [icy-veins](https://www.icy-veins.com/d4/guides/dark-citadel-guide/) |
| Modo SSF | **No disponible** en Solo Self-Found | Notas 3.1.0 (vía cobertura de terceros — ver `No encontrado`) |

**Traducción para tu dúo:** 2 jugadores es el mínimo y la dificultad **no baja** por ir de dos. Diseñada para 4. Con dos nigromantes uno de ellos principiante, esperad muro.

### 4.2 Recompensas

| Recompensa | Detalle | Fuente |
|---|---|---|
| **Prisma Disperso** (Scattered Prism) | `[datamining]`: "A mysterious prism used by the Jeweler to **add sockets to Ancestral equipment**. **Frequently found in Torment difficulties from: World Bosses, Dark Citadel.** Rarely found from: Bartering at the Mercenary Den, Infernal Hordes, Initiate Lair Bosses" | datamining |
| **Citadel Coin** | `[datamining]`: "Used to purchase items from the **Citadel Vendor**. Earned from the Dark Citadel" | datamining |
| **Khazra Horn** | `[datamining]`: "Used to **transmute Boss Summoning items** at the Alchemist. Collected from: The Beast in the Ice, Echo of Varshan, Grigoire, Lord Zir, Urivar, World Bosses, **Dark Citadel**" | datamining |
| **Cofre semanal** | "Weekly Rewards Cache" por el primer clear cooperativo de la semana | [icy-veins](https://www.icy-veins.com/d4/guides/dark-citadel-guide/) |
| **Dark Citadel Challenger's Cache** | `[datamining]`: "for defeating the Rise of the Khazra... Contains gear including **Ancestrals, Legendaries, and Uniques**, as well as crafting materials, gems, and various currencies" | datamining |
| **Scroll of Khazra Shards** | `[datamining]`: "Increase the level of monsters by **10** and rewards in the Rise of the First Khazra Dark Citadel" | datamining |
| Otras cajas | Dark Citadel Gear Cache / Crafting Cache / Gem Cache / Scroll Cache ("3 random Citadel Scrolls") | datamining |

**Precios del Vendedor de la Ciudadela** ([icy-veins](https://www.icy-veins.com/d4/guides/dark-citadel-guide/)):

| Artículo | Coste en Citadel Coins |
|---|---|
| Inciensos | **1600** |
| Elixires | **800** |
| Pergaminos (incl. Scroll of Restoration) | **400 – 2000** |
| Cajas (Caches) | **900 – 1200** |
| Cosméticos / sets de armadura | Exclusivos de **Tormento IV** |

### 4.3 Veredicto honesto: **NO es un motor de farmeo**

En 4 semanas y con Paragón 0, la Ciudadela Oscura no compite con la Undercity ni con la Marea Infernal. **La única razón real para entrar es el Prisma Disperso**: es el material que abre engarces en equipo Ancestral, y el fichero de datos lo lista como "frequently found" en solo dos sitios — **Jefes de Mundo y Ciudadela Oscura** `[datamining]`. Todo lo demás (bartering, Hordas, jefes iniciados) es "rarely".

**Además:** ninguna fuente preferente tiene una página de Ciudadela Oscura actualizada a la era Lord of Hatred / S14. La de Wowhead sigue titulada **"Season 12"** con última actualización **2026/03/11** ([wowhead](https://www.wowhead.com/diablo-4/guide/vessel-of-hatred-raid-dungeon-guide)) — es decir, **anterior a Lord of Hatred (28/04/2026)**. La de Icy Veins no lleva fecha visible. Trato todo lo de esta sección con esa reserva.

**Plan:** una pasada semanal con la pareja, por el cofre semanal y los Prismas. Nunca a costa de un ciclo de Undercity.

---

## 5. 🆕 NAHANTU / KURAST y 🆕 SKOVOS

### 5.1 Nahantu (Vessel of Hatred)

Para ti Nahantu es, esencialmente, **el sitio donde está el Brasero de Espíritus de la Undercity** y donde arranca la Ciudadela Oscura (waypoint Rise of Khazra, misión con Cualli). Hay 30 **Tenets of Akarat** repartidos por la zona — pero lee la §6.1 antes de moverte a por uno solo.

### 5.2 Skovos (Lord of Hatred) — inventario

| Elemento | Cantidad | Fuente |
|---|---|---|
| Puntos de referencia (waypoints) | **8** | [maxroll, Skovos Region Guide](https://maxroll.gg/d4/resources/skovos-region-guide) (act. 16/07/2026) |
| Bastiones (strongholds) | **3** | [maxroll](https://maxroll.gg/d4/resources/skovos-region-guide) |
| Mazmorras | **12** | [maxroll](https://maxroll.gg/d4/resources/skovos-region-guide) |
| Misiones secundarias | **30** | [maxroll](https://maxroll.gg/d4/resources/skovos-region-guide) |
| Áreas por descubrir | **67** | [maxroll](https://maxroll.gg/d4/resources/skovos-region-guide) |
| **Chronicles of Creation** | **30** | [maxroll](https://maxroll.gg/d4/resources/skovos-region-guide) |
| Zona de Marea Infernal | **Skartara – Celestia** | [maxroll](https://maxroll.gg/d4/resources/skovos-region-guide) |
| Jefe de mundo | **Hatred's Mortar** | [maxroll](https://maxroll.gg/d4/resources/skovos-region-guide) |
| Encuentro de jefe | **Echo of the False Prophet** | [maxroll](https://maxroll.gg/d4/resources/skovos-region-guide) |
| Capital | **Temis**, "home of a human civilization led by **Queen Andreona**" | [maxroll](https://maxroll.gg/d4/resources/skovos-region-guide) |

Blizzard describe Temis como *"the ideal Endgame hub for Diablo IV"* tras la campaña ([news.blizzard.com](https://news.blizzard.com/en-us/article/24267729/prepare-for-the-reckoning-lord-of-hatred-draws-near)), y Skovos como región *"steeped in the history of Sanctuary's progenitors"* con la Madre Bendita y el Padre Celestial tallados en el mármol de Temis.

`[datamining]` existe una **"Ancestral Skovos Cache"**: *"Contains an assortment of **Seals, Charms, Horadric Cube Materials** and other useful goods"*, y su gemela **"Ancestral Nahantu Cache"**: *"Contains an assortment of **Undercity Tributes, Runes** and other useful goods"*.

**Para ti:** Skovos importa por **una** razón — Temis y la mesa de mando. Explorarla al 100% no es prioritario (§6.1).

### 5.3 El nivel máximo 70: **NO está detrás de las expansiones**

Blizzard, literal: *"Level Cap: Increases to **70 for all players** beginning Season of Reckoning"* ([news.blizzard.com](https://news.blizzard.com/en-us/article/24267729/prepare-for-the-reckoning-lord-of-hatred-draws-near)). "For all players" = también sin expansión. Confirmado por Maxroll: *"Maximum character level: 70"* ([maxroll](https://maxroll.gg/d4/meta/endgame-progression), act. 09/07/2026). **Tu pareja ya tiene acceso al 70 aunque no haya comprado nada.**

---

## 6. 🚨 RENOMBRE y TENETS OF AKARAT — el modelo muerto que te habría costado el fin de semana

### 6.1 El hallazgo

Prácticamente todas las guías de Tenets of Akarat que vas a encontrar dicen alguna variante de: *"cada Tenet da 10 de Renombre; el Renombre te da puntos de habilidad, cargas de poción y **puntos de Paragón**"*.

**Eso ya no aplica a un personaje de temporada.**

> "With patch **2.5.0** Renown is only active on the **Eternal Realm**. On **Seasonal Realms it has been replaced by the Season Rank system**." — [maxroll.gg/d4/resources/renown-system](https://maxroll.gg/d4/resources/renown-system) (act. 09/12/2025)

> "Season Journey and Renown have officially been **retired on the Seasonal Realm**." · "Renown is permanent **only on the Eternal Realm**." — [icy-veins.com/d4/guides/season-rank](https://www.icy-veins.com/d4/guides/season-rank/)

Corroborado por la cobertura del cambio: a partir de la Temporada 11 / parche 2.5.0 (11/12/2025), el Rango de Temporada sustituye a las pistas de Renombre de región **y** al Viaje de Temporada en los servidores estacionales; el Eterno conserva el Renombre ([icy-veins.com/d4/news/say-goodbye-to-renown...](https://www.icy-veins.com/d4/news/say-goodbye-to-renown-diablo-4-introduces-season-rank-in-season-11/)).

### 6.2 Consecuencia práctica, sin rodeos

Estás en el **reino de temporada** (S14). Por tanto:

- ❌ Recorrer los **30 Tenets of Akarat** de Nahantu **no te da puntos de habilidad ni de Paragón** este mes.
- ❌ Resolver los **30 Chronicles of Creation** de Skovos (el puzle de girar las estatuas de Lilith e Inarius para que sus haces apunten a la crónica) **tampoco**.
- ✅ Lo que sí conservas: la XP/oro/gemas del momento, y los logros/monturas — el logro y la montura **Reins of the Nahantu Lion** por los 30 Tenets son de cuenta y persisten ([wowhead](https://www.wowhead.com/diablo-4/news/everything-you-need-to-know-about-tenets-of-akarat-new-nahantu-renown-347580)).
- ✅ **Donde SÍ están tus puntos ahora:** el **Rango de Temporada**.

### 6.3 Rango de Temporada — dónde están de verdad los puntos

| Dato | Valor | Fuente |
|---|---|---|
| Puntos de habilidad + Paragón del Rango de Temporada de S14 | "up to **12 Skill Points and 42 Paragon Points**" | Cobertura de S14 (fuente no preferente) — ver ⚠️ |
| Puntos de Paragón del Rango de Temporada (declaración oficial LoH) | Recompensas del Rango de Temporada incluyen "up to **42 Paragon points**" | ✅ [news.blizzard.com](https://news.blizzard.com/en-us/article/24267729/prepare-for-the-reckoning-lord-of-hatred-draws-near) |
| Puntos de Paragón del Rango de Temporada (Icy Veins) | "Eternal Renown now grants **12** additional Paragon Points" y "Season Rank grants another **12** Paragon Points spread across the Ranks" | ⚠️ [icy-veins](https://www.icy-veins.com/d4/guides/season-rank/) — **CONTRADICE los 42 de Blizzard** |
| Estructura de recompensas por rango | Rangos 1–2: 1 punto de habilidad c/u · Rango 3: 1 habilidad + 1 Paragón · Rangos 4–5: 1 Paragón c/u · Rango 6: 1 Paragón + extra | [icy-veins](https://www.icy-veins.com/d4/guides/season-rank/) |

⚠️ **12 vs 42: conflicto abierto.** La cifra oficial de Blizzard para la era Lord of Hatred es **42**; la guía de Icy Veins dice **12** y no lleva fecha visible (probablemente escrita en la era S11, cuando el sistema nació). No resuelvo el conflicto: lo declaro. **Compruébalo en tu propia pantalla de Rango de Temporada** — ahí sale el número real de tu temporada.

Y una nota de 3.1.3 que te ahorra una vuelta: *"Escalation Nightmare Dungeons with the **Rupture** affix now count toward"* el objetivo de Rango de Temporada III **Set Fire to the Beacons**, así que ya no hace falta salirte a hacer otra actividad ([cobertura del 3.1.3](https://www.u4gm.com/diablo-4/blog-diablo-4-patch-3.1.3-is-live-what-changed-in-season-14) — fuente no preferente, marcada como tal).

---

## 7. 👥 DÚO — matriz según lo que tenga la pareja

⚠️ **No sabemos si la pareja compró las expansiones.** Los dos casos:

### Caso A — la pareja SÍ tiene VoH + LoH

| Contenido | ¿Juntos? | Nota |
|---|---|---|
| Undercity | ✅ | Cuidado con los tributos "Resolute" (abajo) |
| Ciudadela Oscura | ✅ | **Es la única forma**: mínimo 2 jugadores |
| Planes de Guerra | ✅ | Sincronizad tablero en Temis por **2 Marcas de El'Druin** ([icy-veins](https://www.icy-veins.com/d4/news/diablo-4-season-14-ptr-changes-how-parties-use-war-plans/)) |
| Skovos / Temis | ✅ | — |

### Caso B — la pareja NO tiene expansiones

| Contenido | ¿Juntos? | Fuente |
|---|---|---|
| Juego base (mazmorras, Mareas Infernales, Foso, jefes, Hordas) | ✅ | "You can still team up and play together in the original Diablo IV world" |
| **Nivel 70** | ✅ **Sí lo tiene** | [Blizzard](https://news.blizzard.com/en-us/article/24267729/prepare-for-the-reckoning-lord-of-hatred-draws-near): el cap sube a 70 "for all players" |
| Buscador de grupo (Party Finder) | ✅ | Disponible para todos, no requiere expansión |
| **Nahantu** | ❌ | Contenido de VoH |
| **Undercity** | ❌ | Requiere VoH |
| **Ciudadela Oscura** | ❌ | Requiere VoH |
| **Mercenarios y Palabras Rúnicas** | ❌ | Requieren VoH |
| **Skovos / Temis** | ❌ | Requiere LoH |
| **Planes de Guerra** | ❌ | Requiere completar la campaña de LoH ([icy-veins](https://www.icy-veins.com/d4/guides/war-plans-overview/)) |

**Lo que esto significa de verdad en el Caso B:** tú acabas de comprar acceso a **todo el motor de farmeo de la temporada**, y tu pareja se queda fuera de **los tres sistemas** de este informe. Vais a jugar en carriles distintos. **Si hay presupuesto y queréis empujar juntos las 4 semanas, comprar VoH+LoH en la PS5 es la decisión de mayor impacto que podéis tomar hoy** — más que cualquier optimización de build.

Fuentes del Caso B: síntesis de discusiones y coberturas ([foro oficial Blizzard "Friends without Vessel of Hatred"](https://us.forums.blizzard.com/en/d4/t/friends-without-vessel-of-hatred/191401), [zleague](https://www.zleague.gg/theportal/diablo-4-what-happens-to-players-without-the-expansion/)). **Ninguna página oficial de Blizzard con matriz explícita de co-op por expansión: ver `No encontrado`.**

### 7.1 ⚠️ Aviso sobre tributos "Resolute" en grupo

`[datamining]`, texto literal: *"**Resolute Tributes reward only the Player who offers the Tribute.**"* Afecta a **Tribute of Ascendance (Resolute)** y **Tribute of Radiance (Resolute)**.

Existe además un aviso de jugadores en el foro oficial EU titulado *"PSA: Do not use resolute tributes in a team!"*, que denuncia que ni el que lo pone ni el grupo reciben lo esperado. **Pero:** es del **23–28 de mayo de 2025**, **no tiene respuesta azul de Blizzard**, y en el propio hilo otros jugadores rebaten diciendo que Resolute nunca garantizó Mítico/Ancestral, solo sube la probabilidad ([eu.forums.blizzard.com](https://eu.forums.blizzard.com/en/d4/t/psa-do-not-use-resolute-tributes-in-a-team/21742)).

**Cómo lo trato:** el texto del ítem (que sí es de 3.1.0) es claro y suficiente — **un tributo Resolute solo premia a quien lo pone**. Eso ya es razón para no gastarlos "para el grupo". El bug reportado en 2025 lo dejo como no verificado, no como hecho.

---

## 8. Plan de 4 semanas — lo que este informe implica

### Día 1 (hoy) — abrir las llaves, no farmear todavía

1. **Pit hasta el nivel 10 → desbloquea Tormento I.** El fichero de datos es literal: Tormento I se desbloquea "Unlock Artificer's Tier and **Conquer Tier 10** on this character" `[datamining]`. **Sin Tormento, la mayoría de los Tributos de la Undercity están bloqueados** ("Only usable in Torment Difficulties"). Es el cuello de botella nº1.
2. **Completar la campaña de Lord of Hatred.** Es el **único** requisito de los Planes de Guerra ([icy-veins](https://www.icy-veins.com/d4/guides/war-plans-overview/)). Hasta que no esté, el resto del informe no te aplica.
3. **Misión prioritaria de VoH → Brasero de Espíritus** de la Undercity, si no lo tenías ([maxroll](https://maxroll.gg/d4/resources/kurast-undercity)).

### Semana 1 — subir árboles, no personaje

4. Primer Plan de Guerra **cargado de Mareas Infernales**; subir el árbol de Marea Infernal a **Hellmouth** y después **Writhe and Rot** ([icy-veins](https://www.icy-veins.com/d4/news/fastest-diablo-4-season-14-leveling-route/)).
5. Segundo árbol: **Undercity, rama derecha** — Jade Epiphany → Finely Tuned → Pathfinder → Initiative.
6. Meter **Mazmorras de Pesadilla de Escalada** en los planes: dan **170–510** de XP de actividad en Tormento contra **50–150** de una actividad estándar ([maxroll](https://maxroll.gg/d4/resources/war-plans)). Es la vía rápida a los 7 puntos de árbol.
7. Empujar Tormento en cuanto la build aguante: la XP de actividad escala de **25** (Normal) a **150** (Tormento 12) ([maxroll](https://maxroll.gg/d4/resources/war-plans)), y la XP de monstruo de **+300%** (T1) a **+1400%** (T12) `[datamining]`.

### Semanas 2–4 — el bucle

8. Marea Infernal con Writhe and Rot (XP de Paragón) ⟷ Undercity con **Tribute of Growth** (XP) y **Tribute of Heritage** (únicos de Nigromante) ⟷ Foso (glifos).
9. **Tribute of Titans** para llaves de jefes de guarida → tus Míticos.
10. Ciudadela Oscura: **una vez por semana** con la pareja, por el cofre semanal y los **Prismas Dispersos** (engarces en Ancestral).
11. **Rango de Temporada**: es donde están los puntos de habilidad y Paragón gratis. No el renombre.
12. **NO** recorrer Tenets of Akarat ni Chronicles of Creation. §6.

---

## Fuentes

Páginas realmente abiertas para este informe (WebFetch), en orden de uso:

**Oficiales de Blizzard**
- https://news.blizzard.com/en-us/article/24271857/diablo-iv-patch-notes-3-0 — Notas del parche 3.0, fechadas 10/06/2026, build #72271
- https://news.blizzard.com/en-us/article/24267729/prepare-for-the-reckoning-lord-of-hatred-draws-near — anuncio de Lord of Hatred: Planes de Guerra, Temis, nivel 70, Rango de Temporada
- https://us.forums.blizzard.com/en/d4/t/after-you-gain-max-attunement-in-the-kurast-undercity/205532 — hilo de foro; **descartado por antigüedad (08–09/11/2024)**
- https://eu.forums.blizzard.com/en/d4/t/psa-do-not-use-resolute-tributes-in-a-team/21742 — hilo de foro (23–28/05/2025), sin respuesta azul; usado solo como aviso no verificado
- https://us.forums.blizzard.com/en/d4/t/friends-without-vessel-of-hatred/191401 — co-op sin expansión (vía resultados de búsqueda)

**Maxroll (preferente)**
- https://maxroll.gg/d4/resources/kurast-undercity — act. **16/07/2026**; sección de Planes de Guerra añadida 16/07/2026
- https://maxroll.gg/d4/resources/war-plans — act. **05/08/2026**; tabla de Experiencia de Actividad
- https://maxroll.gg/d4/meta/endgame-progression — act. **09/07/2026**; nivel máximo 70, Writhe and Rot como mejor XP
- https://maxroll.gg/d4/resources/skovos-region-guide — act. **16/07/2026**
- https://maxroll.gg/d4/build-guides/minion-necromancer-guide — act. **22/07/2026**; prioridades de Mítico para Esbirros
- https://maxroll.gg/d4/resources/renown-system — act. **09/12/2025**; renombre solo en Eterno
- https://maxroll.gg/d4/news/lord-of-hatred-3-1-2-patch-notes — 25/07/2026 (act.) / 28/07/2026 (lanzamiento); **sin contenido de mi dominio**

**Icy Veins (preferente)**
- https://www.icy-veins.com/d4/guides/kurast-undercity-guide/
- https://www.icy-veins.com/d4/guides/dark-citadel-guide/
- https://www.icy-veins.com/d4/guides/war-plans-overview/
- https://www.icy-veins.com/d4/news/diablo-4-season-14-ptr-changes-how-parties-use-war-plans/ — sincronización de tablero, 2 Marcas, cenizas 75/300
- https://www.icy-veins.com/d4/news/fastest-diablo-4-season-14-leveling-route/ — ruta Hellmouth → Writhe and Rot
- https://www.icy-veins.com/d4/guides/season-rank/ — Rango de Temporada sustituye al Renombre
- https://www.icy-veins.com/d4/news/say-goodbye-to-renown-diablo-4-introduces-season-rank-in-season-11/
- https://www.icy-veins.com/d4/guides/nahantu-tenets-of-akarat-locations-and-rewards/ — sin fecha visible

**Datamining (declarado como tal)**
- https://assets-ng.maxroll.gg/d4-tools/game/data.min.json — descargado 20/08/2026. `last-modified: Tue, 18 Aug 2026 15:42:02 GMT`, `content-length: 11606376`, **campo `version`: `3.1.0.72698`** (por detrás del parche vivo 3.1.3/73224). Claves usadas: `warPlans`, `skillTrees.Warplans_*`, `skills.Warplans_*`, `items`, `worldTiers`

**Otros (abiertos, con reserva)**
- https://www.wowhead.com/diablo-4/guide/vessel-of-hatred-raid-dungeon-guide — act. **2026/03/11**, titulada "Season 12"; **anterior a Lord of Hatred**, no usada para números
- https://www.wowhead.com/diablo-4/news/everything-you-need-to-know-about-tenets-of-akarat-new-nahantu-renown-347580 — montura y logro
- https://blizzardwatch.com/2026/07/17/diablo-4-season-15-start-september-15/ — fin de S14
- https://mobalytics.gg/diablo-4/guides/warplans-guide — **HTTP 403, no se pudo abrir**

**Fuentes vetadas por el brief y respetadas:** fextralife, primagames, beebom, gamespot, segmentnext, studioloot, gamerguides, pcgamesn, mythicdrop. Aparecieron en resultados de búsqueda; **ninguna se ha usado para efectos ni números**.

---

## No encontrado

Huecos declarados. Ninguno se ha rellenado por inferencia.

### Números que no existen en fuente fechada en 3.1.x

1. **Rango máximo de Sintonía (Attunement) en la Undercity.** Maxroll dice que la barra tiene "four-staged" pero **no afirma que el rango máximo sea 4**. El nodo *Initiative* habla de recompensas "as if your Attunement was 2 higher (**max 6**)" `[datamining]`, lo que sugiere que la tabla de recompensas llega hasta 6. La única fuente que dice "Rango 4" es un hilo de foro de **noviembre de 2024** — descartado. **Míralo en tu barra.**
2. **XP concreta por carrera de Undercity** (paragón/hora, millones de XP por run). Circulan cifras como "20–30 millones por run en T10–12", pero **solo en fuentes no preferentes** (iggm, mmoexp, timesaver, ggwtb, boostmatch, nexttier). No las reproduzco como dato.
3. **Experiencia de Actividad necesaria para cada nivel de árbol de Planes de Guerra (1→7).** Maxroll publica la XP *ganada* por actividad pero **no el umbral por nivel**.
4. **Porcentajes exactos de los aumentos de XP de S14** ("increased for Torment 8 and higher", "increased for Infernal Hordes"). Icy Veins da la dirección, no la cifra.
5. **Requisito de nivel para desbloquear los Planes de Guerra.** Solo consta "completar la campaña de LoH".
6. **Citadel Coins que se ganan por carrera de Ciudadela Oscura.** Tengo los **precios** del vendedor (1600/800/400–2000/900–1200) pero **no la tasa de ingreso**.
7. **Contenido exacto del cofre semanal de la Ciudadela Oscura.**
8. **Umbrales de nivel de Renombre por región** (Nahantu y Skovos) y su desglose exacto de recompensas por escalón. Maxroll da totales agregados de cuenta (12 puntos de habilidad, 6 cargas de poción, 480 de capacidad de óbolos, 24 puntos de Paragón por completar las cinco etapas en todas las zonas) pero **no el desglose por región**, y **Skovos no aparece en esa página** (act. 09/12/2025, anterior a Lord of Hatred).
9. **Coste en Marcas de El'Druin para rehacer el tablero en solitario (¿1?) y tope de acumulación (¿3?).** Solo en fuentes no preferentes. Confirmado en fuente preferente **solo** el coste de sincronizar en grupo: **2 Marcas**.
10. **Número máximo de Paragón** (¿300?). Aparece en fuentes no preferentes y en una mención de nodo ("dwindles after Paragon Level 250"), pero **ninguna fuente preferente fechada lo confirma**.
11. **Estructura de nodos de los árboles de Hordas Infernales y Mazmorras de Pesadilla en el juego** (qué nodo conecta con cuál). Tengo los nombres y textos completos `[datamining]` pero solo he mapeado la topología del árbol de la Undercity.
12. **Tenets of Akarat: renombre por unidad y total.** Las cifras "10 por Tenet / 300 en total" salen en resúmenes de búsqueda pero **no las he leído en una página preferente y fechada**, y en cualquier caso son irrelevantes en temporada (§6).

### Conflictos abiertos entre fuentes — NO resueltos

| Tema | Fuente A | Fuente B | Mi postura |
|---|---|---|---|
| Nivel de desbloqueo de la Undercity | Icy Veins (guía): **20** | Icy Veins (noticia de leveo): **25** | Sin resolver. Da igual: tienes 70 |
| Qué da **Tribute of Radiance** | Maxroll: "**Aspectos** — imprimaciones de Aspecto Legendario" | Datamining: "**Ancestral Legendaries**" | Me inclino por el datamining (texto del ítem), pero está sin resolver |
| XP de actividad en Tormento 12 | Maxroll: **150** | Fuente no preferente: **125** | Uso Maxroll |
| Puntos de Paragón del Rango de Temporada | Blizzard: "up to **42**" | Icy Veins: "**12** spread across the Ranks" | **Sin resolver.** Compruébalo en tu pantalla |
| Nivel requerido para la Ciudadela Oscura | Icy Veins: **60** | — | La página parece escrita cuando el máximo era 60. **No sé si LoH lo subió a 70.** No aparece en ninguna nota oficial que haya leído |

### Cosas que directamente no aparecen en ninguna parte

13. **Matriz oficial de Blizzard de qué puede hacer en co-op alguien sin expansión.** No existe página oficial con esa tabla; la §7 se apoya en foro oficial + coberturas.
14. **Página actualizada de Ciudadela Oscura en fuente preferente para la era Lord of Hatred / S14.** Wowhead sigue en "Season 12" (03/2026), Icy Veins sin fecha, Maxroll no tiene página propia de Ciudadela Oscura que haya localizado. **Toda la §4 hereda esta reserva.**
15. **Notas oficiales del parche 3.1.3.** No he localizado el artículo de news.blizzard.com para 3.1.3. Lo del 3.1.3 en este informe viene de coberturas de terceros y está marcado como tal.
16. **Cambios de Ciudadela Oscura o Undercity introducidos por Lord of Hatred.** Las notas 3.0 solo contienen correcciones de errores, ninguna alteración de mecánica.
17. **"Deathtoll Chambers"** — mencionado como actividad de S14 que "encaja en los Planes de Guerra" en un resumen de búsqueda, pero **no aparece en el fichero de datos entre los 7 árboles de Planes de Guerra** ni lo he leído en página preferente. Puede ser mecánica estacional (otro dominio) o un nombre erróneo. **No lo doy por bueno.**
