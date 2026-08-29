# Refutación adversarial: `crudo/arte-trackers.md`

**Fecha de verificación:** 29 de agosto de 2026
**Fichero auditado:** `investigacion/crudo/arte-trackers.md` (no modificado)
**Veredicto:** **PARCIAL** — el esqueleto aguanta; tres afirmaciones destacadas están mal calibradas
y el barrido de arte previo se dejó fuera el proyecto más parecido al nuestro.

---

## 0. Lo que sí aguanta (verificado, no concedido)

Antes de la parte incómoda, lo que resistió el ataque. **Los 20 repos citados existen** y las
estrellas coinciden con lo declarado (comprobado vía API de GitHub, 29-ago-2026):

| Repo | ★ declaradas | ★ reales | Lenguaje real | Licencia |
|---|---|---|---|---|
| `SnosMe/awakened-poe-trade` | 2,6 k | **2574** | TypeScript | MIT |
| `HearthSim/Hearthstone-Deck-Tracker` | 4,9 k | **4906** | C# | *(sin fichero LICENSE — ver §5)* |
| `josdemmers/Diablo4Companion` | 321 | **321** | C# | MIT |
| `d4lfteam/d4lf` | 206 | **206** | Python | MIT |
| `DestinyItemManager/DIM` | 2,2 k | **2156** | TypeScript | MIT |
| `mxtsdev/d4-item-tooltip-ocr` | 40 | **40** | Python | MIT |
| `mivuorin/d4-ocr` | 0 | **0** | C# | MIT |
| `wenqu/diablo4trading-ocr` | 1 | **1** | *(sin lenguaje)* | Apache-2.0 |
| `josdemmers/D4TTS` | 0 | **0** | **C#** ← *el informe lo daba por no verificado* | MIT |
| `thequantumfalcon/spirescope` | 26 | **26** | Python | MIT |
| `bossNilac/Open-League-Overlay` | — | 2 | **C++** ← *idem* | MIT |
| `jfd02/TFT-OCR-BOT` | — | 339 | Python | GPL-3.0 · **ARCHIVADO** |

Y las atribuciones de fuente de datos son correctas en todos los casos que comprobé uno a uno:
Diablo4Companion = **Tesseract + Emgu CV con overlay in-game** (confirmado en su README), 
d4-item-tooltip-ocr = **PaddleOCR con modelo propio**, d4-ocr = **Tesseract + PInvoke**,
d4lf = **TTS vía Tolk**, HDT = **`Power.log` en disco**. **No hay confusión OCR/portapapeles/memoria
en ninguna fila.** Las citas verbatim de Awakened PoE Trade y del aviso de PezRadar son exactas.

Confirmado además, y el informe se quedó corto: `FenrisDebug.txt` es log de sistema/TACT/`[CRASH]`;
el Ctrl+C de D4 es una **propuesta de foro**, no una función; el GEP de Overwolf para D4 expone
exactamente `gep_internal`, `game_info` (battlenet_tag, gold), `match_info` (in_pit, pit_tier,
pit_completed), `location` (x/y/z, map) y `me` (name, class, level, paragon_level, xp, health) —
**cero inventario, cero afijos**. Y las cuatro afirmaciones sobre WoW 12.0.0 (error al registrar
`COMBAT_LOG_EVENT`, `COMBAT_LOG_EVENT_INTERNAL_UNFILTERED` reservado, namespace `C_DamageMeter`,
razón declarada) están en la wiki tal cual.

---

## 1. REFUTADO — «la vía TTS se rompió»

**Lo que afirma el informe** (§3.6, pega *a*): *«Se rompió. […] desde el PTR y confirmado el
11-mar-2026, sin respuesta azul en el hilo»*, y de ahí la tabla §4: *«roto desde la Temporada 12
(11-mar-2026)»*.

**Lo que pasa de verdad:** el hilo existe y la fecha es correcta (cjshrader-1577, 11-mar-2026, sin
respuesta azul). Pero el informe leyó el hilo y **no leyó el desenlace**. El README de d4lf, cuyo
último push es de **ayer, 28-ago-2026**, abre la sección de instalación así:

> `### Installation and quick start guide (New instructions for season 12 that must be followed!)`

Es decir: **se rompió, y d4lf lo arregló**. El arreglo es precisamente el `install_dll.cmd` que el
informe cita sin darse cuenta de que es la solución al problema que declara sin resolver. La vía TTS
**funciona hoy**. Un proyecto de 206★ con actividad de ayer no vive de una fuente muerta.

> **Consecuencia para el diseño:** la razón (a) para descartar TTS desaparece. Las razones (b)
> —el binario corre dentro del proceso de Diablo— y la restricción dura «nada de inyección» **siguen
> siendo suficientes por sí solas** para descartarla. La decisión no cambia; el argumento que la
> sostiene sí, y publicarla apoyada en «está rota» es publicar algo falso que se cae solo en cuanto
> alguien abra el README de d4lf.

---

## 2. ENGAÑOSO — «la DLL debe ir firmada, dependencia de distribución»

**Lo que afirma el informe** (§3.6, pega *c*): *«La DLL tiene que estar firmada para que Diablo la
recoja, lo que añade una dependencia de distribución que un proyecto personal no quiere.»*

**Lo que dice la fuente** (README de d4lf, verbatim):

> "The TTS dll (`saapi64.dll`) must be signed for Diablo 4 to pick it up. The `install_dll.cmd`
> script handles all of this for you. It will: Copy the dll file to the Diablo 4 directory —
> Download the signtool needed to add a local signature to the dll — Runs the signtool and signs
> the dll"

La firma es **local y autofirmada**, generada en la máquina del usuario por un script incluido que
se descarga `signtool` y instala un certificado local. **No hay CA, no hay coste, no hay dependencia
de distribución.** La pega (c) es, en la práctica, un doble clic. Presentarla como barrera de
distribución infla el argumento.

---

## 3. ENGAÑOSO — el «AVISO DE LATENCIA» de 1–3 s está tomado del peor implementador posible

**Lo que afirma el informe** (§3.7 y recomendación 4): eleva a *dato duro* que d4-ocr *«admite 1-3
SEGUNDOS por captura»* y concluye que *«si nuestro ciclo no cabe muy por debajo de 700 ms, el número
es ficción»*.

**La cita es exacta.** El README de d4-ocr dice *"Currently it takes about 1-3 seconds to perform ocr
for screen capture"* y *"not performing fast enough to exceed experienced players reading speed"*.

**Pero la fuente no soporta la generalización.** `mivuorin/d4-ocr` tiene **0 estrellas**, último
commit **8-feb-2024** (abandonado hace 18 meses), y hace Tesseract contra captura de pantalla. Es el
peor caso disponible, elevado a cota inferior del problema.

**Contramedida encontrada (proyecto que el informe no vio):** `ferpgshy/d4forge` — Python, activo
(12-ago-2026), OCR sobre tooltips de D4 — usa **RapidOCR sobre onnxruntime** y **`mss`, exactamente
la librería de captura de nuestro diseño**. Su `d4forge/vision/ocr.py` documenta, medido:

> `1. cache   ~0.2 ms   linha identica ja' vista antes`
> `2. backend ~30-90 ms primeira vez que ve' aquela linha`

**30–90 ms por línea, 0,2 ms si ya la vio.** Dos órdenes de magnitud por debajo del «dato duro» del
informe. El propio fichero explica por qué el caché no falla: *el juego renderiza la misma línea con
exactamente los mismos píxeles*, así que un hash por contenido tiene cero falsos positivos, y los
rolls salen de un conjunto finito, con lo que el caché satura con el uso.

> **Consecuencia:** los 1–3 s son un artefacto de implementación, no un suelo físico del OCR sobre
> tooltips de D4. La recomendación 4 («medir el ciclo antes de fijar el intervalo») **es correcta y
> se mantiene**; lo que hay que retirar es el marco de «hay una trampa de latencia demostrada».
> Sondear a 0,7 s es perfectamente viable con el motor adecuado. El argumento para pasar a captura
> bajo atajo debe apoyarse en **legalidad percibida** (§4 de esta refutación), que es sólido, y no en
> latencia, que no lo es.

---

## 4. REFUTADO — «cuatro proyectos vivos», y falta el más parecido al nuestro

**Lo que afirma el informe** (§3.7): *«Cuatro proyectos vivos de OCR sobre tooltips de D4»*, y §4:
*«Cuatro proyectos públicos vivos con esta arquitectura»*.

**Últimos commits reales:**

| Proyecto | Último commit | ¿Vivo? |
|---|---|---|
| Diablo4Companion | **28-ago-2026** | Sí |
| d4-item-tooltip-ocr | **18-jul-2023** | No — 3 años |
| diablo4trading-ocr | **4-sep-2023** | No — 3 años |
| d4-ocr | **8-feb-2024** | No — 18 meses |

**Uno de cuatro está vivo.** Tres son arqueología. Importa porque el informe deriva de ellos
«la técnica compartida» del sector (§3.7) y una comparativa de motores: son decisiones tomadas
contra una versión del juego de 2023.

Y el barrido se dejó fuera proyectos activos de 2026. Búsqueda de repos en GitHub `diablo 4 ocr`:

| Proyecto | Último commit | Lenguaje | Fuente de datos |
|---|---|---|---|
| **`Goosterhof/horadric-cube`** | **25-ago-2026** | Rust (Tauri v2) + Vue/TS | **OCR de región bajo atajo global** |
| `ferpgshy/d4forge` | 12-ago-2026 | Python | OCR (RapidOCR/ONNX) + `mss`/`dxcam` — **automatiza el ciclo del Occultist** |
| `reikla/d4dps` | 8-may-2026 | PowerShell | Captura de pantalla + OCR |
| `NineO1/Scara-B-4` | 19-ene-2026 | JavaScript | OCR de estadísticas |

### 4.1 `horadric-cube` es el arte previo que este informe existía para encontrar

Es, punto por punto, el diseño que el informe **recomienda construir** — y ya está construido:

- **«Listens for a single hotkey»** (`Ctrl+Shift+H` global). Es la recomendación 2 del informe
  —«una acción por pulsación»— pero **con precedente en Diablo IV**, no prestada de Path of Exile.
  El informe la presenta como una idea trasplantada de otro juego; existe en el nuestro.
- **«Captures the configured tooltip region»**, no la pantalla entera. Es la recomendación 3.
- **Sección «The Horadrim's Oath»**, verbatim: *"No game memory access. No process injection. No
  network interception. No client modification."* Es literalmente la recomendación 7 («escribir en
  el README la sección de dónde salen los datos y de dónde no»), ya redactada por otro.
- Borra el PNG tras el OCR; sólo sale JSON parseado.

**Dos avisos que sólo se ven leyéndolo:** (1) manda el payload a un servidor remoto
(`horadrim.zmuuzn.nl`) — dependencia de red que nuestro diseño no tiene y no debería adquirir;
(2) su defensa legal es *«inherits its safe-harbor by design proximity»* con Diablo4Companion —
**eso no es un argumento jurídico, es una esperanza**, y conviene no copiarlo aunque sí copiemos la
arquitectura.

### 4.2 Contra-medición sobre el troceado del tooltip

La recomendación 3 del informe dice que trocear antes del OCR es «la técnica compartida». `d4forge`
midió lo contrario y lo dejó escrito en `ocr.py`:

> *«Ler a linha inteira de uma vez, e nao em pedacos. Uma versao que separava "valor" e "nome" para
> cachear cada metade ficou mais rapida e bem menos precisa — "+2 to Imbuement Skills" saiu como
> "to kil". Recortes pequenos confundem o detector de caixas.»*

Localizar el tooltip (recorte grueso) y trocear en fragmentos finos son cosas distintas: lo primero
está bien respaldado, lo segundo tiene una medición en contra. **La recomendación 3 hay que partirla
en dos**, no dejarla como un bloque.

Bonus del mismo fichero, directamente aplicable: binarizar + ampliar por repetición de píxel + margen
blanco, porque las variantes en escala de grises leían la marca de agua *«PUBLIC TEST BUILD»* junto
con el texto; y **marcar la lectura dudosa como dudosa y tratar la duda como "no tocar"** (fail-closed
en el parser, que encaja con la doctrina del proyecto).

---

## 5. Correcciones menores

- **`TFT-OCR-BOT` está ARCHIVADO** (339★, GPL-3.0). El informe lo cita como frontera viva; es un
  repo congelado. No invalida el uso retórico, pero hay que decirlo.
- **Licencia de HDT:** el informe lo dejó en «No encontrado» y hace bien — la API de GitHub devuelve
  **404 en `/license`**, o sea que el repo **no tiene fichero LICENSE reconocible**. Queda como no
  resuelto, ahora con evidencia de por qué.
- **`d4-item-tooltip-ocr` no captura pantalla.** Su interfaz es `--source-img=<fichero>`: procesa una
  imagen que le das. La columna «Captura: captura completa o recorte» de la tabla §3.7 le atribuye
  una capacidad que no tiene. Es una librería de OCR, no un capturador.
- **d4lf permite desactivar la automatización**: `Settings > Automation > Vision Mode Only`. La tabla
  §5 marca «Automatiza entradas: Sí» sin matiz; es *sí por defecto, con interruptor oficial*.
- **d4lf exige juego en inglés** (*"Game Language must be English"*). El informe lo echa en falta en
  «No encontrado» sin haberlo visto en el README que sí abrió. Refuerza el hueco del español.
- **Sobre la API de D4**, el informe dice «no puedo afirmar categóricamente que no exista». Ahora se
  puede afirmar algo más: en el foro de API de Blizzard, un moderador responde *«there is no d4 api
  yet we have had no announcement for one yet»*, y el D4Armory que circula tiene fuente **desconocida
  y sospechada de ingeniería inversa** — no es una vía utilizable.

---

## 6. Lo que hay que cambiar en el informe crudo

1. **Retirar «la vía TTS está rota».** Sustituir por: se rompió en la Temporada 12, d4lf publicó un
   procedimiento nuevo y funciona; se descarta por la razón (b), que basta sola.
2. **Retirar la pega de la firma como barrera.** Es una autofirma local automatizada.
3. **Degradar el «AVISO DE LATENCIA»** de dato duro a anécdota de un repo abandonado de 0★, y
   contraponer los 30–90 ms/línea medidos de d4forge. Mantener la recomendación de medir.
4. **Corregir «cuatro proyectos vivos» → uno vivo y tres abandonados**, y añadir los cuatro activos
   de 2026.
5. **Añadir `horadric-cube` como arte previo principal**, y reetiquetar las recomendaciones 2, 3 y 7
   de «trasplante desde PoE» a «patrón ya existente en D4», con el aviso de no heredar su
   argumentación legal por proximidad.
6. **Partir la recomendación 3** en «localizar el tooltip» (respaldado) y «trocear fino» (con
   medición en contra).
7. Corregir la fila de d4-item-tooltip-ocr (no captura), la de d4lf (automatización desactivable,
   requiere inglés) y marcar TFT-OCR-BOT como archivado.

**Lo que NO hay que tocar:** la tesis central. No hay API de D4, no hay API local, no hay addons, no
hay log de gameplay, no hay portapapeles, y el GEP de Overwolf —única vía con acuerdo de publisher—
no expone un solo afijo. Captura + OCR sigue siendo el único peldaño en pie, y la comparativa de §5
frente a TurboHUD4 sigue saliendo bien. El informe acierta en el mapa y falla en cuatro coordenadas.

---

## Fuentes de esta refutación

Abiertas y leídas el 29-ago-2026:

- https://dev.overwolf.com/ow-native/live-game-data-gep/supported-games/diablo-4/
- https://github.com/d4lfteam/d4lf y https://raw.githubusercontent.com/d4lfteam/d4lf/main/README.md
- https://us.forums.blizzard.com/en/d4/t/3rd-party-screen-readers-no-longer-function-in-season-12/242596
- https://snosme.github.io/awakened-poe-trade/faq
- https://raw.githubusercontent.com/mivuorin/d4-ocr/master/README.md
- https://raw.githubusercontent.com/josdemmers/Diablo4Companion/master/README.md
- https://raw.githubusercontent.com/mxtsdev/d4-item-tooltip-ocr/master/README.md
- https://raw.githubusercontent.com/Goosterhof/horadric-cube/main/README.md
- https://github.com/ferpgshy/d4forge — `requirements.txt` y `d4forge/vision/ocr.py`
- https://us.forums.blizzard.com/en/d4/t/a-notice-regarding-unauthorized-game-modifying-software-in-diablo-iv/102121
- https://us.forums.blizzard.com/en/blizzard/t/diablo-4-api-d4armory/45191
- https://warcraft.wiki.gg/wiki/Patch_12.0.0/API_changes
- https://github.com/jleclanche/fireplace/wiki/How-to-enable-logging
- https://us.forums.blizzard.com/en/d4/t/copy-paste-item-information-feature-proposal/137085
- API de GitHub (`repos/*`, `search/repositories`, `search/code`) para estrellas, lenguaje, licencia,
  estado de archivo y fecha de último commit de los 20 repos.

## No resuelto tras la verificación

- **Licencia de Hearthstone Deck Tracker.** GitHub devuelve 404 en el endpoint de licencia.
- **Motor OCR y latencia de `winocr` sobre tooltips de D4 en español.** Búsqueda de código en GitHub
  para `winocr+diablo`, `Windows.Media.Ocr+diablo` y `OcrEngine+diablo+tooltip`: **0 resultados en
  los tres**. El hueco que declara el informe es real y queda confirmado.
- **Si el fallo de lectores de terceros tuvo respuesta oficial.** Sigue sin haberla en el hilo; lo
  que hay es la solución no oficial de d4lf.
- **Mecanismo técnico del GEP de Overwolf en D4.** La documentación general describe un SDK que
  **el propio juego integra** (DLL incluida por el desarrollador), lo que apunta a integración del
  lado del publisher, no replicable por nosotros. No hay página que lo confirme para D4 en concreto.
