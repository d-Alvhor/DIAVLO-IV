# Refutación adversarial — "Builds de Nigromante de Esbirros CON EXPANSIONES"

**Informe auditado:** `investigacion/crudo/exp-builds-nigro.md`
**Fecha de la verificación:** 20 agosto 2026
**Veredicto:** **PARCIAL** — la mayoría de las cifras se confirman literalmente contra fuente primaria, pero **un hallazgo central del informe es falso tal como está redactado** y arrastra tres puntos del plan de acción.

**Método:** he vuelto a descargar el fichero de datos (11.606.292 bytes, `version` = `3.1.0.72698`) y el HTML crudo de todas las páginas citadas, y he reevaluado cada afirmación contra el texto original, sin fiarme de la transcripción del informe. 8 búsquedas web y 11 páginas abiertas. Ninguna fuente vetada respalda ningún número de esta refutación.

---

## 1. 🔴 ERROR GRAVE — el "+60%[x] al gólem por cada sacrificio" es CONDICIONAL

Es el hallazgo que el informe presenta como su descubrimiento propio ("el motor oculto de estas builds", §2.2) y sobre el que apoya el paso 3 del plan de hoy. **Está mal.**

### Lo que el informe transcribe (§2.2)

```
Necromancer_SkeletonMage_Cold_Passive_Sacrifice:
  "...but the amount of Cold Mages you can Summon is reduced by 50%.
   Your Golem gains 60%[x] increased damage."
```

y concluye: *"**Cada sacrificio que NO sea el del gólem le da al gólem +60%[x] de daño.**"*

### Lo que dice el fichero de datos, literal y completo

```
'You deal {c_number}[0.2*(1+Affix_Value_1(1222268)/100)*100|%x|]{/c} increased damage to
 Vulnerable enemies, but the amount of Cold Mages you can Summon is reduced by
 {c_number}50%{/c}.{if:ParagonNodeIsPurchased(681465)}\r\n\r\nYour Golem gains
 {c_number}60%{c_lightgray}\\[x\\]{/c}{/c} increased damage.{/c}{/if}'
```

**El informe eliminó el `{if:ParagonNodeIsPurchased(681465)}` al transcribir.** La cláusula del gólem está dentro de un condicional. Lo mismo ocurre en `Necromancer_SkeletonWarrior_Reaper_Passive_Sacrifice` y en el resto de sacrificios de guerrero y mago.

### Qué es el nodo 681465

```
/paragonNodes/Necromancer_Legendary_005
  {"id": 681465, "name": "Hulking Monstrosity", "rarity": 4, ...}

/skills/Paragon_Necro_Legendary_005
  "Your Golem has 40%[x] increased Maximum Life and deals 100%[x] increased damage.
   Skeletal Mages and Warriors Sacrifice Bonuses grant an additional 60%[x] Golem damage."
```

Es el **nodo legendario "Hulking Monstrosity"**, que vive en un tablero de Paragón que se llama igual (`paragonBoards.Paragon_Necro_02`, `name` = `Hulking Monstrosity`).

**El +60%[x] no es una propiedad del sacrificio. Es una propiedad de ese nodo de Paragón.** Sin el nodo, sacrificar magos o guerreros no le da absolutamente nada al gólem.

### Y el golpe de gracia: ninguna de las dos builds recomendadas coge ese tablero

El propio informe lista los tableros de ambas builds (§5.1 y §5.2):

- Naz Mages: Starter → Frailty → Cult Leader → Flesh Eater → Wither
- Reaper Summoner: Starter → Frailty → Cult Leader → Flesh Eater → Wither

**Hulking Monstrosity no aparece en ninguna de las dos.** Es decir: en las dos builds que el informe recomienda, el "motor oculto" **no se activa nunca**.

### Corroboración independiente

Existe una **tercera** guía de Icy Veins que el informe no menciona (ver error §4 de esta refutación), **Shadow Golems Summoner**, y es precisamente la que sí engancha el tablero:

> *"Board attachment order and pathways: Starter Board – Glyph Slot Mage / **Hulking Monstrosity – Legendary Node** / **Hulking Monstrosity – Glyph Slot Golem** / Cult Leader – Legendary Node / Frailty – Legendary Node / Wither – Legendary Node..."*
> — <https://www.icy-veins.com/d4/guides/golem-summoner-necromancer-build/> (`dateModified` 2026-07-02)

Y esa build es la que usa **Reaper [Sacrifice]** y **Bone [Sacrifice]**. Todo encaja: el motor existe, pero pertenece a la build de gólem, no a las dos que el informe recomienda.

Confirmación adicional en una wiki no vetada:

> *"Hulking Monstrosity Node — Legendary. Your Golem has 40%[x] increased Maximum Life and deals 100%[x] increased damage. Skeletal Mages and Wa[rriors]..."*
> — <https://www.purediablo.com/diablo4/Hulking_Monstrosity_Node>

### Qué hay que corregir en el informe

| Sitio | Qué dice | Qué debe decir |
|---|---|---|
| §2.2 | "Cada sacrificio que NO sea el del gólem le da al gólem +60%[x]" | Solo si se ha comprado el nodo legendario **Hulking Monstrosity** |
| §9 | Lista "el +60%[x] al gólem por cada sacrificio" entre las ganancias gratis de hoy | No es gratis: exige enganchar un tablero de Paragón que ninguna de las dos builds coge |
| §10, paso 3 | "Active el Sacrifice de guerreros y/o magos. Cada uno da +60%[x] de daño al gólem" | El sacrificio sigue valiendo por su bonus propio, pero **no** por el del gólem |

También cae la explicación causal que el informe daba a la frase de Icy Veins *"This build continues to use all minions, even sacrificed ones, for inter-Minion synergies"*: esa frase no se explica por el +60%.

**Nota de método:** este es exactamente el fallo que el encargo pedía cazar. El informe verificó el **valor** (60%, literal y correcto) pero no el **modelo** (de qué depende). Verificar la cita palabra por palabra no basta si se recorta el condicional que la gobierna.

---

## 2. 🟠 §13 — la "información inventada" existe y es real

El informe justifica todo su método en §13 diciendo que el lector de páginas web le devolvió cambios "que **no existen**":

> *"The Gloom Ward: Now procs every 6th instance of damage, down from every 8th"*, *"Aspect of Serration: Critical Strike Chance increased from 5% to 10%"* … *"Descargué el HTML crudo y ninguna aparece en 3.1.1."*

**Las dos aparecen literalmente en las notas oficiales**, en la sección **Necromancer** del parche **3.1.0**:

> *"Necromancer — The Gloom Ward: Now procs every 6th instance of damage, down from every 8th. Bone Graft Paragon Node: Bone damage increased from 40% to 60%. Aspect of Serration: Critical Strike Chance increased from 5% to 10%."*
> — <https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes>

El informe tiene razón en su frase estricta ("ninguna aparece en **3.1.1**"), pero de ahí salta a "no existen" y a "información inventada". **No fue una alucinación: fue una atribución al parche equivocado.** El contenido era bueno.

Consecuencia práctica: el informe **descartó tres cambios reales de Nigromante del 3.1.0** por creerlos falsos.

---

## 3. 🟠 §1.2 está incompleta, y falta un recorte a un anillo que el propio informe recomienda

§1.2 se titula "Otros números del 3.1.0 que mandan sobre las guías". Faltan, todos verificados en el HTML crudo de las notas oficiales:

| Cambio omitido | Texto literal | Por qué importa |
|---|---|---|
| **Hellbent Commander Aspect** | *"Damage reduced from 50-70% to 40-60%"* | 🚩 Es el **Anillo 1 de Reaper Summoner**, la build que el informe recomienda (§5.2). Se llevó un recorte y el informe no lo menciona |
| **The Gloom Ward** | *"Now procs every 6th instance of damage, down from every 8th"* | Único de habilidades de Oscuridad — mejora, relevante a build de sombra |
| **Aspect of Serration** | *"Critical Strike Chance increased from 5% to 10%"* | Duplicado; el crítico es objetivo duro de Maxroll (100%) |
| **Bone Graft Paragon Node** | *"Bone damage increased from 40% to 60%"* | Nodo de Paragón |
| **Corpse Explosion** | *"Bloody Mess Variant Damage bonus increased from 50% to 75%. Miasma Variant Damage increased from 145% to 210%. Shrapnel Variant Damage increased from 100% to 110%"* | Variantes buffadas |

El valor que el informe cita para Hellbent Commander en §5.2 ("60%[x] [40 – 60]%") **es el correcto post-recorte** — lo copió bien de Icy Veins. El problema no es el número, es que §1.2 se presenta como el filtro de "qué cambió y le afecta" y deja fuera un nerf a una pieza que recomienda.

---

## 4. 🟠 Falta una tercera build de esbirros de Icy Veins, y es la más pertinente a su caso

El informe (§0, §8) presenta el panorama de Icy Veins como dos builds: Naz Mages (S) y Reaper Summoner (A). Existe una tercera:

> **Shadow Golems Summoner — A-Tier**, GhazzyTV y Garm Z, `dateModified` **2026-07-02**
> *"The Golem that will carry you though the deepest levels of Pit!"*
> — <https://www.icy-veins.com/d4/guides/golem-summoner-necromancer-build/>

Por qué es una omisión que duele en este caso concreto:

1. Es **la única de las tres que engancha el tablero Hulking Monstrosity**, o sea la única donde el motor de sacrificios del que habla §2.2 funciona de verdad.
2. Usa **Mace of King Leoric**, el arma cuyo buff (70-80% → 100-120%) el informe destaca en §1.2 y luego no conecta con ninguna build (*"Opción de arma para gólem puro"* y se queda ahí).
3. El jugador viene de **Gravebloom (3 gólems) + Gólem de Sangre**: es un perfil de gólem. Una build A-tier de gólem es un candidato obvio que no se le ha puesto delante.
4. Usa **Litany of Death**, una de las 23 variantes recién desbloqueadas.

Su configuración de tipos es distinta: *"Skeletal Warriors: Reaper [Sacrifice]. Skeletal Mages: Bone [Sacrifice]. Golem: Iron [Upgrade #1]"* — nótese **Upgrade #1**, no Sacrifice.

---

## 5. 🟠 §3.2 — la inferencia del borde no se sostiene por el motivo que da

El informe razona:

> *"Las cinco variantes que usted ya tenía son las cinco del mismo borde (`678742091`), y Gargantua es del borde `858665677`. **Cinco de cinco.** Con la regla '2 de 3 gratis', la conclusión es que el borde `858665677` es el bloqueado."* … *"Es sólida (5/5)"*

**El hecho es correcto; el razonamiento no.** Verificado uno a uno en el fichero:

| Variante | Habilidad | `border` |
|---|---|---|
| Coven | Skeleton Mage | 678742091 |
| Master of Puppets | Skeleton Warrior | 678742091 |
| Gravebloom | Golem | 678742091 |
| Unyielding Commander | Army of the Dead | 678742091 |
| Schadenfreude | Iron Maiden | 678742091 |
| **Gargantua** | Golem | **858665677** |

5/5 en el borde 1: cierto. Pero de ahí **solo** se deduce que el borde 1 es gratis. **No distingue cuál de los otros dos (858665677 o 2916187532) es el bloqueado** — el jugador simplemente eligió la variante 1 en las cinco habilidades, lo que no informa nada sobre las otras dos ranuras. El informe elige `858665677` entre dos candidatos igual de compatibles con su evidencia.

La conclusión probablemente sea correcta (es coherente con que el jugador no tuviera Gargantua), pero **la evidencia que el informe presenta no es la que la sostiene**, y "sólida (5/5)" sobrevende.

Además, un dato de §3.2 es falso: *"solo hay 3 IDs de borde en todo el juego, ~194 usos cada uno"*. Hay **cuatro**:

```
678742091: 194 | 858665677: 195 | 2916187532: 193 | 3096111118: 1
```

El cuarto (`3096111118`) es un caso único, en `Prismatic Familiar` del Hechicero.

**Atenuante:** el informe declara esto como inferencia propia y lo repite en "No encontrado" #4. La honestidad está; la fuerza del argumento no.

---

## 6. 🟡 §6 — la transcripción "literal" del set Black Shroud pierde dos cláusulas

El informe dice de §6: *"Los números de arriba son literales"*. El 5 piezas de Peace of the Black Shroud, completo:

```
"You deal 175%[x] increased Shadow and Cold damage.
 Enemies who are Corrupted or Frostbitten for more than their remaining life are
 permanently Vulnerable, Weakened, Slowed by 85%, take 50%[x] increased damage from you,
 and are Feared every 5 seconds."
```

El informe omite **"permanently"** y **"and are Feared every 5 seconds"**. El miedo no es cosmético en una build de esbirros: dispersa a los enemigos y afecta a cómo pegan los esbirros comandados.

---

## 7. 🟡 Maxroll sigue recomendando Dominate — el informe no lo avisa

§1.2 dice, con razón, que el glifo Dominate está aniquilado y que *"cualquier guía que aún lo recomiende está muerta"*. §10 paso 6: *"si tiene Dominate puesto, quítelo"*. Correcto.

Pero la guía de Maxroll —**actualizada el 22 julio 2026, tres semanas después del recorte**— sigue listando Dominate como **primer glifo a subir** en una de sus tres variantes:

> *"Level up your glyphs in the following order **Dominate** Mage Essence Warrior Abyssal"*
> y antes: *"the increased stacks to Overpower, a healthy boost to the additive damage provided by **Dominate**"*
> — <https://maxroll.gg/d4/build-guides/minion-necromancer-guide>

Es una trampa viva en una fuente que el informe avala en todo lo demás. Debería estar señalada junto al caso Icy Veins/Pelghain de §1.1: es el mismo patrón, en la otra fuente preferente.

---

## 8. 🟡 "No encontrado" #2 no está tan vacío: hay una línea oficial sobre Unholy Frenzy

El informe deja abierto si Unholy Frenzy rompe Blood Moon Breeches. Las notas oficiales del 3.1.0 —el fichero que el informe dice haber leído *"línea a línea"*— contienen:

> *"Fixed an issue where taking the Unholy Frenzy Variant of Decrepify would cause Iron Maiden to fail to apply to enemies."*
> — <https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes> (sección 3.1.0)

No cierra la pregunta entera (habla de Iron Maiden, no de Decrepify), pero es la única evidencia escrita y oficial que existe sobre esa interacción, y cambia el cuadro: **era un bug y está arreglado desde el 30 de junio.**

Contexto adicional, **testimonio de jugadores y anterior al arreglo** (mayo 2026, no autoritativo, lo marco como tal): un hilo del foro oficial describe el comportamiento roto previo — *"casting decrepify on monsters has no effect, whether you do it manually or through runes/blood moon breaches"* (<https://us.forums.blizzard.com/en/d4/t/blood-moon-breachesunholy-combo/249118>). Sirve para saber qué se arregló, no para describir el estado actual.

---

## 9. Lo que he intentado refutar y NO he podido — queda confirmado

Todo esto lo he comprobado contra fuente primaria y **el informe acierta**:

| Afirmación | Resultado |
|---|---|
| Texto literal de Gargantua | ✅ Verbatim en `skills.Necromancer_Golem.mods[2]` |
| `powerTables[34]` → 20/22/24/29/40/51/62% | ✅ Recalculado: exacto. Tabla = `[1,1,1.1,1.2,1.3,1.45,...]` |
| Variantes del gólem = Gravebloom / Fel Gluttony / Gargantua | ✅ Confirmado |
| Bone/Blood/Iron es el **tipo**, eje independiente | ✅ **Confirmado por el propio juego**: el mod 6 del Gólem dice *"based on whether your Golem type is Bone, Blood, or Iron"*. "Gargantua + Iron [Sacrifice]" es legal |
| Fórmulas `pets[].max` | ✅ Verbatim. **Sospeché un error de traducción y me equivoqué**: `Mod(582507894)` es un identificador de *ranura*, reutilizado en las 23 habilidades (ranura 1 = borde 678742091). En la fórmula del guerrero resuelve a Master of Puppets, en la del mago a Coven, en la del gólem a Gravebloom. La lectura del informe es correcta |
| Golem Iron Sacrifice: quita daño, no elimina al gólem | ✅ Verbatim. El aura de Gargantua sobrevive. Retirada de sospecha del informe, correcta |
| Signet of Pelghain 15-20 → 10-15, solo Frío | ✅ Verbatim en notas oficiales |
| Icy Veins sigue publicando 15-20% en su tabla | ✅ Confirmado hoy: *"take 20%[x] [15 – 20]% increased damage"* |
| Glifo Dominate 23,6% → 1,8% | ✅ Verbatim |
| Red Blessing 4 → 2 | ✅ Verbatim |
| Wither y Darkness ahora con Frío | ✅ Verbatim |
| Mace of King Leoric 70-80 → 100-120 | ✅ Verbatim |
| Mítico 5 → 4 fragmentos (3.1.1); 1 solo mítico crafteado | ✅ Verbatim, y Maxroll: *"You can only equip one Mythic that you craft"* |
| 83 puntos / 69 por niveles / 14 por Season Rank | ✅ Verbatim en ambas guías |
| Objetivos duros de Maxroll | ✅ Verbatim: *"MINIMUM STAT REQUIREMENTS: 100% Attack speed… 100% Critical strike chance… 30k maximum life… 40+ resolve stacks"*. (Los busqué primero como "30.000" y no salían; están como "30k". No es un error del informe) |
| Set Rathma's Waking Touch (`Talisman_Necro_05`) — los tres bonus | ✅ Verbatim, los tres |
| Tier lists Maxroll del 29 junio, pre-3.1.0 | ✅ Changelog: *"June 29, 2026 Updated for Season 14 start"*. Contenido de ambas tablas, exacto |
| Icy Veins S / A, `dateModified` 2026-07-03 | ✅ Al segundo: `12:05:00` y `12:04:16` |
| Reapers [Upgrade #2] es **+**50%, el guion de Icy Veins es artefacto | ✅ Datos: *"Reapers deal 50%[x] increased damage and have a 15% chance to Stun"* |
| 3.1.1 y 3.1.2 no tocan Nigromante; 3.1.3 solo el arreglo visual | ✅ Segmenté las notas por parche: 3.1.1 y 3.1.2 → **0 apariciones** de Necromancer/Golem/Skeleton/Minion/Sacrifice |
| Builds #72592 / #72836 / #73020 / #73224 | ✅ Los cuatro, exactos |
| `version` del fichero = 3.1.0.72698 | ✅ Confirmado |
| "Book of the Dead" ausente del fichero | ✅ 0 resultados — y **también 0 en las notas oficiales 3.1.x** |
| Cubo Horádrico requiere Lord of Hatred | ✅ Corroborado por fuentes independientes |
| Tidal Aspect obligatorio para Banished Lord's Talisman | ✅ Verbatim: *"REQUIRES imprinted Tidal Aspect using Kullean Tuning Prisms with the Horadric Cube"* |
| Mobalytics devuelve 403 | ✅ Reproducido (HTTP 403) |

### Una sospecha mía que investigué y resultó infundada

Icy Veins llama al set *"Berú of the Black Shroud"* y el fichero de datos lo llama *"Peace of the Black Shroud"*. Parecía una discrepancia de nombres. **No lo es:** "Berú of the Black Shroud" es **una de las cinco piezas** del set "Peace of the Black Shroud" (junto a Phoba, Fer, Mlor y Linta). El informe usa el nombre correcto del set.

---

## 10. Veredicto

**PARCIAL.**

El informe es, en su parte numérica, **inusualmente sólido**: he intentado tumbar 26 afirmaciones concretas contra fuente primaria y las 26 se sostienen palabra por palabra. La disciplina de citar el fichero de datos y el HTML crudo funciona, y la sección de "No encontrado" es honesta.

Pero **el hallazgo que el informe presenta como su aportación propia —"el motor oculto de estas builds"— es falso tal como está escrito**, y no por un decimal: por haber recortado un condicional al transcribir. El +60%[x] al gólem depende del nodo legendario Hulking Monstrosity, y ninguna de las dos builds recomendadas lo coge. Eso invalida el paso 3 del plan de hoy y una de las tres razones por las que §9 dice que el cambio barato merece la pena.

A eso se suma una omisión con consecuencias (§1.2 sin el nerf a Hellbent Commander, que es un anillo de la build recomendada) y una tercera build A-tier de Icy Veins —la de gólem— que es la que de verdad encaja con el motor de sacrificios y con el perfil actual del jugador.

**Recomendación:** no publicar §2.2, §9 y §10 paso 3 sin corregir; añadir Shadow Golems Summoner al abanico; completar §1.2; y reescribir §13, que acusa de invención lo que era una atribución de parche equivocada.
