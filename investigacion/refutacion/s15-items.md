# Refutación — s15-items

> **Veredicto: SÓLIDO CON DOS DEFECTOS REALES.** He intentado tumbar el informe por los cinco frentes
> encargados y he fallado en cuatro. El armazón aguanta: comprobé literalmente en fuente primaria el
> marco de resistencias, el texto del 7×, los nueve Legacy Uniques con sus clases, las dos recetas de
> la Cuba y las tres vías de Mítico — **todo cuadra palabra por palabra**.
> Lo que SÍ se rompe es la "prueba numérica" del 7:1 (B4/C4): está fuera del alcance de la regla que
> pretende demostrar, lleva etiquetas de rareza inventadas y la aritmética del propio informe es falsa.

---

## 1. Fuentes vetadas respaldando números — **PASA, limpio**

Repasadas las 10 URLs del informe: `news.blizzard.com` (×2), `maxroll.gg` (×3), `icy-veins.com` (×4),
`us.forums.blizzard.com` (×1). **Ninguna vetada. Ninguna cifra apoyada en una vetada.**

El informe además declara en la línea final las descartadas (fextralife, purediablo, mistermenplays,
d4guides.gg, sportskeeda) y no las usa para ningún valor — lo verifiqué buscando esos dominios en el
cuerpo: no aparecen fuera de C3 y de la nota de descarte, y en C3 se citan precisamente **para tacharlas**.
Eso es uso correcto.

**Nota para el expediente:** al buscar yo corroboración del marco de resistencias, los resultados
orgánicos fueron `sportskeeda`, `antberry.com` y de nuevo Maxroll. Confirma el diagnóstico del informe
en C3: este tema concreto está dominado por fuentes no citables.

## 2. Páginas anteriores al 3.2.1 sin declarar — **PASA**

Las cinco fuentes fuera del parche vivo están etiquetadas *en la propia fila*, no escondidas en una nota al pie:

| Fuente | Fecha | ¿Declarada? |
|---|---|---|
| Blizzard PTR 3.2.0 | 30 jul 2026 | Sí, "**PTR**" en cada celda que la usa |
| Maxroll *In-depth Defense Guide* | 16 ago 2026 (3.1.x) | Sí, y con hueco propio (H10) |
| Icy Veins *Players Found a Resistance Change* | 9 ago 2026 | Sí, "**PTR**" |
| Icy Veins *Legacy Uniques Returning* | 30 jul 2026 | Sí, "**PTR, desactualizada**" |
| Icy Veins *Mythic Charms Shadow Dropped* | 14 jul 2026 (3.1.1) | Sí |

**No he encontrado ni una sola página fuera de parche colada como si fuera del parche vivo.** Esto es
lo que más me costó tumbar y no cedió.

## 3. Cita literal vs paráfrasis — **FALLA EN UN PUNTO, GRAVE**

### Lo que verifiqué literalmente y ES literal (fetch directo a fuente primaria)

- **B1** — `"Significantly increased the value of Single Resistance affixes on equipment, Charms, and Tempering recipes. Single Resistance affixes are now 7 times the value of All Resistance affixes."` ✓ exacto en Blizzard y reproducido igual en Icy Veins.
- **B1 (3ª frase)** — `"Re-tuned All Resistance Tempering values to align with other All Resistance affixes."` ✓ exacto.
- **F1** — `"...while protecting desirable traits like Greater Affixes, any Enchanted affixes, Tempers, and Transfigurations (as long as that Transfigured item is not Unmodifiable)."` ✓ el paréntesis existe, palabra por palabra.
- **F2** — `"Available for Legendary+ Charms and Seals, Horadric Reroll fully randomizes all base Affixes..."` ✓ el "Legendario o superior" del informe está en la fuente; no era invención.
- **A2/A4** — `"DR% from Resistance = Resistance / (Resistance*10/9 + Constant)"`, constante **1136** a nivel 70, `"the 10/9 term means that DR from Resistances approach 90%"`, `"7,000 Fire Resistance -> 78.53% DR @ lvl 70"`, changelog `"Updated for Season 11 - Updated Armor and Resistances to follow a rating system, instead of having caps for different difficulties"`, `Last Updated: August 16, 2026`. ✓ **los cinco, exactos.**
- **C7 / clases de In-Geom** — Blizzard final: `"In-Geom (1H Sword) - Barbarian, Druid, Rogue, Necromancer, Paladin, Sorcerer, Warlock"`. ✓ **Hechicera SÍ está.** C2 del informe es correcta.
- **D1, D2, D4, D5, D6, E1, E4, E5, G5** — todos verificados literales, incluida la errata `"a guaranteed Mtyhic Drop"` (aparece dos veces, en Boss y en Item Updates), `"Up to 10 Resplendent Sparks (plus those in Mythic Caches)"`, `"5 Mythic Unique Caches"`, y `"Mythic Uniques created using the Jeweler's Rune Crafting or the Blacksmith's Mythic Unique cache will not have a Crafted tag."`

### R1 — **LO QUE SE ROMPE: B4 no demuestra lo que dice demostrar**

El informe vende B4 como *"Prueba numérica de la proporción 7:1 con cifras oficiales"*, y el Resumen
lo eleva a *"lo confirman cifras oficiales del PTR"*. Tiene tres problemas encadenados:

**(a) Está fuera del alcance de la regla.** La nota oficial acota el 7× a
`"equipment, Charms, and Tempering recipes"`. Los **Soul Splinters son el sistema de GEMAS de la
temporada** — lo confirma el propio informe sin darse cuenta: Leoric's Crown
`"increases the effect of any gem socketed into the helm"` y el bug fix
`"Leoric's Crown did not apply Soul Splinter Effects"`. **Una gema no es un afijo de equipo, ni un
dije, ni una receta de templado.** Usar valores de gema para demostrar una regla de afijos es un
error de categoría, y encima cruza la línea PTR→final que el propio informe patrulla.

**(b) La aritmética del informe es falsa.** C4 afirma: *"Cuadra en tres de cuatro peldaños"*.
No cuadra en tres. Con `35 / 50 / 375 / 625` × 7 = `245 / 350 / 2625 / 4375` frente a lo publicado
`250 / 175 / 2625 / 4375`:

| Peldaño | Único elemento | Todos los elementos | Ratio real | ¿7,0? |
|---|---|---|---|---|
| 1º | 250 | 35 | **7,143** | ✗ |
| 2º | 175 | 50 | **3,5** | ✗ |
| 3º | 2625 | 375 | 7,0 | ✓ |
| 4º | 4375 | 625 | 7,0 | ✓ |

**Cuadran dos de cuatro, no tres.** El informe se contradice consigo mismo: el Resumen dice bien
*"los dos peldaños altos dan exactamente 7,0"* y luego C4 dice *"tres de cuatro"*. Y el 250 nunca se
menciona como anomalía, solo el 175.

**(c) Elige la lectura que le conviene sin declarar la alternativa.** C4 concluye
*"es una errata de la tabla, y la regla 7× se sostiene"*. Hay otra lectura igual de disponible que el
informe no considera: **los Splinters se tunean aparte y sencillamente no siguen el 7:1**, en cuyo
caso B4 no prueba nada sobre afijos. Que dos peldaños den 7,0 exacto puede ser coincidencia de diseño
de gemas, no confirmación de la regla.

**Corrección:** B4 baja de "prueba" a *indicio compatible*. La regla 7× sigue siendo **oficial** por
B1 — no necesita a B4 para nada. Quitar B4 del Resumen no debilita el informe; **mantenerlo como
prueba sí lo ensucia.**

### R2 — **Etiquetas de rareza inventadas sobre una tabla oficial**

El informe escribe: *"dan por rareza (Mágico/Raro/Legendario/Único) 250/175/2625/4375"*.

La página del PTR **no imprime esas etiquetas**. Presenta los valores como lista con barras
(`"250/175/2625/4375 Fire Resistance"` en Splinter of Anguish; `"35/50/375/625"` en Splinter of
Hellfire) con una nota genérica: `"The values provided below scale between the different Item
Quality tiers."` **No nombra los peldaños.**

Esto es exactamente lo que el encargo prohíbe: una paráfrasis del investigador presentada como valor
citado. Y si la escalera real empieza en Común (lo más probable en D4: Común/Mágico/Raro/Legendario),
**el mapeo del informe está desplazado un peldaño entero**.

**Corrección:** escribir `250/175/2625/4375` sin asignar rarezas, y declarar explícitamente que la
fuente no las etiqueta.

## 4. Teorycrafting / PTR vendido como hecho — **PASA con una salvedad**

El etiquetado es honesto en el cuerpo: B5, B6, B7, C1, E6 y el texto de Leoric's Crown llevan todos
marca **PTR** o **sinconfirmar**, y la inferencia propia va rotulada
(*"Lectura para el jugador (inferencia mía, no dato de fuente)"*, *"Inferencia mía, no dato de fuente"*).
Eso está bien hecho y es raro verlo.

### R4 — La salvedad: 5× y 7× conviven sin reconciliarse

B5 da `630 → ~3000` (≈4,8×) medido por jugadores en PTR. B1 da **7×**. El informe pone ambos sin decir
que **miden cosas distintas** — B5 es el valor absoluto de un afijo, B1 es la *proporción entre dos
tipos de afijo*. No son contradictorios, pero el informe no lo aclara, y H3 admite que las únicas
cifras concretas que existen son las del PTR. Un lector saca de ahí que el afijo final vale ~3000.
**Nada respalda eso para 3.2.1.**

**Corrección:** una línea diciendo que 5× y 7× no son la misma magnitud, y que el valor absoluto del
afijo en 3.2.1 es desconocido (ya está en H3, pero el Resumen no lo lleva).

### R3 — C1/C6: la conclusión es correcta, la cronología no

Verifiqué el punto crítico y **el informe acierta en lo que importa: son NUEVE, sin Ring of Royal
Grandeur.** Blizzard final lista 9 y RoRG no está. Confirmado.

Pero fui más allá y la historia real es otra:

- Busqué `"Ring of Royal Grandeur"` en la página **del PTR de Blizzard**: **no aparece en ninguna
  parte**. Hoy esa página lista **nueve** ítems, los mismos nueve del parche final.
- Icy Veins (30 jul) abre con `"Ten new Uniques are being added..."` y lista **diez**, con RoRG entre
  los de todas las clases — **cinco** de todas las clases.
- Y la página del PTR conserva huérfanas `"Five of them will be usable by all classes, and five will
  be available to a mix of classes"` (5+5=10) y `"Eight of the ten legacy Uniques will also have
  Charms"` — mientras su propia lista tiene 4 de todas las clases y 7 con dije.

La transcripción de Icy Veins **encaja exactamente con las frases huérfanas**. Es decir: Blizzard
editó **el artículo del PTR**, recortando RoRG y cambiando el conteo, y se dejó dos frases atrás.
Icy Veins no es descuidada: es una **foto del original**.

Consecuencia: el recorte ocurrió **durante la ventana del PTR**, no "entre el PTR 3.2.0 y la versión
final 3.2.1" como dice C1. La fila de C6 `Legacy Uniques: 10 (PTR) → 9 (final)` **está mal
etiquetada** — hoy no existe ninguna página de Blizzard que diga diez.

También: el informe titula ese bloque *"Prueba de que la página de Blizzard fue editada"*. Con la foto
de Icy Veins cuadrando, la inferencia es casi segura — pero sigue siendo **inferencia**, no prueba
documental (no tenemos histórico de la página). Debe leerse *"inferencia muy fuerte"*.

**No cambia nada operativo para el jugador. Cambia la etiqueta de C6.**

## 5. Huecos ocultos — **PASA; verifiqué yo los tres más importantes**

Fui a buscar por mi cuenta los datos que más dolerían si estuvieran escondidos:

**H1 (retroactividad) — hueco REAL, confirmado.** Pedí expresamente a la nota oficial *"any sentence
saying existing/equipped items will or will not be updated retroactively"* → **NOT PRESENT**. Y al
artículo de Icy Veins del 13 sep → *"No statement addresses whether this change applies to
already-equipped items."* **El informe tiene razón: nadie lo dice. El hueco es honesto y es el
correcto para marcarlo como el más importante.**

**H2 (dirección del re-tuneo) — hueco REAL.** `"Re-tuned ... to align with other All Resistance
affixes"` no lleva cifra ni dirección en ninguna de las tres fuentes. Confirmado.

**H3 (valores finales del afijo) — hueco REAL.** Icy Veins 13 sep: *"No specific affix values for
single resistance are provided."* Confirmado.

**Hueco que el informe NO declara (R5, menor):** la frase del 7× no dice **cómo** se llega al 7:1.
La primera frase (`"Significantly increased..."`) garantiza que el afijo único **sube**, pero no
descarta que el de Todos los Elementos **haya bajado a la vez** en equipo. El informe marca esa
ambigüedad solo para el **templado** (H2) y la da por resuelta en equipo. No lo está.

**R6 — no verificado por mí, no acusado:** los porcentajes de aspectos de B10 (*Deeper Shadows* +50%,
*Fathomless Dark* 65-85%, etc.) no los comprobé uno a uno. No digo que estén mal; digo que **quedan
sin segunda lectura** y alguien debería pasarles el ojo antes de que entren en la guía.

---

## Lo que el informe acierta y hay que blindar, no tocar

1. **El marco de resistencias (A1–A5) resiste mi ataque.** Verifiqué las cinco celdas contra la
   fuente: fórmula, constante 1136, asíntota 90%, 7000→78,53%, changelog de S11 y fecha 16 ago 2026.
   **Exactas.** Además busqué corroboración fuera de Maxroll y la encontré (el cambio de S11 a sistema
   de rating sin topes por dificultad aparece en fuentes independientes, aunque no citables).
   **El diagnóstico de C3 —"el marco que repite medio internet es de una versión muerta"— es el
   hallazgo más valioso del expediente y sobrevive intacto.**
2. **Pero sigue siendo `unica` y del parche 3.1.x.** El informe lo declara en H10; el **Resumen no lo
   lleva en la misma línea**. Según la regla del proyecto (*el nivel de confianza va en la misma línea
   que el dato*), la línea 1 del Resumen debe decir "una sola fuente preferente, parche 3.1.x". El
   1136 y el 78,53% **no están verificados en 3.2.1 por nadie**.
3. La lista de los nueve, las clases, las dos recetas, las tres vías de Mítico, la etiqueta Crafted,
   los drops y los costes de crafteo: **verificados literales, no tocar.**

## Correcciones concretas antes de que esto entre en la guía

1. **B4 y C4:** degradar de "prueba" a "indicio". Corregir *"tres de cuatro"* → **"dos de cuatro"*.
   Añadir que los Soul Splinters son gemas y **quedan fuera** del alcance declarado del 7×
   (`equipment, Charms, and Tempering recipes`). Quitar del Resumen la frase *"lo confirman cifras
   oficiales"*.
2. **B4:** borrar las etiquetas `Mágico/Raro/Legendario/Único`. La fuente no las imprime.
3. **C6:** corregir la fila a `Legacy Uniques: 10 (Icy Veins, foto del PTR original) → 9 (página PTR
   editada y final)`. El recorte fue durante el PTR.
4. **C1:** *"Prueba de que la página fue editada"* → *"Inferencia muy fuerte"*. Añadir el dato nuevo:
   RoRG **no aparece hoy en ninguna página de Blizzard**, y la lista de Icy Veins encaja exactamente
   con las frases huérfanas ("five... all classes", "eight of the ten").
5. **Resumen línea 1:** añadir el nivel de confianza en la misma línea (`unica`, parche 3.1.x).
6. **Nuevo hueco H11:** no se sabe si el 7:1 en equipo se logra subiendo el afijo único, bajando el de
   Todos los Elementos, o ambos.
7. **B10:** pasar una segunda lectura a los porcentajes de aspectos antes de publicarlos.

## Lo que decide el juego a las 16:30 UTC y ninguna fuente va a decidir

- **H1:** ¿se recalculan los objetos equipados? (mirar un templado de resistencia antes/después)
- **H2/H3:** valor real del afijo de resistencia única y dirección del re-tuneo de Todas las Resistencias.
- **R1:** valores reales de los Soul Splinters en vivo — decide si el 175 era errata o si los Splinters
  van por libre.
- **B7:** si Stone of Jordan iguala de verdad todas las resistencias a la más alta. **Toda la "jugada
  de la temporada" del informe cuelga de una frase de una sola fuente de PTR.** Si eso no es cierto en
  vivo, el punto 4 del Resumen se cae entero.
