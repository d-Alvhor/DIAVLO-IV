# El arte previo de Path of Exile: de dónde sacan los datos las herramientas open source

> Investigación de campo sobre el ecosistema de herramientas de PoE/PoE2, con el foco puesto en
> **la fuente de datos** de cada una. Todo lo que aquí se afirma sobre implementación está leído
> del código fuente en GitHub, no de reseñas ni de wikis.
>
> Fecha de la investigación: 29 de agosto de 2026.

---

## 0. Resumen ejecutivo (lo que cambia el diseño de DIAVLO IV)

Hay **un solo hecho** que explica el 90 % de la diferencia entre el ecosistema de PoE y lo que
podemos hacer en Diablo IV:

**Path of Exile copia el objeto bajo el cursor al portapapeles como texto plano cuando pulsas
Ctrl+C.** Es una función del juego, no un truco. CONFIRMADO desde dos ángulos independientes:

1. La FAQ oficial de Awakened PoE Trade lo declara como el mecanismo único de la app:
   > "When you press Ctrl + C Path of Exile copies the item's text (under cursor, if any) to the
   > clipboard. All that remains is to parse text in Awakened PoE Trade and show to you in a fancy way."
   — <https://snosme.github.io/awakened-poe-trade/faq>

2. El código de PoE Overlay envía literalmente esa combinación y lee el resultado:
   `this.keyboard.keyTap(KeyCode.VK_KEY_C, copyAdvancedText ? ['control', 'alt'] : ['control'])`
   — [`item-clipboard.service.ts`](https://github.com/PoE-Overlay-Community/PoE-Overlay-Community-Fork/blob/master/src/app/shared/module/poe/service/item/item-clipboard.service.ts)

Y hay una **segunda** combinación, **Ctrl+Alt+C**, que copia el "advanced mod description": el mismo
objeto pero con los afijos anotados con su tipo (prefijo/sufijo), su nombre de mod, su *tier* y el
rango del roll. Es decir: el juego regala gratis la información que en DIAVLO IV tendríamos que
inferir. Confirmado por el issue de Path of Building sobre "Copying an item (ctrl+alt+c)"
(<https://github.com/PathOfBuildingCommunity/PathOfBuilding/issues/6124>) y por el parser dedicado
[`advanced-mod-desc.ts`](https://github.com/SnosMe/awakened-poe-trade/blob/master/renderer/src/parser/advanced-mod-desc.ts).

**Consecuencia dura:** el ecosistema de PoE es maduro no porque sus desarrolladores sean mejores,
sino porque **no tienen el problema de captura**. Toda su ingeniería está en el *parser*, la
*localización* y los *datos*. Y esas tres cosas sí son copiables tal cual a DIAVLO IV.

La segunda conclusión, incómoda: **OCR sí existe en este ecosistema**, pero solo como *parche* para
las tres o cuatro pantallas donde el Ctrl+C no funciona. Awakened PoE Trade y Exiled Exchange 2
distribuyen un archivo aparte de 6 MB con `tesseract-core-simd.wasm` y `eng.traineddata` para eso.
Nadie lo usa como vía principal si tiene alternativa.

---

## 1. Tabla maestra de herramientas

| Herramienta | Repo | ⭐ | Lenguaje | **Fuente de datos** | Nota |
|---|---|---|---|---|---|
| **Awakened PoE Trade** | [SnosMe/awakened-poe-trade](https://github.com/SnosMe/awakened-poe-trade) | 2.574 | TypeScript (Electron + Vue) | **Portapapeles** (envía Ctrl+C / Ctrl+Alt+C y lee el texto). **OCR (Tesseract WASM + OpenCV)** solo para el botín de Heist. API pública de trade para precios | La referencia del sector. MIT. Vivo (último push 28-ago-2026) |
| **Exiled Exchange 2** | [Kvan7/Exiled-Exchange-2](https://github.com/Kvan7/Exiled-Exchange-2) | 1.161 | TypeScript | Igual que APT (es un fork directo) | Fork para PoE 2. **Incluye español**. Vivo (28-ago-2026) |
| **PoE Overlay (original)** | [Kyusung4698/PoE-Overlay](https://github.com/Kyusung4698/PoE-Overlay) | 693 | TypeScript (Angular + Overwolf) | **Portapapeles** (`plugins/src/clipboard/Clipboard.cs`, DLL nativa) | Último push abr-2022. De facto muerto |
| **PoE Overlay Community Fork** | [PoE-Overlay-Community/PoE-Overlay-Community-Fork](https://github.com/PoE-Overlay-Community/PoE-Overlay-Community-Fork) | 491 | TypeScript (Angular + Electron) | **Portapapeles** + **fichero de log `Client.txt`** (susurros y trade) | Se bifurcó para no depender de Overwolf. Vivo (ago-2026) |
| **Poe Lurker** | [C1rdec/Poe-Lurker](https://github.com/C1rdec/Poe-Lurker) | 606 | C# (.NET 8, WPF) | **`Client.txt` / `KakaoClient.txt`** vía *file watcher* + **portapapeles por evento** (`SharpClipboard`) | Gestor de trade, no de builds. Push may-2026 |
| **MercuryTrade** | [Exslims/MercuryTrade](https://github.com/Exslims/MercuryTrade) | 496 | Java | **Solo `Client.txt`** — el propio proyecto dice que es "the only way to get data from Path of Exile" | Sin mantenimiento desde 2022 |
| **PoE-TradeMacro** | [PoE-TradeMacro/POE-TradeMacro](https://github.com/PoE-TradeMacro/POE-TradeMacro) | 918 | AutoHotkey | **Portapapeles** | El abuelo del ecosistema. Muerto desde 2021 (GPL-3.0) |
| **poe-itemtext-parser** | [klayveR/poe-itemtext-parser](https://github.com/klayveR/poe-itemtext-parser) | 6 | TypeScript | **Solo parser**: recibe el texto del portapapeles, devuelve JSON | Librería pura, sin captura. Útil como referencia de esquema |
| **poe-dat-viewer** | [SnosMe/poe-dat-viewer](https://github.com/SnosMe/poe-dat-viewer) | 107 | TypeScript | **Ficheros `.dat` / `.csd` del juego** | Herramienta *offline* de extracción. Es la que alimenta el vocabulario |
| **RuneHelper** | [Denzeriko/RuneHelper](https://github.com/Denzeriko/RuneHelper) | 13 | C++20 (OpenCV + Tesseract + ImGui) | **OCR puro sobre región de pantalla** | El único con arquitectura igual a la nuestra. Ver §6 |
| **stashvision** | [darvid/stashvision](https://github.com/darvid/stashvision) | 19 | AutoHotkey | API de stash + visión sobre pestaña | Abandonado (feb-2023) |
| **oshabi** | [Vilsol/oshabi](https://github.com/Vilsol/oshabi) | 1 | Go | **OCR** de la estación de Harvest | **Archivado**. Interesante solo porque su OCR cubría *todos* los idiomas |

---

## 2. El formato del texto copiado, y por qué importa

El texto que PoE pone en el portapapeles es un documento estructurado por secciones separadas por
una línea de guiones. Del código de [`Parser.ts`](https://github.com/SnosMe/awakened-poe-trade/blob/master/renderer/src/parser/Parser.ts):

- La función `itemTextToSections()` **parte el texto por `"--------"`** y descarta secciones vacías.
- La primera sección (la "nameplate") lleva cabeceras con prefijo fijo: `Item Class: `, `Rarity: `.

Y esos prefijos están **localizados**. En español (fichero autogenerado de Exiled Exchange 2,
[`dataParser/output/es/client_strings.js`](https://github.com/Kvan7/Exiled-Exchange-2/blob/master/dataParser/output/es/client_strings.js)):

```js
RARITY_NORMAL: 'Normal',
RARITY_MAGIC:  'Mágico',
RARITY_RARE:   'Raro',
RARITY_UNIQUE: 'Único',
RARITY:        'Rareza: ',
ITEM_CLASS:    'Clase de objeto: ',
ITEM_LEVEL:    'Nivel de objeto: ',
QUALITY:       'Calidad: ',
PHYSICAL_DAMAGE: 'Daño físico: ',
ARMOUR:        'Armadura: ',
EVASION:       'Evasión: ',
ENERGY_SHIELD: 'Escudo de energía: ',
CORRUPTED:     'Corrupto',
```

**Esto es exactamente el diccionario que DIAVLO IV necesita construir a mano para el tooltip
español de Diablo IV.** La forma del fichero (constantes con nombre canónico en inglés → cadena
localizada) es directamente copiable.

### 2.1. Arquitectura del parser: cadena de parsers, no regex monolítica

`Parser.ts` (36 KB) **no** es una expresión regular gigante. Es una **cadena de parsers** donde cada
uno declara su resultado con un tipo cerrado:

```ts
type SectionParseResult = 'SECTION_PARSED' | 'SECTION_SKIPPED' | 'PARSER_SKIPPED'
```

`parseClipboard()` recorre la lista de parsers contra las secciones restantes:
- `SECTION_PARSED` → la sección se consume y desaparece de la lista.
- `SECTION_SKIPPED` → esta sección no es para este parser, se sigue probando.
- `PARSER_SKIPPED` → este parser no aplica a este tipo de objeto en absoluto.

Hay ~50 parsers especializados (`parseGem`, `parseWeapon`, `parseArmour`, `parseMap`,
`parseModifiers`, `parseInfluence`, `parseHeistContract`, `parseLogbookArea`, `parseMercenary`…) más
"parsers virtuales" que operan sobre el estado completo del objeto sin consumir secciones
(`type VirtualParserFn = (item: ParserState) => Result<never, string> | void`).

Las regex existen, pero **acotadas**: se usan para extraer números de una línea ya identificada
(`_$.MAP_TIER.exec()`), no para reconocer la línea. Los rangos numéricos se sacan partiendo por
separadores conocidos: `line.slice(_$.PHYSICAL_DAMAGE.length).split('-').map(str => parseInt(str, 10))`.

**Lección de diseño:** identificar la línea por *prefijo del vocabulario cerrado*, extraer el número
por *regex pequeña*. Nunca al revés.

### 2.2. Lo que no se entiende, se declara

En [`ParsedItem.ts`](https://github.com/SnosMe/awakened-poe-trade/blob/master/renderer/src/parser/ParsedItem.ts)
el modelo de datos tiene un campo explícito:

```ts
unknownModifiers: Array<{ text: string, type: ModifierType }>
rawText: string
```

No tiran las líneas que no reconocen: las guardan aparte **y guardan el texto crudo entero**. Un
parser de vocabulario cerrado que descarta en silencio lo que no conoce miente sin que nadie se
entere. Este no.

---

## 3. Cómo se traduce texto → afijo canónico (el corazón del asunto)

De [`stat-translations.ts`](https://github.com/SnosMe/awakened-poe-trade/blob/master/renderer/src/parser/stat-translations.ts)
y del esquema en [`interfaces.ts`](https://github.com/Kvan7/Exiled-Exchange-2/blob/master/renderer/src/assets/data/interfaces.ts).

El vocabulario vive en ficheros de datos **NDJSON, un afijo por línea**, uno por idioma
(`renderer/public/data/{en,ru,ko,cmn-Hant}/stats.ndjson` en APT; en Exiled Exchange 2 además
`de, es, fr, ja, pt`). El fichero español de PoE2 tiene **1.934 líneas**. Un ejemplo real:

```json
{"ref": "# Charm Slot", "better": 1,
 "matchers": [{"string": "# espacios para viales"},
              {"string": "# espacio para viales", "value": 1}],
 "trade": {"ids": {"explicit": ["explicit.stat_2582079000"]}},
 "id": "num_charm_slots"}
```

Esquema (TypeScript real del repo):

```ts
export interface StatMatcher {
  string: string       // texto mostrado, con '#' donde va el número
  advanced?: string
  negate?: true        // el texto dice lo contrario: invertir el signo
  value?: number       // el número está incrustado en el texto (singular/plural)
  oils?: string
}

export enum StatBetter {
  NegativeRoll = -1,   // menos es mejor
  PositiveRoll  =  1,  // más es mejor
  NotComparable =  0,  // no se puede comparar
}

export interface Stat {
  ref: string          // identidad canónica, en inglés, estable entre idiomas
  dp?: true            // el valor lleva decimales
  matchers: StatMatcher[]
  better: StatBetter
  trade: { inverted?: true, option?: true, count?: true, ids: {...} }
}
```

Cinco decisiones de diseño que valen oro:

1. **`ref` en inglés como identidad.** El idioma es una capa de presentación. Todo el código
   interno compara por `ref`, nunca por el texto que ve el jugador.
2. **`matchers` es una lista, no una cadena.** Un mismo afijo canónico tiene varias redacciones.
3. **`value` resuelve el singular/plural.** `"# espacio para viales"` con `value: 1` significa "esta
   redacción implica que el número es 1 aunque el texto no lo muestre como variable". El español
   tiene este problema exactamente igual que el inglés.
4. **`negate`** captura el par ganar/perder con un solo afijo canónico:
   ```json
   "matchers": [{"string": "Ganas # de vida cuando bloqueas"},
                {"string": "Pierdes # de vida cuando bloqueas", "negate": true}]
   ```
   Al hacer *match* con `negate`, el código invierte `stat.roll *= -1` y también los límites
   `bounds.min` / `bounds.max`.
5. **`better`** es un entero de tres valores. Es literalmente el signo que necesita cualquier
   comparador para saber si un número más alto es mejor. Ejemplo real con `better: -1`:
   `"#% de probabilidad de que te apliquen sangrado cuando recibes un impacto"`.

### 3.1. El truco del `#` y las permutaciones

Un problema fino que ya han resuelto: una línea como `+15 a la Fuerza (12-20)` tiene números que son
*el roll* y números que son *el rango*. `_statPlaceholderGenerator` usa esta regex para separarlos:

```
(?<value>(?<!\d|\))[+-]?\d+(?:\.\d+)?)(?:\((?<min>.[^)-]*)(?:-(?<max>[^)]+))?\))?
```

Y luego **genera permutaciones**: sustituye selectivamente cada número por `#` según un
`PLACEHOLDER_MAP`, y prueba cada combinación contra la tabla `STAT_BY_MATCH_STR_V2(matchStr)`. Si
ninguna combinación cabe en el límite, cae de vuelta al texto exacto sin marcadores.

Esto existe porque hay afijos donde el número **forma parte del nombre** del afijo y no es variable
("gana 3 cargas" vs "gana # cargas"). Es un caso que en Diablo IV también aparece.

### 3.2. Agregación: sumar afijos que se repiten

[`modifiers.ts`](https://github.com/SnosMe/awakened-poe-trade/blob/master/renderer/src/parser/modifiers.ts)
implementa `sumStatsByModType()`: agrupa por `(stat.ref, modifier.type)` y guarda **la lista de
fuentes**, no solo el total:

```ts
export interface StatCalculated {
  stat: Stat
  type: ModifierType
  sources: StatSource[]     // cada contribución, con su roll y sus min/max
}
```

`statSourcesTotal(sources, mode: 'sum' | 'max')` colapsa esas fuentes. **Guardar las fuentes y no
solo el total** es lo que permite explicarle al usuario de dónde sale el número. Es el mismo
requisito que tenemos con los "grupos de daño".

---

## 4. Idiomas: dos fuentes, ninguna adivinada

Esta es la parte que menos se parece a nuestro caso, y por eso es la más instructiva.

Exiled Exchange 2 tiene una carpeta `dataParser/` con un pipeline en Python
([`src/main.py`](https://github.com/Kvan7/Exiled-Exchange-2/blob/master/dataParser/src/main.py))
que **regenera el vocabulario entero desde dos fuentes oficiales**:

**Fuente A — los ficheros del juego.** `providers/game_api.py` no hace nada exótico: invoca un
binario externo.

```python
subprocess.run(["pathofexile-dat"], cwd=self.vendor_dir, check=True, shell=True)
```

`pathofexile-dat` es la CLI de [SnosMe/poe-dat-viewer](https://github.com/SnosMe/poe-dat-viewer), que
lee los `.dat`/`.csd` del juego. El `config.json` del vendor lista **24 ficheros
`data/StatDescriptions/*.csd`** (`stat_descriptions.csd`, `skill_stat_descriptions.csd`,
`character_panel_stat_descriptions.csd`…) y **9 traducciones**: `English, Russian, Korean,
Traditional Chinese, Japanese, German, Spanish, Portuguese, French`.

Es decir: **el juego lleva dentro las plantillas de texto de todos los afijos en todos los idiomas**,
y hay una herramienta pública que las extrae.

**Fuente B — la API oficial de trade, por idioma.** `providers/trade_api.py` descarga, para cada
dominio localizado, cuatro endpoints:

```python
LANG_URLS = { ENGLISH: "https://www.pathofexile.com",
              SPANISH: "https://es.pathofexile.com",
              GERMAN:  "https://de.pathofexile.com", ... }

TRADE_QUERY_URLS = ["/api/trade2/data/filters",
                    "/api/trade2/data/stats",
                    "/api/trade2/data/items",
                    "/api/trade2/data/static"]
```

`es.pathofexile.com/api/trade2/data/stats` devuelve la lista completa de afijos **en español, con su
id canónico**. GGG publica ese endpoint. Lo cruzan con la fuente A y sale el `stats.ndjson`.

**Cabeceras de los ficheros generados:** `// autogenerated file, do not edit`. Nada de vocabulario
escrito a mano — salvo excepciones marcadas explícitamente con `// [Manual]` (aparece en el
`client_strings.js` español para `RUNIC_WARD`).

---

## 5. El overlay, el teclado, y el mito del ban

### 5.1. Cómo dibujan encima del juego

De [`OverlayWindow.ts`](https://github.com/SnosMe/awakened-poe-trade/blob/master/main/src/windowing/OverlayWindow.ts):

```ts
import { OverlayController, OVERLAY_WINDOW_OPTS } from 'electron-overlay-window'
```

No es una ventana transparente "a pelo": el módulo `electron-overlay-window` **se engancha a la
ventana del juego** (`this.poeWindow.attach(this.window, windowTitle)`) siguiendo su posición y
tamaño. Alterna entre interactivo y *click-through* según `this.isInteractable`, y devuelve el foco
al juego con `OverlayController.focusTarget()`. Hay un manejador explícito para el caso
`'PoE is running with administrator rights'`.

Técnicamente: **es una ventana externa que se posiciona sobre el juego**, no inyección ni hook de
render. Ninguna de las herramientas serias toca el proceso del juego.

### 5.2. Teclado: aquí sí hacen lo que nosotros hemos descartado

Esta es la diferencia más importante entre APT y nuestro diseño, y hay que verla de frente. De
[`Shortcuts.ts`](https://github.com/SnosMe/awakened-poe-trade/blob/master/main/src/shortcuts/Shortcuts.ts):

- **Registro de atajos:** `globalShortcut.register(...)` de Electron — que por debajo en Windows es
  `RegisterHotKey`, la misma API que tenemos previsto usar.
- **Envío de teclas: SÍ lo hacen.** Con `uiohook-napi`:
  ```ts
  uIOhook.keyToggle(UiohookKey[key as UiohookKeyT], 'down')
  uIOhook.keyTap(UiohookKey.C)
  uIOhook.keyToggle(UiohookKey[key as UiohookKeyT], 'up')
  ```
  Con un detalle de cortesía: *"On non-Mac platforms, don't toggle keys that are already being
  pressed"* — no repite modificadores que el usuario ya tiene pulsados.

O sea: **APT automatiza una entrada** (sintetiza Ctrl+C hacia el juego). Nuestra restricción dura lo
prohíbe. No podemos copiar esta parte. Pero tampoco la necesitamos si no hay Ctrl+C que enviar.

### 5.3. Portapapeles: dos estrategias distintas

| | Awakened PoE Trade | Poe Lurker |
|---|---|---|
| Mecanismo | **Polling** tras enviar Ctrl+C | **Evento** del sistema (`SharpClipboard`, WM_CLIPBOARDUPDATE) |
| Cadencia | `POLL_DELAY = 48` ms | reactivo |
| Límite | `POLL_LIMIT = 500` ms, luego error | — |
| Restauración | Sí: `clipboard.writeText(textBefore)`; y `restoreShortly()` con `RESTORE_AFTER = 120` ms | `ClipboardHelper.ClearClipboard()` al arrancar |
| Validación | `isPoeItem()` — comprueba que el texto empieza por el prefijo localizado de clase de objeto (`"Item Class: "`, `"Класс предмета: "`, …) | filtra por tipo de contenido y por Shift pulsado |

Fuente: [`HostClipboard.ts`](https://github.com/SnosMe/awakened-poe-trade/blob/master/main/src/shortcuts/HostClipboard.ts),
[`ClipboardLurker.cs`](https://github.com/C1rdec/Poe-Lurker/blob/main/src/PoeLurker.Core/ClipboardLurker.cs).

Detalle relevante: APT hace *throttling* de la restauración del portapapeles porque escribir
demasiado rápido puede provocar desconexiones por *"Too many actions"*. Ese cuidado por no
sobrecargar al juego es la razón práctica de que no les baneen.

Y `isPoeItem()` es la guarda de sanidad: **antes de parsear nada, comprueba que el texto tiene la
pinta correcta**. Nosotros necesitamos el equivalente sobre la salida del OCR.

### 5.4. Qué dice GGG frente a lo que dice Blizzard

Aquí hay que ser precisos, porque la creencia popular ("GGG lo permite, Blizzard no") es **más
matizada de lo que parece**.

**Lo que GGG prohíbe por escrito** (Términos de uso, sección 7, verbatim —
<https://www.pathofexile.com/legal/terms-of-use-and-privacy-policy>):

- "Utilise any automated software or 'bots' in relation to your access or use of the Website,
  Materials or Services."
- "Modify or adapt (including through third parties and third-party tools) the game client or its
  data, other than in the normal course of PoE gameplay as permitted in accordance with the Licence."
- "Connect to the Servers through any software other than the authorised game client software."

**Lo que dice el staff de GGG en el foro** (hilo filtrado por respuestas de staff,
<https://www.pathofexile.com/forum/view-thread/3584808/filter-account-type/staff>) — verbatim:

- Recomiendan abstenerse de "programs that automates or does more than one action with a keystroke
  or mouse click".
- Y de cualquier cosa que "interacts with the game client to provide an advantage over other players
  or provide information that isn't normally visible".
- Y, crucialmente: "we cannot comment on the legality of third-party tools, as we aren't able to
  thoroughly and accurately check exactly how they work" / "we're unable to guarantee if a tool is
  allowed or would remain allowed in the future".

**Traducción sin adornos: GGG tampoco tiene lista blanca ni proceso de aprobación.** Su postura
formal es la misma que la de Blizzard: no aprobamos nada, no garantizamos nada. La diferencia real
es de **práctica**, no de derecho:

| | GGG / Path of Exile | Blizzard / Diablo IV |
|---|---|---|
| Lista blanca formal | **No** | No |
| Regla informal citable | Sí: "1 pulsación = 1 acción de servidor" | No encontrada |
| API pública documentada | **Sí** (<https://www.pathofexile.com/developer/docs/game>): perfiles, filtros de objetos, ligas, personajes, stashes, stash público, currency exchange, con OAuth 2.1 | No equivalente |
| Integración de terceros bendecida | **Sí**: Item Filters y el *Build Planner* de PoE2, "designed for players to import builds from third-party sources" | No |
| Ctrl+C sobre objeto | **Sí, función del juego** | Ver §"No encontrado" |
| Tolerancia observada | ~12 años, herramientas con millones de usuarios | Sin equivalente comparable |

Cómo se posiciona el propio APT (FAQ, verbatim): cumple los ToS si "does one server action per
button press and doesn't interact with the game client itself (injecting into the process, changing
the process memory aka cheats)"; y admite que **GGG no lo ha aprobado oficialmente**.

PoE Overlay (producto comercial) dice lo mismo con otras palabras: "follows Grinding Gear Games'
official third-party tool policy and has done so for over 5 years", reconociendo que GGG "doesn't
officially endorse third-party tools" (<https://www.poeoverlay.com/faq>).

**Lo aplicable a nosotros:** la línea que estas herramientas no cruzan es exactamente la nuestra —
nada de memoria, nada de inyección, nada de temporizadores, nada de secuencias. La única cosa que
ellos hacen y nosotros no podemos es sintetizar una tecla hacia el juego. Nuestra restricción es
**más estricta** que la de todo el ecosistema de PoE. Eso es defendible.

---

## 6. ¿Alguien usa OCR? Sí. Y merece un apartado propio

### 6.1. OCR como parche, en las herramientas serias

Awakened PoE Trade tiene `main/src/vision/` con cuatro ficheros:
`HeistGemFinder.ts`, `link-main.ts`, `link-worker.ts`, `utils.ts`, `wasm-bindings.ts`.

Lo que hace [`HeistGemFinder.ts`](https://github.com/SnosMe/awakened-poe-trade/blob/master/main/src/vision/HeistGemFinder.ts),
leído del código:

1. Toma una captura y la redimensiona.
2. **Template matching** con OpenCV compilado a WASM: `cv.matchTemplate()` con `cv.TM_CCOEFF_NORMED`
   contra una imagen de referencia `heist-lock.bmp` — busca el icono del candado.
3. Agrupa los puntos detectados (`findNonZeroWeights()`, `groupWeightedPoints()`, `findLines()`).
4. Recorta la región de interés, **convierte a HSV** para aislar el texto por color, y binariza.
5. Solo entonces llama a Tesseract: `tessApi.Recognize()`, **descartando resultados con confianza ≤ 30**.

Método: `ocrScreenshot()`. Es un pipeline de visión completo, no "una captura y a Tesseract".

**Por qué existe:** la propia FAQ de APT lista las pantallas donde el Ctrl+C no devuelve nada — "Divination Card stash tabs, Curio Display rewards (Heist), Kirac's map offers" — porque "the game
doesn't copy anything to clipboard when pressing Ctrl+C in these places". El OCR cubre justo ese
hueco.

**Cómo lo distribuyen:** *no viene en el instalador*. Hay una guía dedicada
(<https://snosme.github.io/awakened-poe-trade/ocr-guide>, y su gemela en Exiled Exchange 2) que pide
al usuario **descargar un archivo aparte de 6 MB** con la carpeta `cv-ocr`, que contiene
`eng.traineddata` y `tesseract-core-simd.wasm`. Solo inglés.

Y la guía de EE2 pone condiciones de uso muy explícitas: *"Both icons should be fully visible"* y
*"The text should not be occluded by health bar or other elements"*. Es decir: **el OCR es frágil y
lo saben**, y lo compensan con requisitos de encuadre en la documentación.

### 6.2. OCR como vía principal: RuneHelper

[Denzeriko/RuneHelper](https://github.com/Denzeriko/RuneHelper) — 13 ⭐, C++20, MIT, activo (jul-2026).
Es **la única herramienta encontrada cuya arquitectura es la nuestra**, y por eso es la más
instructiva pese a ser pequeña.

Pipeline, de su README:
1. El usuario **selecciona una región** de la pantalla arrastrando un rectángulo. Se guarda en la
   config; solo hay que rehacerlo si cambia la ventana, la escala de UI o la posición del menú.
2. Captura periódica de esa región (OpenCV).
3. Detección de filas de texto dentro de la región.
4. Cada fila se **recorta y binariza** antes de pasar a Tesseract.
5. **"Fuzzy matching for OCR mistakes"** — corrección difusa contra la lista conocida de nombres.
6. Precios desde caché local por liga, o de la API.
7. Overlay con ImGui junto a los objetos detectados.

Su descargo, textual: *"No game memory reading or injection"* — "does **not** inject into the game"
y "does **not** read game memory".

Limitaciones declaradas: Linux solo X11, sin Wayland.

**Aviso de honestidad:** el README dice "Path of Exile 2" en el título y en la descripción del repo,
pero luego habla repetidamente del *"Runeshape loot menu"*. No he podido resolver esa
contradicción; el proyecto puede ser una adaptación de una herramienta para otro juego. Tomar el
**pipeline** como referencia, no el dominio.

### 6.3. La lección de OCR, destilada

De las tres implementaciones (APT/Heist, EE2, RuneHelper) sale un patrón repetido:

1. **Nunca OCR sobre la pantalla entera.** Siempre una región: fijada por el usuario (RuneHelper) o
   localizada por *template matching* de un icono ancla (APT).
2. **Preprocesado agresivo antes de Tesseract**: redimensionar, convertir a HSV o escala de grises,
   aislar por color, binarizar. El texto sobre fondo de juego es el peor caso posible para un OCR.
3. **Umbral de confianza y descarte**: APT tira todo lo que baje de 30.
4. **Corrección difusa contra un vocabulario cerrado.** Esta es la clave: el OCR no tiene que
   acertar, tiene que acercarse lo suficiente a una entrada de una lista finita. El vocabulario
   cerrado no es solo el parser, **es también el corrector del OCR**.
5. **Documentar las condiciones de encuadre** en lugar de fingir robustez.

---

## 7. Qué copiaríamos, en concreto

Ordenado por relación valor/esfuerzo.

**1. El fichero de vocabulario con forma de `stats.ndjson`.** Un afijo por línea, con:
`ref` (identidad canónica), `matchers[]` (redacciones en español con `#`), `better` (−1/0/+1),
`negate`, `value` para singulares, `dp` para decimales. Es el formato exacto que necesita nuestro
parser de vocabulario cerrado, y ya viene con los casos raros resueltos. Esquema verificado en
[`interfaces.ts`](https://github.com/Kvan7/Exiled-Exchange-2/blob/master/renderer/src/assets/data/interfaces.ts).

**2. El `client_strings.js` español como plantilla del diccionario de tooltip.** Constantes con
nombre en inglés → cadena en español, con las marcadas a mano etiquetadas `// [Manual]`.

**3. `better: StatBetter` como campo de primera clase del afijo.** Nuestro valorador por grupos de
daño necesita, antes que nada, saber el signo. Que sea un enum de tres estados (y que exista
`NotComparable`) evita tener que inventar heurísticas para afijos que no se comparan.

**4. La cadena de parsers con `SECTION_PARSED / SECTION_SKIPPED / PARSER_SKIPPED`.** Sobre el texto
del OCR también hay secciones (nombre, tipo, stats base, afijos, aspecto). Un parser por concepto
que declara si consumió o no es infinitamente más depurable que una regex por objeto.

**5. `unknownModifiers[]` + `rawText`.** Guardar siempre el texto crudo y una lista explícita de
líneas no reconocidas. En nuestro caso vale doble: una línea no reconocida puede ser un afijo nuevo
*o* un fallo de OCR, y hay que poder distinguirlo mirando el crudo.

**6. La guarda `isPoeItem()` antes de parsear.** Equivalente nuestro: no aceptar una lectura de OCR
que no empiece por un patrón de tooltip válido de Diablo IV en español. Barato y evita basura.

**7. Del OCR: región acotada + preprocesado + umbral de confianza + fuzzy matching contra el
vocabulario cerrado.** Los cuatro, no tres. En particular el punto 4: **usar el vocabulario cerrado
como corrector del OCR**, no solo como parser. Eso convierte una debilidad (OCR impreciso) en un
sistema con red.

**8. `sumStatsByModType()` guardando `sources[]`.** Para poder decirle al jugador "este 34 % sale de
tres sitios" en vez de solo el total. Es exactamente lo que pide nuestro modelo de grupos de daño.

**9. La política de no cargarse el portapapeles del usuario** (si en algún momento lo tocamos):
guardar, usar, restaurar, con *throttling*.

**10. La posición pública ante la EULA, redactada como ellos.** Enunciar en el README qué NO hace la
herramienta: no lee memoria, no inyecta, no automatiza entradas, no envía nada al servidor. La
formulación de RuneHelper y la FAQ de APT son buenos modelos. Y **no** afirmar que está aprobada:
ni siquiera APT lo hace.

**Lo que NO copiamos, y conviene dejarlo escrito:**

- El envío sintético de teclas (`uiohook-napi keyTap`). Viola nuestra restricción dura.
- El overlay enganchado con `electron-overlay-window`. Viola nuestra restricción dura.
- El pipeline de datos desde ficheros del juego (`pathofexile-dat`) — leer los ficheros de Diablo IV
  sería "modificar o adaptar los datos del cliente" y, además, no consta que exista herramienta.
- La dependencia de una API pública de datos localizados. No existe equivalente.

---

## Fuentes

Páginas y ficheros abiertos de verdad durante esta investigación.

**Repositorios y código fuente**
- <https://github.com/SnosMe/awakened-poe-trade>
- <https://github.com/SnosMe/awakened-poe-trade/blob/master/renderer/src/parser/Parser.ts>
- <https://github.com/SnosMe/awakened-poe-trade/blob/master/renderer/src/parser/stat-translations.ts>
- <https://github.com/SnosMe/awakened-poe-trade/blob/master/renderer/src/parser/advanced-mod-desc.ts>
- <https://github.com/SnosMe/awakened-poe-trade/blob/master/renderer/src/parser/ParsedItem.ts>
- <https://github.com/SnosMe/awakened-poe-trade/blob/master/renderer/src/parser/modifiers.ts>
- <https://github.com/SnosMe/awakened-poe-trade/blob/master/main/src/vision/HeistGemFinder.ts>
- <https://github.com/SnosMe/awakened-poe-trade/blob/master/main/src/shortcuts/HostClipboard.ts>
- <https://github.com/SnosMe/awakened-poe-trade/blob/master/main/src/shortcuts/Shortcuts.ts>
- <https://github.com/SnosMe/awakened-poe-trade/blob/master/main/src/windowing/OverlayWindow.ts>
- <https://github.com/SnosMe/awakened-poe-trade/blob/master/DEVELOPING.md>
- <https://github.com/Kvan7/Exiled-Exchange-2>
- <https://github.com/Kvan7/Exiled-Exchange-2/blob/master/dataParser/README.md>
- <https://github.com/Kvan7/Exiled-Exchange-2/blob/master/dataParser/src/main.py>
- <https://github.com/Kvan7/Exiled-Exchange-2/blob/master/dataParser/src/providers/trade_api.py>
- <https://github.com/Kvan7/Exiled-Exchange-2/blob/master/dataParser/src/providers/game_api.py>
- <https://github.com/Kvan7/Exiled-Exchange-2/blob/master/dataParser/src/constants/urls.py>
- <https://github.com/Kvan7/Exiled-Exchange-2/blob/master/dataParser/data/vendor/config.json>
- <https://github.com/Kvan7/Exiled-Exchange-2/blob/master/dataParser/output/es/client_strings.js>
- <https://github.com/Kvan7/Exiled-Exchange-2/blob/master/dataParser/output/es/stats.ndjson>
- <https://github.com/Kvan7/Exiled-Exchange-2/blob/master/renderer/src/assets/data/interfaces.ts>
- <https://github.com/Kyusung4698/PoE-Overlay>
- <https://github.com/PoE-Overlay-Community/PoE-Overlay-Community-Fork>
- <https://github.com/PoE-Overlay-Community/PoE-Overlay-Community-Fork/blob/master/src/app/shared/module/poe/service/item/item-clipboard.service.ts>
- <https://github.com/C1rdec/Poe-Lurker>
- <https://github.com/C1rdec/Poe-Lurker/blob/main/src/PoeLurker.Core/ClientLurker.cs>
- <https://github.com/C1rdec/Poe-Lurker/blob/main/src/PoeLurker.Core/ClipboardLurker.cs>
- <https://github.com/Exslims/MercuryTrade>
- <https://github.com/PoE-TradeMacro/POE-TradeMacro>
- <https://github.com/klayveR/poe-itemtext-parser>
- <https://github.com/SnosMe/poe-dat-viewer>
- <https://github.com/Denzeriko/RuneHelper>
- <https://github.com/darvid/stashvision>
- <https://github.com/Vilsol/oshabi>
- <https://github.com/PathOfBuildingCommunity/PathOfBuilding/issues/6124>

**Documentación de las herramientas**
- <https://snosme.github.io/awakened-poe-trade/faq>
- <https://snosme.github.io/awakened-poe-trade/ocr-guide>
- <https://kvan7.github.io/Exiled-Exchange-2/ocr-guide>
- <https://www.poeoverlay.com/faq>

**Fuentes oficiales de Grinding Gear Games**
- <https://www.pathofexile.com/legal/terms-of-use-and-privacy-policy>
- <https://www.pathofexile.com/forum/view-thread/3584808/filter-account-type/staff>
- <https://www.pathofexile.com/forum/view-thread/3878010/page/1>
- <https://www.pathofexile.com/developer/docs/game>

**Diablo IV (contexto, sin resolver)**
- <https://us.forums.blizzard.com/en/d4/t/copy-paste-item-information-feature-proposal/137085>

---

## No encontrado

Cosas que he buscado y **no** he podido confirmar. Ninguna de ellas está rellenada con suposiciones.

1. **Si Diablo IV tiene hoy (ago-2026) algún Ctrl+C sobre objeto.** Solo he encontrado una
   *propuesta de función* en los foros de Blizzard (nov-2023), no una confirmación de que se
   implementara. **Es la pregunta más cara del proyecto**: si existiera, la arquitectura entera
   cambiaría y el OCR sobraría. Debe verificarse en pantalla, no por búsqueda.

2. **Un ejemplo verbatim del texto que PoE pone en el portapapeles.** Sé por el código que las
   secciones se separan con `"--------"` y que las cabeceras son `Item Class: ` / `Rarity: `, pero no
   he conseguido abrir una página que muestre un objeto copiado completo. La estructura está
   confirmada desde el código; el ejemplo literal, no.

3. **La sentencia exacta de Chris Wilson sobre "1 pulsación = 1 acción".** Circula muy citada
   ("Any macro that performs more than one action is bannable…") pero solo la he visto en resultados
   de búsqueda y foros de terceros. El hilo de Steam donde debería estar devolvió un aviso de
   contenido sin cuerpo. **La versión que sí he verificado en fuente primaria** es la del staff de
   GGG en su propio foro (hilo 3584808), citada en §5.4, que dice lo mismo con otras palabras.

4. **Configuración concreta de Tesseract** (valores de `psm`/`oem`, listas blancas de caracteres)
   en RuneHelper o en APT. Los README hablan de "single-pass OCR tuned for…" pero no publican los
   parámetros. Habría que leer el `.cpp` / los bindings WASM línea a línea.

5. **El algoritmo exacto de *fuzzy matching* de RuneHelper** (Levenshtein, trigramas, otra cosa) y su
   umbral. El README solo dice "Fuzzy matching for OCR mistakes".

6. **Cifras de usuarios de ninguna herramienta.** Solo tengo estrellas de GitHub, que no son
   usuarios. No he encontrado descargas verificables.

7. **Si Awakened PoE Trade tiene datos en español.** Los idiomas presentes en el repo principal son
   `en, ko, ru, cmn-Hant`. El español aparece en el fork Exiled Exchange 2 (PoE 2), no en APT (PoE 1).
   Y la FAQ de APT dice explícitamente: "No plans to support other languages".

8. **Una declaración oficial de GGG que mencione específicamente overlays o price-checkers.** El
   staff habla de automatización y de "información no visible normalmente"; **no nombra los overlays
   ni por bien ni por mal**. La tolerancia es observada, no escrita.

9. **La postura de Overwolf frente a GGG** (Kyusung4698/PoE-Overlay se construyó sobre Overwolf, que
   sí tiene acuerdos con algunas editoras). No he podido comprobar si existe acuerdo con GGG.

10. **Qué hace exactamente `stashvision`** (¿OCR, o solo API de stash + resaltado?). El repo lleva
    abandonado desde feb-2023 y no he abierto su código.
