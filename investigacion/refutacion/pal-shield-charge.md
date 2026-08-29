# Refutación adversarial — "Paladín Carga con Escudo (Shield Charge Paladin)"

**Informe verificado:** `/Users/alvhor/Proyectos/DIAVLO IV/investigacion/crudo/pal-shield-charge.md`
**Fecha de verificación:** 24/08/2026 · **Parche vivo:** 3.1.3 (build 73224, 12/08/2026)
**Método:** descarga en crudo e independiente de las tres fuentes primarias + 10 búsquedas y 12 páginas abiertas.

## VEREDICTO: **PARCIAL**

El núcleo técnico del informe es **excepcionalmente sólido**. He reproducido de forma independiente
el fichero de datos, el JSON del planificador y el HTML de la guía, y he verificado **nodo a nodo**
el árbol de habilidades, los 18 nodos de mejora seleccionados, los 10 aspectos con sus valores, las
6 runas, los mercenarios, los 5 tableros de Paragón y las 6 bonificaciones de conjunto. Prácticamente
todo cuadra al byte y a la cita literal.

**Pero hay 11 errores**, y **uno de ellos invierte la recomendación central del documento**.

---

## 🔴 E1 — CRÍTICO: la regla que el informe llama "la respuesta a tu pregunta" fue DEROGADA el 16/07/2026

El informe construye su recomendación estructural sobre esta nota del autor del planificador:

> "Solo puedes equipar UN objeto Mítico que hayas crafteado mediante el Cubo Horadrico, pero sí puedes
> equipar todos los Míticos conseguidos por otras vías."

**He confirmado que esa cita está literalmente en el planificador** (aparece 4 veces, una por perfil,
texto original: *"MYTHIC CRAFTING ORDER You can only equip one Mythic item that you have crafted through
the Horadric Cube, but you are able to equip all Mythics that are acquired elsewhere"*).

**El problema no es la cita. Es que la regla ya no existía cuando el autor la escribió.**

Hotfix **3.1.1a, 16 de julio de 2026**, en fuente PREFERENTE:

> "Removed the 'one-crafted Mythic' equipment restriction on Mythic items."
> — https://www.icy-veins.com/d4/news/diablo-4-season-14-hotfix-crafted-mythic-restriction-removed-and-mythic-drop-rate-increased/ (fechada 16/07/2026)

Corroborado por el hilo oficial de Blizzard `3.1.1a Patch - July 16, 2026`
(https://us.forums.blizzard.com/en/d4/t/311a-patch-july-16-2026/263234) y por mobalytics
(https://mobalytics.gg/diablo-4/guides/patch-3-1-1a-what-changed).

**Cronología que lo deja sin defensa:**

| Fecha | Hecho |
|---|---|
| 16/07/2026 | 3.1.1a **elimina** el límite de un solo Mítico crafteado |
| 25/07/2026 | El autor guarda el planificador **con la nota obsoleta dentro** |
| 12/08/2026 | Parche vivo 3.1.3 — el límite sigue sin existir |

**Impacto en las secciones §7, §14 y §15 del informe:**
- ❌ "**Craftea el pecho (Mantle of the Grey) y solo el pecho.** Los otros dos, a esperar que caigan."
- ❌ "🔓 EL OBJETO QUE ABRE EL SALTO A ENDGAME — **El Mítico crafteado — y solo UNO**"
- ❌ "**No hagas esto:** no gastes el crafteo mítico en nada que no sea el pecho"

**Corrección:** el jugador puede craftear y equipar **los tres** (Mantle of the Grey, Tibault's Will,
Herald of Zakarum) por el Cubo. Con ~4 semanas de temporada, esto cambia por completo el plan de farmeo.

⚠️ El informe **sí flagueó la regla** en "No encontrado #11" ("no la vi en notas oficiales"), lo cual es
honesto — pero aun así la usó como titular en tres secciones sin registrar que hay fuentes
independientes diciendo que fue retirada. La duda declarada no neutraliza la recomendación afirmada.

**Nota adicional del mismo hotfix**, relevante y no recogida:
> "Removed the ability to add the Mythic modifier to Unique Charms & Seals in the Cube."

---

## 🔴 E2 — Griswold's Opus: las dos cifras están mal (tope inflado ×3)

**Informe §7:** *"Infligir daño directo otorga **2%[x]** de Daño de Golpe Crítico por cada enemigo
golpeado en 10 s, hasta **[150]%[x]**."*

**Datos reales.** El objeto equipado en el planificador es
`Talisman_Charm_Unique_1HSword_Unique_Paladin_002`, con `values: [1, 150]`. El tooltip del cliente es:

```
Dealing direct damage grants [Affix_Value_1|2%x|] increased Critical Strike Damage
for each enemy hit within 10 seconds, up to [50*Affix_Value_1|%x|].
At Maximum you gain:
Lucky Hit: Critical Strikes have up to a 50% chance to deal double damage,
Heal for [Affix_Value_2] Life, and refresh the duration of the bonus.
```

- `Affix_Value_1 = 1` → **1%[x] por enemigo**, no 2%.
- Tope = `50 × Affix_Value_1` = **50%[x]**, no 150%.
- `Affix_Value_2 = 150` es la **Vida curada** del Golpe de Suerte, no un tope de daño.

**Origen del error:** el informe leyó el especificador de formato `|2%x|` (2 decimales) como si el "2"
fuera el valor. Que es un especificador queda demostrado por Mantle of the Grey, donde
`[Affix_Value_2*100|1%x|]` con valor 0.06 da 6%[x] — y ahí el informe **sí** acertó.

**Prueba de incoherencia interna:** el propio informe da 2% por enemigo y tope 150%. Con la fórmula
`tope = 50 × valor`, 2 × 50 = 100, no 150. Los dos números no pueden ser ciertos a la vez.

**Impacto:** §7 dice *"es de los primeros objetivos, no un lujo"* y §15 lo pone en prioridad 3 como uno de
"los dos mayores multiplicadores". Con 50%[x] real en lugar de 150%[x], su prioridad baja bastante.

---

## 🔴 E3 y E4 — Colisión de identificadores entre habilidades: dos atribuciones falsas

Los `Mod(...)` del fichero de datos **se reutilizan con distinto significado en cada habilidad**. Lo he
verificado volcando los IDs por habilidad:

| ID | En Shield Charge | En Clash |
|---|---|---|
| 2686060762 | **Damage Bonus** | **Faith Generation** |
| 2686060764 | **Hit Count As Blocking** | **Crusader's March Effectiveness** |

El informe cruzó los dos espacios de nombres y produjo dos afirmaciones falsas.

### E3 — Clash: "20 de Fe (30 con la mejora *Damage Bonus*)"

Fórmula real: `Generate Faith: [20+(Mod(2686060762)?10:0)]`. En el espacio de Clash, 2686060762 es
**Faith Generation** (*"Clash generates 10 additional Faith"*), no Damage Bonus.

**Y es peor:** he decodificado los nodos seleccionados del planificador — Clash lleva **Punishment,
Resolve y Crusader's March Effectiveness**. **Faith Generation NO está cogida.** Por tanto en esta build
Clash genera **20 de Fe, punto**. El "(30)" no ocurre nunca.

### E4 — Punishment: "+30% Represalia (×1,25 si tienes *Hit Count As Blocking*)"

Fórmula real: `[0.3*(Mod(2686060764)?1.25:1)*100|+%|]`. En el espacio de Clash, 2686060764 es
**Crusader's March Effectiveness**. El ×1,25 lo activa esa mejora, no Hit Count As Blocking (que es de
Shield Charge y no interviene en esta fórmula).

El resultado numérico (37,5%) **sí es correcto** para esta build, porque Crusader's March Effectiveness
está cogida — pero la relación causal que el informe enseña al lector es falsa.

**Omisión asociada:** el informe corta Punishment con puntos suspensivos (*"+Espinas, …"*) y se deja el
tercer punto: `[0.2*(Mod(2686060764)?1.25:1)*100|%x|]` → **+20%[x] de daño de Espinas (25%[x] con CME)**.
En una build cuyo motor son las Espinas, ese multiplicador no es un detalle.

---

## 🔴 E5 — El perfil Intermedia NO llega a Resolve 30

**Informe §14 (INTERMEDIA):** *"Temples de Resolve +3 → **+6**"* y *"**Ahora sí llegas a Resolve 30.**"*

**Valores reales del planificador** (`Tempered_Generic_ResolveStacks_Tier3`):

| Perfil | Casco | Pecho | Pantalones |
|---|---|---|---|
| Starter | 3 | 3 | 3 |
| **Midgame** | **5** | **5** | **5** |
| Endgame | 6 | 6 | 6 |

Aritmética del perfil Intermedia: 8 (base) + 3×5 (temples) + 2 (Yunque de Glynn) + 2 (set 3 pz) = **27**.

**Solo el perfil Endgame llega a 30.** El informe adelantó el hito una etapa entera.

(El arranque sí lo tiene bien: 8 + 3×3 + 2 = **19**, dentro del "19-21" que estima. Y el propio informe
acierta al decir que el +6 exige crítico de temple *y* crítico de Masterwork — esa frase está literal en
el planificador: *"This temper needs to crit and be Masterwork crit to go to +6."*)

---

## 🔴 E6 — Paragón: se ha dejado fuera un paso entero; los glifos llegan a 150, no a 100

**Informe §11:** *"El planificador guarda **tres estados** con **glifos a nivel 1 → 50 → 100**"*.

**Real: los cuatro perfiles guardan CUATRO pasos, con glifos a 1 → 50 → 100 → 150.**

Recuento de nodos verificado (perfil Endgame):

| Tablero | glifo 1 | glifo 50 | glifo 100 | **glifo 150** |
|---|---|---|---|---|
| Start | 27 ✓ | 31 ✓ | 39 ✓ | **39** |
| Relentless | 60 ✓ | 60 ✓ | 60 ✓ | **68** |
| Beacon | 37 ✓ | 52 ✓ | 60 ✓ | **75** |
| Castle | 46 ✓ | 54 ✓ | 54 ✓ | **81** |
| Shield Bearer | 28 ✓ | 53 ✓ | **75** ← el informe pone "—" | **83** |

Tres fallos derivados:
1. **§14 y §15 mandan al jugador a "Glifos a 100"** cuando el objetivo del propio autor es **150**.
2. La casilla de Shield Bearer a glifo 100 aparece como **"—"** cuando el valor es **75**.
3. *"completa Relentless primero (ya está lleno desde el principio)"* solo vale hasta glifo 100:
   en el paso 4 sube de 60 a **68**.

Todo lo demás del §11 es correcto: tableros, rotaciones, posiciones, glifos asignados, afijos de
Sentinel (`DamageWithJuggernautSkills_Strength_Main` + `MultDmgToClose_Legendary`) y el aviso de los
**tres** glifos homónimos (Spirit, Outmatch y Revenge tienen 3 variantes cada uno — confirmado).

---

## 🟠 E7 — "3.1.3: CERO cambios de clase" es falso tal como está escrito

El informe lo afirma dos veces (§0 y Fuentes #6) y lo usa para justificar el desfase de versión.

Las notas oficiales de 3.1.3 **sí tienen una sección "Class Changes"**, con tres entradas:
Druida (deformación de alas al Petrificar al Corrupted Reaper), Nigromante (habilidades de Sombra
tapaban al Corrupted Reaper) y Brujo (transparencia de Dark Prison).

Son arreglos visuales sin un solo número, y **ninguno toca Paladín**, así que la *conclusión*
("3.1.0 ≈ 3.1.3 para esta build") **se sostiene**. La afirmación categórica, no.

---

## 🟠 E8 — El hueco de "No encontrado #1" es autoinfligido: 3.1.1 y 3.1.2 estaban en la página que ya citaba

**Informe, No encontrado #1:** *"Hay una ventana de dos revisiones (julio 2026) que no he leído.
⚠️ Si algo de esta guía falla, es el candidato número uno."*

Las notas de **3.1.1 (14/07/2026) y 3.1.2 (28/07/2026) están en la misma URL que el informe cita dos
veces**: https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes

Las he leído. **Resultado: ni 3.1.1 ni 3.1.2 contienen una sola entrada de Paladín** — ni habilidades,
ni mecánicas, ni objetos únicos. Es decir: el hueco que el informe señalaba como su mayor riesgo
**se cierra a favor del informe**, pero solo porque otro lector lo ha abierto.

**Consecuencia colateral:** el coste del Cubo que el informe marca **[EXT]** ("bajó de 5 a 4 fragmentos
en 3.1.1", con aviso de "verifícalo en el Cubo") está **literal en esa página oficial**:

> "Reduced the cost of the Upgrade to Mythic recipe on the Horadric Cube from 5 to 4 Pandemonium Fragments."

Está infravalorado como [EXT] cuando es [WEB] oficial. Lo mismo con dos fuentes de fragmentos:
*"Corrupted Reaper now drops up to two Pandemonium Fragments, scaling with Torment level"* y
*"Repeatable Glints of Hope Reputation Reward now guarantees a Pandemonium Fragment."*

---

## 🟠 E9 — Griswold's Opus: se confunde el encanto con la espada, y con él la ruta de farmeo

El planificador equipa `Talisman_Charm_Unique_1HSword_Unique_Paladin_002` — el **encanto único**.
La página de Icy Veins que el informe cita describe Griswold's Opus como **espada de una mano
(One-Handed Sword)** que cae de Duriel y Harbinger of Hatred.

El informe traslada la ruta de caída del **arma** al **encanto** en §7, en §14 ("Farmea Griswold's
Opus — Duriel o Harbinger of Hatred") y en §15 ("Duriel → Mantle of the Grey + Griswold's Opus …
Un solo jefe, dos objetivos").

La página de talismán de Maxroll (fechada 28/06/2026) dice que los encantos únicos son
*"standalone item drops that provide the power of their respective Unique item when they're equipped"*
— caídas independientes. **La fuente de caída del encanto queda sin verificar.**

El gancho "un jefe, dos objetivos" del §14 y del §15 **no está demostrado**.

---

## 🟡 E10 — Yom: la fuente citada dice otra cosa que la que se imprime

**Informe §8** presenta la tabla de runas como *"[maxroll runewords] **[WEB]**, corroborado en d4guides.gg"*,
y para Yom escribe: *"Invoca Petrificar del Druida, Aturdiendo enemigos y **aumentando tu Daño de Golpe
Crítico contra ellos**."*

- **Fichero de datos:** *"Stunning enemies and increasing your Critical Strike Damage against them."*
- **Página de Maxroll citada:** *"Invoke the Druid's Petrify, Stunning enemies and **restoring 100 Resource**."*

Las dos fuentes **no dicen lo mismo**, y el informe imprime la versión del datamining bajo una cita de
Maxroll. El razonamiento *"Yom (Petrificar) aturde y sube crítico"* se apoya solo en el datamining.

(Todo lo demás del §8 está confirmado por ambas: 2 palabras rúnicas por personaje, y las ofrendas
Moni 100 / Igni 25 / Cir 300 / Yom 500 / Kry 300 / Ceh 100 coinciden exactamente.)

---

## 🟡 E11 — La conclusión sobre encantos duplicados está sobreafirmada

**Informe §9:** *"**→ El endgame corre la bonificación de 3 piezas de Cathan's Righteous Will.**"*

El argumento es: el autor dice que el set aporta +2 de Resolve, que es la bonificación de 3 piezas.

**El argumento no cierra.** Las bonificaciones de conjunto en D4 son escalonadas y acumulativas
(2/3/5 confirmado en `itemSets`), así que llevar 5 piezas **también** otorgaría el +2 del escalón de 3.
La aritmética del autor no distingue entre "3 piezas" y "5 piezas". Y la página de talismán de Maxroll
**no dice** si los duplicados cuentan — lo he comprobado expresamente.

El informe marcó la premisa como **[EXT]** (correcto), pero luego escribió la conclusión en negrita y
con flecha. Debe quedarse en hipótesis. Lo mismo aplica al 💡 "pista fuerte" sobre la variante Push,
aunque ahí el informe **sí** avisa de que es deducción suya (y la premisa es correcta: el 3 piezas de
Iron Conviction dice literalmente *"Your Auras Skills gain all of their Upgrades"*).

---

## Omisiones menores (no invalidan nada, pero faltan)

- **Bastion** también da *"surrounding allies Unstoppable for 1.0 seconds"*. Importa porque el §7
  argumenta la Imparabilidad casi permanente para Tibault's Will — y en dúo esa fuente también se pierde.
- **Herald of Zakarum** tiene un tercer implícito no mencionado: `INHERENT_Shield_Damage_Bonus`.
- **Igni** omite *"(Up to 500 Offering)"*.
- La receta *Upgrade to Mythic* **se desbloquea a nivel 70 y en Tormento I o superior** — dato útil
  para un jugador que acaba de llegar a 70.
- **§12** copia del FAQ *"Vulnerable → Fanaticism Aura"*, pero eso requiere **Rite of Humility**, que esta
  build **no coge** (coge Rite of Vengeance). El Vulnerable real viene de Condemn / Gather the Guilty,
  como el propio informe dice en §3. Contradicción interna heredada del FAQ sin filtrar.

---

## ✅ Lo que he intentado tumbar y NO he podido: verificaciones confirmadas

Todo esto lo he reproducido de forma independiente y **coincide exactamente**.

### Procedencia y cifras de fichero
| Afirmación | Resultado |
|---|---|
| Guía fechada `<time dateTime="2026-07-25">` | ✅ **Única ocurrencia** en 477.063 bytes de HTML (HTTP 200, sin 403) |
| `data.min.json` = 11.606.292 bytes, `version` = `3.1.0.72698` | ✅ **Exacto al byte** |
| Planificador = 167.015 bytes, 4 perfiles, `2026-07-25 16:06:08`, `maxrollId: chronikz` | ✅ Exacto (+ `userId 217915`, `season "14"`) |

### Árbol de habilidades — la verificación más fuerte del informe
- **83 puntos** ✅ (suma exacta)
- Rangos 15/15/15/15 + Clash 4 + Condemn 1 ✅
- *"El árbol es IDÉNTICO en arranque, intermedia y endgame … cero diferencias"* → ✅ **diff = 0 nodos**
- Variante Push: suelta **exactamente** las 6 mejoras de las dos Auras y sube Clash 4→10, sigue en 83 ✅
- **Los 18 nodos de mejora seleccionados**, uno por uno ✅ (Shield Charge: Hit Count As Blocking,
  Relentless Charge, Damage Bonus — y *Retribution* y *Resolve* efectivamente a rango 0)

### Textos del cliente, literales
Juramento Juggernaut (2261363: 8 acumulaciones, 0.8→80%[x], 20% tamaño, 5 s, Mínimo +1, ya no se
consume al recibir golpes) ✅ · Hit Count As Blocking ✅ · Relentless Charge (Core, 20 Fe + 1/s) ✅ ·
Damage Bonus (10%[x]/6 s hasta 30%[x]) ✅ · Fortress Resolve Damage Bonus **4.0%[x] por acumulación** ✅ ·
Rampart of Thorns (50% ralentización, **500%** de Espinas/s) ✅ · Fortress Inmune **3 s** (buff 582558634,
`duration: 3`) y **recarga 60 s** (campo `cooldown: 60`) ✅ · Clash Resolve **2 acumulaciones** ✅ ·
Crusader's March Effectiveness **25%[x]** ✅ · **Retribution `heroDetails[1][119]`** — cita textual exacta,
incluido el nombre del campo ✅ · Defiance Aura *"Active: You become Unstoppable for 2 seconds"* ✅
(sospeché que era el nodo y no la activa; **el informe tiene razón**) · Condemn *"you become Unhindered"* ✅

**Corroboración externa independiente:** wowhead.com/diablo-4/skill/shield-charge-2466077 reproduce
palabra por palabra los textos de Relentless Charge, Damage Bonus, Hit Count As Blocking y Retribution.

### Objetos
| Objeto | Verificación |
|---|---|
| Mantle of the Grey | `values [0.06]` → **6%[x] por punto**, 16 Resolve, 25% tamaño ✅ (≈96%[x] correcto) |
| Herald of Zakarum | `values [0.5]` → **50%** ✅; implícito Bloqueo `[0.4]` → **40%** ✅; **Indestructible** ✅; Represalia +50%[+] tamaño ✅ |
| Tibault's Will | `values [20]` → **20%[x]** ✅, 50 regeneración, 5 s ✅ |
| Blood-Mad Idol | 200%[x] Quemadura / 8 s ✅ |
| **Los 10 aspectos** | Valores 4 / 45 / 75 / 0,65 / 70 / 0,4 / 4.578,96 / 1 / 0,6 / 975,73 ✅ **todos exactos**, y los nombres salen de los campos `prefix`/`suffix` reales — incluido el rarísimo **"Sticker-thought"**, que es un prefijo genuino |
| Yunque de Glynn | *"maximum Resolve increased by 2 … [4]% DR per Resolve, up to [40]%"* ✅ |
| Temples | Starter +3 / Endgame +6; crítico 5%→10%; físico 40%→50%; aura 10%→20%; RdR 6%→7,5% ✅ |
| "of Steel" endgame | `X2_Transfiguration_DamageTypePercent_Physical`, valor **0,125**, en **las 10 piezas**, ausente en Intermedia ✅ (y el sufijo real **es** "of Steel") |

### Conjuntos, runas, mercenarios, Paragón
- **Cathan's Righteous Will** (`Talisman_Pala_01`) y **Cathan's Iron Conviction** (`Talisman_Pala_05`) ✅
  — nombres reales, escalones 2/3/5 ✅, y **los seis textos de bonificación son literales exactos**
  (incluido el 3 pz: *"Minimum Resolve … increased by 2 and Maximum Resolve … increased by 2"*).
- Distribución de encantos por perfil ✅ exacta, incluidos los **tres Phoba** del endgame.
- Runas por perfil: Cir+Ceh / Moni+Kry (arranque); Moni+Yom / Igni+Kry (int./endgame/push) ✅ **en los 4 perfiles**.
- Shield Charge lleva las etiquetas `Skill_Mobility`, `Skill_Juggernaut` y `Skill_Channeled` ✅ — lo que
  **valida** los tres razonamientos del informe: Moni se autoalimenta, Chastisement aplica, Channeling aplica.
- `MercenaryClass_ShieldBearer` = **Raheir**, `MercenaryClass_CursedChild` = **Aldkin** ✅.
  Bastion 90%/5 s ✅ · Inspiration 15%[x]/25%[x] ✅ · Raheir's Aegis 15% ✅ · Ground Slam 30%/60% ✅.
- Regla de dúo (Contratado a reserva, Refuerzo invocable) ✅ corroborada — aunque ver aviso abajo.
- 5 tableros con nombres, rotaciones, posiciones y glifos ✅ exactos. Tres glifos homónimos ✅.

### Citas del autor — todas literales
`rotations: []` en los 4 perfiles ✅ · `pinnedStats` exactamente
`{Shield Charge: [Damage], Fortress: [Cooldown]}` ✅ · `world: {renownSkills: 14, renownParagon: 42}` ✅ ·
*"Zoomy zommy"* / *"Short range"* ✅ · *"once every 6 seconds"* ✅ · *"maximize the amount of enemies you
hit"* ✅ (**está en el planificador**, la atribución [PLAN] es correcta) · *"14% at 15 skill ranks"* ✅ ·
*"42% at rank 15"* ✅ · orden de glifos *"Sentinel Spirit Honed Outmatch Revenge"* ✅ ·
*"Raheir grants you Bastion and Inspiration … Aldkin reduces enemy damage and slows with Field of Languish"* ✅

### Otras confirmaciones externas
- **Tibault's Will** fuera de tablas de jefe desde S13, en el fondo general, ruta fiable por Cubo ✅ corroborado.
- Receta *Upgrade to Mythic*: único 850+, **4 Fragmentos**, mítico **aleatorio del mismo hueco** ✅
  (el "mismo hueco" está en notas oficiales, como decía el informe).
- Maxroll runewords **fechada 16/07/2026** ✅ · Maxroll talismán **fechada 28/06/2026** ✅ ·
  tabla de sellos Mágico 3 / Raro 4 / Legendario 5 / Mítico 6 ✅ · receta *Reroll Set Charm* ✅.

---

## Controles obligatorios

### ✅ Contaminación PTR/beta: NEGATIVO
No hay contenido de PTR ni de beta presentado como parche vivo. El informe rechazó explícitamente la
página de wowhead marcada `2026/03/08` (anterior al lanzamiento del Paladín) y el hilo "Patch 3.2 PTR".

**He verificado el vector de contaminación más probable** y el informe lo esquivó: las cifras de PTR 3.1
que circulan (Shield Charge daño base 90→180, recarga 10→8, velocidad y armadura 40%→60%) aparecen en
artículos de PTR de icy-veins, mobalytics y d4gold, y **no están en el informe**. Correcto.

### ✅ Fuentes vetadas respaldando números: NEGATIVO
Ninguna de las vetadas (fextralife, primagames, beebom, gamespot, segmentnext, studioloot, gamerguides,
pcgamesn, mythicdrop) sostiene ningún número del informe.

**Mención especial:** el informe rechazó las cifras de terceros "157% daño, 10%/s Represalia hasta 50%"
por contradecir al cliente y venir de wiki vetada. **Decisión correcta y ahora demostrada**: wowhead
resuelve Relentless Charge a **108%** y *Phalanx Charge* a **158%** — la cifra de la wiki era de otra
mejora distinta.

### ⚠️ Aviso de calidad de fuente en [EXT]
Varias afirmaciones [EXT] descansan en sitios comerciales/SEO (apuesta de Óbolos con pantalones a 40,
encantos duplicados, fuentes de Fragmentos de Pandemónium). El informe avisa de todas ellas
("verifícalo en pantalla"), lo cual es correcto. Añado uno más: **la regla de mercenarios en grupo**,
que el informe da por confirmada, tiene mala cobertura en fuentes preferentes — la página de
mercenarios de Maxroll está **fechada 11/07/2025**, más de un año vieja, y **no describe el
comportamiento en grupo**. La regla se corrobora solo en fuentes secundarias sin fecha fiable.

### ✅ Nombres propios: todos anclados a cita literal
Cathan's Righteous Will, Cathan's Iron Conviction, Raheir, Aldkin, Sticker-thought, of Glynn's Anvil,
of the Indomitable, of the Juggernaut's Covenant, of Layered Wards, of Steel, Sentinel, Spirit,
Honed, Outmatch, Revenge, Moni, Igni, Cir, Yom, Kry, Ceh — **todos verificados** en `data.min.json`.

---

## Correcciones concretas que debe aplicar el informe

| # | Sección | Cambio |
|---|---|---|
| 1 | §7, §14, §15 | **Eliminar la regla del Mítico crafteado único.** Fue derogada en 3.1.1a (16/07/2026). El jugador puede craftear y equipar los tres. Reescribir el plan de farmeo. |
| 2 | §7 | Griswold's Opus: **1%[x] por enemigo, tope 50%[x]**. El 150 es Vida curada. Bajar su prioridad en §15. |
| 3 | §2, §3 | Clash genera **20 de Fe** (Faith Generation no está cogida). La mejora del "+10" es *Faith Generation*, no *Damage Bonus*. |
| 4 | §3 | El ×1,25 de Punishment lo da **Crusader's March Effectiveness**. Añadir el tercer punto: +20%[x] daño de Espinas. |
| 5 | §14 | Intermedia llega a **Resolve 27** (temples a +5), no a 30. Mover el hito a Endgame. |
| 6 | §11, §14, §15 | Hay **4 pasos** de Paragón, glifos hasta **150**. Shield Bearer a glifo 100 = **75**, no "—". |
| 7 | §0 | 3.1.3 **sí** tiene sección "Class Changes" (3 arreglos visuales, ninguno de Paladín). |
| 8 | No encontrado #1 | **Cerrar el hueco**: 3.1.1 y 3.1.2 están en la URL ya citada; **ningún cambio de Paladín**. Subir el coste 5→4 de [EXT] a oficial. |
| 9 | §7, §14, §15 | Separar el **encanto** Griswold's Opus de la **espada**. La ruta Duriel/Harbinger es del arma. Retirar "un jefe, dos objetivos". |
| 10 | §8 | Señalar que Maxroll describe **Yom** de otra forma ("restoring 100 Resource"). |
| 11 | §9 | Degradar a hipótesis la conclusión de las 3 piezas: la aritmética no distingue 3 de 5. |

---

## Fuentes de esta refutación

**Descargas primarias verificadas de forma independiente:**
1. https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide — HTTP 200, 477.063 bytes, `<time dateTime="2026-07-25">`
2. https://planners.maxroll.gg/profiles/d4/19imlp0x — HTTP 200, 167.015 bytes (parseado y decodificado por completo)
3. https://assets-ng.maxroll.gg/d4-tools/game/data.min.json — HTTP 200, 11.606.292 bytes, `version 3.1.0.72698` (**DATAMINING**)

**Páginas abiertas:**
4. https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes — oficial; **3.1.0, 3.1.1, 3.1.2 y 3.1.3**
5. https://www.icy-veins.com/d4/news/diablo-4-season-14-hotfix-crafted-mythic-restriction-removed-and-mythic-drop-rate-increased/ — **16/07/2026, 3.1.1a — clave de E1**
6. https://www.icy-veins.com/d4/news/diablo-4-3-1-3-patch-notes-easier-season-objectives-and-echo-of-mephisto-portal-fix/ — 12/08/2026
7. https://www.icy-veins.com/d4/news/diablo-4-season-14-patch-notes-increased-mythic-and-pandemonium-fragment-drop-rates/ — 3.1.1, 14/07/2026
8. https://www.icy-veins.com/d4/news/diablo-4-paladin-unique-items-boss-drop-locations/ — **sin fecha** (confirmado)
9. https://maxroll.gg/d4/resources/runewords-overview — fechada 16/07/2026
10. https://maxroll.gg/d4/resources/talisman-charms-sets — fechada 28/06/2026
11. https://maxroll.gg/d4/resources/mercenaries-overview — **fechada 11/07/2025, obsoleta**
12. https://www.wowhead.com/diablo-4/skill/shield-charge-2466077 — corroboración independiente de los textos

**Corroboración secundaria de E1:** https://us.forums.blizzard.com/en/d4/t/311a-patch-july-16-2026/263234 (oficial) ·
https://mobalytics.gg/diablo-4/guides/patch-3-1-1a-what-changed

**Vetadas:** ninguna usada. Aparecieron en resultados; no se ha tomado ni un número de ellas.
