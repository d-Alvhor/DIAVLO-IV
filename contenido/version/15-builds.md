---
titulo: Builds de nigromante
capa: version
parche: "3.1.3"
temporada: 14
estado: vivo
entitlement: base
verificado: 2026-08-19
revisar_despues: 2026-10-15
---

## Lo primero, y es incómodo

Ninguna build de nigromante publicada esta temporada es juego base pura. Maxroll e Icy Veins escriben dando por hecho que tenéis las dos expansiones y **no lo advierten en ningún sitio**: cuando una guía lista un charm, una runa o un mercenario, no os da una opción, os da una pieza que no existe en vuestro cliente. Aquí va el filtrado que ellas no hacen.

::: evidencia nivel=corroborado fuentes=icyveins-runewords,blizzard-loh-oficial,maxroll-minion-guide
Las cuatro capas que os faltan y que aparecen en casi todas las guías: **Runas y Runewords** 🔒 VoH (*«Runewords are only available to players who have purchased the Vessel of Hatred expansion»*) · **Mercenarios** 🔒 VoH (*«Mercenaries are unlocked during the Vessel of Hatred campaign»*) · **Talismán y Charms** y **Cubo Horádrico**, ambos 🔒 LoH según la página oficial de Blizzard.
:::

::: evidencia nivel=corroborado fuentes=blizzard-loh-oficial,datos-juego-3-1-0
La **tercera variante** de cada habilidad es 🔒 Lord of Hatred: *«otherwise, 2 out of 3 Bonus Skill Variants are accessible»*. En el fichero de datos del juego (3.1.0.72698) es la variante de máscara 4, con requisito de nivel 30 a 40; las variantes 1 y 2 son ✅. Lo que perdéis es **Gargantua** (Gólem) y **Unholy Frenzy** (Decrepitud).
:::

::: aviso tipo=peligro
Las dos builds de esbirros estrella de Icy Veins, «Naz Mages» y «Reaper Summoner», están montadas alrededor de **Gargantua** 🔒: **no son reproducibles tal cual.** Sí son vuestras *Coven*, *Master of Puppets* y *Unyielding Commander*, las tres ✅.
:::

## Tier list completa, con la marca de expansión

::: evidencia nivel=unica fuentes=maxroll-tierlists
Las tres tier lists de nigromante de Maxroll, 29 de junio de 2026. **Endgame:** A = Blood Wave, Bone Spirit · B = Minion, Golem, Sever, Blood Surge · C = Blight, Army of the Dead, Bone Spear, Blood Lance. **Empuje de Pit y Torre:** A = solo Blood Wave · B = las otras siete · C = Blight, Bone Spear. **Leveleo:** S = Minion solo · A = Blood Surge, Sever, Blight, con criterio declarado «sin recursos, sin templados y sin aspectos desbloqueados».
:::

Es la única lista cuyo criterio se parece a vuestra situación real, y ahí Minion está sola en S.

| Build | Endgame | Push | Dependencia de expansión | Veredicto |
|---|---|---|---|---|
| **Blood Wave** | A | A | Media-alta: runas y mercenario 🔒; item núcleo probablemente ✅ | **Viable, condicional** |
| **Bone Spirit** | A | B | Alta: charm *Red Blessing* y set *Berú of Desecration* 🔒 LoH | **Vetada** |
| **Minion / Esbirros** | B | B | Baja en el núcleo (vive en el árbol ✅); alta en la versión de guía | **La número uno** |
| **Golem** | B | B | Media-alta: cola larga de Míticos, mercenario 🔒 | **Aplazada** |
| **Sever** | B | B | Alta: set *Berú of the Black Shroud* 🔒 de columna vertebral | **Vetada** |
| **Blood Surge** | B | B | Media: runas `Teb` y `Wat` 🔒, sustituibles | **Viable** |
| **Blight** | C | C | Media: charm *Red Blessing* 🔒 | **Vetada** |
| **Army of the Dead** | C | B | Alta: dos charms 🔒 | **Vetada** |
| **Bone Spear** | C | C | **Baja**, la más limpia del catálogo | **Plan B** |
| **Blood Lance** | C | B | Media: curación por runas 🔒 | **Vetada** |

::: aviso tipo=ojo
Las tier lists son de junio; las guías individuales llegan a agosto, con tres parches por medio. **Cuando se contradicen, manda la guía.**
:::

::: evidencia nivel=disputa fuentes=maxroll-tierlists,maxroll-retrospectiva,ezg,diablobytes
Cuál es la mejor build de la clase no tiene consenso. **Maxroll (tier list, 29 jun 2026):** empate Blood Wave / Bone Spirit en A. **Maxroll (retrospectiva, 11 jul 2026):** Blood Wave fue *destronado* por los nerfeos a Sobrepoder y a *Glynn's Anvil*, y Bone Spirit resurgió como líder. **EZG y agregadores:** Blood Wave es «T0» tras el 3.1.1. **DiabloBytes:** el Gólem es la más fuerte contra jefe único. La fuente de primer nivel más reciente es la retrospectiva, y lo que dice os incomoda: la que sube es la que os vetan los charms.
:::

::: evidencia nivel=disputa fuentes=maxroll-tierlists,diablobytes
El tier de Minion también está en disputa: Maxroll lo pone en **B** de endgame y **S** de leveleo; DiabloBytes y varios agregadores sostienen que **se mantiene en A** pese al nerfeo de *Hellbent Commander*. Aviso de método: DiabloBytes y Mobalytics devolvieron HTTP 403, así que esa versión se apoya en resúmenes de búsqueda, no en la página abierta.
:::

## Uno · Esbirros (Minion) ✅

Es vuestra build: no la mejor de la tabla, sino la única cuyo poder vive donde podéis llegar.

::: evidencia nivel=corroborado fuentes=ezg,icyveins-summoner,datos-juego-3-1-0
El rework movió los esbirros del Libro de los Muertos al árbol, *«ya no dependes de poderes legendarios ni de drops de equipo específicos»*. Los desbloqueos son por **nivel de personaje**, verificados en el fichero de datos: Mago Esquelético 3, Guerrero Esquelético 4, Gólem 8, Maldiciones 13, Definitivas 19. Cada habilidad tiene **15 rangos** y el nivel máximo es **70**. El rework es gratis.
:::

::: build nombre="Esbirros — arranque" estado=arranque entitlement=base
**El árbol es la build.** Aparcáis los primeros puntos en Segar y, en cuanto abre el clúster Fundamentales, reespecializáis (es gratis) y os vais a Mago Esquelético. Después Guerrero Esquelético y Zarcillos de Cadáver, luego Gólem, luego Doncella de Hierro y por último Ejército de los Muertos **solo** por *Unyielding Commander*. Regla de gasto: **amplitud primero, profundidad al final.**

Barra: maldición, Comando de Guerreros, Gólem, hueco flexible (Niebla de Sangre o Segar), Ejército de los Muertos, Zarcillos de Cadáver. Equipo: **nada exótico, todo del Códice de Poder**, que se llena completando mazmorras y desguazando legendarios. Prioridad: *Hardened Bones*, *Reanimation*, *Hellbent Commander*, *Hewed Flesh*, *Glynn's Anvil*. El mejor aspecto ofensivo va al **amuleto**.

**Cómo salís de aquí:** a nivel máximo y limpiando Pit hasta abrir el primer Tormento, que es cuando caen Ancestrales. **El objeto que desbloquea el salto es Deathgrip** (guantes): lo suelta **Grigoire**, en el Hall of the Penitent, con una Lair Key normal. Esas llaves llueven de Nightmare Dungeons, Helltides y la colección «Keys» del Árbol de los Susurros. Base y repetible a voluntad.
:::

::: build nombre="Esbirros — intermedia" estado=intermedia entitlement=base
Con Ancestrales cayendo, la build deja de ser «el árbol» y empieza a ser equipo. Únicos por utilidad real: **Deathgrip / The Hand of Naz** (guantes, esbirro extra y área) de Grigoire · **The Undercrown** (casco, guerreros y magos extra) · **Blood Moon Breeches** (pantalón), que aplica maldiciones sin gastar hueco de barra y es el sustituto directo de las runas `Teb` y `Wat` 🔒.

**Cómo salís de aquí:** el salto lo desbloquea un **Mítico**, y vuestra vía es el drop, no el crafteo. Mejor fuente: el **Corrupted Reaper** del Pandemonium Threshold, en Zarbinzet (Hawezar, zona base ✅). Se invoca con **Betrayer's Husk** de las Deathtoll Chambers y su Hoard se abre con **Superior Lair Keys**, de esas mismas cámaras. A las cámaras se llega por Realmwalker o, de forma controlable, por **Nightmare Dungeon con afijo Ruptures**. Segunda vía: la caché del Herrero con Resplendent Sparks, que da un Iconic aleatorio.
:::

::: build nombre="Esbirros — aspiracional" estado=aspiracional entitlement=base
Míticos por drop, glifos altos y Masterworking en orden **S.T.E.A.M.**: engarce, temple, encantamiento, aspecto y masterwork al final, porque multiplica lo anterior. Tableros según Icy Veins: Starter, Frailty, Cult Leader, Flesh Eater y Wither — ojo, Wither pasó a daño de **Frío**, así que vuestro escalado va a Frío. Glifos (Warrior): Warrior, Mage, Essence, Eliminator, Abyssal.

**Aquí se acaba vuestra escalera.** El siguiente escalón no es un objeto farmeable: es el set de charms *Black Shroud* 🔒 LoH y el multiplicador del mercenario 🔒 VoH. No hay sustituto y no lo voy a pintar de otro color.
:::

::: evidencia nivel=unica fuentes=maxroll-minion-guide,icyveins-summoner
Objetivos de las guías: **100% de velocidad de ataque** (prioridad número uno), **100% de crítico**, **30.000 de vida** mínimo y **40 o más** acumulaciones de Resolve en la híbrida. Libro de los Muertos según Icy Veins: Guerreros **Segadores** (+50% de daño), Magos **Sombra** (barrera), Gólem **Hierro sacrificado** (+15% de daño crítico). *Hellbent Commander* fue nerfeado a **40–60%**: recorta esta build directamente.
:::

## Dos · Blood Surge (Oleada de Sangre) ✅

Vuestro motor de farmeo: una tecla, área enorme y aspectos de Códice en vez de charms.

::: build nombre="Blood Surge — arranque" estado=arranque entitlement=base
Barra: Oleada de Sangre en spam, Tormenta de Huesos al entrar, Zarcillos de Cadáver para agrupar, Prisión de Huesos por la velocidad de ataque, Segar para moverse y un hueco de recursos (Hemorragia, Niebla de Sangre o *Life Tap*). **Uno de esos huecos se lo come la maldición a mano**: no tenéis las runas que la automatizan.

Libro de los Muertos: Guerreros **Defensores** (orbes de sangre y Vulnerable) y Magos **Frío** (regeneración de Esencia).

Aspectos, todos de Códice: *Juggernaut's* en pecho, *Tidal* en botas, *Exploiter's* en amuleto (la guía lo imprime con el Cubo 🔒; vosotros por drop o Códice).

**Cómo salís de aquí:** el objeto que abre el siguiente escalón es **Cruor's Embrace** (guantes), que suelta **Lord Zir** en Ancient's Seat con una Lair Key normal ✅. Misma llave que ya farmeáis para Grigoire: no cambia la rutina, solo el jefe.
:::

::: build nombre="Blood Surge — intermedia" estado=intermedia entitlement=base
Con Cruor's Embrace puesto, el objetivo es **Blood Moon Breeches**, que os devuelve el hueco de barra que come la maldición. Su fuente documentada es **Astaroth**, al final de las Escalating Nightmares, y ahí hay un problema serio: última sección.

Contenido: Infernal Hordes, donde esta build brilla y donde menos pesa no tener expansión (oro, Obducita, Almas Olvidadas y un Ancestral con Greater Affix garantizado).

**Cómo salís de aquí:** con un Mítico de drop. El primero que queréis es **Ring of Starless Skies**, que resuelve la gestión de recursos de golpe. Vía: Corrupted Reaper en bucle, con jefes de guarida de fondo, porque cualquier jefe de guarida puede soltar un único en calidad mítica.
:::

::: build nombre="Blood Surge — aspiracional" estado=aspiracional entitlement=base
Míticos por orden de deseo: Ring of Starless Skies, Blood Moon Breeches, Cruor's Embrace, Crown of Lucion. Glifos: Dominate, Corporeal, Essence, Imbiber, Amplify.

**El techo:** el objetivo de crítico es más difícil sin la runa `Gar` 🔒, que apila crítico ella sola. Se compensa con joyería, gemas y rangos de Tormenta de Huesos, pero **en parte**.
:::

::: evidencia nivel=oficial fuentes=blizzard-notas-3-1-x,maxroll-blood-surge
Notas oficiales del parche 3.1.1: *«Fixed an issue that was preventing certain sources of Uniques from dropping as Mythic, including Lair Bosses»*. Los jefes de guarida son juego base ✅, así que esa vía de Míticos os funciona. Guía de Blood Surge, 13 de agosto de 2026, la más reciente del catálogo. Son **mínimos**, no valores cerrados: coste de recurso **>15%**, regeneración de Esencia **>10**, velocidad de ataque **>70%** con Ferocity, crítico **>85%** con Tormenta de Huesos y tres templados de «Lucky Hit Chance: Restore Resource» en joyería. El glifo *Essence* exige nivel 50 antes de subirlo.
:::

## Tres · Blood Wave (Ola de Sangre) ✅ condicional

El techo más alto que podéis tocar, con el pilotaje más bajo del catálogo. El condicional es real.

::: evidencia nivel=disputa fuentes=icyveins-blood-wave,tabla-botin-comunidad,maxroll-blood-wave
La build entera pivota sobre un objeto, **Kessime's Legacy** (pantalón). Icy Veins lo sitúa en la tabla de botín de **Andariel**, jefe de guarida base ✅ que se abre con Greater Lair Key. En contra: la tabla comunitaria de botín de nigromante de esta temporada lista para Andariel solo **Lidless Wall** y **Ebonpiercer**. Puede ser una tabla incompleta o un error de Icy Veins; nadie lo ha cerrado. Y la guía de Maxroll dice *«Lord of Hatred has fundamentally transformed everything about this build»*: jugaréis una versión recortada.
:::

::: build nombre="Blood Wave — arranque" estado=arranque entitlement=base
**No la leveléis.** Subid con esbirros, que es S en leveleo, y guardad esta build en la **Armería** ✅ como segundo loadout para cuando tengáis el pantalón. El arranque real es acumular llaves: Lair Keys de Nightmare Dungeons y Helltides y, con ellas, los Hoards de los jefes Initiate, **que es de donde salen las Greater Lair Keys**.

**Cómo salís de aquí:** con **Kessime's Legacy** en la mochila. Se farmea gastando Greater Lair Keys en **Echo of Andariel**, en Hanged Man's Hall, Kehjistan ✅. Si tras muchas llaves no aparece, la tabla comunitaria tenía razón: pasad al plan B.
:::

::: build nombre="Blood Wave — intermedia" estado=intermedia entitlement=base
Barra: Ola de Sangre con **Hematolagnia**, Segar para acercarse y generar cadáveres, Niebla de Sangre, Lanza de Sangre solo para mantener Sobrepoder, Prisión de Huesos y Zarcillos o vuestra maldición.

Aspectos, todos de Códice: *Juggernaut's*, *Hardened Bones*, *Tidal*, *Exploiter's*, más *Thickened Blood*, *Tides of Blood* y *Untimely Death*.

**Cómo salís de aquí:** el desbloqueo es **Ring of Starless Skies** para los recursos y **Banished Lord's Talisman** para el amuleto. Ambos Míticos, misma vía de siempre: **Corrupted Reaper** en Zarbinzet, con jefes de guarida de fondo.
:::

::: build nombre="Blood Wave — aspiracional" estado=aspiracional entitlement=base
El remate es **Kessime's Legacy en calidad mítica**, que sin Cubo 🔒 no se craftea: os tiene que caer así de Andariel. Variante de empuje: *Glynn's Anvil*, *Disobedience*, *Interdiction*, *Redirected Force* y *Blood-Mad Idol*.

**El techo:** aquí la versión de guía se separa de la vuestra sin remedio, porque incluye tres runewords 🔒 y el mercenario Subo 🔒. Es la build con la que más lejos llegaréis y también con la que más se nota la diferencia.
:::

::: evidencia nivel=unica fuentes=maxroll-blood-wave
Guía actualizada el 17 de julio de 2026: regeneración de Esencia **15+**, reducción de coste de recurso **15%+**, crítico **70%+**, velocidad de ataque **50%+** con Ferocity y tres templados de «Lucky Hit: Restore Resource» en joyería. Glifos: Dominate, Essence, Gravekeeper, Imbiber, Corporeal. **Sobrepoder recibió nerfeos significativos** y el glifo **Dominate fue nerfeado**.
:::

## Plan B · Bone Spear (Lanza de Hueso) ✅

C de endgame y C de push: **no os lleva a la cima**, sin adornos. Pero es la ficha que menos depende de nada exótico. Vuestro paracaídas si Kessime's Legacy no aparece.

::: build nombre="Bone Spear — arranque" estado=arranque entitlement=base
Tormenta de Huesos y luego spam de Lanza de Hueso. Los Magos Esqueléticos os sostienen la Esencia: el Libro de los Muertos sigue importando aunque no seáis invocador.
**Cómo salís de aquí:** con *Aspect of Rapid Ossification* del Códice, que convierte el bucle en una build al recortar el enfriamiento de Tormenta de Huesos.
:::

::: build nombre="Bone Spear — intermedia" estado=intermedia entitlement=base
Dos objetivos: **Deathless Visage** (casco), de **The Beast in the Ice** en Glacial Fissure con Lair Key ✅, y **Lidless Wall** (escudo), de **Echo of Andariel** con Greater Lair Key ✅. Jefes de guarida base, repetibles.
**Cómo salís de aquí:** con esos dos puestos, el siguiente escalón vuelve a ser Mítico de drop del Corrupted Reaper.
:::

::: build nombre="Bone Spear — aspiracional" estado=aspiracional entitlement=base
Míticos: Deathless Visage, Blood Moon Breeches y Lidless Wall.
**El techo:** es una build C. El siguiente escalón no es un objeto: es cambiar de build.
:::

::: aviso tipo=truco
Truco exclusivo de esta build: **no reduzcáis el coste de Esencia.** Cuanta más gastáis por lanzamiento, más procs de *Rapid Ossification* y más reinicios de Tormenta de Huesos. Lo contrario de lo que buscan Blood Surge y Blood Wave.
:::

## Builds vetadas, y el motivo exacto

| Build | Por qué no |
|---|---|
| **Bone Spirit** (A) | Charm *Red Blessing* y set *Berú of Desecration* 🔒 LoH: pierde una capa entera de multiplicadores. Y exige resolver la Esencia |
| **Sever** | Set *Berú of the Black Shroud* 🔒 como columna vertebral. De base ya tiene área limitada y pico de daño bajo |
| **Army of the Dead** | Dos charms 🔒. La guía la describe como muy frágil y con bucle tedioso |
| **Golem** | Pide una cola larga de Míticos y sin crafteo 🔒 eso es lotería. **No vetada: aplazada** a fin de temporada |
| **Blight** | C y C, con *Red Blessing* 🔒 en la lista |
| **Blood Lance** | Guía sin actualizar desde junio, la más vieja del catálogo |
| **Soulrift** | **No existe** como build de endgame esta temporada; la famosa fue de una temporada antigua y dependía de un perk estacional muerto. Definitiva de apoyo ✅, no un plan |
| **Corpse Explosion** | Sin guía de endgame; se usa de relleno dentro de Army of the Dead. Habilidad ✅, build no |

::: aviso tipo=peligro
Filtro para **toda** guía que leáis: si lista un charm, un runeword, un mercenario, el Cubo Horádrico, la guadaña **Blood Wake** (Nahantu 🔒) o una tercera variante de habilidad, esa parte no es vuestra. Y si dice que cada habilidad tiene cinco rangos o menciona una Pasiva Clave, la guía entera está muerta aunque lleve fecha de este año.
:::

## Reparto del dúo

- **Uno de esbirros, otro de área.** El de esbirros ancla: tanquea, agrupa con Zarcillos y sostiene Vulnerable y Decrepitud; el otro revienta. **No llevéis los dos ejército completo**: redundancia de rol y caída de frames en consola.
- **Repartíos las maldiciones.** Cubrir Decrepitud y Doncella de Hierro cuesta dos huecos; uno lleva cada una y os devolvéis un hueco por cabeza. Es la mejor compensación por no tener `Teb` ni `Wat`.
- **Si uno va con mando**, que lleve esbirros o Blood Surge: área con auto-apuntado, frente al apuntado fino de Bone Spear. *(Criterio derivado, sin fuente.)*

## Lo que no se sabe y os afecta a la build

1. **El origen de varios únicos clave.** Nadie clasifica como base o expansión a *Crown of Lucion*, *Pact of Bone*, *The Undercrown*, *The Hand of Naz*, *Deathgrip* ni *Deathless Visage*. El eje gratis/pago documentado va de **sistemas**, no de items, lo que lo hace probable, pero no hay declaración oficial. Miradlo en vuestra colección de únicos antes de montar una build alrededor de uno.
2. **Cómo conseguir Escalation Sigils sin expansión.** Las rutas documentadas pasan por el Cubo 🔒, un nodo de War Plans 🔒 o un Grand Horadric Cache de estado desconocido. **Decide si Astaroth existe para vosotros, y con él Blood Moon Breeches**, el item más valioso del dúo. Es el hueco más caro del expediente.
3. **Si Hematolagnia está en vuestro árbol.** Si llegó con la expansión, Blood Wave queda tocada. Un vistazo al clúster Definitivas el primer día.
4. **Si *Unyielding Commander* se solapa entre dos nigromantes.** Nadie lo ha investigado. Probadlo.
5. **El bug del Gólem de Hueso.** Un jugador del foro oficial reporta que **no aplica Vulnerable** pese al texto, sin respuesta de Blizzard. No construyáis asumiendo esa vulnerabilidad sin verla en pantalla.

::: evidencia nivel=oficial fuentes=captura-jugador
Verificado en pantalla el 18 de agosto de 2026, cliente en español, parche 3.1.3: los Defensores obtienen **10 espinas** de base y astillan por el **50%** al recibir daño; comandarlos hace que **provoquen 6 segundos**; su otra mejora da **10%** de probabilidad de orbe de sangre al infligir daño. El Gólem de Hueso comandado **crea 5 cadáveres**. Las mejoras se alternan libremente, sin coste. El Sacrificio aparece **bloqueado** a nivel 8. Ninguno de estos textos coincide con los de las wikis generalistas: los suyos están muertos.
:::
