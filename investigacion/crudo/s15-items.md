# Itemización en 3.2.1 (Diablo IV — Temporada 15, "Season of Hell's Legacy")

> **Estado al escribir (15 sep 2026, antes de las 16:30 UTC):** el parche 3.2.1 **todavía no ha salido**.
> Todo lo de aquí sale de las notas oficiales publicadas el 12 sep 2026 y del PTR 3.2.0 (30 jul 2026).
> **No existe ni un solo dato de juego real de la S15.** Cualquier cifra marcada como PTR puede haber cambiado.

## Resumen

1. **El marco de resistencias que casi todo internet repite está muerto desde la S11.** No hay tope del 70%/85% ni afijos en "%": las resistencias son un **rating plano** y la reducción de daño sale de `RD% = R / (R·10/9 + 1136)` (nivel 70), asintótica al 90%. 3.2.1 **no toca ningún tope** porque no queda tope que tocar.
2. El cambio real: **un afijo de resistencia a UN elemento vale ahora 7× lo que uno de "a todos los elementos"**, en equipo, dijes (Charms) y recetas de templado. Confirmado con números oficiales: los Soul Splinters dan 4375 de resistencia elemental única frente a 625 de "a todos los elementos" — exactamente 7:1.
3. **Nadie —ni Blizzard— dice si tus objetos ya equipados se recalculan.** Es el hueco grande de este informe. Lo que sí dice la nota es que el templado de "todas las resistencias" ha sido **"re-tuneado"**, sin cifra: puede ser subida o bajada.
4. **Stone of Jordan iguala todas tus resistencias a la más alta** (fuente única, de PTR). Con el buff 7× eso convierte "apilar un solo elemento a saco" en la estrategia dominante. Es la jugada de la temporada, y es teoría: nadie la ha probado en vivo.
5. Todos los Únicos caen ya **desde nivel 1 y en cualquier dificultad**; los Míticos son más deterministas (los jefes de guarida solo sueltan de su propio pool) y la Cuba Horadrim gana **dos recetas de reroll** y una de Mítico 1:1 con etiqueta "Crafted" (solo una equipable). **Maestría (Masterworking): cero cambios.**

---

## Hallazgos

### A. El marco: cómo funcionan HOY las resistencias (verificar esto antes que las cifras)

| # | Dato | Cifra | Fuente | Fecha de la página | Evidencia |
|---|------|-------|--------|--------------------|-----------|
| A1 | Armadura y Resistencias son un **sistema de rating**, no porcentajes con tope por dificultad. Cambió en la **Temporada 11**. | — | [Maxroll — In-depth Defense Guide, changelog](https://maxroll.gg/d4/getting-started/defenses-for-beginners) ("Updated for Season 11 — Updated Armor and Resistances to follow a rating system, instead of having caps for different difficulties", 9 dic 2025) | Actualizada 16 ago 2026 | unica (preferente, pero una sola) |
| A2 | Fórmula de reducción de daño por resistencia | `RD% = Resistencia / (Resistencia·10/9 + Constante)`; **Constante = 1136 a nivel 70** (baja al bajar de nivel). El término 10/9 hace que la RD **tienda al 90%**, nunca lo alcance. | [Maxroll — In-depth Defense Guide](https://maxroll.gg/d4/getting-started/defenses-for-beginners) | 16 ago 2026 | unica |
| A3 | Ejemplo numérico del propio Maxroll de cuánta resistencia se maneja: afijo de anillo **+650 Resistencia al Fuego**, implícito de joyería **250 Todas las Resistencias**, gema **+2000 Resistencia al Fuego**, Inteligencia **+0.4 Todas las Res. por 1 INT**. Total del ejemplo: **19 994 Res. al Fuego**. | ver celda | [Maxroll — In-depth Defense Guide](https://maxroll.gg/d4/getting-started/defenses-for-beginners) | 16 ago 2026 | unica |
| A4 | Referencia de conversión: **7 000 de Res. al Fuego → 78,53% RD a nivel 70** | 7000 → 78,53% | [Maxroll — In-depth Defense Guide](https://maxroll.gg/d4/getting-started/defenses-for-beginners) | 16 ago 2026 | unica |
| A5 | Hay **dos cubos** de resistencia: aditivo (implícitos de joyería, afijos, gemas, Inteligencia) y multiplicativo (aspectos, nodos de Paragón, auras). Los "+50%[+] Resistencia al X" de los aspectos son del cubo multiplicativo, **no** afijos planos. | — | [Maxroll — In-depth Defense Guide](https://maxroll.gg/d4/getting-started/defenses-for-beginners) | 16 ago 2026 | unica |

> **Por qué esto importa más que cualquier cifra:** si una guía te habla de "+35% de resistencia única" o de "llegar al tope del 70%", está usando el modelo pre-S11. Las cifras pueden parecer verosímiles y ser basura porque el marco es de otra versión del juego. Ver *Contradicciones C3*.

### B. El cambio de resistencias en 3.2.1

| # | Dato | Cifra | Fuente | Fecha | Evidencia |
|---|------|-------|--------|-------|-----------|
| B1 | Texto literal de la nota: *"Significantly increased the value of Single Resistance affixes on equipment, Charms, and Tempering recipes. **Single Resistance affixes are now 7 times the value of All Resistance affixes.** Re-tuned All Resistance Tempering values to align with other All Resistance affixes."* | **7×** | [Blizzard — notas 3.2.1, sección Item Updates > Resistances](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 12 sep 2026 | **oficial** |
| B2 | Mismo texto reproducido íntegro | 7× | [Maxroll — Hell's Legacy 3.2.1 Patch Notes](https://maxroll.gg/d4/news/diablo-4-3-2-1-patch-notes) (autor: snail) | Última act. 12 sep 2026 | corroborado |
| B3 | Mismo texto reproducido íntegro | 7× | [Icy Veins — Buffed Resistances and Increased Legendary and Mythic Unique Drop Rates](https://www.icy-veins.com/d4/news/buffed-resistances-and-increased-legendary-and-mythic-unique-drop-rates-diablo-4-season-15-item-updates/) (Miril) | Publicada 13 sep 2026 | corroborado |
| B4 | **Prueba numérica de la proporción 7:1 con cifras oficiales.** Los Soul Splinters (gemas de temporada) dan por rareza Mágico/Raro/Legendario/Único: resistencia a **un** elemento `250 / 175 / 2625 / 4375`; "Resistencia a Todos los Elementos" `35 / 50 / 375 / 625`. | 2625÷375 = **7,0**; 4375÷625 = **7,0** | [Blizzard — The 3.2.0 PTR: What You Need to Know](https://news.blizzard.com/en-us/article/24292852/the-3-2-0-ptr-what-you-need-to-know) | 30 jul 2026 (**PTR**) | oficial (PTR) |
| B5 | Magnitud del salto, medida por jugadores en el PTR: un afijo de resistencia a un elemento estaba **capado en 630 en vivo** y llegaba a **~3 000 en el PTR** (≈5×). | 630 → ~3000 | [Icy Veins — Players Found a Resistance Change Blizzard Never Announced](https://www.icy-veins.com/d4/news/diablo-4-players-found-a-resistance-change-blizzard-never-announced/) (Fallen Mesiah) | Publicada 9 ago 2026 (**PTR**) | unica (PTR, reporte de jugadores) |
| B6 | Cambio **no anunciado** del PTR: los dijes (Charms) podían por fin sacar **resistencias y +rangos de habilidad a la vez**, lo que antes era imposible. | — | [Icy Veins — Players Found a Resistance Change...](https://www.icy-veins.com/d4/news/diablo-4-players-found-a-resistance-change-blizzard-never-announced/) | 9 ago 2026 (**PTR**) | sinconfirmar (no aparece en las notas 3.2.1) |
| B7 | **Stone of Jordan hace que todas tus resistencias igualen a la más alta.** Es la pieza que convierte el buff 7× en resistencia total. | — | [Icy Veins — Players Found a Resistance Change...](https://www.icy-veins.com/d4/news/diablo-4-players-found-a-resistance-change-blizzard-never-announced/) | 9 ago 2026 (**PTR**) | unica (PTR) |
| B8 | Confirmación indirecta oficial de que Stone of Jordan tiene lógica de daño/elemento: corrección de bug *"Fixed an issue where Stone of Jordan did not properly interact with Holy damage effects."* | — | [Blizzard — notas 3.2.1, PTR Bug Fixes](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 12 sep 2026 | oficial |
| B9 | **Tope de resistencia: no cambia, porque no existe como tope duro.** En las notas 3.2.1 no hay ni una línea sobre topes de resistencia. Lo único que limita es la asíntota del 90% de la fórmula (A2). | — | [Blizzard — notas 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) (ausencia) + [Maxroll Defense Guide](https://maxroll.gg/d4/getting-started/defenses-for-beginners) | 12 sep / 16 ago 2026 | oficial (por ausencia) + unica |
| B10 | Aspectos que ahora regalan resistencia (cubo multiplicativo), como referencia de que la temporada empuja hacia resistencias: *Deeper Shadows* `+50% Res. Sombra`; *Immolation* `+50% Res. Fuego`; *Wyward's* `Gain 50%[+] Lightning Resistance`; *Fathomless Dark* y *Scorching Heat* suben a `65-85%` de la res. correspondiente como Damage Resistance. | ver celda | [Blizzard — notas 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 12 sep 2026 | oficial |

**Lectura para el jugador (inferencia mía, no dato de fuente):** con 7:1 a favor del elemento único y Stone of Jordan igualando todo a la más alta, un afijo de "Resistencia a Todos los Elementos" pasa a valer ~1/7 de la casilla. No es que "muera": es que el coste de oportunidad de esa casilla se multiplica por siete. Lo que **no se puede afirmar** es si tus templados actuales se recalculan solos (ver *Huecos H1*).

### C. Los 9 "Legacy Uniques" (permanentes, Eternal y Temporada)

Lista **oficial y final** (los marcados con `*` existen además como **Dije Único / Unique Charm**):

| # | Objeto | Ranura | Clases | Charm | Poder conocido |
|---|--------|--------|--------|-------|----------------|
| C1 | **Leoric's Crown** | Yelmo | Todas | No | *"The item counts as Jewelry and increases the effect of any gem socketed into the helm by 75-100%"* — **oficial (PTR)**. Al contar como joyería admite **Soul Splinters**, confirmado por el bug fix *"Leoric's Crown did not apply Soul Splinter Effects"* |
| C2 | **Nemesis Bracers** `*` | Guantes | Todas | Sí | Genera **packs de élites al interactuar con un santuario** (deducido del bug fix oficial *"the Nemesis Bracers did not spawn elite packs when interacting with a shrine"*). Sin texto de afijo publicado |
| C3 | **Stone of Jordan** `*` | Anillo | Todas | Sí | Iguala todas las resistencias a la más alta (ver B7, fuente única PTR). Interactúa con efectos de **daño Sagrado** (bug fix oficial) |
| C4 | **Squirt's Blouse** `*` | Pecho (el *Squirt's Necklace* convertido en pieza de pecho) | Todas | Sí | Tiene **acumulaciones de buff** (bug fix oficial: *"buff stacks from Squirt's Blouse could randomly fall off"*). Sin texto publicado |
| C5 | **Arioc's Needle** `*` | Alabarda 2M | Bárbaro, Druida, Spiritborn | Sí | Sin texto publicado en fuente preferente |
| C6 | **Henri's Perquisition** `*` | Foco de mano secundaria | Hechicera, Nigromante, Brujo | Sí | Sin texto publicado. Bug fix: *"had an additional Thorns affix"* (se le quitó) |
| C7 | **In-Geom** `*` | Espada 1M | Bárbaro, Druida, Pícaro, Nigromante, Paladín, **Hechicera**, Brujo | Sí | **Reducción de enfriamiento de 15 s** (bug fix oficial: *"In-Geom's cooldown reduction was 12 seconds instead of 15"*). Condición de disparo no publicada |
| C8 | **The Furnace** `*` | Maza 2M | Bárbaro, Druida, Nigromante, Paladín, Brujo | Sí | Sin texto publicado |
| C9 | **Messerschmidt's Reaver** | Hacha 2M | Bárbaro, Druida, Nigromante, Paladín, Brujo | No | **No era testeable en el PTR.** Sin texto publicado. Bug fix: *"had incorrect class availability restrictions"* |

- Fuente de la lista y de las clases: [Blizzard — Celebrate 30 Years of Diablo in Season of Hell's Legacy, sección "Legacy Uniques"](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) — 12 sep 2026 — **oficial**.
- Corroborada literalmente (misma lista, mismas clases, incluida Hechicera en In-Geom) por [Maxroll — Season of Hell's Legacy Guide](https://maxroll.gg/d4/resources/season-guide) (Avarilyn, última act. 13 sep 2026) → **corroborado**.
- Lista de los 7 convertibles en Dije Único, literal en notas: [Blizzard 3.2.1 > Item Updates > Talisman](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) — **oficial**.
- Texto de Leoric's Crown: [Blizzard — The 3.2.0 PTR](https://news.blizzard.com/en-us/article/24292852/the-3-2-0-ptr-what-you-need-to-know), 30 jul 2026 — **oficial pero de PTR**.

**Cómo se consiguen:** no hay método de farmeo dirigido publicado. Blizzard los describe como *"typical Uniques in terms of power and utility"* y *"permanent additions available in all versions of Diablo IV"* → caen como cualquier Único, y por tanto les aplica *"All Unique items are now available to drop at level 1, and in any Difficulty"* (D1). Los 7 con versión Charm caen además por el sistema Talisman. **Evidencia: oficial para el marco, hueco para el ratio de caída concreto.**

### D. Drops

| # | Dato | Cifra | Fuente | Fecha | Evidencia |
|---|------|-------|--------|-------|-----------|
| D1 | *"All Unique items are now available to drop at level 1, and in any Difficulty."* | nivel 1, cualquier dificultad | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 12 sep 2026 | **oficial** |
| D2 | Subida de caída de Legendarios en **Tormento I–V**; Tormento VI y superiores **sin cambios**. Nota del dev: reducir la dependencia de subir Legendarios al azar en la Cuba para completar el Códice de Poder | T I–V | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 12 sep 2026 | **oficial** |
| D3 | **Míticos más deterministas:** los que sueltan los Jefes de Guarida (Initiate y Greater) y los que se eligen del Botín de Belial **solo saldrán del pool de Únicos de ese jefe**. Matiz oficial: los jefes también sueltan botín genérico aleatorio, así que **queda una probabilidad pequeña** de Míticos fuera del pool | — | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 12 sep 2026 | **oficial** |
| D4 | Tasas de Mítico: *"Slightly increased"* en Greater Lair Bosses; **Initiate Lair Bosses igualados a Greater**; *"Slightly increased"* en Belial; subida de la probabilidad desde **fuentes aleatorias** | **sin porcentajes** | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 12 sep 2026 | **oficial** (cualitativo) |
| D5 | **Echo of Mephisto**: sube la calidad global del botín e incluye **un Mítico garantizado** (en la nota oficial aparece con la errata *"Mtyhic"*) | 1 garantizado | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 12 sep 2026 | **oficial** |
| D6 | Recompensas de Rango de Temporada relevantes a itemización: hasta **10 Chispas Resplandecientes** (más las de las cajas) y **5 Mythic Unique Caches** | 10 / 5 | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 12 sep 2026 | **oficial** |

### E. Crafteo de Míticos (determinista)

| # | Dato | Fuente | Fecha | Evidencia |
|---|------|--------|-------|-----------|
| E1 | **Tres vías** para crear un Mítico: (1) Cuba Horadrim → *Upgrade Direct Item to Mythic*; (2) Joyero → *Rune Crafting > Mythic Uniques*; (3) Herrero → *Forge > Mythic Cache* | [Blizzard — sección "Customize with Mythic Unique Crafting Updates"](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 12 sep 2026 | **oficial** |
| E2 | *Upgrade Direct Item to Mythic*: más caro que las otras, pero **transferencia 1:1 total** — *"the random factors are gone"*. Metes un Tibault's Will con los afijos que quieres, templado y maestría hechos, y sale su versión Mítica **con todos los afijos y modificaciones intactos** | [Blizzard](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 12 sep 2026 | **oficial** |
| E3 | **Restricción dura:** no se puede usar la receta sobre un objeto **Unmodifiable** → *"beware of Transfiguring your precious Mythic Unique candidate!"* | [Blizzard](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 12 sep 2026 | **oficial** |
| E4 | Los Míticos hechos con esa receta llevan etiqueta **"Crafted"** y **solo se puede llevar equipado UNO** con esa etiqueta. Los del Joyero y los de la caja del Herrero **no** la llevan → se pueden combinar varios Míticos | [Blizzard](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 12 sep 2026 | **oficial** |
| E5 | **Vuelta atrás respecto al PTR:** en el PTR 3.2.0 los *Iconic Mythics* iban a tener versión Única; el feedback lo tumbó (*"this cheapened the value of Iconic Mythics"*) → **los Iconic Mythics siguen siendo solo de calidad Mítica**. Además se añade una **segunda caja del Herrero que solo tira Iconic Mythics**, al mismo coste que la de Mythic Uniques | [Blizzard, Developer's Note](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) vs [Blizzard PTR 3.2.0](https://news.blizzard.com/en-us/article/24292852/the-3-2-0-ptr-what-you-need-to-know) | 12 sep vs 30 jul 2026 | **oficial** (PTR revertido) |
| E6 | **Dijes Míticos:** *"Any Unique Charm in game will have a low chance to drop as a Mythic Unique. There is no crafting method for Mythic Unique charms, and like regular Unique Charms, there isn't a specific method for target farming."* Propiedades del dije al **máximo** y poder Único **"significantly buffed"** | [Blizzard PTR 3.2.0](https://news.blizzard.com/en-us/article/24292852/the-3-2-0-ptr-what-you-need-to-know) | 30 jul 2026 (**PTR**) | oficial (PTR) — **no repetido en las notas finales 3.2.1** |
| E7 | Los Dijes Míticos **no son nuevos de la S15**: aparecieron sin documentar en el parche **3.1.1** (14 jul 2026), y entonces el efecto Único **no** estaba buffeado, solo los stats al máximo | [Icy Veins — Mythic Unique Charms Shadow Dropped With Patch 3.1.1](https://www.icy-veins.com/d4/news/mythic-unique-charms-shadow-dropped-with-diablo-4-patch-3-1-1/) (Miril) | 14 jul 2026 | unica |

### F. Las dos recetas nuevas de la Cuba Horadrim

| # | Receta | Qué hace exactamente | Fuente | Evidencia |
|---|--------|----------------------|--------|-----------|
| F1 | **Affix Value Reroll** | Rerollea **todos los afijos base** tanto de **equipo** como de **objetos de Talismán (Charms y Seals)**, **protegiendo**: Greater Affixes, cualquier afijo Encantado, Templados (Tempers) y **Transfiguraciones** — *"as long as that Transfigured item is not Unmodifiable"* | [Blizzard — "Hone Your Gear with New Horadric Cube Crafting Recipes"](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy), 12 sep 2026 | **oficial** |
| F2 | **Horadric Reroll** | Solo para **Charms y Seals de calidad Legendaria o superior**. **Aleatoriza por completo** todos los afijos base, **sin tocar** los Bonus de Set ni los poderes de dije Único/Mítico. A diferencia de la anterior, **no cambia los afijos de Bonus de Set de los Seals** — solo los afijos base | [Blizzard](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy), 12 sep 2026 | **oficial** |

Corroboración de ambas: [Maxroll — Season of Hell's Legacy Guide](https://maxroll.gg/d4/resources/season-guide) (13 sep 2026) → **corroborado**.

Resto de cambios de la Cuba en 3.2.1 (todos [oficiales, 12 sep 2026](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy)):
- Se aclara el comportamiento y la descripción de los **Tuning Prisms** al usarlos con **Chaotic Rerolls**.
- **Materiales:** baja el peso de caída del **Pure Primordial Dust** (porque suben los Legendarios base); el **Coarse** se vuelve **menos** común al subir dificultad; **Refined, Volatile, Pure, Enhanced y Attuned** se vuelven **más** comunes al subir dificultad. Los materiales de Cuba de las *Cube Materials Caches* suben **~2-3×**.
- **Bug fixes:** ya se pueden rerollear los poderes de **Dijes Únicos y Objetos Únicos** en la Cuba; y *"Fixed an issue where Mythic Amulets could receive a non-maximum Unique Affix value when first Transfigured."*

### G. Templado, Maestría y calidad de objeto

| # | Dato | Fuente | Evidencia |
|---|------|--------|-----------|
| G1 | **Templado (Tempering):** el único cambio de sistema es el buff 7× a las recetas de resistencia única y el **re-tuneo de los valores de templado de "Todas las Resistencias"** (B1). Aparte, **un solo bug fix**: *"Fixed an issue where Maximum Resolve Stacks was uncapped when Tempering."* Nada de cargas, nada de listas de recetas, nada de probabilidades | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | **oficial** |
| G2 | **Maestría (Masterworking): CERO cambios en 3.2.1.** No hay sección de Masterworking en las notas. Las únicas menciones son colaterales: la receta 1:1 de Mítico conserva la maestría (E2), la bendición *Urn of Masterworking* (más Obducita) y materiales de maestría como recompensa de Rango | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) (por ausencia) | **oficial** (por ausencia) |
| G3 | **Calidad / Poder de Objeto (Normal-Sagrado-Ancestral, Item Power, Greater Affixes): CERO cambios.** No hay ni una línea. Greater Affixes solo se mencionan como cosa *protegida* por la nueva receta F1 | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) (por ausencia) | **oficial** (por ausencia) |
| G4 | **Ocultista:** coste de Almas Olvidadas para encantar objetos **Ancestrales de 25 → 10** | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | **oficial** |
| G5 | **Joyero:** Gemas Reales **30 → 10** Almas Olvidadas; Gemas Grandiosas **300 → 50** | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | **oficial** |
| G6 | **Transfiguración:** sigue siendo lo que decide si una pieza se puede seguir editando. La nota lo confirma dos veces: la receta de Mítico 1:1 **no** funciona sobre Unmodifiable (E3), y el *Affix Value Reroll* protege Transfiguraciones **solo si el objeto no es Unmodifiable** (F1) | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | **oficial** |

---

## Huecos

- **H1 — LO MÁS IMPORTANTE Y NO RESUELTO: no hay ninguna fuente, oficial ni preferente, que diga si el cambio de resistencias se aplica retroactivamente a los afijos y templados de objetos ya equipados, o solo a lo que caiga nuevo.** Lo he buscado en las notas oficiales, en el blog de temporada, en el artículo del PTR, en Maxroll, en Icy Veins y en el hilo del foro oficial ["Full S15 Patch Notes are live"](https://us.forums.blizzard.com/en/d4/t/full-s15-patch-notes-are-live-more-selig-and-tibs-nerfs-more/266249) (12-14 sep 2026, **sin post azul** y **sin que ningún jugador lo discuta**). **No lo sé, y no lo voy a deducir.** Se resuelve mirando el objeto en el juego después de las 16:30 UTC de hoy.
- **H2** — El "re-tuneo" del templado de **Todas las Resistencias**: no hay **ni una sola cifra**, ni antes ni después, ni dirección (subida o bajada). "Align with other All Resistance affixes" admite las dos lecturas.
- **H3** — **Valores finales del afijo de resistencia única en 3.2.1**: no encontrados. Las únicas cifras que existen son del PTR (630 → ~3000, B5) y del reporte de jugadores, no de una tabla oficial. Ninguna fuente preferente publica tabla de rangos por Normal/Sagrado/Ancestral con fecha dentro del parche.
- **H4** — **Texto de afijo de 8 de los 9 Legacy Uniques.** Solo Leoric's Crown tiene texto publicado (y es de PTR). De los demás solo se deduce el mecanismo por los bug fixes. Ninguna base de datos preferente con fecha dentro del parche los tiene todavía: [Maxroll — Unique and Mythic Unique Items](https://maxroll.gg/d4/wiki/uniques) está actualizada a **23 may 2026** y no los incluye.
- **H5** — **Porcentajes concretos de las subidas de Mítico** ("slightly increased", "increased"): Blizzard no publica números. Sin datamine fiable citable, esto se queda cualitativo.
- **H6** — **Coste en materiales de las dos recetas nuevas de la Cuba.** [Maxroll — Horadric Cube](https://maxroll.gg/d4/resources/horadric-cube) está actualizada a **26 ago 2026** (parche 3.1.x) y no las recoge. Ninguna fuente preferente da los costes.
- **H7** — **Cómo se farmean dirigidamente los Legacy Uniques** (¿entran en tablas de jefes de guarida? ¿en el pool del Botín de Belial? ¿en las Waking Nightmares?). No publicado. Dado D3, saber si están en el pool de algún jefe cambia por completo el plan de farmeo.
- **H8** — Si el cambio del PTR de **dijes con resistencia + rangos de habilidad a la vez** (B6) llegó a la versión final: no aparece en las notas 3.2.1 ni en ningún sitio con fecha posterior al 12 sep.
- **H9** — Si los **Dijes Míticos con poder Único buffeado** (E6) están en 3.2.1: la promesa es del blog de PTR del 30 jul; las notas finales del 12 sep **no la repiten**. Sin fuente en el parche vivo.
- **H10** — **Ninguna de las cifras de rating de resistencia está verificada en el juego real de la S15.** La fórmula (A2) y las magnitudes (A3, A4) vienen de una guía actualizada el 16 ago 2026, es decir, **del parche 3.1.x**, no del 3.2.1. Es lo mejor disponible hoy, pero no es del parche vivo.

---

## Contradicciones

### C1 — ¿Nueve o diez Legacy Uniques? (Ring of Royal Grandeur fue cortado)

- **Versión A (PTR, 30 jul 2026):** [Icy Veins — Legacy Uniques From Previous Diablo Games Returning in Season 15](https://www.icy-veins.com/d4/news/legacy-uniques-from-previous-diablo-games-returning-in-season-15/) abre con *"Ten new Uniques are being added"* y lista **10**, incluyendo **Ring of Royal Grandeur (Ring)** entre los de todas las clases.
- **Versión B (final, 12 sep 2026):** [Blizzard](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) dice *"nine legacy Uniques"* y lista **9**. **Ring of Royal Grandeur no está.** Lo corrobora [Maxroll](https://maxroll.gg/d4/resources/season-guide) (13 sep) y lo confirma por ausencia la sección Talisman de las notas 3.2.1.
- **Prueba de que la página de Blizzard fue editada:** su propio artículo de PTR ([30 jul 2026](https://news.blizzard.com/en-us/article/24292852/the-3-2-0-ptr-what-you-need-to-know)) hoy dice *"**Nine** legacy Uniques have been uncovered"* pero acto seguido *"**Five** of them will be usable by all classes"* y **solo lista cuatro**; y más abajo sigue diciendo *"Eight of the **ten** legacy Uniques will also have Charms"* cuando solo lista **siete**. Blizzard cambió el número en un sitio y se dejó los otros dos.
- **Conclusión:** Ring of Royal Grandeur **se cayó entre el PTR 3.2.0 y la versión final 3.2.1**. Icy Veins reprodujo la versión vieja y no la ha corregido. **Manda Blizzard: son nueve, sin RoRG.** (Ejemplo de libro de cómo un artículo de PTR sin fecha visible envenena la información.)

### C2 — Clases de In-Geom

- **Versión A (PTR / Icy Veins, 30 jul):** Bárbaro, Druida, Pícaro, Nigromante, Paladín, Brujo — **6 clases, sin Hechicera**.
- **Versión B (final / Blizzard 12 sep + Maxroll 13 sep):** las 6 anteriores **+ Hechicera** = **7 clases**.
- **Manda B** (fuente oficial y más reciente, corroborada).

### C3 — El marco de porcentajes: cifras que circulan y que NO he podido verificar (probablemente de un modelo muerto)

Al buscar "single resistance 7 times" aparecen resumidas cifras del tipo: *"un afijo de resistencia única da hasta **+35%** en un objeto Normal totalmente mejorado, **+48%** en Sagrado y **+65%** en Ancestral, frente a **+9% / +12% / +16%** de Todas las Resistencias"*.

- **No he encontrado esas cifras en NINGUNA fuente preferente con fecha dentro del parche vivo.** No están en la nota oficial, ni en Maxroll, ni en Icy Veins. Las páginas que las sirven son de la lista vetada o similares (fextralife, purediablo, mistermenplays, d4guides).
- **Se contradicen con la propia nota oficial:** 35/9 = 3,9 · 48/12 = 4,0 · 65/16 = 4,06. Eso es una proporción **4:1**, no la **7:1** que dice Blizzard.
- **Y el marco entero es de otra versión del juego:** los afijos de resistencia dejaron de ser porcentajes en la **Temporada 11** (A1). Un "+35% de resistencia en un objeto Normal" no puede existir hoy.
- **Veredicto: no usar.** Si aparecen en cualquier borrador de la guía, se tachan. Este es exactamente el caso de "todas las fuentes coinciden en el marco y discrepan en los números, y el marco es el que está podrido".

### C4 — Errata aritmética en la tabla oficial de Soul Splinters

Blizzard publica resistencia a un elemento como `250 / 175 / 2625 / 4375` y "a Todos los Elementos" como `35 / 50 / 375 / 625` ([PTR, 30 jul 2026](https://news.blizzard.com/en-us/article/24292852/the-3-2-0-ptr-what-you-need-to-know)). Multiplicando la segunda por 7 sale `245 / 350 / 2625 / 4375`. Cuadra en tres de cuatro peldaños; el segundo, **175**, debería ser **350**, y además rompe la progresión (sería menor que el peldaño Mágico anterior). **Inferencia mía, no dato de fuente: es una errata de la tabla, y la regla 7× se sostiene.** Cifra a verificar en el juego.

### C5 — Dijes Míticos: ¿novedad de la S15 o ya estaban?

- **Versión A (Blizzard, PTR 30 jul):** se presentan como novedad del sistema Talismán: *"Charms will now be available in Mythic quality"*, con las propiedades al máximo y el poder Único **"significantly buffed"**.
- **Versión B (Icy Veins, [14 jul 2026](https://www.icy-veins.com/d4/news/mythic-unique-charms-shadow-dropped-with-diablo-4-patch-3-1-1/)):** ya cayeron sin documentar en el parche **3.1.1**, con los stats al máximo pero **el efecto Único al mismo valor que un dije Único normal**.
- **Compatibles si** lo nuevo de la S15 es únicamente el buff del poder Único. **Pero eso no aparece en las notas finales 3.2.1.** Queda como *sinconfirmar* (H9).

### C6 — PTR 3.2.0 vs final 3.2.1: lo que cambió por el camino

| Tema | PTR 3.2.0 (30 jul) | Final 3.2.1 (12 sep) |
|------|--------------------|----------------------|
| Vías para crear Míticos | **Dos** (Cuba + Joyero) | **Tres** (Cuba + Joyero + caja del Herrero) |
| Iconic Mythics | Tendrían **versión Única** | **Revertido**: siguen siendo solo Míticos |
| Caja del Herrero | Tiraba Mythic Uniques **o** Iconic Mythics mezclados | Se **añade una segunda caja** que solo tira Iconic Mythics, al mismo coste |
| Legacy Uniques | 10 (con Ring of Royal Grandeur) | **9** (sin él) |
| Uniques a nivel 1 | No mencionado | **Sí**, oficial |

Ambas columnas del mismo dominio (news.blizzard.com), así que la discrepancia es real y deliberada, no error de fuente. **Regla: para la guía manda siempre la columna de la derecha.**

---

## Fuentes usadas (con fecha comprobada)

| Fuente | URL | Fecha verificada | Uso |
|--------|-----|------------------|-----|
| Blizzard — *Celebrate 30 Years of Diablo in Season of Hell's Legacy* (incluye las **notas 3.2.1 completas**) | https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy | `datePublished 2026-09-12T18:15:00Z` | Fuente primaria de todo lo oficial |
| Blizzard — *The 3.2.0 PTR: What You Need to Know* | https://news.blizzard.com/en-us/article/24292852/the-3-2-0-ptr-what-you-need-to-know | `datePublished 2026-07-30T17:00:00Z` | **PTR** — usar solo con etiqueta |
| Maxroll — *Hell's Legacy – 3.2.1 Patch Notes* (autor: snail) | https://maxroll.gg/d4/news/diablo-4-3-2-1-patch-notes | Última act. 12 sep 2026 | Corroboración literal |
| Maxroll — *Season of Hell's Legacy Guide* (Avarilyn) | https://maxroll.gg/d4/resources/season-guide | Última act. 13 sep 2026 | Corroboración de features |
| Maxroll — *In-depth Defense Guide* (Icytroll/Northwar/Avarilyn) | https://maxroll.gg/d4/getting-started/defenses-for-beginners | `dateModified 2026-08-16` | **El marco** de resistencias (parche 3.1.x) |
| Icy Veins — *Buffed Resistances and Increased ... Drop Rates* (Miril) | https://www.icy-veins.com/d4/news/buffed-resistances-and-increased-legendary-and-mythic-unique-drop-rates-diablo-4-season-15-item-updates/ | `datePublished 2026-09-13` | Corroboración |
| Icy Veins — *Players Found a Resistance Change Blizzard Never Announced* (Fallen Mesiah) | https://www.icy-veins.com/d4/news/diablo-4-players-found-a-resistance-change-blizzard-never-announced/ | `datePublished 2026-08-09` | **PTR** — 630→3000, Stone of Jordan |
| Icy Veins — *Legacy Uniques From Previous Diablo Games Returning in S15* (Miril) | https://www.icy-veins.com/d4/news/legacy-uniques-from-previous-diablo-games-returning-in-season-15/ | `datePublished 2026-07-30` | **PTR, desactualizada** (ver C1) |
| Icy Veins — *Mythic Unique Charms Shadow Dropped With Patch 3.1.1* (Miril) | https://www.icy-veins.com/d4/news/mythic-unique-charms-shadow-dropped-with-diablo-4-patch-3-1-1/ | `datePublished 2026-07-14` | Antecedente de dijes míticos |
| Foro oficial — *Full S15 Patch Notes are live* | https://us.forums.blizzard.com/en/d4/t/full-s15-patch-notes-are-live-more-selig-and-tibs-nerfs-more/266249 | 12-14 sep 2026 | Comprobado: **sin post azul**, nadie discute retroactividad |

**Descartadas por la regla 2** (aparecieron en búsquedas y no se han usado para ningún valor): fextralife, purediablo, mistermenplays, d4guides.gg, sportskeeda. **Descartadas por fecha** (fuera del parche vivo, aunque sean preferentes): Maxroll *Uniques wiki* (23 may 2026), Maxroll *Horadric Cube* (26 ago 2026), Maxroll *Talisman* (28 jun 2026), Maxroll *Equipment* (25 jul 2026), guías de Tempering/Masterworking de Icy Veins (etiquetadas "Season 14").
