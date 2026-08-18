---
titulo: Ajustes de PS5
capa: nucleo
parche: todas
temporada: todas
estado: vivo
entitlement: base
verificado: 2026-08-19
revisar_despues: 2026-10-15
---

## Lo primero: la asimetría PC/PS5 no es de expansión

Todo lo que sale en este capítulo es ✅ **juego base**. Ni un solo ajuste de consola depende de *Vessel of Hatred* ni de *Lord of Hatred*. Lo que separa vuestras dos pantallas no es lo que habéis pagado: es la plataforma. En el resto de la guía la pregunta constante es "¿esto lo tengo?"; aquí la respuesta es sí a todo.

::: evidencia nivel=oficial fuentes=blizzard-3-1-3,icyveins-3-1-3
El parche vivo **3.1.3** (build 73224, 12/08/2026) no contiene **ningún** cambio de consola, mando, rendimiento, gráficos, accesibilidad, interfaz, cross-play ni filtro de botín. Es un parche de arreglos de la Temporada 14.
:::

::: aviso tipo=ojo
**Aviso de método.** No existe ninguna guía de ajustes de consola escrita dentro de la Temporada 14: casi todo lo verificable sobre PS5 —resoluciones, botones, calibración— está fechado en 2023 y 2024. Nada de 2026 lo contradice y el 3.1.3 no toca esto, así que lo doy por vigente, pero eso es **inferencia**, no confirmación. De ahí el `sinconfirmar` que verás abajo.
:::

::: aviso tipo=truco
Tu juego está en español y las guías en inglés. Los nombres en español que doy son traducción directa, no están verificados contra el cliente. Si un ajuste no aparece con el nombre que digo, **busca por la forma de la frase**, no por la palabra exacta. Y díselo al de PC: él ve los nombres en inglés que usan Maxroll e Icy Veins.
:::

## 1. Rendimiento: en PS5 no eliges "calidad o rendimiento"

Esto choca con lo que te espera de otros juegos. Diablo IV no salió con modos Calidad/Rendimiento/Equilibrado. Salió con un objetivo único de fotogramas altos, y lo que se añadió después fue un interruptor que los **baja** a cambio de trazado de rayos (*ray tracing*).

::: evidencia nivel=sinconfirmar fuentes=purexbox-1-3-5,blizzard-foros-rt
**Visuales Mejoradas (Enhanced Visuals)**, en la pestaña Gráficos, llegó con el parche 1.3.5 (marzo de 2024). Añade sombras y reflejos con trazado de rayos y cambios de oclusión ambiental, y **bloquea el juego a 30 fps por diseño**; sin ella el objetivo es **60 fps**. Hay además reportes de comunidad de caídas **por debajo** de 30 fps en zonas cargadas con el trazado activo. Dos fuentes independientes, pero ambas de 2024: nada de 2026 lo confirma ni lo desmiente.
:::

::: evidencia nivel=disputa fuentes=purexbox-1-3-5,nerdburglars-ps5pro
**Cómo se llama realmente el ajuste.** Versión A: las fuentes abiertas (Pure Xbox, foros de Blizzard) solo conocen **"Enhanced Visuals"** como interruptor único. Versión B: una fuente de 2026 (nerdburglars) afirma que en PS5 se alterna entre **"Performance" y "Fidelity"** sobre la marcha — pero su página devuelve HTTP 403 y solo se leyó el fragmento del buscador. No se ha podido reconciliar. Busca los dos nombres en el menú.
:::

::: paso n=1 obligatorio=si entitlement=base
**Visuales Mejoradas / Enhanced Visuals: OFF.** Sin debate. En Pozo (Pit), Hordas Infernales (Infernal Hordes) y Rupturas, los fotogramas son supervivencia; los reflejos no matan a nada.
:::

::: evidencia nivel=sinconfirmar fuentes=ggrecon-console,altchar-console,nerdburglars-ps5pro
El objetivo de la PS5 es **4K a 60 fps**, según fuentes de lanzamiento (2023) no reverificadas en 2026. **No hay modo de 120 fps**: ninguna fuente abierta confirma uno en consola, solo hay peticiones de comunidad desde la beta. Y sobre **PS5 Pro**, Rod Fergusson confirmó la intención de sacar un parche, pero **no hay ni una especificación oficial** —resolución, fotogramas, PSSR, trazado de rayos—: la única página que las detallaba devuelve HTTP 403.
:::

## 2. HDR y brillo: el orden importa más que los valores

Diablo IV tiene un problema conocido de niveles de negro en HDR: la imagen sale grisácea y lavada. Es lo que más gente hace mal en consola, y en un juego tan oscuro como este arruina la lectura de mazmorras y Rupturas.

::: paso n=2 obligatorio=si entitlement=base
Calibra **primero la consola, después el juego**. Nunca al revés.

1. PS5: `Ajustes > Pantalla y vídeo > Salida de vídeo > Ajustar HDR`.
2. Dentro del juego: `Opciones > Gráficos > Calibrar brillo (Calibrate Brightness)`.
3. Dentro de esa pantalla, en este orden: **Punto de negro (Black Point)** con la imagen de la izquierda → **Punto de blanco (White Point)** con la de la derecha → **Brillo (Brightness)** con la central.
:::

El punto de negro es la clave: viene demasiado alto de fábrica y es la causa del velo gris. Bájalo. El punto de blanco ajústalo al pico real de tu tele, pero júzgalo con una mazmorra en pantalla, no con la imagen de test.

::: evidencia nivel=unica fuentes=game8-consola
Game8 recomienda dejar el **Brillo al 60 % o más** para juego en televisor a distancia de sofá. Es un punto de partida, no un valor canónico.
:::

::: aviso tipo=truco
Si tras calibrar sigue sin convencerte, **apaga el HDR y juega en SDR**: `Ajustes > Pantalla y vídeo > Salida de vídeo > HDR`. Es una opción legítima y muy defendida por la comunidad de HDR precisamente por este juego. Y recalibra si cambias de entorno de luz.
:::

## 3. Jugabilidad e interfaz: los equivalentes a PC

Todo ✅ juego base. Esta tabla no lleva cifras porque no las necesita: son interruptores.

| Opción | Valor | Por qué |
|---|---|---|
| **Advanced Tooltip Information** | ON | Muestra el rango de valores de cada afijo. Sin esto no puedes min-maxear, y además el filtro de botín parsea mal |
| **Advanced Tooltip Compare** | ON | Comparación directa de objetos; con mando se activa manteniendo **Triángulo** |
| **Combat Hit Flash** | ON | Feedback de impacto a distancia de sofá |
| **Screen Shake Effects** | OFF | Claridad visual con la pantalla llena |
| **Item Drop Sounds** | Legendario o superior | Corta el ruido de basura |
| **Highlight Character When Obscured** | ON | Contorno permanente del personaje. Con dos nigromantes en pantalla y sus ejércitos, es el ajuste número uno de consola |
| **Font Scale (escala de fuente)** | Large | "Medium" solo vale pegado a un monitor |
| **Loot audio cues** (sonido ambiental de objetos) | ON | Los objetos suenan según rareza. En consola sustituye al barrido con ratón que hace el de PC |
| **HUD Compass / flecha de objetivo** | ON | En `Accesibilidad > HUD` |
| **Combine Interact and Basic Skill** | **OFF** | Crítico para nigromante. Ver sección 4 |

::: evidencia nivel=unica fuentes=icyveins-accesibilidad
Diablo IV declara más de 50 funciones de accesibilidad ✅. La lista oficial incluye una entrada de **asistencia de mercenarios en combate** — los **Mercenarios son 🔒 Vessel of Hatred**, así que esa entrada no os aplica y no debe confundiros al leer el menú.
:::

::: evidencia nivel=sinconfirmar fuentes=gamertweak-skilltoggle
Varias fuentes describen **"Skill Toggle Behavior"** con valor "Toggle All" como el ajuste de "auto-apuntado". Ni Maxroll ni Icy Veins lo mencionan, y el artículo que más lo desarrolla habla claramente en clave PC (rueda del ratón, teclado numérico). **Está mal documentado. No lo toques a ciegas.**
:::

## 4. Mando: esquema, esquiva y fijado de objetivo

::: evidencia nivel=unica fuentes=game8-controles
Esquema por defecto en PlayStation: moverse con stick izquierdo · **Interactuar y Habilidad Básica combinados en X** · Habilidad Fundamental en Cuadrado · Habilidad 1 en Triángulo · Habilidad 2 en R1 · Habilidad 3 en L2 · Habilidad 4 en R2 · **Esquiva (Evade) en Círculo** · poción en L1 · portal a ciudad en Cruceta abajo · montura en Cruceta derecha · rueda de acciones en Cruceta arriba · **fijar objetivo con R3** · mostrar etiquetas de objetos con L3 · mapa en el panel táctil.
:::

### El remapeo que sí merece la pena

La lógica es una sola: **que nunca sueltes el stick izquierdo**. Los gatillos se pueden mantener pulsados sin mover el pulgar; los botones frontales no.

::: evidencia nivel=unica fuentes=kontrolfreek-mando
KontrolFreek propone: **Habilidad Básica a L2**, **Habilidad Fundamental a R2** (los dos botones que se machacan pasan a gatillos), Interactuar suelto en X, y las habilidades 1-4 repartidas entre Cuadrado, Triángulo, Círculo y R1 para dejar los frontales a los tiempos de reutilización. Sensibilidad de cursor como punto de partida: **6**. Zona muerta (dead zone): **la más pequeña que no te haga derivar el stick**.
:::

::: evidencia nivel=disputa fuentes=game8-controles,kontrolfreek-mando
**Dónde va la Esquiva (Evade).** Versión A: el esquema por defecto la deja en **Círculo**. Versión B: KontrolFreek recomienda moverla a **L3** o a una leva trasera. Mi criterio, que es criterio y no dato: si tienes mando con levas (DualSense Edge), la esquiva a leva trasera es objetivamente superior; si no lo tienes, **déjala en Círculo**. Pulsar el stick para esquivar falla bajo presión, y en consola el pulgar derecho no controla la puntería, así que soltarlo no cuesta nada.
:::

### Fijado de objetivo (target lock): la única configuración correcta

En `Opciones > Controles > Mando`:

- **Hold to Lock Target: OFF**
- **Persist Target Lock: OFF**
- **Use Right Stick to Cycle Locked Target: ON**

Con eso, R3 fija y suelta a mano, y el stick derecho cambia de objetivo. Fijas al jefe cuando quieres y no te quedas pegado a un enemigo lejano mientras te comen.

::: evidencia nivel=unica fuentes=blizzard-foros-targetlock
**Bug reportado el 22/06/2023, sin constancia de arreglo:** con **Hold to Lock Target** y **Use Right Stick to Cycle Locked Target** activados a la vez, mover el stick derecho mientras mantienes el botón de fijado **deja el objetivo bloqueado hasta que acaba el encuentro**. Reportado en Xbox y confirmado por otro jugador; sin respuesta de Blizzard ni nota de parche. Es la razón dura de dejar Hold to Lock Target en OFF.
:::

### El problema de nigromante que nadie te cuenta

Si tienes una **habilidad de cadáver (Corpse Skill)** —Explosión de Cadáveres o Zarcillos de Cadáver— en el mismo botón que hace Interactuar, al recoger un objeto del suelo el juego te obliga a **ciclar por todos los cadáveres** antes de dejarte tocarlo. En una pantalla de nigromante hay cadáveres siempre. Es la diferencia entre farmear y pelearse con el menú.

::: paso n=3 obligatorio=si entitlement=base
Pon **Combine Interact and Basic Skill = OFF** para que Interactuar tenga botón propio, y comprueba que **ninguna habilidad de cadáver comparte botón con Interactuar**. Esto no es preferencia: para un nigromante de consola es obligatorio.
:::

## 5. Qué builds de nigromante son cómodas con mando y cuáles un infierno

Esta es la diferencia real entre vuestras dos pantallas, y es más grande que cualquier ajuste gráfico.

En PC se apunta con el cursor: un Bone Spear va donde está el puntero, con precisión de píxel. **En PS5 no hay cursor.** El personaje lanza en la dirección del stick izquierdo o hacia el objetivo fijado; el stick derecho **no apunta**, solo cicla objetivos. Consecuencias:

- Las habilidades **centradas en ti** (Blood Surge, Blood Mist, Bone Storm) son idénticas con mando. Coste cero.
- Las **direccionales** (Bone Spear, Sever, Blood Wave) pierden precisión: tienes ocho o dieciséis direcciones cómodas, no 360 grados finos.
- Las de **posicionamiento remoto** (Corpse Explosion, Corpse Tendrils) son el punto débil real: hay que elegir un cadáver concreto a distancia, y con mando lo elige el juego, no tú.

::: evidencia nivel=unica fuentes=maxroll-tierlist-necro,maxroll-minion
Cruce de la tier list de nigromante de la Temporada 14 (Maxroll, 29/06/2026) con la exigencia de apuntado:

| Build | Tier endgame | Exigencia de apuntado | ¿Juego base? |
|---|---|---|---|
| Esbirros (Minion) | B | **Muy baja** — los esbirros van auto-apuntados por comandos | ✅ en su núcleo |
| Blood Surge | B | **Muy baja** — área centrada en ti | ✅ probable |
| Gólem | B | Baja | ✅ probable |
| Blood Wave | A | Media | 🔒 la build competitiva pide Runewords y Mercenarios (Vessel of Hatred) |
| Bone Spirit | A | Media | 🔒 su equipo documentado incluye set de Lord of Hatred |
| Bone Spear | C | **Alta** — proyectil que hay que enfilar | ⚠️ su versión de guía usa Talismanes y Mercenarios |

La guía de esbirros de Maxroll (22/07/2026) dice literalmente que los esbirros se dirigen **mediante comandos con auto-apuntado**, y que el sistema de comandos es directo con mando.
:::

**Traducción práctica:** la de PS5 lleva **Esbirros o Blood Surge**. No es una concesión: son las dos builds que no pierden nada por no tener ratón. Bone Spear es la trampa clásica —la build "canónica" de las guías, que el de PC lleva sin problema y que en consola sangra daño efectivo en cada lanzamiento.

::: evidencia nivel=disputa fuentes=informe-nigro-builds,informe-ajustes-consola
**Qué tres builds son viables con juego base.** Versión A (informe dedicado, que filtró build por build las listas de charms y runas): **Esbirros → Blood Surge → Blood Wave**, plan B Bone Spear, y **Bone Spirit vetada** por depender de *Red Blessing* y del set *Berú of Desecration* 🔒 Lord of Hatred. Versión B (informe de consola, mención de pasada sin razonar): Esbirros, Bone Spear y **Bone Spirit**. **Gana la A**: es el informe cuyo trabajo era exactamente ese.
:::

::: aviso tipo=peligro
**No llevéis los dos el ejército completo de esbirros.** Es redundancia de rol, caos visual insoportable y —esto es criterio derivado, sin fuente que lo mida— caída de fotogramas en la consola. Uno de ancla con esbirros, el otro de martillo con área. Repartíos también las maldiciones: sin runas 🔒, cubrir Decrepify e Iron Maiden cuesta dos huecos de barra, y llevando una cada uno os devolvéis un hueco por cabeza.
:::

## 6. Battle.net, PS Plus y cross-play

::: paso n=4 obligatorio=si entitlement=base
**Vincula la cuenta de PSN a Battle.net desde el propio juego, antes de subir un solo nivel.** Al lanzar Diablo IV aparece el aviso de inicio de sesión. Después verifica en `battle.net > Conexiones (Connections)` que el enlace está. Si te saltas esto y luego lo arreglas, te arriesgas a perder el vínculo de cross-progression del personaje.
:::

::: evidencia nivel=corroborado fuentes=maxroll-multiplayer,denofgeek-crossplay
**Cross-play y cross-progression son ✅ juego base, gratuitos y automáticos.** Viajan entre plataformas: personajes y nivel, equipo, Paragón, cosméticos, logros, progreso del Pase de Batalla y progreso estacional. **No viaja la licencia del juego**: para jugar en otra plataforma hay que comprarlo otra vez ahí. Cross-play activo entre PC, PS4, PS5, Xbox One y Xbox Series X|S. Para agregaros necesitáis el **BattleTag** del otro, en formato `Nombre#1234`.
:::

Comprueba que `Opciones > Social > Cross-Network Play` y `Cross-Network Communication` están en **ON**; vienen activados de fábrica. Una guía de Icy Veins sugiere desactivar el cross-play para reducir la población de zona y farmear tranquilo: **si lo hacéis, dejáis de poder jugar juntos.**

::: evidencia nivel=unica fuentes=informe-duo-coop
El jugador de consola necesita **PS Plus** (o Xbox Live Gold) para el multijugador en línea. Lo afirma una sola fuente del expediente. **Compruébalo el día uno**, porque es lo único que puede impedir físicamente que os agrupéis.
:::

::: aviso tipo=peligro
**No marquéis Solo Self-Found (SSF)** al crear el personaje. Es ✅ juego base y es nuevo de la Temporada 14, y **desactiva agrupar, comerciar, co-op de sofá, Party Finder y Dark Citadel 🔒 durante toda la temporada, sin vuelta atrás**. No da ningún bonus de drop: solo da acceso a clasificaciones SSF propias. Es el único error de la primera pantalla capaz de arruinaros la temporada entera. Los dos: **Estacional, Softcore, NO SSF**.
:::

## 7. Lo que la PS5 no puede hacer, y cómo compensarlo

### El filtro de botín (Loot Filter): la herida real

::: evidencia nivel=disputa fuentes=icyveins-loot-filter,maxroll-loot-filter
**¿El filtro de botín requiere expansión?** Versión A: Icy Veins, **citando el anuncio de Blizzard**, dice que está disponible para todos los jugadores independientemente de que tengan la expansión ✅. Versión B: Maxroll escribe que requiere *Lord of Hatred* y no está en el juego base 🔒. **Gana la versión A**: es una cita directa de Blizzard frente a una redacción ambigua sobre "se lanzó con la expansión". Se comprueba en 30 segundos abriendo `Opciones > Jugabilidad`.
:::

::: evidencia nivel=disputa fuentes=maxroll-loot-filter,d4lootfilter,d4filterforge
**¿Puede la PS5 importar códigos de filtro?** Versión A (dos fuentes): no. Maxroll dice que en consola hay que configurar los filtros a mano desde cero, y d4lootfilter.com (act. mayo 2026) que importar/exportar está solo en PC y que PS5 y Xbox pueden crear y editar reglas pero no pegar un código. Versión B (una fuente): D4 Filter Forge afirma que el formato es multiplataforma y que un filtro creado en PC se importa en consola **si estás en la misma cuenta de Battle.net**. No se contradicen del todo —una cosa es pegar texto y otra que el filtro viaje con la cuenta— pero **nadie lo confirma explícitamente**.
:::

::: paso n=5 obligatorio=no entitlement=base
**Plan del filtro de botín, en orden.**

1. Que el de PC importe el código y miréis si el filtro aparece en la cuenta de la PS5. Es inferencia, no está confirmado, pero comprobarlo es gratis.
2. Si no aparece (lo más probable): abre **d4lootfilter.com** en el móvil, pega ahí el código que use el de PC y la web te lo descompone en su lista completa de reglas legibles —visibilidad, colores, afijos requeridos, tipos de objeto—. Las tecleas a mano en `Opciones > Jugabilidad > Filtro de botín`.
3. Media hora, una vez por temporada. Y hay que hacerlo: que los dos veáis lo mismo en pantalla es media conversación del dúo.
:::

::: evidencia nivel=disputa fuentes=maxroll-loot-filter,d4lootfilter
**Límite de reglas por filtro.** Una fuente dice **25**, otra **30**; el 25 tenía además un tercer apoyo en una wiki vetada por este proyecto, que no cuenta. **Planifica con 25 y compruébalo en el menú.** Lo que sí está claro: las reglas se evalúan de arriba abajo y la de arriba manda.
:::

::: aviso tipo=ojo
Empieza con el filtro **Light**, no con **Strict**. Mientras subís nivel necesitáis ver legendarios para extraer aspectos al Códice. Escala Light → Medium → Strict conforme subáis de Tormento.
:::

### El resto de limitaciones

| Limitación de la PS5 | Impacto | Compensación |
|---|---|---|
| No hay overlays ni segunda ventana: no puedes tener Maxroll encima del juego | Medio-alto | **Tablet o móvil al lado del sofá** con el planificador abierto. Maxroll, D4Builds y Mobalytics son webs y van en el móvil igual que en PC |
| Teclear texto (chat, cantidades de oro) es un suplicio, y comerciar es lentísimo | Medio | **Teclado USB o Bluetooth conectado a la PS5**; la consola lo soporta a nivel de sistema. Y que las cantidades de oro las teclee el de PC |
| Las apps de Windows (Diablo4Companion, d4lf, Overwolf) y los addons no existen aquí | Bajo | Diablo IV no tiene ecosistema de addons ni en PC, y el filtro de botín oficial ✅ deja obsoletos casi todos los overlays |

::: evidencia nivel=sinconfirmar fuentes=dexerto-trading
Sobre la lentitud del comercio en consola hay reportes de **40 minutos para tres intercambios** y de jugadores expulsados del servidor por inactividad en mitad de un trade por lo que se tarda en teclear. La fuente es de noviembre de 2023 y Blizzard no lo había reconocido formalmente entonces. **No está reverificado en 2026**, pero el problema de fondo (no hay teclado) sigue existiendo.
:::

## 8. Latencia: nada de lo que importa está dentro del juego

Diablo IV no expone ajustes de latencia en consola: no hay equivalente a Reflex. Todo está fuera del juego.

- **Modo Juego de la tele: ON.** La ganancia más grande con diferencia, porque desactiva interpolación, suavizado y nitidez artificial. Es la causa número uno de las quejas de "input lag en D4". Compruébalo antes que nada, junto con el desenfoque de movimiento y el resto de post-proceso de la tele, que van a OFF.
- **ALLM y VRR en ON** en los ajustes de la PS5, con salida a 120 Hz aunque el juego no tenga modo de 120 fotogramas, y **cable HDMI 2.1 Ultra High Speed** si quieres las tres cosas a la vez.
- **Ethernet en vez de WiFi.** El juego es siempre en línea; el retardo de red se percibe como retardo de mando.

No doy cifras de milisegundos porque el expediente no tiene fuente que las respalde. Que la ganancia del Modo Juego es grande está fuera de duda; cuánto exactamente, no lo sé.

## 9. Checklist de la primera sesión

::: paso n=6 obligatorio=si entitlement=base
**Fuera del juego:** Modo Juego, ALLM y VRR de la tele ON · post-proceso OFF · HDR del sistema calibrado · Ethernet · teclado USB.

**Gráficos:** Visuales Mejoradas OFF · brillo calibrado en el orden negro → blanco → brillo.

**Jugabilidad e interfaz:** los dos Advanced Tooltip ON · Combat Hit Flash ON · Screen Shake OFF · sonidos de drop en legendario o superior · **Combine Interact and Basic Skill OFF** · escala de fuente Large · resaltado de personaje ON · sonido ambiental de objetos ON.

**Mando:** Hold to Lock Target OFF · Persist Target Lock OFF · Cycle Locked Target ON · zona muerta mínima · Básica a L2 y Fundamental a R2 · esquiva en Círculo o leva trasera · **ninguna habilidad de cadáver en el botón de Interactuar**.

**Social:** Cross-Network Play ON · PSN vinculada a Battle.net y verificada en Conexiones · PS Plus comprobado · **NO marcar Solo Self-Found**.
:::
