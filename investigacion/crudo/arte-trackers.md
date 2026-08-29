# Arte previo: trackers de otros juegos y de dónde sacan los datos

**Fecha de investigación:** 29 de agosto de 2026
**Dominio:** arquitectura de captura de datos en herramientas de terceros para juegos
**Pregunta central:** cuando no hay API, ¿qué patrón usa la industria? ¿Y cuál sirve en Diablo IV?

---

## 1. Resumen: los siete patrones, ordenados de mejor a peor

La industria no improvisa. Hay siete formas conocidas de sacar estado de un juego, y están
jerarquizadas por fiabilidad y por riesgo legal. Diablo IV, mirado con esta escalera al lado,
resulta ser un juego que **cierra los seis primeros peldaños**.

| # | Patrón | Ejemplo canónico | Fiabilidad | Riesgo EULA | ¿Disponible en D4? |
|---|--------|------------------|-----------|-------------|--------------------|
| 1 | **API web oficial del publisher** | Bungie.net → Destiny Item Manager | Muy alta | Nulo (OAuth, permiso revocable) | **No** |
| 2 | **API local del propio cliente** | LoL Live Client Data (127.0.0.1:2999) | Alta | Bajo (tolerada, no soportada) | **No** |
| 3 | **Addon / mod dentro del juego** | WoW Lua, mods de Slay the Spire | Muy alta | Nulo donde se permite | **No** (D4 no tiene addons) |
| 4 | **Log de partida en disco** | Hearthstone `Power.log`, save de StS | Alta | Muy bajo (fichero propio del usuario) | **No** (sólo log de motor) |
| 5 | **Portapapeles (el juego copia el objeto)** | Path of Exile, Ctrl+C → Awakened PoE Trade | Muy alta | Muy bajo, es el estándar de oro | **No** |
| 6 | **Capa de accesibilidad (TTS / screen reader)** | D4LF, D4TTS vía Tolk + `saapi64.dll` | Media, frágil | **Ambiguo** (DLL en la carpeta del juego) | Sí, con asteriscos |
| 7 | **Captura de pantalla + OCR** | Diablo4Companion, d4-item-tooltip-ocr, bots de TFT | Baja-media | Bajo si no dibuja ni automatiza | **Sí — es lo que queda** |

Y aparte, fuera de la escalera: **plataforma intermediaria** (Overwolf), que no es una fuente de
datos sino un tercero que negocia con el publisher y revende eventos. En D4 existe, pero lo que
expone no incluye objetos (ver §4).

**La conclusión que importa:** el diseño actual (mss + winocr + parser de vocabulario cerrado,
ventana propia, sin overlay, sin automatizar) **no es una elección perezosa: es el único peldaño que
queda en pie en Diablo IV**. Todos los demás están cerrados por el juego, no por falta de ganas.

---

## 2. Tabla maestra de herramientas

Estrellas leídas el 29-ago-2026. Donde no pude verlas, lo digo.

| Herramienta | Repo | Lenguaje | **Fuente de datos** | Nota |
|---|---|---|---|---|
| **Hearthstone Deck Tracker** | `github.com/HearthSim/Hearthstone-Deck-Tracker` — 4,9 k ★ | C# / WPF | **Log en disco**: `Power.log` que el propio juego escribe si activas `log.config` | El tracker de referencia del sector. El README no explica la fuente; lo confirman el blog de HearthSim y la wiki de logging |
| **python-hslog** | `github.com/HearthSim/python-hslog` | Python | Deserializador de `Power.log` a árbol de paquetes | La pieza reutilizable: parsing separado de la UI |
| **Open-League-Overlay** | `github.com/bossNilac/Open-League-Overlay` | (no verificado) | **API local**: `https://127.0.0.1:2999/liveclientdata/allgamedata` | Sólo funciona con partida en curso |
| **LeagueClientLiveDataApi** | `github.com/Plutokekz/LeagueClientLiveDataApi` | Python | Misma API local del cliente | Wrapper puro |
| **Destiny Item Manager (DIM)** | `github.com/DestinyItemManager/DIM` — 2,2 k ★, MIT | TypeScript / React | **API web oficial de Bungie.net** con OAuth | No necesita el juego abierto. Bungie limita qué puede hacer (p. ej. no desmantela objetos) |
| **bungie-api-ts** | `github.com/DestinyItemManager/bungie-api-ts` | TypeScript | Definiciones de tipos de la API oficial | |
| **wowclp** | `github.com/m-mizutani/wowclp` | Python | **Log en disco**: `WoWCombatLog.txt` (`/combatlog`) | |
| **RunHistoryPlus** (Slay the Spire) | `github.com/modargo/RunHistoryPlus` | Java (mod) | **Mod dentro del juego** (ModTheSpire/BaseMod) | Acceso directo al estado, sin adivinar |
| **runlogger** (Slay the Spire) | `github.com/colinking/runlogger` | Java (mod) | Mod que **escribe su propio log JSON** por run | Patrón híbrido: mod que fabrica el log que no existía |
| **SpireScope** | `github.com/thequantumfalcon/spirescope` — 26 ★ | Python | **Ficheros de guardado + log del juego**, más datos de wiki | Se declara *local-first*, "no requiere mods del juego" |
| **Awakened PoE Trade** | `github.com/SnosMe/awakened-poe-trade` — 2,6 k ★, MIT | TypeScript (Electron + Vue) | **Portapapeles**: el juego copia el texto del objeto con Ctrl+C | El caso más parecido al nuestro y el que mejor razona su legalidad |
| **Diablo4Companion** | `github.com/josdemmers/Diablo4Companion` — 321 ★, MIT | C# | **OCR**: Tesseract + Emgu CV sobre captura de pantalla | **Sí dibuja overlay** sobre el juego (botón in-game arriba a la izquierda) |
| **d4lf (Diablo 4 Loot Filter)** | `github.com/d4lfteam/d4lf` — 206 ★ | Python | **OCR + capa de accesibilidad TTS** (`saapi64.dll` cargado por el juego vía Tolk) | **Automatiza ratón** para mover objetos del alijo. Cruza la línea que nosotros no cruzamos |
| **d4-item-tooltip-ocr** | `github.com/mxtsdev/d4-item-tooltip-ocr` — 40 ★ | Python | **OCR**: PaddleOCR con modelo propio entrenado en D4 (`en_PP-OCRv3_rec-d4_tooltip`) | Salida JSON: nombre, tipo, poder, afijos, aspecto, engarces. Detección opcional del tooltip (`--find-tooltip`) |
| **d4-ocr** | `github.com/mivuorin/d4-ocr` — 0 ★ | C# | **OCR**: Tesseract (tessdata_fast) + captura por PInvoke nativo | Overlay con GameOverlay.Net. **Confiesa 1–3 s por captura**: más lento que leer con los ojos |
| **diablo4trading-ocr** | `github.com/wenqu/diablo4trading-ocr` — 1 ★ | TypeScript | **OCR**: tesseract.js con pipeline por segmentos | Preproceso → detección de bordes → detección de viñetas → troceado → OCR → JSON |
| **D4TTS** | `github.com/josdemmers/D4TTS` — 0 ★, MIT | (no verificado) | **Capa de accesibilidad**: `saapi64.dll` en la carpeta de instalación + lector de pantalla activado en el juego | Prueba de concepto del mismo autor de Diablo4Companion |
| **TFT-OCR-BOT** | `github.com/jfd02/TFT-OCR-BOT` | Python | **OCR** de banquillo/tablero/objetos | **Es un bot: juega solo.** Lo cito como frontera, no como modelo. Sólo 1920×1080 sin bordes |
| **Overwolf (plataforma)** | `dev.overwolf.com` — propietaria | JS sobre runtime propio | **Eventos negociados con el publisher** (GEP), captura por gancho gráfico DX8/9/11/12 y OpenGL | En D4 expone personaje, ubicación y estado del Pozo. **No expone inventario ni afijos** |

---

## 3. Los patrones, uno a uno, con lo que enseña cada uno

### 3.1 Log en disco — el patrón dominante cuando no hay API (Hearthstone)

Hearthstone Deck Tracker, con 4,9 k estrellas y una década de vida, **no lee memoria ni pantalla**:
lee un fichero de texto que el propio juego escribe. Hay que activarlo creando un `log.config` en
`%LOCALAPPDATA%\Blizzard\Hearthstone` con `[Power] LogLevel=1 FilePrinting=true`. A partir de ahí
`Power.log` contiene, en palabras de la wiki de logging, todo lo que pasa en la partida; se borra y
se reinicia cada vez que abres el juego.

Lo interesante para nosotros es la **arquitectura del parser**, no el fichero. HearthSim separó el
deserializador (`python-hslog`) de la interfaz. El log se convierte en paquetes, los bloques
`BLOCK_START` / `BLOCK_END` anidan, y el conjunto forma un "packet tree" recorrible
recursivamente. En su post técnico cuentan que el cuello de botella era parsear la marca de tiempo
de *todas* las líneas: limitar el parseo a las líneas realmente usadas redujo el tiempo **más de un
70 %**.

> Aplicable directo: nuestro parser de tooltips debe ser una librería aparte, con su propia batería
> de fixtures de texto OCR, ejecutable sin tkinter y sin el juego delante. Y el filtro barato va
> antes del caro.

### 3.2 API local del cliente — el regalo de Riot (League of Legends)

Cuando entras en partida, el cliente de LoL abre el puerto 2999 y sirve por HTTPS
`GET https://127.0.0.1:2999/liveclientdata/allgamedata`, más endpoints específicos
(`/activeplayer`, `/playerlist`, `/playeritems`, `/activeplayerabilities`, `/eventdata`,
`/gamestats`). Sólo responde a localhost: peticiones desde otra IP se rechazan. Usa certificado
autofirmado, así que hay que ignorar el error TLS o instalar la raíz de Riot.

El matiz jurídico es delicioso y aplicable: Riot documenta la API **y a la vez avisa** de que no
está oficialmente soportada para aplicaciones de terceros, sin garantía de uptime ni de aviso
previo ante cambios. Es tolerancia documentada, no contrato.

> Aplicable: nada técnicamente (D4 no abre ningún puerto equivalente), pero sí como **modelo de
> expectativas**: incluso donde el publisher ayuda, el tercero asume que la fuente puede cambiar sin
> avisar. Nuestro manifiesto de parche ya hace eso; hay que extenderlo al pipeline de captura.

### 3.3 API web oficial — el caso feliz (Destiny 2 / DIM)

DIM (TypeScript, MIT, 2,2 k ★ en el repo principal) es una PWA que habla con la API pública de
Bungie.net por OAuth. El usuario autoriza en bungie.net, ve la app en "Accounts & Linking" y puede
revocar el permiso cuando quiera. No hace falta que el juego esté abierto. Bungie acota lo que se
puede hacer: DIM mueve y equipa, pero **no puede desmantelar objetos**.

> Aplicable: cero técnicamente. Sirve como **contraste que hay que decir en voz alta en el README**:
> lo que hacemos con OCR sería una llamada HTTP si Blizzard publicase una API de personaje. No la
> hay, y por eso el resto del diseño es como es.

### 3.4 Addon dentro del juego — y cómo un publisher lo cierra (WoW, 2026)

WoW es el ejemplo de manual de "el publisher te da acceso oficial". Y también, desde este mismo
año, el ejemplo de que ese acceso se puede retirar. En el parche **12.0.0 (Midnight)**:

- `COMBAT_LOG_EVENT` y `COMBAT_LOG_EVENT_UNFILTERED` **dan error al registrarse**.
- `CombatLogGetCurrentEventInfo()` deja de estar disponible para código de addon (*tainted*).
- Existe un `COMBAT_LOG_EVENT_INTERNAL_UNFILTERED` reservado a código de Blizzard.
- La razón declarada: limitar la capacidad de los addons de hacer lógica compleja y tomar
  decisiones a partir de información de combate.
- El recambio oficial: el namespace **`C_DamageMeter`** (`GetAvailableCombatSessions()`,
  `IsDamageMeterAvailable()`…) y un `C_CombatLog` filtrado.
- Explícitamente **no** se pretende impedir la personalización estética de la interfaz.

El log en disco (`WoWCombatLog.txt` vía `/combatlog`, que alimenta a Warcraft Logs y a parsers como
`wowclp`) es una vía distinta y sigue siendo un fichero del usuario.

> Aplicable, y es la lección más importante del informe: **Blizzard distingue entre "leer y mostrar"
> y "decidir por el jugador"**. Cuando quiso cortar algo, cortó la capacidad de *tomar decisiones en
> vivo*, no la de enseñar información. Nuestra herramienta cae del lado bueno de esa línea —
> compara objetos que el jugador ya tiene delante, en su propia ventana, sin decirle qué pulsar—
> y eso conviene que esté escrito en el README con estas palabras.

### 3.5 Portapapeles — el estándar de oro (Path of Exile)

En PoE, con el objeto bajo el ratón, Ctrl+C copia el **texto completo del objeto** al portapapeles:
base, rareza y cada modificador. Awakened PoE Trade (Electron + Vue, MIT, 2,6 k ★) escucha ese
portapapeles, parsea el texto y consulta el mercado.

Su FAQ es la mejor formulación pública que he encontrado del criterio de seguridad de una
herramienta de terceros:

> "If app complies with the game ToS, does one server action per button press and doesn't interact
> with the game client itself (injecting into the process, changing the process memory aka cheats)
> it can be considered safe."

Tres condiciones: cumplir el ToS, **una acción por pulsación** (nada de bucles automáticos), y no
tocar el proceso del juego.

**¿Existe esto en Diablo IV? No.** Lo que hay es shift-click para enlazar el objeto en el chat, con
quejas recurrentes de que el enlace no se puede ver y de que ciertos objetos (correlacionado con
engarces y gemas) no se pueden enlazar. Hubo una propuesta comunitaria de añadir Ctrl+C para copiar
la información del objeto; **es una petición, no una función existente**.

> Aplicable — y es la mejor idea del informe: **adoptar el criterio de "una acción por pulsación"
> aunque nuestra fuente sea OCR**. El diseño actual sondea la pantalla cada 0,7 s de forma continua.
> Cambiarlo a *captura bajo atajo* (el usuario apunta al objeto y pulsa la tecla) tiene tres ventajas
> a la vez: elimina el bucle continuo, reduce el coste de CPU a casi nada, y coloca la herramienta
> exactamente en la categoría que Awakened PoE Trade defiende con éxito desde hace años. El
> checklist en vivo de 10 huecos + 6 habilidades se puede hacer igual, sólo que avanzando una casilla
> por pulsación en vez de por sondeo.

### 3.6 Capa de accesibilidad (TTS) — el atajo tentador que yo no cogería

Diablo IV lleva lector de pantalla y usa **Tolk**, una librería de abstracción de lectores de
pantalla (`github.com/dkager/tolk`), con la interfaz System Access API (SAAPI). Tolk permite cargar
DLLs de TTS de terceros. Consecuencia: si pones un `saapi64.dll` firmado en la carpeta de
instalación de Diablo y activas el lector de pantalla y el soporte de lectores de terceros en los
ajustes del juego, **el juego carga tu DLL y le entrega el texto de la interfaz**, incluidos los
tooltips de objetos. En lugar de leerlo en voz alta, la DLL lo reenvía a tu aplicación.

Esto es lo que hace **d4lf** ("D4LF gets item information by reading the screen and using TTS
information sent for accessibility") y lo que demuestra **D4TTS**. Texto perfecto, sin OCR, sin
errores de reconocimiento.

Tres razones para no seguir ese camino:

1. **Se rompió.** Hilo oficial del foro de Blizzard: *"3rd Party Screen Readers no longer function in
   Season 12"*, desde el PTR y confirmado en el lanzamiento de la temporada el **11 de marzo de
   2026**. El mantenedor reporta que su `saapi64.dll` dejó de funcionar sin haber cambiado nada, y
   pregunta qué requisitos se han modificado. En el hilo que leí **no hay respuesta oficial ni
   confirmación de arreglo**.
2. **Requiere poner una DLL dentro de la carpeta del juego y que el proceso del juego la cargue.**
   Aunque sea el mecanismo oficial de accesibilidad y no una inyección, el binario acaba corriendo
   dentro del proceso de Diablo. Contra el criterio de Awakened PoE Trade ("doesn't interact with the
   game client itself, injecting into the process"), eso está del lado incómodo de la raya. Nuestra
   restricción dura dice "nada de inyección"; esto es *casi* inyección con permiso.
3. **La DLL tiene que estar firmada** para que Diablo la recoja, lo que añade una dependencia de
   distribución que un proyecto personal no quiere.

> Aplicable **como nota, no como implementación**: merece un párrafo en la documentación explicando
> por qué la vía TTS, que daría texto perfecto, se descarta a propósito. Es exactamente el tipo de
> decisión que hay que dejar por escrito para no reabrirla cada seis meses. Y hay un aviso operativo:
> **d4lf mueve objetos del alijo automatizando el ratón**. Eso es lo que separa a un lector de un
> bot, y es la línea que nosotros no cruzamos.

### 3.7 Captura + OCR — lo que queda, y cómo lo hacen los que ya están ahí

Cuatro proyectos vivos de OCR sobre tooltips de D4, con cuatro motores distintos:

| Proyecto | Motor OCR | Captura | Salida | Dato duro |
|---|---|---|---|---|
| Diablo4Companion (321 ★) | Tesseract + Emgu CV (visión por computador) | Pantalla | Afijos, aspectos, runas, sigilos | Dibuja overlay sobre el juego |
| d4-item-tooltip-ocr (40 ★) | **PaddleOCR con modelo propio entrenado en D4** | Captura completa o recorte, `--find-tooltip` | JSON estructurado | El único que entrena un modelo específico |
| diablo4trading-ocr (1 ★) | tesseract.js | Imagen | JSON alineado con sus paquetes de datos de juego | Pipeline por troceado; contempla ajustes de daltonismo y tooltips de tamaño variable |
| d4-ocr (0 ★) | Tesseract (tessdata_fast) | PInvoke nativo, contempla escalado de resolución | En pantalla | **1–3 s por captura; el autor admite que es más lento que leer con los ojos** |

Tres cosas que sacar de aquí:

- **Nadie usa `winocr` / `Windows.Media.Ocr`.** Los cuatro tiran de Tesseract o Paddle. No encontré
  ningún proyecto público de D4 con el motor nativo de Windows (ver §6). Eso significa que la
  elección de `winocr` no tiene precedente que copiar, pero también que la comparativa de precisión
  contra Tesseract en la fuente concreta del tooltip de D4 **está sin hacer y hay que hacerla en
  casa**, con capturas propias, antes de dar el motor por bueno.
- **La latencia es el enemigo declarado.** Un proyecto que hace lo mismo confiesa 1–3 s por captura.
  Sondear a 0,7 s sólo tiene sentido si el ciclo completo (captura + OCR + parseo) cabe holgadamente
  dentro de esos 700 ms; si no, el sondeo se solapa consigo mismo. Otra razón para el atajo bajo
  demanda de §3.5.
- **El troceado del tooltip antes del OCR es la técnica compartida.** diablo4trading-ocr detecta
  bordes y viñetas y trocea; d4-item-tooltip-ocr localiza el tooltip. Nadie lanza el OCR contra la
  pantalla entera y espera lo mejor.

### 3.8 Plataforma intermediaria — Overwolf, y por qué no resuelve nuestro problema

Overwolf es el tercero que negocia con los publishers ("works closely with game publishers […] to
make sure all apps on Overwolf comply with the terms of the games") y revende eventos a las apps
mediante el **Game Events Provider (GEP)**, con soporte gráfico de DX8/9/11/12 y OpenGL. Es la
respuesta de la industria a "quiero un overlay legal".

**Diablo IV está soportado.** Y esto es lo decisivo: los eventos que expone son

- `gep_internal` (versión),
- `game_info` (BattleTag, oro total entre personajes),
- `match_info` (estado del Pozo: dentro/fuera, nivel, completado),
- `location` (coordenadas y zona),
- `me` (nombre, clase, nivel, paragón, XP, vida actual).

**No hay inventario. No hay afijos. No hay objetos.** La vía oficial-por-intermediario, la única con
bendición del publisher, no sirve para comparar objetos.

> Aplicable: **es la prueba documental de que no estamos evitando una API que existe**. Vale citarlo
> literalmente en el README: la única fuente de datos de D4 con acuerdo de publisher expone salud,
> nivel y coordenadas, y no expone un solo afijo. Es el mejor argumento de buena fe que tenemos.

---

## 4. Diablo IV, peldaño a peldaño: por qué no queda otra

| Vía | ¿Existe en D4? | Evidencia |
|---|---|---|
| API web de personaje | **No** | No encontré ninguna API pública de Blizzard tipo Bungie.net para inventario de D4 (ver §6) |
| API local (puerto) | **No** | Sin equivalente documentado al 2999 de Riot |
| Addons / mods oficiales | **No** | D4 no tiene sistema de addons; el precedente de WoW muestra que Blizzard, cuando lo da, lo controla |
| Log de partida en disco | **No** | El juego escribe `FenrisDebug.txt` en la carpeta de instalación: configuración de sistema, TACT, locales, entradas `[CRASH]`. Es un log de motor, no de gameplay |
| Copiar objeto al portapapeles | **No** | Sólo shift-click para enlazar en chat, con fallos reportados. El Ctrl+C es una *propuesta* del foro, no una función |
| Eventos vía Overwolf | Sí, pero **inútil aquí** | GEP D4 expone personaje/ubicación/Pozo; **ni inventario ni afijos** |
| Accesibilidad TTS | Sí, **frágil y ambiguo** | Tolk + `saapi64.dll` firmada en la carpeta del juego; roto desde la Temporada 12 (11-mar-2026) sin respuesta oficial en el hilo |
| **Captura + OCR** | **Sí** | Cuatro proyectos públicos vivos con esta arquitectura |

---

## 5. Riesgo legal, comparado

Lo que dice Blizzard, textualmente (aviso oficial de **PezRadar, 26 de julio de 2023**): se prohíbe
"cheating, bots, hacks, and any other unauthorized software which automates, modifies, or otherwise
interferes with the game", y se nombra explícitamente **TurboHUD4** como prohibido, con riesgo de
suspensión permanente. **El aviso no menciona por su nombre overlays, HUDs, filtros de botín ni
herramientas de sólo lectura.** No hay lista blanca ni proceso de aprobación (§6).

Puesto al lado del criterio de Awakened PoE Trade, el diseño actual sale bien parado:

| Criterio | Nuestro diseño | d4lf | Diablo4Companion | TurboHUD4 (prohibido) |
|---|---|---|---|---|
| Lee memoria del proceso | No | No | No | Sí |
| Inyecta código en el juego | No | **DLL cargada por el juego** (accesibilidad) | No | Sí |
| Dibuja sobre el juego | **No, ventana propia** | Overlay | **Sí, overlay** | Sí |
| Automatiza entradas | No | **Sí, mueve objetos del alijo** | No | Sí |
| Atajos globales | `RegisterHotKey` (API oficial, no hook) | (no verificado) | (no verificado) | — |

Tres de las cuatro casillas que nos separan de las herramientas que se citan en los hilos de baneo
son decisiones ya tomadas en el diseño actual. La cuarta —el sondeo continuo cada 0,7 s frente a
"una acción por pulsación"— es la que yo cambiaría.

---

## 6. Lo que hay que copiar, concretamente

1. **Separar el parser del resto** como hizo HearthSim con `python-hslog`: librería sin UI, con
   fixtures de texto crudo de OCR, testeable sin juego ni tkinter. Ya lo pide el vocabulario cerrado;
   esto lo convierte en arquitectura.
2. **Pasar de sondeo continuo a captura bajo atajo**, adoptando el criterio "una acción por
   pulsación" de Awakened PoE Trade. Ya tenemos `RegisterHotKey`. Resuelve a la vez legalidad
   percibida, CPU y la trampa de latencia de §3.7.
3. **Localizar y trocear el tooltip antes del OCR**, no lanzar el motor contra la pantalla entera
   (`--find-tooltip` de d4-item-tooltip-ocr; bordes + viñetas de diablo4trading-ocr).
4. **Medir el ciclo completo antes de fijar cualquier intervalo.** Hay un proyecto equivalente que
   confiesa 1–3 s por captura. Si nuestro ciclo no cabe muy por debajo de 700 ms, el número es
   ficción.
5. **Banco de pruebas propio winocr vs Tesseract sobre capturas reales de tooltips en español.**
   Nadie ha publicado esa comparativa; es un hueco, no un dato heredable.
6. **Salida JSON estructurada del parser** (nombre, tipo, poder, afijos con valor, aspecto,
   engarces), como d4-item-tooltip-ocr. Encaja con los perfiles "yo"/"rival" ya previstos.
7. **Escribir en el README la sección "de dónde salen los datos y de dónde no"**, citando: (a) que el
   GEP de Overwolf para D4 no expone objetos, (b) que la vía TTS se descarta a propósito, (c) que el
   aviso de Blizzard de 2023 apunta a software que automatiza o modifica, y (d) que la herramienta no
   dibuja, no inyecta y no automatiza. Es el equivalente de la FAQ de Awakened PoE Trade, y es lo que
   distingue un proyecto de buena fe de uno que espera no ser mirado.
8. **Tratar la fuente de captura como versionada, igual que el manifiesto de parche.** Riot avisa de
   que su API puede cambiar sin preaviso; Blizzard rompió los lectores de terceros en la Temporada 12
   y cortó el combat log de los addons de WoW en el 12.0.0. Un cambio de fuente o tamaño del tooltip
   es nuestro equivalente: hace falta una prueba de humo que falle en cerrado cuando el OCR deja de
   reconocer el layout.

---

## Fuentes

Páginas abiertas y leídas para este informe:

- https://github.com/HearthSim/Hearthstone-Deck-Tracker
- https://hearthsim.info/blog/fast-hearthstone-log-parsing/
- https://github.com/jleclanche/fireplace/wiki/How-to-enable-logging
- https://developer.riotgames.com/docs/lol
- https://github.com/DestinyItemManager/DIM
- https://warcraft.wiki.gg/wiki/Patch_12.0.0/API_changes
- https://github.com/thequantumfalcon/spirescope
- https://snosme.github.io/awakened-poe-trade/faq
- https://github.com/SnosMe/awakened-poe-trade
- https://dev.overwolf.com/ow-native/live-game-data-gep/supported-games/diablo-4/
- https://github.com/josdemmers/Diablo4Companion
- https://github.com/d4lfteam/d4lf
- https://github.com/mxtsdev/d4-item-tooltip-ocr
- https://github.com/mivuorin/d4-ocr
- https://github.com/wenqu/diablo4trading-ocr
- https://github.com/josdemmers/D4TTS
- https://us.forums.blizzard.com/en/d4/t/a-notice-regarding-unauthorized-game-modifying-software-in-diablo-iv/102121
- https://us.forums.blizzard.com/en/d4/t/3rd-party-screen-readers-no-longer-function-in-season-12/242596

Repos citados desde resultados de búsqueda pero **no abiertos uno a uno** (existencia y descripción
vistas en los resultados; no verifiqué estrellas ni README):
`github.com/HearthSim/python-hslog`, `github.com/bossNilac/Open-League-Overlay`,
`github.com/Plutokekz/LeagueClientLiveDataApi`, `github.com/DestinyItemManager/bungie-api-ts`,
`github.com/DestinyItemManager/dim-api`, `github.com/m-mizutani/wowclp`,
`github.com/modargo/RunHistoryPlus`, `github.com/colinking/runlogger`,
`github.com/MaT1g3R/sts-stat-tracker`, `github.com/jfd02/TFT-OCR-BOT`, `github.com/dkager/tolk`.

---

## No encontrado

- **API pública de Blizzard para inventario/personaje de Diablo IV.** No encontré nada equivalente a
  la API de Bungie.net. No puedo afirmar categóricamente que no exista; sí puedo afirmar que ninguna
  de las herramientas de D4 que he abierto la usa, y que todas recurren a OCR o a la capa de
  accesibilidad.
- **Lista blanca o proceso de aprobación de Blizzard para herramientas de terceros.** No aparece en
  el aviso oficial de 2023 ni en ningún otro sitio que haya abierto.
- **Postura oficial de Blizzard, posterior a julio de 2023, específicamente sobre filtros de botín u
  overlays de sólo lectura.** Hay hilos de comunidad preguntándolo (incluido uno titulado "On the
  legality of 3rd party loot filters"); no abrí ninguno con respuesta azul, y el aviso más reciente
  que sí verifiqué es el de PezRadar de 26-jul-2023.
- **Ningún proyecto público que use `winocr` / `Windows.Media.Ocr` para tooltips de Diablo IV.** Los
  cuatro que encontré usan Tesseract (×2), tesseract.js o PaddleOCR. La comparativa de precisión
  winocr vs Tesseract sobre esta fuente concreta no existe publicada.
- **Cómo obtiene Overwolf técnicamente los eventos de D4.** La página de eventos de D4 no lo explica;
  la documentación general habla de captura gráfica DX/OpenGL y de acuerdos con publishers, pero no
  detalla si hay ganchos en el proceso. No puedo afirmar que sea un método que nosotros pudiéramos
  replicar legalmente.
- **Si el fallo de lectores de pantalla de terceros de la Temporada 12 se ha arreglado.** El hilo que
  leí (abierto en torno al 11-mar-2026) sólo contiene el reporte inicial, sin respuesta oficial.
- **Licencia exacta de Hearthstone Deck Tracker.** El contenido que obtuve indicaba "All Rights
  Reserved"; no lo doy por bueno sin ver el fichero LICENSE.
- **Lenguaje de D4TTS y de Open-League-Overlay**, y estrellas de varios repos citados sólo desde
  resultados de búsqueda.
- **Tesseract vs winocr en español.** Todos los proyectos de D4 que verifiqué trabajan en inglés o no
  especifican idioma; el modelo entrenado de d4-item-tooltip-ocr es `en_...`. El comportamiento del
  OCR con tildes y con el vocabulario de afijos en español de España es un riesgo sin arte previo.
