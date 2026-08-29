# Estado del arte: OCR aplicado a interfaces de juego

**Dominio:** proyectos open source que leen tooltips o interfaces de juego con OCR.
**Fecha de investigación:** 29 de agosto de 2026.
**Pregunta central en cada ficha:** de dónde saca los datos.

---

## 0. Resumen para impacientes

Cinco cosas que cambian el diseño actual:

1. **Existe una fuente de datos que no es OCR.** Diablo IV emite el texto completo del tooltip
   por su API de accesibilidad (lector de pantalla). El proyecto más maduro en Python (d4lf)
   **abandonó el OCR** por esa vía. Tiene un coste de cumplimiento serio (ver §2.1) pero
   demuestra que el texto exacto existe y sale del juego sin OCR.
2. **Nadie hace OCR de la pantalla entera.** Todos localizan primero el tooltip por color o por
   plantilla, recortan, y solo entonces pasan el OCR sobre un recorte pequeño.
3. **El vocabulario cerrado que planeamos es el consenso del sector**, y hay una implementación
   concreta con una trampa documentada: el scorer difuso equivocado elige siempre el afijo corto.
4. **Ya existe el vocabulario de afijos en español de España**, 891 entradas, con el texto ya
   limpio de números, licencia MIT. No hay que construirlo.
5. **`winocr` es defendible pero es la opción de menor precisión** de las que no requieren
   instalar nada, y el "sin instalar" tiene una letra pequeña (el paquete de idioma español).

---

## 1. Herramientas encontradas

| Nombre | Repo | Lenguaje | Fuente de datos | Nota |
|---|---|---|---|---|
| **d4lf** (Diablo 4 Loot Filter) | [d4lfteam/d4lf](https://github.com/d4lfteam/d4lf) | Python (206★) | **TTS de accesibilidad del juego vía named pipe** + `mss` para plantillas | El más avanzado. Ver §2.1. MIT |
| **Diablo4Companion** | [josdemmers/Diablo4Companion](https://github.com/josdemmers/Diablo4Companion) | C# (321★) | Captura de ventana (Win32) → Emgu CV → Tesseract | El más aplicable a nosotros. MIT. Ver §2.2 |
| **d4-item-tooltip-ocr** | [mxtsdev/d4-item-tooltip-ocr](https://github.com/mxtsdev/d4-item-tooltip-ocr) | Python (40★) | Fichero de imagen (PNG/JPG), no captura | PaddleOCR con modelo entrenado a medida. Ver §2.3 |
| **d4-ocr** | [mivuorin/d4-ocr](https://github.com/mivuorin/d4-ocr) | C# (0★) | Captura de escritorio por PInvoke | Tesseract. Overlay dibujado. Prueba de concepto abandonada. Ver §2.4 |
| **horadricapp** | [stephaistos/horadricapp](https://github.com/stephaistos/horadricapp) | (5★) | Recorte de captura guardada | D2R. Tesseract con `traineddata` propio. Ver §2.5 |
| **RSTGameTranslation** | [thanhkeke97.github.io/RSTGameTranslation](https://thanhkeke97.github.io/RSTGameTranslation/) | C# | Captura de región de pantalla | Traductor. Soporta 5 motores y **publica tabla comparativa**. Ver §3 |
| **owocr** | [AuroraWright/owocr](https://github.com/AuroraWright/owocr) | Python | Captura / portapapeles | Multi-motor, orientado a manga y novela visual |
| **oneocr** | [AuroraWright/oneocr](https://github.com/AuroraWright/oneocr) | Python (38★) | Imagen | Wrapper del motor de la Herramienta de Recortes de Win11. Ver §4.2 |
| **winocr** | [GitHub30/winocr](https://github.com/GitHub30/winocr) | Python (25★) | Imagen (PIL/cv2) | Nuestra opción actual. 50 líneas. Ver §4.1 |
| **RapidOCR** | [RapidAI/RapidOCR](https://github.com/RapidAI/RapidOCR) | Python | Imagen | ONNX, `pip install`, sin instalación de sistema. Ver §4.3 |
| **pyugt** | [lrq3000/pyugt](https://github.com/lrq3000/pyugt) | Python | Captura de región seleccionada | Traductor universal de juegos, Tesseract, offline |
| **diablo4trading-ocr** | [wenqu/diablo4trading-ocr](https://github.com/wenqu/diablo4trading-ocr) | JS/Node | Imagen | tesseract.js, para navegador. No verificado en profundidad |

---

## 2. Fichas técnicas

### 2.1 d4lf — el hallazgo que cuestiona el diseño

**Repo:** https://github.com/d4lfteam/d4lf · Python · 206★ · 44 forks · MIT · activo (push 28-ago-2026)

**Fuente de datos: NO es OCR.** Es el propio juego hablando.

Al leer `pyproject.toml` no hay ninguna librería de OCR — ni `pytesseract`, ni `paddleocr`, ni
`rapidocr`. Sí hay `mss`, `opencv-python`, `numpy` y `rapidfuzz`. El OCR está donde no se
esperaba: **no está**.

El mecanismo real está en `tts/`:

- `tts/saapi.cpp` compila un `saapi64.dll` que exporta `SA_SayW`, `SA_IsRunning`,
  `SA_StopAudio`, `SA_BrlShowTextW` — la interfaz **SAAPI** (System Access API) de lectores de
  pantalla.
- En `DllMain`/`DLL_PROCESS_ATTACH` abre un named pipe `\\.\pipe\d4lf` y escribe en él cada
  cadena que el juego manda al lector de pantalla:
  ```cpp
  void InitPipe() { hPipe = CreateFile(_T("\\\\.\\pipe\\d4lf"), GENERIC_WRITE, 0, NULL, OPEN_EXISTING, 0, NULL); }
  extern "C" bool SA_SayW(const wchar_t* str) { ... WriteFile(hPipe, narrowStr.c_str(), ...); }
  ```
- `src/perception/backend/windows.py` levanta el otro extremo con
  `win32pipe.CreateNamedPipe(r"\\.\pipe\d4lf", ...)` y encola cada mensaje.
- `tts/install_dll.cmd` pide **administrador** y acepta un `-signtool_path`: hay que firmar el
  DLL y colocarlo donde el juego lo cargue.

**Consecuencia para nosotros.** El texto que llega por ahí es exacto: cero errores de OCR, cero
umbrales, cero resoluciones. Es tentador. Pero **el mecanismo viola nuestra restricción dura**:
es un DLL de terceros cargado dentro del proceso del juego. No lee memoria y no modifica lógica,
pero es sustitución de biblioteca dentro del proceso — que es lo que la mayoría llamaría
inyección. **Recomiendo no copiarlo.** Lo que sí vale la pena registrar es el hecho subyacente:
*Diablo IV expone el texto del tooltip por accesibilidad*. Si alguna vez existe una ruta que no
pase por meter un DLL en el proceso (un lector de pantalla real instalado exponiendo su propia
API documentada), esa ruta sería estrictamente mejor que el OCR.

**Lo que sí copiamos de d4lf, y es mucho:**

`src/perception/capture/core.py` — captura con `mss`, exactamente nuestro plan, pero:

- Captura **solo el rectángulo de la ventana del juego**, no la pantalla:
  `sct.grab(window_roi)` con `{top, left, width, height}`.
- **Cachea el frame 40 ms** (`time.perf_counter() - self.last_grab < 0.04`) para que varios
  consumidores en el mismo tick no disparen capturas repetidas.
- Desactiva `CAPTUREBLT`: `mss.windows.__dict__["CAPTUREBLT"] = 0`. Es un flag de `BitBlt`;
  quitarlo evita capturar capas superpuestas y acelera.
- Deriva la clave de resolución de la ventana (`f"{width}x{height}"`) y avisa si el aspecto es
  más estrecho que 16:10.

`src/perception/text.py` — el parser de vocabulario cerrado:

- `clean_str()` **quita los números antes de emparejar**: elimina separadores de millar entre
  dígitos, luego `re.sub(r"(\+)?\d+(\.\d+)?%?", "", ...)`, luego `[x]`, luego `[ ] + - : % '`,
  luego corta el texto a partir de palabras clave, y baja a minúsculas.
- `find_number()` extrae el valor por separado con `re.findall(r"[+-]?(\d+\.\d+|\.\d+|\d+\.?|\d+)\%?", s)`.
- `closest_match()` usa `rapidfuzz.process.extractOne` con
  `scorer=rapidfuzz.distance.Levenshtein.distance`.

Es decir: **el afijo y su número se procesan por caminos distintos**. El texto sin números se
empareja contra el vocabulario; el número se parsea aparte. Esto es exactamente lo que necesita
nuestro valorador de afijos.

**Aviso:** `assets/lang/` de d4lf **solo contiene `enUS`**. No sirve para español.

### 2.2 Diablo4Companion — la plantilla más cercana a lo que estamos construyendo

**Repo:** https://github.com/josdemmers/Diablo4Companion · C# · 321★ · 49 forks · MIT · activo (push 28-ago-2026)

**Fuente de datos:** captura de la ventana del juego por Win32 → Emgu CV → TesseractOCR (.NET).

Pipeline reconstruido leyendo el código:

| Paso | Cómo | Fichero |
|---|---|---|
| 1. Localizar la ventana | `PInvoke.GetWindowRect(windowHandle, out region)`, busca el proceso de Diablo IV (y también GeForce NOW) | `ScreenCaptureHandler.cs` |
| 2. Capturar | Región de la ventana, con `delay` configurable (`ScreenCaptureDelay`) | `ScreenCaptureHandler.cs` |
| 3. Gris + umbral | `.Convert<Gray, byte>().ThresholdBinaryInv(ThresholdMin, ThresholdMax)` — **umbral binario invertido**, por defecto **70/255 en SDR** | `ScreenProcessHandler.cs:636` |
| 4. Localizar tooltip y afijos | `CvInvoke.MatchTemplate(..., TemplateMatchingType.SqdiffNormed)` contra una biblioteca de plantillas | `ScreenProcessHandler.cs:531` |
| 5. OCR | Solo sobre los recortes pequeños de cada afijo, salida **hOCR** parseada por regex | `OcrHandler.cs` |
| 6. Emparejar | FuzzierSharp contra la lista cerrada de afijos | `OcrHandler.cs:942` |

**Truco 1 — el umbral es invertido, y por qué.** El texto del juego es claro sobre fondo oscuro;
Tesseract espera oscuro sobre claro. De ahí `ThresholdBinaryInv`. Que el umbral sea un ajuste de
usuario (y que el README avise de que **hay que desactivar HDR** porque "hace la pantalla
demasiado brillante") dice que este es el punto frágil de todo el sistema.

**Truco 2 — encontrar *todas* las apariciones con MatchTemplate.** `MatchTemplate` devuelve un
solo mejor resultado. Para encontrar los N afijos, tras localizar uno **pintan un rectángulo
relleno encima** y repiten, hasta 20 veces:
```csharp
CvInvoke.Rectangle(currentTooltip, rectangle, new MCvScalar(255, 255, 255), -1);
} while (similarity < _settingsManager.Settings.ThresholdSimilarityAffixLocation && counter < 20);
```

**Truco 3 — la trampa del scorer difuso.** Comentario textual en `OcrHandler.cs:939-940`:

> `DefaultRatioScorer`: rápido pero no funciona bien con afijos de una sola palabra como "Thorns".
> Pero no tiene los problemas de `TokenSetScorer`.
> `TokenSetScorer`: elige el equivocado `+#% Damage` en vez del más largo `+#% Shadow Damage Over Time`.

Esto nos afecta en español de forma idéntica: "daño" es subcadena de "daño de sombra a lo largo
del tiempo". **Un scorer de token-set elegirá siempre el afijo corto.** Usan `DefaultRatioScorer`
(ratio tipo Levenshtein sobre la cadena completa), no token-set.

**Truco 4 — caché de emparejamiento.** `_cacheAffixes` es un
`ConcurrentDictionary<string, ...>(StringComparer.OrdinalIgnoreCase)` con
`GetOrAdd(text, TextToAffix)`. El mismo texto OCR no se vuelve a emparejar nunca. Con 891
candidatos y un bucle de 0,7 s, esto no es opcional.

**Truco 5 — pool de motores.** `_engines = new ObjectPool<Engine>(() => new Engine(@"./tessdata", _language, ...))`.
Crear el motor es caro; se reutiliza. Se vacía al cambiar de idioma.

**Truco 6 — desactivan el preprocesador de FuzzierSharp para zh/ru:**
```csharp
bool disablePreprocessor = language.Equals("zhCN") || language.Equals("zhTW") || language.Equals("ruRU");
```
El preprocesador por defecto de las librerías tipo FuzzyWuzzy normaliza a alfanumérico ASCII.
**No lo desactivan para `esES`** — lo cual es un riesgo latente con `ñ`, tildes y `¿`. Si copiamos
el enfoque, hay que comprobar qué hace `rapidfuzz` con acentos antes de fiarse.

**EL ACTIVO REUTILIZABLE: el vocabulario en español ya existe.**

`D4Companion/Data/Affixes.esES.json` — **891 entradas**, confirmado descargando y contando.
Existen 9 idiomas (`esES`, `enUS`, `deDE`, `frFR`, `itIT`, `plPL`, `ptBR`, `ruRU`, `zhCN`), todos
HTTP 200. Estructura de una entrada real:

```json
{
  "IdSno": "2573119",
  "IdName": "2HStaff_Unique_AF_001_PickupRadius",
  "AffixType": 2,
  "Category": 0,
  "IsTemperingAvailable": false,
  "AllowedForPlayerClass": [1,1,0,0,0,0,0,0],
  "AffixAttributes": [{ "Localisation": "+[{VALUE}] de radio de recogida" }],
  "Description": "+# de radio de recogida",
  "DescriptionClean": "de radio de recogida"
}
```

`DescriptionClean` **ya viene sin números ni símbolos**: es literalmente la clave contra la que
hacer el emparejamiento difuso. `IdSno`/`IdName` son identificadores internos del juego, estables
entre parches e idiomas. `AllowedForPlayerClass` permite filtrar por clase. Hay también
`Aspects.esES.json`. Licencia MIT (`Copyright (c) 2022 Jos Demmers`), así que se puede reutilizar
citando la fuente.

### 2.3 d4-item-tooltip-ocr — localización del tooltip sin depender de la resolución

**Repo:** https://github.com/mxtsdev/d4-item-tooltip-ocr · Python · 40★ · último push jul-2023 (sin mantenimiento)

**Fuente de datos:** fichero de imagen por `--source-img`. No captura pantalla. Es un parser puro.

Aunque esté abandonado, tiene **la mejor idea de localización de todo el conjunto**: encontrar el
tooltip **por su color**, no por coordenadas ni por plantillas por resolución.

```python
hsv = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)
tmp = cv2.inRange(hsv, np.array([69, 45, 47]), np.array([85, 106, 73]))
tmp = cv2.dilate(tmp, kernel, iterations = 5)
contours, hierarchy = cv2.findContours(tmp, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if cv2.contourArea(cnt) > 10000 and h > w and w < width * 0.3 and w > width * 0.15:
        ...
```

Máscara HSV del fondo del tooltip → dilatar → contornos → filtrar por: área > 10000, **más alto
que ancho**, y anchura entre el **15 % y el 30 % de la anchura de pantalla**. Eso es
independiente de la resolución y del aspecto. Diablo4Companion, en cambio, necesita *presets* por
resolución (1080p/1440p/1600p/2160p, con algunos marcados como rotos).

Segunda idea: **template matching invariante a escala** con pirámide de imágenes, para encontrar
los iconos que marcan cada tipo de línea (afijo, reroll, aspecto, stat de arma, engarce):

```python
for i, scale in enumerate(np.linspace(0.2, 1.0, 20)[::-1]):
    resized = cv2.resize(source, (0, 0), fx = scale, fy = scale)
    result = cv2.matchTemplate(resized, tmpl, cv2.TM_CCORR_NORMED, mask=tmpl_mask)
    T, threshed = cv2.threshold(result, 0.95, 1., cv2.THRESH_TOZERO)
```
20 escalas de 0,2 a 1,0, `TM_CCORR_NORMED` con máscara, umbral 0,95. Es caro, pero elimina los
presets por resolución.

Configuración de PaddleOCR, que es informativa:
```python
PaddleOCR(lang='en', use_angle_cls=False, det_db_unclip_ratio=2.0,
          rec_model_dir='paddleocr-models/en_PP-OCRv3_rec-d4_tooltip',
          rec_batch_num=10, enable_mkldnn=True)
```
- `use_angle_cls=False`: el texto de interfaz nunca está rotado; quitar el clasificador de ángulo
  ahorra tiempo.
- `det_db_unclip_ratio=2.0`: **expande las cajas detectadas**. Las fuentes de juego tienen borde
  y glow; con el valor por defecto se cortan letras.
- `enable_mkldnn=True`: aceleración CPU.
- **Modelo de reconocimiento entrenado a medida** sobre la fuente de Diablo 4
  (`en_PP-OCRv3_rec-d4_tooltip`). Es la única prueba que he encontrado de que alguien consideró
  necesario reentrenar para esta fuente.

Detalle relevante: **le pasan el recorte del tooltip a PaddleOCR sin umbralizar ni invertir** (la
línea de `cv2.resize` está comentada). PaddleOCR come texto claro sobre oscuro directamente.
Tesseract no. Es una diferencia real entre motores.

### 2.4 d4-ocr — el dato de rendimiento

**Repo:** https://github.com/mivuorin/d4-ocr · C# · 0★ · último push feb-2024

**Fuente de datos:** captura de escritorio por interop nativo y PInvoke. Tesseract con modelos
`tessdata_fast`. Dibuja overlay con GameOverlay.Net.

Valor: es el único que declara un número de rendimiento y una conclusión honesta. El autor mide
**1–3 segundos por escaneo** y concluye:

> "Sadly currently it's not performing fast enough to exceed experienced players reading speed
> when going through loot."

Y en mayúsculas en el README: "IT DOES NOT MODIFY DIABLO 4 GAME IN ANY WAY!!!" — la misma
preocupación de cumplimiento que tenemos nosotros.

**Para nuestro bucle de 0,7 s:** si Tesseract sobre la pantalla completa tarda 1–3 s, el bucle
no cierra. Esto refuerza la regla de §3: recortar primero, OCR después.

### 2.5 horadricapp — el modo de fallo que nos va a pasar

**Repo:** https://github.com/stephaistos/horadricapp · 5★ · D2R, no D4

**Fuente de datos:** recorte de captura guardada. Tesseract con `traineddata` propio, OpenCV.

Lo relevante son sus limitaciones declaradas:

> "OCR might not work properly when the item overlay pops over dark textures (equipped inventory
> seems to be the worse)"

Los tooltips son **semitransparentes**: el mundo del juego se transparenta y cambia los píxeles
del fondo. Un umbral fijo falla cuando el jugador está sobre una textura oscura o muy clara. Es
la misma razón por la que Diablo4Companion expone el umbral como ajuste y exige desactivar HDR.

También: "Large Font Mode MUST be enable in game settings" y "tested resolutions 720p, 1080p,
1440p. Fancy ratios are likely to get terrible results." Coincide con el requisito de d4lf de
que la escala de fuente sea pequeña o mediana y de que el aspecto esté entre 16:10 y 21:9.

---

## 3. Preprocesado: lo que hace todo el mundo

| Truco | Quién | Para qué |
|---|---|---|
| Capturar solo la ventana del juego, no la pantalla | d4lf, Diablo4Companion | Velocidad, y coordenadas relativas estables |
| Cachear el frame unas decenas de ms | d4lf (40 ms) | Evitar capturas duplicadas en el mismo tick |
| Localizar el tooltip **antes** de hacer OCR | Todos | Es lo que hace viable el tiempo real |
| Localizar por máscara HSV + contornos | d4-item-tooltip-ocr | Independiente de resolución |
| Localizar por template matching | Diablo4Companion, d4-item-tooltip-ocr | Preciso pero necesita presets o pirámide de escalas |
| Gris + **umbral binario invertido** | Diablo4Companion (70/255 SDR) | Tesseract quiere oscuro sobre claro |
| No umbralizar nada | d4-item-tooltip-ocr | PaddleOCR come claro sobre oscuro directamente |
| Expandir las cajas detectadas (`det_db_unclip_ratio=2.0`) | d4-item-tooltip-ocr | Fuentes con borde/glow se cortan |
| Desactivar clasificador de ángulo | d4-item-tooltip-ocr | El texto de interfaz nunca está rotado |
| Exigir HDR desactivado | d4lf, Diablo4Companion | HDR rompe cualquier umbral fijo |
| Exigir escala de fuente pequeña/media | d4lf | Consistencia de layout |
| Pool de motores OCR | Diablo4Companion | La inicialización del motor es cara |
| Filtrar por confianza | RSTGameTranslation (0,1 letra / 0,2 línea) | Descartar basura antes del emparejamiento |

**Escalado (upscaling):** buscado explícitamente, **no encontrado** como técnica documentada en
ninguno de estos proyectos. Es la receta habitual para Tesseract con texto pequeño, pero aquí
nadie la declara. Lo anoto como hueco, no como consenso.

### 3.1 Vocabulario cerrado y corrección contra diccionario: sí, es el consenso

Nuestro plan coincide con la práctica de los dos proyectos serios. Ambos hacen lo mismo:

| | d4lf | Diablo4Companion |
|---|---|---|
| Librería difusa | `rapidfuzz` | `FuzzierSharp` |
| Scorer | `Levenshtein.distance` | `DefaultRatioScorer` (ratio, **no** token-set) |
| Limpieza previa | `clean_str()`: quita números, `[x]`, símbolos, minúsculas | `String.Concat(...Where(...))`: quita dígitos y `[](){}+-.,%` |
| Número | Camino separado (`find_number`) | Camino separado (`TextToAffixValue`) |
| Vocabulario | `assets/lang/enUS/affixes.json`, `item_types.json`, `uniques.json`, `sigils.json` | `Affixes.<lang>.json`, `Aspects.<lang>.json`, uniques, runas, sigilos, tipos |
| Caché | — | `ConcurrentDictionary` por texto |

No he encontrado a nadie que use un modelo de lenguaje ni corrección ortográfica genérica. Todos
emparejan contra la lista cerrada de cadenas del juego, que es lo correcto: el espacio de salidas
válidas es finito y conocido.

---

## 4. La pregunta concreta: ¿es `winocr` razonable en Windows?

### 4.1 Qué es realmente `winocr`

**Repo:** https://github.com/GitHub30/winocr · 25★ · 12 forks · MIT · último push 25-oct-2024.

Es un fichero de ~50 líneas. Todo lo que hace:

```python
from winrt.windows.media.ocr import OcrEngine
def recognize_bytes(bytes, width, height, lang='en'):
    cmd = 'Add-WindowsCapability -Online -Name "Language.OCR~~~en-US~0.0.1.0"'
    assert OcrEngine.is_language_supported(Language(lang)), cmd
    writer = DataWriter(); writer.write_bytes(bytes)
    sb = SoftwareBitmap.create_copy_from_buffer(writer.detach_buffer(), BitmapPixelFormat.RGBA8, width, height)
    return OcrEngine.try_create_from_language(Language(lang)).recognize_async(sb)
```

Dependencias: solo los paquetes de proyección `winrt-windows-*`. Pillow/OpenCV/FastAPI son extras.

**Tres observaciones que importan:**

1. **Ese `assert` es la letra pequeña del "sin instalar".** Windows.Media.Ocr necesita el paquete
   de idioma. `Language.OCR~~~es-ES~0.0.1.0` **existe** y se instala con
   `Add-WindowsCapability` desde PowerShell **como administrador**. Suele estar presente si el
   idioma de Windows es español, pero en un Windows en inglés con el juego en español, no.
   Se comprueba con:
   `Get-WindowsCapability -Online | Where-Object { $_.Name -Like 'Language.OCR*' }`.
   Y en código, con `OcrEngine.IsLanguageSupported()` — que además **resuelve** el idioma
   (pedir `es` puede acabar en `es-ES` o `es-MX`), así que conviene comprobar
   `RecognizerLanguage` después de crear el motor, no solo antes.

2. **`picklify()` es un problema de rendimiento.** Las funciones `_sync` hacen
   `asyncio.run(...)` por fotograma y luego serializan el resultado recorriendo `dir(o)` con
   `getattr` sobre cada atributo de cada palabra de cada línea. A 0,7 s de cadencia probablemente
   se aguanta, pero es trabajo puro de reflexión que no necesitamos.

3. **Es tan fino que se puede absorber.** Son ~15 líneas contra `winrt-windows-media-ocr`
   directamente, sin `picklify`, sin `asyncio.run` por frame, con el `OcrEngine` creado una sola
   vez y reutilizado (como el pool de Diablo4Companion). Se elimina una dependencia de 25★ sin
   mantenimiento desde octubre de 2024 y se gana control.

Además conviene comprobar `OcrEngine.MaxImageDimension` (propiedad documentada): hay un máximo de
píxeles admitido, y si algún día recortamos a resoluciones altas hay que respetarlo.

### 4.2 ¿Hay algo mejor y sin instalar? OneOCR

Sí, con matices. **OneOCR** es el motor que usa la Herramienta de Recortes de Windows 11 — más
moderno que `Windows.Media.Ocr`, que es API de 2015 (Windows 10 10240).

La tabla comparativa publicada por RSTGameTranslation, que soporta los cinco motores y por tanto
puede compararlos en el mismo escenario (texto de juego), dice:

| Motor | Recursos | Precisión | Instalación | Mejor para |
|---|---|---|---|---|
| **Windows OCR** (`Windows.Media.Ocr`) | ~2 % CPU | **Media** | Ninguna | GPUs AMD/Intel |
| **OneOCR** | ~10 % CPU | **Alta** | Ninguna | Todos, manga |
| **RapidOCR** | ~10 % GPU | **Muy alta** | 5–15 min | NVIDIA, occidental |
| **EasyOCR** | ~20 % GPU | Buena | 5–15 min | NVIDIA, muchos idiomas |
| **PaddleOCR** | ~15 % GPU | **Muy alta** | 5–15 min | NVIDIA, asiático |

Es decir: **`Windows.Media.Ocr` es el de menor precisión de toda la lista**, y OneOCR le gana sin
coste de instalación.

**Pero el "sin instalar" de OneOCR tiene trampa.** Según
[AuroraWright/oneocr](https://github.com/AuroraWright/oneocr) (Python, 38★), hay que colocar a
mano tres ficheros en `~/.config/oneocr`:
- `oneocr.dll`
- `oneocr.onemodel`
- `onnxruntime.dll`

que se obtienen de la Herramienta de Recortes, o bien de
`C:\Program Files\WindowsApps\Microsoft.ScreenSketch_<versión>_x64__8wekyb3d8bbwe\SnippingTool`
(ruta con versión en el nombre y con ACL restrictivas), o descargando el msixbundle de
`store.rg-adguard.net`. **Ninguna de las dos fuentes documenta si los ficheros son
redistribuibles**, y no hay contrato de API público: es ingeniería inversa. A cambio, la salida es
más rica que la de winocr: texto, ángulo, líneas, y **por palabra: texto, caja delimitadora y
confianza**.

Balance honesto:

| | `winocr` / Windows.Media.Ocr | OneOCR |
|---|---|---|
| API pública documentada | Sí (Microsoft Learn) | No, ingeniería inversa |
| Estabilidad entre versiones de Windows | Alta | Frágil (ruta con versión) |
| Redistribución | No aplica, es del sistema | **Sin aclarar** |
| Precisión en texto de juego | Media | Alta |
| CPU | ~2 % | ~10 % |
| Confianza por palabra | Solo línea/palabra sin score | **Sí, con confianza** |
| Instalación real | Paquete de idioma `es-ES` (admin) | Copiar 3 ficheros a mano |

### 4.3 La tercera vía: RapidOCR

**Repo:** https://github.com/RapidAI/RapidOCR · Apache 2.0 · modelos ONNX de PaddleOCR.

`pip install rapidocr onnxruntime`. **No necesita instalación de sistema** (a diferencia de
Tesseract, que necesita el binario) y **no necesita copiar DLLs del sistema** (a diferencia de
OneOCR). Modelos empaquetados, funciona offline, sin administrador. Precisión "muy alta" según la
tabla de §4.2.

**Caveat importante y verificado:** el README dice soporte por defecto para **chino e inglés**;
otros idiomas requieren otro modelo de reconocimiento. Para español haría falta un modelo latino
distinto, y no he podido confirmar cuál ni con qué precisión. No es un descarte, es un hueco.

### 4.4 Recomendación

**`winocr` es defendible como punto de partida, y lo mantendría para la v1**, por dos razones que
no son técnicas sino de riesgo: es API pública y documentada, y es la única opción sin ficheros
de procedencia dudosa. Pero con cuatro cambios:

1. **Absorber las 15 líneas** en vez de depender del paquete (evita `picklify` y `asyncio.run`
   por frame, y una dependencia sin mantenimiento desde oct-2024).
2. **Crear el `OcrEngine` una sola vez** y reutilizarlo.
3. **Fail-closed al arrancar**: comprobar `IsLanguageSupported('es-ES')` y, si falta, decirle al
   usuario el comando exacto `Add-WindowsCapability` en vez de fallar en mitad del bucle.
4. **Aislarlo tras una interfaz de un método** (`recognize(imagen) -> [(texto, caja, confianza)]`)
   para poder cambiar a OneOCR o RapidOCR sin tocar el parser. La precisión "media" de
   Windows.Media.Ocr es el riesgo real del proyecto; hay que poder sustituirla.

Y una medición pendiente que decide todo esto: **pasar el mismo lote de tooltips reales en
español por winocr y por OneOCR y contar afijos correctamente emparejados**. Nadie ha publicado
esa comparación; hay que hacerla en casa.

---

## 5. ¿Existe una librería para "leer interfaces de juego"?

**No.** No hay ningún paquete que ofrezca "OCR de interfaces de juego" como abstracción. Lo que
existe son dos categorías:

- **Motores OCR genéricos** (Tesseract, PaddleOCR, RapidOCR, EasyOCR, Windows.Media.Ocr, OneOCR).
- **Aplicaciones completas** que integran captura + OCR + traducción para juegos
  (pyugt, Screen-Translate, RSTGameTranslation, owocr, NormCap).

La parte específica de juego — localizar el tooltip, umbralizar, emparejar contra el vocabulario
del juego — **cada proyecto la reescribe**. No hay nada que importar; sí hay técnicas que copiar,
que es de lo que va §3.

---

## 6. Contexto: por qué OCR y no portapapeles

Path of Exile permite **Ctrl+C sobre un objeto** y vuelca el texto completo al portapapeles; de
ahí un ecosistema de parsers triviales (p. ej.
[klayver/poe-itemtext-parser](https://github.com/klayver/poe-itemtext-parser)).

**Diablo IV no tiene esa función.** Existe una petición formal en los foros oficiales de Blizzard
("Copy-Paste Item Information Feature Proposal") que sigue siendo una propuesta. Sin portapapeles
y sin API pública, las únicas fuentes son OCR o la vía de accesibilidad de §2.1. Nuestra elección
de OCR es la correcta bajo la restricción dura.

---

## 7. Implicaciones para nuestro diseño

| Nuestro diseño actual | Qué dice el estado del arte | Acción |
|---|---|---|
| `mss` cada 0,7 s | Correcto; d4lf usa `mss`. Pero captura solo la ventana y cachea 40 ms | Capturar ROI de ventana, no pantalla |
| OCR sobre lo capturado | **Nadie hace OCR de la pantalla entera.** 1–3 s con Tesseract full-screen | Localizar tooltip → recortar → OCR del recorte |
| `winocr` español | Viable, pero es el motor de menor precisión de la lista | Absorber, aislar tras interfaz, medir contra OneOCR |
| Parser de vocabulario cerrado | Es el consenso, hecho igual por los dos proyectos serios | Copiar el patrón: limpiar → quitar números → fuzzy ratio |
| Vocabulario de afijos | **Ya existe en esES, 891 entradas, MIT** | Reutilizar `Affixes.esES.json` con atribución |
| Sin overlay, ventana propia | d4-ocr y Diablo4Companion sí dibujan overlay | Nuestra restricción es más estricta que la práctica común; se mantiene |
| Sin inyección | d4lf **sí** mete un DLL en el proceso | Confirma que nuestra línea roja nos cierra la mejor fuente de datos. Aceptado |

---

## Fuentes

Páginas y ficheros efectivamente abiertos:

- https://github.com/d4lfteam/d4lf
- https://raw.githubusercontent.com/d4lfteam/d4lf/main/pyproject.toml
- https://raw.githubusercontent.com/d4lfteam/d4lf/main/src/perception/text.py
- https://raw.githubusercontent.com/d4lfteam/d4lf/main/src/perception/backend/core.py
- https://raw.githubusercontent.com/d4lfteam/d4lf/main/src/perception/backend/windows.py
- https://raw.githubusercontent.com/d4lfteam/d4lf/main/src/perception/capture/core.py
- https://raw.githubusercontent.com/d4lfteam/d4lf/main/tts/saapi.cpp
- https://raw.githubusercontent.com/d4lfteam/d4lf/main/tts/install_dll.cmd
- https://raw.githubusercontent.com/d4lfteam/d4lf/main/LICENSE
- https://github.com/josdemmers/Diablo4Companion
- https://raw.githubusercontent.com/josdemmers/Diablo4Companion/master/D4Companion.Services/OcrHandler.cs
- https://raw.githubusercontent.com/josdemmers/Diablo4Companion/master/D4Companion.Services/ScreenCaptureHandler.cs
- https://raw.githubusercontent.com/josdemmers/Diablo4Companion/master/D4Companion.Services/ScreenProcessHandler.cs
- https://raw.githubusercontent.com/josdemmers/Diablo4Companion/master/D4Companion/Data/Affixes.esES.json
- https://raw.githubusercontent.com/josdemmers/Diablo4Companion/master/LICENSE
- https://github.com/mxtsdev/d4-item-tooltip-ocr
- https://raw.githubusercontent.com/mxtsdev/d4-item-tooltip-ocr/main/README.md
- https://raw.githubusercontent.com/mxtsdev/d4-item-tooltip-ocr/main/d4-item-tooltip-ocr.py
- https://github.com/mivuorin/d4-ocr
- https://github.com/stephaistos/horadricapp
- https://github.com/GitHub30/winocr
- https://raw.githubusercontent.com/GitHub30/winocr/main/winocr.py
- https://raw.githubusercontent.com/GitHub30/winocr/main/setup.py
- https://raw.githubusercontent.com/GitHub30/winocr/main/README.md
- https://github.com/AuroraWright/oneocr
- https://b1tg.github.io/post/win11-oneocr/
- https://github.com/RapidAI/RapidOCR
- https://thanhkeke97.github.io/RSTGameTranslation/
- https://learn.microsoft.com/en-us/uwp/api/windows.media.ocr.ocrengine
- https://docs.vntranslator.com/user-guide/ocr/ocr-engines/windows-ocr

Citados desde resultados de búsqueda, no abiertos en profundidad:

- https://github.com/klayver/poe-itemtext-parser
- https://us.forums.blizzard.com/en/d4/t/copy-paste-item-information-feature-proposal/137085
- https://github.com/AuroraWright/owocr
- https://github.com/wenqu/diablo4trading-ocr
- https://github.com/lrq3000/pyugt
- https://learn.microsoft.com/en-us/uwp/api/windows.media.ocr.ocrengine.availablerecognizerlanguages

---

## No encontrado

- **Comparación de precisión publicada entre `Windows.Media.Ocr` y Tesseract sobre texto de
  interfaz.** Buscado explícitamente. Solo hay comparaciones sobre documentos escaneados, y varias
  proceden de vendedores comerciales (IronSoftware), que no son fuente neutral. La única
  comparación en escenario de juego es la tabla cualitativa de RSTGameTranslation, sin metodología
  publicada ni cifras.
- **Cifras de precisión numéricas de cualquiera de las herramientas de Diablo.** Ninguna publica
  tasa de acierto por afijo, ni matriz de confusión, ni corpus de prueba.
- **El único dato de rendimiento concreto** es "1–3 segundos" de d4-ocr, sin especificar
  resolución, hardware ni tamaño de región.
- **Escalado (upscaling) como preprocesado** antes del OCR: no documentado en ninguno de estos
  proyectos, pese a ser receta habitual para Tesseract con texto pequeño.
- **Precisión de RapidOCR en español.** El README declara chino e inglés por defecto; no he
  confirmado qué modelo latino usar ni con qué resultado.
- **Redistribuibilidad de `oneocr.dll` / `oneocr.onemodel`.** Ni el repo de AuroraWright ni el
  análisis de b1tg abordan la licencia. Sin resolver.
- **Precisión relativa de OneOCR frente a `Windows.Media.Ocr`.** Ambas fuentes consultadas lo
  omiten explícitamente. La única señal es la tabla de RSTGameTranslation ("Media" vs "Alta").
- **Postura de Blizzard sobre la vía de accesibilidad/TTS de d4lf.** El README de d4lf no contiene
  ninguna declaración sobre EULA ni riesgo de baneo; el de Diablo4Companion tampoco. Solo d4-ocr
  hace una declaración ("IT DOES NOT MODIFY DIABLO 4 GAME IN ANY WAY"). No hay pronunciamiento
  oficial localizado.
- **Datos de `diablo4trading-ocr`** (estrellas, estado): la API de GitHub devolvió límite de tasa
  antes de poder confirmarlos. Solo consta de la búsqueda que es Node + tesseract.js.
- **Contenido de `assets/templates` de d4lf y estructura exacta de sus `affixes.json`**: no
  inspeccionados por presupuesto de tiempo. Se sabe que solo existe `enUS`.
