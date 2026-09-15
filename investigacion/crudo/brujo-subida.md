# Subida de 1 a 70 con Brujo (Temporada 15 — Legado del Infierno, parche 3.2.1)

> **Momento de redacción: 15 de septiembre de 2026, ANTES de las 18:30 CEST.**
> La temporada no ha arrancado. No hay ni una sola partida real de la S15, ni un tiempo 1-70
> medido, ni un leaderboard. Todo lo que sigue sale de notas de parche oficiales y de guías
> escritas **antes** del 3.2.1. Donde una cifra viene de una guía de la S14, lo digo en la
> misma línea que la cifra.

## Resumen

**Ni Maxroll ni Icy Veins tienen una sola guía de subida de Brujo actualizada a la Temporada 15**: a 15 de septiembre las siete guías de subida de Brujo de Maxroll siguen etiquetadas "Season 14 - Death Awakening" (la más reciente, Esbirros, es del 17 de julio de 2026), y la de Icy Veins es del 26 de junio. Maxroll sí actualizó a S15 las guías de subida de Hechicera, Bárbaro, Paladín, Espiritista, Pícaro y Druida — el Brujo y el Nigromante se quedaron fuera. Consecuencia práctica: **el jugador va a subir con una guía de la temporada anterior, y hay que decírselo**. Del cruce entre esas guías y los cambios reales del 3.2.1 sale que **Dread Claws (Garras de Pavor) es la apuesta más segura para subir**: es la única build A de Brujo cuyo núcleo de niveles 3-34 recibió **subidas** en el 3.2.1 (daño base 50%→70%, Ravenous Jaws 125%→500%) y cuyos objetos definitorios no están entre los recortados. Sobre los orbes de XP, **la premisa del encargo es correcta pero incompleta**: el salto de 2 a 4 orbes base sí está cerrado tras Tormento X (que exige nivel 70 y Foso 80, o sea letra muerta durante la subida), pero la **duplicación de los nodos de recompensa Mágico/Raro/Legendario/Mítico no tiene puerta de dificultad** y vale desde el nivel 1. Y hay una trampa que nadie ha contado todavía: el 3.2.1 **recortó** las Larvas del nodo Hellmouth, justo la mecánica que la ruta clásica pescaba.

## Hallazgos

### 0. La advertencia que manda sobre todo lo demás: no hay guía de Brujo para esta temporada

| Dato | Detalle | Fuente | Fecha de la página | Evidencia |
|---|---|---|---|---|
| Guías de subida de Brujo actualizadas a S15 en Maxroll | **Ninguna.** Las 7 (Blazing Scream, Lunatic, Esbirros, Hell Fracture, Dread Claws, Eviscerate, Apocalipsis) siguen marcadas "Season 14 Death Awakening" | https://maxroll.gg/d4/build-guides | índice últ. act. 14 sep 2026 | oficial de la fuente |
| Clases que **sí** tienen guía de subida S15 en Maxroll | Hechicera (Ice Shards, Frozen Orb, Incinerate, Ice Spikes, Blizzard, Firewall), Bárbaro (Whirlwind, Frenzy Throw, HotA, Rend), Paladín (Blessed Hammer, Divine Lance, Zeal, Shield of Retribution), Espiritista (Rock Splitter Thorns, Crushing Hand, Stinger), Pícaro (Penetrating Shot, Flurry, Twisting Blades, Dance of Knives, Heartseeker), Druida (Companion, Shred, Lightning Storm) | https://maxroll.gg/d4/build-guides | 14 sep 2026 | oficial de la fuente |
| Guía de subida de Brujo de Icy Veins | Últ. act. **26 de junio de 2026**, Temporada 14. **No menciona ni el 3.2.1 ni la S15** | https://www.icy-veins.com/d4/guides/warlock-leveling-guide/ | 26 jun 2026 | oficial de la fuente |
| Tier list de subida de Brujo de Maxroll | Últ. act. **30 de junio de 2026**, Temporada 14. **No menciona ni el 3.2.1 ni la S15** | https://maxroll.gg/d4/tierlists/warlock-leveling-builds-tier-list | 30 jun 2026 | oficial de la fuente |
| Guía de subida rápida de Icy Veins | Es de la **Temporada 7** (Brujería): habla de Witchtide, de campaña hasta nivel 40-42 y de "Pit 20 para desbloquear Tormento I". **Inservible para la S15** | https://www.icy-veins.com/d4/guides/speed-leveling-guide/ | sin fecha legible; contenido de la S7 | unica |
| Guía de subida rápida (alts) de Maxroll | Últ. act. **30 de junio de 2026**, Temporada 14. Es la única ruta 1-70 detallada que sigue siendo estructuralmente válida (Planes de Guerra, Ciudad Subterránea) | https://maxroll.gg/d4/meta/alt-leveling-guide | 30 jun 2026 | oficial de la fuente |

**Lo que esto significa:** todo orden de habilidades, toda dificultad y todo objeto que se cite abajo está escrito sobre el juego de la S14. La estructura (qué habilidad desbloquea a qué nivel) no cambia con un parche de equilibrio, así que **los niveles de desbloqueo se pueden dar por buenos**; lo que puede haber envejecido mal es *qué build conviene*, y eso lo reconstruyo yo cruzando con el 3.2.1 en el apartado 7.

### 1. Qué build de subida recomiendan las fuentes preferentes

**Maxroll — tier list global de subida** (etiquetada "Season 15 - Hell's Legacy", últ. act. **14 sep 2026**), https://maxroll.gg/d4/tierlists/leveling-tier-list:

| Build de Brujo | Tier | Evidencia |
|---|---|---|
| Apocalypse Warlock (Apocalipsis) | **A** | unica |
| Minion Warlock (Esbirros) | **A** | unica |
| Dread Claws Warlock (Garras de Pavor) | **A** | unica |
| Lunatic Warlock | B | unica |
| Eviscerate Warlock | B | unica |
| Blazing Scream Warlock | B | unica |
| Hell Fracture Warlock | B | unica |

S-tier completa de esa misma lista (ningún Brujo): Dance of Knives Rogue, Frenzy Throw Barb, Barrage Rogue, Minion Necro, Blizzard Sorc, Shield of Retribution Paladin, Stinger Spiritborn, Rock Splitter Thorns Spiritborn.

**Ojo con esa lista**: aunque la cabecera diga S15 y la fecha sea del 14 de septiembre, **el reparto A/B de Brujo es idéntico, build por build, al de la tier list específica de Brujo fechada el 30 de junio para la S14** (https://maxroll.gg/d4/tierlists/warlock-leveling-builds-tier-list). Es re-etiquetado, no reevaluación: nadie ha podido medir un 1-70 de S15 porque la temporada no ha salido. Metodología que declara la propia página: *"ranks all builds by the most important factors of leveling: Movement speed, survivability, ease of play, damage output and total time to reach level 70 in a season start scenario without resources, tempers or aspects unlocked."*

**Icy Veins** (últ. act. **29 jun 2026**, S14), https://www.icy-veins.com/d4/guides/leveling-tier-list/ y https://www.icy-veins.com/d4/guides/warlock-leveling-guide/ — nombra **tres** builds de Brujo, con nombres que no coinciden con los de Maxroll:

| Build (nombre de Icy Veins) | Habilidades que lista | Tier | Evidencia |
|---|---|---|---|
| **Demon Summoner** (Invocador de demonios) | Command Fallen, Dread Claws, Command Ae'grom, Fiend of Abaddon, Nether Step, Sigil of Subversion | **S** | unica |
| **Abyss Rampage** | Command Fallen, Terror Swarm, Rampage, Sigil of Subversion, Nether Step, Command Laalish | **S** | unica |
| **Hellfire Abodian** | Hellion Sting, Rampage, Metamorphosis, Tyrant's Grasp, Nether Step, Command Abodian | **A** | unica |

Cita literal de Icy Veins sobre la velocidad de la clase: *"Due to limited access to modifiers affecting our Dominance resource the Warlock is not the fastest leveling class in the game. However, it picks up the pace the better gear and higher level you get."* (26 jun 2026). Esto es de la S14 y **es anterior a los buffs de Metamorfosis del 3.2.1** (Dominancia por habilidad básica 2 → 5), que atacan justo ese problema.

### 2. El orden de puntos tramo a tramo — lo que REALMENTE hay escrito

**Aviso de método, importante:** ninguna fuente preferente publica un reparto literal punto a punto ("a nivel 1 pon 1 punto aquí, a nivel 2 otro allá"). Lo que publican son **hitos de desbloqueo**: a qué nivel entra cada habilidad en la barra. Lo que sigue es exactamente eso, sin inventar el relleno. Si alguien presenta un "orden de puntos nivel a nivel" para el Brujo de la S15, se lo ha inventado.

**Dread Claws / Garras de Pavor** (Wudijo) — https://maxroll.gg/d4/build-guides/dread-claws-warlock-leveling-guide — últ. act. **30 jun 2026, S14** · evidencia: unica

| Nivel | Qué entra |
|---|---|
| 3 | **Dread Claws** (habilidad principal / Core) |
| 4 | **Nether Step** (movilidad) |
| 8 | **Rampage** |
| 9 | Mejora de **Hellion Sting** → Eviscerate |
| 14 | **Hellion Sting** variante Tail Spikes |
| 15 | Mejora **Encircling Terror** + se desbloquea el **Mastermind Shard** (Fragmentos de Alma) |
| 20 | Variante **Abyssal Titan** |
| 30 | Se desbloquean los **Fragments** |
| **34** | **Respec:** quitar Hellion Sting y el Sigilo; meter **Command Fallen** y **Dark Prison**; Nether Step → Recall Shadows |
| **40** | **Respec:** quitar Dark Prison; meter **Metamorphosis – Terror Demon** |

**Esbirros / Minion Warlock** (MacroBioBoi) — https://maxroll.gg/d4/build-guides/minion-warlock-leveling-guide — últ. act. **17 jul 2026, S14** (la guía de Brujo más reciente que existe) · evidencia: unica

| Nivel | Qué entra |
|---|---|
| 1 | **Command Fallen** (habilidad de arranque) |
| 3 | **Bombardment** |
| 4 | **Nether Step** y **Dark Prison** |
| 9 | **Rampage** |
| 13 | **Sigil of Summons** |
| 14 | Mejora de Command Fallen: **Mega Lunatic** |
| 15 | **Summon Ae'grom** + se desbloquean los **Fragmentos de Alma** |
| 30 | **Sacrificial Fragment** |
| 34 | *"most of the key synergies are unlocked"*; de 34 a 70, puntos a subir rangos |

Sin hitos de respec marcados: esta build va por un solo camino.

**Apocalipsis** (Wudijo) — https://maxroll.gg/d4/build-guides/apocalypse-warlock-leveling-guide — últ. act. **30 jun 2026, S14** · evidencia: unica

| Nivel | Qué entra |
|---|---|
| 1 | **Command Fallen** |
| 3 | **Bombardment** |
| 4 | **Nether Step** |
| 8 | **Rampage** |
| 12 | **Lesser Demon Wrath** |
| 15 | **Summon Ae'grom** |
| 17 | **Elite Eviscerate** |
| 22 | **Terror Swarm** |
| 25 | **Metamorphosis – Destruction Demon** |
| **32** | **Respec mayor:** pasar a **Apocalypse – Annihilation** + **Umbral Chains – Chain Whips** |

Nota estructural que importa: **hasta el nivel 32 esta build es en realidad una build Lunatic**; Apocalipsis como tal no existe hasta ese respec. Eso cambia el análisis de los recortes (apartado 7).

**Blazing Scream** (MacroBioBoi) — https://maxroll.gg/d4/build-guides/blazing-scream-warlock-leveling-guide — últ. act. **29 jun 2026, S14** · evidencia: unica

| Nivel | Qué entra |
|---|---|
| 3 | **Blazing Scream** |
| 4 | **Dark Prison** |
| 9 | **Rampage** |
| 13 | **Sigil of Chaos** |
| 15 | Fragmentos de Alma (primer nivel) |
| 24 | **Apocalypse** |
| 30 | Fragmentos de Alma (segundo nivel) |
| 36 | **Demonic Smash** |

**Contradicción a la cara entre guías del mismo sitio:** Rampage aparece a **nivel 8** en las dos guías de Wudijo (Dread Claws y Apocalipsis) y a **nivel 9** en las dos de MacroBioBoi (Esbirros y Blazing Scream). Una de las dos cifras está mal y no puedo decidir cuál sin ver la pantalla del juego. **Se resuelve en 5 segundos abriendo el árbol de habilidades.**

### 3. A qué dificultad jugar en cada tramo

Primero, los números duros de XP, que son lo único que no opina:

| Dificultad | Bonus de experiencia | Requisito | Fuente | Fecha | Evidencia |
|---|---|---|---|---|---|
| Normal | base | — | https://maxroll.gg/d4/resources/experience | 21 jul 2026 (S14) | unica |
| **Difícil (Hard)** | **+75 %** | — | ídem | 21 jul 2026 | unica |
| Experto (Expert) | +125 % | — | ídem | 21 jul 2026 | unica |
| Penitente (Penitent) | +175 % | Terminar la campaña base *Legado de los Horadrim*, **o saltársela** | https://maxroll.gg/d4/resources/difficulty-overview | 26 jun 2026 | corroborado (dos páginas de Maxroll) |
| Tormento I | +300 % XP de muerte | **Nivel 70** + Foso 10 | https://maxroll.gg/d4/resources/difficulty-overview | 26 jun 2026 | unica |
| Tormento X | **+1200 %** | **Nivel 70** + **Foso 80** | ídem | 26 jun 2026 | unica |
| Tormento XII | +1400 % | Nivel 70 + Foso 100 | ídem | 26 jun 2026 | unica |

Tabla completa de Tormento (Foso requerido / bonus XP): I=10/300 %, II=15/400 %, III=20/500 %, IV=25/600 %, V=30/700 %, VI=40/800 %, VII=50/900 %, VIII=60/1000 %, IX=70/1100 %, X=80/1200 %, XI=90/1300 %, XII=100/1400 %. Cita literal: *"Players must reach level 70 and progress through the Pit to unlock the new Torment Difficulties."*

**Lo que recomiendan, tramo a tramo:**

| Tramo | Recomendación | Fuente | Fecha | Evidencia |
|---|---|---|---|---|
| Arranque (1-~15) | *"Ideally, start on Normal or Hard difficulty for the extra XP modifier, then try to go higher when it's way too easy."* | guías de Brujo de Maxroll (Dread Claws / Blazing Scream) | 29-30 jun 2026 | corroborado (3 guías de Maxroll dicen lo mismo) |
| Todo el recorrido | *"Preferably, stay on Hard difficulty or above"* para conservar el multiplicador de XP | guía de Esbirros de Maxroll | 17 jul 2026 | unica |
| Regla general | *"select a difficulty where you are quick and efficient, and only increase the difficulty if you find yourself overkilling enemies"* | https://maxroll.gg/d4/meta/alt-leveling-guide | 30 jun 2026 | unica |
| Icy Veins (Brujo) | Empezar en **Difícil**. Experto es posible, pero *"the extra experience from monsters does not make up for the increased time it takes to kill them"* | https://www.icy-veins.com/d4/guides/warlock-leveling-guide/ | 26 jun 2026 | unica |
| **Truco de Oleada Infernal** | Farmear las Cenizas Aberrantes *"on a comfortable difficulty, but swapping to Penitent when you turn in the chests"* — se abre el cofre en Penitente para cobrar la XP al +175 % | https://maxroll.gg/d4/meta/alt-leveling-guide | 30 jun 2026 | unica |

**El tramo que ninguna fuente cubre:** de Penitente a Tormento I hay un salto de +175 % a +300 %, pero **Tormento I exige ya el nivel 70 y Foso 10**. O sea: durante toda la subida 1→70 el techo real es Penitente (+175 %). Ningún Tormento entra en la ecuación de la subida. Esto lo derivo de la tabla de arriba, no lo dice ninguna página con esas palabras — **evidencia: corroborado (derivado de dos páginas de Maxroll)**.

### 4. La ruta general de subida de la temporada

Ruta única disponible, de https://maxroll.gg/d4/meta/alt-leveling-guide (últ. act. **30 jun 2026, Temporada 14** — la estructura sigue viva porque los Planes de Guerra y la Ciudad Subterránea no han cambiado de sitio, pero **nada en ella contempla la S15**) · evidencia: **unica** en todos sus puntos:

**Antes de empezar**
- Saltarse la campaña, para *"enter the most dense areas of the game at Level 1"*.
- Crear el personaje con la campaña de *Lord of Hatred* ya completada.
- Coger **Mercenarios** de inmediato.
- Arrancar la **línea de misiones estacional** para abrir la vía de reputación de temporada.

**Niveles 1-25 — Oleada Infernal + Mazmorras de Pesadilla en paralelo**
- Prioridad simultánea a Oleadas Infernales y Mazmorras de Pesadilla.
- *"Fish for two War Plans connected to Helltides on level 1"* — pescar **dos** Planes de Guerra ligados a Oleada Infernal desde el nivel 1.
- Objetivo: correr al nodo **Writhe and Rot**, que da *"insane experience gain overall"* y llaves extra de Guarida de Jefe (https://maxroll.gg/d4/resources/war-plans, 5 ago 2026).
- Encadenar Favores Macabros del Árbol de los Susurros mientras tanto.
- Llenar el medidor de amenaza matando todo; **guardar las Cenizas** y abrir los cofres al final de la Oleada para maximizar XP.
- *"Save up all Baneful Hearts for when you are Level 70"* — los Corazones Funestos (Doncella de Sangre) **no dan XP**, así que se guardan.

**Nivel 25 — pivote a la Ciudad Subterránea de Kurast**
- A nivel 25 se abren los Planes de Guerra de la Ciudad Subterránea.
- *"Gamble 2/3 of the War Plans to be Undercity to rush the Jade Epiphany upgrade"* — apostar dos de cada tres Planes a Ciudad Subterránea para llegar cuanto antes a **Jade Epiphany**.
- Jade Epiphany escala con la dificultad, lo que a su vez permite farmear más arriba.

**Niveles 25-70**
- Planes de Guerra de Oleada Infernal **y** Ciudad Subterránea a la vez, una vez tienes Jade Epiphany.
- Seguir con Mazmorras de Pesadilla, priorizando **los eventos de la mazmorra** sobre limpiarla entera.
- Jugar en grupo cuando se pueda: **+5 %** de XP por jugadores cerca, **+10 %** si además están en tu grupo; radio de 90 metros, sin límite de radio dentro de mazmorras (https://maxroll.gg/d4/resources/experience, 21 jul 2026). Las hogueras apilan hasta **+15 %**.

**Cómo funcionan los Planes de Guerra** (https://maxroll.gg/d4/resources/war-plans, 5 ago 2026):
- Se monta una lista de hasta **cinco** actividades.
- Cada tipo de actividad tiene su árbol: **7 niveles, 1 punto por nivel**.
- Se pueden **rerrollear hasta tres veces** con el botón *New Plans* — eso es el "pescar".
- Se desbloquean *"once you complete the Lord of Hatred Campaign"* (no da nivel mínimo).

**Novedad de la S15 que cambia la ruta — Planes de Guerra compartidos.** Cita oficial: *"Starting in Season of Hell's Legacy, points you earn in War Plans for one character will be shared across alts on your account that exist in the same partitions within these categories: Eternal/Seasonal; Non-Hardcore/Hardcore; Normal/Solo-Self Found."* (https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy, 12 sep 2026) — **oficial**. Cada personaje mantiene su propio planificador de asignación.
Matiz que hay que decirle al jugador: **Eterno y Estacional son particiones distintas**, así que el Brujo estacional **no** hereda nada del tablero de un personaje Eterno. Compartes entre alts estacionales, no desde el Eterno.

**Renacimiento (Rebirth):** *"Rebirth allows you to convert characters from Eternal to Seasonal states, transferring that character to the Seasonal realm and resetting to level 1."* (mismo artículo oficial, 12 sep 2026) — **oficial**. Conserva clase, nombre, aspecto y cosméticos, pero **resetea a nivel 1**: no es un atajo de subida.

**Bastiones: no confirmado.** El encargo daba por hecho "bastiones al principio". **La ruta viva de Maxroll (30 jun 2026) no menciona Bastiones en ningún punto.** Lo único que los mete en una ruta de subida es la guía de Icy Veins, y ahí están en el tramo 50-60 y **es contenido de la Temporada 7** (habla de Witchtide y de campaña hasta nivel 40). **No publiques "bastiones al principio" como si estuviera verificado: no lo está.**

### 5. Los orbes de XP — la comprobación que pedía el encargo

**Veredicto: la premisa del encargo es correcta en lo que afirma, pero se deja fuera la mitad buena y la trampa mala.**

Todas las citas siguientes son del parche 3.2.1, oficiales en https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026) y transcritas igual en https://maxroll.gg/d4/news/diablo-4-3-2-1-patch-notes (12 sep 2026) → **corroborado, con original oficial**:

| Cambio | Cita literal | ¿Puerta de dificultad? | Vale durante la subida |
|---|---|---|---|
| Base de los Planes de Guerra | *"Increased the baseline number of Experience Orbs awarded for completing any War Plans node in **Torment X and above** from 2 to 4, regardless of reward type or rarity."* | **Sí, Tormento X+** | **NO** |
| Nodos de recompensa Mágico/Raro/Legendario/Mítico | *"Doubled the number of Experience Orbs awarded by Magic, Rare, Legendary, and Mythic Experience reward nodes."* | **No, ninguna** | **SÍ, desde nivel 1** |
| Jade Epiphany (Ciudad Subterránea) | *"Doubled the number of Experience Orbs spawned by the Jade Epiphany Undercity node."* | **No** | **SÍ, desde nivel 25** |
| Choron's Soul (El Foso) | *"Doubled Experience from Progress Orbs while the Choron's Soul Pit node is active."* | **No** | sí, si haces Foso |
| Alijos de Susurros | *"Increased Experience Orbs from Whisper Caches from 3-5 to 4-6, with an additional 2-4 Experience Orbs in **Torment X and above**."* | **Mixta**: el 3-5→4-6 no; los +2-4 sí | **SÍ el 3-5→4-6** |
| Bonus del Foso alto | *"Increased Bonus Experience from higher Pit Tiers. Example: Pit Tier 150 increased from 1800% to 2700%."* | — | no |
| General | *"Experience rewards from War Plans have been increased, and they scale heavily with Torment levels."* | — | — |

**Y la puerta de Tormento X es efectivamente inalcanzable subiendo:** Tormento X pide **Foso 80**, y *"Players must reach level 70 and progress through the Pit to unlock the new Torment Difficulties"* (https://maxroll.gg/d4/resources/difficulty-overview, 26 jun 2026). O sea, el 2→4 es un cambio de endgame puro. **Confirmado: correcto lo que decía el encargo.**

**La trampa que el encargo no tenía — el 3.2.1 RECORTÓ las Larvas del Hellmouth.** Dos citas literales del mismo parche, sección Oleada Infernal:

> *"Reduced the chance for Plague Maggot Young spawned by the Hellmouth Helltide node to drop Experience Orbs."*
> *"Portent of Pain and Plague Devourers now drop 1-2 Experience Orbs instead of always dropping 2."*

— https://news.blizzard.com/en-us/article/24295394/... (12 sep 2026) y https://maxroll.gg/d4/news/diablo-4-3-2-1-patch-notes (12 sep 2026) · **corroborado, con original oficial**.

Es decir: la idea de que "los nodos Hellmouth garantizan Larvas con orbes de XP" era cierta **en la S14** y **el 3.2.1 la ha podado deliberadamente**. Los Devoradores pasaron de 2 orbes garantizados a 1-2. Cualquier guía que hoy venda el Hellmouth como el motor de XP de la Oleada Infernal está describiendo el juego de la semana pasada. **Writhe and Rot sigue siendo el nodo prioritario** — eso no lo tocaron — pero el rendimiento concreto por larva ya no es el de la S14 y **nadie lo ha medido todavía**.

### 6. Únicos y aspectos que hay que buscar MIENTRAS subes

**El cambio del 3.2.1 que lo reordena todo** (cita literal, sección de objetos): *"All Unique items are now available to drop at level 1, and in any Difficulty."* — https://maxroll.gg/d4/news/diablo-4-3-2-1-patch-notes (12 sep 2026) · **corroborado** con https://www.icy-veins.com/d4/news/buffed-resistances-and-increased-legendary-and-mythic-unique-drop-rates-diablo-4-season-15-item-updates/. Hasta ahora buscar un único concreto a nivel bajo no tenía sentido; **ahora sí lo tiene**, y esto es lo que convierte esta sección en accionable de verdad.

Otros cambios de botín del 3.2.1 que afectan a la subida:
- *"Increased Legendary Item drop rates in **Torment I through Torment V**. Torment VI and above are unchanged."* → **no aplica** durante la subida (Tormento pide nivel 70).
- *"Increased the chance for Mythic Uniques to drop from random sources."*, *"Increased the Mythic Unique drop rate from Initiate Lair Bosses to match the rate of Greater Lair Bosses."* → aplica a cualquier nivel.
- *"Single Resistance affixes are now 7 times the value of All Resistance affixes."* → **cambia qué defensa recoger subiendo**: un afijo de resistencia única pasa a valer mucho más que "todas las resistencias". Esto ninguna guía de subida de Brujo lo refleja todavía.

**Lo que hay que cazar, por build** (nombres en inglés: las fuentes preferentes no publican los nombres en español del Brujo — ver Huecos):

| Build | Únicos definitorios | Únicos "buenos" | Aspectos legendarios a imprimir | Fuente | Fecha |
|---|---|---|---|---|---|
| Dread Claws | Spine of Tathamet, Anathema of the Primes | **Litany of Sable**, **Seed of Horazon** | Accelerating, Edgemaster's, Fortress, Deeper Shadows, Malevolence, Insidious, Calamity, Juggernaut's | https://maxroll.gg/d4/build-guides/dread-claws-warlock-leveling-guide | 30 jun 2026 |
| Esbirros | **Ae'grom's Schism**, **Eye of Baal** | Seed of Horazon | Malicious, Demonic, Heavenly Strength, Hellbent Commander | https://maxroll.gg/d4/build-guides/minion-warlock-leveling-guide | 17 jul 2026 |
| Apocalipsis | Spine of Tathamet, Litany of Sable, Anathema of the Primes, **Cage of Madness** | **Hands of the Worldbreaker**, Fleshwrit Carapace, Moloch's Beating Flame | Vehement Brawler's, Cremator's, Edgemaster's, Scorching Heat, Fortress | https://maxroll.gg/d4/build-guides/apocalypse-warlock-leveling-guide | 30 jun 2026 |
| Blazing Scream | Ae'grom's Schism, Anathema of the Primes, Litany of Sable, **Hands of the Worldbreaker** | Moloch's Beating Flame, **Temerity**, Seed of Horazon | Malicious, Demonic, Heavenly Strength, Hellbent Commander | https://maxroll.gg/d4/build-guides/blazing-scream-warlock-leveling-guide | 29 jun 2026 |

Evidencia de toda esa tabla: **unica** (una sola guía por build, y todas de la S14).

**Dos avisos que hay que dar con la tabla, no después:**
- **Hands of the Worldbreaker** y **Cage of Madness** salen en esa tabla como piezas deseables — y son exactamente **dos de los objetos recortados en el 3.2.1**. Hands of the Worldbreaker queda en *"Apocalypse: 290-350% damage"*; Cage of Madness pasa su daño de Command Fallen de **300-340 % a 100-200 %**. Las guías que los recomiendan son de junio y no saben nada de ese recorte.
- **El único que el 3.2.1 convierte en objetivo prioritario y que ninguna guía menciona todavía: Hellhound's Sabatons.** Cambio literal: *"Abodian: 80-100% → 200-280% damage"*, *"Triggers Non-Archfiend Hellfire Skills while moving"*, *"Cooldown reduced 50%"* (https://maxroll.gg/d4/news/diablo-4-3-2-1-patch-notes, 12 sep 2026 · **oficial vía transcripción de Maxroll**). Casa con la build **Hellfire Abodian** que Icy Veins pone en A para subir, y **Command Abodian** también subió: mordisco de **155 % → 245 %**, además de *"Now Unhindered, prioritizes Elites"*. Command Abodian se desbloquea con los **Fragmentos de Alma a nivel 15**. Como ahora los únicos caen desde nivel 1, **merece la pena tener estas botas en el filtro de botín desde el minuto uno**. Que la sinergia funcione en la práctica **no lo ha probado nadie**: es mi lectura del parche, no un dato medido. **Evidencia: derivado / sinconfirmar.**

Otros dos únicos muy subidos en el 3.2.1, por si caen: **Gauntlets of Sheol** (*"Damage increase: 23-33% → 40-50% per demon, max 600-750% for 60 seconds"*) y **Hands of Apotheosis** (*"Any Demonform grants all Metamorphosis Upgrades free, 50-100% more potent"*). Ambos son piezas de Demonform/endgame, no de los primeros 30 niveles.

### 7. Cómo muerden los recortes del 3.2.1 a cada build de SUBIDA

Esta es la parte que no existe en ninguna página y que hay que construir cruzando los hitos del apartado 2 con las notas del parche. **Todo lo de este apartado es análisis derivado: evidencia `derivado`, salvo las cifras del parche, que son oficiales.**

Nota del desarrollador, literal: *"Warlock is performing well with many of their newly improved options. These updates focus on maintaining momentum and build diversity while pruning unintuitive or oppressive scalars."*

Y un dato estructural que pesa sobre toda la clase: **el Brujo no recibió subida de escalar de estadística principal**. Druida, Nigromante, Paladín y Hechicera pasaron de **1,25 a 1,625** *"Damage per 10 points"*; el Bárbaro bajó de 1,1 a 0,8; **el Brujo se queda como estaba** (https://maxroll.gg/d4/news/diablo-4-3-2-1-patch-notes, 12 sep 2026 · **oficial vía Maxroll**). Es un recorte relativo silencioso: cuatro clases ganan ~30 % de daño por estadística y el Brujo no.

| Build de subida | ¿Le entra algún recorte en su tramo 1-70? | Qué le sube el 3.2.1 en ese tramo | Lectura |
|---|---|---|---|
| **Dread Claws** | **No.** Su núcleo (niveles 3-34) no usa Hands of the Worldbreaker ni Cage of Madness ni depende de Demonform | Dread Claws **50 % → 70 %** de daño base y pasa a ser Greater Demon Skill; **Ravenous Jaws: Eviscerate 125 % → 500 %**; Legion Shard *Evisceration Fragment*: probabilidad 2 % → 5 % y daño **200 % → 1000 %**; Hellion Sting pasa a Lesser Demon Skill | **La apuesta más segura.** Es la única A de Brujo cuyo tramo de subida sale del parche mejor de lo que entró |
| **Esbirros** | **No** | Vanguard Shard: **Rampage Brute 13 % → 128 %**; Sigil of Summons **60 % → 80 %**; Command Ae'grom *"Now Unhindered, prioritizes Elites"*; nodo **Dynamism** ahora da *"85% Summon Skill damage while not in Demonform"* | Buffeada. Segunda opción sólida, y la guía es la más reciente que existe (17 jul) |
| **Apocalipsis** | **Parcialmente.** Recuerda que **hasta el 32 es una build Lunatic**, y Lunatic depende de **Cage of Madness**, recortada de 300-340 % a 100-200 % | Rampage y Terror Swarm suben (Terror Swarm **100 % → 130 %/s**, ráfaga **500 % → 650 %**, bonus a Vulnerable **20 % → 40 %**); Metamorphosis da **5 de Dominancia** por básica en vez de 2 | Sigue A en la lista, pero **su objeto definitorio post-32 (Hands of the Worldbreaker) está recortado a 290-350 %** y su fase previa depende de una pieza recortada. Es la build de Brujo con más riesgo de que la guía de junio envejezca mal |
| **Lunatic** | **Sí, de lleno.** Cage of Madness: Command Fallen **300-340 % → 100-200 %** | Radio de explosión +66 %, +60 % de velocidad de movimiento, aparecen Mini Lunáticos | Ya era B. **Es el recorte más duro del parche a una build de subida de Brujo. Yo no subiría con esta** |
| **Blazing Scream** | **Sí.** Su único definitorio es **Hands of the Worldbreaker** | Cap de Brimstone Hunger **25 % → 50 %**; **Elegy** convierte Blazing Scream en Archfiend Skill y sube su daño **20-30 % → 30-50 %**, los cráneos ya no desaparecen contra las paredes | B antes y B ahora. Gana por un lado y pierde por el otro |

## Huecos

- **No existe ninguna guía de subida de Brujo para la Temporada 15.** Ni Maxroll ni Icy Veins. Todo lo de arriba es S14 releída a la luz del 3.2.1. Este es el hueco grande y hay que enseñarlo, no esconderlo.
- **No hay reparto literal de puntos nivel a nivel** para ninguna build de Brujo en ninguna fuente preferente: solo hitos de desbloqueo. No se puede escribir "a nivel 5 pon el punto aquí" sin inventarlo.
- **Niveles de desbloqueo de actividades: no encontrados por escrito.** Oleada Infernal, Mazmorras de Pesadilla, Hordas Infernales, Árbol de los Susurros, Mercenarios — ninguna página preferente da el nivel mínimo. De los Planes de Guerra solo tengo *"once you complete the Lord of Hatred Campaign"* (sin nivel), y de la Ciudad Subterránea solo el "nivel 25" que da la ruta de subida de Maxroll, que **no** cita la página de Planes de Guerra.
- **No he encontrado la descripción textual de los nodos Hellmouth, Writhe and Rot ni Jade Epiphany.** La página de Planes de Guerra de Maxroll (5 ago 2026) los nombra y dice en qué orden cogerlos, pero **no transcribe qué hacen**. Todo lo que tengo de ellos son las notas del parche que los modifican.
- **Bastiones en la ruta de subida de la S15: sin confirmar.** Ninguna fuente preferente vigente los incluye.
- **Nombres en español de habilidades y únicos del Brujo: no encontrados.** El artículo es-es de Blizzard no lista ni Hands of the Worldbreaker ni Hellhound's Sabatons ni Dread Claws. Todo lo de arriba va en inglés y marcado como tal. **Habría que sacarlos de la pantalla del juego en español.**
- **Qué Astilla del Mal conviene para subir: no encontrado.** La guía de temporada de Maxroll (13 sep 2026) *"doesn't identify which splinter aids leveling most"*. Nota propia, sin confirmar: la Astilla de Diablo modifica Oleada Infernal y Hordas Infernales, que son justo las actividades de la ruta 1-25, pero **nadie lo ha escrito**.
- **Pesadillas de Vigilia: sin datos de nivel ni de XP.** La guía de temporada las describe en tres tamaños pero *"provides no specific level requirements or XP rewards"*. No sé si entran en la ruta de subida.
- **Tiempo real 1-70 con Brujo en la S15: no existe.** Cualquier cifra ("1h28m") que circule hoy es de la S14, del PTR, o inventada.
- **Cuánto duele exactamente el recorte de las Larvas del Hellmouth**: el parche dice "reduced the chance" sin número. Nadie lo ha medido.
- **El escalar del Brujo (1,25) frente al 1,625 de las cuatro clases subidas**: confirmado que el Brujo no subió, pero **no he encontrado el valor del Brujo escrito con esa cifra en el parche 3.2.1**; lo doy por el contexto del encargo, no por haberlo leído. Marcar como `sinconfirmar` hasta verlo escrito.

## Contradicciones

1. **Planes de Guerra compartidos.** La página de recurso de Maxroll (5 ago 2026) dice literalmente lo contrario de lo que dice Blizzard para la S15: *"Every alt has an individual War Plans board, and activity experience is not shared, so you must level one from scratch for every character you create."* Blizzard, 12 sep 2026: los puntos **se comparten** dentro de la misma partición. **Gana Blizzard**: la página de Maxroll es anterior al anuncio. Es el ejemplo perfecto de página de sitio preferente que ha caducado sin avisar.
2. **Tier de las builds de Brujo: Maxroll contra Icy Veins.** Maxroll no pone ningún Brujo en S para subir (lo más alto es A). Icy Veins pone **dos** builds de Brujo en **S** (Demon Summoner, Abyss Rampage). Y ni siquiera usan los mismos nombres de build, así que no siempre se puede saber si hablan de lo mismo. Las dos listas son de junio de 2026 y de la S14. **Disputa sin resolver.**
3. **Nivel de Rampage: 8 o 9.** Wudijo dice 8 (Dread Claws, Apocalipsis); MacroBioBoi dice 9 (Esbirros, Blazing Scream). Mismo sitio, mismo parche, dos cifras. **Se comprueba en el árbol de habilidades del juego.**
4. **La tier list "de la S15" que en realidad es de la S14.** https://maxroll.gg/d4/tierlists/leveling-tier-list dice "Season 15 - Hell's Legacy" y "14 sep 2026", pero su reparto de Brujo coincide **exactamente** con el de la tier list específica de Brujo fechada el 30 de junio para la S14. Cambiaron la etiqueta, no los datos. Y no podían tener datos: la temporada no había salido.
5. **Dificultad: Difícil contra Normal.** Las guías de Brujo de Maxroll y la de Icy Veins dicen "Difícil o más". La tier list de subida de Icy Veins dice *"level from 1 to 70 during a new season on Normal to Penitent difficulty"* (más laxo), y su guía de subida rápida —que es de la Temporada 7— llega a recomendar Normal. **La de la S7 se descarta por caducada.** Entre las vivas no hay contradicción real: **Difícil (+75 %) como suelo, Penitente (+175 %) para abrir cofres de Oleada Infernal.**
6. **La premisa del encargo sobre el Hellmouth.** El encargo daba por bueno que los nodos Hellmouth "garantizan Larvas con orbes de XP". El propio 3.2.1 lo desmiente: *"Reduced the chance for Plague Maggot Young spawned by the Hellmouth Helltide node to drop Experience Orbs."* Es un caso de "verificar el modelo, no solo los valores": la estrategia entera venía de la S14 y el parche la ha tocado.
7. **"Oleada Infernal" contra "Marea Infernal".** El fichero de anclaje de este proyecto usa **Oleada Infernal** citando el artículo es-es de Blizzard; mi lectura de ese mismo artículo devolvió **"Marea Infernal"**. No he podido resolverlo. **Se resuelve mirando la pantalla del juego en español.**
