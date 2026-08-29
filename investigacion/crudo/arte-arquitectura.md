# Arte previo: arquitectura de herramientas de escritorio para ARPG

**Dominio:** patrones de arquitectura (stack, ventana, hotkeys, captura, distribución).
**Fecha de la recogida:** 29 de agosto de 2026. Estrellas y fechas de *push* leídas de la API de GitHub ese día.
**Pregunta central que persigo en cada herramienta:** *de dónde saca los datos*.

---

## 1. Veredicto en una frase

El stack que tenemos (Python + tkinter + mss + winocr + RegisterHotKey) **es razonable y está
alineado con el arte previo en lo que más importa —la fuente de datos y la frontera legal—,
pero tiene dos piezas flojas: `tkinter` como GUI y `winocr` como dependencia huérfana**. Las dos
herramientas de Diablo IV más vivas que existen (`d4lf`, 206 ★, Python; `Diablo4Companion`, 321 ★,
C#/WPF) coinciden en usar **captura de pantalla + OCR + emparejamiento difuso contra un catálogo**,
y ninguna de las dos usa tkinter: una usa PyQt6 y la otra WPF. Ese es el cambio que yo haría.

---

## 2. Las herramientas reales, con su fuente de datos

### 2.1 Diablo IV

| Nombre | Repo | Lenguaje | ★ | **Fuente de datos** | Nota |
|---|---|---|---|---|---|
| **D4LF (Diablo 4 Loot Filter)** | https://github.com/d4lfteam/d4lf | Python (MIT), Python ≥3.14 | 206 | **Dos vías: (a) intercepción del TTS del juego** — sustituye la DLL `saapi64.dll` que Diablo IV carga para lectores de pantalla (motor Tolk) y le manda el texto por un *named pipe* `\\.\pipe\d4lf`; **(b) captura de pantalla con `mss` + visión por computador** | Vivo (push 28-ago-2026). PyQt6, OpenCV, `rapidfuzz`, `pynput`, `pywin32`, Selenium para importar builds. Se empaqueta con **PyInstaller `--onefile`**. Tiene `src/automation/` (mueve ratón, vende, mueve botín) y `src/overlay/` — **las dos cosas que nosotros hemos excluido** |
| **Diablo IV Companion** | https://github.com/josdemmers/Diablo4Companion | C# (MIT), `net10.0-windows` | 321 | **Captura de pantalla**: `Emgu.CV` (OpenCV) para *template matching* de iconos/afijos + **TesseractOCR 5.5.2** para el texto + `FuzzierSharp` para emparejar el texto sucio contra el catálogo | Vivo (push 28-ago-2026), v5.3.7. WPF + MahApps.Metro, `GameOverlay.Net` para el overlay, **`NHotkey.Wpf` para atajos globales**, Selenium para importar builds de webs. Tiene `README.esES.md` y recursos `esES`: **soporta cliente en español** |
| **d4-item-tooltip-ocr** | https://github.com/mxtsdev/d4-item-tooltip-ocr | Python (MIT) | 40 | **Imagen de tooltip → PaddleOCR con modelo de reconocimiento entrenado a medida para D4**; salida JSON (nombre, tipo, poder, afijos, aspectos, engarces) | **Abandonado**: último push 18-jul-2023. Interesante como prueba de que hubo que entrenar un modelo propio: la tipografía de D4 castiga al OCR genérico |
| **d4-ocr** | https://github.com/mivuorin/d4-ocr | C# (MIT) | 0 | Captura de pantalla + **Tesseract**, resalta stats buscados | Muerto (push feb-2024). Sirve solo como confirmación del patrón |
| **Diablo IV Item Comparator** | https://github.com/brianjleepub/diablo4_item_comparer | Python (sin licencia) | 0 | **Cámara física apuntando a la pantalla** → visión por computador → puntuación contra un modelo de prioridades de build | 0 ★ y sin tracción, pero su justificación es la mejor formulada del lote: dice evitar a propósito lectura de memoria, overlays e inspección de ficheros del juego, y que la captura por cámara lo hace inmune a cambios de anticheat. Es nuestra misma doctrina llevada al extremo paranoico |

### 2.2 Path of Exile (el ecosistema maduro; es de donde se copia todo)

| Nombre | Repo | Lenguaje | ★ | **Fuente de datos** | Nota |
|---|---|---|---|---|---|
| **Awakened PoE Trade** | https://github.com/SnosMe/awakened-poe-trade | TypeScript (MIT), Electron + Vue | 2.574 | **Portapapeles.** El juego copia el texto del objeto con Ctrl+C; la app lo parsea. Sin OCR, sin memoria | La referencia del sector. `libuiohook` para el input global. Su FAQ es la formulación canónica de la frontera: es seguro si cumple el ToS, hace *una acción de servidor por pulsación* y **no interactúa con el cliente del juego (ni inyección ni memoria)** |
| **Exiled Exchange 2** | https://github.com/Kvan7/Exiled-Exchange-2 | TypeScript (MIT) | 1.161 | Fork del anterior, para PoE 2. Portapapeles | Se distribuye como **instalador `.exe`** (`Exiled-Exchange-2-Setup-0.15.8.exe`) desde web propia + GitHub Releases, con aviso explícito de no descargarlo de otro sitio |
| **Chaos Recipe Enhancer** | https://github.com/ChaosRecipeEnhancer/ChaosRecipeEnhancer | C# (GPL-3.0), .NET + WPF | 514 | **API oficial del juego con OAuth.** Lee el alijo desde los servidores de GGG, no de la pantalla | El caso ideal: cuando el juego te da API, no hay OCR que valga. Usa **Velopack** (2.297 ★) para instalador + autoactualización |
| **Path of Building Community** | https://github.com/PathOfBuildingCommunity/PathOfBuilding | Lua | 5.425 | **Pegado manual** del objeto desde el juego + importación de personaje desde la web/API | Se distribuye con **asistente de instalación y también zip portable**. Es el patrón "doble clic y funciona" mejor validado del ecosistema |

### 2.3 La plataforma que se salta el problema: Overwolf

- Overwolf (https://www.overwolf.com/browse-by-game/diablo-iv) aloja apps para Diablo IV y afirma
  trabajar con los editores para cumplir sus políticas de terceros.
- **Pero:** en el hilo oficial del foro de Blizzard sobre si los overlays están permitidos
  (https://us.forums.blizzard.com/en/d4/t/third-party-app-diablo-iv-overlay-is-permitted-modcheck/41715)
  **no hay respuesta de un azul**. Quien responde es un jugador veterano y un empleado de Overwolf.
  La cita del EULA que ahí se maneja es la misma que nos frena: software no autorizado que
  "cambie o facilite el gameplay". **No hay lista blanca ni aprobación formal.** El consenso del
  hilo es que la aplicación de la norma llega por oleadas de baneos, sin aviso.
- Conclusión operativa: **Overwolf no compra inmunidad**, compra ambigüedad. Y a cambio te ata a su
  runtime, su tienda y su modelo de anuncios. Para una herramienta de un solo usuario, no compensa.

---

## 3. Taxonomía de fuentes de datos, ordenada por riesgo

De más limpia a más sucia. Es la única tabla de este informe que de verdad decide la arquitectura.

| # | Fuente | Quién la usa | Riesgo EULA | Disponible para D4 |
|---|---|---|---|---|
| 1 | **API oficial del juego (OAuth)** | Chaos Recipe Enhancer | Nulo | **NO.** Ver §7 |
| 2 | **Portapapeles alimentado por el propio juego** | Awakened PoE Trade, Exiled Exchange 2, Path of Building | Nulo: el juego te da el texto | **NO.** D4 permite enlazar objetos en el chat con shift+clic, pero eso genera un enlace interno, no texto plano copiable |
| 3 | **Captura de pantalla + OCR** | D4LF, Diablo4Companion, d4-item-tooltip-ocr, d4-ocr | Bajo: solo lees píxeles que ya están en tu pantalla | **SÍ. Es la única vía real.** |
| 4 | **Cámara física** | diablo4_item_comparer | Nulo, pero absurdo | Sí, y no |
| 5 | **Interceptar el TTS / API de accesibilidad** | D4LF (`saapi64.dll`) | **Gris oscuro.** Es un punto de extensión documentado del juego, pero exige colocar una DLL propia que el proceso del juego carga | Sí. **Fuera de nuestra restricción dura** |
| 6 | Leer memoria / inyección | (no lo hace ninguna de las anteriores, y presumen de ello) | Prohibido | Descartado |

**Lectura:** nuestra decisión de ir por el 3 es la correcta y es la mayoritaria en D4. No es un apaño:
es lo que hacen las dos herramientas de D4 con tracción real. Y llegamos ahí porque los niveles 1 y 2
**no existen** en este juego, no por gusto.

---

## 4. Los stacks, comparados en lo que nos importa

| Stack | Ventana siempre visible | Atajos globales | Captura de pantalla | Distribución a no técnico | Peso | Pega principal |
|---|---|---|---|---|---|---|
| **Python + tkinter** | `attributes("-topmost", True)`, una línea | Vía `ctypes`/`pywin32` → `RegisterHotKey`, o `keyboard`/`pynput` (hook) | `mss`, `dxcam` | PyInstaller `--onefile` | ~30-60 MB | **DPI**: tkinter no es DPI-aware por defecto en Windows, sale borroso a 125/150%. Estética de 1998. Sin widgets de tabla decentes |
| **Python + PyQt6/PySide6** | `Qt.WindowStaysOnTopHint` | Igual que arriba (Qt no da hotkey global nativo) | Igual | PyInstaller, exe más gordo | ~80-120 MB | Licencia (PyQt6 = GPL/comercial; **PySide6 = LGPL**, que es la que quieres). Curva un poco mayor. **Es lo que eligió D4LF** |
| **Python + CustomTkinter** (13.524 ★) | Igual que tkinter | Igual | Igual | Igual | ~40 MB | Capa de pintura sobre tkinter: arregla el aspecto y **el escalado HiDPI**, no arregla los widgets que faltan |
| **C# / WPF (.NET)** | `Topmost="True"` | `NHotkey.Wpf` (envuelve `RegisterHotKey`) | `System.Drawing`, Emgu.CV, `GameOverlay.Net` | Publicación *self-contained single-file*; **Velopack** para instalador + autoactualización | 60-150 MB self-contained | Windows y punto. Ecosistema de OCR peor que Python **salvo** que uses `Windows.Media.Ocr`, que en C# es de primera clase. **Es lo que eligió Diablo4Companion** |
| **Electron (+ Vue/React)** | Trivial, `alwaysOnTop` | `globalShortcut` nativo, o `libuiohook` | `desktopCapturer` | Instalador `.exe` con electron-builder | **~150-250 MB** | Peso y RAM. Justificado si tu UI es rica y tu dato viene del portapapeles (APT). **Injustificado si tu dato viene de OCR**: acabas con un Chromium entero para dibujar una lista |
| **Rust + Tauri v2** (110.628 ★) | `alwaysOnTop`, `transparent` | `tauri-plugin-global-shortcut` | `tauri-plugin-screenshots` | Instalador pequeño | ~10-20 MB | **No he encontrado ningún compañero de juego real y con tracción escrito en Tauri.** Y el OCR tendrías que llamarlo a mano por WinRT. Riesgo de ser el primero |
| **AutoHotkey** | Sí | Su razón de ser | Limitada | Un `.ahk` o `.exe` compilado | Mínimo | **Descartado por doctrina**: AHK es exactamente el perfil que los anticheat vigilan, porque su uso normal es automatizar entradas. Aunque tú no automatices nada |
| **Overwolf** | Nativo, overlay real | Sí | Sí, con API del juego cuando la hay | Su tienda | — | Overlay dibujado encima = fuera de nuestra restricción dura |

---

## 5. Nuestro stack, pieza a pieza

| Pieza | Veredicto | Razón |
|---|---|---|
| **Ventana propia, sin overlay** | **Acertado, y es nuestra mejor baza** | D4LF y Diablo4Companion **sí** dibujan overlay. Nosotros no. Eso nos deja más limpios que el arte previo frente al EULA, sin perder casi nada: comparar dos objetos no exige estar encima del juego |
| **`mss` cada 0,7 s** | **Aceptable, con dos matices** | (a) `mss` (1.280 ★, vivo) es lo que usa D4LF, y lo usa **recortando a la ROI de la ventana del juego**, no capturando la pantalla entera, con caché por tiempo. Cópialo. (b) `mss` **no captura pantalla completa exclusiva** en DirectX: hay que exigir modo ventana sin bordes y decírselo al usuario en pantalla. (c) Si 0,7 s se queda corto, `dxcam` (798 ★, Desktop Duplication API) va a ~239 FPS frente a ~76 de `mss` según su propio banco de pruebas |
| **`winocr` (Windows.Media.Ocr)** | **La pieza más floja. Cambia la dependencia, no el motor** | El motor nativo de Windows es buena elección: gratis, rápido, sin modelo que empaquetar, y con paquete de idioma **español** del sistema. El problema es el envoltorio: `GitHub30/winocr` tiene **25 ★ y último push el 25-oct-2024**. Es un *wrapper* fino sobre `winrt-Windows.Media.Ocr`. **Recomendación: hablar con `winrt-Windows.Media.Ocr` directamente** y quedarnos las ~60 líneas de pegamento en nuestro repo. Una dependencia huérfana menos, y control sobre el bitmap. (Ojo: existe otro proyecto llamado `winocr` de `riddleling`, 14 ★, que es un CLI en Rust. No confundir) |
| **Parser de vocabulario cerrado** | **Cámbialo por catálogo + emparejamiento difuso** | Este es el hallazgo más accionable. **Las dos** herramientas de D4 hacen lo mismo y ninguna hace parser estricto: D4LF usa `rapidfuzz` con distancia de Levenshtein contra un `GameCatalog`, Diablo4Companion usa `FuzzierSharp` con un umbral de coincidencia configurable (por defecto 80%). Razón: el OCR **siempre** ensucia una letra, y un vocabulario cerrado convierte un fallo de OCR en un afijo perdido en silencio. El difuso lo convierte en un afijo correcto o en un aviso |
| **`RegisterHotKey`** | **Acertado, y mejor que el arte previo** | `RegisterHotKey` solo escucha las teclas que registras y recibe `WM_HOTKEY`; **no instala un hook global de teclado**. D4LF usa `pynput`, que en Windows sí instala hook de bajo nivel: intercepta *todo* el teclado. Nosotros estamos por encima en higiene. Mantenerlo |
| **tkinter** | **La otra pieza floja** | Nadie del arte previo lo usa. Y para nuestra UI concreta —checklist de 10+6, tabla comparativa de afijos, dos perfiles lado a lado— tkinter no tiene tabla nativa decente y sale borroso en pantallas escaladas. **PySide6 (LGPL) es el salto obvio**, y es la elección de D4LF (con PyQt6). Si el coste de reescribir asusta, **CustomTkinter** es el parche barato: arregla el HiDPI y el aspecto sin cambiar de mundo |
| **Perfiles en JSON** | Bien, sin más | Todo el mundo hace esto. D4LF usa YAML con Pydantic para validar; si el fichero lo va a tocar el usuario a mano, YAML + validación se lee mejor |

---

## 6. Qué copiaríamos, en concreto

1. **La ROI relativa a la ventana del juego** (`d4lf/src/perception/capture/core.py`): localizar la
   ventana de D4, guardar `top/left/width/height`, capturar solo eso, y guardar una clave de
   resolución tipo `"1920x1080"` para escalar coordenadas. Nosotros hoy capturamos pantalla.
2. **Emparejamiento difuso contra catálogo** en vez de vocabulario cerrado (`rapidfuzz`, umbral
   ajustable). Y **exponer el umbral en la UI**, como hace Diablo4Companion.
3. **Caché de captura con cerrojo y marca de tiempo**: no volver a capturar si han pasado menos de
   X ms; nos deja subir la frecuencia sin quemar CPU.
4. **PyInstaller `--onefile` + carpeta de recursos al lado**, tal cual el `build.py` de D4LF.
5. **Instalador con autoactualización**: Velopack es el patrón en .NET; en Python el equivalente
   honesto es el autoactualizador propio que ya tiene D4LF (`src/autoupdater.py`).
6. **La formulación de la frontera**, palabra por palabra, en nuestro README: sin inyección, sin
   memoria, sin overlay, sin automatizar entradas. Lo dicen tanto Awakened PoE Trade como el
   comparador de objetos de brianjleepub. Es la mejor defensa que hay: escrita y verificable.
7. **Localización esES desde el día uno**: Diablo4Companion mantiene `README.esES.md` y recursos
   `esES`. El OCR en español necesita el paquete de idioma del sistema instalado — hay que
   comprobarlo al arrancar y avisar, no fallar en silencio.

---

## 7. Riesgos que el arte previo deja documentados

| Riesgo | Evidencia | Mitigación |
|---|---|---|
| **PyInstaller = falso positivo de antivirus** | Problema conocido y bien documentado (issue #6754 de PyInstaller, guías de pythonguis). Windows Defender puede poner el exe en cuarentena: para un usuario no técnico eso es "no funciona" | Modo carpeta + instalador en vez de `--onefile`; firmar el binario; PyInstaller siempre al día; o **Nuitka** (15.110 ★), que compila a C y da menos falsos positivos |
| **tkinter borroso en HiDPI** | Issue #119174 de CPython; toda la documentación de escalado de CustomTkinter | Marcar el proceso como DPI-aware, o pasar a PySide6/CustomTkinter |
| **Pantalla completa exclusiva devuelve negro** | Issue #28 de python-mss; comportamiento estándar de DirectX | Exigir "ventana sin bordes" y **detectarlo**: si la captura sale negra, decirlo en la UI |
| **La tipografía de D4 castiga al OCR genérico** | `d4-item-tooltip-ocr` tuvo que **entrenar un modelo propio** para PaddleOCR | Preprocesar (recorte, escala 2-3x, umbral) antes del OCR, y difuso después. Medirlo con capturas reales antes de dar nada por bueno |
| **Baneo sin aviso** | El hilo del foro de Blizzard: no hay azul confirmando nada, la aplicación llega por oleadas | Mantener la restricción dura, y que la herramienta **no toque el juego de ninguna forma**: ni ventana encima, ni teclas enviadas, ni DLL |

---

## Fuentes

Páginas y endpoints abiertos de verdad para este informe:

- https://github.com/d4lfteam/d4lf
- https://raw.githubusercontent.com/d4lfteam/d4lf/main/README.md
- https://raw.githubusercontent.com/d4lfteam/d4lf/main/pyproject.toml
- https://raw.githubusercontent.com/d4lfteam/d4lf/main/build.py
- https://raw.githubusercontent.com/d4lfteam/d4lf/main/src/perception/capture/core.py
- https://raw.githubusercontent.com/d4lfteam/d4lf/main/src/perception/text.py
- https://raw.githubusercontent.com/d4lfteam/d4lf/main/src/perception/backend/windows.py
- https://api.github.com/repos/d4lfteam/d4lf/contents/tts
- https://github.com/josdemmers/Diablo4Companion
- https://raw.githubusercontent.com/josdemmers/Diablo4Companion/master/README.md
- https://raw.githubusercontent.com/josdemmers/Diablo4Companion/master/D4Companion/D4Companion.csproj
- https://raw.githubusercontent.com/josdemmers/Diablo4Companion/master/D4Companion.Services/D4Companion.Services.csproj
- https://github.com/SnosMe/awakened-poe-trade
- https://snosme.github.io/awakened-poe-trade/faq
- https://github.com/Kvan7/Exiled-Exchange-2
- https://github.com/ChaosRecipeEnhancer/ChaosRecipeEnhancer
- https://github.com/PathOfBuildingCommunity/PathOfBuilding
- https://github.com/mxtsdev/d4-item-tooltip-ocr
- https://github.com/mivuorin/d4-ocr
- https://github.com/brianjleepub/diablo4_item_comparer
- https://github.com/GitHub30/winocr
- https://github.com/ra1nty/DXcam
- https://github.com/cagartner/awesome-d4
- https://us.forums.blizzard.com/en/d4/t/third-party-app-diablo-iv-overlay-is-permitted-modcheck/41715
- https://d4armory.io/ (301 → https://diablo4.com/, comprobado por cabeceras HTTP el 29-ago-2026)
- https://api.github.com/repos/... (metadatos de estrellas, licencia y último push de las 18 repos citadas)

---

## No encontrado

- **API oficial de Blizzard para datos de personaje/equipo de Diablo IV.** No existe. Y la
  alternativa no oficial que usaba la comunidad, **d4armory.io, está muerta**: hoy responde
  301 a `diablo4.com`, tanto la raíz como la ruta de API. Comprobado con cabeceras HTTP.
- **Un mecanismo tipo Ctrl+C de Path of Exile en Diablo IV.** D4 permite enlazar objetos en el chat
  con shift+clic, pero no he encontrado ninguna prueba de que eso deje texto plano en el
  portapapeles. Si existiera, se cargaría la mitad de nuestro proyecto (para bien).
- **Un compañero de juego real, con tracción, escrito en Rust + Tauri.** He buscado y solo encuentro
  los plugins (`tauri-plugin-global-shortcut`, `tauri-plugin-screenshots`) y discusiones, no un
  producto acabado que sirva de precedente. **Tauri queda como opción teóricamente buena y sin
  validar en este nicho.**
- **Estrellas de `libuiohook`, `GameOverlay.Net` y `NHotkey`**: los cité por su uso en los `.csproj`
  y los agradecimientos, no abrí sus repos.
- **Comparativa medida de winocr (Windows.Media.Ocr) frente a Tesseract o PaddleOCR sobre tooltips
  de Diablo IV.** No existe publicada. `d4-item-tooltip-ocr` no publica banco de pruebas.
  **Esto habría que medirlo nosotros**, y es la incógnita técnica más grande que queda.
- **Confirmación de un empleado de Blizzard** sobre si un compañero de ventana propia sin overlay
  está permitido. El hilo del foro no tiene respuesta oficial. Sigue siendo interpretación.
- **Tamaño real del ejecutable** de D4LF o Diablo4Companion: no abrí la página de *releases*, así que
  las cifras de peso de la tabla §4 son órdenes de magnitud típicos del stack, no medidas.
