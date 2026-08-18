---
titulo: Subida 1 → 70
capa: version
parche: "3.1.3"
temporada: 14
estado: vivo
entitlement: base
verificado: 2026-08-19
revisar_despues: 2026-10-15
---

## La buena noticia: la subida entera es vuestra

**La ruta de subida de esbirros no toca ni un solo nodo de expansión**, comprobada nodo a nodo contra el fichero de datos del juego. Lo que os falta duele en el endgame, no aquí.

::: evidencia nivel=oficial fuentes=blizzard-loh-page
El rework del árbol del parche 3.0, las variantes de habilidad nuevas, la subida de nivel máximo y el Filtro de Botín (*Loot Filter*) están dentro del apartado oficial de Blizzard «Major Updates for all Diablo IV Players»: *«Major Skill Tree reworks including new skill variants for every class, along with level cap increases»*. Todo eso es ✅ juego base.
:::

::: evidencia nivel=corroborado fuentes=maxroll-skill-trees,icyveins-summoner,conquestcapped
El nivel máximo es **70**. La página oficial dice «level cap increases» sin dar el número; el 70 lo confirman tres fuentes independientes fechadas dentro de la Temporada 14. Si leéis «el rush a 60», esa guía es de la Temporada 12 o anterior.
:::

Todo ✅: árbol de habilidades, Libro de los Muertos (*Book of the Dead*), Helltides, Árbol de los Susurros (*Tree of Whispers*), Bastiones (*Strongholds*), Mazmorras de Pesadilla, Rupturas del Pandemónium, Rango de Temporada (*Season Rank*), Filtro de Botín y Paragón.

No tenéis, y sobre ello se apoya casi toda guía pública: Planes de Guerra (*War Plans*), Skovos, Talismanes y la tercera variante de cada habilidad 🔒 *Lord of Hatred*; Ciudad Subterránea de Kurast, Mercenarios y Runas 🔒 *Vessel of Hatred*.

::: aviso tipo=peligro
Cuando una guía diga «id a ver a Tyrael a Temis y montad un War Plan», cerradla. Ese es el motor de XP de la meta pública de esta temporada y es contenido de *Lord of Hatred*: sin la expansión no podéis ni viajar allí. No hay nada que comprobar en el juego.
:::

## Estacional, y sin SSF

Personaje **estacional**. El Renombre (*Renown*) sigue vivo en el Reino Eterno; en temporada lo sustituyó el Rango de Temporada, de donde salen los puntos extra de habilidad. No farmeéis Renombre en temporada: no sirve para nada.

::: aviso tipo=peligro
**No marquéis Solo Self-Found (SSF)**: es permanente para esa temporada e impide agrupar y comerciar. Para un dúo es la peor casilla de la pantalla. «Saltar campaña» no os va a aparecer.
:::

## La campaña: no podéis saltarla

El salto solo existe si ya completasteis esa campaña en la cuenta. Vosotros no: el debate se acaba solo. Y es mejor así, porque completarla desbloquea el salto para todos vuestros personajes futuros y la dificultad Penitente (*Penitent*). Casi todo el consejo de internet sobre «saltar campaña» de esta temporada habla de la campaña de *Lord of Hatred*, que ni siquiera es vuestra. Priorizad la **montura**: el Nigromante es la clase más lenta a pie.

::: evidencia nivel=sinconfirmar fuentes=nigro-leveling
Se afirma que el estado del mundo y el progreso de campaña en grupo son los del **líder de la partida**: el que no lidera no avanzaría su propia campaña. No está atribuido a fuente fechada. Comprobadlo en el diario del que no lleva el grupo; mientras tanto, id siempre en la misma misión y turnaos de líder.
:::

## Cómo funciona el árbol de habilidades

Antes de nada, el vocabulario. La pantalla del árbol tiene tres niveles de zoom y las guías los mezclan sin explicarlos:

- **Clúster.** Un grupo de habilidades del mismo tipo. El nigromante tiene **seis**: Básicas, Fundamentales, Cadáver, Macabras, Maldiciones y Definitivas. Se abren de uno en uno según subes de nivel.
- **Habilidad.** Lo que pones en la barra y pulsas. Cada una admite **15 rangos**: cada punto extra la hace un poco más fuerte.
- **Mejoras y variantes.** Colgando de cada habilidad hay cuatro nodos que se abren más tarde: dos parejas de **modificadores** (eliges uno de cada pareja) y luego las **variantes**, que la transforman. Las dos primeras variantes son tuyas ✅; **la tercera requiere expansión** 🔒.

Y lo que rompe casi todas las guías que vas a encontrar:

**Todo eso se abre por tu NIVEL de personaje, no por cuántos puntos hayas gastado.**

::: diagrama nombre=arbol
:::

Busca tu nivel en la fila de arriba y baja la vista: eso es lo que tienes disponible ahora mismo.

### Lo que se lee de ahí

Los seis clústeres aparecen en los niveles **1 · 3 · 4 · 8 · 13 · 19**. Tus tres esbirros llegan pronto y en este orden: **Mago Esquelético** al 3, **Guerrero Esquelético** al 4, **Gólem** al 8. Las **Maldiciones** al 13, y el **Ejército de los Muertos** al 19.

**A partir del nivel 40 el árbol ya no abre nada más.** Los cincuenta niveles restantes son solo puntos para repartir en lo que ya tienes.

::: evidencia nivel=corroborado fuentes=datos-juego-3-1-0,maxroll-skill-trees,icyveins-necro-skills
El campo de requisito del árbol se llama literalmente `requiredLevel` en el fichero de datos del juego (versión 3.1.0.72698): 2.409 apariciones, y cero campos de «puntos gastados». Escalera completa por nivel:

| Clúster | Habilidad | Modif. A | Modif. B | Variantes 1 y 2 ✅ | 3.ª variante 🔒 |
|---|---:|---:|---:|---:|---:|
| Básicas (*Basic*) | 1 | 5 | 9 | 14 | 30 |
| Fundamentales (*Core*) | 3 | 6 | 10 | 15 | 32 |
| Cadáver (*Corpse*) | 4 | 7 | 11 | 16 | 34 |
| Macabras (*Macabre*) | 8 | 12 | 17 | 20 | 36 |
| Maldiciones (*Curse*) | 13 | 18 | 21 | 23 | 38 |
| Definitivas (*Ultimate*) | 19 | 22 | 24 | 25 | 40 |

Las pasivas ya no están en el árbol y la Pasiva Clave (*Key Passive*) fue eliminada; ese poder se movió a aspectos legendarios y únicos.
:::

::: aviso tipo=truco
**Consecuencia práctica que te ahorra disgustos: guardar puntos sin gastar no te retrasa nada.** Puedes subir tres niveles sin tocar el árbol y los clústeres se abren igual. Si no tienes claro dónde meter un punto, no lo metas.

Y hay **respec gratis**: reembolsar puntos y recolocarlos no cuesta nada mientras subes. No hay ninguna decisión irreversible en esta pantalla.
:::

::: aviso tipo=peligro
**Detector de guía muerta.** Si una guía dice nivel máximo **60**, **71 puntos** totales, **5 rangos** por habilidad, menciona la **Pasiva Clave**, habla de mejoras *Enhanced / Paranormal / Supernatural*, o dice que el Gólem se desbloquea a **nivel 25 con una misión** — es texto de 2023 o 2024. Ciérrala.

La fecha de la página no acredita nada: hay una guía de primera línea con sello de julio de 2026 que sigue diciendo 5 rangos.
:::

## El orden de gasto de puntos

Build: **Nigromante de esbirros** (*Minion Necro*), único S de la tier list de subida de esta temporada, cuyo criterio declarado incluye facilidad de juego y arranque sin recursos. Es también el que menos sufre por no tener Mercenario 🔒: ya lleváis un ejército de tanques.

::: evidencia nivel=unica fuentes=maxroll-skill-trees
*«Cada punto extra hace una habilidad un 10 % más potente de lo que era a rango 1… el primer punto que metes en una habilidad activa es diez veces más potente que los cuatro siguientes»*. Traducción: **amplitud primero, profundidad al final**.
:::

::: evidencia nivel=unica fuentes=planner-maxroll,datos-juego-3-1-0
Secuencia por puntos acumulados, decodificada de los ocho pasos del planificador oficial de la guía de esbirros de Maxroll (build del 22 jul 2026) contra el fichero de datos. **Es una sola fuente**: la ruta de Icy Veins está encerrada en JavaScript, y Mobalytics, Reddit y d4builds fueron inaccesibles.

| Puntos | Qué haces |
|---:|---|
| 3 | 3 rangos en **Segar** (*Reap*). Aparcamiento puro: hasta nivel 3 no hay otra cosa que pulsar |
| 4 | 🔄 **Respec gratis**: reembolsas Segar y metes 4 en **Mago Esquelético** |
| 7 | +1 **Tentáculos de Cadáver** (*Corpse Tendrils*), +1 **Guerrero Esquelético**, Modif. A de Mago, Modif. A de Guerrero (Mago baja a 3) |
| 12 | +1 **Gólem**, Gólem *Unstoppable*, Tendrils *Critical Strike Chance*, Modif. B de Mago, Modif. B de Guerrero |
| 18 | +1 **Doncella de Hierro** (*Iron Maiden*), Guerrero a 2, **✅ *Coven*** (+2 magos), **✅ *Master of Puppets*** (+3 guerreros), Tendrils *Vulnerable*, Modif. B de Gólem |
| 26 | +1 **Ejército de los Muertos** (*Army of the Dead*) con **✅ *Unyielding Commander***, *Cooldown Reduction*, *Corpse Generation*, **✅ Gólem *Gravebloom***, **✅ *Schadenfreude***, **Iron Maiden *Essence Generation*** (deja de costar Esencia y genera 5 por enemigo maldito), Guerrero a 3 |
| 40 | **Doncella de Hierro de 1 a 15.** Catorce puntos seguidos |
| 68 | Mago, Guerrero y Gólem hacia 15/15; Ejército de los Muertos a 6; se cambia Guerrero *Resolve* por *Vulnerable* |
:::

::: build nombre="Esbirros — ruta de subida" estado=arranque entitlement=base
Prioridad por clúster: **Fundamentales** (Mago Esquelético) → **Cadáver** (Guerrero Esquelético y Tentáculos de Cadáver) → **Macabras** (Gólem) → **Maldiciones** (Doncella de Hierro, que es vuestro motor de Esencia) → **Definitivas** (Ejército de los Muertos, **solo** por *Unyielding Commander*) → **Básicas**, ningún punto permanente.

Comprobada nodo a nodo: no usa ni una sola variante de expansión. Lo único que hay que ignorar de la guía original es la sección de Runas y la de Mercenarios.
:::

::: paso n=1 obligatorio=si entitlement=base
Al empezar, todos los puntos a **Segar** (*Reap*) hasta que se abra el clúster Fundamentales. No es inversión, es aparcamiento: lo vais a recuperar.
:::

::: paso n=2 obligatorio=si entitlement=base
En cuanto se abra Fundamentales, **reespecializad**: reembolsar es gratis y sin coste de oro. Sacad todo lo de Segar y metedlo en **Mago Esquelético**. Aquí empieza a existir el personaje.
:::

::: paso n=3 obligatorio=no entitlement=base
Hasta que tengáis el ejército montado, **un solo rango en casi todo** y el resto de puntos a abrir modificadores y variantes. Profundizar en Mago Esquelético antes de tener Gólem, *Coven* y *Master of Puppets* es la forma más común de tirar puntos en esta build.
:::

::: evidencia nivel=unica fuentes=planner-maxroll,datos-juego-3-1-0
Trampas ✅ disponibles para vosotros y malas para esta build: ***Service and Sacrifice*** hace que vuestros esqueletos pierdan el **25 %** de su Vida Máxima por segundo en combate · ***Gift of Death*** convierte al Mago en habilidad de Cadáver que exige un cadáver para invocar · ***Pile the Bodies*** enseña el número más grande de la pantalla pero escala una Definitiva de reutilización larga, mientras *Unyielding Commander* está activa casi siempre · ***Torture Artist*** cambia el tipo de daño a Sombra, puede invalidar vuestro equipo y arrastra un bug de respec reportado en el foro oficial y sin respuesta de Blizzard · **Decrepitud** (*Decrepify*) solo tiene sentido con *Unholy Frenzy* 🔒 y una Palabra rúnica 🔒, así que ese hueco es vuestro para otra cosa · y el **Ejército de los Muertos** termina a **6/15** mientras los esbirros van a **15/15**: no lo subáis más.
:::

## Franja por franja

::: evidencia nivel=unica fuentes=maxroll-dificultad
Bonus de experiencia: Normal es la base · **Difícil (*Hard*) +75 %**, disponible por defecto · **Experto (*Expert*) +125 %**, tras el prólogo · **Penitente (*Penitent*) +175 %**, al terminar la campaña base. Los doce escalones de Torment exigen nivel **70** y se abren limpiando pisos de El Foso (*The Pit*): Torment I con **Foso 10**. Todo el sistema de dificultades, los doce Torment incluidos, es ✅ juego base. Las penalizaciones de resistencia y armadura por Torment **ya no existen** desde la revisión defensiva de la Temporada 11.

| Franja | Dificultad | Qué hacéis |
|---|---|---|
| 1 → 15 | **Difícil** desde el minuto cero | Campaña Acto I. Helltides con objetivos de Susurro dentro. Línea estacional en Kyovashad para abrir las Rupturas |
| 15 → 40 | **Experto** tras el prólogo | Campaña, Susurros, Helltides. Eventos de mundo y Cofres Malditos. Mercader cada 10 niveles |
| 40 → 55 | **Penitente** al cerrar campaña | **Bastiones**: mucha XP por poco tiempo. Sin Planes de Guerra 🔒 son de lo poco masivo que tenéis; hacedlos antes de lo que dicen las guías |
| 55 → 70 | **Penitente** | Mazmorras de Pesadilla solo a Cofres Malditos y Santuarios, sin limpiarlas enteras. Helltides de fondo |
:::

::: aviso tipo=ojo
**No uséis Hordas Infernales para subir**: la única fuente que se moja dice que un ciclo de oleadas tarda varias veces más que una Helltide. Guardadlas para el nivel máximo. Y olvidad la Catedral de la Luz y las mazmorras capstone: el sistema de World Tiers ya no existe y no son requisito de nada.
:::

## Cuándo subir de dificultad

No es «la más alta que sobrevivís», es **la más alta en la que seguís matando rápido**. XP/hora = densidad × multiplicador × velocidad de limpieza: el multiplicador es solo uno de los factores.

::: evidencia nivel=unica fuentes=maxroll-dificultad
Cronometrad una limpieza en vuestra dificultad actual, subid un escalón y repetid. Si el tiempo sube **menos** que el porcentaje de XP que ganáis, el escalón nuevo es rentable. Con **+75 %** o **+125 %** hay margen de sobra; entre Torments consecutivos es minúsculo, porque pasar de **+900 %** a **+1000 %** es un **10 % relativo**, no un 100 %.
:::

Señal de bajar: morís repetidamente, o un jefe normal os lleva minutos. No hay orgullo en el escalón.

## El dúo: cómo no romperlo

::: evidencia nivel=unica fuentes=maxroll-experience
**+10 %** de XP por estar en el mismo grupo a menos de **90 metros** (unas tres pantallas) y **+5 %** por tener a alguien cerca sin agrupar. En mazmorras no hay límite de distancia y la XP se comparte con todos los del interior. Las hogueras (*Campfires*) suman hasta **+15 %** acumulable.
:::

::: evidencia nivel=sinconfirmar fuentes=nigro-leveling,dificultad
Se afirma que la vida de los monstruos escala con el número de jugadores en mazmorras pero no en mundo abierto, y que la densidad no aumenta nunca. De ser cierto, el mundo abierto y las Helltides serían desproporcionadamente rentables en dúo. **Puede ser información anterior al parche 2.0**: no se pudo fechar dentro de 3.1.x.
:::

- **Agrupados y cerca siempre.** El bonus de grupo es XP regalada y no cuesta nada.
- **Repartíos las maldiciones**: uno lleva Doncella de Hierro y el otro Decrepitud. Si vais iguales, se solapan del todo.
- **Diversificad aspectos** y comerciad duplicados. El cross-play PC/PS5 cubre toda la progresión y la campaña; lo que no cruza plataformas es el couch co-op.
- Dos nigromantes de esbirros llenan la pantalla: podéis permitiros **un escalón más de dificultad** del que os tocaría en solitario.

::: evidencia nivel=sinconfirmar fuentes=investigacion
No se sabe si ***Unyielding Commander*** se solapa entre dos nigromantes en dúo. Si vuestros dos ejércitos comparten la reducción de daño, uno de los dos podría gastar ese punto en otra cosa. **Probadlo**: es la comprobación con mejor relación coste/beneficio del capítulo.
:::

## El Libro de los Muertos durante la subida

::: evidencia nivel=corroborado fuentes=datos-juego-3-1-0,gamerant,icyveins-loh-news
El Libro ya no invoca nada: elige **qué tipo** es cada esbirro que invocáis desde el árbol, y aporta **2 mejoras y 1 sacrificio** por variante. Y el sacrificio ya no os quita el esbirro: reduce su cantidad o su daño en un **50 %**.
:::

::: evidencia nivel=disputa fuentes=captura-jugador,icyveins-necro-leveling,maxroll-minion-leveling,ezg
**El nivel de desbloqueo sigue abierto, pero el rango se ha estrechado.** Las fuentes daban tres respuestas: **5** (Icy Veins), **6** (ezg) y **15** (guía de esbirros de Maxroll, 30 jun 2026). La captura del jugador del 18 ago 2026, parche 3.1.3, muestra el Libro abierto y operativo **a nivel 8**, con variantes seleccionables. Eso mata el 15. Queda 5 contra 6, y solo se cierra en vuestra pantalla.
:::

::: evidencia nivel=oficial fuentes=captura-jugador
En esa misma captura, a nivel **8**, **el Sacrificio aparece bloqueado** con candado y texto «Para desbloquear…». Las mejoras, en cambio, se alternan libremente y sin coste observable: la misma variante aparece con Mejora 1 y con Mejora 2 activas. Durante la subida, probad sin miedo.
:::

::: evidencia nivel=oficial fuentes=captura-jugador
Texto real del juego en español. Defensores: base, **10 espinas**, y al recibir daño infligen el **50 %** de sus espinas a los enemigos cercanos; Mejora 1, provocan **6 s** al comandarlos; Mejora 2, **10 %** de formar un orbe de sangre al infligir daño. Gólem de Hueso: Mejora 1, comandarlo **crea 5 cadáveres**; Mejora 2, al recibir daño libera agujas de hueso **una vez cada 3 s**. Lo que publican las wikis generalistas para estas dos variantes está **refutado en pantalla**.
:::

::: evidencia nivel=unica fuentes=datos-juego-3-1-0
Los sacrificios de Guerreros y de Magos llevan una segunda línea que ninguna guía web menciona: **«Tu Gólem gana 60 %[x] de daño»**. Los de Gólem no la tienen. Sacrificar guerreros o magos convierte al Gólem en vuestro pilar de daño.
:::

**Magos de Sombra** es el único consenso de todas las fuentes. Para Guerreros y Gólem hay tres guías con tres respuestas distintas: elegid por lo que os falte, no por copiar.

## Llegáis al nivel máximo: el enganche

::: evidencia nivel=disputa fuentes=maxroll-skill-trees,blizzard-loh-blog,foro-blizzard
**El techo de puntos no está cerrado.** Maxroll dice **80**: un punto por nivel desde el 2 *«hasta el nivel 69»* (**68**) más *«12 puntos adicionales por el Rango de Temporada»*. Blizzard dice **«hasta 83»**, y esos **3** quedan sin explicar. Un usuario del foro oficial dice **81**, restando **2** de Renombre de Skovos 🔒. Planificad con **80**. Dato firme: los puntos del Rango de Temporada **no abren clústeres**, solo suben rangos ya desbloqueados.
:::

::: evidencia nivel=unica fuentes=planner-maxroll
Al tocar **70** tenéis **68 puntos** de nivel, y el reparto final publicado de esta build cuesta **83**. Llegáis con la Doncella de Hierro ya a **15** y con Mago, Guerrero y Gólem a medio camino de **15/15**. Lo que falta sale del Rango de Temporada, no de subir de nivel.
:::

::: evidencia nivel=unica fuentes=maxroll-endgame,conquestcapped
A nivel máximo: los **glifos** (*Glyphs*) se suben primero a **25** y después a **51**, que es donde se desbloquean sus bonus legendarios. El Foso y la Torre los abre el nodo *Hellish Descent* del **Rango de Temporada 2** — puerta estacional, no de expansión. Y solo se sube de Torment cuando su piso del Foso se limpia en **cinco minutos o menos**.
:::

::: paso n=1 obligatorio=si entitlement=base
**No saltéis a Torment nada más tocar el nivel máximo.** Quedaos en Penitente: el error clásico es cambiar de dificultad por el número, no por la potencia.
:::

::: paso n=2 obligatorio=si entitlement=base
Abrid el Paragón y subid los glifos a los dos umbrales de arriba. Prioridad publicada para esta build: *Dominate* → *Scourge* → *Warrior* → *Deadraiser* → *Abyssal*. ⚠️ Circula un rumor de nerf fuerte a *Dominate* que **no se pudo verificar**: no lo deis por bueno ni por falso.
:::

::: paso n=3 obligatorio=si entitlement=base
Abrid El Foso con el nodo *Hellish Descent*, limpiad el piso que abre **Torment I** y cambiad de dificultad en la Estatua del Mundo. A partir de ahí el Foso es el examen. Y ahora sí: temples, imprints y Hordas Infernales.
:::

Ahí acaba este capítulo y empieza el de la build de arranque: llegáis con el árbol de arriba, la Doncella de Hierro a tope como motor de Esencia, *Unyielding Commander* activa y el Libro ya elegido. Lo que cambia a partir de aquí no es el reparto de puntos: es el equipo.

## Lo que no se sabe

::: evidencia nivel=sinconfirmar fuentes=investigacion
Huecos declarados, ninguno relleno con conjetura:

- **Nivel exacto del Libro de los Muertos.** El **15** está muerto por vuestra propia captura; **5** contra **6** sigue abierto.
- **Los niveles de cada variante del Libro.** Icy Veins publica una tabla completa (**5 · 8 · 12** para Guerreros, **5 · 18 · 22** para Magos, **8 · 28 · 32** para Gólems) que no coincide con las tablas de 2023 —no es texto reciclado— pero no tiene segundo testigo.
- **Si «Llamada del Inframundo» (*Call of the Underworld*) sigue gobernando algo del Gólem.** Ninguna fuente de 2026 lo confirma ni lo desmiente. No esperéis a nivel **25** a que llegue.
- **El techo de puntos: 80, 81 u 83.**
- **Si los 12 puntos del Rango de Temporada se alcanzan íntegramente sin expansión.** Parte del Viaje de Temporada exige *Lord of Hatred*; no se sabe si alguno de los objetivos que dan punto de habilidad está entre ellos. Hueco crítico para vuestro perfil.
- **Qué significa `ranks: 3` en los nodos de modificador y de variante.** Si admitiesen **3** puntos cada uno, maximizar una habilidad costaría **24** puntos y no **4**, y el presupuesto entero cambia.
- **Cuánto vais a tardar.** Ninguna fuente da un tiempo de subida sin expansiones; los «**1-70 en 90 minutos**» asumen Planes de Guerra 🔒 y Ciudad Subterránea 🔒. Una estimación derivada y **sin fuente** habla de una semana de tardes: conjetura declarada, no dato.
- **Por qué la Doncella de Hierro se sube a tope antes que los esbirros.** Nadie lo explica: es lo que guarda el planificador. «Lo que dice Maxroll», no ley.
:::

::: aviso tipo=truco
Estas comprobaciones vuestras cierran casi todo lo anterior en un rato: subid un nivel sin gastar el punto; leed el candado de un clúster bloqueado; anotad a qué nivel salta el aviso del Libro de los Muertos; pulsad dos veces un nodo de modificador para ver si admite más; y mirad si la tercera variante de una habilidad lleva candado con texto de expansión.
:::
