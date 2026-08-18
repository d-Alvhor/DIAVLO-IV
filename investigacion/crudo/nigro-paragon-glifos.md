# Paragon y Glifos del Nigromante — Diablo IV Season 14 (parche 3.1.x)

**Fecha de la investigación:** 18 de agosto de 2026
**Temporada vigente:** Season 14 "Death Awakening" (parche 3.1.0, 30/06/2026; parche vivo 3.1.3, build 73224, 12/08/2026)
**Perfil del jugador:** principiante absoluto, Nigromante (Necromancer), **SOLO JUEGO BASE** (sin Vessel of Hatred, sin Lord of Hatred), en dúo cross-play PC + consola, objetivo min-max.

> **Leyenda de disponibilidad**
> ✅ = funciona con el **juego base**, sin comprar nada.
> 🔒 = **requiere expansión** (se indica cuál).

---

## 0. Resumen de un vistazo (lo que hay que retener)

| Concepto | Valor en S14 | ¿Base o expansión? |
|---|---|---|
| Nivel máximo de personaje | **70** | ✅ Base |
| Paragon se desbloquea al | **nivel 70** | ✅ Base |
| Niveles de Paragon | **300** | ✅ Base |
| Puntos de Paragon totales | **342** (300 por niveles + 42 del Rango de Temporada / Season Rank) | ✅ Base (los 42 solo en personaje de temporada) |
| Tableros equipables | **5** = tablero inicial + **4** acoplados | ✅ Base |
| Tableros disponibles por clase | 9 opciones (ver contradicción §14) | ✅ Base |
| Glifos: nivel máximo | **150** | ✅ Base |
| Glifos: radio | 3 → **4 al nivel 15** → **5 al nivel 50** | ✅ Base |
| Glifo Raro → Legendario | **nivel 51** (bonus multiplicativo extra) | ✅ Base |
| Dónde se suben los glifos | **exclusivamente en el Foso del Artífice (The Pit of the Artificers)**, tiers 1–150 | ✅ Base |
| Intentos de mejora por run del Pit | **3**, +1 si acabas sin morir (**4** en total) | ✅ Base |

**El titular para vosotros dos:** *todo* el sistema Paragon —tableros, glifos, el Pit, los 300 niveles, los 42 puntos del Season Rank— es **✅ juego base**. No hay ni un tablero ni un glifo detrás de un muro de pago. Lo que sí está detrás de muro de pago son *aceleradores* externos (Mercenarios, Runewords) y clases (Spiritborn, Warlock). Ver §12.

---

## 1. Marco general: cómo funciona el Paragon en S14

En Season 14 el techo de nivel es **70** y el Paragon se abre justo al llegar ahí; a partir de ese punto toda la experiencia alimenta el Paragon en lugar del nivel (Icy Veins, Maxroll, Skycoach). Esto es un cambio respecto a la era post-*Vessel of Hatred* / Season 6, donde el techo era 60 (así lo sigue documentando Game8, que está desactualizado — ver §14).

- **300 niveles de Paragon = 300 puntos.** 1 punto por nivel.
- **+42 puntos adicionales** del **Rango de Temporada (Season Rank)**, solo para el personaje de temporada. Total **342**.
- Cada punto se gasta en un nodo del tablero. **Los puntos son finitos**: a 342 puntos y con 5 tableros de 70–180 nodos cada uno, **no podéis coger ni de lejos todos los nodos**. El min-max del Paragon es esencialmente un problema de ruta: cada nodo común que cogéis "de paso" es un multiplicador que no cogéis.

### Regla de oro del pathing (fuente: Maxroll)
> "No te desvíes. Casi nunca hay valor en salirte de tu ruta elegida para coger nodos comunes."

Los nodos comunes solo se cogen **como peaje** para llegar a un nodo raro, a una puerta de acoplamiento o a un socket de glifo — o **como munición de atributo** dentro del radio de un glifo (esto último sí es intencional y clave, ver §5).

---

## 2. Anatomía de un tablero: tipos de nodo

| Tipo de nodo | Color | Qué da | Valor de atributo |
|---|---|---|---|
| **Normal / Común** | Gris | Un atributo principal | **+5** a un atributo |
| **Mágico** | Azul | Un stat ofensivo/defensivo/utilidad, o atributo mejorado | **+7** a un atributo (cuando da atributo) |
| **Raro** | Amarillo | **2 bonus** + un **3.º bonus condicionado** a un umbral de atributo | **+10** a un atributo |
| **Legendario** | Naranja | Efecto potente y específico de clase/arquetipo. **1 por tablero** (el tablero inicial no tiene) | — |
| **Puerta de acoplamiento** (Board Attachment Gate) | — | Conecta con el siguiente tablero | **+5 a los cuatro atributos** |
| **Socket de glifo** | — | Aloja un glifo. **1 por tablero** | — |

**Rotación:** cada tablero tiene 4 puntos de conexión y **se puede rotar en incrementos de 90°**. Esto es min-max puro: la rotación correcta ahorra literalmente decenas de puntos de Paragon porque acorta la ruta hasta el nodo legendario y hasta el socket. ✅ Base.

### El tablero inicial del Nigromante (Necromancer Basic Board) ✅ Base
Datos exactos (fuente Game8):

- **Puerta de acoplamiento:** +5 Fuerza, +5 Inteligencia, +5 Voluntad, +5 Destreza.
- **Nodos raros (4):**

| Nodo raro | Bonus |
|---|---|
| **Knowledge** (Conocimiento) | +10% Daño; +10 Inteligencia |
| **Preservation** (Preservación) | +100 Armadura; +10 Inteligencia |
| **Prime** | +10% Daño; +4% Vida |
| **Resilience** (Resiliencia) | 4% Resistencia a Todos los Elementos; +4% Vida |

- **Nodos mágicos (18):** 5× +5% Daño · 4× +2% Vida · 3× +50 Armadura · 2× +7 Voluntad · 2× +7 Destreza · 2× 2% Res. Todos los Elementos.
- **Nodos normales (34):** repartidos entre Inteligencia, Voluntad, Destreza y Fuerza.
- **1 socket de glifo.**

Ese socket inicial es el que casi todas las guías rellenan con **Mage** (Mago) o con el glifo principal de daño de la build.

---

## 3. Nodos raros y requisitos de atributo (lo que casi nadie explica bien)

Los nodos raros tienen dos bonus garantizados y **un tercero bloqueado detrás de un umbral de atributo**. Tres detalles críticos:

1. **El umbral se mide contra el atributo TOTAL del personaje**, no solo contra lo que hayáis gastado en el tablero (fuente: Game8). Es decir, el equipo, los Aspectos y las gemas también cuentan. Esto significa que un nodo raro que hoy parece "muerto" puede activarse solo con cambiar de amuleto.
2. **El umbral sube con cada tablero que acopláis** (fuente: Maxroll). Los primeros tableros tienen requisitos baratos; el cuarto tablero acoplado pide bastante más. Corolario min-max: **si tenéis dudas sobre el orden, poned pronto los tableros cuyos nodos raros queréis activar barato**.
3. Los nodos raros son la fuente **más densa de atributo (+10)**, así que sirven doble propósito: su propio bonus **y** alimentar el requisito de atributo del glifo que tengan en radio.

> Consejo de Maxroll, literal en espíritu: cuando busques cumplir el requisito de un glifo, **mira primero los nodos raros dentro del radio del socket** que ya querías coger igualmente, y comprueba si su atributo es el que necesitas. Rare = +10, Mágico = +7, Común = +5.

---

## 4. Los tableros del Nigromante y sus nodos legendarios ✅ Base

Lista de tableros del Nigromante con el texto del nodo legendario (fuentes: Fextralife, Game8). **Ninguno requiere expansión.**

| Tablero | Nodo legendario — efecto | Arquetipo al que sirve |
|---|---|---|
| **Cult Leader** (Líder de Culto) | Ver contradicción §14. Versión A (Fextralife): "Tus Esbirros infligen 40% más daño por cada 20% de Bonus de Velocidad de Ataque que tengan, hasta un máximo de 100% de Velocidad de Ataque". Versión B (Game8): "Tus Esbirros infligen 15% más daño por cada tipo de Esbirro que tengas activo (Guerrero Esquelético, Mago Esquelético, Gólem)" | **Esbirros / Minion** |
| **Hulking Monstrosity** (Monstruosidad Descomunal) | "Tu Gólem tiene 30% más Vida Máxima e inflige 30% más daño" | Gólem / Minion |
| **Flesh-eater** (Devorador de Carne) | "Consumir 5 Cadáveres otorga 40% más daño durante 6 segundos" | Cualquiera que consuma cadáveres |
| **Scent of Death** (Olor a Muerte) | "Con al menos 2 Cadáveres cerca ganas 15% de Reducción de Daño. Sin Cadáveres cerca, infliges 15% más daño" | Híbrido |
| **Bone Graft** (Injerto Óseo) | "Golpear enemigos con habilidades de Hueso aumenta tu daño 1% y tu Esencia Máxima 3 durante 8 s, acumulable hasta 8% de daño y 24 de Esencia Máxima" | **Hueso** (Bone Spear, Bone Spirit) |
| **Blood Begets Blood** (La Sangre Engendra Sangre) | "Los Orbes de Sangre otorgan 10% más daño, hasta 50%, durante 5 s" | **Sangre** (Blood Surge, Blood Wave) |
| **Bloodbath** (Baño de Sangre) | "Los ataques con Sobrepoder garantizado infligen 50% más daño de Sobrepoder" | **Overpower** (Blood Wave, Blood Surge) |
| **Wither** (Marchitar) | "Tus efectos de daño de Sombra en el tiempo tienen 5% de probabilidad de infligir 50% de daño extra cada vez que dañan. Esta probabilidad aumenta 1% y el daño extra 25% por cada 50 de Voluntad que tengas" | **Sombra / DoT** (Shadowblight, Sever) |
| **Frailty** (Fragilidad) | "Los enemigos Malditos reciben 10% más daño de ti y tus Esbirros. Este bonus aumenta 10% cada segundo que estén Malditos, hasta 40%" | **Maldiciones** (Decrepify, Iron Maiden) |

**Nota de parche 3.1.0:** *Bone Graft* aparece en las notas con "daño de Hueso aumentado de 40% a 60%" — pero esa mención corresponde probablemente a la **habilidad pasiva** homónima, no al nodo legendario del tablero. Marcado como incertidumbre (§14).

### Frailty en detalle (tablero muy usado en S14) ✅ Base
Nodos raros exactos (Game8):

| Nodo raro | Bonus |
|---|---|
| Calculated | +15% Daño a Enemigos con Control de Masas; +20 Armadura |
| Eradicate | +10% Daño Vulnerable; +10 Inteligencia |
| Lingering Shadows | +10% Daño de Sombra en el Tiempo; +10% Daño de Sombra |
| Preservation | +20 Armadura; +10 Inteligencia |
| Relentless | +2,5% Velocidad de Ataque; +4% Vida Máxima |
| Shadow Resilience | +10% Resistencia a Sombra; +4% Vida Máxima |

Nodos mágicos (3 de cada): +5% Daño Vulnerable · +5% Res. Sombra · +7,5% Daño a enemigos con CC · +1,3% Vel. Ataque · +5% Daño de Sombra en el Tiempo (×2 entradas). 1 socket de glifo.

### Cult Leader en detalle (el tablero de esbirros) ✅ Base
Nodos raros exactos (Game8):

| Nodo raro | Bonus |
|---|---|
| Armor-clad | +8% Armadura de Esbirros; 10% Vida Máxima de Esbirros |
| Custody | 10% Reducción de Daño para tus Esbirros; +10 Inteligencia |
| Infused Caster | +25% Daño de Mago Esquelético; 16% Res. Todos los Elementos de Esbirros |
| Infused Warrior | +25% Daño de Guerrero Esquelético; +14% Armadura de Guerrero Esquelético |
| Overlord | +10% Daño de Esbirros; +10 Inteligencia |
| Puppeteer | +10% Daño de Esbirros; +5% Velocidad de Ataque de Esbirros |

20 nodos mágicos orientados a esbirros + 1 socket de glifo. Fijaos en que **Custody y Overlord dan +10 Inteligencia**: son la munición perfecta para cumplir requisitos de glifos de Inteligencia (Control, Amplify, Mage).

---

## 5. Orden de desbloqueo de tableros — recomendaciones S14

**Aviso metodológico importante:** muchas guías (Maxroll en particular) publican el **orden de subida de glifos** y es fácil confundirlo con el orden de tableros, porque comparten nombre en algunos casos (*Essence*, *Dominate*, *Amplify* son glifos, no tableros). Las únicas fuentes que dan explícitamente el **orden de tableros** para S14 son las guías de Icy Veins.

### Orden confirmado en Icy Veins para builds de esbirros S14

**Naz Mages / Mendeln Summoner (Nigromante de magos esqueléticos):**

| # | Tablero | Glifo en el socket |
|---|---|---|
| 1 | **Tablero inicial** | **Mage** (Mago) |
| 2 | **Frailty** | **Warrior** (Guerrero) |
| 3 | **Cult Leader** | **Control** |
| 4 | **Flesh-eater** | **Amplify** (Amplificar) |
| 5 | **Wither** | **Essence** (Esencia) |

**Reaper Summoner / Shadowblight (invocador de Sombra):**

| # | Tablero | Glifo en el socket |
|---|---|---|
| 1 | **Tablero inicial** | **Mage** |
| 2 | **Frailty** | **Warrior** |
| 3 | **Cult Leader** | **Essence** |
| 4 | **Flesh-eater** | **Amplify** |
| 5 | **Wither** | **Deadraiser** |

Ambas guías dan la misma instrucción de pathing:
- **Saltarse de entrada los clústeres de Resistencia** de cada tablero y volver a por ellos más tarde, cuando os sobren puntos.
- **Rellenar nodos de Inteligencia alrededor de los glifos** (Mage, Control) porque esos glifos escalan con Inteligencia en radio.
- La guía Reaper menciona además **nodos de Destreza cerca de Essence y Warrior**, e **Inteligencia alrededor de Eliminator**.
- Al llegar a **Paragon 300**, "intercambiar glifos y posiciones" si hace falta: el reparto óptimo a 342 puntos no es el mismo que a 150.

### Orientación por arquetipo (deducida de los nodos legendarios, no citada literalmente)
- **Hueso (Bone Spear / Bone Spirit):** Bone Graft es el tablero de firma. Scent of Death y Flesh-eater aportan si consumís cadáveres.
- **Sangre / Overpower (Blood Wave, Blood Surge):** Bloodbath + Blood Begets Blood.
- **Sombra / DoT (Sever, Shadowblight):** Wither es obligatorio; Frailty si lleváis maldiciones.
- **Esbirros:** Cult Leader + Hulking Monstrosity (si usáis Gólem) + Frailty.

---

## 6. Glifos: la mecánica exacta

### Rareza
- Tras el parche 2.0 (*Vessel of Hatred*) **los glifos Mágicos fueron eliminados**. Hoy solo hay **Raros** y **Legendarios**. ✅ Base.
- Un glifo Raro **se convierte en Legendario al subir de nivel** (nivel 51 según Icy Veins S14), lo que añade **un bonus multiplicativo extra** y sube el radio.

### Radio y breakpoints (versión mayoritaria S14)

| Nivel de glifo | Radio | Qué desbloquea |
|---|---|---|
| 1–14 | **3** | Efecto base |
| **15** | **4** | Primer salto de radio |
| **50** | **5** | Segundo salto de radio |
| **51** | 5 | **Raro → Legendario**: bonus multiplicativo secundario |
| 51–150 | 5 | Escalado continuo del efecto |
| **150** | 5 | Tope de S14 |

Fuentes que coinciden en 15 / 50 / 150: **Icy Veins (guía de glifos S14)** y **Skycoach (S14)** — que da el rango literal "Niveles 1–14: radio 3; 15–49: radio 4; 50–150: radio 5". **Maxroll dice 25 y 51**, y **Fextralife dice 15 y 45/46 con tope 100**. Ver §14: es la contradicción más gorda de esta investigación.

**Regla práctica que las guías de build repiten sin excepción:**
> "Es imperativo subir todos los glifos a nivel 25 primero para aumentar su radio de activación, y después a 51 para desbloquear el multiplicador de daño secundario." *(Icy Veins, guías de build S14)*

Y para builds concretas hay glifos que directamente **no se activan** hasta cierto nivel: la guía de **Sever** dice literalmente que *Essence* y *Abyssal* **"requieren subirlos a 50 y aumentar el Radio antes de poder activarse"** — hay que subirlos a 50 **antes que nada**. La guía de **Blood Wave** dice lo mismo de *Essence*.

### Requisito de atributo del glifo
Cada glifo tiene dos capas:
1. **Escalado continuo:** "por cada 5 [Atributo] comprado dentro del radio, ganas X%".
2. **Bonus adicional bloqueado:** requiere alcanzar un umbral de ese atributo dentro del radio (típicamente **40**) para activar un multiplicativo.

Ejemplo exacto (Fextralife, glifo **Control**):
- Efecto: *"Por cada 5 de Inteligencia comprada dentro del rango, infliges +2,0% más daño a objetivos con Control de Masas."*
- Requisito: **+40 Inteligencia** comprada dentro del radio.
- Bonus adicional: *"Tú y tus Esbirros infligís 20%[x] más daño a enemigos con Control de Masas."*
- Bonus legendario: multiplicativo extra al daño a objetivos con CC (desbloqueado al convertirse en Legendario).

Ejemplo exacto (Fextralife, glifo **Dominate**):
- Efecto: *"Por cada 5 de Voluntad comprada dentro del rango, infliges +3,0% más daño de Sobrepoder."*
- Bonus adicional: *"Cuando Sobrepoderas a un enemigo, todo el daño que reciba de ti y tus Esbirros aumenta un 12%[x] durante 5 segundos."*

**Implicación min-max:** el multiplicativo del bonus adicional es **muchísimo** más valioso que el escalado lineal. Prioridad absoluta: (a) cumplir los 40 de atributo dentro del radio, (b) subir el glifo a 50/51 para radio 5 + legendario, (c) ya luego rellenar atributo para el escalado lineal.

---

## 7. Catálogo de glifos del Nigromante ✅ Base

Pool de glifos Raros del Nigromante (fuente PureDiablo vía búsqueda; los nombres coinciden con los citados por Maxroll e Icy Veins en sus builds S14):

**Abyssal · Amplify · Blood-Drinker · Control · Corporeal · Darkness · Deadraiser · Desecration · Dominate · Eliminator · Essence · Exhumation · Exploit · Golem · Gravekeeper · Imbiber · Mage · Revenge · Sacrificial · Scourge · Territorial · Undaunted · Warrior**

Detalle de los que sí he podido verificar en fuente:

| Glifo | Atributo que escala | Efecto / bonus | Verificado |
|---|---|---|---|
| **Control** | Inteligencia | +2,0% daño a objetivos con CC por cada 5 INT; a 40 INT: **20%[x]** para ti y tus esbirros contra enemigos con CC | Sí (Fextralife) |
| **Dominate** | Voluntad | +3,0% daño de Sobrepoder por cada 5 WIL; bonus: al Sobrepoderar, el enemigo recibe **12%[x]** más daño 5 s | Sí (Fextralife) |
| **Amplify** | Inteligencia | Potencia los nodos **Mágicos** en radio; a 40 INT: enemigos afectados por Maldiciones reciben 10% más daño | Parcial — texto posiblemente pre-2.0 (§14) |
| **Corporeal** | — | Tú y tus Esbirros infligís **10%[x]** más daño Físico; +1% Velocidad de Movimiento por Esbirro activo | Parcial |
| **Deadraiser** | Voluntad | Potencia nodos de daño de Esbirros y de Reducción de Daño en radio, por cada 5 WIL | Parcial |
| **Eliminator** | Inteligencia (según Icy Veins) | Potencia los nodos **Normales** en radio; + daño contra Élites | Parcial |
| Essence, Warrior, Mage, Exploit, Gravekeeper, Imbiber, Abyssal | — | Existen y se usan; **no he podido verificar sus textos exactos** | **No** |

> ⚠️ **No he inventado ningún número.** Los glifos de la última fila se usan masivamente en las builds S14 pero PureDiablo y d4builds devolvieron 403/contenido dinámico y no pude leer sus fichas. Tratad sus textos como pendientes de confirmar en el juego.

---

## 8. Orden de subida de glifos por build (S14, fuente directa)

Estas listas **sí** están tal cual en las guías, y son lo más accionable de todo el informe.

| Build (fuente) | Prioridad de subida de glifos |
|---|---|
| **Minion Necro — variante Warrior** (Maxroll) | Warrior → Mage → Essence → Eliminator → Abyssal |
| **Minion Necro — variante Mages** (Maxroll) | Mage → Essence → Deadraiser → Eliminator → Abyssal |
| **Minion Necro — variante Balanceada** (Maxroll) | Dominate → Mage → Essence → Warrior → Abyssal |
| **Army of the Dead** (Maxroll) | Dominate → Essence → Warrior → Mage → Amplify |
| **Bone Spirit** (Maxroll) | Essence → Exploit → Amplify → Corporeal → Eliminator |
| **Bone Spear** (Maxroll) | Dominate → Essence → Corporeal → Gravekeeper → Amplify |
| **Blood Wave** (Maxroll) | Dominate → Essence → Gravekeeper → Imbiber → Corporeal — *"hay que subir Essence a 50 primero para activarlo en un tablero"* |
| **Sever** (Maxroll) | Dominate → Essence → Amplify → Eliminator → Abyssal — *"Essence y Abyssal a 50 de inmediato como máxima prioridad; después Essence y Amplify se intercambian"* |
| **Naz Mages** (Icy Veins) | Mage → Warrior → Control → Amplify → Essence |
| **Reaper Summoner** (Icy Veins) | Mage → Warrior → Essence → Amplify → Deadraiser |

**Patrón claro:** *Essence* aparece en 9 de 10 listas y casi siempre en el top-2. *Dominate* lidera todas las builds de Overpower. Para vuestro caso (dos nigromantes principiantes, probablemente esbirros porque es lo más perdonable), la lista de **Minion Necro variante Mages** o la de **Naz Mages** es el punto de partida sensato.

**Nota de parche 3.1.x:** hay una mención en resúmenes de notas de parche a un **nerf del glifo Dominate** (de ~23,6% a ~1,8% de daño por acumulación a nivel de glifo 150). **No he podido verificarlo en fuente primaria** y los números parecen mal transcritos. Si Dominate está en vuestra lista, comprobad el tooltip en el juego antes de invertir 100 niveles de glifo en él. Ver §14.

---

## 9. Cómo se suben los glifos: el Foso del Artífice ✅ Base

En el parche 3.1.0 los glifos **solo suben en el Pit**. No hay Mazmorras de Pesadilla (Nightmare Dungeons) como fuente de nivel de glifo en S14 — esto sí cambió respecto a temporadas antiguas, así que cualquier guía que os mande a Nightmare Dungeons a subir glifos está caducada.

**Mecánica exacta:**
- El Pit se desbloquea automáticamente en los **tiers 1 a 10**; a partir de ahí se progresa completando tiers. Rango total: **1–150**.
- Al completar un run: **3 intentos** de mejora de glifo, **+1 intento extra si acabáis el run sin morir** → **4 intentos**.
- **Probabilidad de éxito:** depende de la diferencia entre el tier del Pit y el nivel del glifo. **Completar un Pit 10 niveles por encima del nivel del glifo garantiza la subida** (100%).
- **Niveles extra por intento:** *"Por cada 20 niveles que tu Pit esté por encima del glifo, ganas un nivel adicional con cada intento de mejora."*
- **Ejemplo trabajado de Icy Veins:** un Pit **50** hecho deathless sobre un glifo de **nivel 10** da **+3, +2, +2, +2** niveles en los cuatro intentos.

**Tabla operativa (derivada de la regla "tier = nivel+10 → 100%"):**

| Nivel del glifo | Tier de Pit para 100% garantizado | Tier para ganar niveles extra |
|---|---|---|
| 10 | 20 | 30 (+1 extra), 50 (+2 extra) |
| 25 | 35 | 45 / 65 |
| 50 | 60 | 70 / 90 |
| 100 | **110** | 130 / 150 |
| 140 | 150 | — (a nivel 140 con Pit 150 la probabilidad cae a ~8% por intento, según resúmenes) |

**Estrategia min-max:** no os quedéis "cómodos" en un tier bajo. El punto óptimo es correr **el tier más alto que podáis limpiar rápido y sin morir**, porque el deathless es un +33% de intentos gratis. La progresión real de una temporada es: subir todos los glifos a ~25 en Pits medios, luego empujar tier para llevar los 5 a 51, y luego una larga cola hasta 150 corriendo tier ≈ nivel+10.

**Valor de llevarlos a 150:** un resumen de guía cifra el salto de glifo **110 → 150** en un **~38% de daño**. Es la fuente de poder más *determinista* del juego (a diferencia del loot, no depende de RNG de drops). Marcado como dato de fuente secundaria.

---

## 10. Rutas de nodos raros y mágicos que merece la pena tocar

Reglas destiladas de Maxroll e Icy Veins:

1. **Ruta principal = puerta → legendario → socket.** Todo lo demás es opcional.
2. **Prioridad de nodos raros:** los que dan **+10 del atributo que alimenta vuestro glifo** en radio. Para Nigromante casi siempre **Inteligencia** (Control, Mage, Amplify, Eliminator) o **Voluntad** (Dominate, Deadraiser).
3. **Nodos mágicos:** valen la pena cuando **agrupan el mismo stat** (clúster). Un clúster de 3 nodos de +5% Daño Vulnerable vale más que 3 nodos sueltos dispersos. Dan **+2 de atributo más que los comunes**.
4. **Clústeres de Resistencia:** **saltárselos al principio, cogerlos al final**. Instrucción explícita en las dos guías de Icy Veins. Motivo: la resistencia es un stat de supervivencia con rendimiento decreciente y en el early Paragon necesitáis el daño.
5. **Fase tardía (Paragon ~250+):** una vez cogidos todos los nodos de daño aditivo, **Maxroll recomienda priorizar Vida Máxima y Armadura**. Esto es lo que os permite empujar Pit alto sin morir — y recordad que **morir cuesta un intento de glifo**.
6. **No construyáis alrededor de un socket demasiado pronto.** Cita de Maxroll: *"construir alrededor de un socket pronto probablemente reduce tu poder... normalmente es mejor esperar a invertir fuerte en sockets hasta que estén suficientemente subidos de nivel."* Con radio 3 y sin bonus legendario, un glifo bajo no justifica gastar 15 puntos rodeándolo de Inteligencia.

---

## 11. Dónde farmear la XP de Paragon en S14

Coste total: **~58.200 millones de XP** para llegar a Paragon 300 (Maxroll, 21/07/2026). La curva es exponencial: los primeros 100 niveles vuelan, los últimos 50 son la cola larga de la temporada.

| Actividad | XP aproximada | ¿Base o expansión? |
|---|---|---|
| **Hellwyrm** en Mareas Infernales (Helltides) | **~30,9 M por Wyrm** | ✅ Base |
| **Rupturas de S14** con spawn de Writhe/Rot | **~21 M** | ✅ Base (mecánica estacional) |
| **Rupturas Surgentes** en Helltide | **~10,7 M** | ✅ Base |
| **Rupturas normales** | **~6,2 M** | ✅ Base |
| **The Pit (Tier 100)** | **~3,6 M** | ✅ Base |

**Lectura para el dúo:** el Pit es **la peor** fuente de XP por minuto pero **la única** fuente de nivel de glifo. Conclusión operativa: **farmead Paragon en Helltide/Rupturas y entrad al Pit solo a subir glifos**, no a farmear niveles.

---

## 12. Base vs expansión — la tabla que os importa

| Sistema | Disponibilidad |
|---|---|
| Sistema Paragon completo (tableros, nodos, puertas, rotación) | ✅ **Juego base** |
| Los 9 tableros del Nigromante, incluido **Frailty** | ✅ **Juego base** (Frailty llegó con el parche **2.0**, que fue gratuito para todos, no con la compra de VoH) |
| Todos los glifos del Nigromante | ✅ **Juego base** |
| 300 niveles de Paragon + 42 puntos del Season Rank | ✅ **Juego base** |
| Nivel máximo 70 | ✅ **Juego base** (el parche 3.x subió el techo "para todo el mundo") |
| The Pit of the Artificers, tiers 1–150 | ✅ **Juego base** |
| Mareas Infernales, Rupturas de Pandemónium, Torment tiers | ✅ **Juego base** |
| Modo Solo Self-Found de S14 | ✅ **Juego base** |
| **Mercenarios (Mercenaries)** — p. ej. Subo, recomendado por casi todas las guías Maxroll | 🔒 **Vessel of Hatred** |
| **Runewords / Runas** (p. ej. Igni) | 🔒 **Vessel of Hatred** |
| **Spiritborn**, Nahantu/Kurast, Ciudadela Oscura, Kurast Undercity | 🔒 **Vessel of Hatred** |
| **Warlock** (clase) | 🔒 **Lord of Hatred** — *pero en S14 hay prueba gratuita de Warlock* |
| **Paladín** (si existe como clase de expansión) | 🔒 posiblemente Lord of Hatred — **sin confirmar** (§14) |
| Sistema de **Talismanes** (Talismans) | 🔒/✅ **sin confirmar** — Icy Veins lo asocia a Lord of Hatred (§14) |

**Traducción práctica:** vuestro Paragon será **idéntico** al de un jugador con las dos expansiones. Lo que os falta es (a) un Mercenario que aporte un multiplicador (Subo da ~25% de daño crítico extra según Maxroll) y (b) Runewords. Eso os costará poder bruto en el push de Pit, pero **no os cierra ningún tablero, ningún nodo ni ningún glifo**. Para leaderboard puro sí es una desventaja real; para llevar los 5 glifos a 150 y tener un Paragon perfecto, no.

---

## 13. Notas específicas para dúo y cross-play

- **Ambos vais de Nigromante:** eso significa que compartís pool de glifos y tableros. Min-max de pareja: **no llevéis la misma build**. Si uno va **Naz Mages / esbirros** (Cult Leader + Frailty) y el otro va **Sombra/DoT** (Wither + Frailty), cubrís curvas de daño distintas y el Pit se limpia más rápido → más intentos de glifo por hora para los dos.
- **Paragon en toda la cuenta:** hay fuentes que afirman que los niveles de Paragon son **de cuenta**, no de personaje (un alt arranca con el mismo Paragon). **No he podido verificarlo en fuente abierta** — está en §14. Si es cierto, cambia radicalmente la estrategia de rerolls.
- **Cross-play PC ↔ consola:** no encontré ninguna diferencia de sistema Paragon entre plataformas. La única asimetría práctica es de interfaz (el planificador de tableros con mando es más lento). Recomendación: **planificad el tablero fuera del juego** con el planner de Maxroll o d4builds y luego replicadlo; ahorra muchísimo tiempo al de consola.
- **El deathless importa el doble en dúo:** el bonus de intento extra del Pit se pierde si **muere alguien**. Con dos principiantes, entrar a un tier 2–3 escalones por debajo de vuestro máximo teórico rinde más glifos/hora que empujar y morir.

---

## 14. Incertidumbres y contradicciones

**Contradicciones reales entre fuentes (no las promedio, las expongo):**

1. **Breakpoints de radio y conversión a Legendario.** Tres versiones incompatibles:
   - **Icy Veins (guía de glifos S14)** y **Skycoach (S14)**: radio 3 (niv. 1–14) → **4 al 15** → **5 al 50**; Legendario al **51**; máximo **150**.
   - **Maxroll (recurso Paragon Boards)**: radio 4 al **25**, radio 5 al **51**; máximo 150.
   - **Fextralife (wiki Glyphs)**: radio 4 al **15**, Legendario + radio 5 al **45/46**; máximo **100**.
   La versión de Fextralife (tope 100, legendario 46) es casi con seguridad **de la era VoH/2.0 y está caducada** para S14, porque cuatro fuentes distintas fechadas en S14 dan tope 150. Entre 15/50 y 25/51 no puedo decidir con las fuentes que he podido abrir. **Lo que sí es seguro operativamente:** las guías de build de Icy Veins y Maxroll coinciden en "**subid a 25 primero, después a 51**", y varias builds (Sever, Blood Wave) exigen **50** para que ciertos glifos se activen. **Verificad el tooltip en el juego.**

2. **Texto del nodo legendario de Cult Leader.** Fextralife: escala con **Velocidad de Ataque de esbirros** (40% por cada 20% de VA, tope 100% VA). Game8: escala con **número de tipos de esbirro activos** (15% por tipo). Son mecánicas completamente distintas y cambian el itemizado. Probablemente una de las dos es de una versión antigua; no he podido fechar cuál.

3. **Nivel máximo de personaje.** Múltiples fuentes S14 dicen **70** (Icy Veins, Maxroll, Skycoach, guías de leveling 1–70). **Game8 dice 60** — pero su página está fechada en la era Season 6 y está desactualizada. Doy 70 por bueno.

4. **Número de tableros disponibles por clase.** Game8: "**9 opciones por clase**, de las que equipas 5 incluyendo el inicial". Maxroll (página de pathing, fechada **agosto 2024 / Season 5**): "**8 tableros + tablero inicial**, elige 5–6". Fextralife lista **9 tableros con nombre** para Nigromante **más** el tablero inicial (= 10). No he podido cerrar el número exacto. Lo que sí es firme y coincide en todas las fuentes S14: **se equipan 5 en total**.

**Cosas que NO he podido verificar (no las deis por ciertas):**

- **Texto exacto de los glifos Essence, Warrior, Mage, Exploit, Gravekeeper, Imbiber y Abyssal.** PureDiablo devolvió 403 y d4builds carga los datos por JavaScript. Son los glifos más usados de la clase y no tengo su tooltip. **Máxima prioridad de verificación in-game.**
- **El nerf del glifo Dominate en 3.1.x** ("23,6% → 1,8% por acumulación a glifo 150"). Solo aparece en un resumen de notas de parche de tercero; los números huelen a transcripción errónea. No lo he visto en notas oficiales de Blizzard (news.blizzard.com no fue accesible en esta sesión).
- **Umbrales numéricos exactos de los nodos raros** (cuánta Fuerza/Int/Vol/Des piden y cómo escalan con cada tablero acoplado). Todas las fuentes dicen que existen y que suben con cada tablero, ninguna publica la tabla.
- **Si el Paragon es de cuenta o de personaje en S14.** Aparece afirmado en un resumen de búsqueda pero no lo confirmé en página abierta.
- **Si el requisito de atributo del glifo es siempre 40** o varía por glifo. Solo tengo el dato confirmado para **Control** (40 INT) y como afirmación general para **Amplify**.
- **Si el texto actual de Amplify** ("potencia los nodos Mágicos en radio un 30%") sigue vigente: ese fraseo es del sistema **pre-2.0**, donde los glifos potenciaban nodos por porcentaje. El sistema actual usa "por cada 5 de [atributo] en rango". Sospecho que la ficha de Amplify que encontré está caducada.
- **Existencia y disponibilidad de la clase Paladín** y del **sistema de Talismanes**. Aparecen mencionados en fuentes de S14 pero no pude confirmar a qué expansión pertenecen.
- **Coste de la conversión Raro → Legendario.** Fextralife menciona "Fragmentos de Gema" (Gem Fragments), pero es dato de la era 2.0; en S14 la conversión parece ser automática al subir de nivel en el Pit. Sin confirmar.
- **No pude abrir news.blizzard.com ni las notas oficiales del parche 3.1.3**, ni las páginas de mobalytics (403) ni purediablo (403). Todo el informe descansa en Maxroll, Icy Veins, Fextralife, Game8 y Skycoach.

---

## 15. Plan de acción concreto para los dos

1. **Llegar a 70** (1–4 h según las guías de leveling S14). El Paragon se abre solo.
2. **Elegir build antes de gastar un solo punto.** Con juego base y siendo principiantes: **Minion / Naz Mages** es lo más perdonable. El otro puede ir **Sombra/DoT (Wither)** para diversificar.
3. **Tablero inicial:** meter **Mage** en el socket, ruta corta a la puerta.
4. **Acoplar en este orden:** Frailty → Cult Leader → Flesh-eater → Wither (orden de Icy Veins para esbirros). **Rotar cada tablero** para que la puerta quede lo más cerca posible del legendario.
5. **Saltarse los clústeres de Resistencia.** Anotad dónde están para volver a Paragon ~250.
6. **Entrar al Pit en cuanto tengáis los 5 glifos colocados.** Objetivo 1: todos a **25**. Objetivo 2: todos a **51** (aquí es donde la build "despierta"). Objetivo 3: cola larga a 150 corriendo tier ≈ nivel de glifo +10.
7. **Farmear Paragon en Helltide (Hellwyrm ~30,9 M) y Rupturas (~21 M)**, no en el Pit.
8. **A Paragon 300:** rehacer el reparto. Rellenar Inteligencia alrededor de cada glifo hasta el umbral, recuperar los clústeres de Resistencia, y meter Vida Máxima + Armadura para poder empujar Pit sin morir.
9. **Verificar in-game** los seis puntos de §14 marcados como no confirmados antes de tomar decisiones irreversibles (aunque el Paragon se puede resetear, resetear 342 puntos con mando es un suplicio).

---

## Fuentes

Páginas realmente abiertas y leídas para este informe:

- https://www.icy-veins.com/d4/guides/paragon-glyph-guide/
- https://www.icy-veins.com/d4/guides/the-pit-of-the-artificers-guide/
- https://www.icy-veins.com/d4/guides/mendeln-summoner-necromancer-build/
- https://www.icy-veins.com/d4/guides/mendeln-summoner-necromancer-paragon-board/
- https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/
- https://maxroll.gg/d4/resources/paragon-boards
- https://maxroll.gg/d4/resources/paragon-board-selection-and-pathing
- https://maxroll.gg/d4/meta/paragon-experience
- https://maxroll.gg/d4/build-guides/minion-necromancer-guide
- https://maxroll.gg/d4/build-guides/army-of-the-dead-necromancer-guide
- https://maxroll.gg/d4/build-guides/bone-spirit-necromancer-guide
- https://maxroll.gg/d4/build-guides/bone-spear-necromancer-guide
- https://maxroll.gg/d4/build-guides/blood-wave-necromancer-guide
- https://maxroll.gg/d4/build-guides/sever-necromancer-endgame-guide
- https://diablo4.wiki.fextralife.com/Necromancer+Paragon+Boards
- https://diablo4.wiki.fextralife.com/Glyphs
- https://diablo4.wiki.fextralife.com/Control+(Necromancer)
- https://diablo4.wiki.fextralife.com/Dominate+(Necromancer)
- https://game8.co/games/Diablo-4/archives/410512 (sistema Paragon — era Season 6, desactualizado)
- https://game8.co/games/Diablo-4/archives/416375 (tablero inicial del Nigromante)
- https://game8.co/games/Diablo-4/archives/416374 (tablero Cult Leader)
- https://game8.co/games/Diablo-4/archives/472898 (tablero Frailty)
- https://skycoach.gg/blog/diablo-4/articles/d4-paragon-board-guide
- https://kami-labs.fr/en/diablo-4/diablo-4-notes-mise-a-jour-3-1-0-saison-14/
- https://timesaver.gg/blog/diablo-4-season-14-patch-notes

Intentadas y **no accesibles** (403 / 404 / contenido dinámico), por transparencia:
- https://www.purediablo.com/diablo4/Necromancer_Glyphs (403)
- https://www.purediablo.com/diablo4/Glyphs (403)
- https://mobalytics.gg/diablo-4/guides/diablo-4-season-14-patch-notes-ptr-3-1 (403)
- https://d4builds.gg/database/paragon-glyphs/ (contenido cargado por JS)
- https://www.wowhead.com/diablo-4/guide/classes/necromancer/paragon-boards (sin contenido servido)
- https://www.wowhead.com/diablo-4/guide/classes/necromancer/paragon-glyphs (sin contenido servido; además fechada Season 12)
- https://maxroll.gg/d4/getting-started/paragon-guide (404)
- https://maxroll.gg/d4/getting-started/the-pit-guide (404)
- news.blizzard.com — notas oficiales del parche 3.1.3: no accesibles en esta sesión
