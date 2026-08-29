# Refutación adversarial — `crudo/pal-miticos.md`

**Objeto:** informe "Míticos (Mythic Uniques) para Paladín — Season 14".
**Fecha de la refutación:** 19/08/2026. **Parche vivo:** 3.1.3 / build 73224 (12/08/2026).
**Método:** contraste con notas oficiales de Blizzard, foro oficial, Maxroll e Icy Veins fechados dentro
de 3.1.x, **y redescarga independiente del fichero de datos** para recomputar las cifras de datamining.

## VEREDICTO: PARCIAL

Las cinco afirmaciones de cabecera —las que mueven dinero del jugador— **resisten el ataque**, y varias
las he podido reproducir yo mismo desde la fuente primaria. Pero el informe contiene **seis errores
factuales**, dos de ellos capaces de mandar al jugador a farmear el objeto equivocado, y **uno de ellos
está dentro del argumento estrella del informe**.

---

## 1. Lo que NO he conseguido refutar (confirmado, a veces reforzado)

Verificado contra fuente primaria. Cuando pone "reproducido", significa que lo he recalculado yo desde
el fichero de datos, no que me haya fiado del informe.

| Afirmación | Estado | Prueba |
|---|---|---|
| Receta del Cubo = **4** Fragmentos, bajó de 5 en 3.1.1 (14/07) | **CONFIRMADO** | Cita literal oficial: *"Reduced the cost of the Upgrade to Mythic recipe on the Horadric Cube from 5 to 4 Pandemonium Fragments."* |
| Límite de 1 Mítico crafteado **ELIMINADO** en 3.1.1a (16/07) | **CONFIRMADO** | Foro oficial, literal: *"Removed the 'one-crafted Mythic' equipment restriction on Mythic items."* |
| Ingrediente: 1 Único de la ranura, **850+** de Poder de Objeto | **CONFIRMADO** | Maxroll 24/06/2026 |
| El Cubo devuelve un Mítico **aleatorio de la misma ranura** | **CONFIRMADO** | *"Putting in a pair of Unique Boots will return a random pair of Mythic Unique Boots"* (Maxroll 24/06) |
| Nivel **70** | **CONFIRMADO — reproducido** | Cadena literal en el fichero: *"Each Level grants a Skill Point until Level 70."* Aparece 1 vez. |
| Mítico = siempre Ancestral, **+30%** de Poder Único, resto de afijos al máximo | **CONFIRMADO** | Maxroll guía de temporada 13/07/2026 (fuente **viva**, no PTR): *"Mythic Uniques are always Ancestral and have their Unique Powers increased by 30%. All other affixes roll at maximum values."* |
| **13** Míticos Icónicos, **10** usables por Paladín | **CONFIRMADO — reproducido exactamente** | Ver §3. Corroborado además por fuente externa: el pool de la caché del Herrero son 13 y 3.1.1 añadió El'Druin. |
| Los 3 no usables: Ahavarion / Nesekem / Shattered Vow | **CONFIRMADO — reproducido** | `classFilter[6] == False` en los tres. Ver §3. |
| Corrupted Reaper: hasta 2 Fragmentos escalando con Tormento (3.1.1) | **CONFIRMADO** | *"Corrupted Reaper now drops up to two Pandemonium Fragments, scaling with Torment level"* |
| Corrupted Reaper en **Zarbinzet** | **CONFIRMADO** | *"the Pandemonium Threshold, the Corrupted Reaper's lair, can be found in Zarbinzet"* |
| "Glints of Hope" garantiza 1 Fragmento (3.1.1) | **CONFIRMADO** | Literal oficial, idéntico |
| Rango de Temporada: **5 Cachés** (3, 7, 8, 9×2); Chispas en 6, 8, 9 | **CONFIRMADO** | Maxroll season-journey 13/07/2026 |
| Bug de jefes de guarida sin Míticos, corregido en 3.1.1 | **CONFIRMADO** | Literal oficial, idéntico |
| 3.1.1a quitó la calidad Mítica a Charms y Sellos | **CONFIRMADO** | Foro oficial: *"Removed the ability to add the Mythic modifier to Unique Charms & Seals **in the Cube**."* (el matiz "in the Cube" el informe lo omite) |
| Fórmula de *Mantle of the Grey* | **CONFIRMADO — reproducido carácter a carácter** | Ver §2 |
| Orden de crafteo de la guía + línea caducada del límite | **CONFIRMADO — literal exacto** | Maxroll build guide, act. 25/07/2026 |
| Fichero de datos: `3.1.0.72698`, 11.606.292 bytes | **CONFIRMADO — redescargado** | HTTP 200, `wc -c` = 11606292, `version` = `3.1.0.72698` |
| 1.075 entradas de calidad Única | **CONFIRMADO — reproducido** | `Counter(magicType)` → `{0: 9676, 2: 1075, 1: 766, 3: 243, 4: 35}` |
| Reddit inaccesible | **CONFIRMADO** | Reintentado: *"Claude Code is unable to fetch from www.reddit.com"* |
| El artículo de S15 de Icy Veins es PTR | **CONFIRMADO** | Referencia explícita al "3.2.0 PTR" |

**Ninguna fuente vetada sustenta ningún número del informe.** Fextralife y pcgamesn aparecieron en mis
resultados de búsqueda; el informe no los cita. Disciplina PTR/vivo: correcta en general (§2 y §5 marcan
el PTR como tal).

**Un punto donde el informe se infravalora:** su "No encontrado #9" dice que el +30% solo consta en el
artículo del PTR. Falso a su favor — la guía de temporada de Maxroll del **13/07/2026**, ya en temporada
viva, lo afirma con esas palabras. El dato es más firme de lo que el propio informe admite.

---

## 2. ERROR EN EL ARGUMENTO ESTRELLA: `{if:IsMythic}` no está en dos objetos, está en 279

El informe (§6, "argumento de datos, no de opinión") afirma:

> "De **todos los Únicos del juego (1.075 entradas de calidad Única en el fichero), solo DOS** tienen en
> el fichero de datos la fórmula condicional explícita `{if:IsMythic}`"

**Es falso.** Recuento sobre el mismo fichero:

```
occurrences of "IsMythic" in raw file: 860
affix entries containing IsMythic:     279     <- no 2
affix entries containing S14_Mythic_UniquePotency: 2
```

`{if:IsMythic}` es un **condicional de presentación** (colorea el texto en dorado y cambia `{c_random}`
por `{c_number}`) y lo lleva prácticamente cualquier Único —*Tibault's Will*, *Blood-Mad Idol* y
*Herald of Zakarum* lo llevan también, y el informe no los cuenta.

Lo que **sí** es exclusivo de dos objetos es otra cosa: la **fórmula de valor** `S14_Mythic_UniquePotency`.
El informe confundió las dos etiquetas y colgó la afirmación "solo DOS" de la equivocada.

**La conclusión sobrevive; la prueba citada, no.** Los dos objetos son exactamente los que dice:

| Clave del afijo | Objeto | Fórmula |
|---|---|---|
| `Chest_Unique_Paladin_001` | **Mantle of the Grey** | `S14_Mythic_UniquePotency>0?0.06*(1+S14_Mythic_UniquePotency):FloatRandomRangeWithInterval(10,0.04,0.06)` |
| `Amulet_Unique_Spiritborn_102` | **Protean Heart** | `S14_Mythic_UniquePotency>0?20*(1+S14_Mythic_UniquePotency):FloatRandomRangeWithInterval(5,16.667,20)` |

Redacción correcta: *"de las 6.196 entradas de afijos, solo DOS usan la fórmula `S14_Mythic_UniquePotency`,
que sustituye la tirada aleatoria por el tope multiplicado por la potencia Mítica."*

**Además, el informe se queda corto en un punto donde tenía razón.** Hedgea el 7,8% diciendo que el 30%
"lo pongo por la fuente de Blizzard, no por el fichero", porque teme no saber si la potencia entra como
`0,30` o como `30`. El fichero lo resuelve:

```
attributeDescriptions["S14_Mythic_UniquePotency"] = "{c_mythic}{i}Mythic:{/i}{/c} [{value1}*100|1%|] Unique Potency"
```

El `*100` con formato `%` implica que el atributo se almacena como **fracción**. Luego `0,06 × 1,30 =
0,078 = 7,8%` es correcto y el fichero **corrobora las unidades**. La aritmética de la tabla (64% / 96% /
124,8% sobre 16 puntos) también es correcta.

Texto del objeto, verificado literal: *"makes your Juggernaut Skills 25% larger but Consumes up to 16
Resolve"*. ✔

---

## 3. Verificación independiente del recuento 13/10 (reproducido, sale bordado)

Recomputado desde cero con `magicType == 4`, deduplicando Crucible y Charm, y excluyendo lo que no es
equipo de combate. `classes[6] = Paladin` — **confirmado en el fichero**.

| # | Mítico Icónico | `classFilter` | Paladín (`[6]`) |
|--:|---|---|:--:|
| 1 | Doombringer | `[T,T,T,T,T,F,T,T]` | **Sí** |
| 2 | The Grandfather | `[F,F,T,F,T,F,T,T]` | **Sí** |
| 3 | Andariel's Visage | todo `T` | **Sí** |
| 4 | Harlequin Crest | todo `T` | **Sí** |
| 5 | Melted Heart of Selig | todo `T` | **Sí** |
| 6 | Ring of Starless Skies | todo `T` | **Sí** |
| 7 | Tyrael's Might | todo `T` | **Sí** |
| 8 | Heir of Perdition | todo `T` | **Sí** |
| 9 | Shroud of False Death | todo `T` | **Sí** |
| 10 | El'Druin, Sword of Justice | `[T,T,T,T,T,F,T,T]` | **Sí** |
| 11 | Ahavarion, Spear of Lycander | `[T,T,F,F,F,F,F,F]` | No |
| 12 | Nesekem, the Herald | `[F,F,F,F,F,T,F,F]` | No |
| 13 | Shattered Vow | `[F,T,T,F,F,T,F,F]` | No |

**13 y 10. Exacto.** No-equipo con `magicType 4`: *Resplendent Spark*, *The Empyrean Eye* y **cuatro**
sellos — exactamente los que lista el informe. *The Cow King's Crown* existe y su tratamiento es correcto.

Valores de §6, todos verificados literales: Tibault's Will `FloatRandomRangeWithInterval(5,15,20)` +
50 de regeneración mientras Imparable y 5 s después ✔ · Herald of Zakarum `(10,0.4,0.5)` → 40-50% de
Fuerza, **Resistance**, Armadura y prob. de Retribution, +50% de tamaño ✔ (la traducción "Resistencia"
es fiel: el texto dice *Resistance*) · Blood-Mad Idol 200%x como Quemadura **en 8 segundos** y 80-100%x ✔
(el informe omite "en 8 segundos").

Existencia de claves internas: `S14_Seasonal_Currency`, `BlackSmith_MythicCrafting`, `Mythic_Cache`,
`BossSummoning_Superior_LairKey` — **todas confirmadas**.

---

## 4. ERRORES DE ATRIBUCIÓN DE PARCHE (dos)

El informe presenta ambos en tabla, con aire de dato duro.

| Línea oficial | El informe dice | Realidad |
|---|---|---|
| *"The Upgrade to Mythic recipe in the Horadric Cube now always creates an item for the same gear slot."* | **3.1.1** | **3.1.0** (30/06/2026) |
| *"Mythic Unique Items cannot be used in the Upgrade to Mythic Unique recipe."* | **3.1.3** | **3.1.0** (30/06/2026) |

Verificado dos veces contra las notas oficiales y una tercera contra las notas 3.1.0 de Maxroll.

**Impacto práctico: ninguno** — las dos reglas están vivas hoy, que es lo que le importa al jugador.
**Impacto metodológico: sí** — el informe usa la primera como "corroboración independiente" del resultado
aleatorio, y una corroboración fechada mal es una corroboración que no se ha comprobado.

---

## 5. ERROR CARO: el material de invocación de Belial está muerto

§4.3 del informe:

> | Exaltado | Belial | **2× Betrayer's Husk** | Emboscada de Belial tras matar un jefe de guarida |

**Refutado por las notas oficiales del parche**, literal:

> *"Betrayer's Husks, the item for Tier 3 boss ladder keys, are now known as **Superior Lair Keys** now
> that Belial is not the only boss in that tier."*

**Betrayer's Husk ya no existe con ese nombre.** Es la Superior Lair Key. Confirmado por tres vías:

1. Notas oficiales de Blizzard (arriba).
2. Maxroll, chuleta de botín de jefes, **act. 16/08/2026** — la página más reciente que el propio informe
   declara haber leído: **Belial requiere "1x Superior Lair Key"**, no dos Husks.
3. El fichero de datos: `BossSummoning_Superior_LairKey` → *"Acquired from **Belial, Lord of Lies**, who
   sometimes ambushes after…"*.

El informe sacó ese renglón de la guía de jefes de guarida de Icy Veins, que **no menciona la Superior
Lair Key en absoluto** — es decir, es anterior al renombrado. Es exactamente el fallo contra el que el
propio informe advierte en su §1: dar por buena una página sin comprobar que su vocabulario siga vivo.

**Y esto además disuelve el "No encontrado #3" del informe.** El informe declaró irresoluble la
discrepancia "2 llaves vs 1 llave" del Corrupted Reaper. No era irresoluble: el "two" que leyó venía del
mundo viejo de los *dos* Betrayer's Husks de Belial. Hoy la moneda es la Superior Lair Key.

### 5b. Conflación de nombres de llave (tres llaves, dos nombres)

El fichero tiene **tres** llaves distintas:

| Clave interna | Nombre | Abre |
|---|---|---|
| `BossSummoning_Initiate_LairKey` | Lair Key | Lair Boss Hoard |
| `BossSummoning_Greater_LairKey` | Greater Lair Key | **Greater** Lair Boss Hoard |
| `BossSummoning_Superior_LairKey` | Superior Lair Key | **Superior** Lair Boss Hoard |

El informe traduce **"Greater Lair Key" como "Llave de Guarida Superior"** en la fila de Duriel/Andariel,
y luego usa **"Superior Lair Key"** para el Corrupted Reaper. Un lector español ve el mismo nombre para
**dos objetos distintos** y se va a farmear Duriel para invocar al Reaper.

Traducción correcta: Lair Key = *Llave de Guarida*; Greater = ***Mayor***; Superior = *Superior*.

### 5c. Falta un jefe y sobra un matiz

- **Astaroth** (material: *Escalation Sigil*) figura en la chuleta de Maxroll del 16/08 y en las notas
  oficiales (*"Escalation Sigils can be Salvaged"*). La tabla del informe se presenta como el censo de
  jefes y lo omite.
- Notas oficiales: *"Deathtoll Chambers will always reward at least one Superior Lair Key **in high
  Torment levels**."* El informe se queda con "salen de Deathtoll Chambers" y tira el condicional, que es
  justo la parte que determina si el jugador las verá o no.

---

## 6. ERROR: la "contradicción" de las Chispas es en buena parte autoinfligida

§4.2 monta una tabla de fuentes que "se contradicen entre sí e incluso Maxroll consigo mismo", y manda el
dato a "No encontrado". Al abrir la chuleta de crafteo citada (act. **14/07/2026**), las dos recetas que
el informe enfrenta **son las dos del Herrero**, y no se contradicen:

| Receta (Maxroll, chuleta de crafteo) | Vendedor real | Coste | Resultado |
|---|---|---|---|
| Random Mythic **Item** (por tipo, nueve tipos) | **Herrero** | **3** Chispas + 3 runas + **5.000.000** oro | Mítico aleatorio de ese tipo |
| Random Mythic **Unique** | **Herrero** | **2** Chispas + **50.000.000** oro | Mítico Único aleatorio |

El informe atribuye la segunda al **Joyero**. **No lo es**: la chuleta la lista bajo el Herrero. Son dos
recetas distintas del mismo vendedor —una por ranura y cara en Chispas, otra totalmente aleatoria y cara
en oro—, no una fuente contradiciéndose.

Lo llamativo es que **el informe tenía la prueba para resolverlo y no la usó**: él mismo señala que el
fichero llama a la caché `BlackSmith_MythicCrafting`. Eso apuntaba al Herrero.

Dato adicional que el informe no recoge: la caché del Herrero da un Icónico del pool de **13**, no un
Mítico cualquiera — lo que hace esa receta bastante mejor de lo que el informe sugiere.

*(La recomendación operativa del informe —"lee la receta en pantalla antes de gastar"— sigue siendo buena.
Lo que sobra es haber declarado irresoluble algo que se resolvía abriendo bien la página citada.)*

---

## 7. Citación floja: "Tormento I" para cualquier Mítico

El informe afirma como confirmado: *"Requisito mínimo de dificultad para cualquier Mítico: Tormento I —
Icy Veins y Maxroll (chuleta de botín, act. 16/08/2026)"*.

- La **chuleta de botín de Maxroll no enuncia ningún mínimo de Tormento** para que caiga un Mítico. Sí dice
  *"Any Unique drop has a chance to be Mythic quality"*, que es otra cosa.
- La **guía de jefes de Icy Veins tampoco** lo enuncia.
- Lo que **sí** está sostenido: **craftear** exige *"level 70 in Torment+ (the recipe does not show up if
  you don't meet those criteria)"* (Maxroll 24/06), y el Hoard estacional exige *"Torment I+"* (Maxroll
  guía de temporada).

El consejo práctico ("sube a Tormento") es correcto. La atribución concreta, no: **está citado a dos
páginas que no lo dicen**. Debería figurar como "Tormento+ para craftear y para el Hoard estacional".

---

## 8. Menor: el tope de 30 de Resolve no sale solo del temple

§6 cierra diciendo que la guía llega al tope de 30 de Resolve "templando +4 Máximo de acumulaciones en
casco, pecho y pantalones". Fuente independiente sobre la misma build añade que hacen falta además
**Glynn's Anvil y el conjunto Phoba**. No invalida el argumento de *Mantle of the Grey*; sí hace la
receta más cara de lo que el informe da a entender.

---

## Errores, en orden de gravedad

1. **Belial: "2× Betrayer's Husk"** — material renombrado a *Superior Lair Key* en 3.1.0 por nota oficial.
   Procede de una guía de Icy Veins anterior al cambio. (§5)
2. **Tres llaves bajo dos nombres en español**: "Greater Lair Key" traducido como "Llave de Guarida
   Superior", colisionando con la Superior Lair Key real. (§5b)
3. **`{if:IsMythic}` "solo en DOS objetos"** — está en **279** entradas de afijo. La etiqueta exclusiva de
   dos es `S14_Mythic_UniquePotency`. La conclusión aguanta; la prueba citada no. (§2)
4. **Receta de 2 Chispas + 50M atribuida al Joyero** — es del **Herrero**; la "contradicción de Maxroll
   consigo mismo" en buena parte no existe. (§6)
5. **"same gear slot" fechado en 3.1.1** — es de **3.1.0**. (§4)
6. **"Mítico no usable como ingrediente" fechado en 3.1.3** — es de **3.1.0**. (§4)
7. **"Tormento I" citado a dos páginas que no lo dicen.** (§7)
8. Omisiones menores: Astaroth / Escalation Sigil; *"in high Torment levels"* en Deathtoll Chambers;
   *"in the Cube"* en el hotfix de Charms y Sellos; "en 8 segundos" en Blood-Mad Idol; Glynn's Anvil y
   Phoba en el tope de Resolve. (§5c, §8)

## Lo que NO hay que tocar

Los cuatro consejos que mueven recursos —**4 fragmentos**, **el límite eliminado el 16/07**, **el Cubo da
aleatorio dentro de la ranura**, **Mantle of the Grey primero**— están confirmados en fuente primaria y
resisten. El orden de §6 es el de la guía y está citado como tal, sin inventar un ranking de DPS. La
sección "No encontrado" es honesta: de sus nueve huecos, dos se cierran con esta refutación (**#3**, las
llaves del Reaper; y **#9**, el +30% sí consta en fuente viva) y el resto siguen abiertos legítimamente.
La advertencia de no abrir las cachés del Rango de Temporada con el nigromante sigue siendo prudente: el
"class-specific" de Maxroll está corroborado, y el mecanismo exacto sigue sin documentarse.
