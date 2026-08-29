# Runas y Palabras Rúnicas (Runes & Runewords) — estado real en el parche 3.1.3

> Investigación cerrada el **19 de agosto de 2026**. Diablo IV, Temporada 14 "Death Awakening"
> (Despertar de la Muerte), parche vivo **3.1.3** (build 73224, 12 ago 2026).
> Jugador objetivo: **Nigromante de esbirros, nivel 70, con Vessel of Hatred Y Lord of Hatred
> recién compradas**, dúo PC + PS5, min-max, en español.
>
> **Regla de esta investigación:** cada número lleva su URL. Lo que no he visto escrito en una
> fuente viva va a `## No encontrado`. **No hay ni un solo valor reconstruido.** Cuando algo es
> deducción mía, lo digo *en la misma línea* que el dato.
>
> 🆕 = lo que el jugador **acaba de desbloquear hoy** al comprar las expansiones.

---

## 0. Resumen ejecutivo — si no lees nada más, lee esto

1. 🆕 **Las runas son 100% contenido de expansión.** Sin *Vessel of Hatred* no existen: ni caen, ni
   se pueden engarzar. Hoy el jugador acaba de desbloquear el sistema entero.
   ([maxroll.gg](https://maxroll.gg/d4/resources/runewords-overview) — *"Runes are exclusive to the
   Vessel of Hatred expansion"* / *"can only drop if the player has the Vessel of Hatred expansion"*;
   [icy-veins.com](https://www.icy-veins.com/d4/guides/runewords-guide/) — *"Runewords are only
   available to players who have purchased the Vessel of Hatred expansion"*)
2. ⚠️ **La premisa del encargo es medio falsa.** Teb y Wat existen y funcionan tal como se dice,
   **pero NINGUNA guía viva de nigromante de ESBIRROS de la S14 los usa.** Teb/Wat aparecen en las
   guías de **Sever** y de **Reaper/Naz Mages** (summoner de sombra), no en la de esbirros pura.
   La build de esbirros de Maxroll (planificador con fecha **22 jul 2026**) monta
   **Nagu + Ceh** y **Igni + Ceh / Nagu + Que / Igni + Gar**. Detalle y pruebas en §7.
3. 🚨 **La runa "obvia" para esbirros ya NO EXISTE.** `Ur` ("tu esbirro mata a un enemigo o muere")
   fue **eliminada del juego**. Confirmado por escrito en las notas del 3.1.0:
   *"Fixed an issue where the removed Ur rune was still required to craft Yul runes"* y
   *"Fixed an issue where Ur runes could still drop from Duriel's Cache"*
   ([maxroll.gg 3.1.0](https://maxroll.gg/d4/news/diablo-4-3-1-0-patch-notes)).
   Sigue apareciendo en el fichero de datos del juego y en tres bases de datos web. **Es un fantasma.**
4. **Huecos: 2 en Casco, 2 en Pecho, 2 en Piernas, 2 en Arma a Dos Manos.** Anillos y amuleto
   tienen 1 (solo gemas). Máximo **2 palabras rúnicas por personaje = 4 runas**. §4.
5. **Las guías de referencia publican números muertos del 3.1.0.** Tanto Maxroll como Icy Veins
   siguen mostrando `Vex` a 100 de Ofrenda cuando el parche 3.1.0 la subió a **300**. §12.
6. **Lo que hace HOY**: §7.3 y el bloque de acción al final.

---

## 1. ✅ / 🔒 — ¿qué necesitas comprar?

| Elemento | Base | VoH | LoH | Fuente |
|---|:--:|:--:|:--:|---|
| Sistema de Runas y Palabras Rúnicas | 🔒 | 🆕 ✅ | — | [maxroll](https://maxroll.gg/d4/resources/runewords-overview), [icy-veins](https://www.icy-veins.com/d4/guides/runewords-guide/) |
| Que te caigan runas del suelo | 🔒 | 🆕 ✅ | — | [maxroll](https://maxroll.gg/d4/resources/runewords-overview) |
| Hueco extra en el Casco (el que permite runa en casco) | 🔒 | 🆕 ✅ | — | [Blizzard 2.0](https://news.blizzard.com/en-us/diablo4/24130178/the-2-0-ptr-what-you-need-to-know) |
| Ciudad Baja de Kurast (Kurast Undercity) como granja de runas | 🔒 | 🆕 ✅ | — | [maxroll](https://maxroll.gg/d4/resources/runewords-overview), [icy-veins](https://www.icy-veins.com/d4/guides/runewords-guide/) |
| Ciudadela Oscura (Dark Citadel) | 🔒 | 🆕 ✅ | — | [icy-veins](https://www.icy-veins.com/d4/guides/dark-citadel-guide/) |
| Runas de Paladín y Brujo (Kel, Zid, Prid, Obr) | 🔒 | ❓ | 🆕 | ver `## No encontrado` |
| Rediseño de runas ("menos morralla") | ✅ gratis | — | — | [icy-veins](https://www.icy-veins.com/d4/news/diablo-4-lord-of-hatred-rune-changes/) (es un parche, no contenido de pago) |

**Traducción práctica:** hasta hoy este jugador tenía el sistema de runas **completamente vacío**.
Hoy le caen runas por primera vez. Todo lo de este documento es nuevo para él.

---

## 2. Cómo funciona el sistema (el modelo, no solo los números)

### 2.1 Las dos mitades

Una **palabra rúnica (Runeword)** = **1 Runa de Ritual** + **1 Runa de Invocación**, engarzadas
**en la misma pieza** ([maxroll](https://maxroll.gg/d4/resources/runewords-overview)).

- **Runa de Ritual (Rune of Ritual)** = la **causa**. Te pone una condición; al cumplirla genera
  **Ofrenda**. Símbolo **amarillo** en el icono.
  Texto oficial de Blizzard: *"Runes of Ritual specify actions you must take to trigger them"*
  ([news.blizzard.com, 4 sep 2024](https://news.blizzard.com/en-us/diablo4/24130178/the-2-0-ptr-what-you-need-to-know)).
- **Runa de Invocación (Rune of Invocation)** = el **efecto**. Consume la Ofrenda acumulada y
  dispara el efecto. Símbolo **morado**.
  *"Runes of Invocation grant a powerful effect when you meet said trigger"* (misma fuente oficial).

### 2.2 La Ofrenda (Offering) — qué es exactamente

**La Ofrenda es un recurso invisible propio de cada palabra rúnica.** No es maná ni esencia: es un
contador que sube cuando cumples la condición de la Runa de Ritual y se **gasta entero** cuando
llega al umbral de la Runa de Invocación.

- *"Runes work off a resource system called Offering, which is generated by Runes of Ritual upon
  meeting their listed condition. Runes of Invocation consume this Offering to activate their
  effects"* ([Blizzard oficial](https://news.blizzard.com/en-us/diablo4/24130178/the-2-0-ptr-what-you-need-to-know)).
- *"The more demanding of a requirement, the more Offering the Rune of Ritual will generate"*
  (misma fuente). Por eso `Noc` da 5 y `Cir` da 300: cumplir `Cir` es mucho más caro.
- **Dónde se ve:** *"You can monitor Offering generation in your buff bar located above your skills.
  The icon itself will change in function of the Runeword you equipped. The purple hue on top of the
  icon indicates how much Offering has been generated so far"*
  ([icy-veins](https://www.icy-veins.com/d4/guides/runewords-guide/)). **El tinte morado sobre el
  icono es tu barra de Ofrenda.**

### 2.3 Desbordamiento (Overflow) — la parte que la gente ignora

Si tu Runa de Ritual genera **más** Ofrenda de la que pide la Runa de Invocación, el sobrante no se
tira: aplica un **bono adicional** propio de cada runa.

- *"The bonus applied is proportional to how much Overflow is acquired, so stack as much as you can!"*
  ([maxroll](https://maxroll.gg/d4/resources/runewords-overview)).
- Ejemplo real: `Teb` tiene desbordamiento **"Increase damage by 1% per Offering"** — cada punto de
  Ofrenda sobrante es +1% de daño de esa Doncella de Hierro invocada
  ([maxroll](https://maxroll.gg/d4/resources/runewords-overview); confirmado en el fichero de datos,
  campo `overflow` de `Rune_Effect_Necromancer_IronMaiden`, ver §5.4).

**Consecuencia de diseño (deducción mía, no una cita):** emparejar una Ritual "cara" con una
Invocación "barata" no es desperdicio — es lo que activa el desbordamiento. `Cir` (300) + `Gar` (25)
desborda 275 puntos cada vez.

### 2.4 La versión mejorada de tu propia clase — clave para el Nigromante

> *"Some runes even cast the improved version of the skill if you use a Rune that relates to your
> class, for example, the Enhanced War Cry for Barbarians. **If you equip your own class skill, you
> will always cast the best possible version in case you have skilled more points in your own talent
> tree.**"* — [icy-veins.com, Runewords (S14)](https://www.icy-veins.com/d4/guides/runewords-guide/)

Esto es lo que hace que **Teb y Wat sean distintos para un Nigromante que para cualquier otra clase**:
el resto de clases lanzan la versión base; el Nigromante lanza **su** versión, con sus puntos y
mejoras del árbol. Por eso los tooltips las llaman *Abhorrent Iron Maiden* y *Horrid Decrepify*.

⚠️ **Aviso de fiabilidad:** esta frase la firma Icy Veins, no Blizzard, y **no he encontrado una nota
oficial que la confirme**. Va en `## No encontrado`.

---

## 3. Cómo se engarzan y se sacan

| Cosa | Regla | Fuente |
|---|---|---|
| Cómo se pone | Arrastrar y soltar la runa sobre el hueco de la pieza | [icy-veins](https://www.icy-veins.com/d4/guides/runewords-guide/) |
| Hace falta | Pieza con **2 huecos**, 1 Ritual + 1 Invocación, **en la misma pieza** | [maxroll](https://maxroll.gg/d4/resources/runewords-overview) |
| Gemas y runas | **Incompatibles en la misma pieza**: o gemas, o runas | [maxroll](https://maxroll.gg/d4/resources/runewords-overview), [icy-veins](https://www.icy-veins.com/d4/guides/runewords-guide/) |
| No puedes repetir | Ni la misma runa dos veces en el personaje, ni dos Rituales o dos Invocaciones en la misma pieza | [maxroll](https://maxroll.gg/d4/resources/runewords-overview) |
| Recuperar runas | **"You get runes back for free when salvaging the item"** — al desguazar la pieza recuperas las runas gratis | [icy-veins, Summoner leveling (27 jun 2026)](https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/) |
| Almacenaje | Se apilan y van solas a la pestaña **"Engarzables" (Socketables)** | [maxroll](https://maxroll.gg/d4/resources/runewords-overview), [icy-veins](https://www.icy-veins.com/d4/guides/runewords-guide/) |
| Comercio | Las runas **son intercambiables** entre jugadores | [maxroll](https://maxroll.gg/d4/resources/runewords-overview) |

**Nota 3.0 (bug ya corregido, útil saberlo):** *"Fixed an issue where socketed Runes or Gems would be
lost when Recycling a Unique Item with the Horadric Cube"*
([Blizzard, notas 3.0, build #72271, 10 jun 2026](https://news.blizzard.com/en-us/article/24271857/diablo-iv-patch-notes-3-0)).

---

## 4. ⭐ Huecos de runa: cuántos y en qué piezas

Esta es una de las dos preguntas explícitas del encargo. **Respuesta cerrada, tres fuentes coinciden.**

| Pieza | Huecos | ¿Admite palabra rúnica? | Fuente |
|---|:--:|:--:|---|
| **Casco (Helm)** | **2** | ✅ Sí | [Blizzard](https://news.blizzard.com/en-us/diablo4/24130178/the-2-0-ptr-what-you-need-to-know) *"The Helm slot has also received an additional Socket"* |
| **Pecho (Chest)** | **2** | ✅ Sí | [Blizzard](https://news.blizzard.com/en-us/diablo4/24130178/the-2-0-ptr-what-you-need-to-know), [maxroll](https://maxroll.gg/d4/resources/runewords-overview) |
| **Piernas (Legs/Pants)** | **2** | ✅ Sí | ídem |
| **Arma a Dos Manos (2H)** | **2** | ✅ Sí | ídem |
| Anillo ×2 | **1** | ❌ No (solo gema) | Datos del planificador de Maxroll, build "Minion Endgame Necromancer" ([planners.maxroll.gg/profiles/d4/7xf3kf0h](https://planners.maxroll.gg/profiles/d4/7xf3kf0h), 22 jul 2026) |
| Amuleto | **1** | ❌ No (solo gema) | ídem |
| Guantes, Botas, Arma a 1 mano, Escudo/Foco | **0** en las builds vistas | ❌ | ídem — ver `## No encontrado` |

**Límite duro del personaje:**
> *"A maximum of 2 Runewords can be equipped (4 Runes total)."* —
> [news.blizzard.com, 4 sep 2024](https://news.blizzard.com/en-us/diablo4/24130178/the-2-0-ptr-what-you-need-to-know)

Repetido por las dos guías vivas: *"you can only have two Runewords on a character"*
([maxroll](https://maxroll.gg/d4/resources/runewords-overview)) y *"You can only equip two Runewords
at a time"* ([icy-veins](https://www.icy-veins.com/d4/guides/runewords-guide/)).

### 4.1 ¿En qué DOS piezas ponerlas? (hay consenso, y es contraintuitivo)

Tienes 4 piezas candidatas pero solo 2 palabras rúnicas. Las dos guías de nigromante coinciden:
**deja el arma para las gemas.**

- Maxroll, guía de esbirros: *"Preferably, socket them into your **Armor pieces** as **Weapon Gems
  offer powerful multiplicative damage bonuses**"*
  ([maxroll, Minion Necromancer Leveling, 30 jun 2026](https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide)).
- Icy Veins, guía de invocador: *"Make sure you slot these in your **Helmet, Pants or Chest**, since
  Weapon allows you to use damage multiplier gems instead"*
  ([icy-veins, 27 jun 2026](https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/)).

En el planificador de la build de esbirros de Maxroll (22 jul 2026), el mandoble lleva
**2× Amatista Horádrica Impecable** en todas las variantes de endgame, y las runas van en **Casco +
Pecho** o **Casco + Piernas** ([planners.maxroll.gg/profiles/d4/7xf3kf0h](https://planners.maxroll.gg/profiles/d4/7xf3kf0h)).

---

## 5. La lista de runas — y por qué hay DOS listas que no cuadran

### 5.1 El problema, dicho claro

Hay tres inventarios de runas y **no coinciden**:

| Fuente | Rituales | Invocaciones | Total | Fecha |
|---|:--:|:--:|:--:|---|
| [maxroll, Runewords Overview](https://maxroll.gg/d4/resources/runewords-overview) — *"With 13 Runes of Ritual and 19 Runes of Invocation"* | 13 | 19 | **32** | 16 jul 2026 (changelog: "Updated for Lord of Hatred launch" 26 abr 2026) |
| [icy-veins, Runewords (S14)](https://www.icy-veins.com/d4/guides/runewords-guide/) | 15 | 19 | 34 | sin fecha visible |
| **Fichero de datos del juego** (datamining, ver §5.5) | 19 | 33 | **52** | build 3.1.0.72698 |

**Lo que sé con certeza documental:** el rediseño de *Lord of Hatred* **eliminó runas**:
> *"Blizzard has removed underutilized runes entirely. As a result, the remaining pool becomes more
> focused, and you are less likely to deal with drops that feel useless."*
> — [icy-veins, Lord of Hatred Rune Rework](https://www.icy-veins.com/d4/news/diablo-4-lord-of-hatred-rune-changes/)

**Ninguna fuente publica la lista de runas eliminadas.** Va a `## No encontrado`.
La única eliminación **confirmada por nombre** es `Ur` (§5.3).

**Cotejo independiente que apoya la lista de 32 (esto es razonamiento mío, no una cita):** la tabla
de "Rune Crafting" del Horadric Cubo de Maxroll tiene **exactamente 9 recetas**, una por cada runa
Legendaria (Bac, Igni, Tam, Yul / Eom, Jah, Ohm, Vex, Yom)
([maxroll, Crafting Cheat Sheet, 14 jul 2026](https://maxroll.gg/d4/resources/crafting-cheat-sheet)).
El fichero de datos tiene **13** runas Legendarias. Las 4 sobrantes (Ahu, Lith, Xol, Xan) no tienen
receta. Encaja con "fueron eliminadas", pero **no está escrito en ningún sitio**.

### 5.2 Runas de Ritual — las 13 que las guías dan por vivas

Rareza, valor de Ofrenda y texto: **fichero de datos del juego, build 3.1.0.72698** (datamining, §5.5).
La columna "coincide maxroll" indica si la cifra también aparece publicada en
[maxroll](https://maxroll.gg/d4/resources/runewords-overview).

| Runa | Rareza | Ofrenda | Condición (traducida) | ¿coincide maxroll? |
|---|---|---:|---|:--:|
| **Cem** | Mágica | 75 | Usar **Evadir** | ✅ 75 |
| **Cir** | Mágica | 300 | Lanzar 5 habilidades; luego quedas exhausto 3 s | ✅ 300 |
| **Moni** | Mágica | 100 | Lanzar 2 habilidades de Movilidad o Macabras | ✅ 100 |
| **Yax** | Mágica | 200 | Beberte una poción de curación | ✅ 200 |
| **Nagu** | Rara | 100 | Mantener ≥1 invocación viva 5 s, **ganando Ofrenda por cada una hasta 5** | ✅ 100 |
| **Neo** | Rara | 200 | Evitar daño a la vida mientras combates durante 2 s | ✅ 200 |
| **Noc** | Rara | 5 | Aplicar un control de masas; **el doble si no es Ralentizar ni Escalofrío** | ✅ 5 |
| **Poc** | Rara | 5 | Gastar 5% de tu recurso máximo | ✅ 5 |
| **Zan** | Rara | 200 | Lanzar una habilidad **Definitiva** | ✅ 200 (icy-veins dice 150 y "Mágica" ❌) |
| **Bac** | Legendaria | 50 | Recorrer 5 metros | ✅ 50 |
| **Igni** | Legendaria | 25 | **Almacena Ofrenda cada 0,3 s**; al lanzar una habilidad No Básica recibes lo almacenado (**máx. 500**) | ✅ 25 |
| **Tam** | Legendaria | 25 | Lanzar una habilidad **Principal** no canalizada | ✅ 25 |
| **Yul** | Legendaria | 50 | Lanzar una habilidad con tiempo de reutilización | ✅ 50 |

### 5.3 Runas de Invocación — las 19 que las guías dan por vivas

`CD` = tiempo de reutilización interno de la runa. `Desbordamiento` = bono al exceder la Ofrenda.
Todo del fichero de datos 3.1.0.72698 salvo donde se indique.

| Runa | Rareza | Ofrenda | CD | Efecto (traducido) | Desbordamiento |
|---|---|---:|---:|---|---|
| **Ceh** | Mágica | 100 | 1 s | Invoca un **Lobo Espiritual** que ataca 8 s | Invocar varios lobos |
| **Gar** | Mágica | 25 | 1 s | +2% Prob. Crítico 5 s, hasta 10% | Acumular varias cargas |
| **Kry** | Mágica | 300 | 3 s | **Vórtice** del Espiritista: daño y atrae enemigos | Hasta +100% tamaño |
| **Ner** | Mágica | 600 | 6 s | **Ocultación** del Pícaro 5 s: Vel. Mov., Imparable y Sigilo | Más duración |
| **Prid** | Mágica | **500** | 3 s | **Prisión Oscura** del Brujo: ata enemigos 3 s | Más duración |
| **Qua** | Mágica | 50 | 1 s | +10% Vel. Movimiento 5 s, hasta 50% | Más duración |
| **🎯 Teb** | **Mágica** | **100** | **1 s** | **Invoca la Doncella de Hierro del Nigromante**: daño con el tiempo y contraataca el daño de los enemigos | **+1% daño por cada punto de Ofrenda** |
| **Tzic** | Mágica | 200 | 1 s | **Pisotón Conmocionante** del Espiritista: daño y Derriba | +1% daño por Ofrenda |
| **Kel** | Rara | 500 | 3 s | **Reagrupar** del Paladín: recurso y Vel. Mov. 8 s | Más recurso |
| **Lac** | Rara | 400 | 1 s | **Grito Desafiante** del Bárbaro: provoca y reduce daño recibido 3 s | Más duración |
| **Mot** | Rara | 150 | 1 s | 1 sombra del **Manto Oscuro** del Pícaro: reduce daño por sombra | Varias sombras |
| **Que** | Rara | 300 | 1 s | **Baluarte de Tierra** del Druida 3 s: te da Barrera | Más duración |
| **Thul** | Rara | 250 | 2 s | **Nova de Escarcha** del Hechicero: Congela | Hasta +100% tamaño |
| **🎯 Wat** | **Rara** | **100** | **1 s** | **Invoca la Decrepitud del Nigromante**: Debilita y Ralentiza | **Más duración** |
| **Eom** | Legendaria | 100 | 1 s | Reduce tus reutilizaciones activas 0,1 s | Aún más reducción |
| **Jah** | Legendaria | 350 | 3,5 s | Tu próximo Evadir se convierte en el **Teleport** del Hechicero | Guarda la Ofrenda sobrante |
| **Ohm** | Legendaria | 600 | 2 s | **Grito de Guerra** del Bárbaro: +7,5% daño 6 s | Más duración |
| **Vex** | Legendaria | **300** ⚠️ | 5 s | **+1 a todas las habilidades** 10 s | Más rangos, hasta **3** |
| **Yom** | Legendaria | 500 | 5 s | **Petrificar** del Druida: Aturde y **aumenta tu Daño Crítico contra ellos** ⚠️ | Más duración de Aturdimiento |

⚠️ **`Vex` 300 y `Yom` "Daño Crítico" son cambios del 3.1.0.** Maxroll e Icy Veins siguen publicando
los valores viejos (Vex 100; Yom "restaura 100 de recurso"). Los cambios están por escrito:
> *"**Vex** (+ to All Skills): Offering required increased from **100 to 300**."*
> *"**Prid** (Dark Prison): Cost increased from **250 to 500**."*
> *"**Ceh** (Spirit Wolves): No longer makes enemies Vulnerable. Chill amount reduced from 50% per
> leap to 10% per leap. **Maximum wolves reduced from 10 to 6**."*
> *"**Yom** — Previous: … Stunning enemies, restoring Primary Resource. Now: … Stunning enemies and
> increasing your Critical Strike Damage against them."*
> — [maxroll, notas del parche 3.1.0 (24 jun 2026)](https://maxroll.gg/d4/news/diablo-4-3-1-0-patch-notes)

### 5.4 Nombres de las palabras rúnicas

- Maxroll dice que el nombre es la **concatenación**: *"By placing Bac and Jah in the same item,
  you've created **BacJah**, a Runeword"* ([maxroll](https://maxroll.gg/d4/resources/runewords-overview)).
- El fichero de datos guarda además un **prefijo** por cada Ritual y un **sufijo** por cada
  Invocación (p. ej. `Igni` → *"Bomber"*, `Nagu` → *"Tyrannical"*, `Cir` → *"Lethargic"*,
  `Teb` → *"Retribution"*, `Wat` → *"Disdain"*, `Ceh` → *"Alpha Canid"*, `Que` → *"Fortress"*,
  `Gar` → *"Precision"*). **No he encontrado ninguna fuente escrita que explique para qué sirven
  esos prefijos/sufijos** → `## No encontrado`.

### 5.5 Sobre el datamining (declaración obligatoria)

Los valores marcados "fichero de datos" salen de
`https://assets-ng.maxroll.gg/d4-tools/game/data.min.json`, el fichero que sirve el planificador de
Maxroll. **Es datamining, no una fuente editorial.** Dos avisos:

1. **Va por detrás del parche vivo.** El campo `version` del fichero dice **`3.1.0.72698`**.
   El parche vivo es **3.1.3 build 73224**. Hay **tres hotfixes de diferencia**.
2. **Contiene entradas muertas.** El fichero sigue teniendo la runa `Ur` completa, con su icono,
   su rareza y su texto — y `Ur` **está eliminada del juego** desde antes del 3.1.0. Es la prueba
   de que este fichero incluye restos.

### 5.6 Las 20 runas fantasma — están en los datos, no en las guías vivas

**Estado: probablemente eliminadas en el rediseño de *Lord of Hatred*. Solo `Ur` está confirmada.**
No las busques, no las cuentes para tus planes.

| Tipo | Runa (rareza / Ofrenda) | Texto en el fichero de datos |
|---|---|---|
| Ritual | **Ur** (Mágica / 10) 🚨 **ELIMINACIÓN CONFIRMADA** | *"Tu Esbirro o Compañero mata a un enemigo o muere"* |
| Ritual | Feo (Rara / 1000) | Quedar Herido o bajo control de masas (CD 10 s) |
| Ritual | Kaa (Rara / 50) | Perder X% de tu Vida Máxima |
| Ritual | Ahu (Legendaria / 15) | Golpe de Suerte contra enemigos no Sanos |
| Ritual | Lith (Legendaria / 25) | Quedarte quieto mientras combates X s |
| Ritual | Xol (Legendaria / 150) | Invocar una habilidad de otra clase |
| Invocación | Lum (M/5), Met (M/100), Ono (M/25), Tal (M/30), Tec (M/50), Ton (M/20), Tun (M/25), Zid (M/25) | Recurso / Tierra Profanada del Nigromante / Rayos Danzantes / Enjambre / Terremoto / Meteoritos / Granadas / Lanza Bendita |
| Invocación | Chac (R/20), Obr (R/100), Qax (R/400), Xal (R/300), Zec (R/100) | Rayo / Brasa del Brujo / recurso→daño / +20% Vida Máx. / −CD de Definitiva |
| Invocación | Xan (Legendaria / 300) | Crítico y Sobrepoder garantizados en el próximo ataque |

🚨 **`Ur` duele especialmente**: era LA runa temática de esbirros ("tu esbirro mata o muere → 10 de
Ofrenda"). **Ya no existe.** Aparece todavía en [diablo4.life](https://diablo4.life/database/runes)
(52 runas), en [d4planner.io](https://d4planner.io/runes) (45 runas) y en la propia hoja de crafteo
de Maxroll. **Todas esas listas están muertas en ese punto.**

---

## 6. 🎯 Teb y Wat a fondo — la pregunta del encargo

### 6.1 Teb — "Retribution"

| Campo | Valor | Fuente |
|---|---|---|
| Tipo | Runa de **Invocación** | [maxroll](https://maxroll.gg/d4/resources/runewords-overview) |
| Rareza | **Mágica** (la más baja → la más fácil de conseguir) | fichero de datos 3.1.0.72698; coincide con [icy-veins](https://www.icy-veins.com/d4/guides/runewords-guide/) ("Teb — Magic") |
| Ofrenda | **100** | [maxroll](https://maxroll.gg/d4/resources/runewords-overview), [icy-veins](https://www.icy-veins.com/d4/guides/runewords-guide/), fichero de datos |
| Reutilización | **1 segundo** | [maxroll](https://maxroll.gg/d4/resources/runewords-overview) |
| Efecto | *"Invoke the Necromancer's **Abhorrent Iron Maiden**, dealing damage over time and counterattacking damage from enemies"* | [maxroll](https://maxroll.gg/d4/resources/runewords-overview) |
| Variante Icy Veins | *"…counterattacking damage from enemies **and Healing you when they die**"* | [icy-veins](https://www.icy-veins.com/d4/guides/runewords-guide/) — ⚠️ la parte de curación **no aparece** en Maxroll ni en el fichero de datos |
| Desbordamiento | **+1% de daño por cada punto de Ofrenda** sobrante | [maxroll](https://maxroll.gg/d4/resources/runewords-overview) |
| Uso como material | **3× Teb** entran en la receta de **Mítico de Arma a Dos Manos** (con 3× Igni, 3× Zan, 3× Chispa Resplandeciente y 5.000.000 de oro) | [maxroll, Crafting Cheat Sheet, 14 jul 2026](https://maxroll.gg/d4/resources/crafting-cheat-sheet) |

**¿"Automatiza la Doncella de Hierro"?** Sí, en el sentido de que la lanza sin ocupar hueco de barra:
> *"Teb Rune automates Iron Maiden application and casts the skill **as if you cast it, without it
> needing to be on your Skillbar**"* — resultado de búsqueda que apunta a las guías de nigromante de
> Maxroll; **no pude abrir la página que lo firma**, así que lo dejo como indicio, no como dato.

### 6.2 Wat — "Disdain"

| Campo | Valor | Fuente |
|---|---|---|
| Tipo | Runa de **Invocación** | [maxroll](https://maxroll.gg/d4/resources/runewords-overview) |
| Rareza | **Rara** | fichero de datos 3.1.0.72698; coincide con [icy-veins](https://www.icy-veins.com/d4/guides/runewords-guide/) ("Wat — Rare") |
| Ofrenda | **100** | [maxroll](https://maxroll.gg/d4/resources/runewords-overview), [icy-veins](https://www.icy-veins.com/d4/guides/runewords-guide/) |
| Reutilización | **1 segundo** | [maxroll](https://maxroll.gg/d4/resources/runewords-overview) |
| Efecto | *"Invoke the Necromancer's **Horrid Decrepify**, Weakening and Slowing enemies"* | [maxroll](https://maxroll.gg/d4/resources/runewords-overview) |
| Variante Icy Veins | *"…Slowing enemies, reducing their damage, **and letting you Execute them**"* | [icy-veins](https://www.icy-veins.com/d4/guides/runewords-guide/) — ⚠️ el "Ejecutar" **no aparece** en Maxroll ni en el fichero de datos |
| Desbordamiento | **Más duración** | [maxroll](https://maxroll.gg/d4/resources/runewords-overview) |
| Uso como material | **3× Wat** entran en la receta de **Mítico de Piernas** (con 3× Ohm, 3× Cem, 3× Chispa Resplandeciente y 5.000.000 de oro) | [maxroll, Crafting Cheat Sheet](https://maxroll.gg/d4/resources/crafting-cheat-sheet) |

### 6.3 El emparejamiento que TODAS las guías de nigromante repiten: **Igni + Wat**

> *"**Igni + Wat** — Applies Decrepify automatically along skills **once every 1.2 seconds**,
> allowing you to invest in Decrepify upgrades **without requiring the skill on your action bar**."*
> — [icy-veins, Summoner Necromancer Leveling (27 jun 2026)](https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/)

**Este es el número más verificable de todo el informe, y cuadra solo.** `Igni` almacena 25 de
Ofrenda cada 0,3 s ([maxroll](https://maxroll.gg/d4/resources/runewords-overview)); `Wat` pide 100.
100 ÷ 25 = 4 tramos × 0,3 s = **1,2 s**. La cifra publicada por Icy Veins y el modelo del fichero de
datos **se validan mutuamente**. (Aritmética mía sobre dos datos publicados; no es un valor nuevo.)

Con `Teb` (también 100 de Ofrenda) el ritmo sería idéntico — **pero eso ya es cuenta mía, no está
escrito en ningún sitio**.

Repetido, en guías de nigromante distintas:
- *"**Igni + Wat** — Endgame Important — Invokes the Necromancer's Decrepify."*
  ([icy-veins, Naz Mages Summoner, 27 jun 2026](https://www.icy-veins.com/d4/guides/mendeln-summoner-necromancer-build/))
- *"**Igni + Wat** — Endgame Important — Applies Decrepify curse early when we cast Blight to start
  Bone Storm cooldown reduction."* — en el **Casco**
  ([icy-veins, Reaper Summoner, 3 jul 2026](https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/))
- *"While Blood Moon Breeches can be triggered by your Minions, **the combo of Teb/Wat runes make for
  better Curse uptime and more consistent automation of the build**."* y, en el equipo inicial,
  *"**Cir** and **Teb**… automate Curse application to save room on your Skillbar"*
  ([maxroll, Sever Necromancer Endgame, 28 jul 2026](https://maxroll.gg/d4/build-guides/sever-necromancer-endgame-guide))

---

## 7. ⭐ Qué debe montar EXACTAMENTE un Nigromante de Esbirros

### 7.1 La evidencia dura: el planificador de la build de esbirros de Maxroll

Sacado del JSON del propio planificador, build **"Minion Endgame Necromancer"**, fecha del fichero
**2026-07-22**, nivel 70 ([planners.maxroll.gg/profiles/d4/7xf3kf0h](https://planners.maxroll.gg/profiles/d4/7xf3kf0h);
guía asociada: [maxroll, Minion Necromancer Endgame, 22 jul 2026](https://maxroll.gg/d4/build-guides/minion-necromancer-guide)).

| Variante de la build | Palabra rúnica 1 | Palabra rúnica 2 |
|---|---|---|
| Leveling | **Cir + Ceh** (Casco) | **Cem + Gar** (Pecho) |
| Starter | **Nagu + Ceh** (Casco) | **Cir + Que** (Piernas) |
| Mid Game | **Nagu + Ceh** (Casco: *The Undercrown*) | **Igni + Gar** (Piernas: *Blood Moon Breeches*) |
| **Warrior** (guerreros) | **Nagu + Que** (Casco: *The Undercrown*) | **Igni + Ceh** (Pecho) |
| **Mages** (magos) | **Nagu + Que** (Casco: *The Undercrown*) | **Igni + Ceh** (Pecho) |
| Zookeeper | **Igni + Gar** (Pecho) | **Nagu + Ceh** (Piernas: *Blood Moon Breeches*) |

🚨 **Ni un solo Teb. Ni un solo Wat. Ni una sola Ur.** En ninguna de las 6 variantes.

Y la guía de subida lo dice con palabras:
> *"The Minion Necromancer focuses on the following combos: **Best in Slot: Cir + Ceh** — Spawns
> wolves that deal damage and freeze enemies. **Cem + Gar** — Additional Crit Chance.
> **Alternative choices** (if you have access to higher level runes): **Que** — Earthen Bulwark helps
> with defense. **Igni** — Another good way of generating offering. **Tam** — We spam our core skill
> all the time. **Jah** — Allows you to go faster with free Teleport. **Nagu** — Incredible source of
> generating offering."*
> — [maxroll, Minion Necromancer Leveling (30 jun 2026)](https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide)

### 7.2 Por qué NO usan Teb/Wat en esbirros — la razón está escrita

> *"**Blood Moon Breeches** is your **Curse delivery system** as your minions constantly have the
> potential to apply both curses to any mob they hit."*
> — [maxroll, Minion Necromancer Endgame (22 jul 2026)](https://maxroll.gg/d4/build-guides/minion-necromancer-guide)

Es decir: en esbirros, **las maldiciones ya las reparten los propios esbirros** a través de las
piernas únicas *Blood Moon Breeches*. Gastar una de tus dos palabras rúnicas en Teb o Wat sería
pagar dos veces por lo mismo. En cambio, la build de **Sever** (sin esbirros que peguen) sí las
necesita, y ahí es donde Teb/Wat aparecen.

Nota adicional del 3.1.0, directamente relevante a las maldiciones:
> *"**Radament's Desecration**: The set bonus will no longer continuously reapply the Curses to
> enemies already Cursed. Developer's Note: **Manually Casting Iron Maiden or Decrepify will still
> reapply the Curse** and is unaffected by this change. **The Blood Moon Breeches Unique will also
> still reapply the Curse when it procs** and is unaffected by this change."*
> — [maxroll, notas 3.1.0](https://maxroll.gg/d4/news/diablo-4-3-1-0-patch-notes)
>
> ❓ **Si una maldición lanzada por Teb/Wat cuenta como "Manually Casting" o no, NO está escrito.**
> Va a `## No encontrado`.

### 7.3 La recomendación concreta para ESTE jugador

Su barra actual: Mago Esquelético, Guerrero Esquelético, Gólem, Tentáculos de Cadáver,
**Doncella de Hierro**, Ejército de los Muertos. Tiene **Coven, Master of Puppets, Gravebloom,
Unyielding Commander, Schadenfreude**. Sobre eso:

**Objetivo (lo que dicen las guías vivas, sin adornos):**

| Prioridad | Palabra rúnica | Pieza | Por qué | Fuente |
|:--:|---|---|---|---|
| **1** | **Nagu + Ceh** | Casco | `Nagu` genera Ofrenda **solo por tener esbirros vivos, hasta 5** — es la runa de Ritual perfecta para él y no le pide cambiar nada de su forma de jugar. `Ceh` invoca lobos que además cuentan como invocaciones. | [planner Maxroll](https://planners.maxroll.gg/profiles/d4/7xf3kf0h), [maxroll leveling](https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide) |
| **2** | **Cir + Ceh** o **Cem + Gar** | Pecho | Lo que Maxroll marca como *Best in Slot* mientras no tengas runas Legendarias | [maxroll leveling](https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide) |
| **3** (endgame) | **Nagu + Que** + **Igni + Ceh** | Casco + Pecho | La configuración de las variantes Warrior/Mages, que son justo las suyas | [planner Maxroll](https://planners.maxroll.gg/profiles/d4/7xf3kf0h) |
| — | **Igni + Wat** | Casco/Pecho | **Solo si abandona la Doncella de Hierro de la barra**: le daría Decrepitud automática cada 1,2 s y liberaría un hueco de barra | [icy-veins summoner](https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/) |

**Aviso honesto (razonamiento mío, no cita):** él **ya lleva Doncella de Hierro en la barra**, así
que `Teb` le duplicaría algo que ya hace. `Wat` (Decrepitud) sí le añadiría **una segunda maldición
que hoy no tiene**, sin gastar hueco de barra. Pero **ninguna guía de esbirros de la S14 lo
recomienda**, y `Ceh`/`Que`/`Gar` sí. Si va a min-maxear, que copie el planificador; si quiere jugar
con dos maldiciones por gusto, `Igni + Wat` es la opción defendible.

### 7.4 Ojo con Ceh: fue nerfeada en el 3.1.0

`Ceh` es la runa que todas las builds de esbirros montan, y el 3.1.0 le metió mano:
**ya no aplica Vulnerable**, el Escalofrío bajó de **50% a 10% por salto**, y el máximo de lobos
bajó de **10 a 6** ([maxroll, notas 3.1.0](https://maxroll.gg/d4/news/diablo-4-3-1-0-patch-notes)).
Sigue siendo lo que montan las guías **después** del nerfeo (planificador del 22 jul, parche del
24 jun), así que la recomendación es post-nerfeo. ✅

---

## 8. Dónde se consiguen las runas

### 8.1 Fuentes de caída — lo que está escrito

| Fuente | Detalle | Quién lo dice | Confianza |
|---|---|---|---|
| **Ciudad Baja de Kurast (Kurast Undercity)** | Con el **Tributo de Armonía (Tribute of Harmony)** | [maxroll](https://maxroll.gg/d4/resources/runewords-overview) | Alta — dos fuentes |
| Ciudad Baja de Kurast | *"especially if you use the appropriate Tribute"* | [icy-veins](https://www.icy-veins.com/d4/guides/runewords-guide/) | Alta |
| **Jefes de Guarida (Lair Bosses)** | *"Killing Lair Bosses such as **Grigoire, Lord Zir, Varshan or The Beast in Ice** is also an excellent way to procure yourself the more rare **Legendary Runes**"* | [icy-veins](https://www.icy-veins.com/d4/guides/runewords-guide/) | Alta — corroborado por notas de parche (ver 8.2) |
| **Jefes del Mundo (World Bosses)** | — | [maxroll](https://maxroll.gg/d4/resources/runewords-overview) | Media — una fuente |
| **Cofres de Marea Infernal (Helltide Chests)** | — | [maxroll](https://maxroll.gg/d4/resources/runewords-overview) | Media |
| **Recompensas del Árbol de los Susurros** | — | [maxroll](https://maxroll.gg/d4/resources/runewords-overview) | Media |
| **Alijo de Duriel (Duriel's Cache)** | Confirmado indirectamente: el 3.1.0 arregla *"an issue where **Ur runes could still drop from Duriel's Cache**"* | [maxroll 3.1.0](https://maxroll.gg/d4/news/diablo-4-3-1-0-patch-notes) | Alta (implícita) |
| Monstruos en general | *"Runes of any rarity can be acquired throughout Sanctuary as a monster drop"* | [Blizzard, 4 sep 2024](https://news.blizzard.com/en-us/diablo4/24130178/the-2-0-ptr-what-you-need-to-know) | Oficial pero **de 2024** |
| **Ciudadela Oscura (Dark Citadel)** | ❌ **NO confirmado.** La guía viva de S14 de la Ciudadela **no menciona runas** en sus recompensas (Monedas de la Ciudadela + alijo semanal) | [icy-veins, Dark Citadel (S14)](https://www.icy-veins.com/d4/guides/dark-citadel-guide/) | → `## No encontrado` |
| **El Foso (The Pit)** | ❌ **NO confirmado** por ninguna fuente viva | — | → `## No encontrado` |

### 8.2 🆕 Nodos de **Planes de Guerra (War Plans)** que suben runas — lo más accionable del informe

Los **Planes de Guerra** son el sistema de modificadores de actividad de la temporada. Dos nodos
tocan runas directamente. Fuente: **fichero de datos 3.1.0.72698** (datamining), corroborados por
notas de parche donde se indica.

| Actividad | Nodo | Texto | Corroboración |
|---|---|---|---|
| **Jefes de Guarida** | **"Lair of Runes"** (`Warplans_BossLair_4`) | *"Lair Bosses have +1 Monster Power. **Lair Bosses have a higher chance of dropping specific Runes.**"* | ✅ Citado en las notas del 3.0.2: *"Fixed an issue where **Belial's Lair of Runes rune pool** was reducing the drop chance of non-legendary runes below Torment 6"* ([maxroll 3.0.2](https://maxroll.gg/d4/news/lord-of-hatred-3-0-2-patch-notes)) |
| **Ciudad Baja** | **"Bauble Day"** (`Warplans_Undercity_5`) | *"If you slay a **Portal Prankster** within the Undercity, the **Cabochon Merchant** will appear after killing the District Boss. The Cabochon Merchant will **sell you Runes and Gems for Gold**."* | Solo datamining |
| Ciudad Baja | "Trials and Tributes" (`Warplans_Undercity_3`) | Por cada Portal Prankster que mates aparece un **Cofre de Tributo** tras el jefe de distrito; se abren ofreciendo un Tributo | Solo datamining |

**"Lair of Runes" es la palanca de farmeo dirigido**: es la única mecánica documentada que dice
"runas **específicas**". Y como está mencionada en unas notas oficiales de parche, **existe de
verdad**.

---

## 9. Crafteo de runas — subir de rareza y fabricar Míticos

Todo de [maxroll, Crafting Cheat Sheet, **14 jul 2026**](https://maxroll.gg/d4/resources/crafting-cheat-sheet)
salvo donde se indique.

### 9.1 Amalgamación (Horadric Cubo) — la ruta de rareza

| Entrada | Salida |
|---|---|
| **5× runas Mágicas cualesquiera** | 1× runa **Rara** aleatoria |
| **5× runas Raras cualesquiera** | 1× runa **Legendaria** aleatoria |

Esto es enorme para alguien que empieza hoy: **toda la basura mágica sube**.

### 9.2 Joyero — 3 iguales

| Entrada | Salida |
|---|---|
| 3× de una runa **Legendaria** concreta | 100% → 1 runa **Legendaria** aleatoria |
| 3× de una runa **Rara** concreta | 85% Rara / **15% Legendaria** |
| 3× de una runa **Mágica** concreta | 85% Mágica / **15% Rara** |

*"The Rune created while crafting is **guaranteed to be different** than the one used"*
([maxroll, Runewords Overview](https://maxroll.gg/d4/resources/runewords-overview)).

### 9.3 Horadric Cubo — recetas **dirigidas** de Legendarias (9 recetas)

Formato: **runa obtenida ← 1× runa semilla + 5× Raras cualesquiera + 5× Legendarias cualesquiera.**

| Obtienes | Semilla | Obtienes | Semilla |
|---|---|---|---|
| **Bac** | 1× Prid | **Jah** | 1× Cem |
| **Igni** ⭐ | 1× **Teb** | **Ohm** | 1× Qua |
| **Tam** | 1× Ner | **Vex** | 1× Gar |
| **Yul** | 1× ~~Ur~~ → **Moni** ⚠️ | **Yom** | 1× Kry |
| **Eom** | 1× Tzic | | |

⚠️ **La hoja de Maxroll está MUERTA en la fila de Yul**: sigue pidiendo `Ur`. Corrección oficial:
> *"Fixed an issue where the removed **Ur** rune was still required to craft **Yul** runes.
> **Developer's Note: Crafting a Yul Rune now requires Moni instead of Ur.**"*
> — [maxroll, notas 3.1.0](https://maxroll.gg/d4/news/diablo-4-3-1-0-patch-notes)

⭐ **Ruta directa para él**: `Igni` es la runa de Ritual estrella del endgame de esbirros y se
fabrica **con Teb de semilla**. Es decir: aunque no vaya a *usar* Teb, **le interesa guardarla**.

### 9.4 Míticos con runas (Joyero) — 3× Chispa + 3+3+3 runas + 5.000.000 de oro

| Mítico aleatorio de… | Runas |
|---|---|
| Arma a 1 mano | 3× Eom · 3× Lac · 3× Ceh |
| **Arma a 2 manos** | 3× Igni · 3× Zan · **3× Teb** |
| Amuleto | 3× Yul · 3× Noc · 3× Qua |
| Botas | 3× Vex · 3× Thul · 3× Kry |
| Pecho | 3× Yom · 3× Nagu · 3× Tzic |
| Guantes | 3× Bac · 3× Noc · 3× Moni |
| Casco | 3× Jah · 3× Que · 3× Gar |
| **Piernas** | 3× Ohm · **3× Wat** · 3× Cem |
| Anillo | 3× Tam · 3× Mot · 3× Yax |

⚠️ **Icy Veins publica una tabla de Míticos con runas completamente distinta** (1× Chispa + 10× de
tres runas, y usando runas fantasma como Ur, Lith, Kaa, Tun, Met). **Esa tabla está muerta**; ver §12.

---

## 10. Talismán y Transfiguración — dos interacciones con runas

🆕 Sistemas de *Lord of Hatred* / S14 que el jugador acaba de desbloquear.

| Cosa | Texto | Fuente |
|---|---|---|
| **Sello de Talismán (Seal)** | *"While **Vitality Charm** equipped, you gain **double Offering from Helm runes**."* | Fichero de datos 3.1.0.72698, afijo `Talisman_SealAffix_Normal_Vitality_01` — **datamining, sin confirmación editorial** |
| **Afijo de Transfiguración** | `X2_Transfiguration_IncreasedRuneOffering`, actúa sobre el atributo interno `Condition_Rune_Scalar` (= generación de Ofrenda) | Fichero de datos — **sin texto de tooltip legible**; ver `## No encontrado` |

Si el sello de Vitalidad funciona como dice el fichero, **duplicar la Ofrenda del casco cambia toda
la ecuación** (por ejemplo `Nagu` en el casco pasaría a generar el doble). **No lo he podido
verificar en ninguna guía.** No lo des por bueno hasta verlo en el tooltip del juego.

---

## 11. Cambios de parche que tocan runas (3.0 → 3.1.3)

| Parche | Cambio | Fuente |
|---|---|---|
| **3.0 (Lord of Hatred, 26 abr 2026)** | Rediseño: **se eliminan runas infrautilizadas**; todas las restantes caben en la pestaña Engarzables; las runas se integran en el **Horadric Cubo** | [icy-veins](https://www.icy-veins.com/d4/news/diablo-4-lord-of-hatred-rune-changes/) |
| 3.0.2 | Arreglado: el conjunto de runas de *Lair of Runes* de **Belial** reducía la caída de runas no legendarias por debajo de Tormento 6 | [maxroll 3.0.2](https://maxroll.gg/d4/news/lord-of-hatred-3-0-2-patch-notes) |
| 3.0.2 | Arreglado: la palabra rúnica **Lac** no funcionaba con Grito Desafiante y las nuevas variantes de habilidad | [maxroll 3.0.2](https://maxroll.gg/d4/news/lord-of-hatred-3-0-2-patch-notes) |
| 3.0.2 | Arreglado: la duración de Enjambre de Terror se reducía cuando los Lobos Espirituales venían de la runa **Ceh** | [maxroll 3.0.2](https://maxroll.gg/d4/news/lord-of-hatred-3-0-2-patch-notes) |
| 3.0.4 (10 jun 2026) | Arreglado: se perdían runas y gemas engarzadas al reciclar un único en el Horadric Cubo | [Blizzard 3.0](https://news.blizzard.com/en-us/article/24271857/diablo-iv-patch-notes-3-0) |
| **3.1.0 (S14, 24 jun 2026)** | **Ceh** nerfeada (sin Vulnerable, Escalofrío 50%→10%, lobos 10→6) · **Vex** 100→**300** Ofrenda · **Prid** 250→**500** · **Yom** cambia recurso por **Daño Crítico** · **Ur** ya no da runa para craftear Yul (ahora **Moni**) · Ur ya no cae del Alijo de Duriel · arreglado el apilamiento del bono de **Vex** | [maxroll 3.1.0](https://maxroll.gg/d4/news/diablo-4-3-1-0-patch-notes) |
| **3.1.3 (12 ago 2026)** | Arreglado: **Pisotón Conmocionante no otorgaba Resolución** con la mejora correspondiente **cuando lo disparaba la runa Tzic** | [icy-veins 3.1.3](https://www.icy-veins.com/d4/news/diablo-4-3-1-3-patch-notes-easier-season-objectives-and-echo-of-mephisto-portal-fix/) |

**Conclusión sobre el parche vivo:** el 3.1.3 **no cambia nada de runas relevante para un nigromante
de esbirros**. El parche que importa es el **3.1.0**.

---

## 12. 🚩 Fuentes muertas detectadas (para que no te las cuelen)

| Fuente | Fecha que muestra | Qué publica mal | Prueba |
|---|---|---|---|
| [maxroll, Runewords Overview](https://maxroll.gg/d4/resources/runewords-overview) | "Last Updated: July 16, 2026" | **Vex a 100** de Ofrenda, **Prid a 250**, **Yom "restoring 100 Resource"** | El 3.1.0 (24 jun) los cambió a 300 / 500 / Daño Crítico ([maxroll 3.1.0](https://maxroll.gg/d4/news/diablo-4-3-1-0-patch-notes)) |
| [maxroll, Crafting Cheat Sheet](https://maxroll.gg/d4/resources/crafting-cheat-sheet) | "Last Updated: July 14, 2026" | Receta de **Yul con Ur** | El 3.1.0 dice que ahora es **Moni** |
| [icy-veins, Runewords guide](https://www.icy-veins.com/d4/guides/runewords-guide/) | sin fecha visible | **Zan 150 y Mágica** (datos: 200, Rara) · **Noc 10** (datos: 5) · **Jah 250 / CD 2 s** (datos: 350 / 3,5 s) · **Thul 300** (datos: 250) · **Vex 100** · **Gar 2,5%→25%** (datos: 2%→10%) · **Nagu "hasta 6 invocaciones"** (datos: 5) · tabla de Míticos con runas **eliminadas** (Ur, Lith, Kaa, Tun, Met) y con la fórmula vieja de "1 Chispa + 10 runas" | Contradice al fichero de datos 3.1.0 y a la hoja de crafteo de Maxroll de julio 2026 |
| [diablo4.life/database/runes](https://diablo4.life/database/runes) | — | **52 runas**, incluida **Ur** | `Ur` está eliminada |
| [d4planner.io/runes](https://d4planner.io/runes) | — | **45 runas**, incluida **Ur**, sin las de Paladín/Brujo (Kel, Prid, Obr, Zid) ni Igni ni Nagu | Mezcla de dos épocas |
| [d4builds.gg](https://d4builds.gg/builds/minion-necromancer-endgame/) | "Season 1" | Página vacía servida por JavaScript; no publica datos legibles | Abierta y comprobada |

**Patrón:** las páginas *"resource/overview"* se actualizan menos que las *guías de build*. Cuando
choquen, **gana la guía de build con planificador fechado**, y por encima de todo **las notas de
parche**.

---

## 13. Dúo PC + PS5 — qué cambia

| Situación | Consecuencia | Fuente |
|---|---|---|
| **La pareja NO tiene Vessel of Hatred** | **Cero runas.** No le caen, no puede engarzarlas, no ve el sistema. Sus piezas de casco/pecho/piernas/mandoble solo aceptan gemas. | [maxroll](https://maxroll.gg/d4/resources/runewords-overview) — *"can only drop if the player has the Vessel of Hatred expansion"* |
| **La pareja NO tiene VoH y juegan juntos** | Él sí las recibe: es una condición **por cuenta**, no por grupo (así lo dice la frase "if the player has"). No he encontrado ninguna nota sobre reparto en grupo → `## No encontrado` | — |
| **La pareja SÍ tiene VoH** | Mismo sistema, mismos límites (2 palabras rúnicas). Las runas son **intercambiables** entre jugadores, así que pueden pasarse las que no usen | [maxroll](https://maxroll.gg/d4/resources/runewords-overview) |
| **PC vs PS5** | **No he encontrado ninguna diferencia** de runas entre plataformas en ninguna nota de parche ni guía | → `## No encontrado` |
| **Ciudadela Oscura** | 🆕 Requiere **mínimo 2 jugadores** (recomendado 4) y **la dificultad NO escala con el número de jugadores** | [icy-veins, Dark Citadel (S14)](https://www.icy-veins.com/d4/guides/dark-citadel-guide/) |

---

## 14. Lo que hace HOY, en orden

1. **Comprueba en el juego el hueco extra del casco.** Si tu casco tiene 2 huecos, el sistema está
   activo. (Blizzard: el hueco extra de casco llegó con el 2.0 / VoH.)
2. **Vacía la pestaña Engarzables**: mira qué runas ya tienes acumuladas. Es probable que tengas
   varias sin saberlo, porque caen de Susurros y Marea Infernal.
3. **Monta la primera palabra rúnica en el CASCO**: busca `Nagu` (Rara) + `Ceh` (Mágica).
   Si no tienes `Nagu`, usa `Cir` + `Ceh`. **No pongas runas en el mandoble** — ahí van gemas.
4. **Segunda palabra rúnica en el PECHO**: `Cem` + `Gar` (ambas Mágicas, las más fáciles).
5. **Amalgama toda la basura**: 5 Mágicas cualesquiera → 1 Rara; 5 Raras → 1 Legendaria
   (Horadric Cubo). Es la vía más rápida a `Igni` y `Nagu`.
6. **En Planes de Guerra, coge "Lair of Runes"** en el árbol de Jefes de Guarida antes de farmear
   jefes: es el único nodo documentado que sube runas **concretas**.
7. **No tires ningún Teb.** Aunque tu build no lo use, **1× Teb es la semilla para craftear `Igni`**,
   que sí es endgame de esbirros. Igual con `Gar` → `Vex`.
8. **Olvida `Ur`.** No existe. Si una guía te la recomienda, esa guía está muerta.
9. **Si la pareja no tiene la expansión**, no le hagas planes con runas: no las tiene ni las tendrá.

---

## Fuentes

Páginas realmente abiertas (WebFetch o descarga directa y lectura del HTML):

1. https://www.icy-veins.com/d4/guides/runewords-guide/ — *Runewords in Diablo 4 (Season 14)* (sin fecha visible)
2. https://maxroll.gg/d4/resources/runewords-overview — *Runewords Overview*, Last Updated **16 jul 2026**
3. https://maxroll.gg/d4/build-guides/minion-necromancer-guide — *Minion Necromancer Endgame*, **22 jul 2026**
4. https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide — *Minion Necromancer Leveling*, **30 jun 2026**
5. https://maxroll.gg/d4/build-guides/sever-necromancer-endgame-guide — *Sever Necromancer Endgame*, **28 jul 2026**
6. https://www.icy-veins.com/d4/guides/mendeln-summoner-necromancer-build/ — *Naz Mages Summoner*, **27 jun 2026**
7. https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/ — *Reaper Summoner*, **3 jul 2026**
8. https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/ — *Summoner Leveling*, **27 jun 2026**
9. https://www.icy-veins.com/d4/guides/dark-citadel-guide/ — *Dark Citadel Guide (Season 14)*
10. https://maxroll.gg/d4/news/diablo-4-3-1-0-patch-notes — *Notas del parche 3.1.0*, **24 jun 2026**
11. https://maxroll.gg/d4/news/lord-of-hatred-3-0-2-patch-notes — *Notas del parche 3.0.2*
12. https://news.blizzard.com/en-us/article/24271857/diablo-iv-patch-notes-3-0 — **oficial**, notas 3.0 (hotfixes 3.0.1–3.0.4)
13. https://news.blizzard.com/en-us/diablo4/24130178/the-2-0-ptr-what-you-need-to-know — **oficial**, 4 sep 2024 (definición del sistema)
14. https://www.icy-veins.com/d4/news/diablo-4-lord-of-hatred-rune-changes/ — *Lord of Hatred Rune Rework*
15. https://maxroll.gg/d4/resources/crafting-cheat-sheet — *Crafting Cheat Sheet*, **14 jul 2026**
16. https://planners.maxroll.gg/profiles/d4/7xf3kf0h — JSON del planificador, build *Minion Endgame Necromancer*, **2026-07-22**
17. https://assets-ng.maxroll.gg/d4-tools/game/data.min.json — **datamining**, `version = 3.1.0.72698`
18. https://diablo4.life/database/runes — base de datos (52 runas; **contiene entradas muertas**)
19. https://d4planner.io/runes — base de datos (45 runas; **contiene entradas muertas**)
20. https://d4builds.gg/builds/minion-necromancer-endgame/ — abierta, **sin datos legibles** (JS)
21. https://www.icy-veins.com/d4/news/diablo-4-3-1-3-patch-notes-easier-season-objectives-and-echo-of-mephisto-portal-fix/ — notas 3.1.3

Intentos fallidos (declarados): `mobalytics.gg` devuelve **HTTP 403** tanto a WebFetch como a
descarga directa; `wowhead.com/diablo-4/runes` devuelve **HTTP 403**;
`reddit.com/r/Diablo4Necromancer` no apareció en ningún resultado de búsqueda utilizable.

Fuentes vetadas: **no se ha usado** fextralife, primagames, beebom, gamespot, segmentnext,
studioloot, gamerguides, pcgamesn ni mythicdrop para ningún efecto ni número.

---

## No encontrado

Huecos declarados. **Prefiero esto a rellenarlos.**

1. **La lista de runas eliminadas en el rediseño de *Lord of Hatred*.** Icy Veins confirma que
   *"Blizzard has removed underutilized runes entirely"* pero **no nombra ni una**. Solo `Ur` está
   confirmada por nombre (notas 3.1.0). Las otras 19 candidatas de §5.6 son **sospechas basadas en
   ausencia**, no hechos.
2. **El número exacto de runas vivas hoy.** Maxroll dice 13+19=32, Icy Veins implica 34, el fichero
   de datos tiene 52. No hay fuente que lo cierre.
3. **Si `Ahu`, `Xol`, `Lith`, `Feo`, `Kaa`, `Xal`, `Zec`, `Met`, `Qax`, `Xan` (y las demás de §5.6)
   siguen cayendo.** No lo dice nadie.
4. **Si las runas de Paladín y Brujo (`Kel`, `Zid`, `Prid`, `Obr`) llegaron con *Lord of Hatred***
   o ya estaban. Nadie lo escribe; solo consta que `Prid` fue rebalanceada en el 3.1.0.
5. **Si `Teb`/`Wat` cuentan como "lanzamiento manual" de la maldición** a efectos de la nota de
   *Radament's Desecration* del 3.1.0. Es la diferencia entre reaplicar la maldición o no.
6. **Los números concretos de `Teb` y `Wat`**: cuánto daño hace la Doncella de Hierro invocada,
   cuánto Debilita/Ralentiza la Decrepitud, y cuántos segundos duran. **Ninguna fuente los publica**,
   y el fichero de datos solo trae el texto, no las tablas de potencia.
7. **Si la curación de `Teb`** (*"Healing you when they die"*, solo en Icy Veins) y el **Ejecutar de
   `Wat`** (*"letting you Execute them"*, solo en Icy Veins) están vivos. Ni Maxroll ni el fichero
   de datos los mencionan.
8. **Qué son exactamente los prefijos/sufijos** del fichero de datos (`Nagu`→"Tyrannical",
   `Teb`→"Retribution"…) y si aparecen en el nombre de la pieza en el juego.
9. **Si la Ciudadela Oscura suelta runas.** La guía viva de S14 de la Ciudadela **no lo dice**.
   El encargo lo daba por hecho; **no lo he podido confirmar**.
10. **Si el Foso (The Pit) suelta runas.** Ninguna fuente lo afirma.
11. **El texto en juego del sello de Talismán** *"double Offering from Helm runes"* y del afijo de
    Transfiguración `IncreasedRuneOffering`. Ambos salen **solo del datamining**, sin tooltip
    editorial que los respalde.
12. **Si guantes, botas, armas a una mano, escudos o focos pueden llevar huecos** (y cuántos).
    En las 6 variantes del planificador de esbirros **no llevan ninguno**, pero eso no es una regla
    escrita.
13. **Diferencias PC / PS5** en runas. Ninguna.
14. **Cómo se reparten las runas en grupo** (si el que no tiene VoH bloquea el botín del que sí).
15. **Cuánta Ofrenda genera `Nagu` en total con 5 invocaciones** (¿100 por cada una, o 100
    repartidos?). El texto dice *"gaining Offering for each up to 5 Summons"* pero **no da la cifra
    por invocación**.
16. **Nota metodológica**: el fichero de datos es de la build **3.1.0.72698**, tres hotfixes por
    detrás del parche vivo **3.1.3 build 73224**. Cualquier valor tomado de ahí puede haber cambiado
    en 3.1.1, 3.1.2 o 3.1.3 sin que yo lo sepa.
