# El PALADÍN (Paladin) de cero — clase, recurso, mecánica y árbol

**Fecha de la investigación:** 19 de agosto de 2026 (fichero generado 24/08/2026)
**Estado del juego asumido:** Diablo IV, Temporada 14 "Death Awakening" (desde 30/06/2026), **parche vivo 3.1.3, build 73224, 12/08/2026**
**Dominio de este documento:** SOLO la clase Paladín — recurso, mecánica única, árbol de habilidades, niveles de desbloqueo, puntos totales, fortalezas y fragilidades. **No cubre** builds concretas, objetos, aspectos, míticos ni Paragón (eso va en otros documentos del proyecto).
**Jugador objetivo:** principiante, con Vessel of Hatred y Lord of Hatred, personaje nuevo de Paladín, juega la mitad del tiempo en dúo con una pareja sin expansiones.

---

## 0. AVISO DE MÉTODO — lee esto antes que la tabla

Tres cosas que condicionan **todo** lo que sigue:

**0.1. El Paladín es una clase joven y hay muchísimo dato muerto circulando.** Esta clase se pudo jugar desde diciembre de 2025 (acceso anticipado por reserva) y la expansión salió el 28/04/2026. Entre medias hubo un **rework total del árbol de habilidades** (parche 3.0, 28/04/2026). Casi todas las guías escritas entre diciembre de 2025 y abril de 2026 describen un árbol que **ya no existe**. Ver §13, que es la sección más importante del documento para ti.

**0.2. Los niveles exactos de cada clúster NO están escritos en ninguna guía web que haya podido abrir.** Icy Veins tiene la página de habilidades del Paladín actualizada a Temporada 14, pero —a diferencia de la del Nigromante— **no lleva los niveles entre corchetes en los encabezados** (comprobado descargando el HTML y listando los `<h2>/<h3>`: los encabezados son solo «Basic Skills», «Core Skills», «Aura Skills», «Valor Skills», «Justice Skills», «Ultimate Skills», «Dismount Skill»). Los niveles concretos de este informe salen del **fichero de datos del juego** (datamining, ver 0.3) y encajan exactamente con la escalera genérica publicada por Maxroll. Lo digo aquí para que no me atribuyas una precisión que no tengo de fuente redactada.

**0.3. Datamining declarado.** He descargado y analizado el fichero que sirve el planificador de Maxroll:
`https://assets-ng.maxroll.gg/d4-tools/game/data.min.json` — **HTTP 200, 11 606 292 bytes (11,6 MB), descargado el 24/08/2026**.
Su campo `version` dice: **`3.1.0.72698`**.

> ⚠️ **Eso es parche 3.1.0, build 72698 — NO es el parche vivo 3.1.3, build 73224.** El fichero va **tres parches por detrás** (3.1.1, 3.1.1a, 3.1.2/3.1.3). Todo lo estructural (clústeres, niveles, nombres, tags) es fiabilísimo porque no lo tocó ningún hotfix; los **valores numéricos** de este fichero los marco y los contrasto con las notas oficiales siempre que puedo. Donde el número del datamining coincide con las notas de parche oficiales de 3.1.0, lo doy por vivo. Donde no lo he podido contrastar, lo digo.

**0.4. Hay un PTR 3.2 activo desde el 30/07/2026.** El foro oficial que Maxroll incrusta en sus páginas muestra hilos como «PTR 3.2 Known Issues - 8/4/2026» y «The 3.2.0 PTR: What You Need to Know» (30/07/2026). Si te cruzas con vídeos o posts de agosto que hablan de cambios al Paladín, **comprueba que no sean del PTR 3.2**: eso no está en tu partida.

---

## 1. RESUMEN EJECUTIVO — lo que necesitas saber en 10 líneas

| Pregunta | Respuesta corta |
|---|---|
| ¿Qué recurso usa? | **Fe (Faith)**. Se genera con las Básicas y con Rally, y se regenera sola despacio. |
| ¿Tiene algo como el Libro de los Muertos? | Sí: los **Juramentos (Oaths)**. Se desbloquean a **nivel 15** y eliges **1 de 4**. Es un solo interruptor, mucho más simple que el Libro. |
| ¿Cuántos clústeres tiene el árbol? | **6**, igual que las demás clases. |
| ¿A qué niveles se abren? | **1 / 3 / 4 / 8 / 13 / 19** (Básicas / Fundamentales / Auras / Valor / Justicia / Definitivas). |
| ¿Cuántas habilidades? | **24** (4 / 5 / 3 / 4 / 4 / 4). |
| ¿Cuántos puntos a nivel 70? | **83** (69 por subir de nivel + 14 por Rango de Temporada). |
| ¿Rango máximo por habilidad? | **15** (y más allá con objetos). |
| ¿Qué la hace fuerte? | Aguante brutal, velocidad, y **auras que buffan también a tu pareja**. |
| ¿Qué la hace frágil? | Cuerpo a cuerpo, muy dependiente de enfriamientos, poco flexible, y sin ráfagas de daño inmediato. |
| ¿Rotaciones difíciles? | No. Es de las clases con menos ceremonia: aura(s) puestas + una Fundamental que machacas. |

---

## 2. QUÉ ES EL PALADÍN Y CUÁNDO LLEGÓ — un conflicto de fuentes que hay que resolver

El briefing de este encargo decía «el Paladín es clase NUEVA (parche 3.0, 28/04/2026)». **Es correcto a medias y conviene precisarlo**, porque explica por qué hay tanta guía caducada.

| Hito | Fecha | Fuente |
|---|---|---|
| El Paladín se anuncia y se puede **jugar por reserva anticipada**, antes de que salga la expansión | **diciembre de 2025** | *"Pre-purchase and play the new Paladin class immediately."* — https://news.blizzard.com/en-us/article/24247511/stand-against-mephisto-pre-purchase-lord-of-hatred · artículo en español del 16/12/2025: https://news.xbox.com/es-latam/2025/12/16/guiado-por-la-luz-el-paladin-se-une-a-diablo-iv/ |
| Temporada 11 «Divine Intervention», parche **2.5.0** — el Paladín entra con ella | **12/12/2025** | Changelog de Maxroll: *"December 12, 2025 — Post created for Season 11 / Patch 2.5.0"* — https://maxroll.gg/d4/resources/paladin-class-overview |
| **Lord of Hatred sale**, con **dos** clases nuevas | **28 de abril de 2026** | *"unlock a second new class at launch on April 28, 2026"* — https://news.blizzard.com/en-us/article/24247511/stand-against-mephisto-pre-purchase-lord-of-hatred · la página oficial de la expansión rotula **"TWO NEW CLASSES"** — https://diablo4.blizzard.com/en-us/lord-of-hatred |
| Rework total del árbol de habilidades (parche 3.0) | **28/04/2026** | Ya documentado en `investigacion/crudo/arbol-estructura.md` de este proyecto |
| La segunda clase nueva es el **Brujo (Warlock)** | anunciado 05/03/2026 | Hilo oficial «Master Hell Itself with the Warlock», 2026-03-05, visible en el foro incrustado en https://maxroll.gg/d4/build-guides/shield-charge-paladin-leveling-guide · el datamining lo confirma: existe una clase `Warlock` con recurso `Wrath` |

> ⚠️ **Contradicción detectada y resuelta.** La página de Maxroll dice literalmente: *"Introduced with Season 11 / Patch 2.5.0 (Diablo IV Vessel of Hatred), the Paladin emerges as an oldschool classic going all the way back to Diablo 2"* (https://maxroll.gg/d4/resources/paladin-class-overview). El paréntesis **"(Vessel of Hatred)" es un error de Maxroll**: la página oficial de Blizzard presenta al Paladín como una de las dos clases nuevas de **Lord of Hatred** (https://diablo4.blizzard.com/en-us/lord-of-hatred). Lo correcto es: *el Paladín es la clase de Lord of Hatred, jugable por adelantado desde la Temporada 11 si reservaste la expansión*. **Tú tienes Lord of Hatred, así que lo tienes desbloqueado sin más.**

**Fantasía de clase (oficial, en español):** *"Canaliza la Luz sagrada"*, «renacido a través de los **Guardianes de la Luz**, una orden dedicada a defender Santuario» — https://diablo4.blizzard.com/es-es/lord-of-hatred. Los Guardianes de la Luz son **lore, no una mecánica**: no hay barra de facción ni progresión asociada. La mecánica es el Juramento (§4).

---

## 3. EL RECURSO: FE (Faith)

### 3.1 Confirmación dura

| Dato | Valor | Fuente |
|---|---|---|
| Nombre del recurso | **Fe (Faith)** | Datamining: `classes["6"].primaryResource.type = 9` y `uiStrings.resourceType["9"] = "Faith"`. Es el único tipo 9 del juego. |
| Es exclusivo del Paladín | Sí | Datamining: las entradas «Faith Regeneration», «Faith Generation» y «Faith On Kill` de `heroDetails` llevan `classFilter` con `true` **solo en la posición 6** (= Paladín) |
| De dónde sale | **Habilidades Básicas + Rally**, más regeneración pasiva lenta | *"Their abilities are fueled by Faith which comes from using Basic Skills and Rally, and also slowly regenerates over time."* — https://maxroll.gg/d4/resources/paladin-class-overview |
| Regeneración pasiva | Existe como estadística propia | Datamining, tooltip: *"Passive Faith Regeneration: … You regenerate {X} Faith per second."* |
| Fe al matar | Existe como estadística propia | Datamining, tooltip: *"Faith On Kill: … You will restore {X} Faith for every enemy you kill."* |
| Atributo que aumenta la generación | **Voluntad (Willpower)** — 0,5 % de generación de recurso por cada 100 | https://maxroll.gg/d4/resources/paladin-class-overview · corroborado por el datamining (`classes["6"].resourceAttribute = 2` = Willpower) |

### 3.2 Cuánta Fe genera y cuesta cada habilidad

Estos números vienen de **Icy Veins, página actualizada el 29/06/2026 para la Temporada 14** (https://www.icy-veins.com/d4/guides/paladin-skills/), y **cuadran exactamente** con las fórmulas del datamining (p. ej. Brandish `Generate Faith: 14+…` / Holy Bolt `16+…`). Que dos vías independientes den el mismo número es la mejor señal de vigencia que tengo.

**Generadoras (Básicas):**

| Habilidad | Fe generada |
|---|---|
| Clash | **20** |
| Advance | **18** |
| Holy Bolt | **16** |
| Brandish | **14** |

**Gastadoras (Fundamentales / Core):**

| Habilidad | Coste de Fe | Coste extra |
|---|---|---|
| Blessed Hammer | **10** | — |
| Zeal | **20** | **+10 % de vida** (datamining: `Health Cost:10%`) |
| Divine Lance | **25** | — |
| Blessed Shield | **28** | — |
| Shield Bash | **32** | — |

**Otras que gastan Fe:** Fanaticism Aura **10**, Defiance Aura **25**, Spear of the Heavens (coste variable, no cifrado en la tabla). **Rally cuesta vida, no Fe**: datamining `Health Cost: 35 %` (o 29,75 % con un modificador), y a cambio genera `15 + rango` de Fe.
Todos estos valores: https://www.icy-veins.com/d4/guides/paladin-skills/

### 3.3 Qué significa esto para ti, principiante

- La gestión es la clásica «genera con la Básica, gasta con la Fundamental». **No hay cadáveres, ni esencia que se autorregenere, ni un Libro que administrar.** Es más simple que tu Nigromante.
- **Ojo con Zeal y con Rally: pagan con VIDA.** Icy Veins lista *"Uses health as a resource"* como **debilidad** explícita de la build de Zeal — https://www.icy-veins.com/d4/guides/zealot-paladin-build/ (actualizada 25/06/2026, T14). Si eres principiante y vas a ir de Shield Charge, esto no te afecta: Shield Charge no cuesta vida.
- Hay una vía para **saltarse la Fe casi entera**: Icy Veins señala que *"Faith is used for casting many skills but there are some nodes in the tree that will shift that resource over to Life instead"* (https://www.icy-veins.com/d4/guides/paladin-skills/). No es la ruta recomendada para empezar.

> **No encontrado:** el valor **máximo de Fe** (equivalente a los 100 de maná). Ni Maxroll, ni Icy Veins, ni el datamining lo exponen como número plano. No lo invento.

---

## 4. LA MECÁNICA DE CLASE: LOS JURAMENTOS (Oaths) — el «Libro de los Muertos» del Paladín

### 4.1 Cómo funciona

| Dato | Valor | Fuente |
|---|---|---|
| Nombre | **Juramentos (Oaths)** | https://maxroll.gg/d4/resources/paladin-class-overview |
| Nivel de desbloqueo | **Nivel 15** | *"At level 15, you can select one of the four possible options"* — https://maxroll.gg/d4/resources/paladin-class-overview · *"This mechanic will unlock upon reaching Level 15"* — https://www.icy-veins.com/d4/guides/paladin-leveling-guide/ (act. 29/06/2026, T14) |
| Cuántos hay | **4** | Ambas fuentes; el datamining lista exactamente 4 en `classes["6"].paladinOaths` |
| Cuántos puedes llevar | **1 a la vez** | https://maxroll.gg/d4/resources/paladin-class-overview |
| ¿Hace falta misión? | No consta ninguna. Se abre solo al llegar a 15 | Ninguna de las fuentes vivas menciona misión de desbloqueo |

**Diferencia clave con el Libro de los Muertos:** el Libro del Nigromante es un panel con muchas casillas independientes que retocas constantemente. El Juramento es **una sola elección de cuatro**, y —según Maxroll— ni siquiera es la decisión que define tu build: *"this can be seen more as an enhancement of your existing kit rather than a build defining choice, as their impact is usually narrowly tailored towards a certain archetype"* (https://maxroll.gg/d4/resources/paladin-class-overview). Es decir: **el Juramento lo escoge tu build por ti**. Si vas de Shield Charge, vas de Juggernaut y punto.

### 4.2 Los cuatro Juramentos, con sus números vivos

Texto **verbatim del datamining 3.1.0** (entradas `Paladin_Oath_*` de `skills`), con los porcentajes **verificados contra las notas de parche oficiales de 3.1.0** (https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes).

| Juramento | Español oficial | Qué hace (traducción del texto del juego) | Número clave | Verificación oficial |
|---|---|---|---|---|
| **Zealot** | *El zelote* | Lanzar habilidades Zealot da **Fervor** durante 2 s (4 s con cierto afijo). Al **golpe crítico**, la habilidad hace un **eco** por un **25 %** extra del daño, repetido **una vez por cada acumulación de Fervor**. A Fervor máximo, además **Fortifica** un 1 % de tu vida máxima. | **25 %** por eco; Fervor acumula hasta **3** (datamining, buff `Fervor`, `maxStackCount: 3`) | ✅ *"Zealot Oath: Damage per echo increased from 21% to 25%."* (parche 3.1.0) |
| **Juggernaut** | *El juggernaut* | Lanzar una habilidad Juggernaut **consume 8 acumulaciones de Resolve** y te da **+80 % de daño multiplicativo** y **+20 % de tamaño** durante **5 s** en tus habilidades Juggernaut. Tu **Resolve mínimo sube en 1** y **deja de consumirse al recibir golpes**. | **80 %[x]**, **8** acumulaciones, **5 s** | ✅ *"Juggernaut Oath: Damage increased from 60% to 80%."* (parche 3.1.0) |
| **Judicator** | *El judicante* | Tus **Básicas aplican Judgement**. El Judgement lo puedes **detonar antes** con tus **Fundamentales Judicator**, haciendo **80 % de daño de arma** en área pequeña. Al **Juzgar** a un enemigo, **el daño que le haces sube un 80 %[x] hasta que muera**. | **80 %[x]** | ✅ *"Judicator Oath: Damage increased from 60% to 80%."* (parche 3.1.0) |
| **Disciple** | *El árbitro* | Lanzar una habilidad Disciple **con enfriamiento** te da forma **Arbiter** durante **4,5 s**. En forma Arbiter, tus habilidades Disciple hacen **+80 % de daño multiplicativo**. Además, **Wing Strikes** gana los beneficios de habilidad Disciple. | **4,5 s**, **80 %[x]** | ✅ *"Disciple Oath: Damage increased from 50% to 80%."* (parche 3.1.0) |

Nombres en español: https://diablo4.blizzard.com/es-es/lord-of-hatred (*"El árbitro"*, *"El zelote"*, *"El judicante"*, *"El juggernaut"*).

> ⚠️ **Tres trampas de datos muertos que he pillado en esta misma sección — todas son números que verás repetidos por ahí y que ya NO valen:**
>
> 1. **Blizzard anunció «17 %» de eco en Zealot** — https://news.blizzard.com/en-us/article/24244399/wield-divine-might-as-the-paladin. Eso es **pre-3.1.0**. Las propias notas de parche muestran la escalera: *"increased from 17% to 21%"* (parche 3.0/expansión) y luego *"increased from 21% to 25%"* (3.1.0). **El valor vivo es 25 %.**
> 2. **Icy Veins dice que Disciple da «50% increased damage»** — https://www.icy-veins.com/d4/guides/paladin-skills/. Ese es el valor **anterior a 3.1.0**. Las notas oficiales dicen *"Disciple Oath: Damage increased from 50% to 80%"*. **El valor vivo es 80 %.** (La página está actualizada al 29/06/2026 pero ese dato concreto se les quedó atrás.)
> 3. **El propio fichero de datos tiene DOS versiones del texto de los Juramentos y una está podrida.** El bloque `classes["6"].paladinOaths` contiene descripciones viejas —habla de *"Devotion Core"*, de *"Zealot stacks"*, y en Disciple pone `[PH]` (placeholder) y «6 seconds»— mientras que las entradas reales `skills["Paladin_Oath_*"]` tienen el texto actual y coincidente con las notas oficiales. **He usado las segundas.** Lo cuento porque cualquiera que datamine este fichero sin mirar puede publicar los números zombis del primer bloque.
>
> ⚠️ **Cuarta discrepancia, esta de nombres:** la página oficial en inglés y en español llama a la cuarta especialización **"The Arbiter" / "El árbitro"** (https://diablo4.blizzard.com/es-es/lord-of-hatred), pero **dentro del juego el Juramento se llama «Disciple»** (datamining: el fichero interno es `Paladin_Oath_Angel` y el nombre mostrado en las guías vivas es *Disciple*; https://maxroll.gg/d4/resources/paladin-class-overview y https://www.icy-veins.com/d4/guides/paladin-skills/ usan «Disciple»). **«Arbiter» es el nombre de la FORMA** en la que te transformas, y también el de la Definitiva *Arbiter of Justice*. Si buscas «Arbiter Paladin» encontrarás la build del Juramento Disciple.

### 4.3 ¿Se puede cambiar de Juramento?

**No lo he podido confirmar por escrito en una fuente preferente.** Un extracto de buscador afirmaba «Respec is free — swap Oaths freely», pero no he podido abrir la página que lo sostiene y **no lo doy por bueno**. Lo que sí está confirmado en este proyecto es que **reasignar puntos del árbol de habilidades es gratis** (https://maxroll.gg/d4/getting-started/skill-trees, ver `investigacion/crudo/arbol-estructura.md` §; *"You can also refund any point in your skill tree … completely free of charge!"*). Para el Juramento en concreto: **ver §17, No encontrado.**

---

## 5. LAS SEIS PALABRAS CLAVE DEL PALADÍN

El Paladín tiene su propio vocabulario de mecánicas. Esta lista es **verbatim de Maxroll** (https://maxroll.gg/d4/resources/paladin-class-overview, actualizada 14/07/2026 para T14), ampliada con lo que confirma el datamining:

| Palabra clave | Atada a | Qué hace | Confirmación adicional |
|---|---|---|---|
| **Resolve** | Juramento **Juggernaut** | *"reduces incoming damage and can trigger certain buffs"*. Es un contador de acumulaciones. Base **8**, ampliable hasta **30** con objetos. | Datamining, fórmula del buff: `Min(30, … 8 + …)`. La guía de Shield Charge de Maxroll dice literalmente que apuntes a *"30 Maximum Resolve Stacks"* — https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide (25/07/2026, T14) |
| **Judgement** | Juramento **Judicator** | *"marks enemies until they explode for some damage"* | Datamining: buff con `maxStackCount: 15` y marcas de 20 s |
| **Arbiter** | Juramento **Disciple** | *"transforms you into an angelic form with enhanced abilities"* | Datamining: `Paladin_Sub_Angel`, con acumulaciones «Angelic Ascension» (hasta 10) que se pierden al salir de la forma |
| **Fervor** | Juramento **Zealot** | *"builds up a stacking buff that makes your attack multi-hit"* | Datamining: *"Certain Skills are empowered for each stack of Fervor"*, **máximo 3 acumulaciones** |
| **Retribution** | Bloqueo + Espinas | *"Creates Thorns explosions around you, triggered by specific skills and passives"* | Datamining, tooltip de estadística: *"Retribution Chance: When you Block, you have a chance to release a nova dealing {X} of your Thorns damage."* |
| **Weaken** | Transversal | *"Reduces enemy damage and triggers certain conditions for other buffs"* | Aparece como `Keyword_Weaken` en Fanaticism Aura y como modificador en Advance, Zeal, Consecration, Condemn y Zenith |

**Nota que te afecta directamente (Shield Charge):** Resolve y Retribution son las dos palancas de esa build. Maxroll dice de ella que *"Hit Count As Blocking triggers Retribution, which works as the primary damage mechanic"* y que el daño de salida es **Espinas físicas** — https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide. Es decir: **tu daño principal saldría de bloquear, no de pegar**. Esto es raro y muy relevante para saber si te va a gustar. El detalle de la build no es mi dominio; lo dejo señalado.

---

## 6. ATRIBUTOS Y EQUIPO

| Atributo | Qué te da al Paladín | Fuente |
|---|---|---|
| **Fuerza (Strength)** — atributo principal | **12,5 % de daño de habilidad por cada 100** y **+200 de armadura por cada 100** | https://maxroll.gg/d4/resources/paladin-class-overview · corroborado por datamining: `damageAttribute: 0` (=Fuerza), `damageScalar: 1.25` |
| **Inteligencia (Intelligence)** | **0,25 % de prob. de crítico por cada 100** y **+40 a todas las resistencias por cada 100** | Ídem · datamining: `critAttribute: 1` (=Inteligencia) |
| **Voluntad (Willpower)** | **0,5 % de generación de recurso por cada 100** y **3,5 % de curación recibida por cada 100** | Ídem · datamining: `resourceAttribute: 2` (=Voluntad) |
| **Destreza (Dexterity)** | **0,6 % de esquiva por cada 100** — *"does less for scaling most Paladin builds"* | Ídem |

**Equipo:** *"The Paladin usually uses a One-Handed Weapon with a Shield, but can wield certain Two-Handed Weapons. They also have access to their own unique weapon type, **Flails (1h only)**."* — https://maxroll.gg/d4/resources/paladin-class-overview. El datamining confirma el tipo de arma exclusivo: existen los objetos `1HFlail_Unique_Paladin_001` a `004`.

**Tablero de Paragón:** el Paladín tiene **10 tableros propios** (`Paragon_Paladin_00` a `09`, datamining). No es mi dominio; lo dejo constatado.

---

## 7. EL ÁRBOL: LOS SEIS CLÚSTERES Y A QUÉ NIVEL SE ABRE CADA UNO

### 7.1 La tabla

**Confirmado que el modelo va por NIVEL DE PERSONAJE (`requiredLevel`), no por puntos gastados.** Los nodos raíz del árbol del Paladín en el fichero de datos llevan el campo `requiredLevel` explícito, y el fichero **no contiene ningún umbral de puntos gastados**.

| # | Clúster (inglés) | Español (traducción de trabajo) | **Nivel** | Nº de habilidades | Evidencia |
|---|---|---|---|---|---|
| 1 | **Basic Skills** | Habilidades Básicas | **Nivel 1** | 4 | Datamining: nodo raíz id `1848`, **sin** `requiredLevel` (= disponible de salida) |
| 2 | **Core Skills** | Habilidades Fundamentales | **Nivel 3** | 5 | Datamining: nodo raíz id `1845`, `requiredLevel: 3` |
| 3 | **Aura Skills** | Habilidades de Aura | **Nivel 4** | 3 | Datamining: nodo raíz id `1842`, `requiredLevel: 4` |
| 4 | **Valor Skills** | Habilidades de Valor | **Nivel 8** | 4 | Datamining: nodo raíz id `1844`, `requiredLevel: 8` |
| 5 | **Justice Skills** | Habilidades de Justicia | **Nivel 13** | 4 | Datamining: nodo raíz id `1952`, `requiredLevel: 13` |
| 6 | **Ultimate Skills** | Habilidades Definitivas | **Nivel 19** | 4 | Datamining: nodo raíz id `1949`, `requiredLevel: 19` |
| — | *Dismount Skill* | *Habilidad de desmontar* | — | 1 | No es un clúster de progresión; sección aparte |

### 7.2 Por qué me fío de esos niveles

**Triple encaje:**

1. **La escalera genérica publicada por Maxroll coincide exactamente.** *"Level 1: Basic cluster… Level 3: Core cluster… **Level 4, 8 and 13: Unique clusters per class**… Level 19: Ultimate Cluster"* — https://maxroll.gg/d4/getting-started/skill-trees. Los tres clústeres propios del Paladín (**Aura / Valor / Justicia**) caen justo en **4 / 8 / 13**.
2. **El mismo patrón ya está verificado para el Nigromante** en este proyecto: Cadáver 4 / Macabras 8 / Maldición 13 (`investigacion/crudo/arbol-estructura.md`, con cita de Icy Veins: *"Necromancer Curses unlock at level 13"*).
3. **La arquitectura del árbol es idéntica entre clases.** Contando los nodos del fichero: Paladín = 24 nodos de habilidad + 168 de modificador + 78 de puerta = **270**; Bárbaro = **24 + 168 + 78 = 270** exactamente igual; Nigromante = 23 + 161 + 75 = 259. No es un árbol improvisado para la clase nueva: es el mismo molde.

### 7.3 Detalle importante: **NO hay clúster de Pasivas ni Pasivas Clave**

En el árbol del Paladín **no existe ningún nodo de recompensa de tipo pasiva**. Los 270 nodos son: `type 0` = habilidad activa (24), `type 1` = modificador (168), y puertas sin recompensa (78). **Cero pasivas.** Esto confirma para el Paladín lo que el proyecto ya había establecido tras el rework 3.0: las pasivas salieron del árbol.

> ⚠️ El fichero de datos **sí conserva** entradas de talentos huérfanas con nombres apetecibles —`Paladin_Talent_KeyPassive_1` «Coat of Arms», `_2` «Path of the Penitent», `_3` «Judgement Day», `_4` «Exaltation»— **pero ninguna de ellas está enganchada al árbol**, y muchas llevan marcas `[WIP]` o `(PH)` (placeholder). Son restos. **Si alguien te enseña una «tabla de Pasivas Clave del Paladín», está leyendo basura del fichero o una guía pre-3.0.**

---

## 8. CÓMO ESTÁ MONTADA CADA HABILIDAD POR DENTRO

Esta es la parte que ninguna guía te explica bien y que cambia cómo gastas los puntos.

Cada una de las 24 habilidades tiene siempre la misma estructura:

```
        [ Nodo de la HABILIDAD ]  ← hasta 15 rangos
                  |
      +-----------+-----------+
      |           |           |
  [Puerta A]  [Puerta B]  [Puerta C]
   2 modif.    2 modif.    VARIANTE: elige 1 de 3
```

- **El nodo de la habilidad** admite hasta **15 rangos** (*"You can invest up to 15 skill points into each active skill"* — https://maxroll.gg/d4/getting-started/skill-trees), y **más allá de 15 con objetos** (*"Each active skill can be leveled up 15 times (**and further with items**)"* — https://maxroll.gg/d4/resources/paladin-class-overview).
- **Puertas A y B:** dos modificadores cada una, **3 rangos** cada modificador en la mayoría de habilidades, **5 rangos** en cinco de ellas (Clash, Holy Bolt, Advance, Shield Bash, Divine Lance) — datamining.
- **Puerta C:** la **variante**, que reescribe la habilidad. Hay **3 variantes y eliges 1**. Ojo: **dos de las tres están disponibles al abrirse la puerta, pero la tercera exige un nivel mucho más alto** (entre 30 y 40 según el clúster). Esto es datamining puro y no lo he visto escrito en ninguna guía.
- Descripción concordante de Maxroll: *"After unlocking a skill, you can enhance it with an additional 3 points in two modifiers and a variant choice to specialize that skill further."* — https://maxroll.gg/d4/resources/paladin-class-overview

**Coste de maximizar UNA habilidad entera:** 15 (habilidad) + 3+3 (puerta A) + 3+3 (puerta B) + 3 (variante) = **30 puntos**. Con 83 puntos totales **no llegas ni a tres habilidades completas**. Esto es lo que de verdad manda en tus decisiones.

### 8.1 Escalera de puertas por clúster (datamining)

| Clúster | Puerta A | Puerta B | Puerta C (variante) | 3.ª variante (tardía) |
|---|---|---|---|---|
| Básicas (nv. 1) | **nv. 5** | **nv. 9** | **nv. 14** | **nv. 30** |
| Fundamentales (nv. 3) | **nv. 6** | **nv. 10** | **nv. 15** | **nv. 32** |
| Auras (nv. 4) | **nv. 7** | **nv. 11** | **nv. 16** | **nv. 34** |
| Valor (nv. 8) | **nv. 12** | **nv. 17** | **nv. 20** | **nv. 36** |
| Justicia (nv. 13) | **nv. 18** | **nv. 21** | **nv. 23** | **nv. 38** |
| Definitivas (nv. 19) | **nv. 22** | **nv. 24** | **nv. 25** | **nv. 40** |

**Consecuencia práctica enorme para ti:** si vas a jugar **Shield Charge**, la habilidad es de **Valor** → la tienes **a nivel 8**, pero su **variante** (que es donde la build se define) no se abre hasta **nivel 20**, y la variante *Phalanx Charge* hasta **nivel 36**. Entre el 8 y el 20 juegas con la habilidad «cruda».

### 8.2 Cuánto vale subir rangos

Las fórmulas del Paladín en el fichero de datos usan una tabla de escalado por rango (`Table(37, sLevel)`). Sus valores: rango 1 = **1,00**; rango 5 = **1,16**; rango 10 = **1,30**; **rango 15 = 1,40**; rango 21 = **1,50**; y se **estanca en 1,60** hacia el rango 31.

Traducción: **pasar una habilidad de rango 1 a rango 15 multiplica por 1,40** la parte escalada de su efecto (armadura de Shield Charge, potencia de las Auras, curación de Consecration, duración de Fortress…). Es decir, **14 puntos para un +40 %**. Rendimiento decreciente muy marcado a partir del rango 10. Esto es datamining sin fuente redactada que lo corrobore; tómalo como orientación, no como evangelio.

---

## 9. LAS 24 HABILIDADES, UNA A UNA

Columna «Juramento» = a qué Juramento pertenece la habilidad. **Doble fuente:** el tipo lo publica Icy Veins (https://www.icy-veins.com/d4/guides/paladin-skills/, act. 29/06/2026, T14) como campo *"Oath Type"*, y coincide al 100 % con las etiquetas internas del fichero de datos (`Skill_Zealot`, `Skill_Juggernaut`, `Skill_Divine`=Judicator, `Skill_Disciple`).

**Nombres en español: NO los he encontrado.** Ver §16 y §17.

### 9.1 Básicas (Basic) — nivel 1

| Habilidad | Juramento | Genera Fe | Prob. golpe de suerte | Tipo daño | Qué hace |
|---|---|---|---|---|---|
| **Brandish** | Disciple | **14** | 20 % | Sagrado | Arco de Luz que hace daño en línea |
| **Holy Bolt** | Judicator | **16** | 44 % | Sagrado | Lanza un martillo sagrado |
| **Clash** | Juggernaut | **20** | 50 % | Físico | Golpe con arma y escudo; da **Marcha del Cruzado**: **+30 % de prob. de bloqueo** (datamining) |
| **Advance** | Zealot | **18** | 14 % | Físico | Avance con el arma (tiene etiqueta de movilidad) |

Fuente de todos los números: https://www.icy-veins.com/d4/guides/paladin-skills/

### 9.2 Fundamentales (Core) — nivel 3

| Habilidad | Juramento | Coste Fe | Prob. golpe de suerte | Tipo daño | Qué hace |
|---|---|---|---|---|---|
| **Zeal** | Zealot | **20** (+10 % vida) | 3 % | Físico | Golpea a velocidad cegadora: 1 impacto + **3 adicionales** |
| **Blessed Shield** | Judicator | **28** | 30 % | Sagrado | Lanza el escudo; **rebota hasta 3 veces** |
| **Blessed Hammer** | Judicator | **10** | 24 % | Sagrado | Martillo que **espiral**a hacia fuera |
| **Divine Lance** | Disciple | **25** | 6 % | Sagrado | Empala con una lanza celestial, **2 estocadas** |
| **Shield Bash** | Juggernaut | **32** | 16 % | Físico | Carga contra un enemigo y golpea con el escudo |

Fuente: https://www.icy-veins.com/d4/guides/paladin-skills/ · descripciones del datamining

### 9.3 Auras (Aura) — nivel 4

Las Auras **tienen una parte pasiva permanente y una activa**. Son *"a staple of every Paladin build"* — https://maxroll.gg/d4/resources/paladin-class-overview.

| Habilidad | Juramento | Coste | Enfriamiento | Qué hace (pasiva) |
|---|---|---|---|---|
| **Fanaticism Aura** | Zealot | 10 Fe | **15 s** | **Gastar Fe** emana poder: **+velocidad de ataque y +prob. de crítico a ti Y A TUS ALIADOS** |
| **Defiance Aura** | Juggernaut | 25 Fe | **20 s** | **+50 % de armadura y +50 % a todas las resistencias, a ti y a tus aliados** |
| **Holy Light Aura** | Judicator | — | **25 s** | Tú y tus aliados **emanáis Luz**: daño cada 2 s a 3 enemigos cercanos al azar. Activa: 2 rayos que encadenan hasta 4 enemigos más |

Enfriamientos y costes: https://www.icy-veins.com/d4/guides/paladin-skills/ · efectos: datamining.
El **+50 %** de Defiance Aura es un valor **verificado en notas oficiales**: *"Defiance Aura: Bonus Armor and Resistances increased from 30% to 50%."* (parche 3.1.0) — https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes

> **Esto es tu mejor argumento para el dúo.** Las tres auras dicen literalmente *"and your allies"* / *"you and your allies"*. Tu pareja nigromante, que **no tiene las expansiones**, se beneficia de tu Defiance Aura y tu Fanaticism Aura sin tener que comprar nada.

### 9.4 Valor (Valor) — nivel 8

| Habilidad | Juramento | Enfriamiento | Prob. golpe de suerte | Qué hace |
|---|---|---|---|---|
| **Shield Charge** | Juggernaut | **10 s** | 35 % | **Canalizada.** Cargas con el escudo empujando enemigos; **+armadura** mientras canalizas. Coste: **Fe + 1 por segundo** |
| **Aegis** | Juggernaut | **20 s** | — | Escudos de Luz: **provoca** a los cercanos, **+prob. de bloqueo y +armadura**. 3.1.0 le añadió **+30 % de armadura** |
| **Falling Star** | Disciple | **12 s** | 26 % | Alas angelicales: subes y te lanzas; daño al despegar y al aterrizar |
| **Rally** | Zealot | **16 s**, **3 cargas** | — | **Cuesta 35 % de vida.** Genera **15 + rango** de Fe y **+15 % de velocidad de movimiento** |

Enfriamientos y cargas: https://www.icy-veins.com/d4/guides/paladin-skills/ · costes y efectos: datamining · el buff de Aegis: *"Aegis: Now also grants 30% Armor while active."* (3.1.0) — https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes

### 9.5 Justicia (Justice) — nivel 13

| Habilidad | Juramento | Enfriamiento | Prob. golpe de suerte | Qué hace |
|---|---|---|---|---|
| **Purify** | Judicator | **12 s** | — | Envuelve en Luz a los enemigos: los **aturde (Daze)** |
| **Consecration** | Judicator | **18 s** | 12 % | Zona sagrada: **te cura a ti y a tus aliados** por % de vida máxima por segundo y daña a los enemigos |
| **Condemn** | Disciple | **15 s** | 26 % | **Atrae a los enemigos**, los aturde brevemente y hace daño. Mientras lo lanzas eres **Imparable (Unhindered)** |
| **Spear of the Heavens** | Judicator | **14 s** | 33 % | Llueven **4 lanzas** celestiales que **derriban**; a los 1,5 s **estallan** |

Fuente: https://www.icy-veins.com/d4/guides/paladin-skills/ · detalles: datamining

### 9.6 Definitivas (Ultimate) — nivel 19

**Solo puedes llevar una:** *"Only one can be chosen"* — https://maxroll.gg/d4/resources/paladin-class-overview.

| Habilidad | Juramento | Enfriamiento | Qué hace |
|---|---|---|---|
| **Heaven's Fury** | Judicator | **30 s** | Agarra la Luz, daña alrededor cada segundo y luego la suelta a buscar enemigos durante **7 s** |
| **Fortress** | Juggernaut | **60 s** | **Te vuelves INMUNE** unos segundos y creas una zona defensiva; dentro, tú y tus aliados ganáis **acumulaciones de Resolve cada 0,5 s** |
| **Zenith** | Zealot* | **25 s** | Espada divina que corta el campo; **al relanzarla** vuelve a cortar y **derriba** |
| **Arbiter of Justice** | Disciple* | **120 s** | **Asciende y te transformas en Arbiter** durante ~20 s (escala con rango), con daño al aterrizar |

Enfriamientos: https://www.icy-veins.com/d4/guides/paladin-skills/
\* Icy Veins **deja el campo «Oath Type» vacío** para Zenith y Arbiter of Justice. Lo relleno con el datamining: Zenith lleva `Skill_Zealot`, Arbiter of Justice lleva `Skill_Disciple`. Lo señalo por transparencia: **ese par de casillas concretas son datamining, no fuente redactada.**

### 9.7 Habilidad de desmontar (Dismount Skill)

*"While mounted, the Paladin class has access to a unique Dismount Skill which causes them to jump off the mount, soaring through the air at a location where they land and dealing damage. Players that are struck by an enemy are automatically dismounted and are unable to use their Dismount Skill."* — https://www.icy-veins.com/d4/guides/paladin-skills/

No está en el árbol, no consume puntos.

---

## 10. EL ÁRBOL COMPLETO, HABILIDAD POR HABILIDAD, CON NIVELES

Todo esto es **datamining de `data.min.json` 3.1.0.72698** (ver §0.3). Es el mapa más completo del árbol del Paladín que he podido reconstruir; **no existe equivalente publicado en ninguna web que haya podido abrir.** Formato: `nivel → contenido`.

### 10.1 Básicas (clúster nivel 1)

| Habilidad | nv. 5 (2 modif.) | nv. 9 (2 modif.) | nv. 14 (variante, elige 1) |
|---|---|---|---|
| **Clash** | Faith Generation (5 rangos) · Resolve (5) | Crusader's March Effectiveness (5) · Damage Increase (5) | Punishment (3) · Skirmish (3) · **Seize Them (3, nv. 30)** |
| **Holy Bolt** | Faith Generation (5) · Judgement (5) | Cast Speed (5) · Slow (5) | Divine Bolt (5) · Ricocheting Bolt (5) · **Storm Bolt (5, nv. 30)** |
| **Brandish** | Damage Increase (3) · Faith Generation (3) | Cast Speed (3) · Vulnerable (3) | Cross Strike (3) · Sword of Mastery (3) · **Returning Light (3, nv. 30)** |
| **Advance** | Critical Strike Chance (5) · Weaken (5) | Fortify (5) · Unhindered (5) | Vanguard's Rush (3) · Wave Dash (3) · **Flash of the Blade (3, nv. 30)** |

### 10.2 Fundamentales (clúster nivel 3)

| Habilidad | nv. 6 | nv. 10 | nv. 15 (variante) |
|---|---|---|---|
| **Blessed Hammer** | Cost Reduction (3) · Damage Bonus (3) | Cast Speed (3) · Slow (3) | Disciple's Halo (3) · Shattering Blow (3) · **Mortar Combat (3, nv. 32)** |
| **Zeal** | Additional Strikes (3) · Fortify (3) | Critical Strike Chance (3) · Weaken (3) | Death or Glory (3) · Zealot's Legacy (3) · **Cull the Wicked (3, nv. 32)** |
| **Blessed Shield** | Armor and Block Chance Bonus (3) · Damage Bonus (3) | Cast Speed (3) · Faith Generation (3) | Shield of Justice (3) · Shield of the Revenant (3) · **Shield of Retribution (3, nv. 32)** |
| **Shield Bash** | Hits Are Blocks (5) · Size Bonus (5) | Damage Bonus (5) · Distance (5) | Lay Siege (5) · Smite (5) · **Breach (5, nv. 32)** |
| **Divine Lance** | Cast Speed (5) · Stacking Damage (5) | Cost Reduction (5) · Damage Bonus (5) | Tip of the Spear (5) · Zealous Joust (5) · **Divine Javelin (5, nv. 32)** |

### 10.3 Auras (clúster nivel 4)

| Habilidad | nv. 7 | nv. 11 | nv. 16 (variante) |
|---|---|---|---|
| **Defiance Aura** | Maximum Life (3) · Unstoppable (3) | Bonus Healing (3) · Potency (3) | Rite of Might (3) · Rite of Prayer (3) · **Rite of Thorns (3, nv. 34)** |
| **Holy Light Aura** | Additional Bounce (3) · Additional Targets (3) | Judgement Damage Bonus (3) · Potency (3) | Rite of Judgement (3) · Rite of Mercy (3) · **Rite of Submission (3, nv. 34)** |
| **Fanaticism Aura** | Additional Maximum Resource (3) · Extra Passive Stack (3) | Potency (3) · Resource Generation (3) | Rite of Humility (3) · Rite of Vengeance (3) · **Rite of Redemption (3, nv. 34)** |

### 10.4 Valor (clúster nivel 8)

| Habilidad | nv. 12 | nv. 17 | nv. 20 (variante) |
|---|---|---|---|
| **Shield Charge** | Damage Bonus (3) · **Resolve (3)** | **Hit Count As Blocking (3)** · **Retribution (3)** | Relentless Charge (3) · Virtuous Charge (3) · **Phalanx Charge (3, nv. 36)** |
| **Aegis** | Cooldown Reduction (3) · Unstoppable (3) | Block Damage Reduction (3) · Duration (3) | Faith Is My Shield (3) · Stay Resolute (3) · **Impunity (3, nv. 36)** |
| **Falling Star** | Additional Charge (3) · Vulnerable (3) | Cooldown Reduction (3) · Damage (3) | Fanatic Descent (3) · Starfall (3) · **Faster Than Light (3, nv. 36)** |
| **Rally** | Critical Strike Chance (3) · Duration Bonus (3) | Cost Reduction (3) · Unhindered and Movement Speed (3) | Words of Inspiration (3) · Words of Rejuvenation (3) · **Words of Sacrifice (3, nv. 36)** |

**Las tres variantes de Shield Charge, en texto del juego (datamining):**
- **Relentless Charge:** *"Shield Charge becomes a **Core** Skill that deals X damage. Shield Charge now costs **20 Faith** to Cast and an additional **1 Faith per second**."*
- **Virtuous Charge:** *"Shield Charge becomes a **Judicator** Skill and consumes Judgement on impact, increasing the ending nova damage by **20 %[+]** for each Judgement consumed **up to 100 %**. When Shield Charge ends you release a Holy nova, dealing X damage and Stunning enemies."*
- **Phalanx Charge** (nv. 36): *"Shield Charge surges forward in a wave of energy and Knocks enemies Back, dealing X damage."*

### 10.5 Justicia (clúster nivel 13)

| Habilidad | nv. 18 | nv. 21 | nv. 23 (variante) |
|---|---|---|---|
| **Consecration** | Duration (3) · Weaken (3) | Fortify (3) · Resource Generation (3) | Bastion (3) · Hallowed Ground (3) · **Sanctify (3, nv. 38)** |
| **Condemn** | Cooldown Reduction (3) · Weaken (3) | Movement Speed (3) · Size Increase (3) | Atonement (3) · Gather the Guilty (3) · **Shepherd the Flock (3, nv. 38)** |
| **Spear of the Heavens** | Cooldown Reduction (3) · Judgement Damage Bonus (3) | Projectiles (3) · Vulnerable (3) | Part the Heavens (3) · Pronouncement of Heaven (3) · **Fist of the Heavens (3, nv. 38)** |
| **Purify** | Cooldown Reduction (3) · Faith Generation (3) | Echo (3) · Size Bonus (3) | Sentence (3) · Surrender (3) · **Absolution (3, nv. 38)** |

### 10.6 Definitivas (clúster nivel 19)

| Habilidad | nv. 22 | nv. 24 | nv. 25 (variante) |
|---|---|---|---|
| **Heaven's Fury** | Damage Bonus (3) · Judgement (3) | Duration (3) · Slow (3) | Triplicate (3) · Walk With The Light (3) · **Final Justice (3, nv. 40)** |
| **Zenith** | Unstoppable (3) · Weaken (3) | Critical Strike Chance (3) · Weaken (3) | Empyrean Edge (3) · Sermon of Steel (3) · **Sunder (3, nv. 40)** |
| **Fortress** | Free Cast (3) · Unstoppable (3) | Duration (3) · **Resolve Damage Bonus (3)** | Barricade (3) · Entrench (3) · **Rampart of Thorns (3, nv. 40)** |
| **Arbiter of Justice** | Cooldown Reduction (3) · Wing Strike Recast (3) | Duration (3) · Movement Speed (3) | Reach of the Law (3) · Seraph's Wings (3) · **Divine Intervention (3, nv. 40)** |

---

## 11. PUNTOS DE HABILIDAD TOTALES A NIVEL 70

| Origen | Puntos | Fuente |
|---|---|---|
| Subir de nivel (2 → 70) | **69** | *"69 skill points are gained by leveling"* — https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/ · **corroborado por datamining**, tooltip del atributo «Level»: *"Each Level grants a Skill Point **until Level 70**. Afterwards, each Paragon Level grants a Paragon Point until Paragon Level 300."* |
| Rango de Temporada (Season Rank) / Renombre (Renown) | **14** | *"14 skill points are locked behind the Season Rank System or Renown"* — https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/ · *"up to 14 extra skill points for a total of 83"* — https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide |
| **TOTAL** | **83** | Corroborado por Blizzard: *"up to 83 available Skill Points"* (citado en https://www.icy-veins.com/d4/news/diablo-iv-lord-of-hatred-full-blog-post-now-available/) |

Los puntos del Rango de Temporada **no abren clústeres**: *"Skill points from the Season Rank System or Renown do not affect Skill Tree progress and can be allocated to skill ranks you already unlocked."* — https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/

> ⚠️ **Cifra rival (dato caducado, no la uses):** https://maxroll.gg/d4/getting-started/skill-trees dice **"12 additional skill points through the Season Rank system"** y una escalera que sale a **80**. Esa página está fechada el **26 de abril de 2026 — dos días ANTES del rework 3.0**. Las páginas de junio-julio de 2026 dicen 69 + 14 = 83, que además cuadra con el «up to 83» oficial. (Este conflicto ya estaba documentado en `investigacion/crudo/arbol-estructura.md`; lo repito porque la misma página es la que uso para la escalera de clústeres, y quiero que sepas que **de esa página me creo la escalera 1/3/4/8/13/19 pero NO el total de puntos**.)

**Aritmética que te importa:** 83 puntos. Maximizar UNA habilidad entera = 30 puntos (§8). Con 6 habilidades en la barra y las auras, **vas a ir cortísimo**. Nadie llega a rango 15 en todo.

---

## 12. QUÉ LA HACE FUERTE Y QUÉ LA HACE FRÁGIL

### 12.1 Lo que dicen las fuentes, literal

**Maxroll** (https://maxroll.gg/d4/resources/paladin-class-overview, act. 14/07/2026, T14) lo pone en dos listas:

| Fortalezas | Debilidades |
|---|---|
| *"Very Fast"* | *"Usually Melee"* |
| *"Super Tanky"* | *"Cooldown Based"* |
| *"Support Capabilities"* | *"Not Very Flexible"* |

**Icy Veins**, para la build de Zealot (https://www.icy-veins.com/d4/guides/zealot-paladin-build/, act. 25/06/2026, T14):

| Fortalezas | Debilidades |
|---|---|
| *"Fast, rapid attacks"* | *"Uses health as a resource"* |
| *"Powerful defensive utility and survivability"* | *"Slower pace in low gear"* |
| *"Large AoE sweeps"* | *"Weaker single target damage"* |

### 12.2 Lectura para un principiante

**Fuerte porque:**
- **Aguanta.** Escudo + Defiance Aura (**+50 % armadura y +50 % resistencias**, verificado en notas 3.1.0) + Fortress (**inmunidad**) + Aegis (bloqueo, armadura y provocación). Un principiante muere mucho menos con esto que con un Nigromante sin equipo.
- **Bloquear es ofensivo.** El keyword **Retribution** convierte bloqueos en explosiones de Espinas. Es una clase donde la defensa **es** el daño.
- **Es la mejor clase de apoyo del juego según Maxroll** (*"bringing lots of support tools to any party"*). En dúo esto no es un detalle: las tres Auras dicen explícitamente *"and your allies"*.
- **Es rápida.** Shield Charge, Shield Bash, Advance, Falling Star, Divine Lance y Rally llevan todas etiqueta de movilidad o velocidad. No es un tanque lento.

**Frágil porque:**
- **Es cuerpo a cuerpo.** *"Usually Melee"*. Tienes que estar dentro del montón. Con Nigromante estabas detrás.
- **Vive de los enfriamientos.** *"Cooldown Based"*. Si tus botones están en enfriamiento, no tienes plan B. Fortress: **60 s**. Arbiter of Justice: **120 s**.
- **Poco flexible.** *"Not Very Flexible"*: el Juramento y las etiquetas encierran cada habilidad en un arquetipo. No puedes mezclar libremente Zealot con Judicator sin perder la mitad del escalado.
- **Arranca floja.** *"Slower pace in low gear"* (Icy Veins). Las primeras horas sin objetos se hacen lentas.
- **Daño a objetivo único mediocre** en varias builds (*"Weaker single target damage"*), lo que se nota contra jefes.

### 12.3 Nota de honestidad sobre el «ranking»

No te doy ranking de daño. **He abierto una sola lista de tiers de Paladín de fuente preferente**: https://maxroll.gg/d4/tierlists/paladin-endgame-tier-list (act. **22/07/2026**, T14). Dice esto:

| Tier | Builds |
|---|---|
| **A** | **Shield Charge Paladin** (añadida a la lista el 20/07/2026) |
| **B** | Divine Lance · Clash · Shield of Retribution · Blessed Hammer |
| **C** | Zeal · Wing Strikes · Brandish · Auradin · Shield Bash |
| **D** | Zenith · Judgement |

**Ahí no hay tier S para el Paladín, y Shield Charge es lo más alto de la clase.** Extractos de buscador me ofrecían un ranking distinto («Auradin y Arbiter en S», «Wing Strike es la mejor») **procedente de páginas que no he abierto**. No lo reproduzco. Si algún otro asistente te da un ranking, pídele la URL que abrió.

---

## 13. CÓMO SE SIENTE FRENTE A OTRAS CLASES (y frente a tu Nigromante)

| Eje | Nigromante (lo que ya conoces) | Paladín |
|---|---|---|
| **Posición** | Detrás; los esbirros hacen de muro | **Dentro del montón**, tú eres el muro |
| **Recurso** | Esencia + cadáveres (dos economías) | **Solo Fe** (una economía) |
| **Mecánica de clase** | **Libro de los Muertos**: muchos interruptores, se retoca sin parar | **Juramento**: **una elección de cuatro**, se hace a nivel 15 y se olvida |
| **Complejidad de rotación** | Media-alta (invocar, mantener, explotar cadáveres) | **Baja**. Auras puestas + una Fundamental que machacas |
| **Qué te mantiene vivo** | Que peguen a los esbirros | Armadura, bloqueo, Fortify, curación de aura |
| **Aporte al dúo** | Los esbirros distraen | **Auras que buffan directamente a tu pareja** |
| **Punto de dolor** | Sin equipo, te evaporas | Sin equipo, **haces poco daño** pero no te mueres |

**Cita que resume el arquetipo:** *"The defining characteristics of the Paladin are their access to shields and heavenly empowered abilities. They carry Auras that buff themselves and allies while going sword-and-board with their foes."* — https://maxroll.gg/d4/resources/paladin-class-overview

**Sobre la dificultad de la rotación** (tu requisito de «daño alto sin rotaciones imposibles»): Icy Veins describe la build de Zealot como *"moderately complex but emphasizes repetitive action rather than intricate sequencing"* — https://www.icy-veins.com/d4/guides/zealot-paladin-build/. Traducido: **es machacar, no coreografía**. Y Maxroll añade sobre el propio Juramento que *"specific skills or setups clearly synergize with one of the Oaths"* — o sea, **la elección se hace sola**. Ambas cosas apuntan a que sí, es apta para principiante.

---

## 14. ⚠️ TRAMPAS DE DATOS MUERTOS QUE HE ENCONTRADO — LEE ESTA SECCIÓN

Cinco fuentes que **parecen buenas y no lo son** para la clase Paladín en el parche 3.1.3:

| Fuente | Por qué parece buena | Por qué NO vale | Prueba |
|---|---|---|---|
| **La guía de SUBIDA de nivel de Shield Charge de Maxroll** — https://maxroll.gg/d4/build-guides/shield-charge-paladin-leveling-guide | Es de Maxroll, es de Shield Charge, es lo que buscas | **Está ARCHIVADA desde antes de que saliera la expansión.** Habla de *"2 points into Basic Skills to unlock the other sections"*, de que Shield Charge llega *"at level 21"* tras *"20 skill points"* y de repartir puntos *"through level 60"*. **Todo eso es el modelo pre-3.0.** | Descargué el HTML (HTTP 200, 464 533 bytes). Contiene: `"dateModified":"2026-04-24"`, etiqueta `Season 12 - Slaughter`, y en el changelog, literal: **«Build archived prior to Lord of Hatred release until a post-release update is available.»** |
| **La guía ENDGAME de Shield Charge** — https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide | — | **Esta SÍ vale.** Última actualización **25/07/2026**, T14 - Death Awakening | Fetch de la página |
| **Wowhead, guía de clase Paladín** — https://www.wowhead.com/diablo-4/guide/classes/paladin/overview | Es Wowhead, está en tus preferentes | Actualizada el **11/03/2026** → **Temporada 12, pre-rework**. Además, cuando la abro solo devuelve navegación, no contenido | Fetch: *"an update date of 2026/03/11"* |
| **maxroll.gg/d4/getting-started/skill-trees** | Es la referencia del árbol | Fechada **26/04/2026, dos días antes del rework**. **La escalera de clústeres 1/3/4/8/13/19 sí concuerda con el juego vivo** (lo verifiqué con el datamining), pero su **total de puntos (80) y su cifra de Rango de Temporada (12) están caducados** | Fetch: *"Last Updated: April 26, 2026"* |
| **La página de resumen de clase de Maxroll** — https://maxroll.gg/d4/resources/paladin-class-overview | Es la mejor fuente redactada que hay | **Está bien**, pero fíjate: sigue **etiquetada «Season 11 - Divine Intervention»** aunque su changelog dice *"July 14, 2026 — Updated for Season 14"*. Y contiene el error de atribuir el Paladín a Vessel of Hatred (§2) | HTML descargado (321 254 bytes) |

**Regla práctica para ti:** para el Paladín, **cualquier página fechada antes del 28/04/2026 describe un árbol que no existe**. Y ojo con las guías de *leveling*, que se actualizan mucho menos que las de *endgame*.

---

## 15. LO QUE ESTO SIGNIFICA PARA TU PARTIDA CONCRETA

1. **Hasta el nivel 15 no eliges nada importante.** Sube tranquilo, prueba habilidades, reasigna gratis. El Juramento llega al 15.
2. **Si vas a Shield Charge, tu Juramento es Juggernaut.** La habilidad lleva la etiqueta `Skill_Juggernaut` (datamining) y la guía de Maxroll la construye sobre Resolve, que es el recurso del Juramento Juggernaut — https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide.
3. **Shield Charge la tienes a nivel 8, pero la build no existe de verdad hasta el 20** (variante) y no está completa hasta el **36** (Phalanx Charge). No te frustres entre el 8 y el 20.
4. **Pon Defiance Aura pronto.** Se abre a **nivel 4**, te da **+50 % armadura y +50 % resistencias**, y **también a tu pareja**. Es probablemente el mejor punto por euro de todo tu árbol temprano.
5. **En dúo, tú eres el soporte además del tanque.** Recuerda lo que ya sabéis del proyecto: en grupo el mercenario **Contratado no aparece, solo el Refuerzo**. Tu compañera nigromante sin expansiones **no puede usar Paladín ni Brujo**, pero **sí recibe tus auras**.
6. **No intentes maximizar seis habilidades.** 83 puntos, 30 por habilidad completa. Elige dos o tres y acepta migajas en el resto.
7. **Cuidado con Zeal y Rally si eres principiante:** cuestan **vida**, no Fe.

---

## 16. NOMBRES EN ESPAÑOL — lo que hay y lo que no

**Confirmado en español oficial** (https://diablo4.blizzard.com/es-es/lord-of-hatred):

| Inglés | Español oficial |
|---|---|
| Paladin | **Paladín** |
| The Arbiter | **El árbitro** — *"Canaliza la forma más pura de la Luz para ascender a una forma angelical"* |
| The Zealot | **El zelote** — *"Impulsa tu fe a través de una furia implacable"* |
| The Judicator | **El judicante** — *"Que el castigo divino llueva desde los cielos"* |
| The Juggernaut | **El juggernaut** — *"Conviértete en la encarnación de la templanza sagrada"* |
| Wardens of Light | **Guardianes de la Luz** |

**Traducciones de trabajo mías** (NO oficiales, las marco como tales): Fe (Faith), Juramentos (Oaths), Habilidades Básicas / Fundamentales / de Aura / de Valor / de Justicia / Definitivas.

**NO he encontrado los nombres en español de las 24 habilidades.** Ni la web oficial en español, ni el artículo de Xbox Wire en español (https://news.xbox.com/es-latam/2025/12/16/guiado-por-la-luz-el-paladin-se-une-a-diablo-iv/, 16/12/2025 — que **deja los nombres en inglés**: *"Blessed Hammer, Blessed Shield, Condemn, Zeal y Heaven's Fury"*), ni el fichero de datos de Maxroll (que solo sirve inglés) los publican. **La pantalla del juego manda:** si abres el árbol en español, los nombres que veas son los buenos.

---

## 17. Fuentes

**Abiertas de verdad y usadas para datos de este documento:**

*Oficiales (Blizzard):*
1. https://diablo4.blizzard.com/en-us/lord-of-hatred — «TWO NEW CLASSES»; las cuatro especializaciones del Paladín
2. https://diablo4.blizzard.com/es-es/lord-of-hatred — nombres en español: Paladín, El árbitro, El zelote, El judicante, El juggernaut
3. https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes — notas de parche; confirma 3.1.3 build 73224 (12/08/2026) y los valores de los cuatro Juramentos tras 3.1.0
4. https://news.blizzard.com/en-us/article/24247511/stand-against-mephisto-pre-purchase-lord-of-hatred — acceso anticipado al Paladín; lanzamiento 28/04/2026
5. https://news.blizzard.com/en-us/article/24244399/wield-divine-might-as-the-paladin — artículo de presentación del Paladín (⚠️ contiene el «17 %» de Zealot ya caducado)
6. https://news.xbox.com/es-latam/2025/12/16/guiado-por-la-luz-el-paladin-se-une-a-diablo-iv/ — 16/12/2025, en español

*Maxroll (preferente):*
7. https://maxroll.gg/d4/resources/paladin-class-overview — act. **14/07/2026**, T14. Identidad, Fe, Juramentos, palabras clave, atributos, equipo, fortalezas/debilidades. (Descargada además por curl: 321 254 bytes)
8. https://maxroll.gg/d4/getting-started/skill-trees — act. **26/04/2026**. Escalera de clústeres 1/3/4/8/13/19 y rango máximo 15 (⚠️ su total de puntos está caducado)
9. https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide — act. **25/07/2026**, T14. Juggernaut, Resolve máx. 30, Retribution como mecánica de daño
10. https://maxroll.gg/d4/build-guides/shield-charge-paladin-leveling-guide — ⚠️ **ARCHIVADA**, `dateModified 2026-04-24`, Temporada 12. Usada solo como prueba de dato muerto (curl: HTTP 200, 464 533 bytes)
11. https://maxroll.gg/d4/build-guides/paladin — act. **09/08/2026**, T14. Catálogo de builds del Paladín
12. https://maxroll.gg/d4/tierlists/paladin-endgame-tier-list — act. **22/07/2026**, T14. Tiers de Paladín

*Icy Veins (preferente):*
13. https://www.icy-veins.com/d4/guides/paladin-skills/ — act. **29/06/2026**, T14. Las 24 habilidades, tipo de Juramento, costes de Fe, enfriamientos, habilidad de desmontar (⚠️ su «50 %» de Disciple está caducado). Descargada por curl: 237 032 bytes
14. https://www.icy-veins.com/d4/guides/paladin-leveling-guide/ — act. **29/06/2026**, T14. Juramento a nivel 15; dificultad recomendada «Hard»
15. https://www.icy-veins.com/d4/guides/zealot-paladin-build/ — act. **25/06/2026**, T14. Fortalezas/debilidades; complejidad de rotación
16. https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/ — 69 + 14 = 83 puntos (vía documentos previos del proyecto)
17. https://www.icy-veins.com/d4/news/diablo-iv-lord-of-hatred-full-blog-post-now-available/ — «up to 83 available Skill Points» (vía documentos previos del proyecto)

*Otras:*
18. https://d4guides.gg/en/s14/database/classes/paladin — corrobora el reparto **4/5/3/4/4/4** habilidades por categoría (⚠️ **dice que el recurso del Paladín es «Resolve». Es INCORRECTO**: el recurso es Fe; Resolve es una acumulación del Juramento Juggernaut. No uses esa página para el recurso.)
19. https://www.wowhead.com/diablo-4/guide/classes/paladin/overview — ⚠️ **11/03/2026, Temporada 12, pre-rework.** Abierta y descartada.

*Datamining (declarado como tal):*
20. **https://assets-ng.maxroll.gg/d4-tools/game/data.min.json** — HTTP 200, **11 606 292 bytes**, descargado **24/08/2026**. Campo `version`: **`3.1.0.72698`** ⚠️ (parche 3.1.0, build 72698 — **tres parches por detrás del vivo 3.1.3/73224**). De aquí salen: `classes["6"]` (Paladín), `uiStrings.resourceType["9"] = "Faith"`, `skillTrees["Paladin_NEW"]` (270 nodos, 6 raíces con `requiredLevel` 1/3/4/8/13/19), las 24 entradas de habilidad con sus etiquetas y modificadores, las cuatro entradas `Paladin_Oath_*`, la tabla de escalado por rango `powerTables[37]`, y los tooltips de `heroDetails` sobre Fe y Retribution.

**No abiertas / bloqueadas (declaradas):**
- https://maxroll.gg/d4/getting-started/paladin-guide — **HTTP 404**, no existe
- https://mobalytics.gg/diablo-4/guides/patch-3-1-3-changes-and-fixes — **HTTP 403**
- https://maxroll.gg/d4/tierlists/solo-tier-list — **HTTP 404**
- Vetadas por encargo y no consultadas: fextralife, primagames, beebom, gamespot, segmentnext, studioloot, gamerguides, pcgamesn, mythicdrop
- **Nota:** Maxroll **no** me devolvió 403 esta vez; todas sus páginas se abrieron con normalidad (fetch y curl).

---

## 18. No encontrado

Cosas que un informe descuidado rellenaría a ojo y que **aquí quedan como hueco declarado**:

1. **Los niveles de clúster del Paladín NO están escritos en ninguna guía web.** Los doy desde el datamining (§7.1) porque encajan al milímetro con la escalera genérica de Maxroll y con el patrón ya verificado del Nigromante, pero **no tengo una frase redactada que diga «las Auras del Paladín se abren a nivel 4»**. Si esto es crítico, se comprueba en 30 segundos abriendo el árbol en la partida.
2. **El valor máximo de Fe.** No aparece en Maxroll, ni en Icy Veins, ni como número plano en el fichero de datos.
3. **Si se puede cambiar de Juramento, y a qué coste.** Un extracto de buscador decía «Respec is free — swap Oaths freely» pero **no pude abrir la página que lo sostiene**. Ninguna fuente preferente lo dice. **Compruébalo en la pantalla del Juramento.**
4. **Los nombres en español de las 24 habilidades.** Ninguna fuente oficial ni comunitaria los publica; el fichero de datos solo trae inglés.
5. **Los valores de daño base (% de daño de arma) de cada habilidad.** El fichero de datos los guarda como fórmulas sin resolver (`[{payload:...}|2?|]`) y no como números. **No los invento.** Icy Veins da algunos porcentajes de modificadores concretos, pero no una tabla comparable de daño base.
6. **El valor exacto de Fe máxima que añade el modificador «Additional Maximum Resource» de Fanaticism Aura.** Igual que arriba: fórmula sin resolver.
7. **La probabilidad base de Retribution y el % de Espinas que libera.** El tooltip existe (*"you have a chance to release a nova dealing {X} of your Thorns damage"*) pero los valores son variables de personaje.
8. **Qué es exactamente «Wing Strikes».** Aparece en el texto del Juramento Disciple (*"Wing Strikes gain Disciple Skill benefits"*), como modificador de Arbiter of Justice (*"Wing Strike Recast"*) y como build en Maxroll e Icy Veins, pero **no es una de las 24 habilidades del árbol** y no he encontrado una definición redactada. Mi lectura —**no confirmada**— es que son los ataques que haces mientras estás en forma Arbiter. Lo dejo como hueco.
9. **Ranking de daño entre builds de Paladín.** Solo reproduzco la lista de tiers de Maxroll que abrí (§12.3). Los rankings alternativos que vi en extractos de buscador **no los reproduzco porque no abrí esas páginas**.
10. **Si el Paladín tiene misión de desbloqueo de clase o de Juramento.** Hay indicios de un contenido «Call of the Paladin / Path of the Paladin» de la Temporada 11, pero es de diciembre de 2025 y no consta que siga vigente ni que sea necesario. No lo afirmo.
11. **Diferencias entre el datamining 3.1.0 (build 72698) y el parche vivo 3.1.3 (build 73224).** El parche 3.1.3 incluye correcciones a habilidades del Paladín (descripciones aditivo/multiplicativo, daño de eco del Juramento Zealot, Brandish y Vulnerable, tipo de daño de Phalanx Charge, entre otras) según extractos de buscador de Mobalytics **que no pude abrir (HTTP 403)**, y las notas oficiales que sí abrí no listan cambios de clase de Paladín en 3.1.3. **No puedo garantizar que ningún valor numérico de §4, §9 y §10 haya sido tocado en 3.1.1 / 3.1.2 / 3.1.3.** Lo estructural (clústeres, niveles, nombres, etiquetas, árbol) no lo toca un hotfix y lo doy por firme.
