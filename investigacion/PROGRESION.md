# PROGRESIÓN DEL NIGROMANTE — síntesis final

**Cerrado el 19 de agosto de 2026** · Diablo IV, Temporada 14 «Death Awakening» · parche vivo **3.1.3 (build #73224, 12 ago 2026)**
Rework de árboles: parche **3.0.0 / Lord of Hatred**, 28 abr 2026.
**Jugador:** principiante, Nigromante (*Necromancer*), **solo juego base** (sin *Vessel of Hatred*, sin *Lord of Hatred*), dúo PC + PS5, min-max, español.

Este documento sintetiza seis informes y sus cuatro refutaciones, **más una pasada nueva** cuya aportación principal es haber abierto y decodificado el **fichero de datos del propio juego** que usa el planificador de Maxroll. Ese fichero cierra huecos que ninguna guía web había cerrado.

---

## 0. Lo primero: la premisa del encargo es falsa, y ahora lo sé por el código del juego

El encargo ordenaba dar por sentado que **los clústeres se desbloquean por PUNTOS GASTADOS**, con 23 puntos para Definitivas y 33 para «Pasivas Definitivas».

**Eso no existe en el juego de hoy.** No es que «no lo haya encontrado»: he mirado dentro de la estructura de datos del árbol y **el campo de desbloqueo se llama literalmente `requiredLevel`**.

Descarga y verificación propias (19 ago 2026):

```
https://assets-ng.maxroll.gg/d4-tools/game/data.min.json   → HTTP 200, 11.606.292 bytes
version: "3.1.0.72698"
```

Recuento de campos de requisito en los 11,6 MB del fichero completo:

| Campo | Apariciones | Dónde vive |
|---|---:|---|
| `requiredLevel` | **2.409** | árboles de habilidades |
| `requiredRank` | 334 | **solo** en `paragonGlyphAffixes` (glifos de Paragón, nada que ver con el árbol) |
| cualquier campo de «puntos gastados» | **0** | — |

Búsqueda literal de claves tipo *points / spent* en todo el fichero: **cero coincidencias** (`"spent"` no aparece ni una vez; `"Point"` solo aparece en nombres de objeto como `SkillPointTome`).

Estructura real del árbol del Nigromante (259 nodos):

| Tipo de nodo | Cantidad | Qué es |
|---|---:|---|
| `reward.type = 0` | **23** | las 23 habilidades activas, `ranks: 15` cada una |
| `reward.type = 1` | **161** | nodos de modificador y de variante, `ranks: 3` cada uno |
| `root = 1` (sin recompensa) | **6** | **las seis puertas de clúster** |
| `root = 2` (sin recompensa) | 69 | las puertas de rama dentro de cada habilidad |

Los seis nodos `root: 1`, con su `requiredLevel` textual:

```
id  70  requiredLevel (ninguno)   → Básicas, abierto desde el principio
id 368  requiredLevel  3          → Fundamentales (Core)
id 381  requiredLevel  4          → Cadáver (Corpse)
id 370  requiredLevel  8          → Macabras (Macabre)
id 371  requiredLevel 13          → Maldiciones (Curse)
id 372  requiredLevel 19          → Definitivas (Ultimate)
```

**Conclusión dura: el gate es el nivel de personaje.** Los números 23 y 33 son del árbol anterior a 2025, documentados con fecha en https://game8.co/games/Diablo-4/archives/402759 (última actualización **13 oct 2024**, con nivel máximo 60, 71 puntos totales y Pasivas Clave que hoy no existen).

Y el clavo lógico: **no puede existir un «clúster de Pasivas Definitivas»**, porque Blizzard eliminó las pasivas del árbol — *«Passive nodes are no longer part of the skill tree, so you can concentrate points into Active skills. But fear not: many Passive and Key Passive nodes are moving to reimagined Legendary Aspects and Uniques instead»* (blog oficial de Blizzard, reproducido en https://www.icy-veins.com/d4/news/diablo-iv-lord-of-hatred-full-blog-post-now-available/).

> **Aviso honesto de método:** el fichero de datos es *datamining* servido por Maxroll, no una publicación de Blizzard. Es lo más cercano al juego que se puede alcanzar desde fuera, y coincide nodo a nodo con la tabla publicada por Maxroll y con los encabezados de Icy Veins (§1). Pero no es una fuente primaria de Blizzard, y **su versión es `3.1.0`, mientras el parche vivo es `3.1.3`**. El 3.1.3 solo trae un arreglo cosmético del Nigromante (*«Fixed an issue where Necromancer Shadow skills would obscure the Corrupted Reaper»*, https://www.icy-veins.com/d4/news/diablo-4-3-1-3-patch-notes-easier-season-objectives-and-echo-of-mephisto-portal-fix/), así que la deriva esperable es nula — pero no la puedo descartar.

---

## La tabla

**Entregable central.** La doy en las dos columnas porque el encargo pide puntos y el juego usa niveles. La columna de puntos es un **contador acumulado**, no un requisito: sirve si gastas cada punto al subir, que es lo que hace todo el mundo.

### A. La escalera completa de desbloqueos

Esta tabla la he obtenido **dos veces por vías independientes** y coincide dígito a dígito:

1. Del fichero de datos: `requiredLevel` de los nodos `root: 1` (clústeres) y `root: 2` (ramas), agrupados por clúster.
2. De la tabla publicada en https://www.maxroll.gg/d4/getting-started/skill-trees, citada literal: *«Skill | Level Unlock | A Modifiers | B Modifiers | Variant 1 & 2 | LoH Variant»*.

| Clúster | Habilidad se abre | Modificadores A | Modificadores B | Variantes 1 y 2 ✅ | 3.ª Variante 🔒 |
|---|---:|---:|---:|---:|---:|
| 1 · Básicas (*Basic*) | **nivel 1** | 5 | 9 | 14 | 30 |
| 2 · Fundamentales (*Core*) | **nivel 3** | 6 | 10 | 15 | 32 |
| 3 · Cadáver (*Corpse*) | **nivel 4** | 7 | 11 | 16 | 34 |
| 4 · Macabras (*Macabre*) | **nivel 8** | 12 | 17 | 20 | 36 |
| 5 · Maldiciones (*Curse*) | **nivel 13** | 18 | 21 | 23 | 38 |
| 6 · Definitivas (*Ultimate*) | **nivel 19** | 22 | 24 | 25 | 40 |

> **Aquí está el origen del «23».** El 23 es el **nivel** al que se abren los nodos de Variante del clúster de **Maldiciones**. No es un umbral de puntos y no es del clúster de Definitivas. Alguien lo leyó de una tabla como esta y lo convirtió en «23 puntos para Definitivas».

### B. La misma escalera, expresada en puntos acumulados

Válida **si gastas cada punto al subir**. Puntos que tienes al llegar al nivel N = **N − 1**.

| Puntos gastados (si gastas al subir) | Nivel equivalente | Qué se abre |
|---:|---:|---|
| 0 | 1 | Clúster **Básicas**. Todas las ranuras de la barra ya están abiertas |
| 2 | 3 | Clúster **Fundamentales** → aquí vive **Mago Esquelético** |
| 3 | 4 | Clúster **Cadáver** → aquí vive **Guerrero Esquelético** |
| 4 | 5 | 1.ª pareja de Modificadores de las Básicas · (Libro de los Muertos, ver §Libro) |
| 5 | 6 | 1.ª pareja de Modificadores de las Fundamentales |
| 6 | 7 | 1.ª pareja de Modificadores de Cadáver |
| 7 | **8** | Clúster **Macabras** → aquí vive el **Gólem** |
| 8 | 9 | 2.ª pareja de Modificadores de las Básicas |
| 9 | 10 | 2.ª pareja de Modificadores de las Fundamentales |
| 10 | 11 | 2.ª pareja de Modificadores de Cadáver |
| 11 | 12 | 1.ª pareja de Modificadores de Macabras |
| **12** | **13** | Clúster **Maldiciones** |
| 13 | 14 | **Variantes** de las Básicas |
| 14 | 15 | **Variantes** de las Fundamentales → *Coven* (+2 magos) |
| 15 | 16 | **Variantes** de Cadáver → *Master of Puppets* (+3 guerreros) |
| 16 | 17 | 2.ª pareja de Modificadores de Macabras |
| 17 | 18 | 1.ª pareja de Modificadores de Maldiciones |
| **18** | **19** | Clúster **Definitivas** |
| 19 | 20 | **Variantes** de Macabras → *Gravebloom* (3 gólems) |
| 20 | 21 | 2.ª pareja de Modificadores de Maldiciones |
| 21 | 22 | 1.ª pareja de Modificadores de Definitivas |
| 22 | 23 | **Variantes** de Maldiciones → *Schadenfreude* |
| 23 | 24 | 2.ª pareja de Modificadores de Definitivas |
| 24 | 25 | **Variantes** de Definitivas → *Unyielding Commander* |
| 29 | 30 | 3.ª Variante de las Básicas 🔒 |
| 31 | 32 | 3.ª Variante de las Fundamentales 🔒 |
| 33 | 34 | 3.ª Variante de Cadáver 🔒 |
| 35 | 36 | 3.ª Variante de Macabras 🔒 |
| 37 | 38 | 3.ª Variante de Maldiciones 🔒 |
| 39 | **40** | 3.ª Variante de Definitivas 🔒 — **a partir de aquí el árbol ya no abre nada más** |
| 68 | 70 | Nivel máximo |

**La diferencia práctica entre los dos modelos, y por qué te conviene:** con gate por nivel, **guardar puntos sin gastar no retrasa nada**. Si subes tres niveles sin tocar el árbol, los clústeres se abren igual. Con el modelo viejo de puntos gastados sí se habrían retrasado. Esa es la prueba de 30 segundos que zanja el asunto en tu partida.

### C. Estructura de cada habilidad (dato del fichero de datos)

Icy Veins lo describe con la misma forma: *«23 different skills, each with two pairs of mutually exclusive Enhancements and three mutually exclusive Transformation variants»* — https://www.icy-veins.com/d4/guides/necromancer-skills/ (act. 26 jun 2026, T14).

En el fichero, cada habilidad tiene 7 nodos de mejora identificados por una máscara de bits:

| Máscara | Función | Cuántos eliges |
|---|---|---|
| 8 y 16 | **Pareja de Modificadores A** | 1 de 2 |
| 32 y 64 | **Pareja de Modificadores B** | 1 de 2 |
| 1, 2 y 4 | **Las tres Variantes** | 1 de 3 |

Las variantes de máscara **1 y 2** tienen `requiredLevel: 2` (o sea, disponibles en cuanto abre el clúster). La de **máscara 4** es la única que lleva `requiredLevel` 30/32/34/36/38/40. Maxroll rotula esa columna **«LoH Variant»**, y Blizzard escribe: *«Must have the Lord of Hatred expansion to open all three Bonus Skill Variants; otherwise, 2 out of 3 Bonus Skill Variants are accessible»*. **La de máscara 4 es la que tú no vas a tener.**

### D. Las 23 habilidades del Nigromante por clúster, y **cuál es la variante que pierdes**

Composición confirmada por **tres vías independientes**: fichero de datos · https://www.icy-veins.com/d4/guides/necromancer-skills/ · https://d4guides.gg/en/s14/database/classes/necromancer (parche 3.1.0, actualizado 19 ago 2026). Las tres dan 4 / 6 / 3 / 4 / 2 / 4 = **23**.

**Esto cierra el hueco más caro de todo el expediente: ninguna guía decía cuál de las tres variantes es la de pago. El fichero de datos sí.**

| Clúster | Habilidad | Variante 1 ✅ | Variante 2 ✅ | Variante 3 🔒 (no la verás) |
|---|---|---|---|---|
| Básicas (1) | Bone Splinters | Bouncing Spines | Bloody Splinter | **Shadow Seekers** |
| Básicas (1) | Reap | Harvest | Cull The Weak | **Chilled To The Bone** |
| Básicas (1) | Decompose | Dry Rot | Putrid Burst | **Rip and Tear** |
| Básicas (1) | Hemorrhage | Blood Boil | Blood Runs Cold | **Soul Rip** |
| Core (3) | Bone Spear | Bone Spikes | Blood Spear | **Shadow Splitter** |
| Core (3) | Blight | Piercing Darkness | Whirlpool | **Volatile Blood** |
| Core (3) | Sever | Reaping Lotus | Inexorable Reaper | **Cold Pursuit** |
| Core (3) | Blood Surge | Bloodbath | You And What Army? | **Pins and Needles** |
| Core (3) | Blood Lance | Blood Seeker | Gore Quills | **Festering Wound** |
| Core (3) | **Skeleton Mage** | **Coven** | Gift of Death | **Singularity** |
| Cadáver (4) | Corpse Explosion | Bloody Mess | Miasma | **Shrapnel** |
| Cadáver (4) | Corpse Tendrils | Bitter Harvest | Get Over Here! | **Jaws Of Death** |
| Cadáver (4) | **Skeleton Warrior** | **Master of Puppets** | Service and Sacrifice | **Litany of Death** |
| Macabras (8) | Blood Mist | Blood Transfusion | Blood Rush | **Devouring Mist** |
| Macabras (8) | Bone Prison | Bramble | Plunging Darkness | **Life Imprisonment** |
| Macabras (8) | Bone Spirit | Poltergeists | Unfinished Business | **Astral Projection** |
| Macabras (8) | **Golem** | **Gravebloom** | Fel Gluttony | **Gargantua** |
| Maldiciones (13) | Iron Maiden | Schadenfreude | Torture Artist | **Blood Maiden** |
| Maldiciones (13) | Decrepify | Dizzying Curse | Life Tap | **Unholy Frenzy** |
| Definitivas (19) | **Army of the Dead** | **Unyielding Commander** | Pile the Bodies | **Dead Cold** |
| Definitivas (19) | Bone Storm | Roll The Bones | Shadow And Bone | **Hungry Cyclone** |
| Definitivas (19) | Blood Wave | Tides of Blood | Path of Darkness | **Hematolagnia** |
| Definitivas (19) | Soulrift 🔒 *VoH* | Distilled Anima | Soul Vortex | **Frozen Wasteland** |

**Lectura para vosotros dos, sin adornos:** las dos variantes que hacen crecer el ejército —**Coven** (+2 magos) y **Master of Puppets** (+3 guerreros)— son **✅ tuyas**. La variante clave de la Definitiva, **Unyielding Commander**, es **✅ tuya**. Lo que pierdes es **Gargantua** (el aura de velocidad para todos los esbirros) y **Unholy Frenzy** (Decrepitud convertida en buff de esbirros). Y eso importa mucho, porque **las dos builds estrella de Icy Veins de esta temporada, «Naz Mages» y «Reaper Summoner», están construidas alrededor de Gargantua**. No son reproducibles tal cual en juego base.

### E. Presupuesto de puntos — **conflicto declarado, no resuelto**

| Cifra | Desglose | Fuente |
|---:|---|---|
| **80** | 68 por nivel + 12 de Rango de Temporada | https://www.maxroll.gg/d4/getting-started/skill-trees, literal: *«You get one skill point each time you level up, starting from level 2. This continues all the way to level 69. You can also unlock 12 additional skill points through the Season Rank system.»* |
| **83** | «hasta 83» | Blizzard, vía https://www.icy-veins.com/d4/news/diablo-iv-lord-of-hatred-full-blog-post-now-available/ — *«up to 83 available Skill Points»* |
| **81** | 83 − 2 del Renombre de Skovos 🔒 | Un usuario del foro **oficial**: *«You can have 83 in Eternal too, but if you havent done the Skovos renown objectives, you will only have 81»* — https://us.forums.blizzard.com/en/d4/t/so-how-many-skill-points-are-we-supposed-to-have-now/255394 |

Los **12 puntos** del Rango de Temporada están confirmados por cuatro fuentes independientes, incluida **Blizzard**: *«Up to 12 Skill Points»* (blog oficial); https://timesaver.gg/blog/diablo-4-season-14-season-journey (1 jul 2026, nueve rangos); https://allthings.how/diablo-4-season-14-season-rank-tasks-and-rewards-death-awakening/; y la propia Maxroll. **El «14» de Icy Veins es minoritario y su propia frase lo delata** (*«the Season Rank System **or** Renown… respectively»* — está sumando dos vías distintas).

**No sé cuál es tu techo real.** 68 + 12 = 80 cuadra con las fuentes verificables; el «hasta 83» de Blizzard deja 3 puntos sin explicar. Planifica con **80** y si te sobran, mejor.

**Dato accionable y confirmado:** los puntos del Rango de Temporada **no abren clústeres**. *«Skill points from the Season Rank System or Renown do not affect Skill Tree progress and can be allocated to skill ranks you already unlocked»* — https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/. Esto es, por sí solo, incompatible con un modelo de puntos gastados.

---

## Traducción a niveles

Para cuando leas una guía vieja y no sepas si te está mintiendo.

### La regla

> **Puntos gastados = Nivel − 1**, si gastas cada punto al subir.
> Los 12 del Rango de Temporada van aparte y **no cuentan** para abrir nada.

### Tabla de equivalencia rápida

| Si la guía dice… | …quiere decir | Estado |
|---|---|---|
| «2 puntos → Core» | nivel 3 | ✅ El nivel es correcto hoy; el modelo de puntos, no |
| «6 puntos → primer clúster de clase» | nivel 7 | ❌ **Muerto.** Hoy el 3.er clúster (Cadáver) es nivel **4** |
| «11 puntos → segundo clúster de clase» | nivel 12 | ❌ **Muerto.** Hoy Macabras es nivel **8** |
| «16 puntos → tercer clúster de clase» | nivel 17 | ❌ **Muerto.** Hoy Maldiciones es nivel **13** |
| «23 puntos → Definitivas» | nivel 24 | ❌ **Muerto.** Hoy Definitivas es nivel **19**. El 23 real es el nivel de las Variantes de Maldiciones |
| «33 puntos → Pasiva Clave» | nivel 34 | ❌ **Muerto y sin objeto.** La ranura de Pasiva Clave fue eliminada |

**Cómo detectar una guía muerta en 5 segundos.** Si dice cualquiera de estas cosas, está publicando texto de 2023–2024 aunque tenga fecha de 2026:

- nivel máximo **60** · **71** puntos totales
- rango máximo **5** por habilidad (hoy son **15**)
- existe una **Pasiva Clave** (*Key Passive*)
- mejoras llamadas **Enhanced / Paranormal / Supernatural / Blighted / Plagued / Dreadful / Ghastly**
- los esbirros se invocan **desde el Libro de los Muertos** (hoy se invocan desde el **árbol**)
- el Gólem se desbloquea **a nivel 25 con la misión «Call of the Underworld»**

> **Trampa metodológica que hay que interiorizar:** la fecha de «última actualización» de una página **no acredita su contenido**. Caso probado: https://maxroll.gg/d4/resources/necromancer-class-overview lleva sello **«Last Updated: July 18, 2026 · Season 14»** y sigue diciendo *«Each active skill can be leveled up 5 times»*. Es texto muerto con fecha viva, en una fuente de primera línea.

---

## Libro de los Muertos hoy

### Qué es hoy el Libro (cambio estructural del 3.0)

| Qué cambió | Cita | Fuente |
|---|---|---|
| Los esbirros se mudaron al árbol | *«Skeletal Mages, Skeletal Warriors, and Golems are now part of the Necromancer skill tree»* | https://www.icy-veins.com/d4/news/diablo-4s-lord-of-hatred-just-broke-the-necromancer-wide-open/ |
| Idem, fuente independiente | *«the Necromancer's minion-summoning skills have moved from the Book of the Dead directly to the Skill Tree itself»* | https://gamerant.com/diablo-4-lord-of-hatred-skill-tree-update-necromancer/ (28 abr 2026) |
| Qué queda en el Libro | *«the Book of the Dead still lets players choose which form their Skeletal Warriors, Mages, and Golem take»* | ídem |
| El Sacrificio ya no te impide invocar | *«choosing to sacrifice a minion type no longer prevents the Necromancer from summoning them at all»* | ídem |
| Confirmación oficial indirecta | *«Fixed an issue where Book of the Dead minion limits were incorrect after Sacrificing minions»* | https://news.blizzard.com/en-us/article/24271857/diablo-iv-patch-notes-3-0 |

**En cristiano:** el Libro ya no invoca nada. Elige **qué tipo** de esbirro es el que invocas desde el árbol, y te da **2 mejoras + 1 sacrificio** por cada tipo. Y el sacrificio ahora **reduce a la mitad** la cantidad o el daño en vez de quitarte el esbirro — se ve en el propio texto: *«…but the amount of X you can Summon is reduced by 50%»*.

### Los textos completos — 3 invocaciones × 3 variantes × (2 mejoras + 1 sacrificio)

**Origen:** entradas `Necromancer_<Esbirro>_<Variante>_Passive_{UpgradeA|UpgradeB|Sacrifice}` del fichero de datos del juego, versión **3.1.0.72698**, descargado y decodificado por mí el 19 ago 2026. Traducción mía; el texto inglés es el del juego.

**Nota sobre las fórmulas:** donde el juego muestra un número, el fichero guarda la fórmula. He dejado el valor base entre corchetes cuando es legible. Los valores planos (daño) escalan con tu nivel y tu arma: **el número de tu pantalla manda siempre**.

**Nota sobre el recuento:** el encargo pedía «18 mejoras y **3** sacrificios». En el juego hay **9 sacrificios**, uno por variante, no 3. Lo corrijo y los doy los nueve.

#### 1 · Guerreros Esqueléticos (*Skeletal Warriors*)

| Variante | Elemento | Texto | Estado |
|---|---|---|---|
| **Escaramuzadores** (*Skirmishers*) | Mejora A | Puedes alzar **2 Escaramuzadores adicionales**. Cuando se invoca un Escaramuzador, le ordenas automáticamente saltar sobre un enemigo cercano y atacarlo | CONFIRMADO EN FUENTE FECHADA |
| | Mejora B | Los Escaramuzadores acuchillan a los enemigos, dejándolos **Vulnerables** y **Ralentizados un 50 % durante 4 s** | CONFIRMADO EN FUENTE FECHADA |
| | Sacrificio | Tu prob. de crítico aumenta un **[5 % base]**, pero la cantidad de Escaramuzadores se reduce un **50 %**. **Tu Gólem gana 60 %[x] de daño** | CONFIRMADO EN FUENTE FECHADA |
| **Defensores** (*Defenders*) | Mejora A | Los Defensores ganan **Espinas**. Al recibir daño, sus huesos estallan e infligen el **50 % de sus Espinas** a los enemigos cercanos. **Comandar a tus Defensores hace que Provoquen (*Taunt*) a los enemigos cercanos durante 6 s** | **CONFIRMADO EN JUEGO** (coincide con tu captura) |
| | Mejora B | Los Defensores tienen un **10 % de probabilidad de formar un Orbe de Sangre** al infligir daño | **CONFIRMADO EN JUEGO** (tu captura) |
| | Sacrificio | Ganas **[40 % base] de Resistencia a Todos los Elementos**, pero la cantidad de Defensores se reduce un **50 %**. **Tu Gólem gana 60 %[x] de daño** | CONFIRMADO EN FUENTE FECHADA |
| **Segadores** (*Reapers*) | Mejora A | Los ataques cargados del Segador ahora **reducen 3 s uno de tus tiempos de reutilización activos y forman un Cadáver** | CONFIRMADO EN FUENTE FECHADA |
| | Mejora B | Los Segadores infligen **50 %[x] más daño** y tienen un **15 % de probabilidad de Aturdir 1 s** | CONFIRMADO EN FUENTE FECHADA (doble: fichero + https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/) |
| | Sacrificio | Infliges **[15 %[x] base] más daño**, pero la cantidad de Segadores se reduce un **50 %**. **Tu Gólem gana 60 %[x] de daño** | CONFIRMADO EN FUENTE FECHADA |

#### 2 · Magos Esqueléticos (*Skeletal Mages*)

| Variante | Elemento | Texto | Estado |
|---|---|---|---|
| **Sombra** (*Shadow*) | Mejora A | Los Magos de Sombra infligen **daño Corruptor adicional durante 6 s** | CONFIRMADO EN FUENTE FECHADA |
| | Mejora B | Los proyectiles de los Magos de Sombra os dan a ti y al mago una **Barrera del 3 % de tu Vida Máxima durante 4 s**, hasta un tope. **El tope escala con el rango de habilidad** (fórmula `0.03*Table(37,SkillRank)*100*2*5`) | CONFIRMADO EN FUENTE FECHADA |
| | Sacrificio | Tu **regeneración de Esencia +[20 % base]** y tu **Esencia máxima +[20 base]**, pero los Magos de Sombra se reducen un **50 %**. **Tu Gólem gana 60 %[x] de daño** | CONFIRMADO EN FUENTE FECHADA |
| **Frío** (*Cold*) | Mejora A | El proyectil inicial de los Magos de Frío **se bifurca en 2** al impactar. Los enemigos dañados quedan **Debilitados 4 s** | CONFIRMADO EN FUENTE FECHADA |
| | Mejora B | Los Magos de Frío lanzan ocasionalmente una **ventisca** que inflige daño de Frío durante 6 s y **Congela un 6 % por segundo**. Los enemigos dañados quedan **Vulnerables 4 s** | CONFIRMADO EN FUENTE FECHADA |
| | Sacrificio | Infliges **[20 %[x] base] más daño a enemigos Vulnerables**, pero los Magos de Frío se reducen un **50 %**. **Tu Gólem gana 60 %[x] de daño** | CONFIRMADO EN FUENTE FECHADA |
| **Hueso** (*Bone*) | Mejora A | Los Magos de Hueso disparan **2 proyectiles adicionales** que infligen el **75 %** del daño normal | CONFIRMADO EN FUENTE FECHADA |
| | Mejora B | Los ataques de los Magos de Hueso te **Fortifican** un % de tu Vida Máxima. **Los Magos de Hueso forman un Cadáver al morir** | CONFIRMADO EN FUENTE FECHADA |
| | Sacrificio | Infliges **[20 %[x] base] más daño mientras tengas una carga de Sobrecarga (*Overpower*)**, pero los Magos de Hueso se reducen un **50 %**. **Tu Gólem gana 60 %[x] de daño** | CONFIRMADO EN FUENTE FECHADA |

> ⚠️ La variante «Hueso» se llama internamente `SkeletonMage_Sacrifice`. Es el mismo Mago de Hueso de siempre; el nombre interno es un residuo.

#### 3 · Gólems (*Golems*)

| Variante | Elemento | Texto | Estado |
|---|---|---|---|
| **Hueso** (*Bone*) | Mejora A | **Comandar a tu Gólem de Hueso hace que forme 5 cadáveres** | **CONFIRMADO EN JUEGO** (tu captura) |
| | Mejora B | Cuando tu Gólem de Hueso recibe daño, **libera púas de hueso**. Este efecto puede ocurrir **una vez cada 3 s**. **Los enemigos dañados por el Gólem de Hueso quedan Vulnerables durante 4 segundos** | **CONFIRMADO EN JUEGO** + fichero. **Es la frase que faltaba** |
| | Sacrificio | Ganas **[10 % base] de Velocidad de Ataque**, pero tu Gólem inflige **50 %[x] menos daño** | CONFIRMADO EN FUENTE FECHADA |
| **Sangre** (*Blood*) | Mejora A | Comandar a tu Gólem de Sangre hace que **drene Vida de tus otros esbirros**, aumentando su Vida Máxima un **5 %** y su daño un **5 %[x] por esbirro drenado** durante **20 s**, hasta **+50 % Vida Máxima y +50 %[x] daño** | CONFIRMADO EN FUENTE FECHADA |
| | Mejora B | Al comandar a tu Gólem de Sangre, te **Fortificas un 10 % de tu Vida Máxima por cada enemigo que drene** | CONFIRMADO EN FUENTE FECHADA |
| | Sacrificio | Tu **Vida Máxima aumenta un [20 %[x] base]**, pero tu Gólem inflige **50 %[x] menos daño** | CONFIRMADO EN FUENTE FECHADA |
| **Hierro** (*Iron*) | Mejora A | Cada ataque del Gólem de Hierro provoca una **onda de choque** que daña al enemigo principal **y a los que están detrás** | CONFIRMADO EN FUENTE FECHADA |
| | Mejora B | El **pisotón** de tu Gólem de Hierro **atrae a los enemigos** y su **tamaño aumenta un 50 %** | CONFIRMADO EN FUENTE FECHADA |
| | Sacrificio | Infliges **[15 %[x] base] más daño crítico**, pero tu Gólem inflige **50 %[x] menos daño** | CONFIRMADO EN FUENTE FECHADA |

### Cuatro hallazgos nuevos que ninguna guía publica

1. **Todos los sacrificios de Guerreros y de Magos incluyen una segunda línea oculta: «Tu Gólem gana 60 %[x] de daño».** Los sacrificios de Gólem no la tienen. Nueve tooltips, mismo patrón. Ninguna guía web lo menciona. **Si sacrificas guerreros o magos, tu Gólem se vuelve el pilar de daño.**
2. **Resuelto el conflicto «5 % vs 10 %» del Sacrificio de Escaramuzadores.** El valor base del juego es **5 %**, y la fórmula es `0.05*(1+Affix_Value_1(1222268)/100)*100`. El afijo **1222268** es un afijo legendario del Nigromante cuyo texto es *«Your Sacrifice bonuses are increased by X%»*. **Los dos números eran ciertos**: 5 % es el base, 10 % es con ese aspecto equipado. Ninguna de las dos fuentes estaba mintiendo, estaban midiendo cosas distintas.
3. **Resuelto el «30 % vs 42 %» de la Barrera de los Magos de Sombra.** La refutación sospechaba de una plantilla rota. **No lo era:** el tope es `0.03*Table(37,SkillRank)*100*2*5`, es decir, **escala con el rango de la habilidad**. 30 % y 42 % son el mismo tooltip a distinto rango.
4. **El Gólem de Hueso puede estar bugueado.** El tooltip promete Vulnerable, pero en el hilo del foro **oficial** https://us.forums.blizzard.com/en/d4/t/the-big-necromancer-lord-of-hatred-bug-thread/247244 un jugador reporta: *«bone golem is also bugged and not applying vulnerable as it should»*. **Sin respuesta de Blizzard en el hilo.** No construyas la build asumiendo esa Vulnerabilidad sin comprobarla.

### Los máximos de esbirros (del fichero de datos)

- **Guerreros:** base **4**, uno cada 2 s desde un cadáver cercano. **+3** con *Master of Puppets* ✅. **+2** con la mejora A de Escaramuzadores.
- **Magos:** base **3**. **+2** con *Coven* ✅.
- Cada sacrificio multiplica la cantidad por **0,5**.
- El «28 esbirros» de PC Gamer sigue siendo una **estimación a ojo** del periodista (*«what looks like 28»*), no una cifra oficial. **No la uses.**

---

## Orden de puntos para esbirros

Ruta de subida de https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide (act. 30 jun 2026, T14), decodificada desde el planificador https://planners.maxroll.gg/profiles/d4/7xf3kf0h contra el fichero de datos.

**Comprobado nodo a nodo: la ruta de subida completa (1 → 70) es 100 % jugable en juego base.** No usa ni una sola variante de máscara 4.

| Puntos acumulados | Qué haces |
|---:|---|
| **3** | 3 rangos en **Reap**. Puro aparcamiento: hasta nivel 3 no puedes tocar nada más |
| **4** | 🔄 **RESPEC (gratis).** Reembolsas Reap y metes 4 en **Skeleton Mage** |
| **7** | +1 **Corpse Tendrils**, +1 **Skeleton Warrior**, +1 Modificador A de Mage, +1 Modificador A de Warrior (Mage baja a 3) |
| **12** | +1 **Golem**, +1 Golem *Unstoppable*, +1 Tendrils *Critical Strike Chance*, +1 Modificador B de Mage, +1 Modificador B de Warrior |
| **18** | +1 **Iron Maiden**, Warrior a 2, **+1 *Coven* (+2 magos)** ✅, **+1 *Master of Puppets* (+3 guerreros)** ✅, +1 Tendrils *Vulnerable*, +1 Modificador B de Golem |
| **26** | +1 **Army of the Dead** con **✅ *Unyielding Commander*** (esbirros −90 % daño recibido, tú +50 %[x] daño de invocación), +1 *Cooldown Reduction*, +1 *Corpse Generation*, **+1 Golem *Gravebloom*** ✅, +1 Iron Maiden *Schadenfreude* ✅, **+1 Iron Maiden *Essence Generation*** (deja de costar Esencia y **genera 5 por enemigo maldito**), Warrior a 3 |
| **40** | **Iron Maiden de 1 → 15.** 14 puntos seguidos |
| **80–83** | **Skeleton Mage, Skeleton Warrior y Golem a 15/15.** Army of the Dead a 6. Se cambia Warrior *Resolve* por *Vulnerable* |

### La regla min-max que da forma a todo esto

> *«Generally, each extra skill point makes a skill 10% more powerful than it was at rank 1. So, a skill with 5/15 points will be 40% stronger than 1/15 points. **In other words, the first point you put into an active skill is 10 times more powerful than the next 4.**»*
> — https://www.maxroll.gg/d4/getting-started/skill-trees

**Amplitud primero, profundidad al final.** Hasta los 26 puntos pones **1 rango** en casi todo y gastas en abrir modificadores y variantes. Subir Skeleton Mage a 5/15 antes de tener Gólem, *Coven* y *Master of Puppets* es la forma más común de tirar puntos.

### Prioridad por clúster, en una línea

1. **Fundamentales (nv 3)** → Skeleton Mage. Antes que nada.
2. **Cadáver (nv 4)** → Skeleton Warrior + Corpse Tendrils.
3. **Macabras (nv 8)** → Golem.
4. **Maldiciones (nv 13)** → Iron Maiden (es tu motor de Esencia vía *Essence Generation*).
5. **Definitivas (nv 19)** → Army of the Dead, **solo** por *Unyielding Commander*.
6. **Básicas (nv 1)** → **cero puntos permanentes**.

### Habilidades trampa ✅ (todas disponibles para ti, todas malas para esta build)

| Trampa | Por qué no |
|---|---|
| ***Service and Sacrifice*** (Warrior) | Tus esqueletos **pierden el 25 % de su Vida Máxima por segundo en combate**. Ninguno de los 6 perfiles del planificador la usa |
| ***Gift of Death*** (Mage) | Convierte a Skeleton Mage en **habilidad de Cadáver que exige un cadáver** para invocar. Compite con todo lo demás. Todos los perfiles cogen *Coven* |
| ***Pile the Bodies*** (AotD) | El «300 %[x]» es el número más grande de la pantalla y es un cebo: escala una Definitiva con reutilización larga. *Unyielding Commander* está activa casi siempre |
| ***Fel Gluttony*** (Golem) | Ningún perfil del planificador la usa. Tu elección real es *Gravebloom* ✅ |
| ***Torture Artist*** (Iron Maiden) | Cambia el tipo de daño a Sombra y **puede invalidar tu equipo**. Además, bug confirmado al reespecializar (ver abajo) |
| **Copiar Decrepify de las guías** | Las guías la llevan por ***Unholy Frenzy*** 🔒 y por un Runeword 🔒. **Sin expansión ese hueco es tuyo para otra cosa** |
| **Subir Army of the Dead por encima de 6** | La build acaba con AotD a 6/15 y los esbirros a 15/15 |

### Dos avisos prácticos

- **Reespecializar es gratis** y el paso 2 ya te obliga a hacerlo. *«You can also refund any point in your skill tree… completely free of charge»* — https://www.maxroll.gg/d4/getting-started/skill-trees.
- ⚠️ **Bug confirmado al reespecializar con variantes que cambian el tipo de daño.** Con *Torture Artist* activa, pulsar «reembolsar todo» **deja pegadas las etiquetas de sombra y oscuridad** aunque elijas otra variante. Hilo del foro oficial https://us.forums.blizzard.com/en/d4/t/skill-tree-bug-necro/249002 (3 y 11 may 2026), **sin respuesta de Blizzard**. Quítate primero los aspectos que conviertan tipo de daño.

---

## Lo que sigue sin saberse

Huecos declarados. Ninguno relleno con conjetura.

### Resueltos en esta pasada (ya no son huecos)

| Antes abierto | Ahora |
|---|---|
| **El final de la frase cortada del Gólem de Hueso, Mejora 2** | ✅ **RESUELTO Y CONFIRMADO POR PARTIDA DOBLE.** Termina en *«Enemies damaged by Bone Golem are made Vulnerable for 4 seconds»* — fichero de datos 3.1.0.72698 **y** https://www.icy-veins.com/d4/guides/bone-spirit-necromancer-build/. Coincide con tu captura. ⚠️ Con la salvedad de que un jugador del foro oficial reporta que **no se está aplicando** (bug) |
| **Cuál de las 3 variantes es la bloqueada, habilidad por habilidad** | ✅ **RESUELTO.** Es la de máscara 4, con `requiredLevel` 30–40. Tabla completa de las 23 en §D |
| **5 % vs 10 % del Sacrificio de Escaramuzadores** | ✅ **RESUELTO.** Base 5 %; sube con el afijo legendario *«Your Sacrifice bonuses are increased by X%»* |
| **30 % vs 42 % de la Barrera de Sombra** | ✅ **RESUELTO.** Escala con el rango de habilidad. No era plantilla rota |
| **Si existe umbral de puntos gastados** | ✅ **RESUELTO EN NEGATIVO.** El árbol solo tiene `requiredLevel`. Cero campos de puntos gastados en 11,6 MB |
| **Si hay clúster de Invocación o de Pasivas Definitivas** | ✅ **RESUELTO EN NEGATIVO.** Son 6 clústeres, 23 habilidades, confirmado por tres vías |
| **Textos de *Fel Gluttony*, *Gargantua*, *Litany of Death*, *Singularity*** | ✅ **RESUELTOS**, texto completo en §D y §Orden |

### Siguen abiertos

1. **🔴 EL DESBLOQUEO DEL LIBRO DE LOS MUERTOS SIGUE SIN CERRARSE.** Es el hueco más molesto y **el fichero de datos no ayuda**: las 27 entradas del Libro tienen `requires: -1`, es decir, **ningún requisito de nivel codificado ahí**. Las fuentes siguen en conflicto:
   - **Nivel 5** — https://www.icy-veins.com/d4/guides/necromancer-leveling-guide/ (26 jun 2026): *«It unlocks for free at Level 5»*
   - **Nivel 5** — https://maxroll.gg/d4/resources/necromancer-class-overview (⚠️ página con texto muerto probado)
   - **Nivel 6** — https://www.ezg.com/blog/diablo-4-season-14-season-of-death-awakening-summoner-necromancer-changes-explained
   - **Nivel 15** — https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide (30 jun 2026)
   **Maxroll se contradice a sí misma.** Mayoría por el 5, sin certeza. **Solo se cierra en tu pantalla.**

2. **Los niveles de desbloqueo de cada variante del Libro.** Icy Veins publica una tabla completa (Skirmishers 5 · Defenders 8 · Reapers 12 · Shadow 5 · Cold 18 · Bone 22 · Gólem de Hueso 8 · Sangre 28 · Hierro 32). **No coincide con la tabla de 2023** (Guerreros 5 → Magos 15 → Gólem 25), así que **no es texto reciclado** — pero tampoco tiene un segundo testigo. Y el fichero de datos no la contiene.

3. **Si la misión «Llamada del Inframundo» (*Call of the Underworld*) sigue gobernando el Gólem.** Ninguna fuente de 2026 lo confirma ni lo desmiente para la T14. **No esperes a nivel 25 asumiendo que llegará.**

4. **El techo real de puntos en juego base: 80, 81 u 83.** Ver §E. El «81» solo lo dice un usuario del foro oficial.

5. **Si los 12 puntos del Rango de Temporada son íntegramente alcanzables sin expansión.** Se sabe que parte de los objetivos del Viaje de Temporada exige *Lord of Hatred*; **no se sabe si alguno de los que dan punto de habilidad está entre ellos.** Hueco crítico para tu perfil.

6. **Qué significa exactamente `ranks: 3` en los nodos de modificador y variante.** En el fichero, cada habilidad es `ranks: 15` y **cada nodo de modificador es `ranks: 3`**. Si eso significa que puedes meter 3 puntos en cada modificador, maximizar una habilidad costaría 15 + 3×3 = **24 puntos**, no 4. Pero Icy Veins dice que las variantes *«in some cases may scale with Skill Ranks»*, lo que apunta a que el 3 es otra cosa. **No lo he podido resolver y no lo voy a inventar.** Afecta directamente a tu plan de gasto: compruébalo pulsando dos veces un nodo de modificador.

7. **Ninguna cifra del árbol tiene respaldo primario de Blizzard.** Las notas oficiales que abren (https://news.blizzard.com/en-us/article/24271857/diablo-iv-patch-notes-3-0) son **solo correcciones 3.0.1–3.0.4**. El blog de sistemas solo lo tengo reproducido por Icy Veins. Todo lo estructural viene de terceros o del *datamining*.

8. **Reddit: cero cobertura, tercera pasada consecutiva.** `www.reddit.com` devuelve `Claude Code is unable to fetch from www.reddit.com`. Es un bloqueo del entorno, no del sitio. **No lo he rodeado con espejos ni proxies a propósito**, porque sería saltarse una restricción de acceso. r/diablo4 y r/Diablo4Necromancer siguen sin cubrir y **tendrás que abrirlos tú**.

9. **El texto «base» de cada una de las 9 variantes del Libro.** El fichero da Mejora A, Mejora B y Sacrificio, pero **no una descripción base separada**. Ojo a este detalle: tu captura muestra las Espinas de los Defensores y el Provocar de 6 s como **dos filas distintas**, mientras el fichero las guarda **juntas en la Mejora A**. Es probable que la interfaz del juego reparta el texto de otra forma que el fichero. **Tu pantalla manda.**

10. **Si *Unyielding Commander* se solapa entre dos nigromantes en dúo.** No investigado. Os afecta directamente: **probadlo.**

11. **Los nombres en español de España** de clústeres y variantes. Todas las fuentes vivas están en inglés; las traducciones de este documento son mías salvo las de tu captura.

### Las cinco comprobaciones que cierran casi todo, con el juego delante

| Comprobación | Cierra |
|---|---|
| **Sube un nivel SIN gastar el punto.** ¿Se abre igual el siguiente clúster? | §0 — la prueba decisiva nivel vs puntos |
| **Lee el texto del candado** de un clúster bloqueado | §0 — dirá «Requiere nivel X» o «X puntos gastados» |
| **A qué nivel exacto te salta el aviso del Libro de los Muertos** | Hueco 1 |
| **Pulsa dos veces un nodo de modificador.** ¿Admite un 2.º y 3.er punto? | Hueco 6 |
| **Mira la tercera variante de una habilidad.** ¿Tiene candado con texto de expansión? | Confirma el «2 de 3» |

---

## Fuentes muertas detectadas

Páginas que **hoy, 19 de agosto de 2026**, siguen publicando el modelo pre-3.0.

### Vetadas por el encargo — confirmadas muertas, no usadas para ningún número

| Fuente | Qué sirve de muerto |
|---|---|
| **fextralife** (`diablo4.wiki.fextralife.com`) | Cabecera de Libro de los Muertos referenciada al **parche 1.1.0a (2023)**. Origen de los nombres *Enhanced / Paranormal / Supernatural / Blighted / Plagued / Dreadful / Ghastly*, que ya no existen. Apareció en primera página en casi todas mis búsquedas |
| **primagames**, **beebom**, **gamespot**, **segmentnext**, **studioloot**, **gamerguides**, **pcgamesn**, **mythicdrop** | Textos del Libro de los Muertos de 2023. **Ninguna abierta, ningún dato de este documento procede de ellas** |

> ⚠️ **Falso positivo que conviene desactivar:** **pcgamer.com** NO es **pcgamesn.com**. Son medios distintos y PC Gamer no está vetado.

### No vetadas, pero igualmente muertas — estas son las peligrosas

| Fuente | Evidencia de muerte | Fecha que muestra |
|---|---|---|
| **https://game8.co/games/Diablo-4/archives/402759** | Publica la escalera completa **0/2/6/11/16/23/33**, «71 total skill points», nivel máximo 60, Pasivas Clave. **Es la partida de defunción de los números 23 y 33 del encargo** | 13 oct 2024 |
| **https://maxroll.gg/d4/resources/necromancer-class-overview** | **El caso más grave.** Dice *«Each active skill can be leveled up 5 times»* y *«one out of two upgrades»* — modelo pre-3.0 | **«July 18, 2026 · Season 14»** ← fecha viva, texto muerto |
| **https://maxroll.gg/d4/resources/necromancer-book-of-the-dead** | Recurso dedicado al Libro: nivel 5, Gólem por misión a nivel 25, esquema de 2024 | 4 oct 2024, Season 5 |
| **https://game8.co/games/Diablo-4/archives/413422** | Libro de los Muertos con Gólem a nivel 25 | 2 oct 2024 |
| **https://www.wowhead.com/diablo-4/guide/classes/necromancer/…** | Sus guías de clase del Nigromante se declaran **«Season 12»** — anteriores al rework del 28 abr 2026 | 11 mar 2026 |
| **https://www.vhpg.com/diablo-4-skill-trees/** | Escalera 0/2/6/11/16/23/33 y costes de respec en oro («222 Gold at level 25») que ya no existen | beta 2023, sin fecha |
| **https://d4dead.com/skill-tree/** | *«Key Passives sit in the final cluster»*, «one skill point per level until level 50» | 30 mar 2026 (**pre-parche**) |
| **https://kami-labs.fr/en/diablo-4/diablo-4-skill-tree-lord-of-hatred/** | Dice **12 puntos por habilidad** (son 15) | 18 abr 2026 (**10 días pre-parche**) |
| **https://www.esports.net/news/blizzard/diablo-4-skill-tree/** | *«you will have to spend 23 points in the Skill Tree»* | sin fecha visible |

### Trampa de segundo orden: páginas pre-parche que parecen post-parche

**https://www.maxroll.gg/d4/getting-started/skill-trees** está fechada **«Last Updated: April 26, 2026»**, es decir, **dos días ANTES del parche 3.0**. Por la regla del encargo es material de previa.

**Pero su contenido sí es post-3.0** y lo he verificado contra el fichero de datos: da rango máximo **15**, no menciona Pasivas Clave, describe *Variant nodes*, y **su tabla de niveles coincide dígito a dígito con los `requiredLevel` del juego**. Es una página escrita con el parche ya conocido y publicada dos días antes. **Es fiable, pero no por su fecha: por haberla podido contrastar contra los datos.**

Sus totales de puntos (68 + 12 = 80) sí chocan con el «hasta 83» de Blizzard. Ver §E.

### El criterio que de verdad funciona

La fecha no acredita nada. **Exige marcadores post-3.0 en el propio texto:**

✅ rango máximo **15** · ✅ **sin** Pasivas Clave · ✅ **sin** pasivas en el árbol · ✅ nivel máximo **70** · ✅ habla de *Variants* / *Transformations* · ✅ los esbirros están **en el árbol**, no en el Libro.

### Fuentes que no se pudieron abrir (tercera pasada consecutiva)

| Fuente | Resultado |
|---|---|
| `reddit.com` / `old.reddit.com` | **Bloqueado por el entorno.** No rodeado a propósito |
| `mobalytics.gg` | HTTP **403** |
| `diablobytes.com` | HTTP **403** |
| `d4builds.gg/skill-tree/` | HTTP **404**; el planificador es JavaScript puro, no expone requisitos |
| `rpgstash.com`, `boostmatch.gg`, `mmopixel.com`, `purediablo.com` | HTTP 403 / muro Cloudflare |
| `forbes.com` (Paul Tassi) | HTTP 403 al abrir directamente |

---

## Fuentes abiertas y verificadas en esta pasada

**Datos del juego (aportación nueva)**
- `https://assets-ng.maxroll.gg/d4-tools/game/data.min.json` — **HTTP 200, 11.606.292 bytes, versión `3.1.0.72698`.** Descargado y decodificado. Origen de: los seis `requiredLevel` de clúster, las puertas de rama, las 23 habilidades por clúster, las 69 variantes con su máscara, las 27 entradas del Libro de los Muertos, los máximos de esbirros y la identificación del afijo 1222268

**Abiertas con WebFetch**
- https://www.maxroll.gg/d4/getting-started/skill-trees — «Last Updated: April 26, 2026». Tabla de desbloqueo, 2 variantes base vs 3 con expansión, rango 15, 68+12
- https://www.icy-veins.com/d4/guides/necromancer-skills/ — 26 jun 2026, T14. 23 habilidades, clústeres [Level 3/4/8/13/19]
- https://www.icy-veins.com/d4/guides/necromancer-leveling-guide/ — 26 jun 2026, T14. Libro de los Muertos a nivel 5 y tabla de variantes
- https://www.icy-veins.com/d4/news/diablo-iv-lord-of-hatred-full-blog-post-now-available/ — blog oficial de Blizzard reproducido: «2 out of 3 Bonus Skill Variants», pasivas fuera del árbol, nivel 70, «up to 83», «Up to 12 Skill Points»
- https://www.icy-veins.com/d4/news/diablo-4-3-1-3-patch-notes-easier-season-objectives-and-echo-of-mephisto-portal-fix/ — 3.1.3 Build #73224, 12 ago 2026
- https://d4guides.gg/en/s14/database/classes/necromancer — **Patch 3.1.0, actualizado 19 ago 2026**. Composición 4/6/3/4/2/4
- https://www.iggm.com/news/diablo-4-season-13-lord-of-hatred-skill-tree-rework-of-8-classes — «only two of the three skill variations…»
- https://us.forums.blizzard.com/en/d4/t/the-big-necromancer-lord-of-hatred-bug-thread/247244 — foro **oficial**. Bug del Gólem de Hueso y del tope de esbirros

**Búsquedas realizadas (8)** — tercera variante y expansión · Libro de los Muertos T14 · Viaje de Temporada y puntos · Gargantua/Blood Maiden/Singularity · parche 3.1.3 · wowhead árbol · «Bonus Skill Variants» 2 de 3 · builds de esbirros T14/SSF

**Heredadas de los informes previos y de sus refutaciones**, citadas sin reabrir: gamerant.com (28 abr 2026), news.blizzard.com/24271857 y /24287406, us.forums.blizzard.com (hilos 255394, 249002, 261095, 256563), maxroll minion-necromancer-leveling-guide, planners.maxroll.gg/profiles/d4/7xf3kf0h, timesaver.gg, allthings.how, switchbladegaming.com, ezg.com.
