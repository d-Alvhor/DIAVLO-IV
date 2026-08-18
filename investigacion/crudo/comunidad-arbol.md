# Lo que dice la COMUNIDAD del árbol nuevo (parche 3.0 / Lord of Hatred)
### Dominio: Reddit, foros oficiales y creadores · Nigromante · Juego base · S14 "Death Awakening" (3.1.3)

**Fecha de la investigación:** 18 de agosto de 2026
**Autor del encargo:** jugador principiante, Nigromante, SOLO JUEGO BASE, dúo PC + PS5, min-max, español.

---

## 0. AVISO PREVIO: dos huecos que debes leer antes que nada

### 0.1. Reddit NO se pudo abrir. Ni un hilo.

Era el núcleo de mi encargo y **fracasó por completo**. No por falta de intentos:

| Intento | Resultado |
|---|---|
| `WebFetch` sobre `www.reddit.com` | Bloqueado por el propio cliente |
| `WebFetch` sobre `old.reddit.com` | Bloqueado por el propio cliente |
| `WebSearch` restringido a `reddit.com` | Error de API: *"The following domains are not accessible to our user agent: ['reddit.com']"* |
| `curl` a `reddit.com`, `old.reddit.com`, `api.reddit.com` (JSON) | **HTTP 403** con página de bloqueo, con y sin User-Agent de navegador |
| Navegador Playwright | No hay Chrome instalado en esta máquina |
| Espejos públicos (redlib/safereddit) | Uno respondía 200, pero **decidí no usarlo**: Reddit ha bloqueado explícitamente a este agente y rodear ese bloqueo con un proxy es saltarse una restricción de acceso puesta por el titular del sitio |

**Consecuencia honesta:** todo lo que en este informe se atribuye a "la comunidad" viene de **foros oficiales de Blizzard**, no de Reddit. r/diablo4, r/Diablo4Necromancer y r/D4Necromancer siguen sin cubrir. Si quieres esa fuente, tendrás que abrirla tú desde tu navegador — y merece la pena, porque los foros de Blizzard tienen mucho menos tráfico.

### 0.2. La pregunta central (¿puntos gastados o nivel?) NO la he podido confirmar. Y encima las guías dicen lo contrario que tú.

Tú refutaste con el juego delante la tabla "nivel 3 → Core, nivel 8 → Gólem". **Yo no he encontrado ni una sola fuente que confirme el modelo por puntos gastados en el árbol post-3.0.** Al revés: tres fuentes vivas y actualizadas después del 28 de abril de 2026 dicen explícitamente **nivel**.

Lo detallo entero en la sección 2. No voy a inventar la confirmación que no tengo.

---

## 1. Qué cambió, según lo que sí está confirmado por escrito

### 1.1. Marco general del rework (✅ todo juego base salvo lo marcado)

| Dato | Valor | Fuente |
|---|---|---|
| Fecha del parche 3.0 / Lord of Hatred | 28 de abril de 2026 | https://diablobytes.com/diablo-iv/guides/skill-tree-rework/ |
| ✅ El rework es gratis para todos | *"the full rework is free to every D4 player. You do not need to buy the expansion to get the new trees, the level cap raise, or the loot filter"* | https://diablobytes.com/diablo-iv/guides/skill-tree-rework/ |
| ✅ Nivel máximo | 60 → **70** | https://diablobytes.com/diablo-iv/guides/skill-tree-rework/ · https://www.keengamer.com/articles/guides/diablo-iv-lord-of-hatred-all-new-changes-and-updates/ |
| ✅ Pasivas Clave (Key Passives) eliminadas | *"The capstone 'Key Passive' slot every class caps out with is being removed entirely. Replaced by expanded branching within the tree."* | https://diablobytes.com/diablo-iv/guides/skill-tree-rework/ |
| ✅ Nodos pasivos fuera del árbol | *"Passive nodes are no longer part of the skill tree, so the tree now focuses more directly on Active skills and their branches"* | https://www.keengamer.com/articles/guides/diablo-iv-lord-of-hatred-all-new-changes-and-updates/ |
| ✅ Volumen del rework | *"more than 40 reworked choices, 80 additional options, and up to 83 available Skill Points"* | https://www.keengamer.com/articles/guides/diablo-iv-lord-of-hatred-all-new-changes-and-updates/ |
| ✅ Reespecialización | *"Skill points auto-refunded... Respec cost is already $0 gold since a prior patch"* | https://diablobytes.com/diablo-iv/guides/skill-tree-rework/ |
| 🔒 Variantes transformadoras | *"Only the 20+ transformative skill variants per class are LoH-exclusive"* | https://diablobytes.com/diablo-iv/guides/skill-tree-rework/ |

### 1.2. 🔒 LO ÚNICO QUE PIERDES POR NO TENER LA EXPANSIÓN (dato duro, y es importante)

Esta es la frase que más te afecta de todo el informe:

> *"only two of the three skill variations offered by the third branch can be unlocked and used without Lord of Hatred. To maximize the impact of this new mechanic, it's best to acquire the new expansion immediately!"*
> — IGGM, 25 de abril de 2026 · https://www.iggm.com/news/diablo-4-season-13-lord-of-hatred-skill-tree-rework-of-8-classes

Traducido a tu situación: **el árbol nuevo entero es tuyo, pero de cada tres variantes de la tercera rama de cada habilidad, solo puedes usar dos.** La tercera está detrás de Lord of Hatred.

Cruzado con DiabloBytes ("20+ transformative variants per class... Paid content"), las dos fuentes coinciden en el fondo: lo bloqueado son **variantes**, no clústeres, no puntos, no nivel 70.

⚠️ **Cautela sobre IGGM:** es una tienda de oro/servicios, tiene interés comercial en que compres la expansión, y esa frase termina en una llamada a la compra. El *hecho* (dos de tres variantes) me lo creo porque coincide con DiabloBytes; el *tono* de urgencia no.

⚠️ **Segundo aviso:** la estructura "tercera rama con tres variantes" viene de IGGM y de DiabloBytes ("12-point / 3-path standard"), y DiabloBytes la etiqueta como *"Confirmed for Necromancer summons, strongly implied class-wide"* — o sea, ellos mismos admiten que para el resto de clases es deducción, no confirmación. **No lo he visto en notas oficiales de Blizzard.**

---

## 2. El conflicto que no puedo resolver: ¿puntos gastados o nivel de personaje?

### 2.1. Lo que dicen las fuentes vivas (todas post-3.0, todas actualizadas en 2026)

| Fuente | Fecha | Qué dice literalmente | Modelo |
|---|---|---|---|
| Maxroll | *"April 26, 2026: Updated for Lord of Hatred launch"* | *"Each cluster is unlocked as you gain more levels, and the upgrades within each cluster unlock in a staggered fashion."* — *"Level 1: Basic cluster." / "Level 3: Core cluster." / "Level 4, 8 and 13: Unique clusters per class." / "Level 19: Ultimate Cluster."* | **NIVEL** |
| Icy Veins | *"June 27th, 2026: Guide updated for Season 14"* + *"July 1st, 2026"* | *"The new Lord of Hatred expansion Skill Tree unlocks in stages, permanently unlocking new skill clusters. For example, Necromancer Curses unlock at level 13."* | **NIVEL** |
| AOEAH | 20 abr 2026, act. 27 abr 2026 | *"Skill nodes and clusters unlock via level-based gating (1–70) instead of rigid skill point thresholds"* | **NIVEL, y lo niega explícitamente** |

URLs: https://maxroll.gg/d4/getting-started/skill-trees · https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/ · https://www.aoeah.com/news/4508--diablo-4-lord-of-hatred--season-13-new-skill-tree-guide

### 2.2. La única fuente que apoya "puntos gastados" está MUERTA

Game8 da exactamente los números 23 y 33 que circulan por todas partes:

> Basic Skills "0 pts" · Core Skills "2 pts" · Unique Class Skills "6, 11, 16 pts" · Ultimate Skills "23 pts" · Key Passives "33 pts"
> — https://game8.co/games/Diablo-4/archives/402759

**Pero esa misma página dice:** *"There are only 71 total skill points to obtain in Diablo 4"*, nivel máximo 60, y las Pasivas Clave siguen existiendo. **Última actualización: 13 de octubre de 2024.** Es contenido pre-3.0.

Lo mismo con D4Dead (30 de marzo de 2026, o sea **antes** del parche): *"Key Passives sit in the final cluster"*, *"one skill point per level until level 50"*. https://d4dead.com/skill-tree/

👉 **Conclusión sobre los números 23/33:** son reales, pero son del árbol VIEJO, donde el 33 abría la Pasiva Clave. Como la Pasiva Clave ya no existe (confirmado arriba), **cualquier guía que hoy te diga "33 puntos para la Key Passive" está copiando 2023-2024.** Que los mismos números 23/33 se hayan reciclado para "Definitivas / Pasivas Definitivas" post-3.0 **no lo he podido verificar en ninguna fuente**.

### 2.3. Hipótesis de reconciliación — ETIQUETADA COMO HIPÓTESIS, NO COMO DATO

La frase de Maxroll tiene dos mitades que podrían explicar por qué tú y las guías veis cosas distintas:

> *"Each cluster is unlocked as you gain more levels, **and the upgrades within each cluster unlock in a staggered fashion**."*

**Hipótesis:** el *clúster* se abre por nivel, pero las *mejoras/ramas dentro* de cada habilidad se escalonan por inversión. Lo que tú viste en pantalla podrían ser las mejoras internas, no los clústeres.

**Esto es una conjetura mía. No la escribas en la guía final como hecho.** Se verifica en 30 segundos con el juego delante: sube un nivel sin gastar el punto y mira si se abre algo.

### 2.4. Dato colateral que sí está escrito y sí es accionable

> *"skill points from the Season Rank System or Renown do not affect Skill Tree progress and can be allocated to skill ranks you already unlocked"*
> — Icy Veins, vía resultado de búsqueda sobre https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/

Es decir: los puntos extra del Rango de Temporada **no** te desbloquean clústeres, solo suben rangos de habilidades que ya tienes. Si el modelo fuera por puntos gastados, esto sería una excepción muy relevante para ti.

### 2.5. Conflicto secundario: ¿cuántos puntos hay en total?

| Fuente | Total | Desglose | URL |
|---|---|---|---|
| Icy Veins (jun-jul 2026) | **83** | *"69 skill points are gained by leveling, and 14 skill points are locked behind the Season Rank System or Renown"* | https://www.icy-veins.com/d4/guides/mendeln-summoner-necromancer-build/ |
| KeenGamer / Blizzard (abr 2026) | **83** | *"up to 83 available Skill Points"* | https://www.keengamer.com/articles/guides/diablo-iv-lord-of-hatred-all-new-changes-and-updates/ |
| Maxroll (abr 2026) | **80** | *"one skill point each time you level up, starting from level 2"* + *"12 additional skill points through the Season Rank system"* | https://maxroll.gg/d4/getting-started/skill-trees |

Dos contra uno a favor de **83 (69 + 14)**. Maxroll parece no haber actualizado la cifra de puntos de temporada (12 vs 14). **No lo doy por cerrado.**

---

## 3. NIGROMANTE: el cambio más grande de todas las clases

Consenso unánime en todas las fuentes: el Nigromante es la clase que más cambió.

> *"Necromancers might be the biggest winners of the expansion"* — PC Gamer, Tyler Colp, 23 de abril de 2026
> https://www.pcgamer.com/games/rpg/diablo-4-lord-of-hatred-has-a-special-gift-for-necromancers-who-want-to-be-surrounded-by-28-skeletons-and-druids-who-hate-being-bears/

### 3.1. Los esbirros se mudaron al árbol de habilidades ✅

| Cambio | Cita literal | Fuente |
|---|---|---|
| Los esbirros viven en el árbol | *"All their minions now live in the skill tree"* | PC Gamer (URL arriba) |
| Reparto de Alzar Esqueleto | *"Raise Skeleton is being split into two separate skills"* | https://www.icy-veins.com/d4/news/diablo-4s-lord-of-hatred-just-broke-the-necromancer-wide-open/ |
| **Magos** = se invocan con Esencia | *"Skeletal mages are summoned with the necromancer's version of mana, essence"* | PC Gamer |
| **Guerreros** = aparecen solos de los cadáveres | *"skeletal warriors show up passively when there are monster corpses nearby"* | PC Gamer |
| Ahora puedes darles órdenes | *"they can finally direct their skeletons to attack targets"* / Warriors gain *"an Active component"* | PC Gamer · Icy Veins News |
| Los esbirros ya reciben puntos | *"invest skill points directly into your minions, layer on modifiers, and shape exactly how each summon contributes to your build"* | https://www.icy-veins.com/d4/news/diablo-4s-lord-of-hatred-just-broke-the-necromancer-wide-open/ |

**Esto es lo más importante que tiene que interiorizar un principiante:** ya no es "un botón invoca todo". Los Guerreros se regeneran solos desde cadáveres; los Magos son una **inversión deliberada de Esencia**. Cambia el ritmo de juego por completo.

### 3.2. Mejoras concretas de esbirros con nombre y número

| Nodo / mejora | Efecto literal | Fuente |
|---|---|---|
| **Singularity** (Magos) | *"lets you dump all remaining Essence into a single, massively buffed temporary mage"* | https://www.icy-veins.com/d4/news/diablo-4s-lord-of-hatred-just-broke-the-necromancer-wide-open/ |
| Singularity (versión GameRant) | *"spend all remaining Essence to summon one large Mage that lasts proportionally to how much Essence was spent"* | https://gamerant.com/diablo-4-lord-of-hatred-skill-tree-update-necromancer/ |
| **Sacerdotes Esqueleto** (ahora mejora de Guerreros) | *"bonus Critical Strike Chance and heal them for **100% of their Maximum Life over 8 seconds**"* | https://www.icy-veins.com/d4/news/diablo-4s-lord-of-hatred-just-broke-the-necromancer-wide-open/ |
| **Litany of Death** | Los Sacerdotes pasan a ser mejora de los Guerreros vía este nodo | https://gamerant.com/diablo-4-lord-of-hatred-skill-tree-update-necromancer/ |
| Modificadores vistos | *"increased damage scaling with Essence consumed, bonus damage to Crowd Controlled enemies, and stacking damage the longer a mage stays alive"* | https://www.icy-veins.com/d4/news/diablo-4s-lord-of-hatred-just-broke-the-necromancer-wide-open/ |
| Tope de esbirros | *"they can gather up to what looks like **28** of them, all at once, with the right items"* | PC Gamer |

⚠️ **El 28 va con pinzas.** El propio periodista escribe *"what looks like"* — lo contó a ojo en una pantalla de preview el 23 de abril, antes del lanzamiento. **No es una cifra oficial de Blizzard.**

### 3.3. El Libro de los Muertos post-rework: SIGUE EXISTIENDO ✅

Aquí las fuentes se contradicen en el alcance, y lo digo tal cual:

| Fuente | Qué afirma |
|---|---|
| DiabloBytes | *"Book of the Dead remains but **re-scopes around buffs and the sacrifice mechanic**"* |
| GameRant | *"the Book of the Dead **still lets players choose which form** their Skeletal Warriors, Mages, and Golem take, but upgrading these summons falls to the Skill Tree's nodes"* |
| IGGM | *"the original Book of the Dead remains **largely unchanged**, but sacrifice can be used with minions active"* |

URLs: https://diablobytes.com/diablo-iv/guides/skill-tree-rework/ · https://gamerant.com/diablo-4-lord-of-hatred-skill-tree-update-necromancer/ · https://www.iggm.com/news/diablo-4-season-13-lord-of-hatred-skill-tree-rework-of-8-classes

**Lo que sí está confirmado en las tres:** el Libro sigue ahí, sigue eligiendo forma de esbirro, y sigue teniendo sacrificios.

#### El cambio de los sacrificios — con números

Este es el cambio de calidad de vida más grande para un jugador de esbirros:

> *"Sacrifice no longer removes your ability to summon those minions"* — los esbirros siguen apareciendo *"albeit in reduced numbers or with reduced damage"*
> — https://www.icy-veins.com/d4/news/diablo-4s-lord-of-hatred-just-broke-the-necromancer-wide-open/

> *"The Book of the Dead... will still let you sacrifice your minions for powerful stat bonuses, but won't stop you from still summoning weaker versions of them in combat. This allows you to use them purely as tanks instead of damage-dealers"*
> — PC Gamer, 23 abr 2026

**Y así se ve en una build S14 real** (Icy Veins "Naz Mages", act. 27 jun / 3 jul 2026, https://www.icy-veins.com/d4/guides/mendeln-summoner-necromancer-build/):

| Opción del Libro | Texto literal del juego |
|---|---|
| Guerreros: Reaper [Sacrificio] | *"You deal x15% increased damage, but the amount of Reapers you can Summon is **reduced by 50%**"* |
| Magos: Cold [Mejora #2] | *"Cold Mages occasionally cast a blizzard that deals #[#%] Cold damage over 6 seconds and Chills for 6% every second"* |
| Gólem: Iron [Sacrificio] | *"You deal 15%[x] increased Critical Strike Damage, but your Golem does **50%[x] less damage**"* |

👉 Fíjate: **"reducido un 50%", no "no puedes invocarlos"**. Esa redacción es la prueba escrita del cambio. Sacrificar ya no es renunciar.

### 3.4. Niveles del Libro de los Muertos: TERCER CONFLICTO, y este te va a tocar pronto

| Fuente | Fecha | Qué dice |
|---|---|---|
| Maxroll, Necromancer Class Overview | **"July 18, 2026 - Updated for Season 14"** | *"You gain access to the actual menu at **Level 5**!"* — *"You first gain access to the basic **Skeleton Mage** and as you level up, you then unlock **Skeleton Warrior** finally unlocking **Golem** last."* |
| Icy Veins, Summoner Leveling | jun-jul 2026 | Nivel 5 (Guerreros y Magos), Nivel 8 (Gólem), Nivel 12 (Reapers), Nivel 50 (optimización final) |

URLs: https://maxroll.gg/d4/resources/necromancer-class-overview · https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/

**Ojo al orden:** Maxroll dice **Mago primero, luego Guerrero, luego Gólem**. Eso es lo contrario del juego de 2023 (Guerreros 5 → Magos 15 → Gólem 25) y también distinto de Icy Veins. Maxroll no da los niveles concretos de Guerrero y Gólem.

Los "nivel 8 / nivel 12" de Icy Veins son **exactamente el tipo de cifra que ya refutaste**. **No los uses.** El único dato que dos fuentes sostienen es **el menú se abre a nivel 5**, y aun así lo marco como pendiente de verificar en tu partida.

---

## 4. SENTIMIENTO DE LA COMUNIDAD (foros oficiales de Blizzard)

### 4.1. Antes del parche: enfado por quitar las pasivas

Dos hilos de febrero de 2026, cuando se filtró el cambio.

**Hilo: "I cant see a way that the removal of all passive skills from the tree is a good thing"**
https://us.forums.blizzard.com/en/d4/t/i-cant-see-a-way-that-the-removal-of-all-passive-skills-from-the-tree-is-a-good-thing/241872

| Postura | Quién / cuándo | Argumento |
|---|---|---|
| En contra | Latimere-1192, 14 feb 2026 | *"an absolutely horrible choice"* — las pasivas llevan 25 años en Diablo; moverlas al Paragon las mete detrás del nivel 60 |
| Preocupado | Gilthas-1277 | *"locking passives behind the Paragon Board can be pretty problematic for some builds"* |
| A favor (cita al desarrollador) | Nyurei-21383 | El motivo declarado por Blizzard: con mismo nivel y mismo equipo había una varianza de poder del **"400-500%"**; quitarlas permite afinar la dificultad del Pit |
| A favor | MFPF-1376 | Separar pasivas de activas simplifica el balanceo |

Sentimiento: desacuerdo cauto. MFPF-1376 acaba cediendo (*"I have nothing to propose"*) tras leer la explicación de los desarrolladores.

**Hilo: "Passives confirmed removed from skilltree! ✅"** (7 feb 2026)
https://us.forums.blizzard.com/en/d4/t/passives-confirmed-removed-from-skilltree/241560
Confirmación de usuario: *"Passives are no longer in skill tree. Devs confirm passives were too build defining in tree and are other places now."*
Reacción representativa (Jemuzu-11303): *"If they force another 'itemization overhaul', as an Eternal Player, I am done."*

⚠️ **Los dos hilos son PRE-lanzamiento (febrero).** Sirven para entender el enfado, no para saber cómo funciona el árbol hoy.

### 4.2. Después del parche, Temporada 14: el veredicto sobre el Nigromante

**Hilo clave: "Season 14 feels like a huge missed opportunity for Necromancer & Build Diversity"** (jul 2026)
https://us.forums.blizzard.com/en/d4/t/season-14-feels-like-a-huge-missed-opportunity-for-necromancer-build-diversity/261095

| Arquetipo | Veredicto de la comunidad | 🔒/✅ |
|---|---|---|
| **Esbirros / Magos** | **FUERTE** | ✅ |
| Espíritu Óseo (Bone Spirit) y variantes de Esquirla Ósea | FUERTE | ✅ |
| Gólem (sobre todo Gólem de Hueso con Lidless) | FUERTE | ✅ |
| Espíritu Óseo + Explosión de Cadáveres híbrido | FUERTE | ✅ |
| Maldiciones (sobre todo Doncella de Hierro) | **DÉBIL** | ✅ |
| Espinas (Thorns) | **DÉBIL — y con bugs** | ✅ |
| Sombra (Shadow) | DÉBIL | ✅ |
| Sever y Oleada de Sangre | DÉBIL | ✅ |

**EL DATO MÁS ACCIONABLE DE TODO EL INFORME**, y viene de un usuario, no de una guía:

> **"4 of the top 5 spots on the SSF solo leaderboard are minion builds, specifically mage builds."**
> — Harlequin-1438, **5 de julio de 2026**, mismo hilo

SSF = Solo Self-Found, sin comercio. Para dos principiantes en dúo sin mercado, **es la clasificación que más se parece a vuestra situación**. Y dice: magos esqueleto.

Otras quejas concretas del hilo:
- Doncella de Hierro procea *"every 2 seconds"* → se siente demasiado lento.
- El daño de Espinas no escala con multiplicadores de DoT ni con velocidad de ataque.
- Slayer-12160 (7 jul 2026): *"The great problem with thorns necro is bugs.. a LOT of bugs with damage multipliers"*.

⚠️ **Nota de contexto:** el OP (Ottodoroki) se queja de falta de diversidad, y otros le responden con datos de leaderboard contradiciéndole. **Hay desacuerdo real dentro del hilo.** No es consenso.

### 4.3. Hilo de jugadores de esbirros: "Minion Necromancer's Only" (mayo 2026)
https://us.forums.blizzard.com/en/d4/t/minion-necromancer%E2%80%99s-only/256563

| Tipo | Cita | Autor / fecha |
|---|---|---|
| **DATO** (opinión informada) | *"Skill points in minions make a large difference now, but I wish it also reduced the CD on Command"* | Shivera-1883, 25 may 2026 |
| OPINIÓN | *"No pure minion build worth a dang"* | Realm-11690, 25 may 2026 |
| OPINIÓN | *"You can spank T-12 Mephisto if you got the right gear"* (la mayoría dice que T10 es lo realista para esbirros puros) | Methos-1409, 25 may 2026 |
| CONSEJO DE EQUIPO 🔒/❓ | *"ziir 2h or bloodless scream if you like dark"* | Apache222-1831, 25 may 2026 |
| **AVISO DE EQUIPO** | *"Don't use the unique gloves. They nerfed into [💩]"* | Apache222-1831, 25 may 2026 |
| QUEJA | El *pathfinding* (movimiento) de los esbirros sigue siendo malo | varios |

⚠️ **Contradicción interna importante:** este hilo de mayo dice "los esbirros puros no valen"; el hilo de julio dice "4 de los 5 primeros del leaderboard SSF son esbirros". **Dos meses de diferencia y parches de por medio.** Prevalece el dato de julio, que además es verificable contra una clasificación.

⚠️ Los "guantes únicos" nerfeados los menciona sin nombrarlos. **No he podido identificar de qué guantes habla.** Ojo: la build "Naz Mages" de Icy Veins **sí** pide *The Hand of Naz* (guantes). Puede ser el mismo ítem antes de un rebalanceo, o puede que no. **No lo sé.**

### 4.4. TRAMPA REAL, CONFIRMADA, CON FECHA: el bug de las variantes al reespecializar

**Hilo: "Skill tree bug (necro)"** — 3 de mayo 2026, reconfirmado el 11 de mayo 2026
https://us.forums.blizzard.com/en/d4/t/skill-tree-bug-necro/249002

Qué pasa: con la variante **Torture Artist** de Doncella de Hierro (que convierte el daño de físico a sombra), si le das a **"reembolsar todo" (refund all)**, las etiquetas de sombra y oscuridad **se quedan pegadas** aunque elijas otra variante.

> *"Hitting refund all while that is active keeps both the shadow and darkness tags. even after selecting Blood Maiden and confirming the changes."*

- El usuario descubrió que el **"Aspect of Crippling Darkness"** equipado contribuía al problema; quitárselo lo resolvió en parte.
- **Sin respuesta de Blizzard. Sin resolver en el último mensaje del hilo.**

**Por qué te importa a ti, principiante y min-maxer:**
1. Confirma que existen **variantes con nombre propio** que cambian el TIPO DE DAÑO de una habilidad (Torture Artist, Blood Maiden). Esto es la mecánica nueva.
2. Confirma el aviso de DiabloBytes: *"Tag-modifying upgrades can invalidate your old gear (different aspects/tempers/glyphs apply)"*.
3. **Consejo práctico:** si vas a reespecializar, quítate primero los aspectos que conviertan tipo de daño y revisa a mano las etiquetas de la habilidad después.

**Hilo relacionado: "Character skill reset?"** (2 may 2026, cerrado el 1 jun sin respuesta de Blizzard)
https://us.forums.blizzard.com/en/d4/t/character-skill-reset/248433
Un jugador reporta que al abrir la expansión *"all my characters have had their skill trees reset"*. Es el reembolso automático anunciado, pero pilló a gente por sorpresa.

---

## 5. Consejos concretos y accionables (separando DATO de OPINIÓN)

### 5.1. Del propio DiabloBytes: "lo que los veteranos tienen que reaprender"
https://diablobytes.com/diablo-iv/guides/skill-tree-rework/ — citas literales:

- ⚠️ *"No Key Passive capstone target — plan around branching upgrade trees"* → **DATO**
- ⚠️ *"Tag-modifying upgrades can invalidate your old gear"* → **DATO** (corroborado por el bug de 4.4)
- ⚠️ *"12-point / 3-path structure per skill is the new mental model"* → **PARCIALMENTE CONFIRMADO** (ellos mismos dicen "strongly implied" fuera de los esbirros del Nigromante)
- ⚠️ *"Necros: summons live in the skill tree, not the Book of the Dead"* → **DATO**, corroborado por PC Gamer, GameRant e Icy Veins
- ⚠️ *"Level ceiling is 70, not 60 — more points to spend"* → **DATO**
- ⚠️ *"Respec is free and auto-applied — experiment freely"* → **DATO**

### 5.2. Estrategia de lanzamiento que recomendaba DiabloBytes (esto es OPINIÓN)

| # | Consejo | Vigencia hoy (18 ago 2026) |
|---|---|---|
| 1 | *"Do not preload a build from a planner. None will be accurate until mid-May at earliest"* | **CADUCADO** — estamos en agosto |
| 2 | *"Play your main class blind for the first session"* | Sigue siendo razonable para principiantes |
| 3 | *"Level to 70 first, then iterate. Extra skill points change which branches are reachable"* | **RELEVANTE**: nota que dice *branches reachable*, otra pista de gating por inversión |
| 4 | *"Necro and Druid players: expect the biggest relearning curve. Plan extra respec time"* | **TE APLICA DIRECTAMENTE** |
| 5 | *"Wait 1-2 weeks for community consensus"* | **CADUCADO** — ya hay consenso |
| 6 | *"Save gold for tempering + masterworking rerolls. Gear optimization costs climb fast at 70"* | Vigente |

### 5.3. Lo que yo destilaría para vosotros dos (esto es MI lectura, no una fuente)

1. **Id a magos esqueleto.** Es lo único que tiene respaldo de leaderboard SSF (4 de 5, jul 2026) y a la vez es la fantasía de clase para dos nigromantes en dúo.
2. **Evitad Maldiciones, Espinas y Sombra** este parche. Consenso del foro, y Espinas además tiene bugs sin arreglar.
3. **Reespecializar es gratis y los puntos se reembolsan.** No hay decisión irreversible en el árbol. La ansiedad de "gastar mal un punto" no está justificada mecánicamente.
4. **Cuidado al reespecializar con aspectos que conviertan tipo de daño equipados** (bug confirmado, sin arreglar).
5. **Los puntos del Rango de Temporada no abren clústeres** — no contéis con ellos para llegar antes a nada.
6. 🔒 **Sin expansión perdéis 1 de cada 3 variantes de la tercera rama.** No perdéis el árbol, ni el nivel 70, ni el filtro de botín. Es una pérdida real pero acotada.

---

## 6. Creadores activos de Nigromante en S14

| Creador | Qué encontré | Verificado |
|---|---|---|
| **wudijo** | Vídeo *"Diablo 4 LoH - NEW SKILL TREES: Necro & Sorceress"*, subido **2026-04-25T07:39:58-07:00**, **22.775 visualizaciones**. Marcas de tiempo del propio autor: `00:00 Info · 00:56 Sorcerer · **24:35 Necromancer** · 44:53 More Info`. https://www.youtube.com/watch?v=ymnzxYQtMtg | ✅ Metadatos leídos directamente de la página |
| **wudijo** | Es creador de Maxroll: https://maxroll.gg/@wudijo | ✅ |
| **Rob2628** | Tiene "cheat sheet" en D4Builds: https://d4builds.gg/cheat-sheet/ — **el `<title>` de la página dice "S14" pero el encabezado del propio documento sigue diciendo "Rob2628's Diablo 4 S13 Cheat Sheet"**. El contenido se renderiza por JavaScript y no pude leerlo. | ⚠️ Posiblemente desactualizado |
| **Rob2628** | Builds: https://d4builds.gg/rob2628/builds/ | No abierto |
| **MacroBioBoi** | Autor en Maxroll: https://maxroll.gg/@macrobioboi | No abierto |
| **Seroc Ifkre** (Maxroll) | Autor de la guía endgame *Army of the Dead Necromancer*, *"Last Updated: August 12, 2026"*, changelog *"6/29 - Updated for Season 14"* y *"7/1 - updated affixes"*. 🔒 **Requiere Vessel of Hatred**: la guía dice *"Mercenaries are unlocked during the Vessel of Hatred campaign"* y construye alrededor de ellos (Raheir, Aldkin). https://maxroll.gg/d4/build-guides/army-of-the-dead-necromancer-guide | ✅ |
| **Lurkin** | **No encontrado.** Ninguna búsqueda devolvió contenido suyo de Nigromante S14. | ❌ |

⚠️ **No he podido ver el contenido de ningún vídeo.** Solo metadatos y descripciones. Lo que wudijo *dice* en el minuto 24:35 sobre el árbol del Nigromante sigue sin cubrir.

---

## 7. Guías S14 de Nigromante localizadas (para el equipo que continúe)

| Guía | Fecha | Puntos | Libro de los Muertos | 🔒 |
|---|---|---|---|---|
| Icy Veins – **Summoner Leveling** https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/ | 27 jun / 1 jul 2026 | 83 (69+14) | Reapers [Mej. #2] · Shadow [Mej. #2] · Gólem Bone [Sacrificio] | ✅ base |
| Icy Veins – **Reaper Summoner** https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/ | 27 jun / 3 jul 2026 | 83 (69+14) | Reapers [Mej. #2] · Shadow [Mej. #2] · Gólem Iron [Sacrificio] | ✅ base (Mercenarios recomendados = 🔒 VoH) |
| Icy Veins – **Naz Mages** https://www.icy-veins.com/d4/guides/mendeln-summoner-necromancer-build/ | 27 jun / 3 jul 2026 | 83 (69+14) | Reaper [Sacrificio] · Cold [Mej. #2] · Iron [Sacrificio] | ❓ Pide 4 únicos: The Hand of Naz, Blood Moon Breeches, Signet of Pelghain, The Undercrown. **No verifiqué su origen.** |
| Maxroll – **Army of the Dead** (endgame) https://maxroll.gg/d4/build-guides/army-of-the-dead-necromancer-guide | 12 ago 2026 | n/d | n/d | 🔒 **Requiere VoH** (Mercenarios) |
| Maxroll – **Sever Leveling** https://maxroll.gg/d4/build-guides/sever-necromancer-leveling-guide | S14 | n/d | n/d | No abierta |

⚠️ **Aviso sobre las guías de Icy Veins:** las tres repiten la frase *"The new Lord of Hatred expansion Skill Tree unlocks in stages"*. Un resumen automático leyó eso como "esta build requiere la expansión". **Es una lectura errónea.** La frase se refiere al árbol *introducido por* el parche de LoH, que es gratis para todos (ver 1.1). Es una confusión fácil de cometer y merece un aviso en la guía final.

---

## 8. Parche vivo 3.1.3 (12 de agosto de 2026) — lo único que encontré del Nigromante

> *"an issue was corrected where Necromancer skills of the 'Darkness' category obscured the 'Corrupted Reaper' model"*
> — https://ixbt.games/en/news/2026/08/12/diablo-iv-polucit-patc-313-blizzard-ispravit-nekromanta-voennye-plany-i-boi-s-exom-mefisto.html

Es un arreglo visual. Pero confirma dos cosas útiles: existe una categoría de habilidades **"Darkness" (Oscuridad)** en el Nigromante, y existe una entidad llamada **"Corrupted Reaper"** en S14.

⚠️ ixbt.games es un medio ruso; es la única fuente que encontré para 3.1.3. **No pude contrastarlo con las notas oficiales.**

---

## 9. Trampa metodológica: por qué las notas OFICIALES no aparecen aquí

Abrí las dos URLs oficiales del parche 3.0:
- https://news.blizzard.com/en-us/article/24271857/diablo-iv-patch-notes-3-0
- Espejo Wowhead Blue Tracker: https://www.wowhead.com/diablo-4/blue-tracker/news/us/diablo-iv-patch-notes-3-0-diablo-iv-blizzard-news-24271857

**Ambas contienen únicamente los hotfixes 3.0.1 → 3.0.4 (27 abr – 10 jun 2026): bugs y balanceo. Ninguna contiene el rework del árbol.** Las notas de lanzamiento 3.0.0 con la descripción del sistema no las localicé en news.blizzard.com. También abrí el artículo oficial de Xbox Wire (https://news.xbox.com/en-us/2026/04/22/diablo-4-skill-tree-overhaul/) y es puramente cualitativo: *"The new Skill Tree has nurtured the previous 'skill twig' into a fully branching system"*. **Cero números.**

👉 **Por eso no hay una sola cifra de gating en este informe respaldada por Blizzard.** Todos los números de desbloqueo que circulan vienen de terceros, y los terceros se contradicen entre sí.

---

## 10. Semáforo de fiabilidad de fuentes (para la síntesis final)

| Fuente | Estado | Motivo |
|---|---|---|
| PC Gamer (23 abr 2026) | 🟢 Fiable | Preview con el juego jugado, autor y fecha; el propio autor marca lo que estima ("what looks like 28") |
| Icy Veins News – "Broke the Necromancer Wide Open" | 🟢 Fiable | Detalle mecánico con números; coherente con PC Gamer y GameRant |
| Foros oficiales de Blizzard | 🟢 Fiable como *comunidad* | Usuarios con fecha y nick; es opinión, pero es opinión trazable |
| GameRant (28 abr 2026) | 🟢 Fiable | Fechado, coherente con las otras dos |
| DiabloBytes | 🟡 **Mixta** | Datos generales correctos, pero **el cuerpo está escrito en futuro** ("What's Changing April 28", "expected at the April 23 livestream", "This page will be updated immediately afterward") pese a decir "Updated July 2026". Ellos mismos etiquetan partes como *"preview-spotted, not confirmed"* y *"safe inferences"* |
| Maxroll | 🟡 Mixta | Class Overview actualizado 18 jul 2026 (fresco); Skill Trees actualizado 26 abr 2026 y con cifra de puntos que no cuadra (80 vs 83) |
| Icy Veins guías de build | 🟡 Mixta | Muy frescas (jun-jul 2026) pero expresan el gating en **niveles** |
| IGGM | 🟡 Con conflicto de interés | Tienda; el dato de "2 de 3 variantes" coincide con DiabloBytes, pero acaba en llamada a la compra |
| AOEAH | 🟡 Con conflicto de interés | Tienda; afirma gating por nivel de forma tajante |
| KeenGamer | 🟢 Fiable para las cifras de Blizzard (40+/80/83) | Cita a Blizzard |
| ixbt.games | 🟡 Sin contrastar | Única fuente para 3.1.3 |
| **Game8** | 🔴 **MUERTA** | 13 oct 2024. Nivel 60, 71 puntos, Key Passives. **Es de donde salen los 23/33** |
| **D4Dead** | 🔴 **MUERTA** | 30 mar 2026 (pre-parche). Key Passives, nivel 50 |
| fextralife, primagames, beebom, gamespot, segmentnext, studioloot, gamerguides, pcgamesn, mythicdrop | ⛔ **VETADAS** | No abiertas. Aparecieron en resultados de búsqueda y fueron descartadas |

---

## Fuentes (URLs realmente abiertas y leídas)

**Foros oficiales de Blizzard (comunidad — mi dominio):**
1. https://us.forums.blizzard.com/en/d4/t/season-14-feels-like-a-huge-missed-opportunity-for-necromancer-build-diversity/261095
2. https://us.forums.blizzard.com/en/d4/t/minion-necromancer%E2%80%99s-only/256563
3. https://us.forums.blizzard.com/en/d4/t/skill-tree-bug-necro/249002
4. https://us.forums.blizzard.com/en/d4/t/character-skill-reset/248433
5. https://us.forums.blizzard.com/en/d4/t/i-cant-see-a-way-that-the-removal-of-all-passive-skills-from-the-tree-is-a-good-thing/241872
6. https://us.forums.blizzard.com/en/d4/t/passives-confirmed-removed-from-skilltree/241560

**Prensa y análisis:**
7. https://www.pcgamer.com/games/rpg/diablo-4-lord-of-hatred-has-a-special-gift-for-necromancers-who-want-to-be-surrounded-by-28-skeletons-and-druids-who-hate-being-bears/
8. https://gamerant.com/diablo-4-lord-of-hatred-skill-tree-update-necromancer/
9. https://www.keengamer.com/articles/guides/diablo-iv-lord-of-hatred-all-new-changes-and-updates/
10. https://ixbt.games/en/news/2026/08/12/diablo-iv-polucit-patc-313-blizzard-ispravit-nekromanta-voennye-plany-i-boi-s-exom-mefisto.html

**Guías y bases de datos:**
11. https://diablobytes.com/diablo-iv/guides/skill-tree-rework/
12. https://maxroll.gg/d4/getting-started/skill-trees
13. https://maxroll.gg/d4/resources/necromancer-class-overview
14. https://maxroll.gg/d4/build-guides/army-of-the-dead-necromancer-guide
15. https://www.icy-veins.com/d4/news/diablo-4s-lord-of-hatred-just-broke-the-necromancer-wide-open/
16. https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/
17. https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/
18. https://www.icy-veins.com/d4/guides/mendeln-summoner-necromancer-build/
19. https://www.iggm.com/news/diablo-4-season-13-lord-of-hatred-skill-tree-rework-of-8-classes
20. https://www.aoeah.com/news/4508--diablo-4-lord-of-hatred--season-13-new-skill-tree-guide
21. https://d4builds.gg/cheat-sheet/ (abierta, contenido renderizado por JS, ilegible)

**Oficiales (abiertas, pero sin el contenido buscado):**
22. https://news.blizzard.com/en-us/article/24271857/diablo-iv-patch-notes-3-0 — solo hotfixes 3.0.1–3.0.4
23. https://www.wowhead.com/diablo-4/blue-tracker/news/us/diablo-iv-patch-notes-3-0-diablo-iv-blizzard-news-24271857 — idem
24. https://news.xbox.com/en-us/2026/04/22/diablo-4-skill-tree-overhaul/ — cualitativo, sin números

**Creadores:**
25. https://www.youtube.com/watch?v=ymnzxYQtMtg — wudijo, metadatos verificados

**Abiertas y descartadas por MUERTAS (documentadas como trampa):**
26. https://game8.co/games/Diablo-4/archives/402759 — 13 oct 2024
27. https://d4dead.com/skill-tree/ — 30 mar 2026, pre-parche

---

## No encontrado

### Reddit — fracaso total
- ❌ **r/diablo4** — no accesible (403 + bloqueo explícito del user-agent)
- ❌ **r/Diablo4Necromancer** — no accesible
- ❌ **r/D4Necromancer** — no accesible
- ❌ Hilos tipo *"things I wish I knew about the new skill tree"* — no localizados en ninguna fuente accesible
- ❌ Hilos de Reddit sobre el Libro de los Muertos post-rework — no accesibles
- ❌ Hilos de Reddit sobre jugar sin expansiones — no accesibles

### El modelo de desbloqueo
- ❌ **NO he confirmado el modelo por PUNTOS GASTADOS.** Ninguna fuente accesible lo afirma para el árbol post-3.0
- ❌ **"Core tras 1 punto, siguiente grupo tras 2 puntos" (Season 11)** — no confirmado en ninguna fuente
- ❌ **"23 puntos → Definitivas"** post-3.0 — solo lo he visto en Game8 (oct 2024, pre-rework)
- ❌ **"33 puntos → Pasivas Definitivas"** — solo he visto "33 puntos → Key Passive" en Game8 (oct 2024). La Key Passive ya no existe. **La existencia misma de un clúster de "Pasivas Definitivas" no la he podido verificar en ninguna parte**
- ⚠️ **Tres fuentes vivas (Maxroll abr-26, Icy Veins jun-26, AOEAH abr-26) afirman gating por NIVEL**, y AOEAH lo niega explícitamente: *"instead of rigid skill point thresholds"*

### Nigromante / Libro de los Muertos
- ❌ Niveles exactos de desbloqueo de Guerreros, Magos y Gólem post-3.0 (Maxroll da el orden Mago→Guerrero→Gólem sin niveles; Icy Veins da niveles que huelen al modelo viejo)
- ❌ Lista completa de nodos y mejoras del árbol nuevo del Nigromante
- ❌ Cuáles de las variantes del Nigromante son 🔒 LoH y cuáles ✅ base — solo tengo la regla genérica "2 de 3"
- ❌ Confirmación oficial del tope de 28 esbirros (PC Gamer lo estima a ojo)
- ❌ Qué "guantes únicos" nerfeados menciona Apache222-1831

### Fuentes que no pude abrir
- ❌ **mobalytics.gg** — HTTP 403 en las dos URLs intentadas (`/diablo-4/necromancer-builds` y `/diablo-4/guides/patch-notes-3-1-1-season-14`), tanto con WebFetch como con curl y User-Agent de navegador
- ❌ **wowhead.com/diablo-4** guía de habilidades del Nigromante — devolvió solo navegación, sin cuerpo del artículo
- ❌ **d4builds.gg/cheat-sheet** — abierta pero el contenido lo genera JavaScript
- ❌ Notas oficiales de lanzamiento **3.0.0** en news.blizzard.com con la descripción del sistema
- ❌ Contenido hablado de cualquier vídeo (wudijo min. 24:35 sigue sin ver)
- ❌ Contenido de **Lurkin**, **Rob2628** y **MacroBioBoi** sobre Nigromante S14

---

## Lo que debe verificar el jugador en 5 minutos con el juego delante

Estas cuatro comprobaciones cierran los huecos que ninguna fuente resuelve:

1. **Sube un nivel SIN gastar el punto.** ¿Se abre algún clúster? → si sí, es por nivel; si no, es por puntos gastados.
2. **Pon el ratón sobre un clúster bloqueado.** El texto del tooltip dice literalmente qué hace falta. Esa frase vale más que todo este informe.
3. **Abre el Libro de los Muertos.** ¿A qué nivel se abrió? ¿Qué esbirro salió primero, Mago o Guerrero?
4. **Mira una habilidad con tres variantes en la tercera rama.** ¿Hay una con candado y texto de expansión? Eso confirma o refuta el "2 de 3".
