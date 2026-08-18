# REFUTACIÓN ADVERSARIAL — «Progresión real del Nigromante» (progresion-real.md)

**Verificador:** pasada adversarial independiente
**Fecha:** 18 de agosto de 2026
**Informe auditado:** `/Users/alvhor/Proyectos/DIAVLO IV/investigacion/crudo/progresion-real.md`
**Veredicto global: PARCIAL.** La tesis central sobrevive. Varios números «confirmados» NO sobreviven. Hay **una cita atribuida a una fuente que no la contiene**.

---

## 0. Resumen ejecutivo — qué cae y qué aguanta

| # | Afirmación del informe | Veredicto | Gravedad |
|---|---|---|---|
| 1 | Cita de DiabloBytes sobre «set level brackets / no arbitrary skill point totals» | **FALSA — la frase no existe en esa página** | 🔴 Crítica |
| 2 | «69 puntos por subir de nivel» | **REFUTADA — son 68** | 🔴 Crítica |
| 3 | «14 puntos del Rango de Temporada» | **REFUTADA — la mayoría de fuentes de S14 dicen 12** | 🔴 Crítica |
| 4 | «69 + 14 = 83 cuadra exactamente» | **REFUTADA — razonamiento circular** | 🔴 Crítica |
| 5 | Gólem por el Libro de los Muertos / misión al nivel 25 (§6) | **REFUTADA — los esbirros están hoy EN EL ÁRBOL** | 🔴 Crítica |
| 6 | «Todas las fuentes post-rework dicen NIVEL» | **FALSA como afirmación universal** | 🟠 Alta |
| 7 | Maxroll `necromancer-class-overview` como fuente fiable de S14 | **REFUTADA — la página es contenido pre-3.0 con fecha nueva** | 🟠 Alta |
| 8 | «Coste de una habilidad completa: 4 puntos» | **MAL ETIQUETADA — Forbes dice ~15** | 🟠 Alta |
| 9 | Hueco #9: «¿5 o 6 clústeres?» | **RESUELTO — son 6, estaba en la fuente que citó** | 🟡 Media |
| 10 | Modelo por NIVEL para los clústeres | **AGUANTA** (mejor sostenido de lo que el informe creía) | ✅ |
| 11 | Nivel máximo 70 | **CONFIRMADA** con fuente independiente | ✅ |
| 12 | Rango máximo 5 → 15 | **CONFIRMADA** con fuente independiente | ✅ |
| 13 | Pasivas y Pasiva Clave eliminadas del árbol | **CONFIRMADA** con fuente independiente | ✅ |
| 14 | 23 y 33 puntos son datos muertos | **CONFIRMADA — y ahora con la prueba documental** | ✅ |
| 15 | «2 de 3 variantes sin expansión» | **CONFIRMADA — y con fuente mucho mejor** | ✅ |
| 16 | Reddit / d4builds inaccesibles | **CONFIRMADA** | ✅ |
| 17 | Ninguna fuente vetada usada para números | **CONFIRMADA** | ✅ |

---

## 1. 🔴 LA FALTA MÁS GRAVE: una cita que no existe

El informe apoya su conclusión central (§0, tabla de citas literales) en esto:

> «Skill clusters, modifier slots, and variant options unlock automatically at set level brackets from 1 to 70, **with no arbitrary skill point totals required to progress**.»
> — atribuido a `https://diablobytes.com/diablo-iv/guides/skill-tree-rework/` *«(vía resultados de búsqueda; la página devuelve HTTP 403 al abrirla)»*

**He abierto esa página en un navegador real. La frase no está.** Tampoco ninguna aproximación.

Prueba ejecutada sobre el DOM de la página cargada:

```
{"arbitrary": false, "bracket": false, "level brackets": false,
 "modifier slot": false, "points spent": false, "len": 8359}
```

Las palabras **«arbitrary» y «bracket» no aparecen ni una sola vez** en los 8.359 caracteres de la página.

**De dónde salió realmente la frase:** de la síntesis automática de un buscador, que mezcla varias páginas. El texto más parecido que sí existe está en **kami-labs.fr**, y es distinto:

> «Gone are the mandatory point thresholds to advance through the tree. With Lord of Hatred, nodes unlock based on your character level.»
> — https://kami-labs.fr/en/diablo-4/diablo-4-skill-tree-lord-of-hatred/ (18 abr 2026)

Y kami-labs **tampoco** contiene «no arbitrary skill point totals» (verificado explícitamente).

**Por qué esto importa más que un error de citado:** el informe se construyó sobre la regla dura nº 5 del encargo («todo valor debe ir con la URL de donde sale; si no lo has visto escrito, di *no encontrado*»). Citar un resumen de buscador como si fuera texto de la fuente **viola esa regla exactamente en el punto donde el informe declara su conclusión más importante**. El informe hace lo mismo una segunda vez con la Pasiva Clave (§1) y una tercera con thephrasemaker y skycoach (§1, §2.3): cuatro citas «vía búsqueda».

**Atenuante:** el contenido de fondo de esa afirmación (Pasiva Clave eliminada) **sí** está en la página, con estas palabras exactas, que ahora sí puedo citar de verdad:

> «The capstone "Key Passive" slot every class caps out with is being removed entirely. Replaced by expanded branching within the tree.»
> — https://diablobytes.com/diablo-iv/guides/skill-tree-rework/

**Nota de herramienta:** el informe declara DiabloBytes y Mobalytics como «no accesibles (HTTP 403)». **Es una limitación de WebFetch, no de la fuente.** Ambas se abren sin problema en el panel de navegador. De ahí salen dos de las refutaciones más importantes de este documento. Un 403 de WebFetch no es motivo para citar de oídas.

---

## 2. 🔴 Los puntos por nivel: son 68, no 69

El informe afirma:

> «69 puntos por subir de nivel (1 por nivel del 2 al 70); *one skill point each time you level up, starting from level 2*» — maxroll.gg/d4/getting-started/skill-trees

**La cita está truncada, y el trozo cortado es justo el que da el número.** Texto literal completo de esa misma página, pedido dos veces y reproducido palabra por palabra:

> «You get one skill point each time you level up, starting from level 2. **This continues all the way to level 69.** You can also unlock **12** additional skill points through the Season Rank system.»
> — https://maxroll.gg/d4/getting-started/skill-trees

Niveles 2 a 69 = **68 puntos**, no 69. El informe cortó la cita antes de «level 69» y rellenó «del 2 al 70» por inferencia desde el cap de nivel — que es precisamente lo que la regla 5 del encargo prohíbe.

---

## 3. 🔴 El Rango de Temporada: 12, no 14

El informe da **14** como respuesta directa (§2.2) y descarta el 12. La instrucción del encargo lo listaba entre los valores «confirmados». **No lo está.**

### Fuentes que dicen 12

| Fuente | Cita | Fecha / temporada |
|---|---|---|
| https://maxroll.gg/d4/getting-started/skill-trees | «You can also unlock **12** additional skill points through the Season Rank system.» | 26 abr 2026 |
| https://mobalytics.gg/diablo-4/guides/everything-lord-of-hatred | «Up to **12** Skill Points» (lista de recompensas del Rango de Temporada) | 2 may 2026 |
| https://timesaver.gg/blog/diablo-4-season-14-season-journey | «Completing it grants up to **12** Skill Points, up to 42 Paragon Points, up to 7 Resplendent Sparks» | S14 |
| https://allthings.how/diablo-4-season-14-season-rank-tasks-and-rewards-death-awakening/ | «Finishing the full chain earns up to **12** Skill Points» | S14 |

### Fuentes que dicen 14

| Fuente | Fecha |
|---|---|
| https://maxroll.gg/d4/resources/season-journey | 13 jul 2026 |
| https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide | 30 jun 2026 |

**Ambas son Maxroll.** Es decir: el «14» del informe no tiene dos fuentes independientes, tiene **una casa** que además **se contradice a sí misma**, porque la propia Maxroll dice 12 en su página de referencia del árbol.

### El fallo de método, que es peor que el número

El informe descartó allthings.how por «internamente incoherente» (su desglose 2+2+2+1 suma 7, no 12). He verificado ese desglose y es correcto: Rango 1 = 2, Rango 2 = 2, Rango 3 = 2, Rango 4 = 1, Rangos 5-9 = 0. Pero:

- El mismo defecto lo tiene la fuente que el informe **sí** aceptó: Maxroll `season-journey` dice que los puntos están «in Ranks 1 through 5», mientras timesaver.gg documenta **9 rangos** en S14. Ninguna de las dos cuadra su desglose con su total.
- El informe aplicó el criterio de descarte **solo a la fuente que decía 12**, y no a la que decía 14. Eso no es escepticismo, es selección.
- Y declaró el motivo: «69 + 14 = 83 cuadra exactamente con la cifra oficial». **Eligió el sumando que hacía cuadrar la cuenta.** Es razonamiento circular: el 83 no valida el 14; el 14 se escogió *porque* daba 83.

**Con los números reales de la fuente citada: 68 + 12 = 80.** Los 3 que faltan hasta 83 quedan **sin explicar** y no debe rellenarlos nadie.

Pista real sobre esos 3 — hay una **tercera** vía de puntos que el informe no contabilizó en su aritmética:

> «Skill points are unlocked by level-ups, the **Renown system (eternal realm)**, and the Season Rank system (seasonal realm).»
> — https://maxroll.gg/d4/resources/necromancer-class-overview

Esto es coherente con el hilo del foro que el informe cita (83 vs 81 según Skovos, que es Renown), y con Game8, que en el sistema viejo daba **12 puntos por Renown**. Pero **no lo doy por bueno**: la página de la que sale está contaminada (§6).

---

## 4. 🔴 El Gólem: el informe describe un sistema que ya no existe

Toda la §6 y buena parte de la §7 del informe se apoyan en que el Gólem y los esbirros se gestionan por el **Libro de los Muertos**, con la misión *Call of the Underworld* al nivel 25. **Eso es pre-3.0.**

Con *Lord of Hatred*, **los esbirros se mudaron al árbol de habilidades**. Cuatro fuentes independientes, todas post-parche:

> «Skeletons, Mages, and Golem now have their own dedicated spaces on the Skill Tree with each having their own unique upgrade paths»
> — https://mobalytics.gg/diablo-4/guides/everything-lord-of-hatred (2 may 2026)

> «All minion summons (Skeletons, Golems, Mages) move out of the Book of the Dead and into the main skill tree… Book of the Dead remains but re-scopes around buffs and the sacrifice mechanic. Summoner Necros rebuild from scratch.»
> — https://diablobytes.com/diablo-iv/guides/skill-tree-rework/

> «Skeletal Mages, Skeletal Warriors, and Golems are now part of the Necromancer skill tree.» · «Raise Skeleton is being split into two separate skills.»
> — https://www.icy-veins.com/d4/news/diablo-4s-lord-of-hatred-just-broke-the-necromancer-wide-open/

> «The old Raise Skeleton skill has been split into two different skills: Raise Skeleton and Raise Mages» · «El Libro de los Muertos cambia: los bonus de Sacrificio ya no exigen sacrificar todos los esbirros»
> — https://mobalytics.gg/diablo-4/guides/everything-lord-of-hatred

**Y la prueba definitiva está en una página que el propio informe citó.** Test de contenido sobre `icy-veins.com/d4/guides/necromancer-skills/`:

> Skeleton Mage, Skeleton Warrior y Golem **aparecen como habilidades propias del árbol**, cada una con su coste de esencia, su cooldown y sus mejoras.

**Consecuencias directas:**

1. La §6 del informe («¿Gólem al 8 o al 25?, ¿sigue haciendo falta la misión?») está **mal planteada**. No es un conflicto entre fuentes: es una fuente viva (el árbol) contra una fuente muerta (el Libro de los Muertos como origen del Gólem).
2. La recomendación de §6.2 —«si no está al 8, el diario os dará *Call of the Underworld* automáticamente al 25»— **no es segura** y puede mandar al jugador a esperar una misión que quizá ya no gobierna el Gólem.
3. Las cifras de variantes del Libro (Reapers 12, Blood Golem 28, Iron Golem 32) que el informe marcó como «sospechosas» en §7 lo son **por un motivo más fuerte del que dio**: no es solo que huelan a 2023, es que el sistema del que salen fue re-alcanzado por el rework.
4. En cambio, el informe **acierta** al decir que el Libro de los Muertos sigue existiendo. Lo confirma también IGGM: «the original Book of the Dead remains largely unchanged» — https://www.iggm.com/news/diablo-4-season-13-lord-of-hatred-skill-tree-rework-of-8-classes (25 abr 2026). Sigue definiendo el tipo de esbirro; lo que cambió es que **los invocas desde el árbol**.

---

## 5. 🟠 «Todas las fuentes post-rework dicen NIVEL»: falso como universal, correcto como conclusión

El informe escribe en §0, en negrita:

> «Todas las fuentes post-rework que he conseguido abrir dicen lo contrario: los clústeres se desbloquean por NIVEL DE PERSONAJE.»

**No es cierto.** Existe al menos una fuente post-lanzamiento que dice lo opuesto, de forma explícita y en dos frases distintas:

> «New modifier's for skills are unlocked when you reach a specific amount of **Skill Points invested**»
> «Players can now **allocate points into any part of their Skill Tree at any level**.»
> — https://mobalytics.gg/diablo-4/guides/everything-lord-of-hatred (2 may 2026, post-lanzamiento)

Y una segunda, en la página de Maxroll que el informe **sí abrió y sí citó** (su fuente nº 6):

> «As you spend more points, you unlock multiple categories of skills.»
> — https://maxroll.gg/d4/resources/necromancer-class-overview

El informe leyó esa página para el Gólem y para el Libro de los Muertos, y **no reportó esta frase**, que contradecía frontalmente la conclusión que estaba defendiendo. Sea por descuido o por sesgo de confirmación, es una omisión material.

### Pero la conclusión del informe aguanta — y por mejores razones

Sometí las dos fuentes clave del informe a un **test de huella** (¿son texto post-3.0 o texto de 2023 con fecha nueva?). Ambas **pasan**:

| Página | Rango máx. | ¿Pasiva Clave? | ¿Variantes/ramas? | ¿Esbirros en el árbol? | Veredicto |
|---|---|---|---|---|---|
| `maxroll.gg/d4/getting-started/skill-trees` | **15** («You can invest up to 15 skill points into each active skill») | No | Sí, «Variant nodes» | — | ✅ post-3.0 |
| `icy-veins.com/d4/guides/necromancer-skills/` | — | No | Sí, «two pairs of mutually exclusive Enhancements and three mutually exclusive Transformation variants» | **Sí** | ✅ post-3.0 |

Es decir: las dos páginas que dan la tabla de clústeres **por nivel** (1 / 3 / 4 / 8 / 13 / 19) son contenido genuinamente reescrito tras el parche, no reciclado. Eso es un apoyo **más fuerte** que el que el informe se atribuyó, porque no depende de la cita inventada de DiabloBytes ni de kami-labs (que es del **18 de abril**, diez días **antes** del parche, y por tanto una previa, no una descripción del juego vivo).

**Estado real de la cuestión, honestamente:**

- **Clústeres (Básicas → Fundamentales → … → Definitivas): por NIVEL DE PERSONAJE.** Dos fuentes post-3.0 verificadas, coincidentes en los seis valores.
- **Mejoras y variantes dentro de cada habilidad: por PUNTOS INVERTIDOS EN ESA HABILIDAD** (hasta 15). Esto es lo que describe Mobalytics, y **no contradice** lo anterior: son dos ejes distintos.
- La premisa del encargo (23 y 33 puntos gastados) no encaja en ninguno de los dos ejes. Sigue muerta (§7).

Lo único que Mobalytics contradice de verdad es «hay puertas de nivel para los clústeres». Ahí queda un conflicto **abierto** de una fuente contra dos. El informe hizo bien en no traducir niveles a puntos; hizo mal en decir que no existía disidencia.

---

## 6. 🟠 Maxroll `necromancer-class-overview` está contaminada — y el informe la usó cuatro veces

El informe la trata como fuente de referencia («18 jul 2026, la más reciente», «más fiable para este dato que una guía de build»). **Contiene texto pre-3.0 bajo una fecha de julio de 2026.** Dos huellas fatales, citadas literalmente:

> «Each active skill can be leveled up **5 times** (and further with items)…»
> «After unlocking a skill, you can enhance it with another point and then choose **one out of two upgrades**…»

- «5 times» contradice el rango máximo **15**, confirmado por Forbes *y* por Maxroll `skill-trees` («up to 15 skill points into each active skill»).
- «one out of two upgrades» es la estructura vieja (Enhanced → Supernatural/Paranormal), no el sistema de **dos pares de Enhancements + tres Transformation variants**.

**Es exactamente el pecado que el informe imputa a Fextralife en §4(a) y a Icy Veins en §7 — y lo comete la fuente que el informe colocó por encima de las demás.**

Datos del informe que dependen de esta página y que **quedan en cuarentena**:
- Gólem nivel 25 + misión *Call of the Underworld* (§6) — ya refutado por otra vía en §4 de este documento
- Libro de los Muertos nivel 5 (§7) — *no refutado* (Icy Veins lo corrobora de forma independiente), pero pierde una de sus dos patas
- Lista de cinco clústeres (§3) — superada, ver §8
- Contenido del clúster Maldiciones (§8 del informe) — sin corroborar

---

## 7. ✅ Lo que el informe acierta, y ahora con mejores pruebas

### 7.1 Nivel máximo 70 — CONFIRMADO independientemente
El informe solo tenía keengamer. Fuente independiente:
> «With this change, the level cap has also been increased from 60 to 70.» — https://mobalytics.gg/diablo-4/guides/everything-lord-of-hatred

### 7.2 Rango máximo 5 → 15 — CONFIRMADO independientemente
El informe solo tenía Forbes. Fuente independiente:
> «You can invest up to 15 skill points into each active skill.» — https://maxroll.gg/d4/getting-started/skill-trees

### 7.3 Pasivas y Pasiva Clave fuera del árbol — CONFIRMADO independientemente
> «Passives on the Skill Tree are gone, with many Passives and Key Passives moving to Uniques.» — https://mobalytics.gg/diablo-4/guides/everything-lord-of-hatred

Y la Pasiva Clave, esta vez citada de la página de verdad y no de un buscador:
> «The capstone "Key Passive" slot every class caps out with is being removed entirely. Replaced by expanded branching within the tree.» — https://diablobytes.com/diablo-iv/guides/skill-tree-rework/

### 7.4 Los 23 y 33 puntos son datos muertos — CONFIRMADO, y ahora con la partida de defunción
El informe dedujo que eran viejos. **Aquí está la prueba documental** que le faltaba: una página que expone el modelo completo *y se fecha a sí misma en 2024*:

> «Basic Skills: 0 points · Core Skills: 2 points spent · Unique Class Skills: 6, 11, 16 points spent · **Ultimate Skills: 23 points spent** · **Key Passives: 33 points spent**»
> «59 Skill Points are granted from levels 1 to 60» · «an additional 12 Skill Points are available from Renown» · «There are only 71 total skill points»
> — https://game8.co/games/Diablo-4/archives/402759 — **Última actualización: 13 de octubre de 2024**

Los 23 y 33 del encargo son **literalmente** los umbrales del sistema anterior, de una página de octubre de 2024, con un cap de nivel 60 y 71 puntos totales. La §5 del informe es correcta y su razonamiento («el 33 se autodestruye porque las pasivas ya no existen») queda validado.

*Además*: el «12 por Renown» de 2024 explica probablemente **por qué circula un 12** y por qué es fácil confundirlo con el 12 del Rango de Temporada. No confundir las dos vías.

### 7.5 «2 de 3 variantes sin expansión» — CONFIRMADO, con fuente mucho mejor
El informe se apoyaba en thephrasemaker (citado vía búsqueda). Fuente directa y mejor:
> «The base game provides **2 Variant nodes per Skill**, and anyone with the Lord of Hatred expansion gets **one extra Variant node**.» — https://maxroll.gg/d4/getting-started/skill-trees

Corroborado por Mobalytics, que además precisa **dónde** está la puerta de pago:
> «The first two skill branches apply general modifiers. The **third branch** has Bonus Skill Variants **when you have the Lord of Hatred expansion**.»

**Matiz que corrige al informe:** no es «pierdes 1 opción de 3 dentro de una ranura». Es que **la tercera rama entera** de cada habilidad está cerrada sin expansión. Para un objetivo min-max en juego base, esta es la limitación estructural real, y está mejor documentada de lo que el informe suponía. El aviso de §1 del informe («el techo teórico de build sí está tocado por la expansión») es **correcto**.

### 7.6 Reddit y d4builds inaccesibles — CONFIRMADO
- `reddit.com` → **bloqueado por política** también en el panel de navegador, no solo en WebFetch. No es subsanable.
- `d4builds.gg/skill-tree/` → 404; la raíz devuelve «Page Not Found».
- `wowhead.com/diablo-4/guide/skill-tree-overview` → 404.
- En cambio **sí conseguí abrir**, y el informe no: **diablobytes.com**, **mobalytics.gg**, **iggm.com**, **game8.co**, **kami-labs.fr**, **timesaver.gg**.

### 7.7 Fuentes vetadas — CONFIRMADO, sin infracciones
Ningún dominio de la lista veda (fextralife, primagames, beebom, gamespot, segmentnext, studioloot, gamerguides, pcgamesn, mythicdrop) respalda ningún número del informe. **Cumplimiento limpio.**

⚠️ **Pero la lista veda no es un certificado de calidad.** El informe apoya datos en keengamer, thephrasemaker, skycoach, ezg.com, esports.net y allthings.how — agregadores de la misma familia editorial que los vetados, que simplemente no estaban en la lista. Y el caso Maxroll `necromancer-class-overview` (§6) demuestra que **una fuente de primera fila también publica texto muerto con fecha viva**. El criterio útil no es el dominio: es el **test de huella** (¿la página conoce el rango 15, las Transformation variants y los esbirros en el árbol?).

---

## 8. 🟡 Un hueco que el informe declaró y que no era un hueco

El informe deja abierto en «No encontrado» el punto 9: *«Si el clúster Corpse es un clúster propio o parte de Macabras. Icy Veins lo separa, Maxroll no lo lista.»*

**Estaba resuelto en la página que citó:**
> «The Skill tree is divided into **6 clusters**.» — https://maxroll.gg/d4/getting-started/skill-trees

Seis clústeres: Básicas, Fundamentales, Cadáver, Macabras, Maldiciones, Definitivas. Icy Veins tiene razón; Maxroll no lo contradice, solo que el informe leyó la lista de la página *contaminada* (`necromancer-class-overview`, §6) en vez de la buena. **Hueco cerrado: son 6.**

---

## 9. 🟠 Una cita bien copiada pero mal etiquetada

El informe pone en su tabla de §1:

| Coste de una **habilidad completa** | «It takes exactly four skill points to get the skill and the next three nodes for those modifiers» |

La cita es literal y correcta. **La etiqueta es engañosa.** El mismo artículo de Forbes dice que una habilidad cuesta del orden de **15 puntos**:

> «after investing in 4-5 of 6 available skills (**requiring roughly 15 points each**)…»
> «dozens and dozens of skill points that just sort of sit around and are dumped into a pile after level 30-40 or so»
> — https://www.forbes.com/sites/paultassi/2026/04/30/…

Los 4 puntos son «la habilidad + sus tres primeros nodos de modificador», **no** una habilidad completa. Con rango máximo 15 confirmado, llamar «completa» a 4 puntos induce a error en un plan de gasto min-max, que es justo para lo que el jugador va a usar la tabla.

*Nota adicional:* el propio Forbes dice sobre el desbloqueo «**I believe** you unlock every single modifier node by level 40» — es una impresión hedgeada de un periodista, no un dato. El informe la usó en su tabla de §3 (fila «~40») sin marcar la reserva.

---

## 10. Sigue sin haber fuente primaria de Blizzard

Confirmo el punto 1 del «No encontrado» del informe, y lo empeoro: **yo tampoco he conseguido ni una cifra del árbol escrita por Blizzard.**

- `news.blizzard.com/…/24261474` (Lord of Hatred Developer Update Stream Announce Blog) — **abierto**: solo anuncia el directo del 23 de abril, sin mecánicas ni números.
- `maxroll.gg/d4/news/lord-of-hatred-3-0-2-patch-notes` — **abierto**: correcciones y balance, nada del sistema de desbloqueo.
- El *Developer Update – Lord of Hatred Overview* en Steam (post oficial de Blizzard) — **no legible**: la página queda tras un muro de consentimiento de cookies y **no he interactuado con él**, por política de privacidad.

**Todo lo estructural de ambos informes —el auditado y este— sigue viniendo de terceros.** Ninguna cifra de árbol de este expediente tiene respaldo primario.

---

## 11. Qué debe corregirse en el informe original

1. **Borrar** la cita de DiabloBytes sobre «level brackets / no arbitrary skill point totals». No existe. Sustituirla por la cita real de Pasiva Clave, que sí verifiqué.
2. **Corregir 69 → 68** puntos por nivel, con la cita completa de Maxroll.
3. **Corregir 14 → 12** puntos de Rango de Temporada, o como mínimo invertir la carga: 12 es la posición mayoritaria (4 fuentes, incluida la propia Maxroll) y 14 la minoritaria (2 páginas de la misma casa).
4. **Retirar** «69 + 14 = 83 cuadra exactamente». Con las cifras reales: **68 + 12 = 80**, y los 3 restantes son un hueco, probablemente Renown, sin confirmar.
5. **Reescribir §6 y §7** partiendo de que **los esbirros viven ahora en el árbol de habilidades**. Retirar el consejo de esperar *Call of the Underworld* al nivel 25.
6. **Degradar** `maxroll.gg/d4/resources/necromancer-class-overview` a fuente contaminada (dice rango máximo 5 y «una de dos mejoras»).
7. **Suavizar** «todas las fuentes dicen nivel» → «dos fuentes post-3.0 verificadas dicen nivel para los clústeres; Mobalytics dice que se puede asignar en cualquier parte a cualquier nivel; las mejoras dentro de cada habilidad sí van por puntos invertidos».
8. **Reetiquetar** los 4 puntos de Forbes como «habilidad + 3 modificadores», no «habilidad completa».
9. **Cerrar** el hueco nº 9: son **6 clústeres**.
10. **Añadir** el matiz de la tercera rama: sin expansión se pierde **la rama entera**, no una opción de tres.
11. **Mantener sin cambios**: §5 (23/33 muertos, ahora con prueba de Game8), el aviso de comprobación en el juego de §0, y la lista de comprobaciones finales — que sigue siendo el consejo más valioso de todo el documento.

---

## 12. Veredicto

**PARCIAL.**

La **tesis** del informe —los clústeres van por nivel de personaje, el modelo de 23/33 puntos gastados está muerto, y la tabla que el jugador refutó mezclaba dos sistemas distintos— **sobrevive a la auditoría**, y con apoyo probatorio más sólido del que el propio informe reunió.

Sus **números confirmados no sobreviven**: 69 es 68, 14 es 12, y la suma «exacta» de 83 era circular. Su §6 y §7 describen un subsistema que el rework desplazó. Y apoyó su conclusión más importante en **una cita que no existe en la fuente a la que se atribuye**.

El informe fue honrado señalando huecos (declara 11), pero **no aplicó su propio escepticismo de forma simétrica**: fue implacable con las fuentes que le contradecían y confiado con las que le confirmaban. La ironía es que diagnosticó con precisión la enfermedad —«guías que republican cifras muertas con fecha nueva»— y luego se apoyó en una página enferma (Maxroll `necromancer-class-overview`) por ser la más reciente por fecha.

**Su mejor frase sigue siendo verdad, y ahora aún más: «Un vistazo del jugador vale más que las 16 páginas que he abierto.»** Yo he abierto 20 y la conclusión no cambia. Que el jugador mire el texto del candado.
