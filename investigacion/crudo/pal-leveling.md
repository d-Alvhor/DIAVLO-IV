# Subida 1 → 70 del Paladín — Season 14 "Death Awakening", parche vivo 3.1.3

> **Dominio:** subida de nivel del Paladín (*Paladin*) con Vessel of Hatred + Lord of Hatred,
> herencia de cuenta, ruta más rápida a 70, tiempos realistas y dúo con nigromante sin expansiones.
> **Fecha de la investigación:** 19/08/2026. **Fin de temporada estimado:** ~15/09/2026 (≈4 semanas).
> **Regla de esta ficha:** cada número lleva su URL. Lo que no vi por escrito está en "No encontrado".

---

## 0. Anclaje al parche vivo y frescura de cada fuente

El **parche vivo es 3.1.3, build 73224, 12 de agosto de 2026**, confirmado en la página oficial de
notas de parche — [Blizzard, Diablo IV Patch Notes](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes)
(textual: *"Diablo IV Patch 3.1.3 Build #73224 (All Platforms)—August 12, 2026"*).

Esto importa porque **casi todas las guías de Paladín para leveling están fechadas el 29–30 de junio
de 2026**, es decir, escritas contra el parche **3.1.0** de arranque de temporada. Han pasado tres
parches desde entonces (3.1.1, 3.1.2, 3.1.3) y **sí ha habido cambios de Paladín en esa ventana**.

| Fuente | Fecha que declara | Parche implícito | Frescura |
|---|---|---|---|
| [Blizzard — Patch Notes](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) | 12/08/2026, build 73224 | **3.1.3** | ✅ Vivo |
| [Maxroll — War Plans](https://maxroll.gg/d4/resources/war-plans) | 05/08/2026 | 3.1.2/3.1.3 | ✅ Fresca |
| [Maxroll — Shield Charge Paladin (endgame)](https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide) | 25/07/2026 | 3.1.1/3.1.2 | ✅ Fresca |
| [Maxroll — Experience](https://maxroll.gg/d4/resources/experience) | 21/07/2026 | 3.1.x | ✅ Fresca |
| [Maxroll — Season Guide S14](https://maxroll.gg/d4/resources/season-guide) | 13/07/2026, "Patch 3.1.0" | 3.1.0 | 🟡 Aceptable |
| [Maxroll — Paladin Leveling Tier List](https://maxroll.gg/d4/tierlists/paladin-leveling-tier-list) | 30/06/2026 | **3.1.0** | 🟡 Arranque de temporada |
| [Maxroll — Speed Leveling](https://maxroll.gg/d4/meta/alt-leveling-guide) | 30/06/2026 | **3.1.0** | 🟡 Arranque de temporada |
| [Maxroll — Judgement Paladin Leveling](https://maxroll.gg/d4/build-guides/judgement-paladin-leveling-guide) | 30/06/2026, "Patch 3.1" | **3.1.0** | 🟡 Arranque de temporada |
| [Maxroll — Shield of Retribution Paladin Leveling](https://maxroll.gg/d4/build-guides/shield-of-retribution-paladin-leveling-guide) | 29/06/2026 | **3.1.0** | 🟡 Arranque de temporada |
| [Icy Veins — Paladin Leveling Guide](https://www.icy-veins.com/d4/guides/paladin-leveling-guide/) | 29/06/2026 | **3.1.0** | 🟡 Arranque de temporada |
| [Maxroll — Multiplayer](https://maxroll.gg/d4/resources/multiplayer) · [Difficulty Scaling](https://maxroll.gg/d4/resources/difficulty-overview) | 26/06/2026 | 3.0.x → S14 | 🟡 Pre-temporada |
| ⚠️ [Maxroll — Shield Charge Paladin **Leveling**](https://maxroll.gg/d4/build-guides/shield-charge-paladin-leveling-guide) | **24/04/2026**, banner **"Season 12 - Slaughter"** | **Pre-3.0** | 🔴 **Escrita antes de que la clase saliera** |
| ⚠️ [Maxroll — Mercenaries Overview](https://maxroll.gg/d4/resources/mercenaries-overview) | **11/07/2025**, "Season 6 / Patch 2.0" | 2.0 | 🔴 **13 meses de antigüedad** |
| 🧪 Datamining `assets-ng.maxroll.gg/d4-tools/game/data.min.json` | campo `version` = **`3.1.0.72698`** | **3.1.0** | 🟡 Un parche por detrás del vivo |

**Declaración de datamining:** he descargado y leído el fichero de datos que sirve el planificador de
Maxroll (`https://assets-ng.maxroll.gg/d4-tools/game/data.min.json`, 12 MB). Es **datamining**, no
documentación oficial. Su campo `version` dice **`3.1.0.72698`**, o sea que refleja el **parche de
arranque de temporada, no el 3.1.3 vivo**. Todo lo que saco de ahí va marcado 🧪.

**403 de Maxroll:** esta vez **Maxroll respondió bien** a casi todas las peticiones. El que sí devolvió
**403 Forbidden** fue **Mobalytics** (`https://mobalytics.gg/diablo-4/guides/warplans-guide`). Lo digo
para que conste: no he podido leer Mobalytics y **no cito nada de ahí**. Reddit tampoco es accesible
para este agente (el buscador rechaza el dominio), así que **no hay ninguna cita de r/diablo4** en esta ficha.

---

## 1. TL;DR — las seis cosas que cambian tu plan

1. **La guía de leveling de Shield Charge que probablemente ibas a seguir está muerta.** El
   [Shield Charge Paladin *Leveling* Guide de Maxroll](https://maxroll.gg/d4/build-guides/shield-charge-paladin-leveling-guide)
   está fechado **24/04/2026** y sigue con el banner **"Season 12 - Slaughter"** — cuatro días *antes*
   del lanzamiento de Lord of Hatred (28/04/2026). Es una guía **pre-lanzamiento** que nadie ha
   tocado en cuatro meses. ⚠️ No la uses para subir.
2. **Maxroll te dice explícitamente con qué subir para llegar a Shield Charge.** La guía de endgame de
   Shield Charge (**25/07/2026**, S14) dice textual: *"This build guide assumes you have a Level 70
   Character and unlocked Torment 1. To get there, level up with one of our Paladin Leveling Guides"*
   y apunta al **Shield of Retribution Paladin Leveling Guide** —
   [Maxroll](https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide). Ese mismo build es
   **S-Tier** en la tier list de leveling — [Maxroll](https://maxroll.gg/d4/tierlists/paladin-leveling-tier-list).
3. **Los Planes de Guerra (*War Plans*) son POR PERSONAJE en la S14, no de cuenta.** Blizzard lo
   reconoció y dijo que **no lo van a cambiar esta temporada**: *"We hear you on the feedback for
   per-character War Plans. We are investigating making this be per-partition, which is how Paragon
   works"* — [Icy Veins, 30/06/2026](https://www.icy-veins.com/d4/news/diablo-4-war-plans-get-faster-xp-but-the-biggest-fix-is-still-missing/).
   Tu Paladín empieza el árbol de Planes de Guerra **desde el rango 0**, aunque el Nigromante lo tenga hecho.
4. **Los Planes de Guerra exigen haber completado la campaña de Lord of Hatred.** Textual:
   *"Once you complete the Lord of Hatred Campaign, you can start a War Plan by visiting Tyrael in
   Temis"* — [Maxroll, 05/08/2026](https://maxroll.gg/d4/resources/war-plans). Y toda la ruta rápida
   de leveling de S14 está construida **encima** de los Planes de Guerra. Si nadie en tu cuenta ha
   terminado LoH, **no tienes acceso a la ruta rápida**.
5. **La ruta rápida oficial asume algo que tú probablemente no tienes.** La
   [Speed Leveling Guide de Maxroll (30/06/2026)](https://maxroll.gg/d4/meta/alt-leveling-guide)
   dice literalmente que asume *"you have completed the Campaign at least once on your account"*.
   Acabas de comprar las dos expansiones. Ver §3.
6. **Tu pareja sin expansiones sí llega a 70.** Icy Veins, en el artículo dedicado a exactamente esa
   pregunta: el tope de nivel **sube a 70 para todo el mundo**, no solo para quien tenga la expansión —
   [Icy Veins, 28/04/2026](https://www.icy-veins.com/d4/news/do-you-need-lord-of-hatred-to-stay-competitive-in-diablo-4/).
   Lo que **no** puede es entrar en Skovos, Planes de Guerra, Talismán ni Cubo Horádrico (§9).

---

## 2. Qué hereda un Paladín nuevo en tu cuenta (con un estacional de 70 ya hecho)

Aquí hay que separar **tres capas** que la gente confunde: lo que es de cuenta permanente, lo que es
de la temporada, y lo que es del personaje. Y hay una **trampa gorda**: los Planes de Guerra son
del personaje.

| Cosa | ¿La hereda el Paladín nuevo? | Evidencia |
|---|---|---|
| **Renombre (*Renown*)** | ✅ Sí | *"your renown rewards"* accesibles en el reino estacional — [Icy Veins — New Season Checklist](https://www.icy-veins.com/d4/guides/diablo-4-new-season-checklist/) |
| **Altares de Lilith** | ✅ Sí | *"your Altars of Lilith bonuses"* — [Icy Veins](https://www.icy-veins.com/d4/guides/diablo-4-new-season-checklist/) |
| **Mapa descubierto y santuarios de viaje** | ✅ Sí | *"Discovered areas and waypoints transfer over"* — [Icy Veins](https://www.icy-veins.com/d4/guides/diablo-4-new-season-checklist/) |
| **Montura** | ✅ Sí | *"you will have access to your horse"* — [Icy Veins](https://www.icy-veins.com/d4/guides/diablo-4-new-season-checklist/) |
| **Alijo (*Stash*)** | ✅ Sí, compartido en el reino estacional | Alijo compartido entre personajes de la cuenta en el mismo modo — [Wowhead — Stash Guide](https://www.wowhead.com/diablo-4/guide/gameplay/stash) 🟡 página sin fecha visible |
| **Oro y materiales** | ✅ Sí, compartidos por modo (Normal/Hardcore) | *"Gold and materials are shared across all characters in that game mode"* — [Wowhead — Stash Guide](https://www.wowhead.com/diablo-4/guide/gameplay/stash) 🟡 sin fecha visible; **verifícalo en pantalla** |
| **Rango de Temporada (*Season Rank*)** | ✅ Sí, es de cuenta dentro de la temporada | *"Season Rank progression is shared across all Seasonal characters, so you do not need to repeat early Ranks on alts"* — [Icy Veins — Season Rank](https://www.icy-veins.com/d4/guides/season-rank/) |
| **Recompensas del Rango de Temporada ya reclamadas** | ➖ Se reclaman una vez; las **no** reclamadas siguen disponibles para otro personaje estacional | [Icy Veins — Season Rank](https://www.icy-veins.com/d4/guides/season-rank/) 🟡 la página no lo dice con esas palabras exactas; ver "No encontrado" |
| **Desbloqueo de El Foso y La Torre** | ✅ Sí, va por Rango de Temporada 2, que es de cuenta | *"Clearing Rank 2 unlocks access to both The Pit and The Tower"* — [Icy Veins — Season Rank](https://www.icy-veins.com/d4/guides/season-rank/) |
| **Ciudad Subterránea de Kurast** | ✅ Sí, **desde nivel 1** una vez desbloqueada en la cuenta | *"all your alt characters will have access to this activity right from level 1"* — [Icy Veins — Kurast Undercity](https://www.icy-veins.com/d4/guides/kurast-undercity-guide/) |
| **Planes de Guerra: acceso** | ✅ Sí, si **alguien** completó la campaña de LoH | *"Upon completion, any future characters will have access to War Plans after a short introduction"* — [Icy Veins — War Plans Overview](https://www.icy-veins.com/d4/guides/war-plans-overview/) |
| **Planes de Guerra: rango y árboles de actividad** | ❌ **NO.** Son por personaje en S14 | Blizzard: *"We hear you on the feedback for per-character War Plans…"* y la mejora **no llega en S14** — [Icy Veins, 30/06/2026](https://www.icy-veins.com/d4/news/diablo-4-war-plans-get-faster-xp-but-the-biggest-fix-is-still-missing/) |
| **Nivel, equipo, Paragón** | ❌ No | *"You will start at Level 1 with no gear or skills"* — [Icy Veins](https://www.icy-veins.com/d4/guides/diablo-4-new-season-checklist/) |
| **Saltar campaña** | ⚠️ Depende. Ver §3 | — |
| **Afinidad de mercenarios (*Rapport*)** | ❓ No encontrado con fecha 3.1.x. Ver "No encontrado" | La página de Maxroll es de **11/07/2025** ⚠️ |

### La trampa de los Planes de Guerra, explicada

Los Planes de Guerra tienen **rangos del 0 al 10** y **siete árboles de actividad**
([Maxroll, 05/08/2026](https://maxroll.gg/d4/resources/war-plans); 🧪 el datamining confirma los
siete árboles: `Warplans_Whispers`, `Warplans_NightmareDungeons`, `Warplans_Helltide`,
`Warplans_Undercity`, `Warplans_BossLair`, `Warplans_InfernalHordes`, `Warplans_Pit`).

Los nodos de esos árboles son **la fuente principal de XP de la ruta rápida de S14**. Y como son
**por personaje**, tu Paladín tiene que volver a farmearlos desde cero. Además, un personaje recién
hecho arranca con un plan más corto: *"on a fresh character, your Path will only require finishing
two activities before being able to claim rewards"*, frente a tres la primera vez tras la campaña —
[Icy Veins — War Plans Overview](https://www.icy-veins.com/d4/guides/war-plans-overview/).

---

## 3. El bloqueo real: la campaña. Léelo antes que nada

Esto es lo que decide si tu subida dura 3 horas o 20.

**Regla del "Saltar campaña" (*Skip Campaign*), dos condiciones a la vez:**

1. Solo se ofrece **en la pantalla de creación de personaje**.
2. Solo aparece si **esa** campaña está completada **al menos una vez en la cuenta**. Textual de Icy
   Veins para LoH: *"To skip the story in future seasons, you must complete the Lord of Hatred
   campaign at least once"* — [Icy Veins — Lord of Hatred Overview, 24/04/2026](https://www.icy-veins.com/d4/guides/lord-of-hatred-overview/).

Y son **campañas separadas**: base, Vessel of Hatred y Lord of Hatred. Saltarse una no salta las otras.
*"if you have beaten the base game campaign, skipping it gives you all base game waypoints. If you have
beaten Vessel of Hatred, skipping it gives you all waypoints from both campaigns"* —
[Icy Veins — Skipping the Campaign Now Unlocks All Waypoints](https://www.icy-veins.com/d4/news/diablo-4-skip-campaign-unlocks-waypoints/).

**Tu situación, en tres escenarios. Compruébalo tú en 30 segundos** (crea un personaje de prueba y
mira si aparecen los interruptores de "saltar campaña"; no lo confirmes, solo míralo):

| Escenario | Qué tienes disponible | Qué hacer |
|---|---|---|
| **A — Nadie ha completado ninguna campaña** (lo más probable: acabas de comprar) | Ni salto de campaña, ni Planes de Guerra, ni Ciudad Subterránea, ni mercenarios, ni Talismán, ni Cubo | Ver "La jugada del Nigromante", abajo |
| **B — Campaña base completada, VoH/LoH no** | Puedes saltar la base (santuarios base abiertos) pero no VoH ni LoH | El Paladín sube rápido en zonas base; alguien tiene que hacer VoH y LoH |
| **C — Las tres completadas** | Salto total, Planes de Guerra desde el minuto uno | Aplica la ruta de §6 tal cual |

### La jugada del Nigromante (el consejo con más palanca de toda esta ficha)

Si estás en el escenario A: **no hagas las campañas con el Paladín de nivel 1. Hazlas con el
Nigromante de 70.** Motivos, todos con fuente:

- La completitud de campaña que abre el "saltar" es **de cuenta**, no del personaje: *"you only have
  to play through the campaign once in order to unlock the skip for all future seasons"* —
  [Icy Veins — New Season Checklist](https://www.icy-veins.com/d4/guides/diablo-4-new-season-checklist/).
- El acceso a Planes de Guerra se propaga a los demás personajes: *"Upon completion, any future
  characters will have access to War Plans after a short introduction"* —
  [Icy Veins — War Plans Overview](https://www.icy-veins.com/d4/guides/war-plans-overview/).
- La Ciudad Subterránea se propaga **desde nivel 1**: *"all your alt characters will have access to
  this activity right from level 1"* — [Icy Veins — Kurast Undercity](https://www.icy-veins.com/d4/guides/kurast-undercity-guide/).

Un Nigromante de 70, aunque vaya mal equipado, atraviesa las campañas mucho más rápido que un
Paladín de nivel 1, y **desbloquea la infraestructura para el Paladín y para toda temporada futura**.

⚠️ **Incertidumbre honesta:** la frase de Icy Veins dice *"any future characters"*. **No he encontrado
ninguna fuente fechada en 3.1.x que confirme que un personaje que YA existe** (tu Paladín, si ya lo
creaste) recibe los Planes de Guerra retroactivamente al completar LoH en otro personaje. En el
material previo de este proyecto hay reportes de foro de que **alts existentes no reciben el salto de
campaña** ([foro US, 03/05/2026](https://us.forums.blizzard.com/en/d4/t/unable-to-skip-campaign-on-existing-level-60-alts/249303)),
pero eso es sobre el *salto*, no sobre el *acceso a Planes de Guerra*. Está en "No encontrado".
**Implicación práctica:** si aún no has creado el Paladín, **haz primero las campañas con el Nigromante
y crea el Paladín después**. Ese orden te cubre en ambos casos.

**Duración de las campañas de expansión** — ninguna fuente preferente fechada en 3.1.x da un número.
Las cifras que circulan (LoH: *"10-15 hours"*, *"6 to 8 hours, or even 10"*) vienen de
[Sportskeeda](https://www.sportskeeda.com/mmo/how-long-diablo-4-lord-hatred-take-beat) y
[TweakTown](https://www.tweaktown.com/news/111308/diablo-4s-lord-of-hatred-is-a-game-changer-heres-everything-you-need-to-know/index.html),
**fuera de la lista de preferentes y sin fecha de parche**. Trátalas como orden de magnitud, no como dato.

---

## 4. Con qué build subir el Paladín

### 4.1 La respuesta corta

**Shield of Retribution Paladin (Escudo de Retribución).** Es la única que satisface las tres
condiciones a la vez: es la mejor valorada para subir, es fácil, y es la que la propia guía de tu
build objetivo te dice que uses.

### 4.2 La tier list de leveling de Paladín

[Maxroll — Paladin Leveling Builds Tier List, 30/06/2026](https://maxroll.gg/d4/tierlists/paladin-leveling-tier-list).
Criterio declarado: *"Movement speed, survivability, ease of play, damage output and total time to
reach level 70"*.

| Tier | Build |
|---|---|
| **S** | **Shield of Retribution Paladin** |
| A | Blessed Hammer Paladin |
| B | Zeal Paladin |
| B | Judgement Paladin |

⚠️ Fechada el **30/06/2026 = parche 3.1.0**. No refleja los ajustes de Paladín de 3.1.1–3.1.3 (§4.5).

### 4.3 El puente hacia Shield Charge, dicho por Maxroll

La [guía de endgame de Shield Charge Paladin (25/07/2026, S14)](https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide)
dice textual:

> *"This build guide assumes you have a Level 70 Character and unlocked Torment 1. To get there, level
> up with one of our Paladin Leveling Guides"*

…y la que nombra es la **Shield of Retribution Paladin Leveling Guide**. O sea: **no subes con Shield
Charge; subes con Shield of Retribution y a los 70 te reespecializas a Shield Charge**. Las dos son
builds de escudo y Espinas/Resolución, así que **el equipo que juntas subiendo no se tira**.

Encaja además con lo que pides ("daño alto sin rotaciones imposibles"): la propia guía de Shield of
Retribution lista como pros *"Super Fast"*, *"Can Ignore Items"* y *"Easy Endgame Transition"*, y como
contras *"Small AoE"*, *"Cooldown Timing"*, *"Best on Stationary Targets"* —
[Maxroll](https://maxroll.gg/d4/build-guides/shield-of-retribution-paladin-leveling-guide).
Ese *"Can Ignore Items"* es literalmente lo que necesita un principiante: **subes sin pelearte con el loot**.

### 4.4 ⚠️ Por qué NO uses la guía de leveling de Shield Charge

| Dato | Valor |
|---|---|
| URL | https://maxroll.gg/d4/build-guides/shield-charge-paladin-leveling-guide |
| Última actualización declarada | **24 de abril de 2026** |
| Banner de temporada | **"Season 12 - Slaughter"** |
| Lanzamiento de Lord of Hatred (y del Paladín) | **28 de abril de 2026** — [Icy Veins](https://www.icy-veins.com/d4/news/do-you-need-lord-of-hatred-to-stay-competitive-in-diablo-4/) |

La guía es **cuatro días anterior al lanzamiento de la clase**. Es material de **pre-lanzamiento /
acceso anticipado**, no de parche vivo. Han pasado **cuatro parches** (3.0.x, 3.1.0, 3.1.1, 3.1.2, 3.1.3)
sin que la toquen. Lo que dice (por si te la encuentras y quieres saber qué estás mirando, ⚠️ **todo
esto es pre-parche y puede estar roto**):

- Niveles 1–20: Clash, Shield Bash – Breach, Holy Light Aura, Defiance Aura, Consecration.
- *"At level 21 (without extra points), you are ready to switch to Shield Charge - Relentless Charge.
  Replace Shield Bash and become much more mobile."*
- Pasiva clave: Coat of Arms. Mercenarios: Varyana contratada, Aldkin de refuerzo.
- *"Thorns"* como estadística rectora; *"weapon damage is actually irrelevant"*.

Como ves, **es casi la misma familia que Shield of Retribution** (Clash, Espinas, escudo). No pierdes
nada usando la guía viva en vez de esta.

### 4.5 Cambios de Paladín posteriores a las guías (3.1.1 – 3.1.3)

De la página oficial de notas de parche —
[Blizzard](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) — que cubre 3.1.3
y hacia atrás hasta 3.1.0:

| Cambio | Verbatim |
|---|---|
| Wing Strikes | *"Wing Strikes Base damage increased from 160% to 200%."* |
| Defiance Aura | Ajustada (la página lista el cambio; **no he podido extraer el número exacto**, ver "No encontrado") |
| Aegis | Ajustada (ídem) |
| Seal of the Second Trumpet (único) | Ajustado (ídem) |
| Judicator / Judgement | *"Damage after an enemy is Judged changed from 8% stacking 10 times to 60% stacking once"*, con nota de desarrollo: *"Judicator builds without stacking Judgement procs were less successful than intended"* — recogido del resumen de [Maxroll — 3.1.2 Patch Notes](https://maxroll.gg/d4/news/lord-of-hatred-3-1-2-patch-notes) 🟡 el extracto no ancla el cambio a un parche concreto; ver "No encontrado" |
| Carga (*Charging*) | *"Movement Speed while Charging changed from 100% Cap 1 speed to 50% Cap 1 and 50% Cap 2 speed"*, con *"base armor granted while charging increased from 40% to 60%"* 🟡 misma advertencia de anclaje |

**Lectura:** los ajustes de Judicator y de Carga afectan a **Judgement** (B-tier) y a **Shield Charge**
(tu objetivo de endgame), no a Shield of Retribution. La recomendación de subir con Shield of
Retribution **no se ve tocada** por lo que he podido leer.

### 4.6 Barra de habilidades y orden de puntos — Shield of Retribution

[Maxroll — Shield of Retribution Paladin Leveling Guide, 29/06/2026](https://maxroll.gg/d4/build-guides/shield-of-retribution-paladin-leveling-guide):

| Elemento | Valor |
|---|---|
| **Juramento (*Oath*)** | **Juggernaut Oath** — *"your minimum Resolve cannot fall below 1, permanently reducing all damage you take by 20%"* |
| **Barra final** | Clash · Blessed Shield – **Shield of Retribution** · Holy Light Aura · Defiance Aura · Fanaticism Aura · Rally – Words of Sacrifice |
| **Punto de inflexión** | *"transitioning to Blessed Shield at level 32 when Shield of Retribution unlocks"* |
| **Puntos totales a nivel 70** | *"14 extra skill points for a total of 83"* |
| **Estadística rectora** | *"weapon damage is actually irrelevant because everything scales off Thorns"* → **Espinas (*Thorns*)**, Probabilidad de Bloqueo, Armadura, Resistencias, Vida |
| **Runas BiS** | Cir + Ceh (invoca lobos congelantes) · Cem + Qua (velocidad de movimiento) |
| **Mercenarios** | Contratado: **Varyana** · Refuerzo: **Aldkin** |

**Orden de gasto de puntos, por etapas** (así es como lo estructura la guía; ver el aviso de abajo):

| Etapa | Sección de la guía | Qué priorizas |
|---|---|---|
| 1 | *Getting Started* | **Clash** al máximo — es tu generador y el que mantiene el buff **Punishment**, que escala Bloqueo y Espinas |
| 2 | nivel **32** | Entra **Blessed Shield – Shield of Retribution**; pasa a ser tu habilidad principal |
| 3 | *Auras* | Holy Light Aura, Defiance Aura, Fanaticism Aura, según se van abriendo |
| 4 | *Rally* | **Rally – Words of Sacrifice** (recurso + movilidad) |
| 5 | *Final Journey to Level 70* | Los **14 puntos extra** hasta los **83** totales, a rellenar principales y utilidad |

⚠️ **Hueco declarado, no lo relleno inventando:** **ninguna de las guías que he abierto publica en
texto una tabla nivel-a-nivel** ("nivel 5: X, nivel 8: Y"). Ni Maxroll ni Icy Veins. En Maxroll ese
detalle vive dentro del **planificador interactivo embebido**, que el lector automático no renderiza;
en Icy Veins la sección existe (*"Below is the recommended order for spending your points as you level
up"*) pero **la tabla tampoco viene en el HTML servido**. Lo honesto: **abre el planificador de la
guía en el navegador y sigue el orden ahí**. Lo que sí está en texto es lo de arriba, y es suficiente
para jugar bien.

### 4.7 Alternativas, por si Shield of Retribution no te entra

| Build | Tier | Barra | Juramento | Mercenarios | Fuente |
|---|---|---|---|---|---|
| **Blessed Hammer** | A | Advance · Blessed Hammer · Falling Star · Defiance Aura · Rally · Condemn (o Arbiter of Justice) | — | Raheir contratado, Varyana refuerzo | [Icy Veins, 29/06/2026](https://www.icy-veins.com/d4/guides/blessed-hammer-paladin-leveling-build/) |
| **Divine Lance** | — (no listada) | Advance · Divine Lance · Fanaticism Aura · Defiance Aura · Holy Light Aura · Rally | **Zealot Oath** | Raheir contratado, Varyana refuerzo | [Icy Veins, 29/06/2026](https://www.icy-veins.com/d4/guides/divine-lance-paladin-leveling-build/) |
| **Judgement** | B | Arbiter of Justice · Spear of the Heavens · Blessed Hammer · Fanaticism Aura · Defiance Aura | **Judicator Oath** | Varyana contratada, Aldkin refuerzo | [Maxroll, 30/06/2026](https://maxroll.gg/d4/build-guides/judgement-paladin-leveling-guide) |

Estadísticas y gemas de Blessed Hammer, por si vas por ahí: **Reducción de Enfriamiento, Fuerza, Vida
Máxima, Velocidad de Ataque**; **Rubí** en armas/armadura, **Diamante** en joyería —
[Icy Veins](https://www.icy-veins.com/d4/guides/blessed-hammer-paladin-leveling-build/).

Aspectos de Blessed Hammer con su texto: **Aspect of Glynn's Anvil** (*"Your maximum Resolve is
increased by 2 and you gain [3-4%] Damage Reduction per Resolve"*), **Aspect of Holy Punishment**
(*"Holy and Fire damage are increased by [40-60%]"*), **Aspect of Lagera's Sovereignty** (*"Your
Disciple Skills deal [40.0–60.0%] increased damage"*), **Aspect of Angelic Masterwork** —
[Icy Veins](https://www.icy-veins.com/d4/guides/blessed-hammer-paladin-leveling-build/).

### 4.8 Aspectos a cazar con Shield of Retribution, en orden

Orden de prioridad textual de [Maxroll](https://maxroll.gg/d4/build-guides/shield-of-retribution-paladin-leveling-guide):

1. Needleflare · 2. Might · 3. Umbral · 4. The Penitent's · 5. Utmost Glory · 6. Virtuous ·
7. Chastisement · 8. Lapa's Scripture · 9. Juggernaut's Covenant · 10. Verdant Restoration

### 4.9 🧪 Las 23 habilidades activas del Paladín (datamining)

Del árbol `Paladin_NEW` en `data.min.json` (**versión `3.1.0.72698`**, un parche por detrás del vivo).
Sirve para que reconozcas los nombres en pantalla:

Advance · Aegis · Arbiter of Justice · Blessed Hammer · Blessed Shield · Brandish · Clash · Condemn ·
Consecration · Defiance Aura · Divine Lance · Fanaticism Aura · Fortress · Heaven's Fury · Holy Bolt ·
Holy Light Aura · Purify · Rally · Shield Bash · Shield Charge · Spear of the Heavens · Zeal · Zenith

🧪 Nota curiosa del datamining: el identificador interno de **Clash** es `Paladin_Punish`, el de
**Divine Lance** es `Paladin_Impale` y el de **Advance** es `Paladin_Advance_lunge`. Son nombres de
desarrollo, no del juego.

---

## 5. Dificultad mientras subes, y los multiplicadores de XP

### 5.1 Qué dificultad poner

Dos fuentes preferentes, dos consejos ligeramente distintos:

- **Icy Veins (29/06/2026):** *"The recommended difficulty to level in is Hard. This will provide you
  with the smoothest and fastest leveling experience."* Añade que Experto **suma tiempo sin XP
  proporcional** y que Normal es más lento en conjunto —
  [Icy Veins — Paladin Leveling Guide](https://www.icy-veins.com/d4/guides/paladin-leveling-guide/).
- **Maxroll (30/06/2026):** regla de eficiencia, no de dificultad fija: sube de escalón mientras
  puedas matar a un ritmo razonable; el umbral que da es el punto en el que *"kill enemies half as
  quickly"* — [Maxroll — Speed Leveling](https://maxroll.gg/d4/meta/alt-leveling-guide).
- **d4builds:** empezar en **Normal** y ajustar; a partir de 70, **Penitent** —
  [d4builds — Season 14 Leveling Guide](https://d4builds.gg/leveling-guide/).

**Síntesis para un principiante:** empieza en **Difícil (*Hard*)**. Si mueres más de una vez cada
20 minutos, baja a Normal. Si los paquetes se derriten, sube a Experto.

### 5.2 Bonus de XP por dificultad

| Dificultad | Bonus de XP y Oro | Fuente |
|---|---|---|
| Normal | Base | [Maxroll — Difficulty Scaling, 26/06/2026](https://maxroll.gg/d4/resources/difficulty-overview) |
| **Difícil (Hard)** | ***"75% more Experience and Gold"*** | [Maxroll — Speed Leveling, 30/06/2026](https://maxroll.gg/d4/meta/alt-leveling-guide) |
| **Experto (Expert)** | ***"125%"*** | [Maxroll — Speed Leveling](https://maxroll.gg/d4/meta/alt-leveling-guide) |
| **Penitente (Penitent)** | ***"175%"*** | [Maxroll — Speed Leveling](https://maxroll.gg/d4/meta/alt-leveling-guide) |
| Tormento I | **+300%** — se abre con **El Foso nivel 10** | [Maxroll — Difficulty Scaling](https://maxroll.gg/d4/resources/difficulty-overview) |
| Tormento II | +400% — Foso 15 | [Maxroll](https://maxroll.gg/d4/resources/difficulty-overview) |
| Tormento III | +500% — Foso 20 | [Maxroll](https://maxroll.gg/d4/resources/difficulty-overview) |
| Tormento IV | +600% — Foso 25 | [Maxroll](https://maxroll.gg/d4/resources/difficulty-overview) |
| Tormento V | +700% — Foso 30 | [Maxroll](https://maxroll.gg/d4/resources/difficulty-overview) |
| Tormento VI | +800% — Foso 40 | [Maxroll](https://maxroll.gg/d4/resources/difficulty-overview) |
| Tormento VII | +900% — Foso 50 | [Maxroll](https://maxroll.gg/d4/resources/difficulty-overview) |
| Tormento VIII | +1000% — Foso 60 | [Maxroll](https://maxroll.gg/d4/resources/difficulty-overview) |
| Tormento IX–XII | +1100% / +1200% / +1300% / **+1400%** — Foso 70 / 80 / 90 / 100 | [Maxroll](https://maxroll.gg/d4/resources/difficulty-overview) |

⚠️ **Ojo:** el parche 3.1.3 dice *"Increased experience rewards in Torment 8 and up"* —
[Blizzard](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) — así que **la
tabla de Maxroll (26/06) puede estar por debajo de lo real de T8 en adelante**. Para subir 1→70 da
igual: no vas a estar en T8.

### 5.3 Otros multiplicadores confirmados

| Multiplicador | Valor | Fuente |
|---|---|---|
| Jugador cerca (no en grupo) | ***"x5% experience bonus if a player is within 90m of you"*** | [Maxroll — Multiplayer, 26/06/2026](https://maxroll.gg/d4/resources/multiplayer) |
| **En grupo, a menos de 90 m** | ***"x10% experience bonus if you are partied with a player within 90m of you"*** — **no se acumulan entre sí ni con más miembros** | [Maxroll — Multiplayer](https://maxroll.gg/d4/resources/multiplayer) |
| Confirmación cruzada | *"When you are within 90 meters of each other (~3 screens radius), you get a Party Bonus buff, increasing XP gains by 10%"* | [Maxroll — Experience, 21/07/2026](https://maxroll.gg/d4/resources/experience) |
| Hoguera (*Campfire*) | **+15% de XP máximo**, acumulándose durante dos minutos | [Maxroll — Experience](https://maxroll.gg/d4/resources/experience) |
| XP base por tipo de monstruo | Secuaces: base **+1568** · Campeones: base **+2352** · **Élites: base +4704** | [Maxroll — Experience](https://maxroll.gg/d4/resources/experience) |

Ese último dato es la razón de todo lo demás: **los élites valen ~3× un secuaz**. Por eso la Ciudad
Subterránea es buena XP (*"thanks to the high amount of elites that provide bonus experience"* —
[Icy Veins](https://www.icy-veins.com/d4/guides/kurast-undercity-guide/)) y por eso barrer el 100%
de una mazmorra es un error.

**Escalado de monstruos en grupo:** *"The life and damage done by monsters in the Open World do not
scale with the number of players. However, the life and damage done by Monsters in Dungeons (instances
with a maximum of 4 players) scale up with the number of party members"* —
[Maxroll — Multiplayer](https://maxroll.gg/d4/resources/multiplayer). Traducción: **en dúo, el mundo
abierto y las Oleadas Infernales son XP gratis; las mazmorras cerradas suben de dureza**.

---

## 6. La ruta a 70, franja por franja

### 6.1 Ruta rápida canónica (requiere campañas hechas — escenario C)

Esta es la ruta que publican las fuentes preferentes. **Asume campaña completada** (*"you have
completed the Campaign at least once on your account"* — [Maxroll](https://maxroll.gg/d4/meta/alt-leveling-guide)).

| Franja | Qué haces | Fuente y verbatim |
|---|---|---|
| **1–25** | Dificultad **Difícil**. Arrancas la línea de misiones estacional. **Oleadas Infernales (*Helltides*) + Mazmorras de Pesadilla**, "pescando" Planes de Guerra que incluyan Oleadas Infernales. Objetivo: desbloquear **Writhe and Rot** en el árbol de Oleadas Infernales cuanto antes | *"Prioritize Helltides and Nightmare Dungeons while fishing for specific War Plans"*, *"Target level 1 War Plans connected to Helltides"*, *"Unlock Writhe and Rote upgrade in your War Plans as soon as possible"* — [Maxroll — Speed Leveling](https://maxroll.gg/d4/meta/alt-leveling-guide) |
| **25** | Se abre el árbol de **Ciudad Subterránea** en Planes de Guerra. Fuerzas planes de Subterránea | *"At level 25, unlock Kurast Undercity War Plans… gamble 2/3 of the War Plans to be Undercity to rush the Jade Epiphany upgrade"* — [Maxroll](https://maxroll.gg/d4/meta/alt-leveling-guide) |
| **25–70** | Con **Jade Epiphany** dentro: alternas **Oleadas Infernales** y **Ciudad Subterránea** hasta el máximo | *"Once Jade Epiphany unlocks, prioritize Helltide and Undercity warplans if possible, and continue blasting until max level"* — [Maxroll](https://maxroll.gg/d4/meta/alt-leveling-guide) |
| **~35** | Primera mazmorra de capitel (*Capstone*) | [d4builds](https://d4builds.gg/leveling-guide/) |
| **~60** | Segunda mazmorra de capitel | [d4builds](https://d4builds.gg/leveling-guide/) |
| **70** | **Penitente**. El Foso hasta nivel 10 → **Tormento I** → empieza el endgame | [d4builds](https://d4builds.gg/leveling-guide/) · [Maxroll — Difficulty](https://maxroll.gg/d4/resources/difficulty-overview) |

**Orden de prioridad de actividades**, según d4builds:
**Oleadas Infernales > Mazmorras de Pesadilla > El Foso > Ciudad Subterránea > Hordas Infernales** —
[d4builds](https://d4builds.gg/leveling-guide/).

Icy Veins matiza el final de esa lista: *"Focus Helltide first, then Undercity and Nightmare Dungeons.
Avoid Infernal Hordes"* — [Icy Veins — Fastest S14 Leveling Route](https://www.icy-veins.com/d4/news/fastest-diablo-4-season-14-leveling-route/).
Las dos fuentes coinciden en que **Hordas Infernales van al final**, aunque en 3.1.x su XP se dobló
(*"Horde experience therefore is outright doubled in Season 14"* —
[Icy Veins, 30/06/2026](https://www.icy-veins.com/d4/news/diablo-4-war-plans-get-faster-xp-but-the-biggest-fix-is-still-missing/)),
porque una Horda dura ~10 minutos frente a pocos minutos de las demás.

### 6.2 Por qué las Oleadas Infernales rinden más: el bucle del Hellwyrm

Este es el motor de XP de la S14 y conviene entenderlo, no solo copiarlo.

> *"One of the best sources of experience in the game is Helltides, so we will be aiming to spend a big
> portion of our time leveling there"* — [Icy Veins](https://www.icy-veins.com/d4/news/fastest-diablo-4-season-14-leveling-route/)

> *"Hellwyrms start spawning at Threat Level 2 during a Helltide and will drop XP globes when killed"*
> — [Icy Veins](https://www.icy-veins.com/d4/news/fastest-diablo-4-season-14-leveling-route/)

Y aquí está el mecanismo exacto, 🧪 leído en los tooltips reales del fichero de datos (versión
`3.1.0.72698`):

| Nodo (árbol de Oleadas Infernales) | Tooltip textual 🧪 |
|---|---|
| **Hellmouth** | *"When a Hellwyrm emerges, it unleashes one of the following: A Chaos Rift, which releases varied rewards upon collapse. **Maggots, which burst out Experience Orbs when slain.** Bloodseekers, which are more likely to drop Ance[stral]…"* |
| **Writhe and Rot** | *"**Hellwyrms will always spew Maggots** that gain +1 Monster Power. Sometimes, a Pang of Duriel will also crawl forth. **Lair Keys often burst out of Pangs of Duriel.**"* |
| **Undying Embers** | *"You lose no Aberrant Cinders on death."* |
| **Planar Tremors** | *"Hellwyrms will always open a Chaos Rift, and enemies that emerge from it gain +1 Monster Power…"* |

O sea: **Hellmouth** hace que el Hellwyrm *pueda* soltar gusanos que sueltan orbes de XP, y
**Writhe and Rot** hace que **siempre** los suelte. Los dos juntos convierten cada Hellwyrm en una
bolsa de experiencia. Maxroll lo resume así: Writhe and Rot *"provides us with insane experience gain
overall and extra Boss Lair keys"* — [Maxroll — War Plans, 05/08/2026](https://maxroll.gg/d4/resources/war-plans).

⚠️ **Discrepancia de nombre:** Maxroll y d4builds escriben **"Writhe and Rote"**; el fichero de datos
del juego dice 🧪 **"Writhe and Rot"** (sin la "e"). En el juego busca **"Writhe and Rot"**.

**Nota de 3.1.3 que te afecta:** *"Helltides quest now requires a flat Cinder spend amount rather than
a number of chests to be opened"* y *"Loot rewards from Helltide chests have been improved"* —
[Blizzard](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes). Las guías del
30/06 no lo reflejan.

### 6.3 El bucle alternativo: Ciudad Subterránea de Kurast

Para cuando no haya Oleada Infernal activa, o si el bucle del Hellwyrm no te divierte.

| Dato | Valor | Fuente |
|---|---|---|
| Requisitos de desbloqueo | **Vessel of Hatred** + **nivel 20** + invocar el Brasero Espiritual en Nahantu | [Icy Veins — Kurast Undercity](https://www.icy-veins.com/d4/guides/kurast-undercity-guide/) |
| Una vez desbloqueada | *"all your alt characters will have access to this activity right from level 1"* | [Icy Veins](https://www.icy-veins.com/d4/guides/kurast-undercity-guide/) |
| Temporizador | *"100 seconds on the three floors to gather Attunement"* | [Icy Veins](https://www.icy-veins.com/d4/guides/kurast-undercity-guide/) |
| Condición de éxito | *"you need to achieve at least Level 1 Attunement before entering the boss room"* | [Icy Veins](https://www.icy-veins.com/d4/guides/kurast-undercity-guide/) |
| Por qué da XP | *"Running Kurast Undercity is an excellent method for leveling, thanks to the high amount of elites that provide bonus experience"* | [Icy Veins](https://www.icy-veins.com/d4/guides/kurast-undercity-guide/) |
| Nodo clave | **Jade Epiphany** 🧪: *"When you gain an Attunement level in the Undercity, Experience Orbs appear around you. All enemies within the Undercity have +1 Monster Power."* | Datamining `data.min.json` v3.1.0.72698 · descrito también en [Maxroll — War Plans](https://maxroll.gg/d4/resources/war-plans) como *"provides us with some decent experience"* |
| Ventaja de escalado | *"Jade Epiphany scales with difficulty, meaning you can do a higher difficulty and still level faster"* | [Maxroll — Speed Leveling](https://maxroll.gg/d4/meta/alt-leveling-guide) |
| Alternativa declarada | *"If uninterested in Helltides, spam Undercity runs after unlocking Jade Epiphany"* | [d4builds](https://d4builds.gg/leveling-guide/) |

### 6.4 Mazmorras de Pesadilla: cómo hacerlas sin perder tiempo

- **No las limpies enteras**: *"Clear approximately 80% of monsters rather than full completion"* —
  [Maxroll — Speed Leveling](https://maxroll.gg/d4/meta/alt-leveling-guide).
- **Prioriza los eventos**: *"Prioritize Cursed Chest and Cursed Shrine events (grant absurd amounts
  of Experience)"* — [Maxroll](https://maxroll.gg/d4/meta/alt-leveling-guide).
- **Recoge solo Raro/Legendario** — [Maxroll](https://maxroll.gg/d4/meta/alt-leveling-guide).
- **Sinergia con el Rango de Temporada:** el 3.1.3 hizo que *"The Season Rank III objective Set Fire to
  the Beacons will now count Escalation Nightmare Dungeons with the Ruptures affix toward completion"*
  — [Blizzard](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes). Si eliges
  Mazmorras de Pesadilla con el afijo **Rupture**, avanzas dos cosas a la vez.

### 6.5 Ruta si NO tienes las campañas hechas (escenario A — el tuyo, probablemente)

**No existe guía publicada para esto.** Lo construyo yo, y lo digo: es **síntesis mía**, no una ruta
citada de una fuente. Cada pieza sí está citada.

| Paso | Qué | Por qué |
|---|---|---|
| 0 | Reinicia el juego tras comprar, para que se apliquen las expansiones | Práctica estándar; el material previo de este proyecto lo documenta contra [la página de LoH de Blizzard](https://diablo4.blizzard.com/en-us/lord-of-hatred) |
| 1 | **Con el NIGROMANTE de 70**: campaña de Vessel of Hatred | Abre Nahantu, Ciudad Subterránea (nivel 20+), mercenarios y Palabras Rúnicas para toda la cuenta |
| 2 | **Con el NIGROMANTE**: campaña de Lord of Hatred | Abre Skovos/Temis, **Planes de Guerra**, Talismán y Cubo Horádrico. Y habilita el **salto de campaña** para siempre |
| 3 | **Crea el Paladín** y márcale **saltar las tres campañas** | *"characters that skip either campaign automatically unlock all non-stronghold waypoints for their chosen region"* — [Maxroll — Speed Leveling](https://maxroll.gg/d4/meta/alt-leveling-guide); *"Skip the Lord of Hatred campaign if you want to have War Plans unlocked right away"* — misma fuente |
| 4 | Aplica la ruta de §6.1 tal cual | — |

**Variante si ya creaste el Paladín y no quieres empezar de nuevo:** súbelo en paralelo con Oleadas
Infernales + Mazmorras de Pesadilla (**ambas existen en el juego base y no necesitan campaña de
expansión**) mientras el Nigromante hace las campañas por la noche. Perderás el bucle de Planes de
Guerra durante la primera mitad de la subida. Con 4 semanas de temporada, sigue siendo viable.

---

## 7. ¿Cuánto se tarda de verdad?

**Declaración previa:** **ninguna** de las fuentes preferentes (Blizzard, Maxroll, Icy Veins) publica
un tiempo 1→70. Lo he buscado en las cuatro guías de leveling que abrí y no está. Los números que
circulan vienen de **sitios de venta de oro y servicios de boosting**, que tienen interés comercial en
que el número parezca pequeño. Los doy **etiquetados**, no como dato:

| Cifra que circula | Fuente | Calidad |
|---|---|---|
| *"Level 70 in around one hour"* | [mmoexp](https://www.mmoexp.com/News/diablo-4-season-14-guide-fastest-level-70-in-1-hour-with-two-broken-methods.html) | 🔴 Sitio de venta de oro |
| *"under 2 hours"* | [leprestore](https://leprestore.com/guides/diablo-4/diablo-4-season-14-fastest-leveling-guide-reach-70-in-under-2-hours/) | 🔴 Sitio de boosting |
| *"roughly two to four hours"* | [d4gold](https://d4gold.com/news/diablo-4-season-14-leveling-guide-hit-level-70-4-hours-no-campaign-required) | 🔴 Sitio de venta de oro |
| *"2 hours 52 minutes"* (Barbarian Whirlwind, self-found, sin temple ni encantamiento) | ⚠️ **declarado como PTR** por la propia fuente | 🔴 Sitio de boosting **y** PTR |

**Todas** esas cifras asumen: campaña saltada, jugador experto, Planes de Guerra rodados y, en varios
casos, grupo. **Ninguna describe tu caso.**

**Mi estimación razonada** (y la marco como estimación, no como dato con fuente):

| Escenario | Estimación 1→70 | Razonamiento |
|---|---|---|
| Escenario C (campañas hechas, salto activo, ruta §6.1, principiante) | **6–10 h** | Multiplica por 3–4 las cifras de speedrun: un principiante ni rutea óptimo ni encadena Planes de Guerra |
| Escenario C, en dúo | **5–9 h** | El +10% de XP de grupo es pequeño; lo que ayuda es matar más rápido, no el bonus |
| Escenario A con "la jugada del Nigromante" | **+8–20 h de campañas** (Nigromante) **+ 6–10 h** (Paladín) | La horquilla de campaña viene de fuentes no preferentes; ver §3 |
| Escenario A subiendo el Paladín sin Planes de Guerra | **12–20 h** | Sin el bucle Hellwyrm ni Jade Epiphany pierdes el motor principal de XP |

**Con ~4 semanas de temporada por delante, incluso el peor escenario cabe de sobra.** Lo que no cabe
es hacer las campañas *dos veces*.

---

## 8. Planes de Guerra durante la subida: qué desbloquear y en qué orden

| Prioridad | Nodo | Árbol | Qué hace |
|---|---|---|---|
| 1 | **Writhe and Rot** | Oleadas Infernales | 🧪 *"Hellwyrms will always spew Maggots that gain +1 Monster Power…"* → orbes de XP garantizados. Maxroll: *"insane experience gain overall and extra Boss Lair keys"* ([Maxroll](https://maxroll.gg/d4/resources/war-plans)) |
| 2 | **Hellmouth** | Oleadas Infernales | 🧪 Es el nodo que introduce los gusanos que *"burst out Experience Orbs when slain"*. Icy Veins lo empareja con Writhe and Rot: *"Once unlocking the Hellmouth and Writhe and Rot nodes, our goal is to spawn and kill as many Hellwyrms as possible"* ([Icy Veins](https://www.icy-veins.com/d4/news/fastest-diablo-4-season-14-leveling-route/)) |
| 3 | **Jade Epiphany** | Ciudad Subterránea | 🧪 *"When you gain an Attunement level in the Undercity, Experience Orbs appear around you."* Se abre desde nivel **25** ([Maxroll](https://maxroll.gg/d4/meta/alt-leveling-guide)) |
| 4 | **Undying Embers** | Oleadas Infernales | 🧪 *"You lose no Aberrant Cinders on death."* Red de seguridad para principiante: mueres y no pierdes la sesión |

**Cómo se "pesca" un plan:** el consejo textual de Maxroll es *"gamble 2/3 of the War Plans to be
Undercity to rush the Jade Epiphany upgrade"* — [Maxroll](https://maxroll.gg/d4/meta/alt-leveling-guide).
Es decir: **rerolleas el plan hasta que salgan las actividades que te interesan.**

**Puertas internas que debes conocer** (del material previo de este proyecto, contra
[Maxroll — War Plans](https://maxroll.gg/d4/resources/war-plans)): el árbol de **Jefe de Guarida**
requiere **Tormento 1+**; el árbol de **El Foso** requiere **Rango de Temporada 2**; los nodos de
**Jefe de Guarida Mayor** requieren **Tormento 6+**. Nada de eso te bloquea la subida a 70.

**Rangos:** del **0 al 10** — [Maxroll](https://maxroll.gg/d4/resources/war-plans).
**Actividades por plan:** hasta **5**; en personaje nuevo el camino solo pide **2** antes de poder
reclamar — [Icy Veins](https://www.icy-veins.com/d4/guides/war-plans-overview/).

---

## 9. El dúo: tú con Paladín + expansiones, ella con Nigromante SIN expansiones

Esta es la parte con más aristas y la que más te va a condicionar el día a día.

### 9.1 Qué NO puede hacer ella

De [Icy Veins — Do You Need Lord of Hatred to Stay Competitive, 28/04/2026](https://www.icy-veins.com/d4/news/do-you-need-lord-of-hatred-to-stay-competitive-in-diablo-4/):

| Bloqueado sin Lord of Hatred |
|---|
| Clases **Paladín** y **Brujo (*Warlock*)** |
| Región **Skovos** (y por tanto **Temis**) |
| *"The continuation of the main campaign"* |
| Actividad de endgame **Echoing Hatred** |
| **Planes de Guerra** |
| *"20+ additional transformative Skill choices exclusive to expansion owners"* |
| Sistema de **Talismán y Amuletos (*Charms*)** |
| **Cubo Horádrico** |

Y sin **Vessel of Hatred**, además: **Nahantu**, **Ciudad Subterránea de Kurast**, **mercenarios** y
**Palabras Rúnicas** (documentado en el material previo de este proyecto y en la cobertura general de
VoH; la Ciudad Subterránea exige VoH de forma explícita —
[Icy Veins](https://www.icy-veins.com/d4/guides/kurast-undercity-guide/)).

### 9.2 Qué SÍ puede hacer ella

| Sí puede | Evidencia |
|---|---|
| **Llegar a nivel 70** | *"The level cap increases to 70 for everyone, not just expansion owners"* — [Icy Veins, 28/04/2026](https://www.icy-veins.com/d4/news/do-you-need-lord-of-hatred-to-stay-competitive-in-diablo-4/) |
| **Todo el rework de árbol de habilidades** | *"A full Skill Tree rework for all eight classes"* + *"over 80 additional options per class"* — [Icy Veins](https://www.icy-veins.com/d4/news/do-you-need-lord-of-hatred-to-stay-competitive-in-diablo-4/) |
| **La mecánica estacional entera** | La misión *"A Gospel of Despair"* arranca **en Kyovashad**, ciudad del juego base — [Blizzard](https://news.blizzard.com/en-us/article/24268702/hunt-the-death-cult-in-season-of-death-awakening) |
| **Oleadas Infernales, Mazmorras de Pesadilla, El Foso, Hordas Infernales, Susurros** | Contenido de juego base |
| **~85% del Rango de Temporada** | *"About 15% of the objectives require Lord of Hatred"* — [Blizzard](https://news.blizzard.com/en-us/article/24268702/hunt-the-death-cult-in-season-of-death-awakening) |

**Conclusión operativa:** vuestro **terreno común es Oleadas Infernales + Mazmorras de Pesadilla +
Rupturas del mundo abierto**. Y da la casualidad de que **ese es exactamente el mejor bucle de XP de la
temporada** (§6.1–6.2). El dúo **no os frena para subir a 70**; os frena para el endgame de expansión.

### 9.3 Lo que sí rompe el dúo, en concreto

| Actividad | ¿Podéis juntos? |
|---|---|
| Oleadas Infernales (zonas base) | ✅ Sí |
| Mazmorras de Pesadilla | ✅ Sí |
| Rupturas de Pandemonio (mecánica S14) | ✅ Sí |
| El Foso, Hordas Infernales, Susurros | ✅ Sí |
| **Ciudad Subterránea de Kurast** | ❌ Ella no tiene VoH |
| **Planes de Guerra** | ❌ Ella no tiene LoH; **el plan se inicia en Temis (Skovos)**, zona a la que no puede entrar — [Maxroll](https://maxroll.gg/d4/resources/war-plans) |
| **Cualquier cosa en Nahantu o Skovos** | ❌ |
| **Solo Self-Found** | ❌ SSF prohíbe grupo y comercio (documentado en el material previo de este proyecto) |

**Consecuencia práctica y honesta:** tu mejor ruta de XP individual (Planes de Guerra + Ciudad
Subterránea) **es contenido que ella no puede tocar**. Vas a tener que partir las sesiones:
**contigo solo** para Planes de Guerra y Ciudad Subterránea, **en dúo** para Oleadas Infernales,
Mazmorras de Pesadilla y Rupturas.

### 9.4 Planes de Guerra en grupo (para cuando ella sí tenga las expansiones)

El parche vivo lo confirma: *"Parties can now generate fully shared War Plans boards that have
completely synchronized progression and objectives"* —
[Blizzard, 3.1.3 y anteriores](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes).

Detalle de funcionamiento — ⚠️ **cuidado, esta parte la encontré descrita en artículos de Icy Veins
etiquetados como PTR de la S14**, no en una página de parche vivo:
*"When all party members are in Temis, a New Plan prompt will appear, costing 2 Marks of El'druin,
which all party members can vote on"* y *"Plans are synced regardless of War Plan Level or other States
(Torment Level, Campaign Completion etc.)"* — ⚠️ [Icy Veins — S14 PTR Changes How Parties Use War Plans](https://www.icy-veins.com/d4/news/diablo-4-season-14-ptr-changes-how-parties-use-war-plans/).
**El mecanismo existe en vivo** (lo dice Blizzard); **el coste exacto de 2 Marcas de El'Druin y la
mecánica de votación vienen de material de PTR** y podrían haber cambiado.

### 9.5 Mercenarios en grupo

| Dato | Estado |
|---|---|
| **Contratado (*Hired*)** *"fights alongside you constantly and has a fully fleshed-out skill tree with skills and passives"* | ⚠️ [Maxroll — Mercenaries, **11/07/2025**, S6/2.0](https://maxroll.gg/d4/resources/mercenaries-overview) |
| **Refuerzo (*Reinforcement*)** *"abbreviated skill tree and comes in tag-team style on command"*, *"will only use the base version of their skills and will not be affected by their passives"* | ⚠️ [Maxroll, 11/07/2025](https://maxroll.gg/d4/resources/mercenaries-overview) |
| *"you can only hire one Mercenary to join you at a time, solo or in a party (via the Party Leader)"* | ⚠️ [Maxroll, 11/07/2025](https://maxroll.gg/d4/resources/mercenaries-overview) |
| **"El Contratado no aparece en grupo, solo el Refuerzo"** | 🟡 **No confirmado en ninguna página fechada en 3.1.x.** Ver "No encontrado" |

**Lo que sí puedo decirte con seguridad:** las cuatro guías de leveling de Paladín que abrí recomiendan
**siempre una pareja Contratado + Refuerzo**, y **tres de las cuatro ponen a Aldkin de Refuerzo**:

| Build | Contratado | Refuerzo | Fuente |
|---|---|---|---|
| Shield of Retribution | **Varyana** | **Aldkin** (Field of Languish, reducción de daño) | [Maxroll](https://maxroll.gg/d4/build-guides/shield-of-retribution-paladin-leveling-guide) |
| Judgement | **Varyana** (Hysteria = velocidad de ataque; Taste of Flesh = curación) | **Aldkin** | [Maxroll](https://maxroll.gg/d4/build-guides/judgement-paladin-leveling-guide) |
| Blessed Hammer | **Raheir** el Portaescudos | **Varyana** | [Icy Veins](https://www.icy-veins.com/d4/guides/blessed-hammer-paladin-leveling-build/) |
| Divine Lance | **Raheir** (Ground Slam + Bastion) | **Varyana** (Bloodthirst) | [Icy Veins](https://www.icy-veins.com/d4/guides/divine-lance-paladin-leveling-build/) |
| **Shield Charge (endgame, tu objetivo)** | **Raheir** — *"grants you Bastion and Inspiration to buff your damage"* | **Aldkin** — *"reduces enemy damage and slows with Field of Languish"* | [Maxroll, 25/07/2026](https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide) |

**Consejo con criterio, no con fuente:** como acabas en Shield Charge con **Raheir + Aldkin**, y como
la afinidad (*Rapport*) se gana jugando, **empieza a subir Raheir y Aldkin desde el principio** aunque
la guía de subida prefiera Varyana. Evitas duplicar el farmeo de afinidad. Lo marco como criterio mío.

**Y si el "Contratado no aparece en grupo" es cierto** (el brief lo da por bueno): en las sesiones de
dúo, tu Contratado no está, así que **la mitad de tu tiempo de juego el Refuerzo es lo único que
tienes**. Eso refuerza priorizar **Aldkin de Refuerzo** cuanto antes: reducción de daño es lo que más
te salva siendo principiante.

---

## 10. La mecánica estacional mientras subes

| Dato | Valor | Fuente |
|---|---|---|
| Mecánica | **Rupturas de Pandemonio (*Pandemonium Ruptures*)** | [Maxroll — Season Guide, 13/07/2026, patch 3.1.0](https://maxroll.gg/d4/resources/season-guide) |
| Dónde aparecen | *"Ruptures can appear throughout Sanctuary but are more frequent in Helltide Zones"* | [Maxroll](https://maxroll.gg/d4/resources/season-guide) |
| Cómo empieza | *"travel to Kyovashad on the Seasonal Realm and read the ominous scroll"* → misión **"A Gospel of Despair"** | [Blizzard](https://news.blizzard.com/en-us/article/24268702/hunt-the-death-cult-in-season-of-death-awakening) |
| Ajuste de leveling | Redujeron *"mob density and Elite spawning on Normal difficulty"* porque estaban *"overtuned for early leveling in PTR"* ⚠️ | [Maxroll](https://maxroll.gg/d4/resources/season-guide) |
| Moneda | Cerrar Rupturas da **Glints of Hope**, canjeables en el tablero de reputación de **Zarbinzet** | [Maxroll](https://maxroll.gg/d4/resources/season-guide) |
| Premios del Rango de Temporada | *"Up to 12 skill points"*, *"up to 42 paragon points"*, *"7 resplendent sparks"*, *"5 mythic unique caches"* | [Blizzard](https://news.blizzard.com/en-us/article/24268702/hunt-the-death-cult-in-season-of-death-awakening) |

**Lo importante para ti:** las Rupturas son **más frecuentes en zonas de Oleada Infernal**, o sea que
**se solapan gratis con tu bucle de XP**. Y el Rango de Temporada, al ser de cuenta, **ya lo tienes
parcialmente hecho** por el Nigromante: hasta **12 puntos de habilidad y 42 de Paragón** que tu
Paladín cobra sin volver a currárselos (§2).

---

## 11. Errores que te van a costar horas

1. **Seguir la guía de leveling de Shield Charge.** Está congelada en el 24/04/2026, antes de que la
   clase existiese en vivo (§4.4).
2. **Hacer las campañas con el Paladín de nivel 1 en vez de con el Nigromante de 70.** Es el mismo
   trabajo a un tercio de velocidad, y el desbloqueo es de cuenta (§3).
3. **Esperar que los Planes de Guerra del Nigromante sirvan al Paladín.** No sirven: son por personaje
   en S14 y Blizzard confirmó que no lo cambian esta temporada (§2).
4. **Limpiar mazmorras al 100%.** *"Clear approximately 80% of monsters rather than full completion"* —
   [Maxroll](https://maxroll.gg/d4/meta/alt-leveling-guide).
5. **Quedarse en Normal "por seguridad".** Difícil da *"75% more Experience and Gold"*
   ([Maxroll](https://maxroll.gg/d4/meta/alt-leveling-guide)) y con un build S-tier que
   *"Can Ignore Items"* no lo vas a notar en dureza.
6. **Farmear objetos mientras subes.** Shield of Retribution está diseñada para ignorarlos:
   *"weapon damage is actually irrelevant because everything scales off Thorns"* —
   [Maxroll](https://maxroll.gg/d4/build-guides/shield-of-retribution-paladin-leveling-guide).
7. **Priorizar Hordas Infernales.** *"Avoid Infernal Hordes"* durante la subida —
   [Icy Veins](https://www.icy-veins.com/d4/news/fastest-diablo-4-season-14-leveling-route/).
8. **Separaros más de 90 metros en dúo.** El bonus de grupo es *"x10%"* y solo dentro de 90 m —
   [Maxroll — Multiplayer](https://maxroll.gg/d4/resources/multiplayer).
9. **Meteros los dos en mazmorras instanciadas para "ir más rápido".** En mazmorras *"the life and
   damage done by Monsters… scale up with the number of party members"*; en mundo abierto no —
   [Maxroll — Multiplayer](https://maxroll.gg/d4/resources/multiplayer). En dúo, **el mundo abierto es
   más eficiente**.

---

## 12. Plan de las próximas 4 semanas, condensado

| Semana | Objetivo |
|---|---|
| **1** | Nigromante: campaña de VoH → campaña de LoH. Comprobar en creación de personaje que aparecen los tres interruptores de salto |
| **1–2** | Crear/reencauzar el Paladín con **salto de campaña**. Subir 1→25 con **Shield of Retribution** en **Difícil**, pescando Planes de Guerra de Oleada Infernal hasta tener **Writhe and Rot** + **Hellmouth** |
| **2** | Nivel 25: forzar planes de **Ciudad Subterránea** hasta **Jade Epiphany**. Alternar Oleadas ↔ Subterránea hasta 70 |
| **2–3** | A 70: **Penitente**, El Foso hasta nivel **10** → **Tormento I**. Reespecializar a **Shield Charge** siguiendo [la guía de endgame](https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide) |
| **3–4** | Míticos en el orden que dice Maxroll: **Mantle of the Grey → Tibault's Will → Herald of Zakarum** ([Maxroll, 25/07/2026](https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide)) |

**Sesiones de dúo**, en paralelo, en cualquier momento: Oleadas Infernales en zonas base + Mazmorras de
Pesadilla + Rupturas. A menos de 90 m. Sin meterse en Nahantu ni Skovos.

---

## Fuentes

Páginas **abiertas de verdad** durante esta investigación. Marco entre corchetes el estado.

**Oficiales (Blizzard)**
1. https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes — [abierta] Notas de parche, cubre **3.1.3 build 73224, 12/08/2026**
2. https://news.blizzard.com/en-us/article/24268702/hunt-the-death-cult-in-season-of-death-awakening — [abierta] Anuncio de la Season 14

**Maxroll**
3. https://maxroll.gg/d4/tierlists/paladin-leveling-tier-list — [abierta] 30/06/2026
4. https://maxroll.gg/d4/build-guides/shield-of-retribution-paladin-leveling-guide — [abierta, 2 veces] 29/06/2026
5. https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide — [abierta] 25/07/2026, endgame
6. https://maxroll.gg/d4/build-guides/shield-charge-paladin-leveling-guide — [abierta] ⚠️ **24/04/2026, "Season 12"**
7. https://maxroll.gg/d4/build-guides/judgement-paladin-leveling-guide — [abierta] 30/06/2026
8. https://maxroll.gg/d4/meta/alt-leveling-guide — [abierta] 30/06/2026, Speed Leveling
9. https://maxroll.gg/d4/resources/war-plans — [abierta] 05/08/2026
10. https://maxroll.gg/d4/resources/multiplayer — [abierta] 26/06/2026
11. https://maxroll.gg/d4/resources/difficulty-overview — [abierta] 26/06/2026
12. https://maxroll.gg/d4/resources/experience — [abierta] 21/07/2026
13. https://maxroll.gg/d4/resources/season-guide — [abierta] 13/07/2026, patch 3.1.0
14. https://maxroll.gg/d4/resources/mercenaries-overview — [abierta] ⚠️ **11/07/2025, S6/2.0**
15. https://maxroll.gg/d4/news/lord-of-hatred-3-1-2-patch-notes — [abierta] 28/07/2026
16. https://maxroll.gg/d4/resources/difficulty-guide — [**404 Not Found**]

**Icy Veins**
17. https://www.icy-veins.com/d4/guides/paladin-leveling-guide/ — [abierta] 29/06/2026
18. https://www.icy-veins.com/d4/guides/blessed-hammer-paladin-leveling-build/ — [abierta] 29/06/2026
19. https://www.icy-veins.com/d4/guides/divine-lance-paladin-leveling-build/ — [abierta] 29/06/2026
20. https://www.icy-veins.com/d4/guides/season-rank/ — [abierta] sin fecha visible, referencia S14
21. https://www.icy-veins.com/d4/guides/war-plans-overview/ — [abierta] sin fecha visible
22. https://www.icy-veins.com/d4/guides/kurast-undercity-guide/ — [abierta] "Updated:" sin fecha, referencia S14 + VoH
23. https://www.icy-veins.com/d4/guides/helltide-guide/ — [abierta] sin fecha visible; ⚠️ **contiene terminología muerta ("World Tier Normal")**
24. https://www.icy-veins.com/d4/guides/diablo-4-new-season-checklist/ — [abierta] sin fecha visible, referencia S14
25. https://www.icy-veins.com/d4/news/fastest-diablo-4-season-14-leveling-route/ — [abierta] sin fecha visible
26. https://www.icy-veins.com/d4/news/diablo-4-war-plans-get-faster-xp-but-the-biggest-fix-is-still-missing/ — [abierta] 30/06/2026, **parche vivo**
27. https://www.icy-veins.com/d4/news/do-you-need-lord-of-hatred-to-stay-competitive-in-diablo-4/ — [abierta] 28/04/2026

**Otros**
28. https://d4builds.gg/leveling-guide/ — [abierta] sin fecha visible, referencia S14
29. https://www.wowhead.com/diablo-4/news/everything-first-time-paladin-players-should-know-in-diablo-4-379625 — [abierta pero **el cuerpo del artículo no vino en la respuesta**; solo cabecera. No cito nada de aquí]
30. https://mobalytics.gg/diablo-4/guides/warplans-guide — [**403 Forbidden**. No citado]

**Datamining**
31. https://assets-ng.maxroll.gg/d4-tools/game/data.min.json — [descargado, 12 MB] 🧪 campo `version` = **`3.1.0.72698`**. Usado para: tooltips de nodos de Planes de Guerra (Oleadas Infernales y Ciudad Subterránea) y lista de las 23 habilidades activas del Paladín

**Citadas de segunda mano, marcadas como tales en el texto**
32. https://www.sportskeeda.com/mmo/how-long-diablo-4-lord-hatred-take-beat — duración de campaña LoH (fuente no preferente)
33. https://www.tweaktown.com/news/111308/... — duración de campaña LoH (fuente no preferente)
34. https://www.icy-veins.com/d4/news/diablo-4-season-14-ptr-changes-how-parties-use-war-plans/ — ⚠️ **PTR**, coste de 2 Marcas de El'Druin
35. https://www.icy-veins.com/d4/guides/lord-of-hatred-overview/ — 24/04/2026, regla del salto de campaña (recogida del material previo de este proyecto)
36. https://www.icy-veins.com/d4/news/diablo-4-skip-campaign-unlocks-waypoints/ — santuarios al saltar campaña
37. https://www.wowhead.com/diablo-4/guide/gameplay/stash — alijo/oro/materiales compartidos (🟡 sin fecha visible)
38. Sitios de boosting/venta de oro citados **solo** para etiquetar cifras de tiempo: mmoexp, leprestore, d4gold

**Nota sobre Reddit:** el buscador de este agente **rechaza el dominio reddit.com**
(*"The following domains are not accessible to our user agent"*). **No hay ninguna cita de r/diablo4
en esta ficha**, pese a estar en la lista de fuentes a intentar.

---

## No encontrado

Cosas que la petición pedía o que serían útiles y **no he podido verificar por escrito**. No las relleno.

1. **Tabla nivel-a-nivel de gasto de puntos de habilidad del Paladín.** Ni Maxroll ni Icy Veins la
   sirven en texto: vive dentro del planificador interactivo embebido. Icy Veins dice *"Below is the
   recommended order for spending your points as you level up"* pero la tabla no está en el HTML.
   **Hay que abrir el planificador en el navegador.**
2. **Tiempo 1→70 en fuente preferente.** Ninguna de las cuatro guías de leveling ni Blizzard publican
   un número. Todas las cifras que circulan son de sitios comerciales de boosting/oro.
3. **Confirmación fechada en 3.1.x de que el mercenario Contratado desaparece en grupo.** La única
   página de Maxroll sobre mercenarios es de **11/07/2025**. La afirmación circula en foros y sitios
   secundarios, pero **no la he visto en una página preferente fechada en el parche vivo**.
4. **Si la afinidad (*Rapport*) de mercenarios es de cuenta o por personaje.** La página de Maxroll no
   lo dice y es de 2025.
5. **Si un Paladín YA CREADO recibe acceso a Planes de Guerra retroactivamente** cuando otro personaje
   de la cuenta completa la campaña de LoH. Icy Veins dice *"any future characters"*. No he encontrado
   nada sobre personajes preexistentes. **Es la incertidumbre que más te puede costar.**
6. **Números exactos de los cambios de Defiance Aura, Aegis y Seal of the Second Trumpet** en
   3.1.1–3.1.3. La página de Blizzard los lista pero el extractor no devolvió las cifras.
7. **A qué parche concreto pertenecen** los cambios de Judicator (*"8% stacking 10 times to 60%
   stacking once"*) y de Carga (*"100% Cap 1 speed to 50% Cap 1 and 50% Cap 2"*). Los vi en el agregado
   de notas, sin anclaje a versión.
8. **Bonus de XP exactos de Normal / Difícil / Experto / Penitente en la página de Difficulty Scaling
   de Maxroll** — esa página solo tabula los Tormentos. Los 75/125/175% vienen de la Speed Leveling Guide.
9. **XP total necesaria para 70 y curva por nivel.** La página de Experience de Maxroll (21/07/2026)
   **no la publica**, pese a llamarse así.
10. **Multiplicadores de Elixires, Inciensos y Profane Mindcage** durante la subida. No están en la
    página de Experience ni en la Speed Leveling Guide.
11. **Qué le pasa exactamente a un jugador sin expansión que está en grupo** cuando el otro se
    teletransporta a Nahantu o Skovos (¿se queda atrás? ¿le expulsa del grupo? ¿mensaje de error?).
    **Ninguna página fechada lo documenta.** Búsqueda específica en foros oficiales: sin resultados
    relevantes.
12. **Si las recompensas ya reclamadas del Rango de Temporada se pueden volver a reclamar** en el
    Paladín. Icy Veins confirma que el *progreso* es de cuenta, pero no aclara el detalle de reclamación.
13. **Cuántos objetivos concretos del Rango de Temporada requieren LoH.** Solo existe el agregado
    *"About 15%"*.
14. **Contenido de Mobalytics** (403) y **de Reddit** (dominio bloqueado para este agente). Dos de las
    fuentes que la petición pedía intentar quedan sin cubrir.
15. **Página de Paladín para principiantes de Wowhead**: la URL responde pero el cuerpo del artículo no
    llegó. No he podido extraer la explicación de Fe (*Faith*), Resolución (*Resolve*), Juramentos ni
    número de Auras simultáneas de una fuente fechada.
