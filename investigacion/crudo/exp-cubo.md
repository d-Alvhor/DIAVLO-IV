# Cubo Horádrico (Horadric Cube) y crafteo de Míticos — S14 "Death Awakening"

**Dominio:** Cubo Horádrico, receta de Mítico (Mythic Unique), Polvo Primordial (Primordial Dust),
límite de míticos crafteados equipados, ruta alternativa del Joyero (Jeweler).

**Parche vivo declarado por el encargo:** 3.1.3 (build 73224, 12/08/2026).
**Fecha de la investigación:** 19-20/08/2026.
**Estado del jugador:** Nigromante nivel 70, Paragón recién empezado, **acaba de comprar Vessel of Hatred + Lord of Hatred**.

---

## 0. Aviso de fiabilidad — leer antes que nada

Esta investigación ha encontrado **datos muertos publicados hoy mismo en fuentes preferentes**. No es teoría:

| Fuente | Fecha de la propia página | Qué dice | Estado real |
|---|---|---|---|
| Maxroll, ficha del Cubo | 16/07/2026 | "Upgrade to Mythic: 1x Unique (850+ IP), **5x Pandemonium Fragment**" | ❌ **MUERTO**. Blizzard lo bajó a 4 el 14/07/2026, dos días antes |
| Maxroll, guía Minion Necro | 22/07/2026 | "Solo puedes equipar un Mítico que craftees en el Cubo" | ❌ **MUERTO**. Blizzard quitó el límite el 16/07/2026, seis días antes |
| Icy Veins, guía Naz Mages | 27/06/2026 | "solo puedes tener 1 mítico crafteado equipado a la vez" | ❌ **MUERTO** desde el 16/07/2026 |
| Wowhead, ficha del Cubo | 09/05/2026 | — | ❌ Es de **Season 13**. Descartada entera |

**Regla aplicada en este informe:** ante conflicto, mandan las notas oficiales de Blizzard. Las guías van detrás.

**Fuente de datamining usada:** el fichero del planificador de Maxroll
(`assets-ng.maxroll.gg/d4-tools/game/data.min.json`, descargado 20/08/2026, 11,6 MB).
Su campo `version` dice **`3.1.0.72698`** — es decir, **el build de lanzamiento de temporada, NO el parche vivo 3.1.3**.
Sirve para confirmar *qué existe* y los textos internos de los objetos; **no sirve para los costes de receta**,
que no están en ese fichero. Declarado como datamining.

---

## 1. Cómo se desbloquea y dónde está 🆕

| Dato | Valor | Fuente |
|---|---|---|
| Requisito de desbloqueo | Jugar la campaña de **Lord of Hatred** | [maxroll.gg/d4/resources/horadric-cube](https://maxroll.gg/d4/resources/horadric-cube) |
| Ubicación una vez desbloqueado | **Temis** | [maxroll.gg/d4/resources/horadric-cube](https://maxroll.gg/d4/resources/horadric-cube) |
| Expansión necesaria | **Lord of Hatred** (el Cubo es contenido de expansión) | [maxroll.gg/d4/resources/horadric-cube](https://maxroll.gg/d4/resources/horadric-cube) |

🆕 **Esto es nuevo para el jugador hoy.** Antes de comprar LoH el Cubo no existía en su cuenta. La cita literal de Maxroll:
el Cubo "becomes available by playing through the Lord of Hatred campaign and is located in Temis afterwards".

⚠️ **No hay atajo documentado.** No he encontrado en fuente preferente ninguna forma de saltarse la campaña de LoH.
Hay que jugársela.

### Puertas adicionales de la receta de Mítico — SIN CONFIRMAR

Varias guías secundarias (no preferentes) afirman que la receta de Mítico exige además **nivel 70** y
**Tormento I (Torment I) o superior**. **No he encontrado esto escrito en ninguna nota oficial de Blizzard,
ni en Maxroll, ni en Icy Veins.** Va a "No encontrado". Es plausible y el jugador ya cumple el nivel 70
de todas formas, así que en la práctica no le bloquea.

---

## 2. La receta EXACTA de Mítico en el parche vivo — la contradicción 5 vs 4, resuelta

**Resuelta: son 4.** Y hay un segundo cambio que casi nadie ha recogido: **la receta ya no se llama "Upgrade".**

### Historial oficial de la receta

| Parche | Fecha | Cambio (texto oficial) | Fuente |
|---|---|---|---|
| 3.1.0 | 30/06/2026 | "The Upgrade to Mythic recipe in the Horadric Cube now always creates an item for the same gear slot" | [news.blizzard.com/…/24287406](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) |
| 3.1.0 | 30/06/2026 | "Mythic Unique Items cannot be used in the Upgrade to Mythic Unique recipe" | [news.blizzard.com/…/24287406](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) |
| **3.1.1** | **14/07/2026** | **"Reduced the cost of the Upgrade to Mythic recipe on the Horadric Cube from 5 to 4 Pandemonium Fragments"** | [news.blizzard.com/…/24287406](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) · [icy-veins.com](https://www.icy-veins.com/d4/news/diablo-4-season-14-patch-notes-increased-mythic-and-pandemonium-fragment-drop-rates/) |
| **3.1.2** | **28/07/2026** | **"Updated the name of the Mythic crafting Horadric Cube recipe from 'Upgrade' to 'Craft'"** — nota del desarrollador: para que el nombre sea consistente con el resto de recetas del Cubo | [maxroll.gg/d4/news/lord-of-hatred-3-1-2-patch-notes](https://maxroll.gg/d4/news/lord-of-hatred-3-1-2-patch-notes) |
| 3.1.2 | 28/07/2026 | "Fixed an issue where Mythic Unique items could not be recycled" | [maxroll.gg/d4/news/lord-of-hatred-3-1-2-patch-notes](https://maxroll.gg/d4/news/lord-of-hatred-3-1-2-patch-notes) |

### La receta tal y como está viva hoy

| Campo | Valor vivo | Confianza |
|---|---|---|
| Nombre en pantalla | **"Craft Mythic"** (ya no "Upgrade to Mythic") | Alta — nota oficial 3.1.2 |
| Entrada | **1x objeto Único (Unique) de 850+ de poder de objeto (Item Power)** | Alta — Maxroll lista el umbral 850 |
| Coste | **4x Fragmento de Pandemónium (Pandemonium Fragment)** | **Alta — nota oficial 3.1.1** |
| Ranura de salida | **La misma ranura que el objeto de entrada** (garantizado desde 3.1.0) | Alta — nota oficial 3.1.0 |
| Entrada prohibida | **Un Mítico no se puede meter como entrada** | Alta — nota oficial 3.1.0 |

⚠️ Si el jugador ve **5** en la interfaz del juego, manda su pantalla y hay que avisar: significaría que la nota
oficial no se aplicó o se revirtió sin anunciarlo. Con lo que hay escrito hoy, son 4.

### Qué NO conserva la salida — esto es lo caro de entender

Cita literal de Maxroll sobre la receta:

> "This completely randomizes the item gained, meaning it does not retain Greater Affixes, Affixes, nor is it guaranteed to be the same item."
> — [maxroll.gg/d4/resources/horadric-cube](https://maxroll.gg/d4/resources/horadric-cube)

Traducido a decisiones: **es una tragaperras por ranura, no un upgrade dirigido.**
- Metes unas botas Únicas cualquiera de 850+ → sale **un Mítico de botas al azar** de los que tu clase pueda usar.
- **No** conserva Afijos Mayores (Greater Affixes) del objeto de entrada.
- **No** conserva los afijos normales.
- **No** garantiza que salga el objeto que quieres.
- El objeto de entrada **no influye en qué Mítico sale**, solo en la ranura.

Corolario práctico: **el objeto de entrada debe ser el Único más basura que tengas de 850+ en esa ranura.**
Meter un Único con Afijos Mayores buenos es quemarlo para nada.

### Afirmaciones que circulan y que NO he podido verificar

Fuentes secundarias afirman que todos los Míticos crafteados salen **Ancestrales** y con un **+30 % de poder Único**.
**No lo he encontrado en Blizzard, Maxroll ni Icy Veins.** Va a "No encontrado". No lo uses para decidir.

---

## 3. El límite de "un solo mítico crafteado equipado" — YA NO EXISTE ✅

**Respuesta corta: el límite se eliminó el 16/07/2026 (PC) / 17/07/2026 (consola), en el hotfix 3.1.1a.**

Texto oficial del post de parche de Blizzard:

> "Removed the 'one-crafted Mythic' equipment restriction on Mythic items."
> — [us.forums.blizzard.com/…/311a-patch-july-16-2026/263234](https://us.forums.blizzard.com/en/d4/t/311a-patch-july-16-2026/263234)
> Confirmado también en [icy-veins.com](https://www.icy-veins.com/d4/news/diablo-4-season-14-hotfix-crafted-mythic-restriction-removed-and-mythic-drop-rate-increased/)

### Por qué esto importa muchísimo y por qué medio internet aún dice lo contrario

Al arrancar la S14, los Míticos hechos en el Cubo salían marcados como **"Crafted"** y solo podías llevar **uno**
equipado; los Míticos **caídos** no tenían ese tope. Ese era el modelo que todas las guías interiorizaron.
El hotfix 3.1.1a lo tiró entero. Las guías de build de Maxroll (22/07) e Icy Veins (27/06) **siguen enseñando el modelo viejo**.

**Consecuencia directa para el jugador: puede llenarse de Míticos crafteados. No hay tope. Ninguno.**

### Resto del hotfix 3.1.1a (16/07/2026)

| Cambio | Texto | Fuente |
|---|---|---|
| Tope de míticos crafteados | "Removed the 'one-crafted Mythic' equipment restriction on Mythic items." | [Blizzard forums](https://us.forums.blizzard.com/en/d4/t/311a-patch-july-16-2026/263234) |
| Drops del jefe de temporada | "Increased the drop rates of Mythic and Iconic Unique Items from the Corrupted Reaper." | [Blizzard forums](https://us.forums.blizzard.com/en/d4/t/311a-patch-july-16-2026/263234) |
| Bugfix (cierra un exploit) | "Removed the ability to add the Mythic modifier to Unique Charms & Seals in the Cube." No era intencionado en S14 | [Blizzard forums](https://us.forums.blizzard.com/en/d4/t/311a-patch-july-16-2026/263234) |

### 🔮 Aviso oficial para la S15 — relevante para el objetivo "llegar preparado a S15"

En la nota del desarrollador del mismo hotfix 3.1.1a, Blizzard adelanta que en la **Season 15**:
- **quitarán el crafteo de Mítico por re-roll del Cubo**,
- lo sustituirán por **una mejora directa que conserva el objeto Único original**,
- y **evaluarán reponer la regla de "un solo crafteado" solo para esa nueva vía**.

Fuentes: [Blizzard forums 3.1.1a](https://us.forums.blizzard.com/en/d4/t/311a-patch-july-16-2026/263234) ·
[gamesradar.com](https://www.gamesradar.com/games/diablo/diablo-4-hotfix-makes-it-easier-to-farm-mythics-as-blizzard-confirms-season-15-will-remove-mythic-reroll-crafting-from-the-horadric-cube-adding-a-direct-upgrade-instead/)

**Lectura estratégica: la lotería barata por ranura es una ventana que se cierra el ~15/09.** Lo que se craftee
ahora es aprovechable ahora; el sistema de la S15 será otro. Los Fragmentos de Pandemónium son moneda
**de temporada** (`S14_Seasonal_Currency` en el datamine) — no viajan a la S15. **Gastarlos todos antes del final.**

---

## 4. Fragmentos de Pandemónium — de dónde salen

Texto interno del objeto (datamining, build 3.1.0.72698):
`S14_Seasonal_Currency` — "Pandemonium Fragment" — *"A piece of the fractured realm at the center of creation…"*

| Fuente del fragmento | Detalle | Origen del dato |
|---|---|---|
| **Corrupted Reaper** (jefe de guarida de temporada) | **Hasta 2 por muerte, escalando con el nivel de Tormento** (desde 3.1.1) | Oficial: "Corrupted Reaper now drops up to two Pandemonium Fragments, scaling with Torment level" — [icy-veins.com](https://www.icy-veins.com/d4/news/diablo-4-season-14-patch-notes-increased-mythic-and-pandemonium-fragment-drop-rates/) |
| **Recompensa de reputación "Glints of Hope" repetible** | **Garantiza 1 fragmento** (desde 3.1.1) | Oficial: "Repeatable Glints of Hope Reputation Reward now guarantees a Pandemonium Fragment" — [icy-veins.com](https://www.icy-veins.com/d4/news/diablo-4-season-14-patch-notes-increased-mythic-and-pandemonium-fragment-drop-rates/) |
| Tablero de reputación de temporada / Resplendent Caches | Mencionado por fuentes secundarias | Secundaria — confianza media |

**Ubicación del Corrupted Reaper:** Pandemonium Threshold, en **Zarbinzet**. Fuente secundaria; también se menciona
que abrir su alijo requiere una **Superior Lair Key** farmeada en la mini-mazmorra **Deathtoll Chamber**.
⚠️ **Estos dos últimos datos NO están confirmados en fuente preferente ni oficial.** Verificar en pantalla.

**Aritmética que sí es sólida:** a 4 fragmentos por craft y hasta 2 fragmentos por Corrupted Reaper,
**~2 kills de Reaper = 1 Mítico crafteado**, en Tormento alto.

---

## 5. Re-roll de afijos con Polvo Primordial — el taller de min-max

### 5.1 Los 8 polvos y para qué sirve cada uno

Textos internos del juego (datamining, build 3.1.0.72698 — `X2_HoradricCube_CraftingMaterial_A…H`):

| Polvo | ID interno | Para qué sirve (texto del juego) |
|---|---|---|
| **Raw** (Bruto) | `..._A` | "for most Transmutations" — el combustible genérico |
| **Coarse** (Basto) | `..._B` | "for Transmutations that **add affixes**" |
| **Refined** (Refinado) | `..._C` | "for Transmutations that **change or remove affixes**" |
| **Volatile** (Volátil) | `..._D` | "to **Transfigure** Items" |
| **Pure** (Puro) | `..._E` | "for Transmutations that create **Legendary** items" |
| **Enhanced** (Mejorado) | `..._F` | "for Transmutations that create **Unique** items" |
| **Attuned** (Sintonizado) | `..._G` | "for **rerolling the value of a Unique item's power**" ← clave para Míticos |
| **Resonant** (Resonante) | `..._H` | "to **upgrade a random affix into a Greater Affix**" ← clave para min-max |

**Fuentes de polvo (texto del juego, idéntico en casi todos):** Cube Spoils en **War Plans**, recompensas de alijo
del **Árbol de los Susurros**, monstruos **Élite**, y la **Undercity of Kurast**.
(El Resonante omite la Undercity en su texto.)

Cambio oficial relevante: **3.1.0 (30/06/2026)** — *"The drop rate for Refined Primordial dust has been increased
significantly in Torment VII and above"* — [news.blizzard.com](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes).

### 5.2 Recetas de modificación con sus costes exactos

Todas de [maxroll.gg/d4/resources/horadric-cube](https://maxroll.gg/d4/resources/horadric-cube) (actualizada 16/07/2026).
⚠️ Esa misma página tiene mal el coste del Mítico, así que **trata estos números como fiables-pero-verificables en pantalla**.

| Receta | Coste exacto | Prisma |
|---|---|---|
| **Unique Power Reroll** (re-rollea el **valor del poder Único**) | 1x Único **Ancestral** + **1x Attuned Primordial Dust** + **100x Raw** | — |
| **Chaotic Reroll** (cambia un afijo al azar) | 1x objeto Mágico/Raro/Legendario + **1x Refined** + **15x Raw** | opcional |
| **Focused Reroll** | 1x objeto Mágico/Raro/Legendario + **1x Refined** + **15x Raw** | **obligatorio** |
| **Add Affix** | 1x objeto Común/Mágico/Raro/Legendario + **1x Coarse** + **5x Raw** | opcional |
| **Remove Affix** | 1x objeto Mágico o Raro + **1x Refined** + **15x Raw** | opcional |
| **Transfigure Item** | 1x Legendario, **Único o Mítico** + **1x Volatile** | opcional |
| **Upgrade to Unique** | 1x objeto Común + **1x Enhanced** + **10x Raw** | — |
| **Upgrade to Legendary** | 1x objeto Raro + **1x Pure** + **10x Raw** | opcional |
| **Craft Mythic** | 1x Único 850+ IP + **4x Pandemonium Fragment** (corregido vs. Maxroll) | — |
| Reroll Set Charm | 1x Set Charm + 25x Raw + 50x Infused Horadric Resin | — |
| Craft Unique Charm | 1x Único Ancestral + 3x Unique Charms + 1x Enhanced + 50x Raw + 100x Infused Horadric Resin | — |

### 5.3 Qué se puede y qué NO se puede tocar en un Mítico

| Elemento del Mítico | ¿Se puede modificar? | Cómo |
|---|---|---|
| **El poder Único definitorio** (el efecto que le da nombre) | ❌ **No se puede cambiar por ningún método** | — |
| **El VALOR numérico de ese poder Único** | ✅ Sí | **Unique Power Reroll** en el Cubo: 1 Attuned + 100 Raw. Datamining confirma la función del polvo Attuned |
| **Afijos normales (no-poder)** | ✅ Sí | Encantador (Occultist) — 1 afijo · **Chaotic Reroll** en el Cubo — con Refined + Raw · Temple (Tempering) en el Herrero |
| **Subir un afijo a Afijo Mayor** | ✅ Sí | **Resonant Primordial Dust** — "upgrade a random affix into a Greater Affix" (datamining). **Coste exacto: no encontrado** |

⚠️ Ojo con **Transfigure**: acepta Míticos como entrada. El **Entropic Tuning Prism** dice literalmente
*"Has a 100% chance of making an item Unmodifiable"*. Un Mítico marcado como **Unmodifiable** ya no se puede
seguir puliendo. **No metas un Mítico bueno en Transfigure sin saber lo que haces.**

### 5.4 Prismas de Sintonía (Tuning Prisms) — 8, no 6

Del datamining (`X2_HoradricCube_TuningStone_1…8`):

| Prisma | Dirige hacia |
|---|---|
| **Aggressive** | Afijos **ofensivos** |
| **Protector's** | Afijos **defensivos** |
| **Resourceful** | Afijos de **recurso** |
| **Pragmatic** | **Movilidad** y **utilidad** |
| **Chromatic** | **Resistencias** |
| **Adept's** | **Habilidades** y **estadística principal** ← el que le interesa a un nigro de esbirros |
| **Entropic** | Transfiguración: quita los resultados más arriesgados **y los más potentes**; 100 % de dejar el objeto **Unmodifiable** |
| **Kullean** | **Solo amuletos.** Transfiguración: añade un **Aspecto Legendario** extra y **deja el objeto Modificable** |

🔎 Dato cruzado útil: la guía de Icy Veins de Naz Mages señala que el amuleto **Banished Lord's Talisman**
*"REQUIRES imprinted Tidal Aspect using Kullean Tuning Prisms with the Horadric Cube"* —
[icy-veins.com](https://www.icy-veins.com/d4/guides/mendeln-summoner-necromancer-build/). 🆕 Vía que antes no tenía.

---

## 6. Ruta alternativa: Joyero (Jeweler) y Herrero (Blacksmith) con Chispas Resplandecientes

Texto interno de la **Resplendent Spark** (datamining, `CraftingMaterial_Salvage_Uber_Unique`):

> "A rare material used by the **Blacksmith** to **Forge** a **Mythic Unique Cache**.
> Also used at the **Jeweler** with **Rune Crafting** to craft a **Mythic Unique Item**.
> Collected from **Salvaging** a **Mythic Unique** at the Blacksmith."

Es la confirmación limpia de que hay **dos rutas distintas** además del Cubo.

| Ruta | Coste | ¿Elige el objeto? | Expansión | Fuente |
|---|---|---|---|---|
| **Cubo Horádrico** — Craft Mythic | 1 Único 850+ IP + **4 Fragmentos de Pandemónium** | ❌ Al azar dentro de la ranura | **Lord of Hatred** 🆕 | Blizzard 3.1.1 + Maxroll |
| **Herrero** — Mythic Unique Cache | **2x Resplendent Spark + 50.000.000 de oro** | ❌ Mítico al azar | Ninguna (juego base) | [maxroll.gg/d4/resources/crafting-cheat-sheet](https://maxroll.gg/d4/resources/crafting-cheat-sheet) (act. 14/07/2026) |
| **Joyero** — Rune Crafting, pestaña Mythic Uniques | **2x Resplendent Spark + runas** (cantidades en disputa, ver abajo) | ✅ **Sí, eliges el Mítico concreto** | **Vessel of Hatred** 🆕 | [icy-veins.com](https://www.icy-veins.com/d4/guides/how-to-farm-uber-uniques/) + datamining |

### ⚠️ Contradicción NO resuelta en el coste del Joyero

Tres versiones distintas circulando, ninguna en fuente oficial ni en la hoja de crafteo de Maxroll:

- **A)** "2 Resplendent Spark + 3x 6 runas Legendarias distintas" — [icy-veins.com](https://www.icy-veins.com/d4/guides/how-to-farm-uber-uniques/)
- **B)** "6 runas Mágicas + 6 Raras + 6 Legendarias + 1 Resplendent Spark" — agregadores secundarios
- **C)** "2 Resplendent Sparks + runas Legendarias/Raras/Mágicas específicas por objeto + 5.000 de oro" — agregadores secundarios

**No lo doy por cerrado.** Va a "No encontrado". Lo que **sí** está confirmado por el texto del propio juego es que
la ruta existe, que usa Resplendent Spark y que va por **Rune Crafting** en el Joyero.
**Que lo mire en pantalla: el coste real está en la interfaz del Joyero.**

### Cómo conseguir Resplendent Sparks

| Vía | Detalle | Fuente |
|---|---|---|
| **Desguazar un Mítico en el Herrero** | 1 Chispa por Mítico | Texto del juego (datamining) + [icy-veins.com](https://www.icy-veins.com/d4/guides/how-to-farm-uber-uniques/) |
| **Resplendent Cache** | "Contains a wondrous assortment of items, currencies, and a resplendent spark" | Datamining (`Resplendent_Cache`) |
| Fases del Viaje de Temporada (Season Journey) | Mencionado por fuentes secundarias | Confianza media |

🔁 **Bucle que se abre hoy:** Cubo (4 fragmentos) → sale un Mítico al azar → si no sirve, **desguazarlo** → 1 Chispa →
2 Chispas = 1 Mítico **elegido** en el Joyero. Los fragmentos de temporada se convierten en Míticos dirigidos.
Además, **3.1.2 arregló** que los Míticos no se podían reciclar
([maxroll 3.1.2](https://maxroll.gg/d4/news/lord-of-hatred-3-1-2-patch-notes)), así que el bucle está operativo.

---

## 7. Verificación del MODELO: "Mythic Uniques 3.0" e "Iconic Mythics"

Esto es lo que el encargo pedía comprobar: **el marco conceptual cambió en la S14 y muchas guías siguen con el viejo.**

**Modelo viejo (S13 y anteriores):** "Mítico" = una lista cerrada de ~13 objetos uber con nombre propio.

**Modelo vivo (S14):** **"Mítico" es una CALIDAD que cualquier Único puede alcanzar.** Los ~13 objetos con nombre
de siempre pasan a llamarse **"Iconic Mythics"** y forman una piscina aparte.

Prueba oficial de que el término "Iconic Mythic" es real y distinto: la nota de 3.1.1 de Blizzard dice
*"Increased the chance of naturally dropped Mythics being an **Iconic Mythic**"* —
[icy-veins.com](https://www.icy-veins.com/d4/news/diablo-4-season-14-patch-notes-increased-mythic-and-pandemonium-fragment-drop-rates/).
Si "Mítico" e "Icónico" fueran lo mismo, esa frase no tendría sentido.

### Los Iconic Mythics según el datamine (magicType 4, build 3.1.0.72698)

Son **14 piezas de equipo + 1 gema**. Ninguna es específica de Nigromante:

| Objeto | Ranura |
|---|---|
| Harlequin Crest | Casco |
| Andariel's Visage | Casco |
| Heir of Perdition | Casco |
| Tyrael's Might | Pecho |
| Shroud of False Death | Pecho |
| Melted Heart of Selig | Amuleto |
| Ring of Starless Skies | Anillo |
| Doombringer | Espada 1M |
| El'Druin, Sword of Justice | Espada 1M |
| The Grandfather | Espada 2M |
| Shattered Vow | Lanza 2M |
| Ahavarion, Spear of Lycander | Bastón 2M |
| Nesekem, the Herald | Glaive (Spiritborn) |
| The Cow King's Crown | Casco |
| The Empyrean Eye | Gema mítica |

También aparecen: **Mythic Unique Horadric Seal**, y tres sellos — *Seal of the Severed Finger*,
*Seal of the Golden Epiphany*, *Seal of the Diamond Mind*.
⚠️ Recuerda que **3.1.1a cerró** la posibilidad de añadir el modificador Mítico a **Unique Charms y Seals** en el Cubo.

**Cambio de 3.1.1:** *"Added El'Druin, Sword of Justice to the Mythic Unique Cache from the Blacksmith"* —
[icy-veins.com](https://www.icy-veins.com/d4/news/diablo-4-season-14-patch-notes-increased-mythic-and-pandemonium-fragment-drop-rates/).

### Por qué esto le cambia la vida a un nigro de esbirros 🆕

Bajo el modelo nuevo, **los Únicos de su propia build pueden ser Míticos**. Los objetos que la guía de Minion Necro
de Maxroll (act. 22/07/2026) marca como prioritarios son Únicos **de clase**, no icónicos:

| Variante de la build | Prioridad de objetos | Fuente |
|---|---|---|
| Guerreros (Warrior) | Pact of Bone → The Undercrown → Deathgrip → Blood Moon Breeches | [maxroll.gg/d4/build-guides/minion-necromancer-guide](https://maxroll.gg/d4/build-guides/minion-necromancer-guide) |
| Magos (Mages) | Bloodless Scream → Pact of Bone → The Undercrown → The Hand of Naz → Blood Moon Breeches | ídem |
| Híbrida (todos los esbirros) | "The Undercrown is the centerpiece to the build" | ídem |

Dato adicional de Icy Veins (act. 27/06/2026, guía Naz Mages): *"Mythic Unique Items like Ring of Starless Skies and
Heir of Perdition now only have two guaranteed affixes, with the rest being random ones."*
⚠️ Esto es de una página de junio; **no verificado contra el parche vivo**. Tratar como pista, no como dato.

---

## 8. El dúo: qué puede hacer cada uno según lo que tenga comprado

El encargo pide cubrir ambos casos. **Las tres rutas tienen puertas de expansión distintas:**

| Ruta a Míticos | Él (VoH + LoH ✅) | Pareja **con** ambas expansiones | Pareja **sin** expansiones (juego base) |
|---|---|---|---|
| **Cubo Horádrico** (4 fragmentos) | ✅ 🆕 | ✅ | ❌ **Bloqueado** — el Cubo es contenido de LoH |
| **Joyero**, Mítico elegido con runas + Chispas | ✅ 🆕 | ✅ | ❌ **Bloqueado** — requiere Vessel of Hatred |
| **Herrero**, Mythic Unique Cache (2 Chispas + 50M oro) | ✅ | ✅ | ✅ **Disponible** — no consta requisito de expansión |
| Míticos caídos de jefes | ✅ | ✅ | ✅ (con las salvedades de contenido de expansión) |

**Si la pareja NO ha comprado las expansiones:** su única vía de crafteo es el **Herrero, 2 Chispas + 50.000.000 de oro**,
y las Chispas salen sobre todo de desguazar Míticos caídos. Es una vía **mucho** más lenta. Además, ni el Cubo ni
Temis ni la campaña de LoH existen para ella/él.

⚠️ **No he encontrado escrito** en fuente preferente si el jugador con LoH puede llevar a alguien sin expansión a las
zonas o jefes de LoH en dúo, ni cómo se reparte el botín en ese caso. Va a "No encontrado". Es la pregunta que más
le va a doler y **no la voy a improvisar**.

---

## 9. Discrepancias y avisos sueltos

- **Build de 3.1.1:** Icy Veins dice **#72805**; un agregador dice **#72836**. No los he podido reconciliar contra
  Blizzard. El número de build de 3.1.1 queda **sin confirmar**; el *contenido* de la nota sí está confirmado.
- **Datamine desfasado:** el fichero de Maxroll sirve `3.1.0.72698`. Está **tres parches por detrás** del 3.1.3 vivo.
  Todo lo que sale de ahí en este informe es **existencia y texto de objetos**, nunca costes de receta.
- **Nada específico de 3.1.2 sobre Fragmentos, Chispas, salvage o Polvo Primordial**, más allá de los dos puntos citados.
- **No he encontrado notas de 3.1.3** (build 73224, 12/08/2026) en ninguna fuente. Es el parche que el encargo declara
  como vivo. **Hueco importante:** cualquier cosa que 3.1.3 haya tocado del Cubo no está cubierta aquí.
- **PTR de 3.2.0 (S15):** se menciona una ventana 04–11/08/2026 y una receta "Upgrade Direct to Mythic".
  Fuente secundaria, **no confirmada**. Encaja con la nota oficial del desarrollador de 3.1.1a, pero no la sustituye.

---

## Fuentes

URLs realmente abiertas durante esta investigación:

**Oficiales de Blizzard**
- https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes — notas de parche 3.1.0 y 3.1.1
- https://us.forums.blizzard.com/en/d4/t/311a-patch-july-16-2026/263234 — post oficial del hotfix 3.1.1a

**Preferentes**
- https://maxroll.gg/d4/resources/horadric-cube — tabla de recetas (act. 16/07/2026) ⚠️ coste de Mítico desfasado
- https://maxroll.gg/d4/resources/crafting-cheat-sheet — hoja de crafteo (act. 14/07/2026)
- https://maxroll.gg/d4/news/lord-of-hatred-3-1-2-patch-notes — notas 3.1.2 (28/07/2026)
- https://maxroll.gg/d4/build-guides/minion-necromancer-guide — build de esbirros (act. 22/07/2026) ⚠️ límite desfasado
- https://www.icy-veins.com/d4/news/diablo-4-season-14-patch-notes-increased-mythic-and-pandemonium-fragment-drop-rates/ — 3.1.1
- https://www.icy-veins.com/d4/news/diablo-4-season-14-hotfix-crafted-mythic-restriction-removed-and-mythic-drop-rate-increased/ — 3.1.1a
- https://www.icy-veins.com/d4/guides/how-to-farm-uber-uniques/ — obtención de Míticos ⚠️ sin fecha visible
- https://www.icy-veins.com/d4/guides/mendeln-summoner-necromancer-build/ — Naz Mages (act. 27/06/2026) ⚠️ límite desfasado

**Datamining (declarado como tal)**
- https://assets-ng.maxroll.gg/d4-tools/game/data.min.json — fichero de datos del planificador de Maxroll,
  descargado el 20/08/2026 (11,6 MB), campo `version` = **3.1.0.72698**

**Abiertas sin resultado utilizable**
- https://www.wowhead.com/diablo-4/guide/systems/horadric-cube — **Season 13** (act. 09/05/2026), descartada
- https://mobalytics.gg/diablo-4/guides/patch-3-1-1a-what-changed — **HTTP 403**, no accesible
- https://dotesports.com/diablo/guides/how-to-craft-mythic-uniques-in-diablo-4 — **HTTP 403**, no accesible
- https://maxroll.gg/d4/resources/mythic-uniques — **HTTP 404**, no existe
- https://www.gamesradar.com/…/diablo-4-hotfix-makes-it-easier-to-farm-mythics-… — contenido truncado, solo sirvió
  para corroborar el anuncio de S15 ya presente en el post oficial

**Fuentes vetadas por el encargo:** no se ha usado ningún dato de fextralife, primagames, beebom, gamespot,
segmentnext, studioloot, gamerguides, pcgamesn ni mythicdrop. Aparecieron en resultados de búsqueda y fueron ignoradas.
Tampoco se ha tomado como dato firme nada procedente de webs de venta de oro/boosting (mmogah, timesaver, nexttier,
leprestore, conquestcapped, skycoach, overgear, iggm, aoeah, playerauctions y similares): cuando coinciden con una
fuente preferente se cita la preferente, y cuando no, el dato va a "No encontrado".

---

## No encontrado

Huecos declarados. **Nada de esto se ha reconstruido ni inferido.**

1. **Notas del parche 3.1.3** (build 73224, 12/08/2026). No localizadas en ninguna fuente. Es el parche vivo:
   cualquier cambio suyo al Cubo o a los Míticos queda fuera de este informe.
2. **Coste exacto de la receta de Mítico en el Joyero.** Tres versiones contradictorias, ninguna en fuente oficial
   ni en la hoja de crafteo de Maxroll. **Hay que leerlo en la interfaz del Joyero.**
3. **Nivel 70 y Tormento I como requisitos de la receta del Cubo.** Solo en fuentes secundarias. No confirmado
   por Blizzard, Maxroll ni Icy Veins.
4. **"Todos los Míticos crafteados salen Ancestrales" y "+30 % de poder Único".** Muy repetido en agregadores,
   ausente de toda fuente preferente. **No usar para decidir.**
5. **Coste exacto del Resonant Primordial Dust** para subir un afijo a Afijo Mayor. El datamine confirma la función
   del polvo; la receta y su cantidad no aparecen en la tabla de Maxroll.
6. **Número de build de 3.1.1.** Dos cifras en circulación (#72805 / #72836), sin reconciliar contra Blizzard.
7. **Reglas de dúo entre cuentas con y sin expansión:** si un jugador con LoH puede llevar a uno sin LoH a Temis,
   a la campaña de LoH o al Corrupted Reaper, y cómo se reparte el botín. **Este es el hueco que más le afecta.**
8. **Confirmación en fuente preferente de la ubicación del Corrupted Reaper** (Pandemonium Threshold, Zarbinzet)
   y de la **Superior Lair Key / Deathtoll Chamber**. Solo en secundarias.
9. **Tope de acumulación de Fragmentos de Pandemónium**, si existe, y cuántos da el tablero de reputación en total.
10. **Si la vía del Joyero puede craftear Míticos NO icónicos** (es decir, Únicos de clase con calidad Mítica,
    como Pact of Bone o The Undercrown) o solo la lista de 14 icónicos. **Es la pregunta que decide toda su
    estrategia de min-max** y no tengo respuesta escrita.
11. **Probabilidades** de cada Mítico dentro de una ranura al usar Craft Mythic. Ninguna fuente publica la tabla.
12. **Confirmación oficial del PTR 3.2.0** y de la receta "Upgrade Direct to Mythic" de la S15, más allá de la
    nota del desarrollador de 3.1.1a.
