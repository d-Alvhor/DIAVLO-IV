# Orden de gasto de puntos — Nigromante de esbirros (Minion / Reaper Summoner)
### Diablo IV, Season 14 "Death Awakening" · árbol nuevo post-parche 3.0 · expresado en PUNTOS GASTADOS

> **Investigación:** 18 de agosto de 2026.
> **Jugador objetivo:** principiante absoluto, Nigromante, **solo juego base** (sin Vessel of Hatred, sin Lord of Hatred), en dúo, min-max.
> **Leyenda:** ✅ = disponible en juego base · 🔒 = requiere expansión · ⚠️ = dato en conflicto entre fuentes · ❓ = no confirmado.

---

## 0. AVISO PREVIO — un conflicto que NO puedo cerrar y no voy a maquillar

El encargo daba por sentado que los clústeres del árbol se desbloquean **por puntos gastados** y citaba "23 puntos para el clúster de Definitivas, 33 para el de Pasivas Definitivas".

**No he encontrado ni una sola fuente que diga eso.** Todas las fuentes vivas que he podido abrir —incluidos los datos de juego extraídos— dicen **nivel de personaje**:

| Qué dice la fuente | Fuente |
|---|---|
| "The Skill tree is divided into 6 clusters. **Each cluster is unlocked as you gain more levels**, and the upgrades within each cluster unlock in a staggered fashion." | https://maxroll.gg/d4/getting-started/skill-trees (act. 26 abr 2026) |
| "The new Lord of Hatred expansion Skill Tree unlocks in stages... For example, **Necromancer Curses unlock at level 13**... **Skill points from the Season Rank System or Renown do not affect Skill Tree progress**" | https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/ (act. 1 jul 2026) |
| "As you level up, more and more branches gradually unlock at **specific level thresholds**." / "**Until level 3** you can only invest Basic Skills before you unlock the other sections." | https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide (act. 30 jun 2026) |
| El campo del fichero de datos del planificador se llama literalmente **`requiredLevel`**, con valores 1/3/4/8/13/19 en los nodos raíz de clúster | https://assets-ng.maxroll.gg/d4-tools/game/data.min.json (versión de datos `3.1.0.72698`) |

Además, el detalle **"Skill points from the Season Rank System or Renown do not affect Skill Tree progress"** es incompatible con un modelo de puros puntos gastados: si el desbloqueo fuese por puntos gastados, esos puntos contarían.

**Los números 23 y 33 no aparecen como umbrales de puntos en ninguna fuente.** El 23 sí aparece en la tabla de Maxroll, pero como el **nivel** al que se abren las variantes del quinto clúster. El 33 no aparece en absoluto.

**Cómo lo he resuelto:** te doy la secuencia en **puntos acumulados** (que es lo que pediste, y es válida sea cual sea el modelo de desbloqueo), y aparte te doy la tabla de niveles tal y como la publican las fuentes, para que la contrastes con el juego delante. Si en tu pantalla pone "puntos gastados", la secuencia de la sección 2 te sigue sirviendo tal cual; solo cambiaría el momento en que se abre cada rama.

**Nota de versión:** los datos extraídos del planificador de Maxroll declaran versión **3.1.0.72698**, mientras que el parche vivo es 3.1.3. Puede haber deriva.

---

## 1. Estructura del árbol nuevo (lo confirmado)

### 1.1 Reglas generales ✅ (gratis para todos, no hace falta expansión)

| Dato | Valor | Fuente |
|---|---|---|
| Rework del árbol, subida de nivel máximo y filtro de botín | **Gratis para todos** | https://diablobytes.com/diablo-iv/guides/skill-tree-rework/ — "the full rework is free to every D4 player. You do not need to buy the expansion to get the new trees, the level cap raise, or the loot filter" |
| Nivel máximo | **70** (antes 60) | https://diablobytes.com/diablo-iv/guides/skill-tree-rework/ — "Level Cap 60 → 70" |
| Pasiva Clave (Key Passive) | **Eliminada** | https://diablobytes.com/diablo-iv/guides/skill-tree-rework/ — "The capstone 'Key Passive' slot every class caps out with is being removed entirely. Replaced by expanded branching within the tree." |
| Rangos máximos por habilidad activa | **15** | https://maxroll.gg/d4/getting-started/skill-trees — "You can invest up to 15 skill points into each active skill." |
| Nº de clústeres | **6** | https://maxroll.gg/d4/getting-started/skill-trees |
| Coste de reespecializar | **0 oro**, y refund automático al parche | https://diablobytes.com/diablo-iv/guides/skill-tree-rework/ — "Respec Cost $0 (gold) / Auto Refund Yes" |
| Nodos de Variante por habilidad | **2 en juego base** ✅, **3 con Lord of Hatred** 🔒 | https://maxroll.gg/d4/getting-started/skill-trees — "The base game provides 2 Variant nodes per Skill, and anyone with the Lord of Hatred expansion gets one extra Variant node to choose from." |
| Estructura por habilidad | 1 nodo de habilidad (15 rangos) + **par de modificadores A** (elige 1) + **grupo de Variantes** (elige 1) + **par de modificadores B** (elige 1) | Derivado de los grupos del fichero de datos (`group` 215/216/217 para Skeleton Mage, etc.), https://assets-ng.maxroll.gg/d4-tools/game/data.min.json |

### 1.2 ⚠️ Conflicto sobre el total de puntos

| Total | Desglose | Fuente |
|---|---|---|
| **80** | 68 por subir de nivel (nv2→nv69) + 12 de Rango de Temporada | https://maxroll.gg/d4/getting-started/skill-trees |
| **83** | 69 por subir de nivel + 14 de Rango de Temporada / Renombre | https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide — "You can unlock 14 extra skill points for a total of 83." |
| **83** | 69 por nivel + 14 de Rango de Temporada / Renombre | https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/ — "Use the Skill Tree above to complete the 83-point build. 69 skill points are gained by leveling, and 14 skill points are locked behind the Season Rank System or Renown" |
| **hasta 83** | "up to 83 available Skill Points" | Nota de prensa del parche 3.0.0 (vía búsqueda; ver sección "No encontrado") |

El planificador real de Maxroll **suma exactamente 83 puntos** en su paso final, así que 83 es el número operativo. La página general de Maxroll (80) parece desactualizada respecto a sus propias guías.

### 1.3 Tabla de desbloqueo por nivel (según las fuentes, no según el encargo)

Reproduzco la tabla de Maxroll y la contrasto con los `requiredLevel` del fichero de datos. **Coinciden exactamente**, valor por valor.

| Clúster | Habilidad | Modificadores A | Modificadores B | Variantes 1 y 2 ✅ | Variante LoH 🔒 |
|---|---|---|---|---|---|
| 1 · Básicas | 1 | 5 | 9 | 14 | 30 |
| 2 · Core / Esencia | 3 | 6 | 10 | 15 | 32 |
| 3 · (Cadáver + Guerreros) | 4 | 7 | 11 | 16 | 34 |
| 4 · (Macabras + Gólem) | 8 | 12 | 17 | 20 | 36 |
| 5 · Maldiciones | 13 | 18 | 21 | 23 | 38 |
| 6 · Definitiva | 19 | 22 | 24 | 25 | 40 |

Fuente de la tabla: https://maxroll.gg/d4/getting-started/skill-trees
Verificación cruzada: nodos raíz con `root:1` y `requiredLevel` 3, 4, 8, 13, 19 en https://assets-ng.maxroll.gg/d4-tools/game/data.min.json

> Ese **23** de la fila "Maldiciones / Variantes" es, casi con seguridad, el origen del "23 puntos para Definitivas" que circulaba. No es un umbral de puntos y no es del clúster de Definitivas.

### 1.4 Qué habilidad vive en qué clúster (dato duro, no inferencia)

Esto lo he derivado del propio fichero de datos: la columna "Variante LoH" tiene un `requiredLevel` distinto por clúster (30/32/34/36/38/40), así que la variante bloqueada de cada habilidad identifica su clúster sin ambigüedad. Coincide además con la posición geométrica de los nodos y con el "Curses unlock at level 13" de Icy Veins.

| Clúster (nivel raíz) | Habilidades activas del Nigromante |
|---|---|
| 1 · Básicas (nv 1) | Bone Splinters, **Reap**, Decompose, Hemorrhage |
| 2 · Core/Esencia (nv 3) | Bone Spear, Blight, Blood Surge, Blood Lance, **Sever**, **⭐ Skeleton Mage** |
| 3 · (nv 4) | Corpse Explosion, **Corpse Tendrils**, **⭐ Skeleton Warrior** |
| 4 · (nv 8) | Blood Mist, Bone Spirit, Bone Prison, **⭐ Golem** |
| 5 · Maldiciones (nv 13) | **Iron Maiden**, Decrepify |
| 6 · Definitiva (nv 19) | **Army of the Dead**, Bone Storm, Blood Wave, Soulrift |

**Esto es lo que probablemente rompió la investigación anterior.** En el árbol nuevo:
- **Skeleton Mage es una habilidad CORE** (clúster de nivel 3). Por eso "nivel 3 → Core" y "empieza a meter puntos en Skeleton Mage a nivel 3" son la misma frase.
- **Skeleton Warrior está en el clúster de nivel 4**, no en un clúster de esbirros aparte.
- **Golem está en el clúster de nivel 8** junto a las Macabras.
- **"Reapers" NO es un nodo del árbol.** Es una especialización del **Libro de los Muertos**, un sistema distinto. Mezclar ambas cosas en una sola tabla "nivel → cosa" es exactamente el error que detectaste.

---

## 2. EL ORDEN DE GASTO DE PUNTOS — secuencia real, paso a paso

**Origen:** planificador oficial de la guía de Maxroll, perfil "Leveling", extraído vía la API del planificador.
- Guía: https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide (act. 30 jun 2026, Season 14)
- Planificador: https://maxroll.gg/d4/planner/7xf3kf0h
- Datos crudos: https://planners.maxroll.gg/profiles/d4/7xf3kf0h (JSON, fecha del build `2026-07-22`)

El planificador guarda 8 "pasos" (`skillTree.steps`), cada uno un estado acumulado del árbol. He decodificado los IDs de nodo contra el fichero de datos del juego. **Todos los nodos de esta ruta de subida son ✅ juego base: no usa ni una sola variante de Lord of Hatred.**

### PASO 1 — 3 puntos acumulados ✅
| Nodo | Qué es | Rangos |
|---|---|---|
| Reap | Habilidad Básica | 3 |

*Punto 1, 2 y 3 → Reap.* Es puro relleno hasta que se abre el clúster Core; Maxroll lo dice explícitamente: "Until level 3 you can only invest Basic Skills... Reap is a good choice to get you to your ability to begin summoning your mighty army."

### PASO 2 — 4 puntos acumulados ✅ (RESPEC)
| Nodo | Qué es | Rangos |
|---|---|---|
| **Skeleton Mage** | Habilidad Core ⭐ | 4 |
| ~~Reap~~ | retirado | 0 |

*Se reembolsan los 3 de Reap y se meten los 4 en Skeleton Mage.* Maxroll: "At level three, you swap Reap out and begin putting your points into Skeleton Mage." **El respec es gratis, úsalo sin miedo.**

### PASO 3 — 7 puntos acumulados ✅
| Nodo | Qué es | Rangos |
|---|---|---|
| Skeleton Mage | Core ⭐ | 3 (baja de 4) |
| **Corpse Tendrils** | Clúster nv4 | 1 |
| **Skeleton Warrior** | Clúster nv4 ⭐ | 1 |
| Skeleton Mage: *Duration Damage Bonus* | Modificador A | 1 |
| Skeleton Warrior: *Damage Bonus* | Modificador A | 1 |

### PASO 4 — 12 puntos acumulados ✅
| Nodo | Qué es | Rangos |
|---|---|---|
| **Golem** | Clúster nv8 ⭐ | 1 |
| Golem: *Unstoppable* | Modificador A | 1 |
| Corpse Tendrils: *Critical Strike Chance* | Modificador A | 1 |
| Skeleton Mage: *Ferocity, Resolve, or Overpower* | Modificador B | 1 |
| Skeleton Warrior: *Resolve* | Modificador B | 1 |

### PASO 5 — 18 puntos acumulados ✅
| Nodo | Qué es | Rangos |
|---|---|---|
| **Iron Maiden** | Maldición, clúster nv13 | 1 |
| Skeleton Warrior | ⭐ | 2 (sube de 1) |
| **Skeleton Mage: *Coven*** | **VARIANTE** — "+2 magos" | 1 |
| **Skeleton Warrior: *Master of Puppets*** | **VARIANTE** — "+3 guerreros" | 1 |
| Corpse Tendrils: *Vulnerable* | Modificador B | 1 |
| Golem: *Resolve, Overpower, or Ferocity* | Modificador B | 1 |

> Aquí está el primer salto de potencia real: las dos variantes que **añaden esbirros** (Coven +2 magos, Master of Puppets +3 guerreros). Ambas ✅ juego base.

### PASO 6 — 26 puntos acumulados ✅
| Nodo | Qué es | Rangos |
|---|---|---|
| **Army of the Dead** | Definitiva, clúster nv19 | 1 |
| **Army of the Dead: *Unyielding Commander*** | **VARIANTE ✅** — esbirros reciben 90% menos daño y tú haces 50%[x] más daño de invocación | 1 |
| Army of the Dead: *Cooldown Reduction* | Modificador A (−20 s de reutilización) | 1 |
| Army of the Dead: *Corpse Generation* | Modificador B (50% de generar cadáver) | 1 |
| **Golem: *Gravebloom*** | **VARIANTE ✅** — 3 gólems pequeños al 60% de daño y +30%[+] vel. ataque | 1 |
| Iron Maiden: *Schadenfreude* | **VARIANTE ✅** — Espinas + daño de Iron Maiden aumentado | 1 |
| Iron Maiden: *Essence Generation* | Modificador B — Iron Maiden deja de costar Esencia y **genera 5 por enemigo maldito** | 1 |
| Skeleton Warrior | ⭐ | 3 (sube de 2) |

### PASO 7 — 40 puntos acumulados ✅
| Nodo | Rangos |
|---|---|
| **Iron Maiden** | **1 → 15** |

*14 puntos seguidos a Iron Maiden.* Este es el paso que descoloca a todo el mundo y tiene una explicación mecánica: ver sección 4.

### PASO 8 — 83 puntos acumulados (build completa) ✅
| Nodo | Rangos |
|---|---|
| Skeleton Mage ⭐ | 3 → **15** |
| Skeleton Warrior ⭐ | 3 → **15** |
| Golem ⭐ | 1 → **15** |
| Army of the Dead | 1 → **6** |
| Skeleton Warrior: *Vulnerable* (Mod. B) | 0 → 1 |
| ~~Skeleton Warrior: *Resolve*~~ | retirado (se cambia por *Vulnerable*) |

### Resumen en una línea

```
3 pts Reap → [respec] 4 pts Skeleton Mage → 7 pts +Tendrils +Warrior
→ 12 pts +Golem → 18 pts +Iron Maiden +variantes de nº de esbirros
→ 26 pts +Army of the Dead (Unyielding Commander) → 40 pts Iron Maiden a 15
→ 83 pts Mage/Warrior/Golem a 15, AotD a 6
```

### Prioridad por clúster (el mínimo que pediste)

1. **Core / Esencia (nv3)** → Skeleton Mage. Primero y por delante de todo.
2. **Clúster nv4** → Skeleton Warrior + Corpse Tendrils.
3. **Clúster nv8** → Golem.
4. **Maldiciones (nv13)** → Iron Maiden.
5. **Definitiva (nv19)** → Army of the Dead, solo por *Unyielding Commander*.
6. **Básicas (nv1)** → cero puntos permanentes. Solo aparcamiento inicial.

---

## 3. Versión recortada real para juego base (sin VoH ni LoH)

### 3.1 La ruta de SUBIDA (1→70) es 100% jugable en juego base ✅

He comprobado nodo por nodo la ruta del paso 1 al 8: **no usa ninguna variante de Lord of Hatred**. Es la mejor noticia del informe. Lo único que tienes que ignorar de la guía de Maxroll es la sección de Runas y la de Mercenarios.

### 3.2 La build de ENDGAME publicada **sí** depende de expansión 🔒

Decodificando los perfiles de endgame del mismo planificador (`Starter`, `Mid Game`, `Warrior`, `Mages`, `Zookeeper`), **todos y cada uno** usan variantes exclusivas de Lord of Hatred:

| Perfil de endgame (Maxroll) | Nodos 🔒 LoH que usa |
|---|---|
| Starter | Golem: *Gargantua*, Iron Maiden: *Blood Maiden* |
| Mid Game | Golem: *Gargantua*, Iron Maiden: *Blood Maiden*, Decrepify: *Unholy Frenzy* |
| Warrior | Golem: *Gargantua*, Iron Maiden: *Blood Maiden* |
| Mages | Golem: *Gargantua*, Iron Maiden: *Blood Maiden*, Skeleton Warrior: *Litany of Death* |
| Zookeeper | Golem: *Gargantua*, Iron Maiden: *Blood Maiden*, Blood Wave: *Hematolagnia* |

Fuente: https://planners.maxroll.gg/profiles/d4/7xf3kf0h decodificado contra https://assets-ng.maxroll.gg/d4-tools/game/data.min.json

### 3.3 Tabla de sustitución: qué coger en lugar de cada variante bloqueada

Cada habilidad tiene 3 variantes; a ti solo te salen 2. Esta es la lista completa para las habilidades que te importan:

| Habilidad | Variante 🔒 LoH (no la verás) | Tus 2 opciones ✅ base | Cuál usar |
|---|---|---|---|
| **Skeleton Mage** | *Singularity* | *Coven* (+2 magos) · *Gift of Death* (pasa a ser hab. de Cadáver, +regen. Esencia) | **Coven** — es la que usa la ruta de subida |
| **Skeleton Warrior** | *Litany of Death* (invoca Sacerdote Esqueleto) | *Master of Puppets* (+3 guerreros) · *Service and Sacrifice* (pierden 25% vida/s y explotan) | **Master of Puppets** |
| **Golem** | *Gargantua* (gólem grande con aura de +vel. lanzamiento y movimiento a los esbirros) | *Gravebloom* (3 gólems al 60% daño, +30%[+] vel. ataque) · *Fel Gluttony* (erupción al comandar; consume cadáveres para reducir reutilización 2 s por cadáver) | **Gravebloom** — es la de la ruta de subida |
| **Iron Maiden** | *Blood Maiden* (pasa a hab. de Sangre, orbes) | *Schadenfreude* (Espinas + más daño) · *Torture Artist* (hab. de Oscuridad, daño de Sombra, 30% aturdir 2 s) | **Schadenfreude** por defecto |
| **Army of the Dead** | *Dead Cold* (daño de Frío, Congela) | ***Unyielding Commander*** · *Pile the Bodies* | **Unyielding Commander** ✅ — la variante clave de la build **NO está bloqueada** |
| **Corpse Tendrils** | *Jaws Of Death* | *Bitter Harvest* (no consume el cadáver, Inmoviliza 3 s) · *Get Over Here!* (se lanza sobre ti, Fortifica 5% vida por enemigo) | Ruta de subida no coge variante aquí; endgame de Maxroll usa *Get Over Here!* |
| **Sever** | *Cold Pursuit* | *Reaping Lotus* (3 espectros extra) · *Inexorable Reaper* (pasa a hab. de Movilidad, embiste) | *Inexorable Reaper* (lo que usan las guías) |
| **Decrepify** | *Unholy Frenzy* (la maldición pasa a **tus esbirros**: +vel. lanzamiento y movimiento) | *Life Tap* (hab. de Sangre, cura) · *Dizzying Curse* (Aturde la 1ª vez) | Pérdida real; ver abajo |

Fuente de todas las descripciones: fichero de datos del juego, https://assets-ng.maxroll.gg/d4-tools/game/data.min.json (versión `3.1.0.72698`).

**Lo que pierdes de verdad sin LoH, en orden de gravedad:**
1. **Golem: Gargantua** 🔒 — aura de velocidad de lanzamiento y movimiento para **todos** tus esbirros. Es el pegamento de la build de endgame. Sustituto ✅: *Gravebloom* (3 gólems, +30% vel. ataque). No es lo mismo, pero funciona.
2. **Decrepify: Unholy Frenzy** 🔒 — convierte la maldición en un buff de esbirros. Sin ella, Decrepify vuelve a ser una maldición normal y pierde su hueco en la build de esbirros.
3. **Iron Maiden: Blood Maiden** 🔒 — sustituible por *Schadenfreude* sin drama.
4. **Skeleton Warrior: Litany of Death** 🔒 — solo lo usa el perfil "Mages".

### 3.4 Sistemas completos que NO tienes

| Sistema | Estado | Impacto en esta build | Fuente |
|---|---|---|---|
| **Mercenarios** (Raheir, Aldkin, Varyana, Subo) | 🔒 Vessel of Hatred | Maxroll recomienda Raheir contratado + Aldkin de refuerzo; Icy Veins recomienda Varyana. **Nada de esto existe para ti.** | https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide — "Mercenaries are unlocked during the Vessel of Hatred campaign" |
| **Runas y Runewords** (Nagu, Ceh, Igni, Wat, Que, Cir, Kry, Cem, Gar) | 🔒 Vessel of Hatred | Maxroll da como BiS `Cir + Ceh` y `Cem + Gar`. Icy Veins hace que **Decrepify se aplique solo** vía `Igni + Wat`, y por eso lo saca de la barra. **Sin runas, Decrepify tiene que ir en la barra o no va.** | https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide (sección Runes) · https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/ |
| **Talismanes y Charms** (Sello Horádrico, set Black Shroud) | 🔒 Lord of Hatred | La build "Reaper Summoner" de Icy Veins está **construida alrededor** del set de Charms *Berú of the Black Shroud*. Sin LoH esa build no existe. | https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/ — "The Lord of Hatred expansion introduces Talismans as a new character progression and itemization layer" |
| **Cubo Horádrico** | 🔒 Lord of Hatred | Icy Veins lo exige para imprimar *Tidal Aspect* en el Banished Lord's Talisman | https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/ |
| **War Plans / Skovos / Echoing Hatred** | 🔒 Lord of Hatred | Maxroll estructura toda la subida 1-70 alrededor de "War Plans activities" | https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide |
| **Undercity of Kurast / Nahantu** | 🔒 Vessel of Hatred | Citado como actividad de subida | https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide |
| **Variante nº3 de cada habilidad** | 🔒 Lord of Hatred | Ver 3.3 | https://maxroll.gg/d4/getting-started/skill-trees |

### 3.5 Veredicto sobre "Reaper Summoner"

La build que se llama **"Reaper Summoner"** (Icy Veins, tier A, https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/) **no es reproducible en juego base**: depende del set de Charms Black Shroud 🔒, de Gargantuan Golem 🔒, de dos Runewords 🔒, de Mercenarios 🔒 y del Cubo Horádrico 🔒.

Lo que sí es tuyo es la **ruta de subida de esbirros de Maxroll (sección 2)**, que llega a 70 sin tocar nada de expansión, y su variante de endgame recortada según la tabla 3.3.

---

## 4. Habilidades trampa para esta build

### 4.1 La trampa madre: repartir rangos pronto

Este es el dato min-max más importante que he encontrado, y explica toda la forma de la secuencia:

> "Generally, each extra skill point makes a skill 10% more powerful than it was at rank 1. So, a skill with 5/15 points will be 40% stronger than 1/15 points. **In other words, the first point you put into an active skill is 10 times more powerful than the next 4.**"
> — https://maxroll.gg/d4/getting-started/skill-trees

**Consecuencia práctica:** hasta el paso 6 (26 puntos) la ruta pone **1 rango** en casi todo y gasta los puntos en abrir modificadores y variantes. Subir Skeleton Mage a 5/15 antes de tener el Gólem y las variantes de "+2 magos / +3 guerreros" es la forma más común de tirar puntos. **Amplitud primero, profundidad al final.**

### 4.2 Trampas concretas

| Trampa | Por qué parece buena | Por qué no lo es |
|---|---|---|
| **Reap más allá de 3 rangos** | Es lo único que puedes pulsar al empezar | La ruta la reembolsa entera a los 4 puntos. Es aparcamiento, no inversión. |
| **Skeleton Warrior: *Service and Sacrifice*** ✅ | "Explotan al morir y se levantan cada 0,5 s desde cadáveres": suena a más daño | Tus esqueletos **pierden el 25% de su vida máxima por segundo en combate**. Va en contra de toda la build. Ninguno de los 6 perfiles del planificador de Maxroll la usa. |
| **Skeleton Mage: *Gift of Death*** ✅ | Regeneración de Esencia por cada mago activo | Convierte a Skeleton Mage en **habilidad de Cadáver que requiere un cadáver para invocar**. Compite por cadáveres con todo lo demás. Ningún perfil la usa: todos cogen *Coven*. |
| **Army of the Dead: *Pile the Bodies*** ✅ | "hasta 300%[x] de daño incrementado" — el número más grande de la pantalla | Escala la Definitiva, que tiene reutilización larga. *Unyielding Commander* da **90% de reducción de daño a los esbirros y 50%[x] de daño de invocación**, y las guías la mantienen activa prácticamente siempre. **Los 6 perfiles del planificador cogen Unyielding Commander.** |
| **Golem: *Fel Gluttony*** ✅ | Erupción al comandar + reduce reutilización comiendo cadáveres | Ningún perfil del planificador la usa. La elección real es Gargantua 🔒 o *Gravebloom* ✅. |
| **Iron Maiden: *Torture Artist*** ✅ | La convierte en habilidad de Oscuridad con daño de Sombra y aturdimiento | La ruta de subida coge *Schadenfreude* (Espinas + más daño de Iron Maiden) y el endgame coge *Blood Maiden* 🔒. |
| **Subir Army of the Dead por encima de 6** | Es la Definitiva, "debería" pegar más | La build acaba con AotD a **6/15** mientras Mage/Warrior/Golem van a 15/15. Se coge por la variante, no por el daño. |
| **Ignorar *Iron Maiden: Essence Generation*** | Parece un modificador menor | Hace que Iron Maiden **deje de costar Esencia y genere 5 por enemigo maldito nuevo**. Es tu motor de recurso. Va en el paso 6. |
| **Meter puntos en Básicas "por si acaso"** | Cuesta 0 recursos y genera Esencia | La build termina con **0 puntos en Básicas**. Toda la generación viene de Iron Maiden. |
| **Poner Decrepify en la build copiando la guía** | Aparece en los perfiles Mid Game / Warrior / Mages | Lo hacen por *Unholy Frenzy* 🔒 y porque el Runeword `Igni + Wat` 🔒 la aplica sola. **Sin expansión, ese hueco es tuyo para otra cosa.** |

### 4.3 Sobre el paso 7 (Iron Maiden 1 → 15)

Es el paso más contraintuitivo del planificador. La lógica declarada por Maxroll: "Iron Maiden provides you a curse that provides you with Essence generation as well as additional damage in the form of thorns. This also provides your source of curse for Amplified Damage" (https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide). El nodo *Schadenfreude* dice literalmente que **el daño de Iron Maiden aumenta** con las Espinas, y las Espinas escalan con el rango.

⚠️ **No he encontrado la explicación numérica completa de por qué 15 rangos de Iron Maiden van antes que subir a los propios esbirros.** Es el orden que guarda el planificador de Maxroll; no lo he podido verificar contra prosa ni contra vídeo. Trátalo como "lo que dice Maxroll", no como ley.

---

## 5. Libro de los Muertos (Book of the Dead) — zona de datos podridos ⚠️

Este es el sistema donde la investigación anterior se estrelló, y sigo sin poder cerrarlo.

**Lo que sí es sólido:** las especializaciones (Skirmishers / Defenders / **Reapers**; Shadow / Cold / Sacrifice; Bone / Blood / Iron) **siguen existiendo** en el parche actual — aparecen en el fichero de datos vivo como `Necromancer_SkeletonWarrior_Reaper_Passive_UpgradeA/B/Sacrifice`, etc. (https://assets-ng.maxroll.gg/d4-tools/game/data.min.json, versión `3.1.0.72698`). **No** son nodos del árbol de habilidades: son un sistema aparte.

**Lo que está en conflicto abierto:**

| Fuente | Qué dice | Fecha |
|---|---|---|
| Maxroll, guía de subida | "**At level 15**, you can unlock your class mechanic called Book of the Dead." | 30 jun 2026 |
| Maxroll, recurso dedicado | "You unlock the UI Menu for the Book of the Dead **at Level 5**" / "at level 25 you unlock a Quest to summon your Golem" | **⚠️ Última actualización: 4 oct 2024 — anterior al rework. NO FIABLE.** |
| Icy Veins, guía de subida | Nivel 5: Warrior→Skirmishers [Mej. 1] y Mage→Shadow [Mej. 2]; **Nivel 8**: Golem→Bone [Mej. 1]; **Nivel 12**: Warrior→**Reapers** [Mej. 1]; Nivel 50: Golem→Bone [Sacrificio] y Warrior→Reapers [Mej. 2] | 1 jul 2026 |

- URLs: https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide · https://maxroll.gg/d4/resources/necromancer-book-of-the-dead · https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/

**Los "nivel 8 → Gólem" y "nivel 12 → Reapers" que refutaste vienen de Icy Veins**, y se refieren al Libro de los Muertos, no al árbol. Al mismo tiempo, en el árbol nuevo el Gólem **sí** está en el clúster de nivel 8 (sección 1.4) — dos cosas distintas que caen en el mismo número, lo cual hace la confusión casi inevitable.

**Recomendación de elecciones (según las guías, elige según lo que te salga en pantalla):**

| Ranura | Subida (Maxroll) | Endgame (Icy Veins, Reaper Summoner) |
|---|---|---|
| Guerreros | **Defenders** (espinas extra) | **Reapers [Mejora 2]** — 50%[x] más daño y 15% de Aturdir 1 s |
| Magos | **Shadow** (genera barrera) | **Shadow [Mejora 2]** — barrera por impacto, hasta 42% de vida máx. |
| Gólem | **Blood** (imparable + fortificar) | **Iron [Sacrificio]** — +15%[x] daño crítico, el Gólem hace 50%[x] menos daño |

(La guía de subida de Icy Veins propone en cambio Golem: **Bone [Sacrificio]** — "+10%[+] Attack Speed y el Gólem hace 50%[x] menos daño". Tres fuentes, tres recomendaciones de gólem distintas: elige por lo que necesites, no por copiar.)

---

## 6. Cosas útiles que salieron de paso (juego base ✅ salvo marca)

**Aspectos legendarios recomendados para la subida** (https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide): Frenzied Onslaught, Reanimation, **Hellbent Commander**, Hardened Bones, Amplified Damage, Vehement, Brawler's.

**Únicos que buscar** (misma fuente): The Undercrown, The Hand of Naz, Deathgrip, Blood Moon Breeches.
Icy Veins añade para endgame: Pact of Bone, Bloodless Scream, Lidless Wall, Banished Lord's Talisman 🔒 (es un Talismán).

**Prioridad de glifos de Paragón para la subida** (https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide): Dominate → Scourge → Warrior → Deadraiser → Abyssal.
❓ Vi en resultados de búsqueda que el glifo **Dominate** habría sido nerfeado fuerte en Season 14, pero no pude abrir la página que lo afirma. **No lo des por bueno.** Ver sección "No encontrado".

**Consejo de imprimación con fuente:** "Ideally, put your best Offensive Aspect on your Amulet, since it is usually not replaced as often as other gear" — el amuleto aplica el aspecto **al 150%** (https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/).

**Umbral de endgame:** "Complete Pit Tier 10 to enter Torment 1" (https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide).

---

## 7. Qué hacer con esto, en concreto

1. **Abre el árbol en el juego y mira qué pone el tooltip del candado de un clúster.** Si dice "Nivel X", la sección 1.3 es correcta y la premisa de "puntos gastados" está muerta. Si dice "X puntos gastados", avísame: significa que todas las fuentes vivas (y los datos extraídos) van con retraso respecto a 3.1.3.
2. **Sigue la secuencia de la sección 2 tal cual.** Es válida en ambos modelos porque está expresada en puntos acumulados.
3. **Reespecializar es gratis.** El paso 2 ya te obliga a hacerlo. Hazlo sin ceremonia cada vez que se abra un clúster nuevo.
4. **Ignora sin culpa** todo lo que hable de Mercenarios, Runas, Runewords, Talismanes, Charms, Cubo Horádrico, War Plans y Skovos.
5. **En dúo, ojo con solapar:** si tu pareja también va de esbirros, *Unyielding Commander* (90% red. daño a esbirros) no se suma entre vosotros — no lo he verificado, es una pregunta abierta, no una afirmación.

---

## Fuentes

**Abiertas y leídas con éxito:**

- https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide — guía de subida Minion Necromancer, Season 14, act. 30 jun 2026
- https://maxroll.gg/d4/build-guides/minion-necromancer-guide — guía de endgame Minion Necromancer, Season 14, act. 22 jul 2026
- https://maxroll.gg/d4/getting-started/skill-trees — Skill Tree Overview, act. 26 abr 2026 (con changelog "December 9, 2025 — Updated for Season 11: Changed number of skill points needed to hit Core skills and the 2nd skill cluster")
- https://maxroll.gg/d4/resources/necromancer-book-of-the-dead — ⚠️ act. 4 oct 2024, DESACTUALIZADA, citada solo para documentar el conflicto
- https://maxroll.gg/d4/news/diablo-iv-lord-of-hatred — anuncio de Lord of Hatred, gratis vs. de pago
- https://maxroll.gg/d4/planner/7xf3kf0h — planificador de la build (página)
- https://planners.maxroll.gg/profiles/d4/7xf3kf0h — **datos crudos del planificador en JSON**, build "Minion Endgame Necromancer", fecha `2026-07-22`. De aquí sale la secuencia paso a paso.
- https://assets-ng.maxroll.gg/d4-tools/game/data.min.json — **fichero de datos del juego** usado por el planificador, versión `3.1.0.72698`. De aquí salen los nombres de nodo, los `requiredLevel`, los grupos de variantes y la marca de exclusividad LoH.
- https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/ — Summoner Necromancer leveling, act. 1 jul 2026
- https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/ — **Reaper Summoner** endgame, act. 3 jul 2026
- https://diablobytes.com/diablo-iv/guides/skill-tree-rework/ — Skill Tree Rework Explained, act. jul 2026 (⚠️ gran parte redactada antes del lanzamiento; ver "No encontrado")
- https://news.blizzard.com/en-us/article/24271857/diablo-iv-patch-notes-3-0 — notas oficiales 3.0.x (solo contienen 3.0.1→3.0.4, correcciones; **no** el documento estructural del rework)
- https://www.wowhead.com/diablo-4/guide/classes/necromancer/skills-tree — abierta, pero **act. 11 mar 2026 y cubre Season 12**, es decir, anterior al rework del 28 abr 2026. Inservible para esto.

**Intentadas y fallidas (declaradas, no simuladas):**

- `mobalytics.gg/diablo-4/builds/minion-necromancer-endgame-build-guide` — HTTP 403 tanto por WebFetch como por petición directa. **No he leído esta página.**
- `reddit.com/r/diablo4` y `reddit.com/r/Diablo4Necromancer` — bloqueado (403 / la herramienta se niega). **Cero contenido de Reddit en este informe.**
- `d4builds.gg/builds/minion-necromancer-endgame/` — la página carga (HTTP 200) pero **el árbol es JavaScript puro**: el HTML entregado tiene 613 caracteres de texto y ninguna habilidad. No hay secuencia extraíble.
- `d4guides.gg/en/build/necromancer-negro-minion-39e56e17` — igual: SPA, el HTML dice literalmente "Loading Skill Tree...". Sin datos.
- `wowhead.com/diablo-4/guides/necromancer-builds` — 403 por petición directa.
- Herramienta de árbol de Icy Veins (`icy-veins.com/d4/tools/talent-tree/?uid=mr2jm1t8jzrh`, con `data-leveling-path="true"`): **es una app Next.js y no he encontrado su endpoint de datos.** Icy Veins dice tener una ruta de subida ordenada ("Use 'Leveling Path' toggle to see the exact order of skill allocation") pero **no he podido extraerla**. Sería la segunda opinión independiente ideal.

**Fuentes vetadas — NO usadas para ningún efecto ni número:** fextralife, primagames, beebom, gamespot, segmentnext, studioloot, gamerguides, pcgamesn, mythicdrop. Aparecieron en resultados de búsqueda (sobre todo al preguntar por el Libro de los Muertos, donde dominan los resultados con datos de 2023) y fueron descartadas.

---

## No encontrado

Lo que busqué y **no** pude confirmar. Prefiero el hueco:

1. **El modelo de "puntos gastados".** Ninguna fuente lo respalda. Cero apariciones de "23 puntos para Definitivas" o "33 puntos para Pasivas Definitivas". Tampoco encontré nada que describa un clúster de **"Pasivas Definitivas" (Ultimate Passives)**: el árbol extraído tiene 6 clústeres y ninguno de pasivas. Es coherente con "Passive nodes are no longer part of the skill tree", pero **no tengo una frase oficial de Blizzard que lo diga**.
2. **Las notas oficiales estructurales del parche 3.0.0.** La URL de Blizzard que encontré (article/24271857) contiene 3.0.1 a 3.0.4, que son correcciones. **No localicé el documento oficial de Blizzard que describa el desbloqueo de clústeres.** Todo lo estructural de este informe viene de terceros o de datos extraídos.
3. **Nivel de desbloqueo del Libro de los Muertos y de cada especialización en 3.1.3.** Conflicto abierto (nv5 vs nv15), y el único recurso dedicado de Maxroll es de octubre de 2024. **Compruébalo en el juego.**
4. **Cuántos de los 14 puntos extra son alcanzables en juego base.** Las fuentes dicen "Rango de Temporada o Renombre". El Renombre incluye regiones de expansión (Skovos 🔒, Nahantu 🔒). **No sé si llegas a 83 puntos sin expansión.** Puede que tu build real sea de menos puntos.
5. **El total real de puntos**: 80 (página general de Maxroll) vs 83 (ambas guías + planificador). No resuelto, aunque 83 tiene más peso.
6. **El nerf del glifo Dominate** ("de 23,6% a 1,8% de daño por acumulación en Season 14") apareció en un fragmento de búsqueda pero **no pude abrir la página que lo afirma**. No lo trato como cierto.
7. **La justificación numérica del paso 7** (Iron Maiden a 15 rangos antes que los esbirros). Es lo que guarda el planificador; no encontré prosa, vídeo ni hilo que lo explique.
8. **Segunda opinión independiente sobre el orden punto a punto.** Solo tengo la de Maxroll. Icy Veins la tiene pero está encerrada en JavaScript; Mobalytics, Reddit, d4builds y d4guides fueron inaccesibles o vacíos. **Todo el orden de la sección 2 depende de una sola fuente.**
9. **Si *Unyielding Commander* se solapa entre dos nigromantes en dúo.** No investigado, no afirmado.
10. **Números de daño concretos de los esbirros en 3.1.3.** Los datos extraídos son de la versión `3.1.0.72698`; no he verificado que 3.1.1/3.1.2/3.1.3 no los hayan tocado.
