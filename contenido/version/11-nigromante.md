---
titulo: El nigromante de cero
capa: version
parche: "3.1.3"
temporada: 14
estado: vivo
entitlement: base
verificado: 2026-08-19
revisar_despues: 2026-10-15
---

## El dato que gobierna todo lo demás

Antes de una sola habilidad, antes de una sola pieza de equipo: **los esbirros (*minions*) heredan tus estadísticas**. No tienen hoja de personaje propia. La tuya es la suya.

::: evidencia nivel=corroborado fuentes=maxroll-minion-leveling,icyveins-summoner
Maxroll, literal: *«Minions inherit your stats so pay close attention to your stats and balance to make sure you are not over capping.»* Icy Veins concreta qué se hereda: Armadura, Resistencias, Velocidad de Ataque y Probabilidad de Golpe Crítico.
:::

De ahí salen las dos consecuencias que separan al nigromante que sabe del que copia builds:

- **Pasarte de un tope lo desperdicia dos veces**, en ti y en el ejército a la vez.
- **El stat egoísta es el stat de grupo.** Cada punto de crítico que te pones se lo pones a todos. Por eso los Sacrificios del Libro, que te dan estadísticas *a ti* a cambio de menos esbirros, no son la renuncia que parecen.

## Los tres relojes: Esencia, cadáveres, esbirros

### Esencia ✅ (juego base)

La Esencia (*Essence*) es tu recurso: las Básicas la generan, las Fundamentales la gastan. Es vuestro limitador real durante todo el leveling — casi todo lo que se siente mal en un nigromante de nivel bajo es quedarse seco.

::: evidencia nivel=unica fuentes=pcgamer-loh-necro
PC Gamer describe la Esencia como *«the necromancer's version of mana»* y confirma que los Magos Esqueléticos se invocan gastándola.
:::

El motor de Esencia de una build de esbirros no son las Básicas: es una maldición.

::: evidencia nivel=unica fuentes=datos-juego-3-1-0
El Modificador B de Doncella de Hierro (*Iron Maiden*), llamado *Essence Generation*, hace que la maldición **deje de costar Esencia** y **genere 5 por cada enemigo maldito**. Es la razón por la que la ruta de subida de esbirros acaba con cero puntos permanentes en el clúster de Básicas.
:::

En la ficha de personaje, la Voluntad (*Willpower*) sube generación de recurso y curación recibida; la Inteligencia (*Intelligence*) es vuestro stat de daño y la Destreza (*Dexterity*) da crítico y esquiva.

::: evidencia nivel=unica fuentes=maxroll-necro-overview
Inteligencia: **+12,5 % de daño de habilidad por cada 100 puntos**.
:::

### Cadáveres ✅ (juego base)

Los cadáveres son la segunda moneda de la clase y la fuente de su fragilidad estructural: sin muertos en el suelo, medio kit deja de funcionar. El clúster de Cadáver (*Corpse*) depende de ellos, y los Guerreros se alzan de ellos solos.

::: evidencia nivel=corroborado fuentes=icyveins-necro-skills,icyveins-loh-necro
Guerreros Esqueléticos: *«Passive: Raise a skeletal warrior from a nearby Corpse every 2 seconds, up to a maximum of 4 warriors»*. Se generan solos desde cadáveres cercanos y además se les puede **ordenar** atacar, cosa que antes no se podía.
:::

::: evidencia nivel=unica fuentes=maxroll-necro-overview
Maxroll declara que las habilidades de Cadáver (*Corpse Skills*) están *«currently underutilized in modern builds»*. Si venís de guías viejas centradas en Explosión de Cadáver, ese ya no es el camino: hoy los cadáveres son **combustible de esbirros**, no una build en sí.
:::

### Esbirros ✅ (juego base) — y ya no se invocan desde el Libro

Este es el cambio que deja muerto casi todo lo publicado sobre el nigromante: los esbirros se mudaron del Libro al árbol de habilidades.

::: evidencia nivel=corroborado fuentes=icyveins-loh-necro,gamerant-loh-necro
Icy Veins: *«Skeletal Mages, Skeletal Warriors, and Golems are now part of the Necromancer skill tree.»* GameRant, el día del lanzamiento del rework: *«the Necromancer's minion-summoning skills have moved from the Book of the Dead directly to the Skill Tree itself.»*
:::

Y cada tipo se comporta distinto, lo que cambia el ritmo de juego:

::: evidencia nivel=corroborado fuentes=datos-juego-3-1-0,icyveins-necro-skills
Magos: base **3**, se invocan gastando Esencia, decisión deliberada tuya. Con la variante *Coven* ✅ suben a **5**.
Guerreros: base **4**, aparecen solos desde cadáveres cada **2 s**. Con *Master of Puppets* ✅ suben a **7**; la Mejora A de Escaramuzadores añade **2** más.
Gólem: habilidad activa del clúster Macabras, uno solo. Con *Gravebloom* ✅ pasan a ser **3**.
Cada Sacrificio del Libro multiplica la cantidad de ese tipo por **0,5**.
:::

::: aviso tipo=ojo
El famoso «28 esbirros» viene de un periodista de PC Gamer que escribió *«what looks like 28»* contándolos a ojo en una pantalla de previa, antes del lanzamiento. **No es cifra oficial. No planifiquéis con ella.**
:::

## Dónde vive cada esbirro en el árbol (y por qué se abre por NIVEL)

Todo lo que leáis sobre «gastar X puntos para abrir tal clúster» es de dos años atrás. Los clústeres se abren por **nivel de personaje**, punto. Guardar puntos sin gastar no retrasa nada.

::: evidencia nivel=corroborado fuentes=datos-juego-3-1-0,maxroll-skill-trees,icyveins-necro-skills
El fichero de datos del juego (versión 3.1.0.72698) usa un campo llamado `requiredLevel` — **2.409 apariciones** — y **cero** campos de «puntos gastados». Los seis clústeres del Nigromante y su nivel:

| Clúster | Nivel | Esbirro que vive ahí |
|---|---:|---|
| Básicas (*Basic*) | 1 | — |
| Fundamentales (*Core*) | 3 | **Mago Esquelético** |
| Cadáver (*Corpse*) | 4 | **Guerrero Esquelético** |
| Macabras (*Macabre*) | 8 | **Gólem** |
| Maldiciones (*Curse*) | 13 | — (Doncella de Hierro, vuestro motor de Esencia) |
| Definitivas (*Ultimate*) | 19 | — (Ejército de los Muertos) |

Cada habilidad tiene **15 rangos**, no 5. Nivel máximo de personaje: **70**. Las pasivas ya no están en el árbol y la ranura de Pasiva Clave (*Key Passive*) fue **eliminada**.
:::

::: aviso tipo=peligro
Si una guía dice «23 puntos para Definitivas», «33 para la Pasiva Clave», «5 rangos por habilidad», «nivel máximo 60» o «el Gólem se desbloquea a nivel 25 con la misión Llamada del Inframundo», está publicando texto de 2023–2024 aunque lleve fecha de este mes. Una página de Maxroll con sello de julio de 2026 sigue diciendo que cada habilidad sube 5 veces. La fecha no acredita nada.
:::

Cada habilidad tiene tres variantes mutuamente excluyentes. Vosotros veréis dos.

::: evidencia nivel=corroborado fuentes=blizzard-loh-blog,datos-juego-3-1-0
Blizzard: *«Must have the Lord of Hatred expansion to open all three Bonus Skill Variants; otherwise, 2 out of 3 Bonus Skill Variants are accessible.»* En el fichero, la tercera variante es la única con `requiredLevel` entre **30 y 40** 🔒 **Lord of Hatred**. Las variantes 1 y 2 son ✅ juego base.

**Buenas noticias concretas:** las tres variantes que sostienen un ejército —*Coven* (+2 magos), *Master of Puppets* (+3 guerreros) y *Unyielding Commander*— son **✅ vuestras**. Lo que perdéis es *Gargantua* (aura de velocidad para todos los esbirros) y *Unholy Frenzy*. Duele porque las dos builds estrella de esta temporada en Icy Veins están construidas alrededor de *Gargantua*: **no son reproducibles tal cual sin expansión**.
:::

## Qué es hoy el Libro de los Muertos ✅ (juego base)

El Libro es la mecánica de clase del Nigromante y **es de juego base**, no de expansión. Si veis «Spirit Hall» o «Sala de Espíritus» en una guía, eso es del Spiritborn 🔒 Vessel of Hatred: saltadlo.

Hoy el Libro **no invoca nada**. Hace tres cosas: elige **qué forma** tiene cada uno de los tres esbirros que invocas desde el árbol, te da **dos Mejoras** por forma (eliges una), y te ofrece un **Sacrificio**.

::: evidencia nivel=corroborado fuentes=gamerant-loh-necro,blizzard-3-0
GameRant: *«the Book of the Dead still lets players choose which form their Skeletal Warriors, Mages, and Golem take»* y *«choosing to sacrifice a minion type no longer prevents the Necromancer from summoning them at all»*. Blizzard lo confirma de refilón en sus notas: *«Fixed an issue where Book of the Dead minion limits were incorrect after Sacrificing minions»* — es decir, tras sacrificar **siguen existiendo** esbirros con un límite.
:::

Sacrificar ya no es renunciar: **reduce a la mitad**, no elimina.

## Los 27 textos del Libro, uno por uno

Tres esbirros × tres formas × (dos Mejoras + un Sacrificio). Lo que sigue sale de **capturas del propio juego** y del **fichero de datos**. Ninguna wiki generalista publica estos textos: siguen con los de 2023.

### Guerreros Esqueléticos (*Skeletal Warriors*) ✅

::: evidencia nivel=oficial fuentes=captura-jugador
**Defensores (*Defenders*)** — texto literal del cliente en español, nivel 8, parche vivo:

- **Base:** «Los defensores obtienen **10 espinas**. Cada vez que reciben daño, sus huesos se astillan e infligen un **50 %** de sus espinas a los enemigos cercanos.»
- **Mejora 1:** «Comandar a tus defensores hace que **provoquen** a los enemigos cercanos durante **6 s**.»
- **Mejora 2:** «Los defensores tienen un **10 %** de probabilidad de formar un **orbe de sangre** cada vez que infligen daño.»

Las mejoras **se alternan libremente**, sin coste de cambio observable.
:::

::: evidencia nivel=unica fuentes=datos-juego-3-1-0
Resto de formas de Guerrero, del fichero de datos. Traducción propia; el número de tu pantalla manda siempre.

| Forma | Elemento | Efecto |
|---|---|---|
| Escaramuzadores | Mejora A | **2 Escaramuzadores adicionales**; al invocarse saltan solos sobre un enemigo cercano |
| Escaramuzadores | Mejora B | Dejan a los enemigos **Vulnerables** y **Ralentizados un 50 % durante 4 s** |
| Escaramuzadores | Sacrificio | **+5 % de prob. de crítico**, cantidad **−50 %**, y **tu Gólem gana 60 %[x] de daño** |
| Defensores | Sacrificio | **+40 % de Resistencia a Todos los Elementos**, cantidad **−50 %**, **Gólem +60 %[x] daño** |
| Segadores | Mejora A | Los ataques cargados **reducen 3 s un tiempo de reutilización** y **forman un Cadáver** |
:::

::: evidencia nivel=corroborado fuentes=datos-juego-3-1-0,icyveins-summoner
Segadores, Mejora B: infligen **50 %[x] más daño** y tienen **15 % de probabilidad de Aturdir 1 s**.
Segadores, Sacrificio: infliges **15 %[x] más daño**, cantidad de Segadores **−50 %**, y **tu Gólem gana 60 %[x] de daño**.
:::

### Magos Esqueléticos (*Skeletal Mages*) ✅

::: evidencia nivel=unica fuentes=datos-juego-3-1-0
| Forma | Elemento | Efecto |
|---|---|---|
| Sombra | Mejora A | Daño **Corruptor adicional durante 6 s** |
| Sombra | Mejora B | Los proyectiles te dan a ti y al mago una **Barrera del 3 % de tu Vida Máxima durante 4 s**, hasta un tope |
| Sombra | Sacrificio | **Regeneración de Esencia +20 %** y **Esencia máxima +20**, magos **−50 %**, **Gólem +60 %[x]** |
| Frío | Mejora A | El proyectil inicial **se bifurca en 2**; los dañados quedan **Debilitados 4 s** |
| Frío | Mejora B | Lanzan una **ventisca** de daño de Frío durante **6 s** que **Congela un 6 % por segundo**; los dañados quedan **Vulnerables 4 s** |
| Frío | Sacrificio | **+20 %[x] daño a enemigos Vulnerables**, magos **−50 %**, **Gólem +60 %[x]** |
| Hueso | Mejora A | Disparan **2 proyectiles adicionales** al **75 %** del daño normal |
| Hueso | Mejora B | Te **Fortifican** un porcentaje de tu Vida Máxima y **forman un Cadáver al morir** |
:::

::: evidencia nivel=corroborado fuentes=datos-juego-3-1-0,icyveins-summoner
Magos de Hueso, Sacrificio: infliges **20 %[x] más daño mientras tengas una carga de Sobrecarga (*Overpower*)**, los magos se reducen un **50 %**, y **tu Gólem gana 60 %[x] de daño**.
:::

::: evidencia nivel=disputa fuentes=datos-juego-3-1-0,icyveins-summoner
**El tope de la Barrera de los Magos de Sombra no está cerrado.** Una lectura dice que la fórmula del fichero (`0.03*Table(37,SkillRank)*100*2*5`) **escala con el rango de la habilidad**, y que el «30 %» y el «42 %» publicados son el mismo tooltip a distinto rango. La otra señala que la página del 42 % contiene, en esa línea, un marcador de plantilla `#%` **sin sustituir**: un fallo de renderizado. El **3 % por proyectil** es firme; **el tope no**.
:::

### Gólems (*Golems*) ✅

::: evidencia nivel=oficial fuentes=captura-jugador
**Gólem de Hueso** — texto literal del cliente en español, nivel 8:

- **Mejora 1:** «Comandar a tu gólem de hueso provoca que **cree 5 cadáveres**.»
- **Mejora 2:** «Cuando tu gólem de hueso sufre daño, libera unas **agujas de hueso** que infligen **140 [275 %]** de daño. Este efecto puede ocurrir **una vez cada 3 s**. Los enemigos que sufren daño del gólem de hueso…» — la captura corta aquí.
:::

::: evidencia nivel=corroborado fuentes=datos-juego-3-1-0,icyveins-summoner
El final de esa frase cortada: *«…quedan **Vulnerables durante 4 segundos**»*. Coincide en el fichero de datos y en una guía fechada dentro de la temporada.
:::

::: aviso tipo=peligro
En el hilo **oficial** de bugs del Nigromante hay un jugador reportando que *«bone golem is also bugged and not applying vulnerable as it should»*, **sin respuesta de Blizzard**. No construyáis alrededor de esa Vulnerabilidad sin comprobar en pantalla que se aplica.
:::

::: evidencia nivel=unica fuentes=datos-juego-3-1-0
| Forma | Elemento | Efecto |
|---|---|---|
| Sangre | Mejora A | Comandarlo **drena Vida de tus otros esbirros**: **+5 % Vida Máxima** y **+5 %[x] daño por esbirro drenado** durante **20 s**, hasta **+50 % / +50 %[x]** |
| Sangre | Mejora B | Al comandarlo, te **Fortificas un 10 % de tu Vida Máxima por cada enemigo drenado** |
| Sangre | Sacrificio | **Vida Máxima +20 %[x]**, tu Gólem inflige **50 %[x] menos daño** |
| Hierro | Mejora A | Cada ataque provoca una **onda de choque** que daña también a los de detrás |
| Hierro | Mejora B | El **pisotón atrae a los enemigos** y su **tamaño aumenta un 50 %** |
:::

::: evidencia nivel=corroborado fuentes=datos-juego-3-1-0,icyveins-summoner
Gólem de Hueso, Sacrificio: **+10 % de Velocidad de Ataque**, tu Gólem inflige **50 %[x] menos daño**. Recordad la regla de arriba: esa velocidad de ataque **la heredan todos los esbirros**.
Gólem de Hierro, Sacrificio: **+15 %[x] de daño crítico**, tu Gólem inflige **50 %[x] menos daño**.
:::

### El patrón que no publica ninguna guía

::: evidencia nivel=unica fuentes=datos-juego-3-1-0
**Los nueve Sacrificios de Guerreros y Magos llevan una segunda línea: «Tu Gólem gana 60 %[x] de daño».** Los Sacrificios de Gólem no la tienen. Mismo patrón en todos los tooltips del fichero. Traducción práctica: **si sacrificáis guerreros o magos, el Gólem pasa a ser vuestro pilar de daño**, os enteréis o no.
:::

### Qué NO está confirmado, dicho sin adornos

Lo que media internet os venderá como hecho y no lo es:

- **De los 27 textos, solo cinco filas están vistas en pantalla:** la base y las dos Mejoras de los **Defensores**, y las dos del **Gólem de Hueso** (una, cortada). El resto sale del **fichero de datos**: *datamining* servido por Maxroll, no una publicación de Blizzard, y de versión anterior al parche vivo.
- **Ningún Sacrificio está confirmado en juego.** A nivel 8 aparecen con candado y el texto «Para desbloquear…». Los nueve Sacrificios de arriba son texto de fichero.
- **No existe «texto base» publicado** de las nueve formas, salvo el de los Defensores que capturasteis. El fichero solo guarda Mejora A, Mejora B y Sacrificio.
- **La interfaz reparte el texto distinto que el fichero.** Vuestra captura separa las espinas de los Defensores y el Provocar en **dos filas**; el fichero las guarda **juntas en la Mejora A**. Cuando difieran, **manda vuestra pantalla**.
- **Los niveles de desbloqueo de cada forma** (Escaramuzadores, Segadores, Frío, Hueso, Sangre, Hierro) los publica una sola fuente y sin segundo testigo. No los uséis para planificar.

## Cuándo se abre el Libro: la única pregunta que no se cierra desde fuera

::: evidencia nivel=disputa fuentes=icyveins-necro-leveling,ezg-s14-necro,maxroll-minion-leveling
Cuatro fuentes, tres respuestas: **nivel 5** (Icy Veins, y también el resumen de clase de Maxroll), **nivel 6** (EZG) y **nivel 15** (la guía de subida de esbirros de Maxroll). **Maxroll se contradice a sí misma.** El fichero de datos no ayuda: las 27 entradas del Libro tienen `requires: -1`, sin requisito de nivel codificado.
:::

::: evidencia nivel=oficial fuentes=captura-jugador
**El «nivel 15» está muerto.** Vuestra propia captura, a **nivel 8**, muestra el Libro abierto y operativo, con las variantes Defensores y Gólem de Hueso seleccionables y con las Mejoras alternándose. Lo único bloqueado a ese nivel es el **Sacrificio**.
:::

Queda saber si es 5 o 6. Es un dato de treinta segundos que solo se cierra en vuestra pantalla.

## Qué hace especial a esta clase

- **Es la clase que menos depende de que os caiga un objeto concreto**, y eso sin expansión vale oro. El rework movió el control del ejército al árbol, que es **gratis para todos** ✅: Blizzard lo mete bajo el epígrafe *«Major Updates for all Diablo IV Players»*, junto a la subida de nivel máximo.
- **Tenéis tanques propios.** Es la build que menos sufre por no tener mercenario 🔒 Vessel of Hatred: ya lleváis un ejército delante.
- **Un Sacrificio bien elegido escala a diez cuerpos a la vez**, por la herencia de estadísticas. Ninguna otra clase tiene un multiplicador con esa forma.

::: aviso tipo=truco
En dúo, el min-max más barato: **repartíos las maldiciones** — uno Decrépito (*Decrepify*), otro Doncella de Hierro (*Iron Maiden*). Si lleváis la misma se solapa entera y habéis tirado un hueco de barra cada uno. Sin las runas `Teb` y `Wat` 🔒 Vessel of Hatred hay que ponerlas a mano, y ese hueco es caro.
:::

## Qué la hace frágil

::: evidencia nivel=unica fuentes=maxroll-necro-overview
Debilidades que declara la propia Maxroll: *ability bloat* (demasiadas habilidades peleando por seis huecos de barra), **muy frágil al principio**, rotaciones complejas, **dependencia de cadáveres** y **escalado más lento en el late game** que otras clases.
:::

Traducido: los primeros niveles se sienten flojos y os vais a morir. Es normal. El personaje empieza a existir cuando abre Fundamentales y entra el Mago Esquelético, y empieza a funcionar cuando tenéis Gólem, *Coven* y *Master of Puppets* juntos.

La fragilidad estructural es la dependencia de cadáveres: sin muertos no hay Guerreros, y sin Guerreros no hay muro entre vosotros y los golpes. Por eso las builds serias meten generación de cadáveres a propósito.

::: aviso tipo=ojo
Y la fragilidad que nadie os va a contar porque no vende: la Vida base a nivel 70 es **1.526**, y las builds de endgame piden **30.000+**. Todo lo demás es equipo, Paragón ✅ y multiplicadores. Si a nivel 70 tenéis cinco mil de vida, no estáis rotos: estáis empezando el juego.
:::

## Cuatro comprobaciones con el juego delante

::: paso n=1 obligatorio=si entitlement=base
Subid un nivel **sin gastar el punto** y mirad si el siguiente clúster se abre igual. Si se abre, queda demostrado en vuestra partida que el gate es el nivel y podéis tirar a la basura cualquier guía que hable de puntos gastados.
:::

::: paso n=2 obligatorio=si entitlement=base
Anotad **a qué nivel exacto** os salta el aviso del Libro de los Muertos. Es el único hueco de este capítulo que se cierra desde dentro.
:::

::: paso n=3 obligatorio=si entitlement=base
Pulsad **dos veces** un nodo de Modificador. ¿Admite un segundo y un tercer punto? En el fichero de datos cada Modificador figura con `ranks: 3` mientras la habilidad figura con `ranks: 15`, y nadie ha podido resolver qué significa. Si admite tres puntos, maximizar una habilidad cuesta muchísimo más de lo que dice cualquier planificador.
:::

::: paso n=4 obligatorio=no entitlement=base
Mirad la **tercera variante** de cualquier habilidad y leed el texto del candado. Debería pedir *Lord of Hatred* 🔒. Confirmarlo os ahorra semanas de planificar builds que no podéis montar.
:::
