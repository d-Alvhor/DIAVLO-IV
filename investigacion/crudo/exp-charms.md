# Talismán, Sellos y Charms — Lord of Hatred
### Dominio: sistema de Talismán (Talisman) · Charms · Sets de Charms · Sello Horádrico (Horadric Seal)
### Enfoque: Nigromante de esbirros (Minion Necromancer), nivel 70, dúo PC + PS5

**Fecha de investigación:** 19 de agosto de 2026
**Parche vivo asumido:** 3.1.3, build 73224 (12/08/2026)
**Temporada:** 14 "Death Awakening" (desde 30/06/2026)

---

## 0. Anclaje de parche — leer esto ANTES que los números

Esta es la parte que en pasadas anteriores salió mal. Tres capas de datos, con distinta caducidad:

| Capa | Versión | Estado respecto al parche vivo (3.1.3) |
|---|---|---|
| Notas oficiales de Blizzard 3.1.0 (build 72592, 30/06/2026) | 3.1.0 | Vigentes. Es el último parche que **tocó** el balance de Talismán/Charms |
| Datos del juego servidos por el planificador de Maxroll | **3.1.0.72698** | Un build por detrás de 3.1.3 (73224) pero **posterior** al build de las notas 3.1.0 |
| Notas oficiales 3.1.1 (14/07/2026), 3.1.2, 3.1.3 (12/08/2026) | — | **Ningún cambio de balance de Charms/Sellos**; solo correcciones |

**Consecuencia práctica:** los valores de esta ficha son de 3.1.0 y, salvo que Blizzard haya metido un cambio silencioso, siguen vivos en 3.1.3. He verificado explícitamente que las notas de 3.1.3 no tocan Talismán ni Charms ([mobalytics vía búsqueda](https://mobalytics.gg/diablo-4/guides/patch-3-1-3-changes-and-fixes); confirmado contra [notas oficiales](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes)).

**Datamining declarado:** todo lo marcado 📦 sale del fichero de datos del juego
`https://assets-ng.maxroll.gg/d4-tools/game/data.min.json`, campo `version` = **`3.1.0.72698`**.
Es datamining, no documentación oficial. Es el texto que el juego usa para pintar los tooltips, así que es muy fiable para *qué dice el objeto*, pero **no** prueba cómo se comporta en combate.

**Trampas de datos muertos que he encontrado y neutralizado en esta pasada** (detalle en §11):
1. Varias wikis publican Red Blessing con **4 de Sobrepoder máximo** y **8–10%** de daño por acumulación. Ambos números están **muertos desde 3.1.0**.
2. Varias guías publican Seal of the Golden Epiphany con **penalización de −2 ranuras / máximo 4**. Esa penalización **se eliminó en 3.1.0**.
3. Varias guías siguen listando **Seal of the Severed Finger** como opción. Se **eliminó en 3.1.0** y se convierte automáticamente en Golden Epiphany.
4. Maxroll e Icy Veins justifican el set Black Shroud diciendo que las habilidades de esbirros "son todas de Oscuridad". Los datos de etiquetas **lo contradicen** (§9). La conclusión puede seguir siendo correcta; el razonamiento publicado no lo es.

---

## 1. Qué es el Talismán y cómo se desbloquea 🆕

🆕 **Todo este capítulo es nuevo para el jugador**: el Talismán es exclusivo de **Lord of Hatred**. Sin la expansión no existe. Al comprarla hoy, se le abre entero.

| Dato | Valor | Fuente |
|---|---|---|
| Requiere expansión | **Sí, Lord of Hatred obligatoria**. Los jugadores de juego base están fuera del sistema | [maxroll.gg/d4/resources/talisman-charms-sets](https://maxroll.gg/d4/resources/talisman-charms-sets) · [diablo4.blizzard.com/en-us/lord-of-hatred](https://diablo4.blizzard.com/en-us/lord-of-hatred) |
| Requisitos oficiales | "Lord of Hatred and Vessel of Hatred Expansion require Diablo IV base game" | [diablo4.blizzard.com/en-us/lord-of-hatred](https://diablo4.blizzard.com/en-us/lord-of-hatred) |
| Cómo se desbloquea | Misión principal **"Last of the Horadrim"**, de la campaña de Lord of Hatred | [game8.co/games/Diablo-4/archives/597017](https://game8.co/games/Diablo-4/archives/597017) (vía búsqueda) |
| Momento exacto | Pronto en la campaña, **antes de embarcar hacia Temis**; se conoce a Lorath en Backwater | [maxroll](https://maxroll.gg/d4/resources/talisman-charms-sets) · [icy-veins](https://www.icy-veins.com/d4/guides/talisman-system-overview/) |
| Misión previa | "Solace Beyond Sight" | búsqueda (game8) |
| Qué te dan al desbloquearlo | El Talismán Horádrico, **un Sello y tu primer Charm** listos para equipar | búsqueda (game8) |
| ¿Vale para toda la cuenta? | **Sí**, desbloquea el sistema para el resto de personajes | [maxroll](https://maxroll.gg/d4/resources/talisman-charms-sets) · [icy-veins](https://www.icy-veins.com/d4/guides/talisman-system-overview/) |
| Dónde vive el Talismán | En una **ranura de interfaz dedicada**, no en el inventario: no compite por espacio de equipo | búsqueda (thenerdstash / d4gold) |
| Cuándo empiezan a caer Charms | En cuanto acabas "Last of the Horadrim", como botín de mundo | búsqueda (game8) |

> ⚠️ **Aviso de orden de juego para el jugador:** el Talismán **no** se desbloquea al comprar la expansión. Hay que **jugar la campaña de Lord of Hatred hasta "Last of the Horadrim"**. Está muy al principio, pero es un paso obligatorio y hoy no lo tiene hecho.

---

## 2. El Sello Horádrico (Horadric Seal) — ¿es cosa distinta? **No** 🆕

Respuesta directa a la pregunta del encargo: **el Sello Horádrico no es un sistema aparte. Es la pieza central del Talismán.**

📦 En el fichero de datos, `Horadric Seal` es literalmente el **tipo de objeto** (`itemTypes` → clave `HoradricSeal`, nombre "Horadric Seal"). Todos los sellos del juego —incluidos los tres míticos con nombre propio— son objetos de ese tipo.

**El modelo real:**

```
        ┌─────────────────────────────┐
        │        TALISMÁN             │
        │   (ranura de interfaz)      │
        │                             │
        │   ○  ○  ○                   │  ← anillo exterior: CHARMS
        │  ○  [SELLO]  ○              │  ← centro: 1 SELLO HORÁDRICO
        │   ○  ○  ○                   │
        └─────────────────────────────┘

  El SELLO decide CUÁNTAS ranuras de Charm se abren y aporta sus propios afijos.
  Los CHARMS van en el anillo exterior y son los que dan stats y bonus de set.
```

- Total: **7 posiciones** — 1 central (Sello) + hasta 6 exteriores (Charms) — según [overgear](https://overgear.com/guides/diablo-4/talisman-system/) y [grindout](https://grindout.com/diablo-4/guides/talismans) vía búsqueda. Corroborado por el máximo de 6 en los datos 📦.
- El Sello aporta **afijos propios** además de las ranuras ([icy-veins](https://www.icy-veins.com/d4/guides/talisman-system-overview/)).

---

## 3. Sellos: rarezas y ranuras — números exactos 📦

📦 El número de ranuras es el atributo interno **`Talisman_Charm_Slot_Count_Base`** (id 829). Valores leídos directamente del fichero de datos `3.1.0.72698`:

| Sello | Rareza | Ranuras de Charm | Nivel req. | Clave interna 📦 |
|---|---|---|---|---|
| Horadric Seal (base) | Común | **3** | — | `Talisman_Seal_First` |
| Magic Horadric Seal | Mágico | **3** | — | `Talisman_Seal_Magic` |
| Rare Horadric Seal | Raro | **4** | — | `Talisman_Seal_Rare` |
| Legendary Horadric Seal | Legendario | **5** | 50 | `Talisman_Seal_Legendary` |
| Ancestral Horadric Seal | Ancestral | *(sin valor de ranuras en los datos)* | **70** 🆕 | `Talisman_Seal_Ancestral` |
| Mythic Unique Horadric Seal | Mítico | *(base sin valor; los tres con nombre dan 6)* | **70** 🆕 | `Talisman_Seal_MythicUnique` |

**Afijo clave del Sello** 📦: `Talisman_SealAffix_AdditionalCharmSlot` → **"+1 Charm Slot"**.
Esto es lo que convierte un Sello Legendario de 5 ranuras en uno de **6**.

**Cruce con la tabla publicada por Icy Veins** ([talisman-system-overview](https://www.icy-veins.com/d4/guides/talisman-system-overview/), actualizado 28/06/2026):

| Rareza | Ranuras (Icy Veins) | Ranuras (datos 📦) | ¿Cuadra? |
|---|---|---|---|
| Magic | 3 | 3 | ✅ |
| Rare | 4 | 4 | ✅ |
| Legendary | 5 | 5 | ✅ |
| Mythic Unique | 6 | 6 | ✅ |

Icy Veins añade que un afijo puede "desbloquear una ranura adicional a costa de un bonus de Sello" — coherente con `AdditionalCharmSlot`.

---

## 4. Los tres Sellos Míticos — el techo del sistema 🆕

📦 Los tres tienen **`Talisman_Charm_Slot_Count_Base` = 6** y **nivel 70**. Su poder está en el afijo único (`explicits`):

| Sello Mítico | Efecto único — texto exacto 📦 | Clave del afijo 📦 | Estado |
|---|---|---|---|
| **Seal of the Diamond Mind** | *"Reduces the number of Charms needed for Set bonuses by 1 (to a minimum of 2)."* | `Talisman_SealAffix_Ancestral_03` | **Vivo. El mejor para casi todo.** |
| **Seal of the Golden Epiphany** | *"Can equip up to 3 Unique Charms"* | `Talisman_SealAffix_Ancestral_02` | Vivo. Mejorado en 3.1.0 |
| **Seal of the Severed Finger** | *"Cannot have more than 5 Sockets, but can equip 2 Unique Charms"* | `Talisman_SealAffix_Ancestral_01` | ❌ **ELIMINADO en 3.1.0** |

**Cambios oficiales 3.1.0** ([news.blizzard.com/en-us/article/24287406](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes)), citados literalmente:
- *"Seal of the Golden Epiphany: -2 Charm slots, but you can equip up to 3 Unique Charms"* → **cambiado para quitar la penalización de ranuras**.
- *"Seal of the Severed Finger: Removed, existing copies will convert into Seal of the Golden Epiphany"*.
- Corrección: *"Fixed an issue where the Seal of the Diamond Mind did not correctly grant its intended number of Charm slots"*.

### 4.1 Por qué **Diamond Mind** es el objeto-objetivo de esta build

Con Diamond Mind, un set de 5 piezas se completa con **4 charms**, y uno de 3 con **2**.
Sobre 6 ranuras eso significa: **set de 5 piezas activo (4 charms) + 2 ranuras libres** para un Charm único y otro charm — o dos sets a la vez.

📦 Confirmado por el texto del afijo. Corroborado de forma independiente por [timesaver.gg](https://timesaver.gg/blog/diablo-4-mythic-seals-3-unique-charms-season-14): *"Reduces charms needed to complete a Set by 1 (minimum 2), enabling a 5-piece and 3-piece set bonus simultaneously"*. Icy Veins también lo marca como *chase unique* en la guía de Reaper Summoner ([icy-veins](https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/)).

> ⚠️ **Corrección a Icy Veins:** su guía de build describe Seal of the Diamond Mind como *"equips an extra charm slot"*. Eso **no es lo que hace** según los datos 📦: da 6 ranuras como los otros dos míticos, y su poder único es **rebajar el requisito de set en 1**. Fuente del error probable: la corrección de bug de 3.1.0 sobre las ranuras.

> ⚠️ **Corrección a timesaver.gg:** esa misma página dice que Golden Epiphany tiene *"a maximum of 4 Sockets"* y presenta Severed Finger como opción viva. Ambas cosas son **datos de antes de 3.1.0**.

---

## 5. Tipos de Charm

| Tipo | Qué da | Cuándo aparece | Fuente |
|---|---|---|---|
| **Charm Mágico / Raro** | Bonus individuales flojos, afijos sueltos | Pronto, desde el desbloqueo | [icy-veins](https://www.icy-veins.com/d4/guides/talisman-system-overview/) |
| **Charm de Set** (Set Charm) | Bonus individual flojo + **bonus progresivos a 2, 3 y 5 equipados** | Set Charms de clase: nivel **70** 📦 | [icy-veins](https://www.icy-veins.com/d4/guides/talisman-system-overview/) + 📦 |
| **Charm Único** (Unique Charm) | El poder de un objeto único, **reescrito** (§11) + 2 afijos aleatorios | Torment altos | [icy-veins](https://www.icy-veins.com/d4/guides/talisman-system-overview/) |
| **Charm Mítico** | Poder de un objeto mítico | Nivel **70** 📦, Torment muy altos | 📦 |

📦 **Recuento exacto en los datos:** 365 objetos de tipo `Charm` en total. De ellos, **112 son utilizables por el Nigromante** y 72 son de clase libre.

📦 Los Set Charms de clase requieren **nivel 70** (`levelRequirement: 70`). 🆕 **El jugador acaba de llegar a 70 justo hoy: hoy es literalmente el primer día en que estos charms le pueden caer y equipar.**

📦 Existen además variantes **pre-Torment** de los sets genéricos (`Talisman_Charm_Set_Small_PreTorment_*`), sin requisito de nivel — son las versiones de baja dificultad.

---

## 6. Los cinco nombres — el patrón de nomenclatura

📦 Los cinco charms de **cualquier** set de clase llevan siempre los mismos cinco nombres propios:

> **Phoba · Fer · Mlor · Linta · Berú**

Ejemplo: *Phoba of the Black Shroud, Fer of the Black Shroud, Mlor of the Black Shroud, Linta of the Black Shroud, Berú of the Black Shroud*.

Esto explica el texto de ambientación del Seal of the Golden Epiphany 📦: *"I know what I must do. Phoba, Fer, Mlor, aligned upon a single, terrible course."* —Tal Rasha.

**Consecuencia práctica:** "Berú of the Black Shroud" —el nombre que traía el encargo— **no es un set**. Es **una de las cinco piezas** del set *Peace of the Black Shroud*. Corroborado por [wowhead](https://www.wowhead.com/diablo-4/item/ber%C3%BA-of-the-black-shroud-2426839) (Set Charm, Nigromante, **nivel 70**, poder de objeto 850) y por [purediablo](https://www.purediablo.com/diablo4/Ber%C3%BA_of_the_Black_Shroud_-_Charm).

---

## 7. Los CINCO sets de Nigromante — texto y números exactos 📦

📦 Leídos de `itemSets` + `affixes` del fichero `3.1.0.72698`. Ninguna guía consultada lista los cinco.

### 7.1 🥇 Rathma's Waking Touch — **el set de esbirros** 🆕
📦 `Talisman_Necro_05` · charms: *Phoba/Fer/Mlor/Linta/Berú **of the Waking Touch***

| Piezas | Efecto exacto |
|---|---|
| **(2)** | Tus **Esbirros infligen 60%[x] más daño** y reducen el tiempo de reutilización de **Ejército de los Muertos en 1 segundo** cada vez que infligen daño |
| **(3)** | El **35% del daño que recibes se redirige a tus Esbirros** |
| **(5)** | **Ejército de los Muertos inflige 450%[x] más daño.** Mientras esté activo, tus Esbirros son más grandes, tienen **100%[x] más Vida** y ganan **25%[+] Velocidad de Ataque** |

✅ **Corroborado de forma independiente** por [game8.co/games/Diablo-4/archives/598000](https://game8.co/games/Diablo-4/archives/598000), que da exactamente los mismos números (60%, 1 s, 35%, 450%, 100%, 25%) y añade que los esbirros son **"20% larger"**.

### 7.2 🥈 Peace of the Black Shroud — el que recomiendan las guías
📦 `Talisman_Necro_04` · charms: *...**of the Black Shroud***

| Piezas | Efecto exacto |
|---|---|
| **(2)** | Tus habilidades de **Oscuridad (Darkness)** infligen el **75%** de su daño como daño adicional de Corrupción o Congelación durante **30 s** |
| **(3)** | Ganas **30% de Reducción de Daño** durante **5 s** siempre que infliges daño con el tiempo a un enemigo |
| **(5)** | Infliges **175%[x] más daño de Sombra y Frío**. Los enemigos Corrompidos o Congelados por encima de su vida restante quedan permanentemente **Vulnerables**, **Debilitados**, **Ralentizados un 85%**, reciben **50%[x] más daño tuyo** y son **Aterrorizados cada 5 s** |

✅ **Corroborado** por [game8](https://game8.co/games/Diablo-4/archives/598000) (mismos 75%, 30 s, 30%, 5 s, 175%, 85%, 50%) y por búsqueda en [purediablo](https://www.purediablo.com/diablo4/Ber%C3%BA_of_the_Black_Shroud_-_Charm).

### 7.3 Radament's Desecration
📦 `Talisman_Necro_01` · charms: *...**of Desecration***

| Piezas | Efecto exacto |
|---|---|
| **(2)** | Formar o consumir un Cadáver reduce el coste de Esencia y los tiempos de reutilización de tus habilidades **Profanas y Macabras un 25%** y aumenta su daño un **30%[x]** durante **6 s**. Lanzar una habilidad Suprema forma **10 Cadáveres** durante su duración |
| **(3)** | Al formar o consumir un Cadáver ganas **15% de Reducción de Daño** durante **6 s**. Los enemigos Cercanos a tus Cadáveres reciben **Decrepitud e Doncella de Hierro** |
| **(5)** | Tus habilidades **Profanas y Macabras infligen 225%[x] más daño**. Tus habilidades Supremas son **también** Profanas o Macabras |

📌 Nota oficial 3.1.0: *"The set bonus will no longer continuously reapply the Curses to enemies already Cursed"* ([news.blizzard.com](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes)).

### 7.4 Art of the Bone Weaver
📦 `Talisman_Necro_02` — set de Hueso. (2) Quintaesencia tras gastar Esencia en habilidades de Hueso: **+10%[+] Prob. Crítico y +50%[x] Daño Crítico** durante 15 s. (3) Quintaesencia da además Reducción de Daño. (5) Al ganar Quintaesencia lanzas **12 esquirlas** perforantes, generas **3 de Esencia** por enemigo alcanzado.

📌 Cambio oficial 3.1.0: *"5-Piece Set Bonus: Damage bonus increased from 175% to 200%"* ([news.blizzard.com](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes)).

### 7.5 Word of the Blood Binder
📦 `Talisman_Necro_03` — set de Sangre. (2) Habilidades de Sangre te Fortifican **5% de Vida Máxima** y hacen **60%[x]** más daño mientras la Fortificación te cura. (3) Cada punto porcentual de Vida Fortificada sube tu Vida Máxima otro tanto durante **20 s**, hasta **50%**. (5) Tus habilidades Básicas, Principales y Supremas de Sangre drenan **3%** de Vida Máxima al lanzar para **activarse dos veces**; las habilidades de Sangre infligen **75%[x]** más daño.

📌 Texto reconfirmado en las notas 3.1.0 ([news.blizzard.com](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes)) y ajustado en 3.1.1 (búsqueda).

---

## 8. Sets genéricos (cualquier clase) 📦

📦 Solo llegan a **(3) piezas**, no a 5. Útiles para rellenar ranuras sueltas.

| Set | (2) piezas | (3) piezas |
|---|---|---|
| **Mastery** | **+X a Todas las Habilidades** *(valor por fórmula, no fijo)* | — |
| **Survival** | **+1000 Armadura, +100 a Todas las Resistencias** | **+200 a Todos los Atributos** |
| **Slaughter** | +X% Reducción de Daño, x% Daño | +X% Reducción de Daño de Élites, x% Daño a Élites |
| **Practiced Technique** | +X% Vel. Ataque, +X% Vel. Movimiento | +X% Oro, +X% Experiencia extra por muerte |
| **Dark Pact** | Golpe Afortunado: hasta **40%** de infligir **1500** de daño de Frío / Fuego / Rayo (tres líneas) | — |

📦 **Survival** es el único con números planos y grandes garantizados: **+1000 Armadura / +100 Resist. Todas / +200 Todos los Atributos**. Con **Diamond Mind** el (2) piezas se consigue con **1 solo charm** y el (3) con **2**.

---

## 9. ⚠️ VERIFICACIÓN DEL MODELO: ¿Black Shroud o Rathma's Waking Touch?

Esta es la sección más importante del informe, y donde discrepo de las guías.

### 9.1 Lo que dicen las guías

- **Maxroll** ([minion-necromancer-guide](https://maxroll.gg/d4/build-guides/minion-necromancer-guide), actualizado **22/07/2026**, S14): *"The Black Shroud set pairs perfectly with this build as all the skills are also Darkness skills. Providing a good Damage reduction and great 5 piece multiplier."* Recomienda Black Shroud en **las tres variantes** (Warrior, Mages, Híbrida).
- **Icy Veins** ([shadowblight-summoner-build](https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/), actualizado **27/06/2026**, S14): *"Full Black Shroud Charm Set of any quality"*, con el 5-set por delante de cualquier otro charm.

Ninguna de las dos menciona **Rathma's Waking Touch** en su sección de charms.

### 9.2 El problema con el razonamiento publicado

📦 Etiquetas (`tags`) reales de las habilidades, leídas del fichero de datos:

| Habilidad (en la barra del jugador) | Etiquetas 📦 | ¿Oscuridad? |
|---|---|---|
| Skeleton Warrior | `Summon, Corpse, Corpse, Physical, Minion` | ❌ **No** |
| Skeleton Mage | `Summon, Minion, Core, Damage, Minion` | ❌ **No** |
| Golem | `Unstoppable, Summon, Macabre, Damage, Cooldown, Minion` | ❌ **No** |
| Army of the Dead | `Summon, Crowd Control` | ❌ **No** |
| Corpse Tendrils | `Profane` | ❌ **No** |
| Iron Maiden | `Profane, Physical, Essence` | ❌ **No** |
| *(referencia)* Blight | `Darkness, Shadow` | ✅ Sí |
| *(referencia)* Decompose | `Darkness, Channeled, Shadow` | ✅ Sí |
| *(referencia)* Reap | `Darkness` | ✅ Sí |

**Ninguna habilidad de esbirros lleva la etiqueta `Darkness`.** La afirmación de Maxroll, tal cual está escrita, **no se sostiene contra los datos**.

Dónde **sí** aparece `Darkness` en el árbol de esbirros 📦 — solo en mejoras concretas del Libro de los Muertos:

| Entrada 📦 | Etiquetas | ¿La tiene el jugador? |
|---|---|---|
| `SkeletonWarrior_Reaper_Passive_UpgradeB` | `Summon, Darkness` | ✅ **Sí** — tiene Guerreros Segadores mejora **B** |
| `SkeletonMage_Shadow_Passive_UpgradeA` | `Summon, Darkness` | ❌ No — tiene Magos de Sombra mejora **B** |
| `SkeletonMage_Cold_Attack` | `Summon, Darkness` | ❌ No — usa Magos de Sombra, no de Frío |
| `Golem_Iron_Passive_UpgradeA` | `Summon, Darkness, Macabre` | ❌ No — tiene Gólem de **Sangre** mejora A |

### 9.3 Cómo funciona Black Shroud **de verdad** para esta build

El (5) piezas de Black Shroud **no** es un multiplicador de "habilidades de Oscuridad". Es literalmente:

> *"You deal 175%[x] increased **Shadow and Cold** damage"*

Es decir: funciona por **tipo de daño**, no por etiqueta. Y ahí sí entra la build — pero **solo en parte**:

| Fuente de daño del jugador | Tipo | ¿Recibe el 175%[x] de Black Shroud? |
|---|---|---|
| Magos Esqueléticos de **Sombra** | Sombra | ✅ **Sí** |
| Guerreros **Segadores** | *(no confirmado — ver "No encontrado")* | ❓ |
| Gólem de **Sangre** | Sangre / Físico | ❌ Probablemente no |
| Tentáculos de Cadáver, Doncella de Hierro | Físico / Profano | ❌ No |
| Ejército de los Muertos | *(no confirmado)* | ❓ |

Y el **(2) piezas** (75% del daño como Corrupción/Congelación) solo se dispara con habilidades **etiquetadas Darkness**, que en su barra actual es un conjunto muy reducido.

En cambio, **Rathma's Waking Touch (2)** da **60%[x] a TODO el daño de esbirros**, sin importar el tipo, y el **(5)** da **450%[x] a Ejército de los Muertos** —que el jugador **tiene equipado**— más **100%[x] de Vida** y **+25% Vel. Ataque** a los esbirros mientras dura.

### 9.4 Veredicto honesto

**No lo resuelvo con lo que he podido leer.** Lo que puedo afirmar con evidencia:

1. ✅ **Rathma's Waking Touch es, por diseño, el set de esbirros.** Cada línea de sus tres bonus habla de Esbirros o de Ejército de los Muertos. Esto es un hecho, no una opinión.
2. ✅ **El razonamiento con que las guías descartan implícitamente ese set es incorrecto** (§9.2).
3. ⚠️ **Su conclusión puede seguir siendo correcta de todos modos.** 175%[x] de Sombra y Frío + 50%[x] adicional + Vulnerable/Debilitado permanentes es un paquete enorme para una build centrada en Magos de Sombra, y Maxroll e Icy Veins están mirando hojas de daño reales que yo no tengo.
4. ❌ **No he encontrado ni una sola comparación numérica publicada entre los dos sets.** Ni en Maxroll, ni en Icy Veins, ni en game8, ni en las búsquedas de Reddit.

**Lo que esto significa para hoy:** los charms de set **caen del mismo sitio y son intercambiables en el Cubo Horádrico dentro del mismo set**. Recoge **los dos**. La decisión se toma con el maniquí, no con este informe. Ver §14, punto 6.

---

## 10. Charms Únicos para un Nigromante de esbirros 📦

📦 Únicos **exclusivos de Nigromante** disponibles como Charm:

| Charm Único | Efecto — **texto de la versión CHARM** 📦 | Valores 📦 | Interés para esbirros |
|---|---|---|---|
| **Pact of Bone** | *"Your Minions deal X% increased damage. When one of your Minions die, your other Minions enrage, gaining Y% Attack Speed and Critical Strike Chance for 3 seconds."* | X = **15–25%[+]**, Y = **20–35%[+]** | 🥇 **El más directo.** Ninguna guía consultada lo menciona |
| **Blood Moon Breeches** | *"Your Summons have a X% chance to randomly inflict Decrepify or Iron Maiden when they deal damage. You deal Y% increased Critical Strike Damage to enemies affected by your Curses."* | X = **3–7%**, Y = **20–50%[x]** | 🥈 Muy bueno: **lleva Doncella de Hierro en la barra** |
| **Will of Rathma** | *"Vulnerable, Weakened, Crowd Controlled, or Corrupted enemies are Afflicted, taking **20%** increased damage from you..."* | daño de maldición **2–10** | Recomendado por Icy Veins |
| **The Gloom Ward** | Shadow damage infecta con Shadowblight; cada 6.º impacto añade daño de Corrupción | **500–600%** | Sinergia con Magos de Sombra |
| **Omen of Pain** | Aura oscura que aplica Decrepitud y Doncella de Hierro alrededor | — | Defensivo/maldiciones |
| **Red Blessing** | Ver §11 — **datos en conflicto** | ver §11 | ⚠️ Golpeado dos veces |
| **Gravewalker's Hand** | Generación de Esencia + daño de habilidades de Hueso | — | ❌ No es de esbirros |
| **Bloodless Scream** | Habilidades de Oscuridad Enfrían; daño a Congelados | **1–2** | Nicho |

📦 Únicos **genéricos** notables: Wyrdskin (**30–40%[x]** a Vulnerable+Debilitado), Godslayer Crown (**7.5–10%[x]**), Banished Lord's Talisman (**5.33–6.67%[x]** por acumulación de Sobrepoder), Temerity, Endurant Faith, Flickerstep, Tibault's Will, Ring of Starless Skies, Harlequin Crest (**+6 rangos a todas las habilidades**, mítico).

**Lo que recomienda Icy Veins** ([shadowblight-summoner-build](https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/)), en su orden:
- Ofensivos: Red Blessing (si tiene el mítico Banished Lord's Talisman) → Wyrdskin → Godslayer Crown → Will of Rathma
- Defensivos: Endurant Faith → Temerity
- Chase: Seal of the Diamond Mind

> ⚠️ **Nota:** "Banished Lord's Talisman" es un **amuleto único** (y su charm), **no** el sistema de Talismán. Colisión de nombres que confunde a muchas guías.

---

## 11. 🚨 LA TRAMPA GRANDE: el Charm Único ≠ el objeto único

**Todas las fuentes consultadas afirman lo mismo**, y todas simplifican de más:

- Icy Veins: *"Unique Charms provide the power of their respective Unique item when equipped"* ([talisman-system-overview](https://www.icy-veins.com/d4/guides/talisman-system-overview/))
- Búsquedas y wikis repiten la misma frase.

📦 **Es falso.** Los datos guardan **dos afijos distintos** para cada único: el del objeto y el del charm (`Talisman_Charm_Affix_*`). Y los textos **no coinciden**:

| Único | Versión **OBJETO** 📦 | Versión **CHARM** 📦 | Veredicto |
|---|---|---|---|
| **Will of Rathma** | Los Afligidos reciben **40%** más daño | Los Afligidos reciben **20%** más daño | 🔻 Charm **más débil** |
| **Pact of Bone** | Esbirros ganan **30–35%[+]** Vel.Ataque y Prob.Crítico; al morir uno, los demás **infligen 30–35%[x]** más | Esbirros **infligen 15–25%[+]** más daño; al morir uno, los demás ganan **20–35%[+]** Vel.Ataque y Prob.Crítico | 🔀 **Efecto distinto**, no una versión escalada |
| **Red Blessing** | **2** de Sobrepoder máx.; **5.33–6.67%[x]** por acumulación | **4** de Sobrepoder máx.; **15–25%[x]** por acumulación | ⚠️ **Conflicto sin resolver** |

**Esto es un hallazgo, no una nota al pie.** Significa que **no puedes deducir lo que hace un Charm Único mirando el objeto**, y que las tablas de "poderes únicos" de las wikis **no describen los charms**.

### 11.1 El caso Red Blessing — tres números distintos circulando

| Fuente | Sobrepoder máx. | Daño por acumulación | Estado |
|---|---|---|---|
| Wikis (fextralife, game8, purediablo) vía búsqueda | **4** | **8–10%** | ❌ **MUERTO** — anterior a 3.1.0 |
| Notas oficiales 3.1.0 | **4 → 2** | *(no citado)* | ✅ Oficial |
| 📦 Afijo del **objeto** (`Amulet_Unique_Necro_100_x2`) | **2** | **5.33–6.67%** | ✅ Coherente con lo oficial |
| 📦 Afijo del **charm** (`Talisman_Charm_Affix_Amulet_Unique_Necro_100_x2`) | **4** | **15–25%** | ⚠️ **Sin resolver** |

Cita literal de las notas 3.1.0 ([news.blizzard.com](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes)): *"Red Blessing (Balance): Maximum Overpower bonus reduced from 4 to 2"*.

**No sé** si el charm conserva 4 a propósito (tuneado aparte) o si es un afijo sin parchear. **No lo reconstruyo.** Va a "No encontrado". Se comprueba en 5 segundos mirando el tooltip en el juego.

### 11.2 Contexto que agrava el caso Red Blessing

Búsqueda: en Season 14 el **glifo Dominate recibió un nerf grande** y *"every build that was stacking Overpower has seen a significant damage loss"*; las guías han abandonado el glifo (búsqueda, [d4guides.gg](https://d4guides.gg/en/builds/necromancer)).

Red Blessing es **exactamente** un charm de acumulación de Sobrepoder. Icy Veins lo pone el primero de su lista ofensiva **condicionado a tener el mítico Banished Lord's Talisman**. Con el nerf de Dominate más el nerf directo al objeto, **es el charm con más probabilidad de estar sobrevalorado en las guías**. No lo persigas primero.

---

## 12. Afijos de Sello específicos de cada set 📦 — la lista de la compra

📦 Hallazgo que no aparece en ninguna guía consultada: **los Sellos pueden llevar afijos ligados a un set concreto**. Para el set de esbirros:

| Afijo del Sello 📦 | Texto |
|---|---|
| `..._Set_Necromancer_01_MinionDamage` | **"Rathma's Walking Touch: +X% [x] Minion Damage"** |
| `..._Set_Necromancer_01_MinionAttackSpeed` | "Rathma's Walking Touch: +X% Minion Attack Speed" |
| `..._Set_Necromancer_01_SkeletonWarriorRanks` | **"+X a Skeleton Warrior"** |
| `..._Set_Necromancer_01_SkeletonMageRanks` | **"+X a Skeleton Mage"** |
| `..._Set_Necromancer_01_PhysicalDamage` | "+X%[x] Daño Físico" |

> 🔍 **Ojo al buscar:** el juego escribe **"Rathma's *Walking* Touch"** en los afijos de Sello, pero el set se llama **"Rathma's *Waking* Touch"**. Es una errata en las cadenas del juego (📦 ambas grafías conviven en el mismo fichero). Si busca en Google o en la casa de subastas, que pruebe **las dos**.

Para Black Shroud existen los equivalentes: `+X%[x] Darkness Skill Damage`, `+X%[x] Shadow Damage`, `+X%[x] Cold Damage`, `+X Resist. Todos`, `Darkness Skill CDR`, `+X%[x] Daño a Enemigos con Control de Masas`.

**Afijos de Sello que recomienda Icy Veins** ([shadowblight-summoner-build](https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/)): **+% Daño Crítico**, **+% Velocidad de Ataque**, **+% multiplicador de daño**.
**Afijos de Charm a buscar:** **+ a habilidades de Oscuridad**, **+ a habilidades de Esbirros**.
**Maxroll** ([minion-necromancer-guide](https://maxroll.gg/d4/build-guides/minion-necromancer-guide)): *"Look for one with at minimum one extra damage multiplier. You may also opt for Critical Strike Chance in the event you are low on that stat."*

---

## 13. Dónde caen y cómo se farmean

⚠️ **Aviso de fiabilidad:** los umbrales de Torment de abajo vienen de webs de *boosting* (skycoach, boostmatch, mmogah, aoeah, timesaver) y de game8. **Blizzard no los publica** y ni Maxroll ni Icy Veins los concretan. Trátalos como orientación, no como número duro.

| Qué | Umbral citado | Fiabilidad | Fuente |
|---|---|---|---|
| Charms en general | Botín de mundo: mobs, cofres, jefes, actividades de endgame | Media | búsqueda (skycoach/boostmatch) |
| **Set Charms** | Más frecuentes a partir de **Torment 3** | **Media-alta** (2 fuentes) | [game8](https://game8.co/games/Diablo-4/archives/598000) + búsqueda |
| Set Charms (mínimo) | Empiezan a caer desde **Torment I** | Media | búsqueda ([icy-veins](https://www.icy-veins.com/d4/guides/talisman-system-overview/) menciona Torment I) |
| Charms Únicos | **Torment 8** | Baja (1 fuente booster) | búsqueda (skycoach) |
| **Sellos Míticos** | **Torment 10+** | Media-alta (2 fuentes) | [timesaver](https://timesaver.gg/blog/diablo-4-mythic-seals-3-unique-charms-season-14) + [maxroll](https://maxroll.gg/d4/resources/talisman-charms-sets) (*"only in the highest tiers of Torment"*) |

**Mejores fuentes de Sellos Míticos** ([timesaver.gg](https://timesaver.gg/blog/diablo-4-mythic-seals-3-unique-charms-season-14)): Corrupted Reaper (jefe de guarida de temporada), Echo of Mephisto, Echoing Hatred, Tributos de Kurast Undercity, Regalos Torturados de Misterios en Helltide.

✅ **Corroboración oficial parcial:** las notas de **3.1.3** confirman que **Corrupted Reaper** y **Echo of Mephisto** son contenido vivo de S14 ([news.blizzard.com](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) / [icy-veins 3.1.3](https://www.icy-veins.com/d4/news/diablo-4-3-1-3-patch-notes-easier-season-objectives-and-echo-of-mephisto-portal-fix/)). El parche 3.1.3 arregló además el portal de la tercera fase de Echo of Mephisto **para quien se une a la partida en curso** — relevante en dúo.

### 13.1 Cubo Horádrico — recetas 🆕

El Cubo se desbloquea **más tarde** en la campaña de Lord of Hatred, **en Temis** (búsqueda, game8).

| Receta | Ingredientes | Fiabilidad | Fuente |
|---|---|---|---|
| **Reroll Set Charm** | Transmutar un Set Charm en **otro charm del mismo set** | **Alta** | [maxroll](https://maxroll.gg/d4/resources/talisman-charms-sets) |
| **3-a-1 Transmutación** | 3 objetos del mismo tipo → 1 objeto nuevo del mismo tipo | **Alta** | [maxroll](https://maxroll.gg/d4/resources/talisman-charms-sets) |
| **Crear Charm Único** | 1 Único Ancestral + 3 Únicos aleatorios | Media | búsqueda (skycoach) |
| **Reroll Unique Power** | Ahora **funciona en Talisman Charms** y objetos no ancestrales | Media (3.1.1) | búsqueda |

🔑 **"Reroll Set Charm" es la receta que cierra el set.** Si te caen tres *Fer of the Waking Touch* repetidos, los conviertes en las piezas que faltan. Es el mecanismo que hace realista completar un 5-set antes del 15 de septiembre.
📌 Maxroll añade: los rerolls de Set Charm pueden salir con **Afijos Superiores (Greater Affixes) con ~4% de probabilidad por afijo** ([maxroll](https://maxroll.gg/d4/resources/talisman-charms-sets)).

---

## 14. Dúo PC + PS5 — y el caso de la pareja sin expansión

### 14.1 Si la pareja **NO** tiene Lord of Hatred

| Consecuencia | Detalle |
|---|---|
| **No tiene Talismán en absoluto** | Es un sistema exclusivo de la expansión ([maxroll](https://maxroll.gg/d4/resources/talisman-charms-sets), [blizzard](https://diablo4.blizzard.com/en-us/lord-of-hatred)) |
| **No puede hacer la misión de desbloqueo** | "Last of the Horadrim" es campaña de LoH |
| **¿Pueden jugar juntos igualmente?** | ❓ No confirmado — ver "No encontrado" |
| **Regalarle charms no sirve de nada** | Sin Talismán no hay dónde ponerlos |
| Diferencia de poder | Se abrirá una brecha grande: él sumará set de 5 piezas + sellos míticos y ella/él no |

> 💡 **Dato de compra relevante:** la página oficial indica que **Vessel of Hatred va incluido en cualquier compra de Lord of Hatred** ([diablo4.blizzard.com](https://diablo4.blizzard.com/en-us/lord-of-hatred)). Si la pareja va a comprar, que compre **solo Lord of Hatred**: VoH viene dentro. (Y conviene que el jugador revise si hoy pagó las dos por separado sin necesidad.)

### 14.2 Si la pareja **SÍ** tiene la expansión

| Punto | Detalle | Fuente |
|---|---|---|
| **Charms y Sellos NO míticos son intercambiables** | 3.0 corrigió: *"Fixed an issue where non-Mythic Charms and Seals could not be traded"* | [news.blizzard.com 3.0](https://news.blizzard.com/en-us/article/24271857/diablo-iv-patch-notes-3-0) |
| **Míticos: presuntamente ligados** | ❓ No confirmado — ver "No encontrado" | — |
| Ventana de intercambio | Hubo un bug (reportado en PTR) que obligaba a **tirar el charm al suelo** en vez de usar la ventana segura | [us.forums.blizzard.com](https://us.forums.blizzard.com/en/d4/t/potential-bug-allow-charms-in-trade-window/247489) |
| **Farmeo en pareja** | Los dos son Nigromantes: **los Set Charms de Nigromante que le caigan a uno le valen al otro**. Es la mejor situación posible para cerrar dos sets de 5 | 📦 (`classFilter` de Nigromante) |
| PC vs PS5 | ❓ No he encontrado ninguna diferencia de plataforma en este sistema | — |

🎯 **La jugada del dúo:** al ser ambos Nigromantes, **cada charm de set duplicado que le caiga a uno es una pieza que le falta al otro**. Combinado con el reroll del Cubo, dos jugadores cierran sets al doble de velocidad que uno.

---

## 15. Qué hacer HOY, en orden

| # | Acción | Por qué | Bloqueante |
|---|---|---|---|
| **1** | **Jugar la campaña de Lord of Hatred hasta "Last of the Horadrim"** | Sin eso **no hay Talismán** y no cae ni un charm. Está al principio, antes de embarcar a Temis | ⛔ **Todo lo demás depende de esto** |
| **2** | Equipar el Sello y el Charm que da Lorath | Arranca el sistema | — |
| **3** | Seguir la campaña hasta desbloquear el **Cubo Horádrico en Temis** | Sin Cubo no hay "Reroll Set Charm" y cerrar un 5-set es cuestión de suerte pura | ⛔ Bloquea el paso 6 |
| **4** | Conseguir un **Sello Legendario** y buscar el afijo **"+1 Charm Slot"** → **6 ranuras** | Es el objetivo intermedio realista. Recomendación explícita de Icy Veins | — |
| **5** | Subir a **Torment 3** en cuanto aguante | Es donde los Set Charms empiezan a caer con frecuencia | — |
| **6** | **Recoger TODOS los Set Charms de Nigromante que caigan** — de Waking Touch y de Black Shroud | La comparación entre ambos **no está resuelta** (§9). Los duplicados se convierten en piezas que faltan con el Cubo | Necesita paso 3 |
| **7** | **Comprobar en el juego el tooltip de Red Blessing** si le cae | Hay **conflicto de datos** (§11.1). Es un vistazo de 5 segundos que cierra un agujero real | — |
| **8** | Buscar **Pact of Bone** como Charm Único | 📦 Es el único de Nigromante más directo para esbirros (+15–25% daño de esbirros) y **ninguna guía lo menciona** | — |
| **9** | Preguntar a la pareja si tiene Lord of Hatred | Cambia por completo la estrategia de farmeo compartido (§14) | — |
| **10** | Objetivo de temporada: **Seal of the Diamond Mind** (Torment 10+) | 5-set con 4 charms → 2 ranuras libres. Es el techo del sistema | Necesita mucho empuje |

### 15.1 La prueba que zanja el debate del set (paso 6, ampliado)

Cuando tenga **4 piezas de un set** (o 5), en el **maniquí de entrenamiento**:
1. Equipar los 5 de **Rathma's Waking Touch**, anotar DPS con Ejército de los Muertos activo y sin él.
2. Equipar los 5 de **Peace of the Black Shroud**, repetir.
3. Comparar.

Es la única forma honesta de resolverlo, porque **nadie ha publicado esa comparación**. Y encaja con la regla que ya tiene interiorizada: **la pantalla del jugador gana**.

---

## Fuentes

**Oficiales de Blizzard**
- https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes — Notas del parche 3.1.0, build 72592, 30/06/2026. Cambios a Golden Epiphany, Severed Finger, Diamond Mind, Red Blessing, Art of the Bone Weaver, Radament's Desecration, Word of the Blood Binder, Mace of King Leoric, The Gloom Ward
- https://news.blizzard.com/en-us/article/24271857/diablo-iv-patch-notes-3-0 — Notas 3.0 (lanzamiento de Lord of Hatred); intercambio de Charms/Sellos no míticos
- https://diablo4.blizzard.com/en-us/lord-of-hatred — Página oficial de la expansión; requisitos, Paladín y Brujo, Skovos, "equip set bonuses with the new Talisman"
- https://us.forums.blizzard.com/en/d4/t/potential-bug-allow-charms-in-trade-window/247489 — Foro oficial: bug de la ventana de intercambio de Charms

**Datamining (declarado como tal)**
- https://assets-ng.maxroll.gg/d4-tools/game/data.min.json — Fichero de datos del juego que sirve el planificador de Maxroll. `version` = **3.1.0.72698**. De aquí salen: `itemSets` (45 sets), `items` (365 Charms, 12 Sellos), `affixes`, `skills`, `skillTags`, `itemTypes`, `attributes` (id 829 = `Talisman_Charm_Slot_Count_Base`)

**Preferentes**
- https://maxroll.gg/d4/resources/talisman-charms-sets — Recurso de Talismán. Requisito de expansión, desbloqueo, recetas del Cubo, ~4% Afijos Superiores en reroll
- https://maxroll.gg/d4/build-guides/minion-necromancer-guide — Guía de Nigromante de esbirros, **actualizada 22/07/2026, S14 Death Awakening**. Black Shroud, 6 ranuras, afijos de charm
- https://www.icy-veins.com/d4/guides/talisman-system-overview/ — Visión general del Talismán, **actualizada 28/06/2026**. Tabla de rarezas de Sello y ranuras
- https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/ — Reaper Summoner S14, **actualizada 27/06/2026**. Sello Legendario +1 ranura, orden de charms únicos, Diamond Mind como chase
- https://www.icy-veins.com/d4/news/diablo-4-3-1-3-patch-notes-easier-season-objectives-and-echo-of-mephisto-portal-fix/ — Notas 3.1.3
- https://www.wowhead.com/diablo-4/item/ber%C3%BA-of-the-black-shroud-2426839 — Berú of the Black Shroud: Set Charm, Nigromante, nivel 70, poder de objeto 850

**Secundarias (usadas y marcadas como tales)**
- https://game8.co/games/Diablo-4/archives/598000 — Talismanes de Nigromante. **Corroboración independiente** de los números de Rathma's Waking Touch y Peace of the Black Shroud; Torment 3 para Set Charms
- https://timesaver.gg/blog/diablo-4-mythic-seals-3-unique-charms-season-14 — Sellos míticos y farmeo. **Contiene datos muertos** (Golden Epiphany con 4 ranuras, Severed Finger vivo)
- https://www.purediablo.com/diablo4/Ber%C3%BA_of_the_Black_Shroud_-_Charm — Ficha del charm (vía búsqueda)

**Búsquedas realizadas (14):** talisman charms slots unlock · LoH talisman charm sets · "Beru of the Black Shroud" · "Red Blessing" charm set bonus · Necro minion S14 charms talisman · blizzard 3.1.3 charm seal talisman · patch 3.1.3 build 73224 · farm charms seals Horadric Cube · patch 3.1.1/3.1.2 necro talisman · reddit Rathma vs Black Shroud · talisman requires expansion · charms tradeable co-op · "Last of the Horadrim" Temis · Undercity War Plans farm charms

**Fuentes vetadas — respetadas:** no se ha tomado ningún efecto ni número de fextralife, primagames, beebom, gamespot, segmentnext, studioloot, gamerguides, pcgamesn ni mythicdrop. Aparecen en resultados de búsqueda pero **no se han abierto ni citado como fuente de datos**.

**Fetches fallidos:** mobalytics.gg (HTTP 403 en `/patch-3-1-3-changes-and-fixes` y `/patch-notes-3-1-1-season-14`) — su contenido solo ha llegado por resumen de búsqueda, marcado como tal. d4builds.gg no devolvió resultados útiles en las búsquedas.

---

## No encontrado

Huecos declarados. **Ninguno de estos se ha rellenado por inferencia.**

### Conflictos de datos sin resolver
1. **Red Blessing como Charm: 2 o 4 de Sobrepoder máximo.** El afijo del objeto dice 2 (coherente con el nerf oficial de 3.1.0); el afijo del charm dice 4 y 15–25% por acumulación. No sé si es tuneo aparte o un afijo sin parchear. **Se resuelve mirando el tooltip en el juego.**
2. **Cuál de los dos sets gana en DPS real para esta build**, Rathma's Waking Touch o Peace of the Black Shroud. **No existe ninguna comparación numérica publicada** en las fuentes preferentes ni en las secundarias.

### Datos que no he encontrado escritos en ninguna parte
3. **Cuántos afijos lleva exactamente cada Charm** por rareza, y si se pueden **templar (temper) o mejorar (masterwork)**. Maxroll e Icy Veins no lo concretan.
4. **Ranuras del Ancestral Horadric Seal y del Mythic Unique Horadric Seal genérico.** En los datos no llevan el atributo 829; solo los tres míticos con nombre lo tienen (6).
5. **Valores numéricos de los afijos de Sello específicos de set** (`+X% Minion Damage`, `+X a Skeleton Mage`). Están definidos por fórmula interna, no por rango fijo, y no puedo resolverlos.
6. **Valores de los sets genéricos** Slaughter, Practiced Technique y Mastery (`Affix_Value_1/2` sin resolver). Solo Survival y Dark Pact tienen números planos.
7. **El tipo de daño exacto de los Guerreros Segadores y de Ejército de los Muertos.** Sin esto no puedo decir si se benefician del 175%[x] de Sombra y Frío de Black Shroud.
8. **Si los Charms y Sellos Míticos son intercambiables.** 3.0 solo confirma que los **no** míticos sí. Lo contrario es la suposición razonable, pero **no está escrito**.
9. **Si un jugador sin Lord of Hatred puede jugar en grupo** con uno que sí la tiene, y con qué limitaciones de zona o de contenido.
10. **Diferencias entre PC y PS5** en el sistema de Talismán. No he encontrado ninguna mención; probablemente no las haya, pero no lo he verificado.
11. **Probabilidades de caída reales** de Set Charms, Charms Únicos y Sellos Míticos. Blizzard no las publica; los umbrales de Torment de §13 son de webs de boosting.
12. **El nombre en español** de los sets, sellos y charms. Todos los datos consultados están en inglés; las traducciones de este informe son mías y **el jugador verá los nombres en inglés o en la traducción oficial, que puede diferir**.
13. **Contenido de los parches 3.1.2 y de cualquier hotfix entre 3.1.1 y 3.1.3.** No encontré notas de 3.1.2; asumo que no tocó Charms, pero **no lo he verificado**.
14. **Reddit** (r/diablo4, r/Diablo4Necromancer): las búsquedas no devolvieron ningún hilo utilizable sobre Talismán o comparativa de sets. Sigue siendo un fallo de esta vía, igual que en pasadas anteriores.
