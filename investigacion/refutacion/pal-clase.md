# REFUTACIÓN ADVERSARIAL — `investigacion/crudo/pal-clase.md`

**Documento auditado:** `/Users/alvhor/Proyectos/DIAVLO IV/investigacion/crudo/pal-clase.md`
**Fecha de la auditoría:** 24 de agosto de 2026
**Parche vivo de referencia:** Diablo IV **3.1.3, build 73224, 12/08/2026** — confirmado abriendo la página oficial de notas de parche (https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes), cuya primera entrada es literalmente «3.1.3 Build #73224 (All Platforms)—August 12, 2026».
**Veredicto:** **PARCIAL**

---

## 0. Cómo se ha auditado

No me he fiado de ninguna afirmación del informe. He **rehecho** el trabajo:

1. **He vuelto a descargar el fichero de datos** `https://assets-ng.maxroll.gg/d4-tools/game/data.min.json`: HTTP 200, **11 606 292 bytes**, campo `version` = **`3.1.0.72698`**. Byte a byte, el mismo fichero que dice el informe. Y he reejecutado sus consultas: árbol, nodos, costes, enfriamientos, textos de Juramento, tablas de escalado.
2. **He descargado por `curl` las páginas web citadas** y he buscado las citas literales dentro del HTML, no en un resumen. **Maxroll no devolvió 403 en ninguna petición** (coincide con lo que dice el informe).
3. He buscado en la web para intentar **contradecir** cada cifra con una fuente independiente.

**Páginas abiertas (16):** notas oficiales de parche · maxroll `paladin-class-overview` · maxroll `getting-started/skill-trees` · maxroll `shield-charge-paladin-guide` · maxroll `shield-charge-paladin-leveling-guide` · maxroll `tierlists/paladin-endgame-tier-list` · maxroll `resources/season-journey` · maxroll `news/diablo-4-3-1-0-patch-notes` · icy-veins `paladin-skills` · icy-veins `paladin-leveling-guide` · icy-veins `paladin-oaths-breakdown` · diablo4.blizzard.com en-us y es-es · news.blizzard `wield-divine-might-as-the-paladin` · d4guides.gg `classes/paladin` · wowhead `skill/shield-charge-2466077`. Más el `data.min.json`.
**Búsquedas: 8.**

---

## 1. RESUMEN DEL VEREDICTO

| Bloque del informe | Resultado |
|---|---|
| §3 Recurso Fe, §4 Juramentos, §5 palabras clave, §6 atributos | **Confirmado** (reproducido en el fichero de datos y en cita literal) |
| §7 clústeres y niveles, §8.1 escalera de puertas, §10 árbol completo | **Confirmado nodo a nodo.** Es la parte más sólida del documento |
| §11 los 83 puntos | **Confirmado**, pero **la fuente que da era mala**; hay una mejor y la aporto |
| §9 tablas de las 24 habilidades | **PARCIALMENTE REFUTADO.** Dos enfriamientos son valores muertos, uno de ellos el de **Shield Charge**, que es la build del jugador |
| §12.3 lista de tiers, §14 trampas de datos muertos | **Confirmado literalmente** |
| §18 «No encontrado» | **Dos huecos eran innecesarios** y **uno se apoya en un artefacto del buscador** |
| Citas entrecomilladas | **Una es inventada** y **una está mal atribuida** |

**Nada del informe procede de una fuente vetada.** He revisado los 20 enlaces de su §17: todos son blizzard.com, maxroll.gg, icy-veins.com, d4guides.gg, wowhead.com o news.xbox.com. Ninguna cifra se apoya en fextralife, primagames, beebom, gamespot, segmentnext, studioloot, gamerguides, pcgamesn ni mythicdrop.

**Nada del informe es PTR presentado como parche vivo.** Al contrario: el informe avisa del PTR 3.2 en su §0.4 y he verificado ese aviso (el foro incrustado en Maxroll trae el hilo «PTR 3.2 Known Issues - 8/4/2026», `created_at` 2026-08-04).

---

## 2. ERRORES DUROS — cifras refutadas

### 2.1 🔴 **Shield Charge: el enfriamiento NO es 10 s. Es 8 s.** (§9.4, §1, §15)

Este es el error caro, porque es **exactamente la habilidad sobre la que el jugador va a montar su personaje**.

Tres fuentes independientes lo contradicen:

| Fuente | Qué dice |
|---|---|
| **Notas oficiales 3.1.0** (https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) | *"Shield Charge — Base damage increased from 90% to 180%. **Cooldown reduced from 10 to 8 seconds.** Movement Speed while Charging changed from 100% Cap 1 speed to 50% Cap 1 and 50% Cap 2 speed. **Base armor granted while charging increased from 40% to 60%.**"* |
| **Maxroll, artículo de notas 3.1.0** (https://maxroll.gg/d4/news/diablo-4-3-1-0-patch-notes) | *"Base damage increased from 90% to 180%. Cooldown reduced from 10 to 8 seconds."* |
| **El propio `data.min.json` que usa el informe** | `skills["Paladin_ShieldCharge_Channel_Short"].cooldown = "Mod(2686060809)?0:8"` y armadura `0.6*Table(37,sLevel)*100`, daño `1.8*Table(34,sLevel)` |

El informe tomó el 10 s de Icy Veins (§9.4: *«Enfriamientos y cargas: icy-veins.com/d4/guides/paladin-skills/»*) y **no lo contrastó con el fichero de datos que tenía delante**, que es justo donde las dos fuentes divergen. Icy Veins sigue publicando la ficha vieja: *"Cooldown | 10 seconds"* y *"granting **40% Damage Reduction** and dealing 36% damage while Channeling"*.

**Doble error dentro del mismo error:** Icy Veins dice «40 % Damage Reduction»; el juego dice **Armadura**, y **60 %**, no 40. El informe acertó al escribir «+armadura» en vez de «reducción de daño», pero se quedó sin el número y con el enfriamiento viejo.

> **Valor vivo:** Shield Charge = **enfriamiento 8 s**, **+60 % de armadura** mientras canalizas, daño base 180 %, probabilidad de golpe de suerte 35 %.

### 2.2 🔴 **Heaven's Fury: el enfriamiento NO es 30 s. Es 15 s.** (§9.6)

Mismas tres fuentes. Notas oficiales 3.1.0, sección Expansion → Balance Updates → Paladin → Skills: *"**Heaven's Fury — Cooldown reduced from 30 to 15 seconds.**"* Corroborado por el artículo de Maxroll sobre 3.1.0. Y en el fichero: `skills["Paladin_HeavensFury"].cooldown = "15+(Mod(2686060811)?10:0)"`.

Icy Veins sigue diciendo *"Cooldown | 30 seconds"*. El informe copió el 30.

Esto **cambia una conclusión del informe**: en §12.2 escribe *«Vive de los enfriamientos… Fortress: 60 s. Arbiter of Justice: 120 s»* y en §1 vende la clase como «muy dependiente de enfriamientos». Con Heaven's Fury a 15 s y Shield Charge a 8 s, la clase es bastante menos «botón en enfriamiento» de lo que pinta.

### 2.3 🟠 **Shield Charge no cuesta Fe en su forma base** (§9.4)

El informe escribe, en la tabla de Valor: *«Shield Charge … Coste: **Fe + 1 por segundo**»*.

En el fichero: `cost = [{"type": 9, "cost": "Mod(2686060809)?20:0", "channellingCost": 1}]`. El mod `2686060809` es **Relentless Charge**. Es decir: **la habilidad base no cuesta Fe y va por enfriamiento**; los 20 de Fe + 1/s **solo aparecen si eliges la variante Relentless Charge**, que es precisamente lo que el propio informe cita bien tres párrafos más abajo en §10.4 (*"Shield Charge becomes a Core Skill… now costs 20 Faith to Cast and an additional 1 Faith per second"*). El descriptor del juego lo dice de forma explícita: `{if:Mod(2686060809)}Faith Cost…{else}Cooldown…{/if}`.

Presentar el coste de la variante como coste de la habilidad base es engañoso para un principiante que va a leer la tabla y no el anexo.

### 2.4 🟠 **Falling Star: 26 % de golpe de suerte no cuadra con el fichero (24 %)** (§9.4)

Icy Veins: *"Lucky Hit Chance | 26%"*. Fichero: `skills["Paladin_LanceDive_OLD"].combatEffectChance = 24`. El informe eligió el 26 sin declarar el conflicto. Todos los demás valores de golpe de suerte del informe (50/44/20/14, 30/24/16/6/3, 35/33/26/12) sí coinciden con el fichero.

### 2.5 🟠 **Rally: mezcla de fuentes sin declarar el conflicto** (§9.4)

| Dato | Informe | Fichero de datos | Icy Veins | d4guides.gg |
|---|---|---|---|---|
| Velocidad de movimiento | **+15 %** | `15%[+]` ✅ | *"20% Movement Speed for 8 seconds"* | *"15%[+] Movement Speed for 6 seconds"* |
| Fe generada | **15 + rango** | `15+sLevel` ✅ | *"generate 22 Faith"* | — |
| Cargas | **3** | `Charges: [3+(Mod…?1:0)]` ✅ | *"Charges | 3"* ✅ | — |
| Enfriamiento | **16 s** | campo `cooldown` = `Mod(...)?0:0.5` — **no verificable** | *"Cooldown | 16 seconds"* | — |
| Coste de vida | **35 %** | `(Mod(2686060763)?0.2975:0.35)*100` ✅ | no lo menciona | — |

El informe acertó en 4 de 5 tirando del fichero, pero se trajo el **16 s** de la única fuente que en esa misma ficha se equivoca en otras dos casillas. El 16 s **puede ser correcto** (es un enfriamiento de carga, no el campo `cooldown`), pero **no está verificado** y el informe lo presenta como si lo estuviera.

---

## 3. ERROR DE MÉTODO — la fuente principal escrita está **fuera del parche**

Esta es la falla sistémica, y contradice una regla dura del encargo («solo páginas fechadas **dentro** del parche 3.1.x»).

- **Patch 3.1.0 salió el 30 de junio de 2026** (notas oficiales: «3.1.0 Build #72592 (All Platforms)—June 30, 2026»).
- **Icy Veins `paladin-skills` se actualizó el 29 de junio de 2026** (changelog literal en la página: *"June 29th 2026: Guide updated for Season 14"*). **Un día ANTES del parche.**
- Lo mismo con `paladin-leveling-guide`: *"June 29th 2026: Guide updated for Season 14"*.

O sea: la página que el informe usa como su gran fuente redactada para **costes, enfriamientos y golpes de suerte de las 24 habilidades** es **pre-3.1.0**, y lo demuestra su propio contenido (Shield Charge 10 s / 40 % DR, Heaven's Fury 30 s, Disciple 50 %).

El informe **detectó un síntoma** —marca el «50 %» de Disciple como caducado en §4.2— pero **diagnosticó mal la causa**: escribió *«La página está actualizada al 29/06/2026 pero ese dato concreto se les quedó atrás»*. No es «ese dato concreto». Es la **fecha de la página**: está publicada antes del parche, y por eso arrastra varios valores viejos a la vez.

**Consecuencia:** todo número de §9 cuya única fuente sea Icy Veins hay que degradarlo a «pendiente de comprobar en pantalla». Los que coinciden con el fichero de datos (que es build 72698, **posterior** al 72592 de 3.1.0) sí están vivos.

---

## 4. CITAS QUE NO SON CITAS

### 4.1 🔴 Cita literal inventada (§5)

El informe escribe:

> «Maxroll dice de ella que *"Hit Count As Blocking triggers Retribution, which works as the primary damage mechanic"*»

**Esa frase no existe en la página.** He descargado https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide (HTTP 200, 477 063 bytes) y buscado la cadena: 0 coincidencias. Lo que la página dice, literal:

> *"Shield Charge is your main source of damage with Retribution. Make sure you maximize the amount of enemies you hit with it by positioning accordingly to trigger Hit Count As Blocking as often as possible."*

Es una paráfrasis puesta entre comillas. Y la conclusión que el informe saca de ella —*«tu daño principal saldría de bloquear, no de pegar»*— **fuerza la fuente**: Maxroll dice que la fuente principal de daño es **Shield Charge**, y que «Hit Count As Blocking» es algo que conviene disparar a menudo. Lo que sí está verbatim y sí sostiene la idea del arquetipo es la introducción: *"This build is using Shield Charge to deal Physical Thorns damage to your enemies through direct hits and Retribution pulsing around you everytime you block."*

### 4.2 🟠 Cita bien copiada, mal atribuida (§3.3)

El informe atribuye a `icy-veins.com/d4/guides/paladin-skills/` la frase *"Faith is used for casting many skills but there are some nodes in the tree that will shift that resource over to Life instead"*. Esa cadena **no aparece** en esa página (0 coincidencias en 237 032 bytes). Está en **`icy-veins.com/d4/guides/paladin-leveling-guide/`**, donde sí la he encontrado íntegra. La cita es real; el enlace es el equivocado.

### 4.3 🟠 Escalera de parches mal fechada (§4.2, «trampa» nº 1)

El informe dice: *«Las propias notas de parche muestran la escalera: "increased from 17% to 21%" (parche 3.0/expansión) y luego "increased from 21% to 25%" (3.1.0)»*.

**Las dos líneas están dentro de la MISMA nota de 3.1.0.** En la página oficial:
- `Expansion → Balance Updates → Paladin → Oaths` → *"Zealot Oath — Damage per echo increased from 17% to 21%."*
- `Updates from PTR → Balance Updates → Paladin → Oaths` → *"Zealot Oath — Damage per echo increased from 21% to 25%."*

**El valor vivo (25 %) es correcto** —lo confirma el fichero de datos, `0.25*(1+…)*100`—, pero la procedencia que cuenta el informe no es la que dice la fuente. El 17 % es el valor del artículo de presentación (https://news.blizzard.com/en-us/article/24244399/wield-divine-might-as-the-paladin, verificado literal: *"echoes the attack for an additional 17% of the damage"*), no una línea de notas de 3.0.

---

## 5. UN «NO ENCONTRADO» QUE SE APOYA EN UN ARTEFACTO DEL BUSCADOR

**§18.11** dice: *«El parche 3.1.3 incluye correcciones a habilidades del Paladín (descripciones aditivo/multiplicativo, daño de eco del Juramento Zealot, Brandish y Vulnerable, tipo de daño de Phalanx Charge, entre otras) según extractos de buscador de Mobalytics que no pude abrir (HTTP 403)»*.

**Refutado.** Esas correcciones están, palabra por palabra, en la nota de **3.1.0**, no en 3.1.3. Sección `Expansion → Bug Fixes → Paladin` de 3.1.0:

> *"Fixed multiple instances where Paladin skills had incorrect descriptions for denoting whether a damage modifier was additive or multiplicative."*
> *"Fixed an issue where the Zealot Oath echo damage was not dealing the correct values across base skill and all variants."*
> *"Fixed an issue where Brandish could apply Vulnerable without the proper upgrade."*
> *"Fixed an issue where Shield Charge's Phalanx Charge Variant dealt the incorrect damage type."*

He recorrido la página entera: **el Paladín aparece exactamente una vez entre 3.1.1, 3.1.2 y 3.1.3**, y es un fallo cosmético:

| Parche | Build | Fecha | Paladín |
|---|---|---|---|
| **3.1.3** | 73224 | 12/08/2026 | **Nada.** Solo Druida, Nigromante y Brujo (arreglos visuales del Corrupted Reaper) |
| **3.1.2** | 73020 | 28/07/2026 | **Nada** |
| **3.1.1** | 72836 | 14/07/2026 | *"Fixed issue where Damage with Holy was not showing in Stats and Materials tab."* |

Yo también recibí ese artefacto: al buscar «patch 3.1.1 3.1.2 3.1.3 Paladin balance changes», el buscador me devolvió **la misma lista de arreglos de 3.1.0** etiquetada como si fuese de agosto. Es un error de indexación, no un cambio del juego.

**Lo que esto significa para el informe:** su §18.11 era **más pesimista de lo necesario**. Entre el fichero de datos (build 72698) y el parche vivo (73224) **no hay ningún cambio de equilibrio del Paladín**. Los números de §4, §9 y §10 que coinciden con el fichero se pueden dar por vivos con confianza alta, no media.

---

## 6. ERRORES MENORES Y COSAS QUE EL INFORME NO DECLARÓ

| # | Punto | Qué encontré |
|---|---|---|
| 1 | §11: descarta maxroll `skill-trees` por *«fechada dos días ANTES del rework»* | Su changelog dice literalmente **«April 26, 2026 — Updated for Lord of Hatred launch»**. Está *actualizada para* el lanzamiento, no *anterior a* él. El conflicto es real (esa página dice *"one skill point each time you level up… all the way to level 69"* + *"12 additional skill points through the Season Rank system"* = **80**), pero el motivo del descarte que da el informe es falso |
| 2 | §11: los **14 puntos** de Rango de Temporada se citan a guías de **Nigromante** | Hay una fuente preferente, del Paladín-agnóstico y **dentro del parche**: **https://maxroll.gg/d4/resources/season-journey** (Rango de Temporada, act. **13/07/2026**): *"Some objectives of the Season Rank rewards Skill Points, with these objectives being found in Ranks 1 through 5, **netting you a total of 14 Skill Points**."* Y el fichero da los 69: tooltip del atributo `Level` — *"Each Level grants a Skill Point until Level 70."* **69 + 14 = 83 se sostiene**, ahora bien citado |
| 3 | §8: *«maximizar UNA habilidad entera = 30 puntos»* | **No es universal**, y las propias tablas §10 del informe lo desmienten. Cinco habilidades llevan modificadores de 5 rangos: **Clash** y **Advance** = 15+5+5+5+5+3 = **38**; **Holy Bolt**, **Shield Bash** y **Divine Lance** = 15+20+5 = **40**. Los 30 valen para las otras 19 (Shield Charge entre ellas, así que la conclusión práctica para el jugador aguanta) |
| 4 | §5: *«Judgement … marcas de 20 s»* | El propio fichero define el keyword así: `Keyword_Judgement` → *"Judgement marks an enemy for **3 seconds**, dealing 80% damage after it expires."* Los buffs de 20 s existen dentro de `Paladin_Sub_Judgement`, pero **no son la duración de la marca**. El `maxStackCount: 15` sí es correcto |
| 5 | §5: Resolve presentado como mecánica atada al Paladín/Juggernaut | El indicador de personaje «Maximum Resolve» tiene `classFilter` en **true para las ocho clases**, y las notas 3.1.0 traen *"Fixed an issue where Concussive Stomp would not grant Resolve"* — para **Spiritborn**. La cita de Maxroll (*"Thematically tied to Juggernaut skills"*) está bien copiada, pero Resolve **no es exclusivo del Paladín** |
| 6 | §8.2: escala de rangos ×1,40 a rango 15 | **Correcto según el fichero** (`powerTables[37]`: r5 = 1,16 · r10 = 1,30 · r15 = 1,40 · r21 = 1,50 · se estanca en 1,60). Pero el informe **no declara que choca frontalmente** con la página de Maxroll que sí usa para otras cosas: *"each extra skill point makes a skill 10% more powerful… a skill with 5/15 points will be 40% stronger than 1/15 points"*. Es un conflicto abierto entre fuentes y debería estar dicho |
| 7 | §6: *«existen los objetos `1HFlail_Unique_Paladin_001` a `004`»* | En el fichero solo existen **`_003` y `_004`**. El `001` y el `002` no están. El tipo de objeto `Flail` sí existe y la afirmación de fondo (arma exclusiva) es correcta |
| 8 | §7.3: talentos huérfanos | El informe nombra 4 (`KeyPassive_1..4`) y dice que *«muchas llevan marcas [WIP] o (PH)»*. En realidad hay **~45 talentos huérfanos del Paladín**, y solo ~12 llevan esas marcas; los cuatro `KeyPassive` que cita **no llevan ninguna**. Ahora bien, **la conclusión es correcta y además generaliza**: he contado los nodos de las 8 clases y **ningún árbol de clase tiene un solo nodo de pasiva** (Bárbaro 24+168+78=270, Brujo 270, Nigromante 23+161+75=259, Hechicera 25+176+81=282…), y **todas** las clases arrastran entre 74 y 177 pasivas huérfanas en el fichero. No es una rareza del Paladín |
| 9 | §16: *«renacido a través de los Guardianes de la Luz»* | El texto oficial en español dice *«los paladines renacen a través de los **Guardianes de la luz**»* (minúscula) — https://diablo4.blizzard.com/es-es/lord-of-hatred. Irrelevante para el juego, pero es una cita |

---

## 7. HUECOS DE §18 QUE NO HACÍA FALTA DEJAR ABIERTOS

### 7.1 «Qué es Wing Strikes» (§18.8) — **cerrable con una fuente que el propio informe ya cita**

El informe dice: *«no he encontrado una definición redactada. Mi lectura —no confirmada— es que son los ataques que haces mientras estás en forma Arbiter»*.

Su lectura es correcta y **está por escrito en la fuente nº 5 de su propia lista**, https://news.blizzard.com/en-us/article/24244399/wield-divine-might-as-the-paladin:

> *"Arbiter Form grants increased movement speed, evade is replaced with Angelic Leap, and **wings strike around you dealing damage to nearby enemies**."*

Además: las notas 3.1.0 lo tratan como habilidad con número propio (`Paladin → Skills → Wing Strikes — "Base damage increased from 160% to 200%"`), y Maxroll tiene guía de temporada 14 dedicada (https://maxroll.gg/d4/build-guides/wing-strikes-paladin-guide). No era un hueco.

### 7.2 «El valor máximo de Fe» (§18.2) — matiz

El informe dice que *«ni el datamining lo expone como número plano»*. Cierto para el valor **base**, pero la cadena «Maximum Faith» **sí aparece** en el fichero, en un talento huérfano: `Paladin_Talent_Core_1` «Piety» → *"Your Maximum Faith is increased by [5*sLevel]"*. No da el máximo base, pero decir que el fichero no lo menciona es inexacto.

### 7.3 «¿Se puede cambiar de Juramento?» (§4.3, §18.3) — sigue abierto, pero hay indicio

No he encontrado fuente preferente y fechada dentro de 3.1.x que lo afirme. El artículo de Icy Veins sobre los Juramentos (https://www.icy-veins.com/d4/news/diablo-4-paladin-oaths-breakdown-of-the-new-class-mechanic/) es de diciembre de 2025 y solo dice que *"The Paladin can adjust Oath based on the situation"*, sin coste ni nivel. Hay además un hilo de soporte oficial —«Bug report: Armory does not store/change Paladin Oath or runewords», eu.forums.blizzard.com— cuyo mero enunciado implica que el Juramento **se cambia** (lo que no hace es guardarse en la Armería). **Sigue siendo «compruébalo en pantalla»**: la cautela del informe está justificada.

---

## 8. LO QUE NO HE PODIDO REFUTAR — verificado y firme

He intentado tumbar esto y no he podido. Todo reproducido por mí en el fichero de datos y/o en cita literal:

**Recurso y atributos (§3, §6)**
- `classes["6"] = {nameMale: "Paladin", primaryResource: {type: 9}, damageAttribute: 0, damageScalar: 1.25, resourceAttribute: 2, critAttribute: 1, tree: "Paladin_NEW"}` y `uiStrings.resourceType["9"] = "Faith"`. **Fe es el tipo 9 y es del Paladín.** Los indicadores «Faith Regeneration» y «Faith On Kill» tienen `classFilter` en true **solo en la posición 6** ✅
- Fuerza 12,5 %/100 y +200 armadura, Inteligencia 0,25 % crítico y +40 resistencias, Voluntad 0,5 % generación y 3,5 % curación, Destreza 0,6 % esquiva — **verbatim en Maxroll** ✅
- Generación de Fe **Clash 20 / Advance 18 / Holy Bolt 16 / Brandish 14** — fórmulas del fichero y ficha de Icy Veins, coinciden ✅
- Costes **Blessed Hammer 10 / Zeal 20 / Divine Lance 25 / Blessed Shield 28 / Shield Bash 32** ✅ · **Zeal `Health Cost:10%`** ✅ · **Rally 35 % de vida (29,75 % con mod), 3 cargas, `15+sLevel` de Fe** ✅
- Auras: Fanaticism 10 Fe / 15 s, Defiance 25 Fe / 20 s, Holy Light — / 25 s ✅

**Juramentos (§4)** — los cuatro textos, palabra por palabra, con sus números vivos:
- Zealot: *"echoes the attack for an additional [**0.25**…] of the damage, repeating for each stack of Fervor"*; `Paladin_Fervor` → `maxStackCount: "3"` ✅
- Juggernaut: *"consumes **8** stacks of Resolve… **[0.8…|x%|]** increased damage and gain **20%** increased size for **5** seconds. Your Minimum Resolve is increased by 1 and is no longer consumed when getting hit"* ✅
- Judicator: *"detonated early by your Core Judicator Skills, dealing **80%** weapon damage… increase the damage they take from you by **80%[x]** until they die"* ✅
- Disciple: *"grants Arbiter for **4.5** seconds… your Disciple Skills deal **80%[x]** increased damage"* ✅
- Y **el hallazgo del bloque podrido es real**: `classes["6"].paladinOaths` trae descripciones viejas con «Devotion Core», «Zealot stacks», Juggernaut al **20 %** y Disciple con `[PH]`. Quien datamine sin mirar publica esos zombis. **Buen trabajo del informe aquí.**
- **Los cuatro porcentajes de 3.1.0 están en la sección `Updates from PTR`** de la nota — es decir, son los valores **posteriores** al PTR, los que se publicaron. El fichero (build 72698, posterior al 72592 de salida) los confirma. **No hay contaminación de PTR.**

**Árbol (§7, §8.1, §10)** — reproducido nodo a nodo:
- Raíces: `1848` (sin `requiredLevel` = nivel 1), `1845`→3, `1842`→4, `1844`→8, `1952`→13, `1949`→19 ✅
- **270 nodos = 24 habilidades (`type 0`) + 168 modificadores (`type 1`) + 78 puertas** ✅. **Cero pasivas** ✅
- Reparto por clúster recorriendo el grafo de conexiones: Básicas 4 (Brandish, Advance, Clash, Holy Bolt) · Fundamentales 5 · Auras 3 · Valor 4 · Justicia 4 · Definitivas 4 = **4/5/3/4/4/4** ✅ (y d4guides.gg lo corrobora: «Basic 4», «Core 5», «Valor 4», «Justice 4», «Ultimate 4»)
- **Escalera de puertas idéntica a §8.1**: 5/9/14 · 6/10/15 · 7/11/16 · 12/17/20 · 18/21/23 · 22/24/25, y las 24 terceras variantes en **30/32/34/36/38/40** ✅
- **Los 24 nodos de habilidad admiten 15 rangos**, ni uno más ni uno menos ✅
- **Las tablas §10.1–§10.6 son exactas**: he comparado los 168 modificadores uno a uno —nombre, rangos y nivel— y **coinciden al 100 %**, incluidos los rangos de 5 en Clash, Advance, Holy Bolt, Shield Bash y Divine Lance. Es la mejor parte del documento
- `powerTables[37]`: r1 = 1,00 · r5 = **1,16** · r10 = **1,30** · r15 = **1,40** · r21 = **1,50** · 1,60 desde r31 ✅

**Habilidades (§9)** — todo lo demás cuadra:
- Etiquetas de Juramento de las 24: **coinciden al 100 %** con Icy Veins y con el fichero (`Skill_Divine` = Judicator). Y el informe tiene razón en que **Icy Veins deja en blanco «Oath Type» para Zenith y Arbiter of Justice**: el fichero les da `Skill_Zealot` y `Skill_Disciple` ✅
- Tipos de daño (Físico/Sagrado) de las 24 ✅ · golpes de suerte, salvo Falling Star ✅
- Enfriamientos de Aegis 20, Falling Star 12, Purify 12, Consecration 18, Condemn 15, Spear of the Heavens 14, Zenith 25, Fortress 60, Arbiter of Justice 120 ✅
- **Defiance Aura: 50 % de armadura y 50 % de resistencias, y son PORCENTAJES.** Icy Veins escribe *"granting 50 Armor and 50 bonus on All Resistances"* (se come el símbolo %); el fichero dice `[(0.5*Table(37,sLevel)+…)*100|%|]` y las notas oficiales *"Bonus Armor and Resistances increased from 30% to 50%"*. **El informe acertó y su fuente escrita no.** ✅
- **Las tres Auras dicen «and your allies» / «you and your allies» en el texto del juego** ✅ — el argumento del dúo se sostiene entero
- Clash → Crusader's March **+30 % de bloqueo**: notas 3.1.0 *"Crusader's March Block Chance increased from 15% to 30%"* + fichero `0.3*(1+…)` ✅
- Aegis +30 % de armadura en 3.1.0 ✅ · Fortress: inmune, Resolve **cada 0,5 s** a ti y a tus aliados ✅
- Habilidad de desmontar: cita literal correcta y **no está en el árbol** ✅

**Contexto y trampas (§2, §12.3, §14)**
- **«DOS NUEVAS CLASES» / «TWO NEW CLASSES»** en las páginas oficiales ✅ · nombres «El árbitro / El zelote / El judicante / El juggernaut» ✅
- **El error de Maxroll es real**: *"Introduced with Season 11 / Patch 2.5.0 (Diablo IV **Vessel of Hatred**)"*, con etiqueta «Season 11 - Divine Intervention» y *"Last Updated: July 14, 2026"*, changelog `["Post created for Season 11 / Patch 2.5.0", 2025-12-12]` + `["Updated for Season 14", 2026-07-14]` ✅
- **La guía de subida de nivel de Shield Charge está archivada**: `"dateModified":"2026-04-24T14:03:37+00:00"`, título «Season 12 - Slaughter», changelog *«Build archived prior to Lord of Hatred release until a post-release update is available.»*, y dentro *"put 2 points into Basic Skills"*, *"you need 20 skill points"*, *"At level 21 (without extra points)"* ✅ **Todo literal.**
- **Lista de tiers exacta**: `paladin-endgame-tier-list`, *"Last Updated: July 22, 2026"*, Season 14. **No hay tier S.** A = Shield Charge Paladin. B = Divine Lance · Clash · Shield of Retribution · Blessed Hammer. C = Zeal · Wing Strikes · Brandish · Auradin · Shield Bash. D = Zenith · Judgement. Changelog: *"July 20, 2026 — Added Shield Charge"* ✅
- **d4guides.gg dice «Resource: Resolve»** ✅ — y es peor de lo que dice el informe: **la misma página** pone «⚡ Faith» en la cabecera y «Generate Faith / Faith Cost» en cada ficha. Se contradice sola. Y arrastra **valores pre-3.1.0 de los Juramentos** (Juggernaut 60 %, Disciple 50 %, Judicator «8 %, up to 80 %»). Usarla solo para el reparto 4/5/3/4/4/4, como hizo el informe, fue correcto
- **Wowhead está muerto para esto**: su ficha `skill/shield-charge-2466077` sigue dando *"Cooldown: 10 seconds"*, *"granting 40%[+] Armor"*, daño 90 % — la foto anterior a 3.1.0, sin fecha visible ✅ (el informe ya la descarta)
- **Hilo del Brujo**: `created_at: 2026-03-05T20:08:20.535Z`, «Master Hell Itself with the Warlock» ✅ · y `classes["7"] = Warlock, primaryResource: {type: 10}` con `uiStrings.resourceType["10"] = "Wrath"` ✅
- **PTR 3.2 activo**: hilo «PTR 3.2 Known Issues - 8/4/2026» ✅
- **Paragon**: `classes["6"].paragonBoards` = `Paragon_Paladin_00` … `_09`, **10 tableros** ✅
- **Resolve base 8, tope 30**: `maxStackCount: "Min(30, … 8 + MaxStacks(1843183) + …)"` y la guía de Shield Charge, literal: *"Your basline maximum Resolve is 8 and you need 3x +6 Maximum Resolve Tempers, Aspect of Glynn's Anvil and the Phoba of Righteous Will set to reach exactly 30 Maximum Resolve."* ✅

---

## 9. FICHA DE CORRECCIONES — lo que hay que cambiar en el crudo

```
§1  tabla resumen  → «muy dependiente de enfriamientos» pierde fuerza (ver 2.2)
§3.3 fuente        → la cita de «shift that resource over to Life» es de
                     icy-veins.com/d4/guides/paladin-leveling-guide/, no de /paladin-skills/
§4.2 trampa 1      → «17→21» NO es de 3.0: es la misma nota 3.1.0, sección Expansion.
                     El «21→25» está en la sección «Updates from PTR» de 3.1.0. 25 % es lo vivo.
§5   Judgement     → quitar «marcas de 20 s». El keyword dice 3 s.
§5   Resolve       → no es exclusivo del Paladín (classFilter = 8 clases; Spiritborn también).
§5   cita Maxroll  → «Hit Count As Blocking triggers Retribution, which works as the primary
                     damage mechanic» NO existe. Sustituir por la frase real (ver 4.1).
§6   flails        → solo existen 1HFlail_Unique_Paladin_003 y _004.
§8   «30 puntos»   → cierto para 19 habilidades; 38 en Clash y Advance; 40 en Holy Bolt,
                     Shield Bash y Divine Lance.
§8.2 escala        → añadir que maxroll/skill-trees dice «10 % por rango» y contradice la tabla.
§9.4 Shield Charge → ENFRIAMIENTO 8 s (no 10). +60 % de ARMADURA (no 40 %). Daño base 180 %.
                     La habilidad base NO cuesta Fe; los 20 + 1/s son de Relentless Charge.
§9.4 Falling Star  → golpe de suerte 24 % según el fichero (Icy Veins dice 26 %).
§9.4 Rally         → +15 % de velocidad (Icy Veins dice 20 % y se equivoca);
                     el enfriamiento de 16 s queda como NO verificado.
§9.6 Heaven's Fury → ENFRIAMIENTO 15 s (no 30).
§11  fuentes       → los 14 puntos: maxroll.gg/d4/resources/season-journey (13/07/2026),
                     «netting you a total of 14 Skill Points». Los 69: tooltip «Level» del fichero.
§11  nota          → maxroll/skill-trees está «Updated for Lord of Hatred launch», no es
                     «anterior al rework». El conflicto (80 vs 83) sigue; el motivo cambia.
§14  Icy Veins     → añadir fila: paladin-skills act. 29/06/2026 = UN DÍA ANTES de 3.1.0
                     (30/06/2026). Es una página PRE-PARCHE. Varias de sus cifras están muertas.
§18.8 Wing Strikes → cerrar el hueco con news.blizzard.com/.../24244399 (cita en 7.1).
§18.11             → eliminar. 3.1.3 no toca al Paladín. 3.1.2 tampoco. 3.1.1 solo un fallo
                     cosmético («Damage with Holy was not showing in Stats and Materials tab»).
                     Entre el fichero (72698) y el vivo (73224) NO hay cambios de equilibrio
                     del Paladín. Confianza ALTA, no media.
```

---

## 10. VEREDICTO RAZONADO — **PARCIAL**

**Por qué no es «refutado».** El esqueleto del documento —recurso, mecánica de Juramentos, los seis clústeres y sus niveles, la escalera de puertas, el mapa completo de los 270 nodos, la tabla de escalado por rango, los cuatro Juramentos con sus números vivos, los 83 puntos, las auras que buffan a la pareja— **lo he reconstruido desde cero y sale idéntico**. El §10, que el informe presenta como «el mapa más completo que he podido reconstruir», es correcto **modificador a modificador**. Y sus tres secciones de higiene (§0, §14, §18) detectan trampas reales y verificables: la guía archivada, el bloque `paladinOaths` podrido, el error «Vessel of Hatred» de Maxroll, el «Resolve» de d4guides, el Wowhead muerto. Eso es trabajo bueno.

**Por qué no es «confirmado».** Tres cosas serias:

1. **Dos enfriamientos son valores muertos**, y **uno de ellos es el de Shield Charge**, la habilidad sobre la que este jugador va a construir su personaje. Un principiante que planifique con 10 s y no con 8 planifica mal.
2. **La fuente escrita principal del §9 está fechada un día antes del parche vivo**, lo que viola una regla dura del encargo y explica de golpe todos los desajustes numéricos. El informe vio el síntoma y no el diagnóstico.
3. **Una cita entrecomillada no existe en la página que se le atribuye**, y otra está atribuida a la página equivocada. En un documento cuyo mérito es precisamente el rigor de citas, eso pesa.

Ninguno de los tres invalida el documento. Los tres se arreglan con la ficha de §9.

**Nota final para el proyecto:** el patrón vuelve a ser el de la memoria del proyecto —*«las wikis de juegos vivos caducan»*—, pero con una vuelta de tuerca útil: aquí **la wiki no está sin fechar, está fechada… y la fecha es un día anterior al parche**. Una fecha reciente no basta; **hay que compararla con la fecha del parche vivo**, no con la de la temporada. Y cuando el fichero de datos y una guía discrepan, gana el fichero si su build es posterior al de la nota de parche — que es justo el caso aquí (72698 > 72592).
