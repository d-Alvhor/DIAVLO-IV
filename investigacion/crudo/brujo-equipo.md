# Equipo, Paragón y glifos del Brujo (3.2.1 — Temporada 15, "Legado del Infierno")

> **Momento de redacción: 15 de septiembre de 2026, ANTES de las 18:30 CEST.** La temporada no ha
> arrancado. **Cero leaderboards, cero builds probadas en vivo.** Todo lo de abajo sale de: notas
> oficiales 3.2.1 (12 sep), guías de Maxroll/Icy Veins con su fecha citada una a una, y el PTR 3.2.0.
> Cuando digo "esta build sigue viva" estoy razonando sobre texto de parche, no sobre una pantalla.

## Resumen (5 líneas)

1. **Solo UNA guía de Brujo del planeta está escrita para la S15:** *Blazing Scream Warlock* de Maxroll (14 sep 2026, changelog literal "Created for Season 15"). Las otras **catorce** guías de Brujo de Maxroll son de junio–agosto (S14 / parche 3.1.0) y **ninguna** menciona el 3.2.1. Icy Veins tiene **cero** guías de Brujo actualizadas.
2. La poda del 3.2.1 golpea **por objeto, no por clase**: los dos únicos que sostenían las builds A-tier (*Hands of the Worldbreaker* → Apocalipsis; *Jaula de la locura* → Lunático) están tocados, mientras que *Elegía*, *Homúnculo infernal*, *Guanteletes de Sheol*, *Mano de apoteosis* y *Escarpes del can infernal* suben fuerte.
3. **La "bajada" de Jaula de la locura NO es una bajada: es un rediseño** de multiplicador plano a multiplicador por segundo. 300-340 % fijo → 100-200 % **por cada segundo** transformado (hasta 15 s). Nadie ha publicado el neto.
4. Paragón: glifo **nuevo Superiority** (30 % a nodos mágicos + 10 % RD), *Occultist* 12→15 %, *Control* reescrito, y el nodo legendario **Dynamism reparte poder de Forma Demoníaca hacia los esbirros** (+85 % daño de invocación fuera de Forma Demoníaca). Máximo de glifo **150**; los saltos que importan son **50** (radio 5) y **51** (se vuelve Legendario).
5. Astilla del Mal: **Mefisto es la única que modifica la Falla** (oficial). Diablo es fuego, que es el color del Brujo, pero modifica Oleada Infernal/Hordas. Mi recomendación —**inferencia mía, no dato**— es Diablo hasta 70 y luego cambiar a Mefisto en una Pesadilla de Vigilia grande para el empujón.

---

## Hallazgos

### A. Estado de las fuentes: qué guía está viva y cuál está caducada

Esto va primero porque **condiciona todo lo demás**. La fecha la he leído en cada página.

| Guía | Última act. | Temporada que declara | ¿Menciona 3.2.1? | URL |
|---|---|---|---|---|
| **Blazing Scream Warlock Endgame** (Maxroll) | **14 sep 2026** | **Season 15 – Hell's Legacy** | Changelog: *"Created for Season 15"* | https://maxroll.gg/d4/build-guides/blazing-scream-warlock-guide |
| Lunatic Warlock Endgame (Maxroll) | 4 ago 2026 | Season 14 – Death Awakening | No | https://maxroll.gg/d4/build-guides/lunatic-warlock-guide |
| Minion Warlock Leveling (Maxroll) | 17 jul 2026 | Season 14 | No | https://maxroll.gg/d4/build-guides/minion-warlock-leveling-guide |
| Minion Warlock Endgame (Maxroll) | 13 jul 2026 | Season 14 | No | https://maxroll.gg/d4/build-guides/minion-warlock-guide |
| Hell Fracture Warlock Endgame (Maxroll) | 11 jul 2026 | Season 14 | No | https://maxroll.gg/d4/build-guides/hell-fracture-warlock-guide |
| Tyrant's Grasp / Dread Claws / Eviscerate / **Apocalypse** Endgame (Maxroll) | **30 jun 2026** | Season 14 (parche 3.1.0) | **No** | https://maxroll.gg/d4/build-guides/apocalypse-warlock-guide |
| Abyss Rampage Endgame (Icy Veins) | 26 jun 2026 | Season 14 | No | https://www.icy-veins.com/d4/guides/abyss-rampage-endgame-warlock-build/ |
| Hub de builds de Brujo (Icy Veins) | sin fecha legible | sin temporada declarada | No | https://www.icy-veins.com/d4/warlock/builds/ |

**Evidencia: corroborado** (fecha y cabecera de temporada leídas en cada página, 15 sep 2026).

**La trampa concreta de este dominio:** la guía de **Apocalypse** de Maxroll —la build estrella del PTR— sigue diciendo *"Season 14 - Death Awakening, Last Updated: June 30, 2026"* y su prioridad de míticos empieza por **Hands of the Worldbreaker**, el objeto que el 3.2.1 ha recortado. Está escrita **antes de que existieran las notas**. Si la abres hoy, te da la build vieja sin un solo aviso.

**Tier lists — ojo con cuál lees:**

| Tier list | Fecha | Temporada | Brujo |
|---|---|---|---|
| **Overall Endgame Tier List** (Maxroll) | **14 sep 2026** | **Season 15** | **A**: Minion, Apocalypse, Lunatic · **B**: Hell Fracture, Blazing Scream · **C**: Tyrant's Grasp, Dread Claws, Eviscerate |
| Warlock Endgame Builds Tier List (Maxroll) | 29 jun 2026 | Season 14 | B: Lunatic, Apocalypse, Minion, Hell Fracture · C: Dread Claws, Tyrant's Grasp, Blazing Scream, Eviscerate |
| Warlock Push Builds Tier List (Maxroll) | 7 jul 2026 | Season 14 | A: Lunatic, Apocalypse, Blazing Scream, Dread Claws · B: Minion, Tyrant's Grasp, Hell Fracture, Eviscerate |

- Overall S15: https://maxroll.gg/d4/tierlists/endgame-tier-list — **14 sep 2026** — **unica** (una sola fuente, y no cita el 3.2.1 en ningún sitio).
- Las dos listas **específicas de Brujo siguen en S14** y no sirven para esta temporada: https://maxroll.gg/d4/tierlists/warlock-endgame-builds-tier-list (29 jun) y https://maxroll.gg/d4/tierlists/warlock-push-builds-tier-list (7 jul) — **corroborado** (fechas leídas).
- **El Brujo no tiene ni una build en S** en la única lista fechada dentro del parche. Encaja con la poda.

---

### B. Veredicto build por build: ¿sigue viva tras el 3.2.1?

Cada veredicto sale de cruzar **el objeto núcleo de la build** (leído en su guía) contra **la línea de las notas oficiales** (leída en el parche). El veredicto en sí es **razonamiento mío**, marcado como tal.

| Build | Objeto núcleo | Qué le hace el 3.2.1 | Veredicto (inferencia mía) |
|---|---|---|---|
| **Apocalipsis** (A-tier) | *Hands of the Worldbreaker* (mítico nº 1 de su guía) | *"Apocalypse damage bonus **reduced to 290%-350%**."* — **oficial** | **Tocada donde duele.** Es el multiplicador que la sostiene. **No se puede cuantificar el daño**: Blizzard publica el "a" y no el "de" (ver Huecos H1). |
| **Lunático** (A-tier) | *Jaula de la locura* (mítico nº 1; la guía la llama *"the key item"*) | Plano 300-340 % → **100-200 % por segundo** transformado, hasta 15 s; y la explosión pasa a *"Command Fallen's **Base** damage"* — **oficial** | **Rediseñada, no podada.** A partir de ~2-3 s transformado el nuevo texto supera al viejo; la explosión sí pierde. **Neto no publicado por nadie.** |
| **Esbirros / Minion** (A-tier) | *Ae'grom's Schism*, *Eye of Baal*, *Seed of Horazon*, *Crown of Lucion*, *Bindings of Attrition* | **Ningún nerf a sus núcleos.** Y encima: *Bindings of Attrition* **"Life Cost now scales down from 48%-27%"**; nodo **Dynamism** *"now also grants **85% increased Summon Skill damage while not in Demonform**"*; *Aspect of Authority* +15 % daño de Gran Demonio; *Ominous Aspect* rehecho a 15-19 % → 75-95 % daño de Gran Demonio — **oficial** | **La menos dañada, y probablemente buffeada.** Es la única A-tier cuyo núcleo no toca el parche. |
| **Blazing Scream / Grito llameante** (B-tier) | *Elegía*, *Homúnculo infernal*, *Moloch's Beating Flame* | *Elegy*: pasa a ser **habilidad Archifiend** y 20-30 % → **30-50 %**; *Infernal Homunculus*: 50-70 % → **80-110 %** y ahora **cualquier** lanzamiento Archifiend activa las mejoras; *The Eightfold Idol* rehecho — **oficial** | **Viva y subida.** Y es la **única** con guía escrita para la S15. La sinergia Elegía+Homúnculo es explícita en el texto nuevo. |
| **Abaddon / Fiend of Abaddon** (sin guía en Maxroll) | *Guanteletes de Sheol* | 23-33 %[x] por demonio → **40-50 % por demonio, tope 600-750 % durante 60 s**, y ya no hay que resumonear: *"While Fiend of Abaddon is alive, you **periodically** sacrifice…"* — **oficial** | **La subida más grande del parche en el Brujo, y nadie tiene guía.** Icy Veins tiene *Abaddon Summoner* pero en S14. Oportunidad, no plan. |
| **Metamorfosis / Demonform** | *Mano de apoteosis* | 30-50 % → **50-100 %**, y ahora *"**Any** Demonform grants you all Metamorphosis Upgrades for free"* — **oficial**. Contrapeso: **Dynamism** baja el daño por Dominance en Forma Demoníaca **3 % → 2,5 %** | **Mezcla deliberada:** el objeto sube, el nodo de paragón traslada poder a los esbirros. Es la "redistribución de Demonform" que anuncia el dev. |

Fuente de todas las líneas de parche de esta tabla: [Blizzard — notas 3.2.1, sección Warlock](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy), 12 sep 2026 — **oficial**. Corroboración literal del "antes/después" de *Jaula de la locura* (300-340 % → 100-200 %) y *Bridle of Tor'baalos* en [Maxroll — 3.2.1 Patch Notes](https://maxroll.gg/d4/news/diablo-4-3-2-1-patch-notes), 12 sep 2026 — **corroborado**.

---

### C. Únicos del Brujo hueco por hueco, con el texto nuevo del 3.2.1

Todos estos textos son **oficiales** y están leídos en [las notas 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) (12 sep 2026). El nombre ES sale de las notas en español del **RPP 3.2.0** ([es-es, 30 jul 2026](https://news.blizzard.com/es-es/article/24292852/el-rpp-3-2-0-todo-lo-que-necesitas-saber)) o del **3.0** ([es-es](https://news.blizzard.com/es-es/article/24271857/notas-del-parche-de-diablo-iv-3-0)) — **oficial para la nomenclatura**. Donde pone `[EN]` es que no he encontrado el español escrito.

| Ranura | Objeto (ES / EN) | Texto 3.2.1 (literal, abreviado) | Dirección |
|---|---|---|---|
| **Guantes** | **Mano de apoteosis** / *Hands of Apotheosis* | *"Any Demonform grants you all Metamorphosis Upgrades for free, and they are **50-100%** more potent."* (antes 30-50 %) | ▲ sube |
| **Guantes** | `[EN]` *Hands of the Worldbreaker* | *"Apocalypse damage bonus **reduced to 290%-350%**."* | ▼ baja |
| **Guantes** | **Guanteletes de Sheol** / *Gauntlets of Sheol* | *"While Fiend of Abaddon is alive, you periodically sacrifice all other Archfiend Summons… increasing Fiend of Abaddon's damage by **40-50% per demon killed, up to 600-750% for 60 seconds**."* | ▲▲ sube mucho |
| **Yelmo** | **Jaula de la locura** / *Cage of Madness* | *"…you gain **100-200% increased Command Fallen damage every second** you are transformed."* Explosión ahora a **daño base** | ↔ rediseño |
| **Yelmo** | **Capuz del tormento maléfico** / *Cowl of Malefic Torment* | *"Hex dooms enemies, maintaining the Hex and dealing **100-200% of Doom's damage** every second… Doom deals **140-175%** increased damage."* (antes 80-100 %) | ▲ sube |
| **Botas** | **Escarpes del can infernal** / *Hellhound's Sabatons* | *"Abodian deals **200-280%** increased damage. Command Abodian periodically triggers your Non-Archfiend Hellfire Skills while moving, and its Cooldown is reduced by 50%."* (antes 80-100 %[x]) | ▲▲ sube mucho |
| **Pecho** | **Homúnculo infernal** / *Infernal Homunculus* | *"Your Archfiend Skills deal **80-110%** increased damage, and casting **any** Archfiend Skill activates all their Lesser Demon Upgrades for free with 200% longer durations."* (antes 50-70 %[x]) | ▲ sube |
| `sin ranura publicada` | **Elegía** / *Elegy* | *"Blazing Scream is now an **Archfiend Skill** and deals **30-50%** increased damage… the Lesser Demon skulls deal the same damage as the main skull."* (antes 20-30 %[x]) | ▲ sube |
| `sin ranura publicada` | **La hematopiedra** / *The Hemat Stone* | *"Bonuses from Command Valloch and the Ritualist Shard and its Fragments have **200%** increased Potency. Your Occult Skills deal **40-60%** increased damage."* (antes 100 %[+] / 20-30 %[x]) | ▲ sube |
| `sin ranura publicada` | **El ídolo óctuple** / *The Eightfold Idol* | Ya no da 160-200 %[x] a Sigil; ahora *"You deal **60-80%** increased Abyss or Hellfire Skill damage to enemies on Sigil of Subversion trails"* | ↔ rediseño |
| `sin ranura publicada` | **Cetro de los Tres** / *Scepter of the Three* | *"Hitting enemies with Non-Ultimate Skills builds up your Ultimate Skill damage by **1.7-2.5%, up to 170-250%**."* (antes 4-5 %[x] hasta 80-100 %[x]) | ▲ sube el techo |
| `sin ranura publicada` | **Uñas del crúor coronado** / *Nails of the Gore-Crowned* | *"Hellion Sting deals **80-100%** increased damage and bursts out of enemies when you Eviscerate them. Hellion Sting gains **0.5-2.5% Eviscerate Chance** each second…"* | ▲ sube |
| `sin ranura publicada` | `[EN]` *Rictus of Terror* | *"Command Laalish is now an **Ultimate Skill** and deals 100-120% increased damage. Terror Realm lasts **50%** longer…"* (antes 100 % más) | ↔ rediseño |
| **Cinturón** | `[EN]` *Bindings of Attrition* | *"Life Cost now scales down from **48%-27%**."* | ▲ sube |
| `sin ranura publicada` | `[EN]` *Bridle of Tor'baalos* | *"Damage bonus increased from **120-160% to 160-200%**."* | ▲ sube |
| **Anillo** | `[EN]` *Hellbrand Signet* | *"Damage bonus increased to **100-130%**."* | ▲ sube |
| `sin ranura publicada` | `[EN]` *Night Terror* | *"Damage bonus increased to **9-12%**."* | ▲ sube |
| `sin ranura publicada` | `[EN]` *Sire of Sin* | *"Damage bonus increased to **120-130%**."* | ▲ sube |
| `sin ranura publicada` | `[EN]` *Thrice-Woven Nightmare* | *"Terror Swarm damage bonus increased to **60-100%**."* | ▲ sube |
| `sin ranura publicada` | `[EN]` *Sashes of the Wretched* | Taunt ahora **10-15 % más daño recibido y 10-15 % menos daño infligido, 20 s** (antes 8-10 %[x], 5 s) | ▲ sube |
| `sin ranura publicada` | `[EN]` *The Blade of Sight Aflame* | Explosión de demonio menor **400 % → 400-600 %** de un impacto de Bombardment | ▲ sube |
| **Pecho** | `[EN]` *Morlu Fleshward* | *"Maximum Life Reduction from this item will no longer constantly consume Fortify."* | ▲ arreglo |
| **Anillo** | `[EN]` *Lurid Pact* | *"Now considers the player to be the Brute and scales them up when using the Demonic Smash Variant."* | ▲ arreglo |

**Lectura importante sobre la notación:** varias de estas líneas **han perdido el `[x]`** al reescribirse (p. ej. *Homúnculo infernal* pasa de `50-70%[x]` a `80-110%` sin marca). En D4 `[x]` es multiplicativo y sin marca suele ser aditivo. **No afirmo que se hayan convertido en aditivos** —Blizzard es inconsistente escribiendo la notación en las notas— pero es exactamente el tipo de cambio de modelo que vale mucho más que las cifras. **Hay que mirarlo en el tooltip del juego.** Evidencia: **sinconfirmar**.

#### Míticos que piden las builds de Brujo (según sus guías)

| Build | Orden de míticos que publica su guía | Fecha de esa guía |
|---|---|---|
| **Grito llameante** (la de S15) | 1. *Moloch's Beating Flame* · 2. *Temerity* · 3. *Ring of Starless Skies* · 4. *Elegía* · 5. *Homúnculo infernal* · 6. *Crown of Lucion* | 14 sep 2026 — **unica**, pero dentro del parche |
| Lunático | 1. *Jaula de la locura* · 2. *Dirge of Odium* · 3. *Seed of Horazon* · 4. *Paingorger's Gauntlets* · 5. *Tibault's Will* | 4 ago 2026 — **caducada** |
| Esbirros | 1. *Ae'grom's Schism* · 2. *Eye of Baal* · 3. *Seed of Horazon* · 4. *Crown of Lucion* · 5. *Bindings of Attrition* | 13 jul 2026 — **caducada** |
| Apocalipsis | 1. *Hands of the Worldbreaker* · 2. *Fleshwrit Carapace* · 3. *Moloch's Beating Flame* · 4. *Ring of Starless Skies* | 30 jun 2026 — **caducada, y su nº 1 está nerfeado** |

URLs en la tabla A. **Evidencia: unica** para cada orden (una sola fuente por build).

#### Dijes / Talismán (Charms) — lo que cambia en 3.2.1 para el Brujo

| Dato | Detalle | Evidencia |
|---|---|---|
| Set del Brujo tocado | **Flesh of Abaddon's Set**: *"3-Piece Set Bonus: Increased to **20% Maximum Demonform Life** with an additional **0.55% Life per Demonic Strength**."* | **oficial** (notas 3.2.1) |
| **Ae'grom's Schism y Eye of Baal pasan a tener versión Dije** | Están entre los **16 únicos existentes** que ahora se craftean como Charm | **oficial** (notas 3.2.1, sección Talisman) |
| Dijes que la guía de S15 pone en el Grito llameante | *Phoba of Abaddon's Flesh*, *Anathema of the Primes*, *Phoba of the Nameless*, *Seal of the Diamond Mind*, *Fer of Slaughter* | **unica** ([Maxroll Blazing Scream](https://maxroll.gg/d4/build-guides/blazing-scream-warlock-guide), 14 sep) |
| Arreglo | *"Fixed an issue where Cauldron set stacks could reset erroneously."* | **oficial** |

**Lo que esto vale (inferencia mía):** que *Ae'grom's Schism* y *Eye of Baal* tengan versión Dije es, para el Brujo de esbirros, más relevante que media tabla de nerfs — son sus dos objetos obligatorios y ahora pueden ocupar dos ranuras distintas. Nadie ha publicado si el efecto se apila. **Hueco H5.**

---

### D. Afijos: qué buscar y en qué orden

**Dato de partida — stat principal:** el stat nuclear del Brujo es **Voluntad / Willpower**. Cita: *"Willpower is the main Core Stat for the Warlock, granting you bonus Skill Damage"* — [Maxroll — Warlock Class Overview](https://maxroll.gg/d4/getting-started/warlock-class-overview) — **unica** (Maxroll; la página no declara fecha legible). Esto **cierra el hueco** que dejaba abierto `s15-clases.md` línea 186. Recordatorio del parche: el Brujo **se queda en escalar 1.25**, no sube a 1.625 (Druida, Nigromante, Paladín, Hechicera sí) — **oficial por ausencia de línea**.

**Objetivos numéricos de la única guía escrita para la S15** (Grito llameante, Maxroll, 14 sep 2026) — cita literal de su sección *Important Stats*:

> "100% Attack Speed. 100% Critical Strike Chance. >10 Wrath Regeneration. Maximum Life Rolls on nearly every gear piece. 2x Temper of 'Lucky Hit Restore Resource'. >10,000 Fire Resistance"

**Evidencia: unica.** Ojo: una lectura previa de la misma página me devolvió *">70% Attack Speed, >60% Critical Strike Chance"* y la segunda devolvió *"100% / 100%"* — probablemente son los umbrales de **variante intermedia vs. endgame**. **No me fío de ninguno de los dos como cifra exacta; el orden de prioridad sí es sólido.** Ver Contradicción C3.

**Orden de prioridad de afijos por ranura.** No hay tabla por ranura en la guía de S15. La única tabla slot-a-slot que existe para Brujo es de **Icy Veins, Abyss Rampage, 26 jun 2026 (S14, caducada)** — la doy como *forma*, no como *verdad de esta temporada*:

| Ranura | Afijo principal (asterisco = prioridad de Maestría) | Secundarios | Templado |
|---|---|---|---|
| Yelmo | Recurso Máximo* | Vida Máx., Armadura Total, Voluntad | *Worldly Endurance* (Vida Máx.) |
| Pecho | Recurso Máximo*, Vida Máxima | Armadura Total, Voluntad | *Worldly Endurance* |
| Guantes | Multiplicador de Daño a Vulnerables* | Voluntad, Daño Crítico, Daño de Sombra | *Worldly Finesse* (Daño Crítico) |
| Pantalones | Voluntad* | Vida Máx., Armadura Total, Resistencias | *Worldly Endurance* |
| Botas | Voluntad*, Cargas de Evasión Máx.* | Rangos de la habilidad, Vida Máx. | *Natural Motion* (Vel. Movimiento) |
| Arma 2M | Recurso Máximo* | Daño de Arma, Prob. Crítico | *Worldly Destruction* (Prob. Crítico) |
| Amuleto | Multiplicador de Daño Crítico* | Daño a Vulnerables, Recurso Máx., Voluntad | *Worldly Finesse* |
| Anillo 1 | Multiplicador Crítico* | Voluntad, Daño a Vulnerables, Daño de Sombra | *Worldly Finesse* |
| Anillo 2 | Prob. Crítico* | — | *Worldly Finesse* |

Fuente: https://www.icy-veins.com/d4/guides/abyss-rampage-endgame-warlock-build/ — **26 jun 2026** — **unica y caducada**. La cito porque es la única estructura publicada; **los afijos concretos cambian con la build**.

**Regla de orden que sí aguanta el cambio de parche** (síntesis mía de las dos fuentes): `Voluntad` y `Vida Máxima` en casi todo → `multiplicadores` (Vulnerable / Crítico / elemento de tu build) en guantes, amuleto y anillos → `Prob. Crítico` y `Vel. Ataque` hasta el umbral de la build → `Recurso Máximo` si la build escala con recurso (Lunático lo hace, vía *Dirge of Odium* + *Seed of Horazon*) → defensas en las piezas defensivas.

---

### E. Templado (Tempering)

| Dato | Detalle | Evidencia |
|---|---|---|
| **Único cambio de sistema en 3.2.1** | *"Significantly increased the value of Single Resistance affixes on equipment, Charms, and Tempering recipes. **Single Resistance affixes are now 7 times the value of All Resistance affixes.** Re-tuned All Resistance Tempering values…"* | **oficial** ([notas 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy)) |
| Otro cambio | Un solo bug fix: *"Fixed an issue where Maximum Resolve Stacks was uncapped when Tempering."* Nada de cargas ni de recetas nuevas | **oficial** |
| Templado que pide la build de S15 | **"2x Temper of 'Lucky Hit Restore Resource'"** (2 templados de *Golpe de Suerte: Restaura Recurso*) | **unica** (Maxroll, 14 sep) |
| Maestría (Masterworking) | **Cero cambios en 3.2.1** | **oficial por ausencia** |

**Cómo se conectan las dos cosas (inferencia mía, no dato):** la misma guía pide **>10.000 de Resistencia al Fuego** y el parche acaba de multiplicar por **7** el valor de las recetas de resistencia **única**. La forma barata de llegar a esa cifra es templar **Resistencia al Fuego** concreta, no "a Todos los Elementos". Nadie lo ha escrito así en fuente preferente todavía.

---

### F. Paragón, tableros y glifos

#### Lo que cambia oficialmente en 3.2.1 (todo de las notas, 12 sep 2026 — **oficial**)

| Elemento | Texto literal |
|---|---|
| **Glifo NUEVO: Superiority** | *"Grants **+30% bonus to all magic Nodes within range**. Additional Bonus: You gain **10% Damage Reduction** and your Dominance Regeneration is increased by **2.0%** of your most recent Dominance spend. Legendary Bonus: Increase damage by **5.5%**."* |
| Glifo **Control** | *"Now grants **15%** increased damage to Slowed or Taunted enemies or instead deal **30%** increased damage to Tethered or Knocked Down enemies."* |
| Glifo **Occultist** | *"Additional bonus reworded and damage bonus increased from **12% to 15%**."* |
| Nodo legendario **Dynamism** | *"Now also grants **85% increased Summon Skill damage while not in Demonform**. Damage per Dominance while in Demonform reduced from **3% to 2.5%**."* |
| Nodo legendario **Dominion** | *"Wrath Cost Reduction now also applies to Core Archfiend Skills using Anathema of the Primes."* |

**Nota de traducción:** el 3.0 en español trae un *"Glifo: Poderío"*, pero **Superiority es glifo nuevo del 3.2.1** y no puede aparecer en un parche anterior. **No doy "Poderío" como traducción de Superiority.** Ver Contradicción C4.

#### Orden de glifos que publica la única guía de S15

**Grito llameante** (Maxroll, 14 sep 2026) — orden literal: **Superiority → Attrition → Unbound → Demonologist → Archfiend**.
Y la condición que da: *"Superiority and Attrition need to be **rank 50** to meet the Intelligence requirements on any board."* Progresión que recomienda: llegar primero a los **mínimos** de cada glifo, no maximizar; luego **50 → 100 → 150**. **Evidencia: unica.**

**Esbirros** (Maxroll, 13 jul 2026, **caducada**) — orden: **Unbound → Eliminator → Demonologist → Archfiend → Eldritch Sight**, con nota de que la variante de jefe cambia *Vanguard* por *Attrition*. **Evidencia: unica y caducada.**

#### A qué nivel subir los glifos

| Umbral | Qué pasa | Evidencia |
|---|---|---|
| **Nivel 15** | El radio pasa a **4** | **unica** — [Icy Veins — Paragon Glyphs](https://www.icy-veins.com/d4/guides/paragon-glyph-guide/), declara *Season 15*, **sin fecha legible en la página** |
| **Nivel 50** | El radio pasa a **5**. Es el umbral que la guía de S15 exige para *Superiority* y *Attrition* | **corroborado** (Icy Veins + Maxroll Blazing Scream) |
| **Nivel 51** | El glifo *"upgrade to **Legendary** and gain an additional effect"* — aquí es donde *Superiority* entrega su *Legendary Bonus: 5.5 % daño* | **corroborado** (Icy Veins + notas oficiales, que sí listan un "Legendary Bonus") |
| **Nivel 150** | **Máximo de glifo** | **unica** (Icy Veins) |
| Cómo se sube | *"If the pit is at least **10 levels above** the Glyph, it is **guaranteed** to level it up"*, con progreso extra *"For every **20 levels above** the Glyph that your pit is"* | **unica** (Icy Veins) |

**Plan de glifos que se deriva (inferencia mía):** 50 en *Superiority* y *Attrition* lo antes posible porque es **requisito estructural** de los tableros, no una mejora de daño; 51 en todo lo que se pueda para desbloquear el efecto Legendario; y a partir de ahí, la Falla a **+10 niveles por encima del glifo** como bomba de XP hacia 100/150. Esto además **encaja con el objetivo del jugador**: subir glifos y empujar la clasificación son la misma actividad.

#### Tableros

**No he encontrado los nombres de los tableros de Paragón del Brujo en ninguna fuente preferente.** Las dos lecturas de la guía de S15 me devolvieron la misma lista de cinco nombres pero etiquetada una vez como "glifos" y otra como "tableros"; los cinco (*Superiority, Attrition, Unbound, Demonologist, Archfiend*) son **glifos** —*Superiority* aparece como glifo en las notas oficiales—. **El orden de tableros del Brujo es un hueco (H3).**

---

### G. Astilla del Mal: cuál le conviene a un Brujo

**Los hechos oficiales** ([notas 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy), 12 sep 2026; corroborado por [Maxroll — Season Guide](https://maxroll.gg/d4/resources/season-guide), 13 sep 2026):

| Astilla | Poder Icónico | Actividades que modifica | Contrapartida |
|---|---|---|---|
| **Astilla del Terror de Diablo** | **Fuego** | Oleada Infernal + Hordas Infernales | Más vulnerable a Diablo |
| **Astilla de la Destrucción de Baal** | **Frío** | Ciudad Subterránea + Jefes de Guarida | Más vulnerable a Baal |
| **Astilla del Odio de Mefisto** | **Físico** | **El Foso (la Falla) + Mazmorras de Pesadilla** | Más vulnerable a Mefisto |

Las tres modifican además el Árbol de los Susurros. Cada vía tiene **8 modificadores de actividad + 6 mejoras del Poder Icónico**. Se cambia de astilla **en las Pesadillas de Vigilia grandes** — todo **oficial**.

**El razonamiento, que es mío y lo marco como tal:**

1. **Para el objetivo declarado (top 10 de la Falla), Mefisto es la única que toca la Falla.** Ocho modificadores de actividad aplicados a El Foso y la vía de reputación entera alimentada por la actividad que el jugador va a repetir de todas formas. **Esto es una consecuencia directa del texto oficial, no una opinión.**
2. **Pero el Brujo es una clase de fuego e infierno, y el Poder Icónico de Mefisto es físico.** Si el Poder Icónico escalase con los multiplicadores del personaje, Diablo (fuego) sería el que se beneficia del equipo del Brujo. **Nadie ha publicado si escala con los stats del jugador.** Lo he buscado en las notas oficiales y no está. **Hueco H2 — y es el que más cambia la respuesta.**
3. **La contrapartida es asimétrica y juega a favor de Diablo.** La build de S15 del Brujo ya pide **>10.000 de Resistencia al Fuego**; llevar la astilla de Diablo, que te hace más vulnerable **al fuego**, es la penalización más barata de absorber para esta clase en concreto. La de Mefisto (físico) no tiene ese colchón natural. **Ningún porcentaje publicado** (hueco H2 también).
4. **Recomendación práctica, condicionada:** **Diablo mientras subes a 70** —modifica Oleada Infernal y Hordas Infernales, que son las actividades de subir nivel y farmear, y su daño de fuego es el color de la clase— y **cambiar a Mefisto en una Pesadilla de Vigilia grande** cuando empiece el empujón de Falla. El cambio es oficialmente reversible, así que el coste de equivocarse es un viaje.
5. **Lo que NO digo:** no digo que Mefisto sea mejor ni peor en DPS. Digo que es la única que modifica la Falla y que el resto depende de un dato que no existe todavía.

**Aviso de nomenclatura que puede costar caro:** en la S15 hay **dos cosas distintas que se llaman "Splinter"**. Las **Astillas del Mal** (Diablo/Baal/Mefisto, mecánica de temporada) y las **Soul Splinters**, que son las **gemas** de temporada. Cuando la guía del Grito llameante recomienda *"Abyssal Splinter of the Black Soulstone"*, *"Abyssal Splinter of Anguish"* o *"Lesser Splinter of Hellfire"*, está hablando de **gemas**, no de la elección de Mal Supremo. Yo mismo lo leí mal en el primer pase.

**Dato de engarce que conecta las dos cosas:** **Corona de Leoric** *"counts as Jewelry and increases the effect of any gem socketed into the helm by **75-100%**"*, y el bug fix oficial *"Leoric's Crown did not apply Soul Splinter Effects"* confirma que **admite Soul Splinters**. Un yelmo que multiplica por ~2 el efecto de una gema de temporada. Fuente del texto: [Blizzard — RPP 3.2.0](https://news.blizzard.com/en-us/article/24292852/the-3-2-0-ptr-what-you-need-to-know), 30 jul 2026 — **oficial pero de PTR**; el bug fix sí es del 3.2.1 — **oficial**.

---

### H. Legacy Uniques: ¿hay alguno para Brujo?

**Sí. Ocho de los nueve.** Solo *Arioc's Needle* queda fuera.

| # | Objeto (ES / EN) | Ranura | ¿Brujo? | Dije | Poder conocido |
|---|---|---|---|---|---|
| 1 | **Corona de Leoric** / *Leoric's Crown* | Yelmo | ✅ todas | No | Cuenta como **joyería** y **+75-100 % al efecto de la gema engarzada**; admite Soul Splinters |
| 2 | **Brazales Némesis** / *Nemesis Bracers* | Guantes | ✅ todas | Sí | Genera **packs de élites al usar un santuario** (deducido de un bug fix oficial). Sin texto publicado |
| 3 | **Piedra de Jordán** / *Stone of Jordan* | Anillo | ✅ todas | Sí | Iguala todas las resistencias a la más alta (**fuente única, PTR**). Interactúa con daño Sagrado |
| 4 | **Blusa de Pitusa** / *Squirt's Blouse* | Pecho | ✅ todas | Sí | Tiene acumulaciones de buff. Sin texto publicado |
| 5 | **Aguja de Arioc** / *Arioc's Needle* | Alabarda 2M | ❌ Bárbaro, Druida, Espiritado | Sí | — |
| 6 | **Batida de Henri** / *Henri's Perquisition* | **Foco de mano secundaria** | ✅ Hechicera, Nigromante, **Brujo** | Sí | Sin texto publicado |
| 7 | **Jingum** / *In-Geom* | Espada 1M | ✅ Bárbaro, Druida, Pícaro, Nigromante, Paladín, Hechicera, **Brujo** | Sí | **Reducción de enfriamiento de 15 s** (bug fix oficial). Condición de disparo no publicada |
| 8 | **El Horno** / *The Furnace* | Maza 2M | ✅ Bárbaro, Druida, Nigromante, Paladín, **Brujo** | Sí | Sin texto publicado |
| 9 | `[EN]` *Messerschmidt's Reaver* | Hacha 2M | ✅ Bárbaro, Druida, Nigromante, Paladín, **Brujo** | No | **No era testeable en el PTR.** Sin texto publicado |

- Lista, ranuras y clases: **oficial**, leídas literalmente en [Blizzard — sección *Legacy Uniques*](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy), 12 sep 2026. Corroborado por [Maxroll — Season Guide](https://maxroll.gg/d4/resources/season-guide), 13 sep 2026 → **corroborado**.
- Nombres ES: [Blizzard es-es RPP 3.2.0](https://news.blizzard.com/es-es/article/24292852/el-rpp-3-2-0-todo-lo-que-necesitas-saber), 30 jul 2026 → **oficial** para nomenclatura. *Messerschmidt's Reaver* e *In-Geom* no aparecían en esa página; *Jingum* sí, como traducción de In-Geom.
- Los 7 con `Dije`: lista literal de [Blizzard 3.2.1 > Item Updates > Talisman](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) → **oficial**.
- Caída: sin método de farmeo dirigido publicado. Les aplica *"All Unique items are now available to drop at level 1, and in any Difficulty"* → **oficial** para el marco, **hueco** para el ratio.

**Los tres que de verdad importan a un Brujo (inferencia mía, no dato):**
- **Corona de Leoric** es la más interesante de las nueve para esta clase y esta temporada: duplica casi el efecto de una gema y admite las gemas de temporada. Pero compite con *Crown of Lucion* / *Jaula de la locura* en la misma ranura.
- **Batida de Henri** es la única de las nueve en una ranura que **solo** comparten tres clases, y el Brujo es una. Si el Brujo usa foco de mano secundaria en sus builds de empuje, es la que menos competencia tiene.
- **El Horno** y **Messerschmidt's Reaver** son armas a 2 manos y el Brujo las puede llevar (su build de S15 va con arma 2M: *Moloch's Beating Flame*). **Ninguno de los dos tiene texto de afijo publicado**, así que no puedo decir si merecen la ranura.

---

## Huecos

- **H1 — El valor ANTERIOR de *Hands of the Worldbreaker*.** Blizzard escribe *"reduced to 290%-350%"* sin decir desde cuánto. Maxroll reproduce la línea igual de incompleta. **Sin el "de", no se puede cuantificar el nerf a la build de Apocalipsis**, que es justo la pregunta que importa. No lo he encontrado en ninguna fuente preferente.
- **H2 — Todo el modelo numérico de la Astilla del Mal.** (a) Cuánto daño hace el Poder Icónico. (b) **Si escala con los stats y multiplicadores del jugador** — esto decide si a un Brujo le conviene el fuego de Diablo o el físico de Mefisto. (c) El porcentaje concreto de "más vulnerable a ese Mal Supremo". (d) Qué hacen los 8 modificadores de la vía de Mefisto sobre la Falla y las 6 mejoras del Poder Icónico. **Nada de esto está publicado.**
- **H3 — Los nombres y el orden de los tableros de Paragón del Brujo.** Tengo el orden de **glifos** de dos builds, no el de **tableros**. Ninguna fuente preferente lo publica en texto legible (van en el planner interactivo, que no puedo leer).
- **H4 — Texto de afijo de 8 de los 9 Legacy Uniques.** Solo *Corona de Leoric* tiene texto, y es de PTR. De *El Horno*, *Messerschmidt's Reaver* y *Batida de Henri* —los tres candidatos reales del Brujo— no hay ni una línea. [Maxroll — wiki de Únicos](https://maxroll.gg/d4/wiki/uniques) está actualizada a **23 may 2026** y no los incluye.
- **H5 — Si *Ae'grom's Schism* / *Eye of Baal* apilan su efecto entre la versión objeto y la versión Dije.** El parche dice que ahora existen como Dije; no dice si se suman.
- **H6 — Ranura de la mitad de los únicos del Brujo.** Las notas 3.2.1 dan el texto pero **no la ranura**, y la wiki de Maxroll está desactualizada. He marcado `sin ranura publicada` en vez de deducirla.
- **H7 — Prioridad de afijos por ranura para la S15.** La única guía dentro del parche da umbrales globales, no tabla por ranura. La tabla por ranura que existe es de **26 jun (S14)**.
- **H8 — Si los multiplicadores reescritos siguen siendo `[x]`.** Varios perdieron la marca al reescribirse. Solo se resuelve mirando el tooltip en el juego.
- **H9 — Nombres en español de los glifos y de *Hands of the Worldbreaker*, *Rictus of Terror*, *Dynamism*, *Bindings of Attrition*, *Bridle of Tor'baalos*, *Hellbrand Signet*, *Night Terror*, *Sire of Sin*, *Thrice-Woven Nightmare*, *Sashes of the Wretched*, *Morlu Fleshward*, *Lurid Pact*, *The Blade of Sight Aflame*, *Messerschmidt's Reaver*.** Las notas 3.2.1 **no tienen versión española publicada**: la página es-es dice literalmente *"Puedes consultar las notas completas del parche de la actualización 3.2.1, cuando estén disponibles, aquí"*. He sacado lo que he podido del RPP 3.2.0 y del 3.0 en español.
- **H10 — Cero datos de juego real.** No hay leaderboard, no hay tiempo de limpieza de Falla, no hay una sola build probada en 3.2.1. Todo veredicto de arriba es lectura de texto de parche.

---

## Contradicciones

### C1 — "Al Brujo lo han podado" vs. la tabla de objetos

- **Versión A (dev note oficial):** *"…pruning unintuitive or oppressive scalars. In particular, the Overwhelming Aspect was scaling up too much and Metamorphosis was interacting with several stacking mechanics in unintended ways… We are also looking to redistribute power out of Demonform."*
- **Versión B (el recuento real de líneas):** en la sección de únicos del Brujo del 3.2.1 hay **~15 subidas** y **2 bajadas claras** (*Hands of the Worldbreaker* y el plano de *Jaula de la locura*). *Guanteletes de Sheol* sube a un techo de **600-750 %**. *Escarpes del can infernal* casi triplica.
- **Resolución:** las dos son ciertas y no se contradicen. **La poda es quirúrgica y está dirigida a los dos objetos que sostenían las builds dominantes del PTR; el resto del catálogo sube para forzar diversidad**, que es exactamente lo que dice la nota ("maintaining momentum and build diversity"). **La conclusión práctica es la contraria a la intuitiva: el Brujo no está peor, está obligado a cambiar de build.**

### C2 — El tier list de S15 pone Grito llameante en B, pero es la build que el parche sube y la única con guía nueva

- **Versión A:** [Maxroll Overall Endgame Tier List](https://maxroll.gg/d4/tierlists/endgame-tier-list) (14 sep, S15) → Grito llameante **B**, por debajo de Apocalipsis y Lunático en **A**.
- **Versión B:** el 3.2.1 sube *Elegía* (+ pasa Grito llameante a habilidad Archifiend), sube *Homúnculo infernal* a 80-110 % con activación en cualquier lanzamiento Archifiend, y Maxroll **crea una guía nueva** de Grito llameante ese mismo 14 de septiembre, mientras deja la de Apocalipsis intacta desde el 30 de junio.
- **Versión C (PTR):** [Icy Veins, PTR](https://www.icy-veins.com/d4/news/warlock-is-suddenly-diablo-4s-best-class-and-it-is-not-close-in-season-15/) daba al Brujo la corona; el propio artículo avisa: *"PTR values are almost certainly going to change before the season goes live."*
- **Sin resolver.** La hipótesis que me parece más probable —**y es hipótesis**— es que el tier list de 14 sep arrastre la valoración de S14 para las builds cuyas guías no se han reescrito, y que la A de Apocalipsis sea inercia. **No lo puedo demostrar y no lo doy por bueno.** Se resuelve solo cuando haya leaderboard.

### C3 — Umbrales de Vel. Ataque y Crítico de la guía de S15

Dos lecturas de **la misma página** ([Maxroll Blazing Scream](https://maxroll.gg/d4/build-guides/blazing-scream-warlock-guide), 14 sep) me devolvieron *">70 % Attack Speed / >60 % Critical Strike Chance"* y *"100 % Attack Speed / 100 % Critical Strike Chance"*. Lo más probable es que sean **variante intermedia vs. endgame**, pero **no lo he podido confirmar**, así que **ninguna de las dos cifras vale como objetivo exacto**. Lo que sí es estable: velocidad de ataque y crítico son los dos umbrales que la build persigue, y `>10 Regeneración de Ira` + `>10.000 Res. Fuego` aparecen en las dos lecturas.

### C4 — "Glifo: Poderío" no puede ser *Superiority*

Una lectura de las notas **3.0 en español** devolvió *"Glifo: Poderío"* como equivalente de *Superiority*. **Es imposible:** *Superiority* se introduce en el **3.2.1** (*"New Glyph: Superiority"*). O "Poderío" es otro glifo distinto que ya existía, o la extracción emparejó mal. **Descartado: no doy traducción española para el glifo Superiority.** Mismo problema con *"Puños del destino"* para *Hands of the Worldbreaker*: una lectura del 3.0 es-es lo devolvió, otra lectura del 3.2.0 es-es dijo que no aparece, y la traducción no se parece al original. **Marcado sinconfirmar, no lo uso.**

### C5 — *Jaula de la locura*: ¿nerf o buff?

- **Versión A (titular):** 300-340 % → 100-200 %. Un recorte de dos tercios.
- **Versión B (texto completo):** el 100-200 % es **por cada segundo** que estás transformado, hasta 15 s. A los 2 segundos ya empatas con el valor viejo; a los 15, lo multiplicas.
- **Contrapeso real:** la explosión baja de *"Command Fallen's damage"* a *"Command Fallen's **Base** damage"*.
- **Resolución: es un rediseño, no un recorte, y el neto depende de cuánto tiempo mantengas la transformación.** Ninguna fuente lo ha calculado. **Este es el caso de libro de por qué hay que leer el modelo y no la cifra: quien copie el titular "Jaula de la locura nerfeada de 300 % a 100 %" está diciendo lo contrario de lo que hace el objeto.**

---

## Índice de fuentes

| Fuente | URL | Fecha leída | Uso |
|---|---|---|---|
| Blizzard — *Celebrate 30 Years of Diablo in Season of Hell's Legacy* (contiene las notas 3.2.1) | https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy | 12 sep 2026 | Todo lo oficial: únicos, aspectos, glifos, nodos, Talismán, Legacy Uniques |
| Blizzard — *El RPP 3.2.0* (español) | https://news.blizzard.com/es-es/article/24292852/el-rpp-3-2-0-todo-lo-que-necesitas-saber | 30 jul 2026 | Nomenclatura ES de únicos del Brujo y Legacy Uniques |
| Blizzard — *Notas del parche 3.0* (español) | https://news.blizzard.com/es-es/article/24271857/notas-del-parche-de-diablo-iv-3-0 | — | Nomenclatura ES: Jaula de la locura, Grito llameante, Forma demoníaca, Apocalipsis |
| Blizzard — *The 3.2.0 PTR* | https://news.blizzard.com/en-us/article/24292852/the-3-2-0-ptr-what-you-need-to-know | 30 jul 2026 | Texto de Corona de Leoric (**PTR**) |
| Maxroll — *Blazing Scream Warlock Endgame Guide* | https://maxroll.gg/d4/build-guides/blazing-scream-warlock-guide | **14 sep 2026, "Created for Season 15"** | **La única guía de Brujo del parche vivo** |
| Maxroll — *Overall Endgame Tier List* | https://maxroll.gg/d4/tierlists/endgame-tier-list | 14 sep 2026 (S15) | Posición del Brujo |
| Maxroll — *Apocalypse / Lunatic / Minion Warlock guides* | https://maxroll.gg/d4/build-guides/warlock | 30 jun / 4 ago / 13 jul 2026 (**S14**) | Objetos núcleo y glifos — **caducadas** |
| Maxroll — *3.2.1 Patch Notes* | https://maxroll.gg/d4/news/diablo-4-3-2-1-patch-notes | 12 sep 2026 | Corroboración del "antes/después" |
| Maxroll — *Season of Hell's Legacy Guide* | https://maxroll.gg/d4/resources/season-guide | 13 sep 2026 | Astillas del Mal, Legacy Uniques |
| Maxroll — *Warlock Class Overview* | https://maxroll.gg/d4/getting-started/warlock-class-overview | sin fecha legible | Voluntad como stat principal |
| Icy Veins — *Paragon Glyphs* | https://www.icy-veins.com/d4/guides/paragon-glyph-guide/ | declara S15, **sin fecha legible** | Umbrales 15/50/51/150 |
| Icy Veins — *Abyss Rampage Endgame Warlock* | https://www.icy-veins.com/d4/guides/abyss-rampage-endgame-warlock-build/ | 26 jun 2026 (**S14**) | Única tabla de afijos por ranura — **caducada** |
| Icy Veins — *Warlock Is Suddenly D4's Best Class* | https://www.icy-veins.com/d4/news/warlock-is-suddenly-diablo-4s-best-class-and-it-is-not-close-in-season-15/ | **PTR**, se autodeclara provisional | Contexto del PTR, no valores |

**Fuentes descartadas por las reglas:** todas las tiendas de oro y boosting que inundan esta búsqueda (iggm, mmoexp, u4gm, aoeah, mmogah, timesaver, mtmmo, expcarry…) y sportskeeda. Aparecen en primera página con títulos como *"Apocalypse Warlock Pit 150 Setup"* y cifras concretas ("limpia Falla 150 en 2-3 minutos", "25 millones de dureza") **el día antes de que exista el parche**. **Cero de sus números está en este informe.**
