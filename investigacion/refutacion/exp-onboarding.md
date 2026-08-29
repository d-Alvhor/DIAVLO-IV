# Refutación adversarial — `crudo/exp-onboarding.md`

**Verificado:** 20 de agosto de 2026 · **Parche vivo de referencia:** 3.1.3 (build 73224, 12/08/2026)
**Veredicto:** **PARCIAL.** El esqueleto del informe y la mayoría de sus números resisten. Pero **tres citas presentadas como literales no existen en las URL que se les atribuyen**, la cabecera del fichero de datamining **no se reproduce**, una fuente central es **un artículo pre-lanzamiento en futuro** que el propio informe no detectó en su sección de "marco muerto", y **falta una clase entera** en la tabla de compra.

> Método de esta refutación: cada cita sospechosa se ha comprobado sobre el **HTML crudo** de la página (`curl` + extracción de texto + conteo de ocurrencias), no sobre un resumen. Cuando digo "0 apariciones", es un conteo literal sobre el documento descargado hoy.

---

## A. Refutaciones duras (el informe afirma algo que la fuente citada no dice)

### A1. Cita inexistente — los "waypoints" al saltar campaña

El informe, §5.3:

> *"characters that skip either campaign automatically unlock all non-stronghold waypoints for their chosen region"* — [Maxroll Speed Leveling, act. 30/06/2026](https://maxroll.gg/d4/meta/alt-leveling-guide)

**Comprobación sobre el HTML de esa página (318.638 caracteres, descargada 20/08/2026):**

| Término buscado | Apariciones |
|---|---|
| `waypoint` (cualquier caso) | **0** |
| `stronghold` | 2, ambas dentro del *changelog* de 2025 ("Clarified Stronghold Information") |

**La cita no existe en esa página.** Lo que sí dice, literal, es:

- *"Skipping the Campaign allows you to enter the most dense areas of the game at Level 1 and tremendously speeds up the leveling process."*
- *"You can also skip the Lord of Hatred campaign if you want to have War Plans unlocked right away, though the campaign is a very good source of experience."*
- *"The following strategies assume you have completed the Campaign at least once on your account."*

Nótese además que el informe presenta la segunda como *"Skip the Lord of Hatred campaign if you want to have War Plans unlocked right away"* — recorta el inicio y **omite la coletilla** *"though the campaign is a very good source of experience"*.

**Consecuencia:** el "premio de consolación" que §5.3 vende para la S15 (arrancar con todos los santuarios de viaje abiertos) **no tiene fuente**. Borrar o marcar como no verificado.

---

### A2. Cita inexistente — "hasta 3 Amuletos Únicos"

El informe, §4.3, tabla de números concretos:

> Talismán: amuletos únicos equipables — *"you can equip up to 3 Unique Charms"* — [Maxroll Talisman](https://maxroll.gg/d4/resources/talisman-charms-sets)

**Comprobación sobre el HTML de esa página (43.529 bytes, descargada 20/08/2026):**

| Término buscado | Apariciones |
|---|---|
| `up to 3` | **0** |
| `equip up to` | **0** |
| `Unique Charm` | 3, ninguna con cifra de tope |

Lo que la página dice sobre Amuletos Únicos, literal y completo:

> *"Unique Charms are stand-alone Charms that provide the power of their respective Unique item when they're equipped, for instance Tibault's Will (Unique Charms also have 2 random affixes in-game). This makes them ideal to slot in to fill gaps in your Talisman after you've slotted the Set Charms you want."*

**No hay ningún tope de 3.** Además, la búsqueda independiente apunta a que el "3 Amuletos Únicos" no es un límite global sino una **propiedad de un Sello Mítico concreto de la S14** (Seal of the Golden Epiphany) — es decir, el informe habría convertido un condicional en una regla fija. Esa pista viene de fuentes no preferentes (game8, timesaver.gg, odealo), así que **no la doy por buena**: la doy como motivo para retirar el dato, no para sustituirlo.

**Acción:** el número **3** debe salir de la tabla y pasar a "No encontrado".

---

### A3. Cita inexistente — el argumento de orden narrativo

El informe, §7, es la **única evidencia citada** para su recomendación central de orden (VoH antes que LoH) más allá de un hilo de foro sin respuesta:

> *"It picks up the story after the events of Vessel of Hatred"* — [Blizzard](https://diablo4.blizzard.com/en-us/lord-of-hatred)

**Comprobación sobre el HTML de esa página (16.662 caracteres de texto, descargada 20/08/2026):**

| Término buscado | Apariciones |
|---|---|
| `picks up` | **0** |
| `after the events` | **0** |

Lo que la página oficial sí dice sobre la relación entre expansiones, literal:

> *"Purchase Lord of Hatred™ and instantly unlock Diablo IV's first expansion, uncovering the events that set Mephisto's dark ambitions into motion."*

Eso apunta en la misma dirección ("los eventos que pusieron en marcha las ambiciones de Mefisto" = VoH es anterior), pero **no es la frase citada**. La recomendación "VoH primero" sigue siendo razonable como riesgo asimétrico; **el respaldo oficial que el informe le atribuye no existe**.

---

### A4. La cabecera del fichero de datamining no se reproduce

El informe, §10 y sección de Fuentes, declara:

> `https://assets-ng.maxroll.gg/d4-tools/game/data.min.json` — `last-modified: Tue, 18 Aug 2026 15:42:02 GMT`, `version: "3.1.0.72698"`, **11.606.376 bytes**

**Descarga real de hoy (20/08/2026, 11:21 GMT, edge de Madrid):**

```
HTTP/2 200
content-length: 11606292
last-modified: Fri, 14 Aug 2026 15:49:39 GMT
etag: "f3c48f86db532d153c102611fb3b1209"
cf-cache-status: HIT   age: 293999
```

- **Fecha distinta:** 14/08/2026, no 18/08/2026.
- **Tamaño distinto:** 11.606.292 bytes, no 11.606.376 (84 bytes de diferencia).
- **El campo `version` sí coincide:** `3.1.0.72698`.

Puede ser un edge de CDN distinto, pero **la evidencia tal y como está escrita no se reproduce**, y era precisamente la prueba con la que §10 razonaba sobre el desfase de versión. La observación de fondo del informe (el fichero declara 3.1.0 mientras el parche vivo es 3.1.3) **sigue siendo válida y correcta**; la cabecera concreta que la sostiene, no.

---

### A5. "Cada mercenario con 6 habilidades" — falso para Aldkin

El informe, §4.1: *"Cada uno con **6 habilidades**."*

**Contenido real de la clave `mercenaries` del fichero descargado:**

| Clave interna | Nombre | Nº de entradas en `skills` |
|---|---|---|
| `MercenaryClass_ShieldBearer` | Raheir | 6 |
| `MercenaryClass_BerserkerCrone` | Varyana | 6 |
| `MercenaryClass_CursedChild` | **Aldkin** | **14** |
| `MercenaryClass_BountyHunter` | Subo | 6 |

Aldkin lista 6 activas (`Haunt`, `Wither`, `soulChain`, `FlameSurge`, `FireStorm`, `WaveOfFlame`) **más 8 entradas repetidas** de `NPC_Mercenary_CursedChild_passiveA1`. Puede ser un artefacto del volcado, pero el informe afirmó "6 cada uno" sobre un fichero que dice 14 en uno de los cuatro. **Lo confirmado son los 4 mercenarios y sus nombres, no el "6 cada uno".**

*Dato de paso:* el informe dejó la cuarta clave sin identificar ("y una cuarta (Subo)"). Es `MercenaryClass_BountyHunter`.

---

### A6. Falta la clase Spiritborn en la tabla de "qué has comprado"

Ni §1 ni §3 mencionan al **Spiritborn** (Nacido del Espíritu). La página oficial de LoH dice, literal:

> *"Instantly unlock early access to the Vessel of Hatred™ expansion **including the Spiritborn class**, with any Lord of Hatred™ expansion purchase."* — [diablo4.blizzard.com/lord-of-hatred](https://diablo4.blizzard.com/en-us/lord-of-hatred)

El datamining lo corrobora: la clave `classes` tiene **8** entradas — Sorcerer, Druid, Barbarian, Rogue, Necromancer, **Spiritborn**, Paladin, Warlock — y `itemSets` incluye `Talisman_Spirit_01`–`05`.

El jugador acaba de comprar y **tiene tres clases nuevas disponibles, no dos**. Es una omisión material en un informe cuya tesis es "todo lo que antes estaba bloqueado ahora es suyo".

---

### A7. Fila fantasma en una tabla declarada "verbatim"

§1 presenta la lista de la Edición Estándar como *"verbatim de la misma fuente de Blizzard"* ([news.blizzard.com/24247511](https://news.blizzard.com/en-us/article/24247511/stand-against-mephisto-pre-purchase-lord-of-hatred)) e incluye la fila **"Warlock / Brujo (clase) — Al lanzamiento (28/04/2026)"**.

Esa fila **no está en la lista de ese artículo**. El artículo enumera: Expansion 2, Paladin Early Access, Expansion 1 (VoH), 1 Extra Stash Tab, 2 Additional Character Slots, WoW Decor Items. Sobre la segunda clase dice, sin nombrarla: *"A second class looms on the dark horizon"*.

El nombre "Warlock" **sí está verificado**, pero en **otro** artículo: *"Two classes burn into Sanctuary, opposite counterparts of light and dark"* — [Prepare for the Reckoning](https://news.blizzard.com/en-gb/article/24267729/prepare-for-the-reckoning-lord-of-hatred-draws-near). Una lista "verbatim" no puede llevar filas que no están en la fuente.

**Contradicción interna añadida:** §1 dice que el Brujo llega "al lanzamiento"; §3 lo lista como "Solo comprar. Instantáneo". Como el lanzamiento fue en abril, la conclusión práctica no cambia, pero las dos tablas se contradicen.

---

## B. Problema de MODELO que el informe no detectó (y su §10 debía haber cazado)

### B1. Icy Veins "Do You Need Lord of Hatred to Stay Competitive" es un artículo **pre-lanzamiento**

El informe lo usa como fuente en §2, §3 (las "+20 opciones transformadoras") y, sobre todo, como **columna vertebral de toda la tabla de contenido vetado del §9** — la sección que sostiene el consejo más caro del informe ("habla con la pareja hoy... decidid ya si compra").

Texto crudo del artículo (descargado hoy, 4.809 caracteres):

> *"**When** Diablo 4 **launches** its second expansion, Lord of Hatred, **on April 28, 2026**, it **will** not just add a new region and two classes."*
> *"So far, it is **unknown** exactly what those transformative choices are and **if they will impact builds**."*
> *"Base players **might be** locked out of what is Diablo 4's version of set items. This means missing out on a ton of builds, **most likely**."*
> *"However, so far we do **not have many details** about the new systems, so it is **hard to really judge if this will be an issue** or not."*
> *"There is also a ton of content that has **not been announced yet**."*

Es un artículo escrito **en futuro, antes del 28/04/2026**, cuatro meses antes del parche vivo. El informe lo cita sin fecha y **no lo incluyó** en su tabla de "marco muerto" del §10, donde sí cazó tres páginas de Maxroll y una de Icy Veins.

**Qué sobrevive y qué no:**

- **Sobrevive la LISTA de contenido de pago.** No por Icy Veins, sino porque Blizzard la publica en su propia tabla: *"War Plans, Horadric Cube, Talisman, and the Skovos Region require Lord of Hatred Purchase"*, frente a *"Major Skill Tree Updates, Loot Filter, Map Overlay, and increased Torment tiers... available across full game regardless of realm or expansion ownership"* — [Prepare for the Reckoning](https://news.blizzard.com/en-gb/article/24267729/prepare-for-the-reckoning-lord-of-hatred-draws-near). **Sustituir la fuente del §9 por ésta.**
- **NO sobrevive el tono de la advertencia.** *"Missing out on a ton of builds"* es una **especulación pre-lanzamiento explícitamente hedgeada por su propio autor**, y el informe la eleva a hecho en §9 y en el paso 8 del plan del §12. Debe ir marcada como conjetura de abril de 2026, o retirarse.
- **Ojo con un error del propio Icy Veins:** dice *"A new Torment difficulty tier"* (un nivel nuevo). Blizzard dice *"Torment levels expand from 4 to 12"* (ocho nuevos). El informe usó, correctamente, la cifra de Blizzard — pero es la prueba de que ese artículo no estaba mirando el juego final.

> **Cita que sí verifiqué y que el informe reproduce bien:** *"These features affect progression and build optimization, and it would simply not be fair to make them expansion-only."* Está literal en esa página. Mi primera pasada de lectura automática no la encontró; la lectura del HTML crudo sí. **No es una cita fabricada.**

---

## C. Atribuciones cruzadas (el dato es correcto, la URL no lo respalda)

| Dato del informe | Fuente que cita | Problema | Dónde está de verdad |
|---|---|---|---|
| "Skovos (región) y **Temis** (capital)" (§4.2) | Icy Veins LoH Overview, 24/04/2026 | La palabra **Temis no aparece** en esa página | Maxroll Talisman (28/06/2026): *"before boarding the ship towards Temis"*; Maxroll War Plans (05/08/2026): *"Tyrael in Temis, the main city of Skovos"* |
| "Planes de Guerra: la primera vez tras la campaña son **3**, en personaje nuevo **2**" (§4.3) | Maxroll primero, Icy Veins después | En el HTML de [Maxroll War Plans](https://maxroll.gg/d4/resources/war-plans): `three activities` = **0** apariciones, `two activities` = **0**. Solo dice *"a playlist of up to five activities"* | **Solo** Icy Veins War Plans Overview — página que el propio informe marca "⚠ sin fecha visible". El orden de citación invierte la fiabilidad |

---

## D. Omisiones materiales para un jugador que quiere min-maxear

Ninguna de estas es un error de hecho, pero las cuatro cambian decisiones.

### D1. Un Sello Legendario puede llegar a 6 huecos

La tabla de §4.3 (Mágico 3 / Raro 4 / Legendario 5 / Único Mítico 6) **es exacta** — la he verificado carácter a carácter en el HTML. Pero el informe corta la frase inmediatamente siguiente:

> *"Magic / Rare / Legendary Seals can roll an affix that unlocks an additional charm slot at the cost of a Seal bonus. **Legendary Seals are your bread-and-butter for most of the endgame**, with Mythic Unique Seals dropping only in the highest tiers of Torment difficulty."* — [Maxroll Talisman, 28/06/2026](https://maxroll.gg/d4/resources/talisman-charms-sets)

La propia página ilustra un **"6 Charm slot Legendary Seal"**. Presentar la tabla como techo por rareza, sin el afijo de hueco extra, hace que el jugador persiga Míticos cuando su objetivo realista es un Legendario bien roleado.

### D2. El tablero de Planes de Guerra es **por personaje** y no comparte experiencia

> *"Every alt has an individual War Plans board, and activity experience is not shared, so you must level one from scratch for every character you create."* — [Maxroll War Plans, 05/08/2026](https://maxroll.gg/d4/resources/war-plans)

Esto **matiza directamente** la promesa de §5.3 ("el personaje de la S15 arrancará con Planes de Guerra desde el minuto uno"). Se desbloquea el sistema, sí; el **árbol se sube desde cero otra vez**. El informe vende la parte buena y omite la mala.

### D3. Maxroll clasifica el Nigromante de Esbirros en **tier B**, no arriba

La primera línea del veredicto del informe dice que el personaje "es el correcto" con confianza **Alta**, y todo el plan del §12 se optimiza alrededor del set de esbirros. Eso es cierto en cuanto a *clase y nivel*. Pero el jugador ha pedido **min-max**, y el informe nunca abre la tier list:

[Maxroll — Necromancer Endgame Builds Tier List, act. 29/06/2026](https://maxroll.gg/d4/tierlists/necromancer-endgame-tier-list):

- **A:** Blood Wave Necro, Bone Spirit Necro
- **B:** **Minion Necro**, Golem Necro, Sever Necro, Blood Surge Necro
- **C:** Blight, AotD, Bone Spear, Blood Lance

⚠ Esa tier list es del **29/06/2026**, anterior a los parches 3.1.2 (28/07) y 3.1.3 (12/08). No afirmo que el ranking siga vigente. Afirmo que **el informe debía haberlo mirado y declarado**, porque el jugador podría querer reencauzar el Paragón antes de invertir toda la campaña en un set de esbirros.

### D4. Bug de agrupación entre **dos** poseedores de la expansión

El informe lista en sus Fuentes el hilo [us.forums.blizzard.com/.../251798](https://us.forums.blizzard.com/en/d4/t/cant-play-with-friend-in-new-expansion-lord-of-hatred/251798) pero **no lo usa en el cuerpo**. Su contenido es directamente relevante para un jugador en dúo (09/05/2026):

> *"we've played for a long time and now with expansion (yes we have the same version purchased) and both seasonal sorcerer and cannot play together anymore."*

Es decir: hay un fallo de agrupación reportado **incluso teniendo ambos la expansión**. Sin respuesta azul. Debería estar en la tabla de riesgos del §11, junto al bug de licencia del foro EU.

---

## E. Calibración de confianza demasiado alta

### E1. "Solo se ofrece en la pantalla de creación de personaje" (§5.2, condición 1)

El informe da la regla completa de dos condiciones con confianza **Alta** en la tabla del §0. La **condición 2** está sólidamente citada: *"To skip the story in future seasons, you must complete the Lord of Hatred campaign at least once"* — verificada literal en [Icy Veins LoH Overview, act. 24/04/2026](https://www.icy-veins.com/d4/guides/lord-of-hatred-overview/).

La **condición 1** no la respalda ninguna fuente preferente con fecha de parche vivo: sale de **tres hilos de foro sin respuesta azul**. Y circula material contrario — de baja calidad y de la era del juego base de 2023, incluyendo un dominio vetado — que afirma que el salto puede aplicarse retroactivamente a personajes existentes. **No lo doy por bueno ni lo uso para refutar**, pero su existencia significa que la confianza correcta es **Media**, no Alta, y que la verificación en cliente que el informe propone para Kurast debería extenderse aquí: mirar la pantalla de selección de personaje antes de dar por perdida la tarde.

Esto no cambia el plan (jugar las campañas con el de 70 sigue siendo lo correcto y lo más rápido), pero sí el nivel de certeza con que se enuncia.

### E2. "No encontrado #10" es demasiado absoluto

El informe dice de la fecha de fin de la S14: *"no lo he visto escrito en ninguna fuente abierta"*. **Sí está escrito** en varias fuentes no preferentes (blizzardwatch, allthings.how, seasondex, seasontimer), todas apuntando al **15 de septiembre de 2026** y todas declarando que **el origen es el temporizador dentro del juego, no un anuncio de Blizzard**. La forma correcta del hueco es: *"sin confirmación oficial de Blizzard; los rastreadores leen 15/09/2026 del contador in-game"*. La estimación del jugador queda corroborada, con la reserva puesta donde toca.

---

## F. Lo que he intentado tumbar y **resiste**

Verificado carácter a carácter contra la fuente citada:

| Afirmación | Estado | Prueba |
|---|---|---|
| LoH incluye VoH | **Confirmado literal** | *"Diablo IV: Lord of Hatred includes our first expansion, Vessel of Hatred"* (Blizzard 24247511) |
| Nivel máximo 70 | **Confirmado, doble fuente** | *"The Level Cap increases to 70 for all Diablo IV players"* (Blizzard 24267729) + *"Level cap raised from 60 to 70."* (Icy Veins, 24/04/2026) |
| Tormento de 4 a 12 | **Confirmado literal** | *"Torment levels expand from 4 to 12"* (Blizzard 24267729) |
| Lanzamiento 28/04/2026 | **Confirmado** | Blizzard 24247511. *(No he encontrado respaldo para el matiz "27 en América" que el prompt arrastraba; el informe hace bien en no repetirlo en el cuerpo.)* |
| Desbloqueos "after next login" | **Confirmado literal** | *"After purchase, instantly available items will be delivered in-game after next login."* (página oficial LoH, nota al pie ¹) |
| Talismán se desbloquea antes del barco a Temis, a nivel de cuenta | **Confirmado literal** | *"The Talisman is unlocked early on during the Lord of Hatred Campaign before boarding the ship towards Temis. This unlocks it for your other characters as well."* (Maxroll, 28/06/2026) |
| Huecos por rareza de Sello 3/4/5/6 | **Confirmado literal** (con la salvedad D1) | Tabla `Rarity \| Charm Slots`: Magic 3, Rare 4, Legendary 5, Mythic Unique 6 |
| 5 conjuntos de Talismán de Nigromante, con esos nombres | **Confirmado en el fichero** | `Talisman_Necro_01`–`05` = Radament's Desecration (id 2296936), Art of the Bone Weaver (2297192), Word of the Blood Binder (2297194), **Peace of the Black Shroud (2297196)**, Rathma's Waking Touch (2297198) |
| Bonos de conjunto en 2 / 3 / 5 | **Confirmado en el fichero y en la web** | `"required": 2 / 3 / 5` en los cinco sets; y en Maxroll: *"if we were to equip two Charms... even better bonuses with 3 and 5 Charms"* |
| Black Shroud recomendado para esbirros | **Confirmado literal** | *"The Black Shroud set pairs perfectly with this build as all the skills are also Darkness skills."* (Maxroll Minion Necro, 22/07/2026). ⚠ La guía dice **"The Black Shroud set"**; el nombre completo *"Peace of the Black Shroud"* sale del datamining. El informe los fusiona sin decirlo — es correcto, pero conviene declararlo |
| Mercenario Subo o Aldkin para esbirros | **Confirmado literal** | *"Subo provides his map hack and a small amount of damage increase while Aldkin provides a boost to your damage reduction."* (Maxroll, 22/07/2026) |
| Mercenarios se desbloquean en la campaña de VoH | **Confirmado literal, fuente de parche vivo** | *"Mercenaries are unlocked during the Vessel of Hatred campaign and assist you in battle."* (Maxroll Minion Necro, 22/07/2026) |
| Son 4 mercenarios y se llaman así | **Confirmado en el fichero** | Ver A5 para la corrección del "6 habilidades" |
| Build de esbirros apuntado a nivel 70 / Tormento 1 | **Confirmado literal** | *"This build guide assumes you have a Level 70 Character and unlocked Torment 1."* |
| Cubo Horádrico tras la campaña de LoH, en Temis | **Confirmado literal** | *"The Horadric Cube becomes available by playing through the Lord of Hatred campaign and is located in Temis afterwards."* (Maxroll, 16/07/2026) |
| Planes de Guerra: Tyrael en Temis tras la campaña | **Confirmado literal** | *"Once you complete the Lord of Hatred Campaign, you can start a War Plan by visiting Tyrael in Temis, the main city of Skovos."* (Maxroll, 05/08/2026) |
| Planes de Guerra: rangos 0–10, puertas T1 / Rango de Temporada 2 / T6+ | **Confirmado** | *"Rank 0/10"*; *"you must be in Torment 1 difficulty or higher"*; *"complete Season Rank 2 by clearing the Hellish Descent capstone dungeon"*; *"Greater Lair Boss activity nodes require Torment 6+"* |
| Planes de Guerra: 7 actividades elegibles | **Confirmado doblemente** | Web: *"Tree of Whispers, Nightmare Dungeons, Helltides, The Undercity, Lair Bosses, Infernal Hordes, and The Pit"*. Fichero: `warPlans` es una lista de **7** entradas con esos mismos nombres |
| Conflicto Kurast (Maxroll vs Icy Veins) | **Confirmado que el conflicto es real** | Maxroll (16/07/2026): *"you must progress the Vessel of Hatred campaign until you get a priority quest"*. Icy Veins: tres requisitos — *"Purchase the Vessel of Hatred Expansion"*, *"Reach Level 20"*, *"Invoke the Spirit Flame"* — sin campaña. **El informe declara el conflicto en lugar de resolverlo a ojo: es lo correcto** |
| Ciudad Subterránea: 100 segundos, Sintonía nivel 1 | **Confirmado literal** | *"You have 100 seconds on the three floors to gather Attunement"* + *"at least Level 1 Attunement before entering the boss room"* (Icy Veins) |
| Recompensas del cofre de Planes de Guerra | **Confirmado literal** | *"Uniques, Set Charms, Unique Charms, Ancestral Gear, Runewords, Gold And Materials, And More!"* (Icy Veins) |
| "+80 opciones por clase" y "+20 transformadoras" | **Citas literales correctas** | Están textuales en Icy Veins — pero ver B1: son de un artículo pre-lanzamiento |
| Parche 3.1.3 del 12/08/2026 | **Confirmado** | Coherente con Icy Veins y Maxroll; **ningún cambio de "saltar campaña" en 3.1.3** |
| mobalytics.gg devuelve 403 | **Confirmado hoy** | `HTTP 403 Forbidden` al agente. La queja del informe es real |

### F1. Higiene de fuentes: limpia

He revisado la lista completa de fuentes del informe contra la lista de vetados (fextralife, primagames, beebom, gamespot, segmentnext, studioloot, gamerguides, pcgamesn, mythicdrop). **Ningún número del informe se apoya en un dominio vetado.** El informe usa exclusivamente Blizzard oficial, foros oficiales de Blizzard, Maxroll, Icy Veins y datamining. En esto cumple.

*(Los dominios vetados aparecieron en mis búsquedas de control — primagames en la de "skip campaign" — y por eso mismo no he usado ese material para refutar nada.)*

---

## G. Qué hay que cambiar en el informe original

**Retirar (cita inexistente):**
1. §5.3 — la frase de los waypoints al saltar campaña. Todo el párrafo pierde su base.
2. §4.3 — el "máximo 3 Amuletos Únicos". A "No encontrado".
3. §7 — *"It picks up the story after the events of Vessel of Hatred"*. Sustituible por la frase oficial real: *"uncovering the events that set Mephisto's dark ambitions into motion"*.

**Corregir:**
4. §10 y Fuentes — cabecera real del `data.min.json`: `last-modified: Fri, 14 Aug 2026 15:49:39 GMT`, 11.606.292 bytes. La tesis del desfase 3.1.0 vs 3.1.3 se mantiene.
5. §4.1 — Aldkin lista 14 entradas, no 6. Añadir la clave `MercenaryClass_BountyHunter` para Subo.
6. §1 y §3 — añadir **Spiritborn** (llega con VoH, incluido en la compra). Quitar la fila "Warlock" de la tabla declarada verbatim o cambiar su fuente al artículo 24267729. Resolver la contradicción §1 vs §3.
7. §4.2 — quitar Icy Veins como fuente de "Temis"; usar Maxroll Talisman o Maxroll War Plans.
8. §4.3 — el "3 / 2 actividades" es de Icy Veins, no de Maxroll. Reordenar y heredar el ⚠ de "sin fecha".
9. §0 — bajar a **Media** la confianza de "no se puede saltar", separando la condición documentada (campaña completada) de la que solo sostienen foros (solo en creación de personaje).
10. "No encontrado #10" — reformular: existe la fecha 15/09/2026 en rastreadores, leída del contador in-game, sin confirmación oficial.

**Añadir:**
11. §4.3 — el afijo de hueco extra: un Sello Legendario puede llegar a 6 huecos, y son *"your bread-and-butter for most of the endgame"*.
12. §5.3 — el tablero de Planes de Guerra es por personaje y no comparte experiencia.
13. §0 o §5.1 — la tier list de Maxroll (29/06/2026) sitúa Minion Necro en **B**, con Blood Wave y Bone Spirit en **A**. Con su fecha y su advertencia de que es anterior a 3.1.2/3.1.3.
14. §11 — el bug de agrupación entre dos poseedores de la expansión (hilo 251798), que ya estaba en las fuentes sin usar.
15. §9 — cambiar la fuente de la tabla de contenido de pago de Icy Veins a la tabla oficial de Blizzard, y marcar *"a ton of builds"* como especulación pre-lanzamiento.

**Lo que NO hay que tocar:** el plan operativo del §6 y del §12. Las tres refutaciones duras afectan a la *justificación* de dos pasos, no a su orden. La secuencia VoH → Kurast → Raheir/Cubil → Talismán temprano en LoH → terminar LoH → Foso 10 → Planes de Guerra sigue siendo la correcta con las fuentes verificadas.

---

## Páginas abiertas para esta refutación

**Blizzard oficial**
- https://news.blizzard.com/en-us/article/24247511/stand-against-mephisto-pre-purchase-lord-of-hatred
- https://news.blizzard.com/en-gb/article/24267729/prepare-for-the-reckoning-lord-of-hatred-draws-near
- https://diablo4.blizzard.com/en-us/lord-of-hatred *(HTML crudo, 17.798 bytes)*

**Foros oficiales**
- https://us.forums.blizzard.com/en/d4/t/cant-play-with-friend-in-new-expansion-lord-of-hatred/251798
- https://us.forums.blizzard.com/en/d4/t/do-both-players-accounts-need-to-have-purchased-the-dlc-to-play-co-op-dlc-content/192584

**Maxroll**
- https://maxroll.gg/d4/resources/talisman-charms-sets — 28/06/2026 *(HTML crudo, 43.529 bytes)*
- https://maxroll.gg/d4/resources/war-plans — 05/08/2026 *(HTML crudo, 54.448 bytes)*
- https://maxroll.gg/d4/build-guides/minion-necromancer-guide — 22/07/2026
- https://maxroll.gg/d4/resources/kurast-undercity — 16/07/2026
- https://maxroll.gg/d4/resources/horadric-cube — 16/07/2026
- https://maxroll.gg/d4/meta/alt-leveling-guide — 30/06/2026 *(HTML crudo, 318.741 bytes)*
- https://maxroll.gg/d4/tierlists/necromancer-endgame-tier-list — 29/06/2026

**Icy Veins**
- https://www.icy-veins.com/d4/guides/lord-of-hatred-overview/ — 24/04/2026
- https://www.icy-veins.com/d4/news/do-you-need-lord-of-hatred-to-stay-competitive-in-diablo-4/ *(HTML crudo, 22.740 bytes — pre-lanzamiento)*
- https://www.icy-veins.com/d4/guides/kurast-undercity-guide/
- https://www.icy-veins.com/d4/guides/war-plans-overview/

**Bloqueado**
- https://mobalytics.gg/diablo-4/guides/patch-3-1-3-changes-and-fixes — **HTTP 403**

**Datamining (declarado como tal)**
- https://assets-ng.maxroll.gg/d4-tools/game/data.min.json — descargado íntegro y consultado con Python. `version: 3.1.0.72698`, `last-modified: Fri, 14 Aug 2026 15:49:39 GMT`, 11.606.292 bytes. Claves inspeccionadas: `mercenaries` (4), `itemSets` (45), `warPlans` (7), `classes` (8)
