# Refutación adversarial — "Runas y Palabras Rúnicas (Runes & Runewords) — estado real en el parche 3.1.3"

**Informe auditado:** `investigacion/crudo/exp-runas.md`
**Fecha de la verificación:** 20 agosto 2026
**Veredicto:** **PARCIAL** — la parte mecánica y numérica del informe resiste el ataque casi entera (huecos, límite de 2 palabras rúnicas, Teb/Wat, Ur eliminada, cambios del 3.1.0, tablas de crafteo, planificador de Maxroll): todo confirmado contra HTML crudo. **Pero el hallazgo #2 del resumen ejecutivo es falso tal como está redactado**, y con él se cae el razonamiento de §7.2 y la recomendación de §7.3 sobre Teb/Wat — que es justo lo que el encargo preguntaba.

**Método:** he descargado el HTML crudo (`curl`, sin intermediarios) de todas las páginas citadas y he leído el texto original en vez de fiarme de la transcripción del informe; he descargado y parseado el JSON del planificador de Maxroll (`planners.maxroll.gg/profiles/d4/7xf3kf0h`, 214 ítems, 6 perfiles) y he comprobado runa a runa qué lleva equipado cada variante; y he abierto la página **oficial** de notas de parche de Blizzard, que el informe no usó. 9 búsquedas web, 22 páginas abiertas. Ninguna fuente vetada respalda ningún dato de esta refutación.

---

## 1. 🔴 ERROR GRAVE — "ninguna guía viva de nigromante de esbirros usa Teb/Wat" es **falso**

El informe abre con esto (resumen ejecutivo, punto 2):

> *"La premisa del encargo es medio falsa. Teb y Wat existen y funcionan tal como se dice, **pero NINGUNA guía viva de nigromante de ESBIRROS de la S14 los usa.** Teb/Wat aparecen en las guías de Sever y de Reaper/Naz Mages (summoner de sombra), no en la de esbirros pura."*

**Tres guías vivas de Icy Veins, todas de Temporada 14, montan `Igni + Wat`, y las tres son builds de esbirros.** No son "summoner de sombra": son ejércitos de Magos Esqueléticos, Guerreros Esqueléticos y Gólem — exactamente lo que juega este jugador.

| Guía (Icy Veins, S14) | Barra de habilidades | Únicos requeridos | Palabras rúnicas |
|---|---|---|---|
| **Naz Mages** (S-Tier) [naz] | Mago Esquelético, Sever, Gólem, **Guerrero Esquelético**, Ejército de los Muertos, Hemorragia | The Hand of Naz, **Blood Moon Breeches**, Signet of Pelghain, **The Undercrown** | **Nagu Que** — *"Endgame Important"* · **Igni Wat** — *"Endgame Important — Invokes the Necromancer's Decrepify"* |
| **Reaper Summoner** (A-Tier) [reap] | **Guerrero Esquelético**, Sever, **Mago Esquelético**, **Gólem**, Blight, Ejército de los Muertos | Blood Moon Breeches, Deathgrip, **The Undercrown**, Pact of Bone | **Nagu Que** · **Igni Wat** — *"Endgame Important — Applies Decrepify curse early…"* |
| **Summoner Leveling** [ivsum] | **Mago Esquelético, Guerrero Esquelético, Gólem**, Sever, **Doncella de Hierro**, Ejército de los Muertos | — | *"Nagu + Ceh / Cir + Ceh"* y **"Igni + Wat"** |

Textos literales, del HTML crudo:

> *"**Igni Wat** — Endgame Important — Invokes the Necromancer's Decrepify."* — [Naz Mages][naz]
> *"Iron Maiden and Decrepify are activated via Blood Moon Breeches and **via Wat Runeword** so they are not needed on the skill bar."* — [Reaper Summoner][reap]
> *"**Decrepify is activated via Wat Runeword if obtained, making it not needed on the skill bar.**"* — [Summoner Leveling][ivsum]

**Por qué importa para ESTE jugador y no es una discusión de etiquetas:** la guía de *Naz Mages* pide **The Undercrown** y **Blood Moon Breeches**, los mismos dos únicos que el planificador de Maxroll monta en las variantes *Warrior* y *Mages* del informe (§7.1). Es la misma build vista por dos webs; una monta Wat y la otra no. El informe convirtió ese desacuerdo real (**1 fuente en contra, 3 a favor**) en una unanimidad inventada.

**Redacción correcta:** *"Las guías de esbirros de **Maxroll** no usan Teb ni Wat; las tres guías de esbirros de **Icy Veins** montan `Igni + Wat` como pieza de endgame. Hay desacuerdo entre las dos casas."* Eso es lo que aguanta la evidencia.

Nota de honestidad hacia el informe: **el propio informe cita Naz Mages y Reaper en §6.3** y ve el `Igni + Wat`. El error no es de investigación, es de titular: el resumen ejecutivo dice lo contrario de lo que el cuerpo del documento demuestra.

---

## 2. 🔴 ERROR DE MODELO — Blood Moon Breeches **no** es un "sistema de reparto de maldiciones" que haga redundante a Wat

Es el argumento entero de §7.2, y el informe lo construye sobre una frase de marketing de Maxroll sin ir a leer el afijo del ítem.

**Lo que el informe usa como prueba:**
> *"Blood Moon Breeches is your Curse delivery system as your minions constantly have the potential to apply both curses to any mob they hit."* — [maxroll minion endgame][minend]

y concluye: *"en esbirros, las maldiciones ya las reparten los propios esbirros… Gastar una de tus dos palabras rúnicas en Teb o Wat sería pagar dos veces por lo mismo."*

**Lo que dice el afijo del pantalón, literal, en dos guías distintas:**
> *"Your Summons have a **[7 – 10%] chance** to **randomly** inflict Decrepify **or** Iron Maiden when they deal damage. You deal x[50 – 60%] increased Critical Strike Damage to enemies affected by your Curses."* — [Reaper Summoner][reap]; idéntico en [Naz Mages][naj]

Es decir: **7–10% de probabilidad, y encima elige al azar entre las dos maldiciones.** No es un sistema de reparto, es una lotería. Fíjate además en la segunda mitad del afijo: el multiplicador de +50–60% de Daño Crítico **solo se cobra sobre enemigos maldecidos**, así que la fiabilidad de la maldición es lo que decide cuánto vale el pantalón.

**Y el propio informe cita la frase que lo refuta, sin darse cuenta.** En §6.3 transcribe correctamente de Maxroll:
> *"**While Blood Moon Breeches can be triggered by your Minions, the combo of Teb/Wat runes make for better Curse uptime and more consistent automation of the build**."* — [maxroll Sever, 28 jul 2026][sev]

Maxroll dice literalmente que Teb/Wat **son mejores** que Blood Moon Breeches para mantener las maldiciones. El informe lo pega en §6.3 y en §7.2 argumenta lo contrario. **Contradicción interna con la misma cita.**

Esto es exactamente el fallo que la regla 6 del encargo pide cazar: un marco conceptual ("las maldiciones ya están cubiertas") heredado de una frase de guía, aceptado sin verificar los números del ítem.

---

## 3. 🟠 La recomendación de §7.3 sobre `Igni + Wat` está **invertida**

El informe escribe:

> *"**Igni + Wat** — Casco/Pecho — **Solo si abandona la Doncella de Hierro de la barra**"*
> y *"él ya lleva Doncella de Hierro en la barra, así que Teb le duplicaría algo que ya hace. Wat sí le añadiría una segunda maldición… Pero ninguna guía de esbirros de la S14 lo recomienda"*.

Las guías dicen lo opuesto: Wat **es** lo que te permite quitar la maldición de la barra, no algo que exija sacrificar nada.

> *"Iron Maiden and Decrepify are activated via Blood Moon Breeches and via Wat Runeword **so they are not needed on the skill bar**."* — [Reaper Summoner][reap]
> *"Decrepify is activated via Wat Runeword if obtained, **making it not needed on the skill bar**."* — [Summoner Leveling][ivsum]

El jugador tiene **Doncella de Hierro ocupando un hueco de barra** (dato del encargo). La lectura correcta para él es: `Igni + Wat` (+ Blood Moon Breeches) **le libera ese hueco**, le da Decrepitud determinista y le deja meter otra habilidad. El informe se lo presentó como un peaje. Y la frase "ninguna guía de esbirros lo recomienda" es la del error #1: tres lo recomiendan.

---

## 4. 🟠 La "cura" de Teb y el "Ejecutar" de Wat **sí están corroborados** — el informe los enterró en `No encontrado`

El informe marca con ⚠️ ambas coletillas de Icy Veins y las manda a `No encontrado #7` como posiblemente muertas, porque *"no aparece en Maxroll ni en el fichero de datos"*.

**Segunda fuente independiente, viva, abierta hoy:**
> **Teb** — *"Magic Rune of Invocation. Requires: 100 Offering. Cooldown: 1 Seconds. **Evoke the Necromancer's Abhorrent Iron Maiden, counterattacking damage from enemies and Healing you when they die.**"* — [d4planner.io/runes/Teb][d4pteb]

Y **la explicación estaba en el propio informe**, §2.4: la runa lanza *"the best possible version"* de tu propia clase. `Abhorrent Iron Maiden` (mejora del Nigromante) **es** la que cura al morir el enemigo; `Horrid Decrepify` **es** la que ejecuta. El texto corto de Maxroll describe el efecto base; el largo de Icy Veins describe la versión mejorada, que es la que recibe un Nigromante. **No son fuentes en conflicto: son dos niveles de detalle del mismo efecto**, y el informe tenía la clave escrita dos secciones más arriba.

**Consecuencia práctica:** el informe le vende `Wat` como *"Debilita y Ralentiza"* a secas. Le falta *"reduce su daño y te permite Ejecutarlos"*, que es la mitad del valor de la runa.

---

## 5. 🟡 Falso positivo en la lista de "fuentes muertas": la runa `Noc`

§12 acusa a Icy Veins de publicar *"Noc 10 (datos: 5)"* como prueba de que su tabla está caducada. **Los dos textos son matemáticamente idénticos**, solo cambian la línea base:

- Maxroll: *"Noc **5** — Inflict a Crowd Control, **gain double offering** if it isn't a Slow or Chill."* → 5 con Ralentizar/Escalofrío, **10** con cualquier otro control.
- Icy Veins: *"Noc Rare **10** Offering — Inflict a Crowd Control. **Gains half the offering** when inflicting a Slow or Chill."* → 10 normal, **5** con Ralentizar/Escalofrío.

Mismo resultado en los dos casos. No es un error de Icy Veins y no debe contar como prueba de caducidad. (El resto de la acusación de §12 **sí se sostiene**: ver punto 10.)

---

## 6. 🟡 Conflicto de rareza de `Nagu` **no declarado** — y la prueba cruzada que el informe tenía delante

§5.2 da **`Nagu` = Rara** (fichero de datos) y §14 le dice al jugador *"busca `Nagu` (Rara) + `Ceh` (Mágica)"*. Icy Veins publica lo contrario, y el informe no lo menciona en ninguna parte:

> *"**Nagu Legendary** 100 Offering — Maintain at least 1 Summon for 5 seconds, up to 6 Summons for maximum benefit."* — [icy-veins runewords][ivrw]

No es cosmético: Rara se amalgama con 5 mágicas cualesquiera, Legendaria cuesta 25. El informe sí flageó el "hasta 6 invocaciones" de esa misma línea y **se saltó la palabra `Legendary` de la línea de al lado**.

**La buena noticia: el informe acierta, y hay una prueba que no usó.** La propia hoja de Maxroll dice cómo se compone cada receta de Mítico:

> *"Each Mythic Unique requires 3x Resplendent Spark, **3x Legendary Runes** of a specific name, **3x Rare Runes** of a specific name, and **3x Magic Runes** of a specific name."* — [maxroll runewords overview][rwo]

Aplicado a las 9 recetas de la hoja de crafteo, la posición de cada runa **fija su rareza sin datamining**, y sale exactamente la tabla del informe:

| Receta | Legendaria | Rara | Mágica |
|---|---|---|---|
| Arma 2H | Igni | **Zan** | **Teb** |
| Pecho | Yom | **Nagu** | Tzic |
| Piernas | Ohm | **Wat** | Cem |
| Casco | Jah | Que | Gar |
| Botas | Vex | Thul | Kry |
| Anillo | Tam | Mot | Yax |
| Amuleto | Yul | Noc | Qua |
| Guantes | Bac | Noc | Moni |
| Arma 1H | Eom | Lac | Ceh |

→ **`Nagu` Rara, `Zan` Rara, `Teb` Mágica, `Wat` Rara**: confirmado por una fuente editorial, sin tocar el fichero de datos. El informe pudo cerrar esa columna sin declarar datamining y no lo vio. (Y de paso: `Tzic` Mágica y `Kry` Mágica, donde Icy Veins dice "Rare" en ambas. La tabla de rarezas de Icy Veins es la de **antes** de *Lord of Hatred*.)

---

## 7. 🟡 Una cita de §6.3 **no es literal** aunque va entre comillas

El informe presenta como cita textual:
> *"Igni + Wat — Applies Decrepify automatically along skills once every 1.2 seconds, allowing you to invest in Decrepify upgrades without requiring the skill on your action bar."*

El texto real de la página es:
> *"**Igni + Wat** – Applies Decrepify automatically along **your** skills once every 1.2 seconds. **It allows you to invest into** Decrepify upgrades **and use them without having the skill on your Skill Bar**."* — [ivsum]

El contenido no cambia, pero la regla del encargo era cita literal. Es una paráfrasis vestida de comillas.

---

## 8. 🟡 La aritmética del "1,2 s" **no se valida sola**

§6.3 dice: *"Este es el número más verificable de todo el informe, y cuadra solo… La cifra publicada por Icy Veins y el modelo del fichero de datos se validan mutuamente."*

No del todo. El texto de `Igni` en Maxroll es:
> *"Igni 25 — **Stores** offering every 0.3 second. **Cast a non-Basic Skill** to gain the stored offering."*

La Ofrenda **se almacena y solo se cobra al lanzar una habilidad No Básica**. Los 1,2 s son un **suelo teórico condicionado a que estés lanzando**, no un tictac automático. Para una build de esbirros, donde los esbirros pegan solos y tú lanzas menos, la distinción no es académica. La cifra de Icy Veins sigue siendo válida como cifra publicada; lo que no se sostiene es la etiqueta de "se valida sola".

---

## 9. 🟡 Al transcribir `Ceh`, el informe se dejó fuera **lo más relevante para su propio jugador**

§5.3 da `Ceh` como *"Invoca un Lobo Espiritual que ataca 8 s"*. El texto de Maxroll es:
> *"Ceh 100 — Summon a Spirit Wolf to attack enemies for 8 seconds **(now benefits from Summon and Companion bonuses)**."* — [rwo]

Ese paréntesis es la razón por la que `Ceh` es la runa de esbirros. El informe lo afirma en §7.3 (*"`Ceh` invoca lobos que además cuentan como invocaciones"*) presentándolo como **razonamiento propio**, cuando estaba escrito literalmente en la fuente que citaba. Recorte a la baja, no invención — pero deja el consejo peor sostenido de lo que estaba.

---

## 10. 🟢 Lo que ataqué y **no cayó** (confirmado contra HTML crudo, cita a cita)

| Afirmación del informe | Estado | Prueba |
|---|---|---|
| Huecos: Casco 2, Pecho 2, Piernas 2, Arma 2H 2 | ✅ **Confirmado, y con fuente mejor que la suya** | Blizzard: *"you must socket a Rune of Ritual and a Rune of Invocation into an item containing two Sockets, such as Chest, Leg, and Two-Handed weapon slots… **The Helm slot has also received an additional Socket and can now house a Runeword**"* [bliz20]; Maxroll: *"Runewords can only be created in items with two sockets, this includes **Helm, Chest, Legs, and 2H Weapon**"* [rwo] |
| Anillo 1 / Amuleto 1, solo gemas | ✅ Confirmado — pero el informe lo sacó **solo del planificador**, habiendo fuente editorial viva | Maxroll *Jeweler, Gems & Socketing* e Icy Veins *Gear Systems (S14)*: casco/pecho/pantalón/2H llevan 2 huecos, el resto 1 |
| Máximo **2** palabras rúnicas = 4 runas | ✅ Confirmado por **tres** fuentes | *"A maximum of 2 Runewords can be equipped (4 Runes total)."* [bliz20] · *"you can only have two Runewords on a character"* [rwo] · *"Only two Runewords may be active at a time"* [d4pteb] |
| Gemas y runas incompatibles · no repetir runa · las dos en la MISMA pieza | ✅ Literal | *"The Runes have to be socketed into the same item… You also cannot equip both Gems and Runes in the same item… You cannot use two of the same Runes, nor can you use two Runes of Ritual or two Runes of Invocation in the same item"* [rwo] |
| Runas = exclusivas de *Vessel of Hatred* | ✅ Literal | *"Runes can drop from various activities within Diablo 4, and **can only drop if the player has the Vessel of Hatred expansion**"* [rwo] |
| **Teb**: Invocación, Mágica, 100 Ofrenda, 1 s, Doncella de Hierro, desbordamiento +1%/Ofrenda | ✅ Confirmado en 3 fuentes | [rwo] (100 / 1 Second / *"Increase damage by 1% per offering"*), [ivrw] (*"Teb Magic 100 Offering 1 Second"*), [d4pteb] (*"Magic Rune of Invocation"*) |
| **Wat**: Invocación, Rara, 100 Ofrenda, 1 s, Decrepitud, desbordamiento más duración | ✅ Confirmado | *"Wat 100 Increased Duration — Invoke the Necromancer's Horrid Decrepify, Weakening and Slowing enemies. Cooldown: 1 Second."* [rwo]; *"Wat Rare 100 Offering 1 Second"* [ivrw]; rareza Rara confirmada además por la receta de Mítico de Piernas (punto 6) |
| `Ur` **eliminada** del juego | ✅ Confirmado **en fuente OFICIAL**, no solo Maxroll | news.blizzard.com: *"Fixed an issue where **the removed Ur rune** was still required to craft Yul runes. **Developer's Note: Crafting a Yul Rune now requires Moni instead of Ur.**"* y *"Fixed an issue where Ur runes could still drop from Duriel's Cache."* [bliznotes] |
| Cambios del 3.1.0: Ceh sin Vulnerable / Escalofrío 50→10% / lobos 10→6 · Vex 100→300 · Prid 250→500 · Yom pasa a Daño Crítico | ✅ **Literal, palabra por palabra**, en Blizzard y en Maxroll | [bliznotes] y [n310] (*"Last Updated: June 24, 2026"*, la fecha que da el informe) |
| Maxroll publica valores muertos (Vex 100, Prid 250, Yom "restoring 100 Resource") | ✅ **Confirmado en el HTML de hoy** | [rwo], *Last Updated: July 16, 2026*: *"Vex **100** … Gain +1 to all Skills"* y *"Yom **500** … Stunning enemies and **restoring 100 Resource**"* y *"Prid **250**"* |
| La hoja de crafteo sigue pidiendo `Ur` para `Yul` | ✅ Confirmado | [cheat]: *"Yul — **1x Ur** — 5x Any Rare Runes — 5x Any Legendary Runes"* |
| Míticos: 3× Chispa + 3+3+3 runas + 5.000.000 de oro, con **3× Teb** (2H) y **3× Wat** (Piernas) | ✅ Confirmado literal | [cheat]: *"2-Handed Weapon — 3x Resplendent Spark 3x Igni 3x Zan **3x Teb** 5,000,000x Gold"*, *"Pants — 3x Resplendent Spark 3x Ohm **3x Wat** 3x Cem 5,000,000x Gold"* |
| Amalgamación 5 Mágicas→1 Rara, 5 Raras→1 Legendaria; Joyero 3 iguales 85/15 | ✅ Confirmado | [cheat] |
| `Igni` se craftea **con `Teb` de semilla** (§9.3, base del consejo "no tires ningún Teb") | ✅ Confirmado literal | [cheat]: *"Igni — **1x Teb** — 5x Any Rare Runes — 5x Any Legendary Runes"* |
| **Planificador de esbirros de Maxroll: cero Teb, cero Wat, cero Ur en las 6 variantes** | ✅ **Verificado a mano sobre el JSON** | Descargado y parseado: 214 ítems, 6 perfiles, fecha `2026-07-22 14:38:51`. Runas equipadas: Leveling `Cir+Ceh` (casco) + `Cem+Gar` (pecho) · Starter `Nagu+Ceh` (casco) + `Cir+Que` (piernas) · Mid Game `Nagu+Ceh` (casco) + `Igni+Gar` (piernas) · Warrior y Mages `Nagu+Que` (casco) + `Igni+Ceh` (pecho) · Zookeeper `Igni+Gar` (pecho) + `Nagu+Ceh` (piernas). **La tabla §7.1 del informe es exacta.** No existe `Rune_Effect_Necromancer_IronMaiden` en ningún ítem del fichero; `Rune_Effect_Necromancer_Decrepify` (=Wat) aparece **una vez, en un ítem no equipado** (id 66, casco "Loath Sanctum", `Igni+Wat`) |
| Cita de Maxroll leveling (*"Best in Slot Cir + Ceh"*, *"Cem + Gar"*, alternativas Que/Igni/Tam/Jah/Nagu, *"socket them into your Armor pieces as Weapon Gems offer powerful multiplicative damage bonuses"*) | ✅ Literal, y la fecha *Last Updated: June 30, 2026* también | [minlvl] |
| Cita de Sever (*"Cir and Teb… automate Curse application"*) | ✅ Literal | [sev]: *"**Cir + Teb** help to automate Curse application to save room on your Skillbar."* |
| Nota de *Radament's Desecration* del 3.1.0 | ✅ Literal, incluida la coletilla de Blood Moon Breeches | [n310] |
| *"Lair of Runes"* existe (nodo de Planes de Guerra) | ✅ Confirmado en notas del 3.0.2 | [n302]: *"Fixed an issue where **Belial's Lair of Runes rune pool** was reducing the drop chance of non-legendary runes below Torment 6."* |
| Icy Veins publica una tabla de Míticos incompatible y con runas muertas | ✅ Confirmado | [ivrw]: *"Each Mythic Unique requires **10 runes** of three different types, along with **a Resplendent Spark**"*, y en la tabla: *"Shroud of False Death — Resplendent Spark x1, Bac x10, Kry x10, **Ur x10**"*, *"Tyrael's Might — … **Lith** x10, , **Met** x10"*, *"The Grandfather — … **Xol** x10, **Kaa** x10, Yax x10"*. Runas eliminadas + fórmula distinta a la de Maxroll de julio 2026. **El veredicto "esa tabla está muerta" se sostiene** |
| Zan: Icy Veins dice **150 y Mágica** (informe §12) | ✅ Confirmado literal, contra mi propia sospecha inicial | [ivrw]: *"Zan **Magic 150 Offering** Cast an Ultimate Skill"* |
| Fichero de datos = `3.1.0.72698`, por detrás del parche vivo | ✅ Confirmado | `curl -r 0-3000 assets-ng.maxroll.gg/d4-tools/game/data.min.json` → `{"version":"3.1.0.72698"…}`. Y el 3.1.1 es build **#72836** [bliznotes], o sea posterior: la advertencia del informe es correcta |
| *"Ninguna fuente publica la lista de runas eliminadas"* (`No encontrado #1`) | ✅ **Se sostiene.** Abrí el artículo de Icy Veins sobre el rediseño: habla de *"Blizzard has removed underutilized runes entirely"* y **no nombra ni una sola runa**. Lo único que hay son reconstrucciones de foro previas al lanzamiento, con el propio autor advirtiendo *"Don't trust any of this until you verify in game yourself"* | [ivrew], foros de Blizzard |
| Talismán *"double Offering from Helm runes"* → sin confirmación editorial | ✅ Se sostiene. Busqué específicamente y **ninguna guía de Talismán de la S14 lo menciona**. Bien declarado como datamining | — |
| Ciudadela Oscura no confirmada como fuente de runas | ✅ Se sostiene | Ninguna guía viva la lista entre las recompensas |

---

## 11. 🟢 Dos cosas que el informe **acierta y podría haber cerrado mejor**, y una fecha que ahora está mejor

1. **3.1.1 y 3.1.2 tampoco tocan runas.** El informe solo verificó que el 3.1.3 no las toca. La página oficial acumulada de Blizzard permite cerrarlo del todo: **3.1.1 (#72836, 14 jul 2026)** y **3.1.2 (#73020, 28 jul 2026)** no contienen ni una línea de runas. La conclusión *"el parche que importa es el 3.1.0"* queda **reforzada**, no debilitada.
2. **El arreglo de `Tzic` del 3.1.3 está en fuente oficial**, no solo en Icy Veins: *"Fixed an issue where Concussive Stomp would not grant Resolve when taking the appropriate upgrade while triggered by the **Tzic Rune**."* [bliznotes]. El informe citó la fuente secundaria teniendo la primaria disponible.
3. **Matiz menor:** §8.1 dice que El Foso *"NO confirmado por ninguna fuente viva"*. Sí existe alguna página que lo lista entre zonas de farmeo de runas (de baja calidad y sin fecha), así que lo correcto es *"ninguna fuente fiable lo confirma"*, no *"ninguna"*. La cautela del informe es acertada; el absoluto no.
4. **Matiz menor:** §8.2 dice que *"Lair of Runes"* está *"mencionada en unas notas oficiales de parche"* citando a Maxroll. Maxroll **reproduce** las notas de Blizzard, así que el contenido vale, pero la etiqueta "oficial" va a una fuente de segunda mano. En la página oficial viva de Blizzard (que solo cubre 3.1.x) esa frase no aparece.

---

## Veredicto por afirmación auditada

| # | Afirmación auditada | Veredicto |
|---|---|---|
| 1 | Huecos 2/2/2/2, anillo y amuleto 1 | **Confirmada** |
| 2 | Máximo 2 palabras rúnicas = 4 runas | **Confirmada** |
| 3 | Gemas/runas incompatibles, no repetir, misma pieza | **Confirmada** |
| 4 | Runas exclusivas de Vessel of Hatred | **Confirmada** |
| 5 | Teb: Invocación / Mágica / 100 / 1 s / Doncella de Hierro / +1% por Ofrenda | **Confirmada**, con el efecto **incompleto** (falta la curación) |
| 6 | Wat: Invocación / Rara / 100 / 1 s / Decrepitud / más duración | **Confirmada**, con el efecto **incompleto** (falta el Ejecutar) |
| 7 | Igni+Wat cada 1,2 s sin ocupar barra | **Confirmada** como cifra publicada; **la validación "cuadra sola" no se sostiene** |
| 8 | `Ur` eliminada | **Confirmada, y elevada a fuente oficial** |
| 9 | Cambios de runas del 3.1.0 (Ceh, Vex, Prid, Yom) | **Confirmada, literal, en Blizzard** |
| 10 | Planificador de esbirros: pares de runas, cero Teb/Wat/Ur | **Confirmada, verificada sobre el JSON** |
| 11 | Maxroll esbirros: "Best in Slot Cir+Ceh", "Cem+Gar", armadura y no arma | **Confirmada, literal** |
| 12 | *"Ninguna guía viva de esbirros usa Teb/Wat"* (resumen ejecutivo #2) | **REFUTADA** |
| 13 | *"Blood Moon Breeches ya reparte las maldiciones → Teb/Wat es pagar dos veces"* (§7.2) | **REFUTADA** |
| 14 | *"Igni+Wat solo si abandona la Doncella de Hierro"* (§7.3) | **REFUTADA — está invertida** |
| 15 | Icy Veins publica `Noc 10` = error (§12) | **REFUTADA — es la misma mecánica con otra base** |

---

## Fuentes abiertas para esta refutación

Todas descargadas en crudo con `curl` y leídas sobre el HTML, no sobre resumen.

- [bliznotes] `https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes` — **oficial**, notas acumuladas: 3.1.3 build #73224 (12 ago 2026), 3.1.2 #73020 (28 jul), 3.1.1 #72836 (14 jul), bloque de Runas del 3.1.0
- [bliz20] `https://news.blizzard.com/en-us/diablo4/24130178/the-2-0-ptr-what-you-need-to-know` — **oficial**, definición del sistema y límite de 2 palabras rúnicas
- [rwo] `https://maxroll.gg/d4/resources/runewords-overview` — *Last Updated: July 16, 2026*
- [cheat] `https://maxroll.gg/d4/resources/crafting-cheat-sheet` — *Last Updated: July 14, 2026*
- [n310] `https://maxroll.gg/d4/news/diablo-4-3-1-0-patch-notes` — *Last Updated: June 24, 2026*
- [n302] `https://maxroll.gg/d4/news/lord-of-hatred-3-0-2-patch-notes`
- [minlvl] `https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide` — *Last Updated: June 30, 2026*
- [minend] `https://maxroll.gg/d4/build-guides/minion-necromancer-guide` — *Last Updated: July 22, 2026*
- [sev] `https://maxroll.gg/d4/build-guides/sever-necromancer-endgame-guide` — *Last Updated: July 28, 2026*
- [plan] `https://planners.maxroll.gg/profiles/d4/7xf3kf0h` — JSON, `date` = `2026-07-22 14:38:51`, 6 perfiles, 214 ítems (parseado a mano)
- [data] `https://assets-ng.maxroll.gg/d4-tools/game/data.min.json` — **datamining**, `version` = `3.1.0.72698`
- [ivrw] `https://www.icy-veins.com/d4/guides/runewords-guide/` — Season 14, sin fecha visible
- [ivsum] `https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/` — Summoner (esbirros) Leveling, S14
- [naz] / [naj] `https://www.icy-veins.com/d4/guides/mendeln-summoner-necromancer-build/` — Naz Mages, S-Tier, S14
- [reap] `https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/` — Reaper Summoner, A-Tier, S14
- [ivrew] `https://www.icy-veins.com/d4/news/diablo-4-lord-of-hatred-rune-changes/` — rediseño de runas; **no nombra ninguna runa eliminada**
- [iv313] `https://www.icy-veins.com/d4/news/diablo-4-3-1-3-patch-notes-easier-season-objectives-and-echo-of-mephisto-portal-fix/`
- [d4pteb] `https://d4planner.io/runes/Teb` — base de datos; corrobora rareza, coste, CD y el texto completo de Teb
- `https://www.wowhead.com/diablo-4/blue-tracker/news/us/diablo-iv-patch-notes-diablo-iv-blizzard-news-24287406` — espejo Blue Tracker de las notas oficiales
- `https://nexttier.pro/guide/diablo-4-season-14-runewords-tier-list` — *Updated Jul 20, 2026*; **descartada para números**: sigue diciendo que `Ceh` *"can Freeze and apply Vulnerable"*, eliminado en el 3.1.0
- `https://us.forums.blizzard.com/en/d4/t/runes-removed-in-loh/245508` y `.../runes-in-loh-which-ones-are-going-away/245681` — foros oficiales; **solo reconstrucciones de jugadores anteriores al lanzamiento de LoH**, el propio autor advierte que no son fiables
- `https://mobalytics.gg/diablo-4/guides/rune-guide` — **HTTP 403**, sigue sin poder abrirse (igual que en el informe original)

**Fuentes vetadas:** no se ha usado fextralife, primagames, beebom, gamespot, segmentnext, studioloot, gamerguides, pcgamesn ni mythicdrop para ningún dato de esta refutación.
