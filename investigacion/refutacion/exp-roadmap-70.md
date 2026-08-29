# Refutación adversarial — `crudo/exp-roadmap-70.md`

**Verificador:** pasada independiente, 20/08/2026
**Objeto:** informe "Roadmap 70 → Tormento IV (y más allá)", Nigromante de esbirros, S14
**Método:** no se ha leído el informe como guía sino como acusación. Cada número de la lista de
afirmaciones se ha intentado romper con una fuente distinta de la que lo publicó. Cuando existía
vía directa al dato del juego, se ha descargado el fichero y se ha recalculado a mano.

**VEREDICTO: PARCIAL.**

La columna vertebral factual del informe **resiste**: la escalera de 12 Tormentos, los umbrales de
Foso, los bonos de XP y oro, los desbloqueos por escalón, el Paragón, los glifos, el Masterworking
y el reparto expansión/gratis se han verificado uno a uno y son correctos. Buena parte se ha
reproducido desde el fichero de datos crudo, no desde la guía que lo cita.

Lo que falla es un **racimo de errores de atribución de parche**, y ese racimo no es cosmético:
sostiene un consejo que el informe le da al jugador y que está **invertido**. Y hay un **error de
modelo** — exactamente el tipo que el encargo pedía cazar — en la tabla de tableros de Paragón.

---

## A. REFUTADO — fallo sistemático de atribución de parche

El informe cita tres veces `news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes` como
"notas del parche 3.1.3". **Esa URL no son las notas de 3.1.3: es una página acumulativa** que
apila, en orden inverso, 3.1.3 (build 73224, 12/08/2026), 3.1.2 (73020, 28/07), 3.1.1 (72836,
14/07) y 3.1.0 (72592, 30/06). El informe atribuyó a 3.1.3 tres cambios que no están en esa
sección.

Contenido **íntegro** de la sección 3.1.3 Build #73224 (12/08/2026), verificado: el objetivo de
Rango de Temporada III "Set Fire to the Beacons" cuenta Mazmorras de Pesadilla de Escalada con
afijo Ruptures; portal a la fase 3 de Echo of Mephisto para quien se une; reinvocar al Corrupted
Reaper limpia el cadáver anterior; y cuatro correcciones de bugs (Petrify/alas del Reaper,
habilidades de Sombra del Nigromante tapando al Reaper, Dark Prison del Brujo, teletransporte de
Planes de Guerra a Hordas Infernales). **Nada más.**

| # | Afirmación del informe | Realidad verificada | Dónde |
|---|---|---|---|
| **A1** | "Dominate Glyph: Reduced from 23.6% to 1.8% — Blizzard, notas **3.1.3**" | Está bajo **3.1.0 Build #72592, 30/06/2026**, sección Paragon de Base Game Balance Updates | [Blizzard, página acumulativa](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) · corroborado por [Icy Veins — PTR patch notes major nerfs](https://www.icy-veins.com/d4/news/diablo-4-ptr-patch-notes-reveal-major-nerfs-coming-for-top-builds/) y [Maxroll — 3.1.0 Patch Notes](https://maxroll.gg/d4/news/diablo-4-3-1-0-patch-notes) |
| **A2** | "Increased experience rewards in Torment 8 and up — 3.1.3" | Está bajo **3.1.0 Build #72592**, sección War Plans de Miscellaneous | misma URL |
| **A3** | "el parche **3.1.3** lo bajó a 4 [Fragmentos de Pandemónium]" | Está bajo **3.1.1 Build #72836, 14/07/2026**, en Bug Fixes de Season of Death Awakening | misma URL |

**El valor 4 de Fragmentos de Pandemónium sigue siendo correcto.** Lo que está mal es el parche —
y aquí la cronología corregida en realidad *refuerza* la conclusión: Maxroll publicó "5" el
13/07/2026 y Blizzard lo bajó a 4 el 14/07. La página quedó obsoleta al día siguiente.

### A4 — REFUTADO: el consejo sobre Dominate está invertido

Esta es la consecuencia grave. El informe escribe, en §3, en negrita:

> "La variante 'Mixta' de Maxroll arranca por el tablero Dominate, y esa página está fechada el
> 22/07/2026 — es decir, **ANTERIOR** al parche 3.1.3 del 12/08 que hundió el glifo.
> No sigas esa variante a ciegas."

El nerfeo es del **30/06/2026** (3.1.0). La guía de Maxroll es del **22/07/2026**. La página es
**POSTERIOR al nerfeo por tres semanas**, no anterior. Maxroll siguió recomendando Dominate
**sabiendo** que estaba nerfeado (verificado hoy: la guía sigue listando "Dominate, Mage, Essence,
Warrior, Abyssal" para la variante híbrida —
[Maxroll — Minion Necromancer](https://maxroll.gg/d4/build-guides/minion-necromancer-guide),
Last Updated: July 22, 2026).

El aviso puede seguir siendo prudente por otras razones, pero **la razón que da el informe es
falsa** y el jugador la leería como "esta guía no se ha enterado", cuando el hecho es lo contrario.

### A5 — REFUTADO: el aviso del §14 sobre el datamining es falso

El informe cierra con un aviso en negrita:

> "el fichero se refrescó el 18/08/2026, pero su versión interna dice 3.1.0 build 72698… sé de al
> menos dos casos donde **no** [están reflejados]: el nerfeo de Dominate (3.1.3) y la subida de XP
> de Tormento VIII+ (3.1.3)."

Tres cosas, todas comprobadas:

1. Ambos cambios son de **3.1.0**, no de 3.1.3 (ver A1, A2).
2. El build del parche 3.1.0 es **#72592**. El del fichero es **72698**. El fichero es
   **posterior** al parche, no anterior.
3. **Lo he recalculado desde el fichero.** El glifo Dominate del Nigromante
   (`Rare_035_Willpower_Side_Necro`, id 1331811) usa el afijo `OverpowerDamage_Willpower_Side`,
   que en el fichero trae `base = 1`, `perLevel = 0.005625`. A nivel de glifo 150:
   `1 + 0.005625 × 149 = 1.838` → **1,8%**. Es **exactamente el valor post-nerfeo** que publica
   Blizzard. El valor pre-nerfeo (23,6%) exigiría `perLevel ≈ 0.1517`.

**El fichero SÍ refleja el nerfeo.** El único aviso metodológico que el informe pone en negrita al
final —y que el lector usaría para descontar todos los números del datamining— está construido
sobre una premisa falsa.

---

## B. REFUTADO — error de modelo: no existen los tableros que el informe nombra

El encargo pedía verificar el marco, no solo los valores. Aquí hay uno.

El informe §3 presenta una tabla titulada **"Órdenes de tablero publicados para esbirros (S14)"**
con una columna **"Orden de tableros"**:

| Variante | "Orden de tableros" según el informe |
|---|---|
| Warrior | Warrior → Mage → Essence → Eliminator → Abyssal |
| Mage | Mage → Essence → Deadraiser → Eliminator → Abyssal |
| Mixta | Dominate → Mage → Essence → Warrior → Abyssal |

**Ninguno de esos tableros existe.** Los diez tableros de Paragón del Nigromante, leídos del propio
fichero (`classes[4].paragonBoards` → `paragonBoards[*].name`), se llaman:

> **Start · Cult Leader · Hulking Monstrosity · Flesh-eater · Scent of Death · Bone Graft ·
> Blood Begets Blood · Bloodbath · Wither · Frailty**

Warrior, Mage, Essence, Eliminator, Abyssal, Deadraiser y Dominate son **glifos**, los siete
aparecen en la lista de 23 glifos de Nigromante que el propio informe publica dos párrafos más
abajo. Lo que Maxroll lista son **prioridades de glifo**, no órdenes de tablero (verificado hoy:
la extracción de la página devuelve el encabezado "Paragon Board **Glyph** Priorities").

Consecuencias:

- La frase "La variante Mixta de Maxroll **arranca por el tablero Dominate**" describe un objeto
  inexistente.
- El informe rellena la columna "Prioridad de glifos" con **la misma secuencia** que la columna
  "Orden de tableros", presentando un solo dato como dos hechos distintos.
- Tablero y glifo son elecciones **separadas** (10 tableros contra 23 glifos, 1 ranura por
  tablero). Un jugador que siga la tabla buscará en pantalla cinco tableros que no están.
- Ironía útil: la lista de **Icy Veins** que el informe reproduce justo debajo (Frailty →
  Warrior, Cult Leader → Control, Flesh Eater → Amplify, Wither → Essence) **sí** empareja tablero
  real con glifo, y sus nombres de tablero coinciden uno a uno con el fichero. El modelo correcto
  estaba en la propia página del informe, al lado del incorrecto.

---

## C. REFUTADO — hecho menor sobre el propio método

**C1.** "No encontrado" #20: *"d4builds.gg — el dominio devolvió **HTTP 404**"*.
Comprobado hoy con UA de navegador y `-L`: **`https://d4builds.gg` → HTTP 200**;
`https://www.d4builds.gg` → HTTP 200. El dominio responde. El encargo pedía expresamente
intentar d4builds.gg; no se usó, y el motivo declarado no se sostiene.

*(Mobalytics sí: `https://mobalytics.gg/diablo-4/builds/minion-necromancer-endgame-build-guide`
→ **HTTP 403** confirmado. Ahí el informe es exacto.)*

---

## D. PARCIAL — sobreafirmaciones y conflictos no declarados

| # | Punto | Qué falla |
|---|---|---|
| **D1** | *"Umbrales de Foso… fichero de datos + Maxroll difficulty-overview, **dos vías independientes**"* | No son independientes. El "fichero de datos del juego" se sirve desde **`assets-ng.maxroll.gg`**: es infraestructura de Maxroll. Son datos crudos del cliente frente a prosa humana, lo cual vale, pero la **cadena de custodia es la misma organización**. Llamarlo "dos vías independientes" infla la garantía. (Los **valores** sí los he verificado y son correctos.) |
| **D2** | Freshness de las fuentes | El encargo exigía "nada anterior al parche 3.1.x". **3.1.0 salió el 30/06/2026.** Son anteriores: **difficulty-overview (26/06/2026)** — la fuente que sostiene toda la escalera de Tormentos; **masterworking-guide (23/05/2026)** — la única fuente de *todos* los números de Masterworking; **item-crafting (29/06/2026)**; **Icy Veins Naz Mages (27/06/2026)**. El informe las presenta como vigentes de S14 sin señalar que preceden al parche que inaugura la temporada. |
| **D3** | *"Rerodar el capstone: **10.000.000 de oro**"*, sin conflicto declarado | Tres cifras distintas en tres sitios: Maxroll → 10.000.000 de oro; [Icy Veins — Masterworking (S14)](https://www.icy-veins.com/d4/guides/masterworking-guide/) → **1.000 Obducita + 1 Neathiron + 1.000.000 de oro**; agregadores → 200 Obducita + 1 Neathiron + 10M. Además el informe **omite los componentes de Obducita y Neathiron**, que es justo lo que el jugador necesita para planificar el gasto. Conflicto real, no declarado. |
| **D4** | *"Ancestrales **priorizando armas**"* como cita de la fase inicial | La página dice dos cosas distintas: *"Ancestral Weapons provide a huge spike in power"* (observación) y *"Prioritize Weapons since their base damage goes up with each Quality rank"* — esto último referido al **Masterworking**, no a la recolección de Ancestrales. El informe funde ambas en una instrucción que la fuente no da con esas palabras. |
| **D5** | Totales del Rango de Temporada según Maxroll: *"14 habilidad, 42 Paragón, 9 Chispas, **3 alijos Míticos**"* | En mi lectura de la misma página el total declarado de alijos Míticos es **2**, mientras el desglose rango a rango suma **5**. El "3" no es reproducible. Además el desglose de Paragón del informe (6+12+10+8 = **36**) **omite el Rango 9**, que en mi extracción da **7 puntos** más. Ninguna combinación cuadra limpiamente con 42: la página es internamente inconsistente y el informe la cita como si no lo fuera. |
| **D6** | *"0% cuando el Foso está **50+** niveles por debajo"* | La página lee **"51+ levels lower"**. Desviación de uno, en un dato ya marcado como parcialmente extraído. |
| **D7** | *"Lord of Hatred (**28/04/2026**)"* atribuido a la página de Blizzard | El texto literal de esa página es *"Lord of Hatred begins rollout on **April 27 at 4:00 p.m. PDT**"*. El 28/04 es defendible por huso horario y lo corroboran terceros, pero **no es lo que dice la fuente citada**. |
| **D8** | Cita de la restricción SSF | El informe atribuye *"Free Trial, Couch Co-Op, and Dark Citadel are unavailable for SSF characters"* a la página de Maxroll sobre la Ciudadela Oscura que **él mismo fecha en abril de 2025 (S8)** — imposible, SSF es un sistema de S14. La **conclusión es correcta y de hecho más fuerte** de lo que el informe dice: Blizzard, en el blog de S14 que el informe ya tenía abierto, escribe *"SSF characters **cannot join parties or trade** with other players"*. Fuente primaria disponible, sin usar, en favor de una cita imposible. |
| **D9** | Trampa de datos muertos no catalogada | El informe lista las fuentes contaminadas que detectó, pero se le escapa una relevante: **Wowhead** publica el marco muerto en su guía de dificultad (*"Beating Pit Tier 20 unlocks Torment Tier I… Pit Tier 35 unlocks Torment II… 50… 65"*, y *"Reaching Level 60 unlocks the Pit"*) — el modelo de Vessel of Hatred / nivel 60. El encargo pedía intentar wowhead.com/diablo-4 como fuente preferente; para umbrales **no lo es**. |

---

## E. CONFIRMADO — lo que resistió el intento de romperlo

Esto no es relleno: es la parte del informe que el jugador puede usar sin reservas. Todo lo de
abajo se ha verificado con una vía distinta a la que el informe usó, o recalculado desde el dato
crudo.

**Verificado directamente contra el fichero de datos** (descargado hoy 20/08/2026;
`content-length: 11606376`, `last-modified: Tue, 18 Aug 2026 15:42:02 GMT`, `version: 3.1.0.72698`
— los tres coinciden con lo que declara el informe):

- **Las 16 dificultades y los 12 Tormentos**, con requisito literal, XP, oro y desbloqueos.
  La tabla del informe es **exacta, entrada por entrada**: T1=Foso 10 · T2=15 · T3=20 · T4=25 ·
  T5=30 · T6=40 · T7=50 · T8=60 · T9=70 · T10=80 · T11=90 · T12=100; XP +300% → +1400%; oro
  +100% → +300%; y los desbloqueos (Ancestrales, Manuales de Temple Legendarios + Pergaminos de
  Restauración, Set Charms, Neathiron, Runas Legendarias, Greater Lair Keys, Polvo Primordial
  Volátil, Unique Charms, Kullean Tuning Prisms, Mythic Horadric Seals).
- **Texto literal de Tormento I**: `"Unlock Artificer's Tier and Conquer Tier 10 on this character"`. Exacto.
- **Escalones bajos**: Duro +75%/+25%, Experto +125%/+50%, Penitente +175%/+75%. Exacto.
  *(Nota: mi extracción de la página de Maxroll devolvió aquí cifras incoherentes —Experto por
  debajo de Duro—; el fichero es consistente y le da la razón al informe. No hay conflicto real.)*
- **"For paragons and fools"** existe, y es el campo `recommended` de Tormento XI y XII. Exacto.
- **23 glifos de Nigromante** con `classFilter[4] == true`. Recuento exacto, y los 23 nombres
  coinciden con la lista del informe.
- **10 tableros de Paragón** (`Paragon_Necro_00`…`_08`, `_10`). Exacto.
- **7 árboles de Planes de Guerra**: Tree of Whispers, Nightmare Dungeons, Helltide, The Undercity,
  Lair Bosses, Infernal Hordes, The Pit. Exacto.
- **`damageScalar: 1.25`** para Nigromante. Exacto.
- **Derivación del bono legendario de glifo**: `MultDmgPercentAll_Legendary` trae `base = 0.005`,
  `perLevel = 0.001`. Recalculado: nivel 51 → **5,500%**; nivel 150 → **15,400%**. Reproduce los
  dos puntos de Maxroll al decimal. La derivación del informe es correcta y está bien etiquetada
  como derivación.
- **Sin campo de radio** en `paragonGlyphs` (los registros solo tienen `affixes`, `classFilter`,
  `icon`, `id`, `name`, `rarity`). El informe tiene razón: el dato no está ahí.
- *Extra que el informe declaró no haber podido cotejar:* el glifo **Essence**
  (`MultCritDmgPercent_Legendary`, `base = 0.02825`, `perLevel = 0.00115`) da **8,575% en nivel 51**
  y **19,96% en nivel 150**.

**Verificado contra Blizzard:**

- **Nivel 70 gratis para todos.** La página trae una tabla comparativa explícita:
  *"Lord of Hatred Expansion / Requires Lord of Hatred Purchase"* frente a *"Permanent Updates /
  Available across full game regardless of realm or expansion ownership"*. **"Level Cap increase to
  70"** y **"Added Torment Tiers"** están en la columna gratuita. Confirmado.
- **"Torment levels expand from 4 to 12"**, literal. Confirmado.
- **Planes de Guerra, Cubo Horádrico y Talismán son de pago.** Aparecen en la columna
  *Requires Lord of Hatred Purchase*, junto a campaña, Brujo, Paladín, Skovos, Echoing Hatred y
  Fishing. **La afirmación con más consecuencias del informe para el caso de la pareja está bien.**
  Corroborado por terceros.
- **Totales de S14**: "Up to 12 Skill Points", "Up to 42 Paragon points", "Up to 7 Resplendent
  Sparks", "5 Mythic Unique Caches", "nine ranks", "over 120 objectives", sincronización de Planes
  de Guerra por **2 Marks of El'Druin** con aceptación unánime. Todo exacto.
- La discrepancia Blizzard-vs-Maxroll en Chispas y puntos de habilidad **existe y está bien
  declarada** por el informe.
- Las notas 3.0 efectivamente **no** contienen los cambios de sistema (solo builds 3.0.1–3.0.4).

**Verificado contra Maxroll e Icy Veins:**

- Foso: **150 niveles**, **15 minutos**, apertura por **Hellish Descent rango II** en temporada y
  por **nivel 70** en Eterno, **4** intentos base de glifo **+1** sin morir, **"Up to 4 extra from
  nodes in the Pit Skill Tree from War Plans"** → los 9 del informe. Todo literal.
- Paragón: **1–300**, **342 puntos**, **5 tableros** incluido el inicial, **4 puertas**, **1 ranura
  de glifo**. Todo literal.
- Glifos: **máximo 150**, **15.000 fragmentos de gema** al llegar a nivel 50 para pasar a
  Legendaria. Literal.
- Masterworking: **rango 25**, **+1% por rango** a daño base/armadura/resistencia y afijos,
  **capstone +50% a un afijo aleatorio en el 25**, `floor(3.75 × CurrentQuality + 10)`,
  **10 → 100**, total **492–1.366**. Todo literal (con la salvedad D2 sobre la fecha y D3 sobre el
  rerodado).
- Orden de gasto: *"don't bother with Masterworking yet"*, *"Level relevant Glyphs to level 25"*,
  *"until about Paragon level ~100"*, *"Masterwork the rest of your items to 25 Quality"*,
  *"Get your main Glyph(s) to 51 for the Legendary Bonus"*, *"Keep farming the Pit to upgrade your
  glyphs beyond level 51"*, y la regla de ritmo *"It is often more efficient to farm in a lower
  Torment difficulty…"*. Todo literal. También *"Use the Horadric Cube to upgrade Rare items into
  Legendary"* y *"use on 750 item power gear"*.
- Defensas: `DR% from Armor = Armor / (Armor*10/9 + Constant)`, **5678** a nivel 70, **1136** de
  resistencias, techo asintótico **90%**, sistema de *rating* **sin topes por dificultad desde la
  Temporada 11**, y la Dureza declarada **"not real"** como métrica única. Todo literal, página del
  **16/08/2026** — la más fresca del informe. **La demolición del "9.230 de armadura" es correcta.**
- Objetivos de la build: **100% velocidad de ataque** ("number one priority"), **100% crítico**,
  **30k de vida**, **40+ Resolve** en la variante híbrida. Literal, página del 22/07/2026.
- **Runewords solo con Vessel of Hatred**, literal en Icy Veins.
- **El conflicto del radio de glifo es real** y el informe lo declara con honradez. Icy Veins
  sostiene radio 4 en **15**, radio 5 en **50**, Legendaria en **51**, y **3** intentos base — tal
  cual lo describe el informe. La búsqueda amplia se inclina por el modelo 25/51 de Maxroll, pero
  no lo cierra. **El consejo de mirar el tooltip en pantalla es la respuesta correcta.**
- Los huecos de "No encontrado" #4, #5, #6, #7, #14 y #17 se han vuelto a intentar y **siguen
  siendo huecos**. Bien declarados.

---

## F. Resumen ejecutivo para el redactor

**Lo que hay que corregir sí o sí antes de publicar:**

1. **§3, aviso de Dominate** — invertir el argumento. El nerfeo es del 30/06 (3.1.0); la guía de
   Maxroll del 22/07 es posterior y recomienda el glifo con conocimiento de causa.
2. **§14, aviso del datamining** — retirarlo o reescribirlo. El fichero (build 72698) es posterior
   al parche 3.1.0 (build 72592) y **contiene el valor post-nerfeo** (1,838% recalculado a mano).
3. **§3, tabla "Órdenes de tablero"** — es una lista de **glifos**, no de tableros. Los tableros
   del Nigromante son Start, Cult Leader, Hulking Monstrosity, Flesh-eater, Scent of Death, Bone
   Graft, Blood Begets Blood, Bloodbath, Wither y Frailty.
4. **§5 y §8** — reetiquetar los tres cambios: Dominate y XP de T8+ son **3.1.0**; Fragmentos de
   Pandemónium 5→4 es **3.1.1**. Y decir que la URL de Blizzard es una página acumulativa.
5. **§8** — declarar el conflicto del coste de rerodar el capstone y añadir los componentes de
   Obducita y Neathiron que faltan.
6. **"No encontrado" #20** — d4builds.gg responde 200. O se usa, o se dice otra cosa.
7. **§12** — sustituir la cita imposible sobre SSF por la de Blizzard, que además es más rotunda.
8. **Fechas** — marcar que difficulty-overview, masterworking-guide, item-crafting y la guía de
   Icy Veins de Naz Mages son **anteriores a 3.1.0**.
9. **§0** — añadir Wowhead a la tabla de trampas de datos muertos para umbrales de Tormento.

**Lo que NO hay que tocar:** toda la §5 (valores), §4 (salvo D6), §6, §9 (salvo D5), §1 y §12
(reparto expansión/gratis), y la derivación del bono de glifo. Se ha intentado romper y no se ha
podido.

---

## Fuentes de esta refutación

1. https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes — página **acumulativa** 3.1.0/3.1.1/3.1.2/3.1.3; ubicación real de los tres cambios mal atribuidos
2. https://news.blizzard.com/en-us/article/24267729/prepare-for-the-reckoning-lord-of-hatred-draws-near — tabla comparativa expansión vs. permanente; fecha literal de despliegue
3. https://news.blizzard.com/en-us/article/24271857/diablo-iv-patch-notes-3-0 — builds 3.0.1–3.0.4; sin cambios de sistema
4. https://www.wowhead.com/diablo-4/blue-tracker/news/eu/hunt-the-death-cult-in-season-of-death-awakening-diablo-iv-blizzard-news-24268702 — totales de S14, sincronización de Planes de Guerra, restricción SSF literal
5. https://assets-ng.maxroll.gg/d4-tools/game/data.min.json — **datamining**, descargado 20/08/2026; `worldTiers`, `paragonGlyphs`, `paragonGlyphAffixes`, `paragonBoards`, `classes`, `warPlans` inspeccionados y recalculados
6. https://maxroll.gg/d4/resources/difficulty-overview — 26/06/2026 (**anterior a 3.1.0**)
7. https://maxroll.gg/d4/resources/pit-guide — 16/07/2026
8. https://maxroll.gg/d4/resources/paragon-boards — 09/07/2026
9. https://maxroll.gg/d4/resources/masterworking-guide — 23/05/2026 (**anterior a 3.1.0**)
10. https://maxroll.gg/d4/meta/endgame-progression — 09/07/2026
11. https://maxroll.gg/d4/resources/season-journey — 13/07/2026 (totales internamente inconsistentes)
12. https://maxroll.gg/d4/build-guides/minion-necromancer-guide — 22/07/2026; **posterior** al nerfeo de Dominate y aun así lo recomienda
13. https://maxroll.gg/d4/getting-started/defenses-for-beginners — 16/08/2026
14. https://www.icy-veins.com/d4/guides/paragon-glyph-guide/ — S14; sostiene el modelo de radio 15/50 y 3 intentos
15. https://www.icy-veins.com/d4/guides/masterworking-guide/ — S14; **coste de rerodado distinto** al de Maxroll
16. https://www.icy-veins.com/d4/guides/runewords-guide/ — S14; Runewords exclusivas de Vessel of Hatred
17. https://www.icy-veins.com/d4/news/diablo-4-ptr-patch-notes-reveal-major-nerfs-coming-for-top-builds/ — Dominate en 3.1.0
18. https://maxroll.gg/d4/news/diablo-4-3-1-0-patch-notes — Dominate en 3.1.0
19. https://www.wowhead.com/diablo-4/guide/gameplay/difficulty-torment-levels — **fuente contaminada**: publica el marco muerto Foso 20/35/50/65
20. https://d4builds.gg — **HTTP 200** (contra el 404 declarado en el informe)
21. https://mobalytics.gg/diablo-4/builds/minion-necromancer-endgame-build-guide — **HTTP 403** confirmado
