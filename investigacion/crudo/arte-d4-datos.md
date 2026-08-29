# Arte previo: ¿de dónde sacan los datos las herramientas de Diablo IV?

**Dominio:** ¿expone Diablo IV los datos del personaje sin OCR?
**Fecha de la investigación:** 29 de agosto de 2026.
**Metadatos de GitHub (estrellas, lenguaje, último push):** consultados vía `gh api repos/<owner>/<repo>` el 29-08-2026. Son verificables y reproducibles, no estimados.

---

## Veredicto en una línea

**Sí, hay una vía sin OCR, y está viva: el lector de pantalla de accesibilidad del propio juego.**
No es un fichero, ni una API, ni el portapapeles: es el juego llamando a `SA_SayW(texto)` sobre una DLL que tú pones. Te da la cadena exacta del tooltip, sin píxeles de por medio. Pero tiene un coste que hay que mirar de frente: implica meter un binario propio dentro del proceso del juego, y eso roza la restricción dura del encargo.

Las otras tres vías están **cerradas**: no hay ficheros locales con el personaje, no hay exportación de build dentro del juego, y no hay API (oficial ni no oficial) viva en 2026.

---

## 1. Las cuatro preguntas del encargo, respondidas

| # | Pregunta | Respuesta | Confianza | Prueba |
|---|---|---|---|---|
| a | ¿Escribe el juego ficheros/logs/cachés con equipo, habilidades o estadísticas? | **NO.** Todo el personaje vive en el servidor. En local solo hay `LocalPrefs.txt` (ajustes gráficos) y volcados de error (`BlizzardError/`). | Alta | Foro oficial: "Characters are not stored locally no." · "Even your settings are stored on bnet" |
| b | ¿Hay exportar build / copiar al portapapeles / código de build dentro del juego? | **NO para el personaje.** El *Armory* interno guarda hasta 5 loadouts pero no exporta nada. **SÍ, pero solo para el filtro de botín** (abril 2026): Exportar → copia un código base64 al portapapeles. Son reglas, no tus objetos. | Alta | Petición de CTRL+C sin respuesta de Blizzard (nov-2023); guías del filtro de botín (2026) |
| c | ¿API oficial o no oficial viva en 2026? | **NO.** `d4armory.io` responde **301 → diablo4.com**: muerto y aparcado. Su *fetcher* de GitHub está archivado. No hay D4 en el portal de desarrolladores de Battle.net (solo D3, WoW, SC2, Hearthstone). Nadie ha ocupado el hueco. | Alta | Redirección comprobada; hilo de API en foros de Blizzard sin respuesta azul |
| d | ¿Maxroll / d4builds importan desde el juego? | **NO.** El flujo va justo al revés: los planificadores **exportan** hacia las herramientas (d4lf y D4Companion importan de Maxroll, D4Builds, Mobalytics, InfinityBuilds, D2Core). Ninguno lee tu personaje real. | Alta | READMEs de d4lf y Diablo4Companion |

**Consecuencia para el diseño actual:** el OCR **no sobra**, pero **deja de ser la única opción**. Hay una segunda fuente, mejor y más barata en CPU, que ninguna de las cuatro preguntas del encargo contemplaba.

---

## 2. El hallazgo que puede cambiar el diseño: el lector de pantalla (TTS)

Diablo IV incluye una opción oficial en **Opciones → Accesibilidad → "Lector de pantalla de terceros"**. Blizzard lo anunció como soporte para JAWS, NVDA "y otro software lector de pantalla de terceros", para que un jugador ciego pueda "entender el equipo que lleva puesto".

El mecanismo es Tolk / **System Access API (SAAPI)**: el juego busca `saapi64.dll` **en su propia carpeta de instalación** y, si está firmada Authenticode, la carga y le llama a `SA_SayW(const wchar_t*)` con cada texto que narraría.

### Cómo lo explota d4lf (código real, ~50 líneas)

`d4lf` sustituye esa DLL por una propia que **no sintetiza voz**: reenvía la cadena por una *named pipe* de Windows.

```cpp
// tts/saapi.cpp — d4lfteam/d4lf
void InitPipe() { hPipe = CreateFile(_T("\\\\.\\pipe\\d4lf"), GENERIC_WRITE, 0, NULL, OPEN_EXISTING, 0, NULL); }

extern "C" bool SA_SayW(const wchar_t* str) {
    // WideCharToMultiByte(CP_UTF8, ...) y luego:
    BOOL flg = WriteFile(hPipe, narrowStr.c_str(), ..., &bytesWritten, NULL);
    if (!flg) InitPipe();
    return true;
}
```

El instalador (`tts/install_dll.cmd`, PowerShell embebido) hace exactamente esto, y merece la pena leerlo porque es la parte incómoda:

1. Pide **administrador**.
2. **Cierra Diablo IV a la fuerza** (`Stop-Process -Force`) para poder reemplazar la DLL.
3. Copia `saapi64.dll` a la carpeta del juego.
4. Crea un **certificado autofirmado** `CN=Cert for D4LF` (`New-SelfSignedCertificate -Type CodeSigningCert`, 10 años).
5. **Lo instala en el almacén Trusted Root del usuario.**
6. Descarga `Microsoft.Windows.SDK.BuildTools` de NuGet para conseguir `signtool.exe` y firma la DLL.

### Qué te da y qué te cuesta

| | Lector de pantalla (TTS) | OCR (diseño actual) |
|---|---|---|
| Fidelidad del texto | Cadena exacta, tal cual la del juego | Reconocimiento con error; confusiones de dígitos |
| Sensible a resolución / escala de fuente / HDR | **No** | **Sí, mucho** (ver §3: D4Companion mantiene *presets* por resolución) |
| Coste en CPU | Casi nulo, guiado por eventos | Captura a 0,7 s + inferencia continua |
| Idioma | Emite en el idioma del cliente → **español sale gratis** | Hay que entrenar/ajustar por idioma |
| Instalación para el usuario | Admin, cerrar el juego, certificado en Trusted Root | Copiar un `.exe` y listo |
| Riesgo frente a la EULA | **Alto**: binario de terceros dentro del proceso del juego | **Bajo**: nada toca al juego |
| Fragilidad ante parches | Se ha roto al menos una vez (temporada 12, marzo 2026) | Se rompe cuando cambia la UI |

### El precedente de rotura

El 11 de marzo de 2026 un desarrollador de lector de pantalla reportó en los foros oficiales que su herramienta dejó de funcionar con el PTR y el lanzamiento de la **temporada 12**, sin haber tocado su `saapi64.dll` en mucho tiempo. **Blizzard no respondió** en ese hilo y quedó sin resolver.

Pero la vía sigue viva hoy: `d4lf` tiene push del **28-08-2026** (ayer) y en julio de 2026 cerró incidencias del tipo *"Items in the armory, especially seals, should now be properly parsed"* — es decir, sigue leyendo objetos, incluido dentro del Armory del juego.

### El aviso honesto

El encargo prohíbe "inyección". Esto **no es inyección** en sentido técnico: el juego carga la DLL voluntariamente, por una ruta de accesibilidad oficial, con un interruptor oficial en el menú. Pero **sí es código propio ejecutándose dentro del proceso de Diablo IV**, y la interpretación comunitaria de la EULA que más circula es: *"¿Te enseña datos de Diablo 4 que no puedes ver con las funciones del juego? Si sí, no lo uses."* (foro de Blizzard, usuario veterano — **no hay post azul**; Blizzard no evalúa herramientas una a una y no existe lista blanca). Los datos del TTS **sí** son datos que el juego ya te enseña; la duda no está en qué se lee, sino en dónde corre el código que lo lee.

**Esto es una decisión del fundador, no mía.** Yo lo dejo medido: el OCR es defendible al 100 % frente a la restricción dura; el TTS es técnicamente superior y legalmente gris.

---

## 3. Herramientas encontradas · nombre · repo · lenguaje · **fuente de datos** · nota

| Nombre | Repo | Lenguaje | ★ | Último push | **Fuente de datos** | Nota |
|---|---|---|---|---|---|---|
| **D4LF (Diablo 4 Loot Filter)** | github.com/d4lfteam/d4lf | Python | 206 | 2026-08-28 | **TTS de accesibilidad (SAAPI/Tolk) + lectura de pantalla** | La referencia. `saapi64.dll` propia → named pipe. Exige inglés, HDR apagado, fuente pequeña/media, 16:10–21:9. Automatiza el ratón salvo en "Vision Mode Only" |
| **Diablo IV Companion** | github.com/josdemmers/Diablo4Companion | C# (.NET) | 321 | 2026-08-28 | **OCR (TesseractOCR) + emparejamiento de imágenes (Emgu CV)** | El repo más estrellado. Overlay en juego. **Soporta esES**. Ver §4: mantiene *presets* por resolución/HDR/fuente |
| **d4-item-tooltip-ocr** | github.com/mxtsdev/d4-item-tooltip-ocr | Python | 40 | 2023-07-18 | **OCR (PaddleOCR + modelo entrenado a medida para D4)** sobre imágenes ya capturadas | Muerto desde 2023, pero el enfoque es el más limpio: entrada = imagen, salida = JSON de afijos. Sin captura, sin overlay |
| **D4TTS** | github.com/josdemmers/D4TTS | C# | 0 | 2025-06-08 | **TTS de accesibilidad (SAAPI/Tolk)** | "App para probar la función TTS de Diablo IV". Banco de pruebas mínimo para validar la vía sin montar todo |
| **diablo4-build-calc** | github.com/Lothrik/diablo4-build-calc | HTML/JS | 221 | 2026-07-09 | **Minado de datos del cliente (CASC, ficheros `.stl`)** — datos del juego, no del jugador | El autor documenta la función hash de Blizzard y recomienda empezar por los `.stl`. Sus herramientas de minado no son públicas |
| **Diablo4Tools / D4Analyzer** | github.com/DiabloTools/Diablo4Tools-Releases | — | 29 | 2026-06-19 | **Instalación local del juego (CASC)**: listas de cadenas/traducciones, texturas, modelos | Apuntas a tu carpeta de Diablo IV y saca las **StringLists traducidas**. Clave para el §5 |
| **d4data** | github.com/DiabloTools/d4data | — | 55 | 2026-08-13 | **Volcado de datos del juego** (sucesor vivo de blizzhackers/d4data) | El de blizzhackers (101★) está **archivado** desde 2024 |
| **diablo-4-string-parser** | github.com/alkhdaniel/diablo-4-string-parser | Python | 26 | 2023-03-22 | **Ficheros `.stl` del juego → JSON** | 30 líneas de utilidad. Advierte: probado con enUS, no garantiza no-latinos (el español no es problema) |
| **d4parse** | github.com/Dakota628/d4parse | Go | 7 | 2024-10-10 | **Ficheros SNO del juego** (genera código Go desde las definiciones de d4data) | Parado |
| **diablo4-data-harvest** | github.com/mfloob/diablo4-data-harvest | Rust | 39 | 2023-04-02 | **CASC descomprimido** | **Archivado** |
| **d4-tools (calculadora de daño)** | github.com/bytemind-de/d4-tools | JavaScript | 44 | 2026-05-19 | **Entrada manual del usuario** (localStorage, export JSON) | Muy pertinente: implementa los *buckets* de daño (aditivo vs multiplicativo). En su lista de deseos: *"Read the data from your actual account via some Blizzard API (d4armory seems to be able to do it, but how???)"* — nadie sabe cómo lo hacía |
| **diablo_4_armory_fetcher** | github.com/ryancollingwood/diablo_4_armory_fetcher | Python | 17 | 2025-09-25 | **API no oficial de d4armory.io** | **Archivado.** Es el fósil que prueba que la vía API murió |
| **awesome-d4** | github.com/cagartner/awesome-d4 | — | 52 | 2026-07-27 | Índice curado | Útil para barrer el ecosistema; no marca nada como muerto (incluye d4armory.io como si viviera) |
| **d4-ocr** | github.com/mivuorin/d4-ocr | C# | 0 | 2024-02-08 | **OCR** | Abandonado |
| **diablo4trading-ocr** | github.com/wenqu/diablo4trading-ocr | JS | 1 | 2023-09-04 | **OCR (tesseract.js en navegador)** | Abandonado |
| **Diablo4DpsMeter** | github.com/shalzuth/Diablo4DpsMeter | — | 4 | 2024-10-07 | **No verificable** | El nombre prometía un log de combate. **El repo solo tiene README, LICENSE y .gitignore: no hay código.** No es prueba de que exista ningún log |
| **DiabloIV.Helper** | github.com/DarkDBx/DiabloIV.Helper | Python | 25 | 2026-07-21 | Píxeles + **automatización de entradas** | "pixel bot". Zona prohibida por el encargo. Lo cito como frontera, no como referencia |

---

## 4. Lo que cuesta el OCR de verdad: la tabla de *presets* de D4Companion

D4Companion no tiene "un OCR". Tiene **un preset por combinación de resolución × escala de fuente × HDR**, y cada preset declara **qué idiomas** cubre:

| Preset | Idiomas cubiertos | Condición |
|---|---|---|
| `1080p_SMF` | de, **en, esES, esMX**, fr, pl, ptBR, ru | SDR (HDR apagado), fuente media |
| `1080p_SSF` | de, **en, esES, esMX**, pl, ptBR, ru | SDR, fuente pequeña |
| `1440p_HSF` | de, **en, esES**, pl, ptBR, ru | **HDR**, fuente pequeña |
| `1440p_SMF` | de, **en, esES, esMX**, fr, it, pl, ptBR, ru | SDR, fuente media |

Los presets se **descargan y actualizan** desde la app ("click the update / download button first to get the latest version"). Es decir: el proyecto con más estrellas del ecosistema mantiene infraestructura permanente solo para que el OCR siga leyendo cuando Blizzard mueve un píxel.

Y d4lf, que ya usa TTS, **aun así** exige: HDR apagado ("makes the screen too bright and D4LF is unable to read the state of some items"), fuente pequeña o media, y "Advanced Tooltip Information" activado en Opciones → Jugabilidad.

**Lectura para nuestro caso:** el coste real del OCR no es escribir el OCR. Es la matriz de configuraciones que hay que mantener viva después.

---

## 5. Regalo: el vocabulario cerrado no hay que escribirlo a mano

El parser del diseño actual usa "vocabulario cerrado" de afijos en español. Ese vocabulario **está dentro de la instalación del juego**, en los ficheros `.stl` (StringList) del almacenamiento CASC, en el idioma que tenga instalado el jugador.

- **D4Analyzer** (DiabloTools) ya soporta "StringLists / translations": apuntas a la carpeta de Diablo IV y las exporta.
- **diablo-4-string-parser** convierte un directorio de `.stl` a un `StringList.json` de un tirón.
- El autor de diablo4-build-calc lo confirma como el punto de entrada: *"I recommend examining the `.stl` files first"*, y publica la función hash de Blizzard.

Esto es **leer ficheros de tu propia instalación**, no leer memoria del juego ni tocar el proceso. Cae del lado seguro de la restricción dura.

---

## 6. La única exportación real que existe: el filtro de botín (abril 2026)

Con **Lord of Hatred** (28 de abril de 2026, actualización universal y gratuita) el juego incorporó por fin un **filtro de botín oficial**, y con él lo primero que Diablo IV escribe al portapapeles:

> Lista de filtros → menú de tres puntos → **Exportar** → copia el filtro como **cadena base64** al portapapeles. Importar pega un código.

Existen decodificadores comunitarios (d4lootfilter.com, diablofilter.com) que traducen el código a reglas legibles: tipos de objeto, afijos exigidos, visibilidad, colores, reglas por clase.

**Lo que NO contiene:** tus objetos, tu personaje, tus habilidades. Son **plantillas de reglas**.

Dos consecuencias:

1. **Prueba que el juego puede escribir al portapapeles.** La vía "portapapeles" no está muerta por principio, solo no cubre el personaje.
2. **Aparece un competidor parcial.** Parte de lo que resolvía una herramienta como la nuestra ("¿este objeto merece la pena?") ahora lo resuelve el juego de fábrica, y encima con código compartible. Conviene decidir explícitamente si nuestra herramienta se apoya en ese formato o lo ignora.

---

## 7. Frontera legal: qué se sabe y qué no

- La EULA prohíbe software no autorizado que "automatice, modifique o interfiera de otro modo" con el juego. **No hay lista blanca ni proceso de aprobación** — confirmado en el hilo del foro y consistente con lo que dice el encargo.
- El único pronunciamiento concreto localizado señala a **TurboHUD4**: *"TurboHUD4, like any game-modifying software, is prohibited for use with Diablo IV. Players who install this kind of software will put their accounts at risk for disciplinary action, which can include permanent suspension."*
- El criterio que circula en la comunidad (foro oficial, **usuario, no Blizzard**): *"¿Te enseña datos de Diablo 4 que no puedes ver con las funciones del juego? Si sí, no lo uses."*
- **No he encontrado** ni una sola oleada de baneos documentada contra usuarios de d4lf o D4Companion, ni un pronunciamiento de Blizzard sobre herramientas basadas en el lector de pantalla. Ni a favor ni en contra. **Ausencia de evidencia, no evidencia de ausencia.**
- Ni d4lf ni D4Companion incluyen aviso alguno de ToS o riesgo de baneo en su README, pese a lo que hacen. Eso es un dato sobre ellos, no una garantía para nosotros.

---

## 8. Qué copiaríamos, en concreto

1. **Los `.stl` como origen del vocabulario.** Generar el diccionario de afijos en español desde la instalación del jugador con D4Analyzer + un parser al estilo de `diablo-4-string-parser`. Elimina la transcripción a mano, se actualiza solo con cada parche, y no cruza ninguna línea roja.
2. **El contrato de d4-item-tooltip-ocr: imagen → JSON.** Aislar el parser del capturador. Con esa frontera, cambiar OCR por TTS más adelante es sustituir un módulo, no reescribir la herramienta.
3. **Los *buckets* de daño de bytemind d4-tools.** Es JavaScript abierto y ya modela aditivo vs multiplicativo, crítico, vulnerable, overpower. Es exactamente el corazón del valorador de afijos del diseño actual; conviene contrastarlo antes de escribir el nuestro.
4. **El "Vision Mode Only" de d4lf como principio, no como opción.** Nunca tocar el ratón ni el teclado del juego. Ellos lo tienen como ajuste; nosotros lo tenemos como restricción dura, y eso ya nos deja mejor colocados.
5. **La tabla de presets de D4Companion como presupuesto realista.** Si se sigue con OCR, hay que asumir de entrada una matriz resolución × escala de fuente × HDR, y exigir HDR apagado y fuente pequeña/media como requisito documentado, igual que hacen los dos proyectos vivos.
6. **Importar el rival desde un planificador, no desde el juego.** d4lf y D4Companion importan builds de Maxroll, D4Builds, Mobalytics e InfinityBuilds. Para el perfil "rival" del diseño actual eso es mejor fuente que capturar la pantalla de otro: es texto estructurado y ya hay parsers de referencia.
7. **`D4TTS` (josdemmers) como prueba de concepto de una tarde.** Si se quiere evaluar la vía TTS sin comprometerse, es el experimento más barato: montar la DLL, ver qué cadenas emite el cliente **en español** al pasar el ratón por los 10 huecos de equipo y las 6 habilidades, y decidir con datos.
8. **Leer el código del filtro de botín oficial desde el portapapeles.** Vía 100 % limpia y ya existente: el usuario pulsa Exportar en el juego, nuestra herramienta lee el base64. No da objetos, pero da las preferencias del jugador sin captura ni OCR.

---

## Fuentes

Páginas abiertas de verdad durante esta investigación:

**Repositorios y código**
- https://github.com/d4lfteam/d4lf
- https://github.com/d4lfteam/d4lf/blob/main/README.md
- https://raw.githubusercontent.com/d4lfteam/d4lf/main/README.md
- https://github.com/d4lfteam/d4lf/releases
- https://github.com/d4lfteam/d4lf/blob/main/tts/saapi.cpp (leído vía `gh api repos/d4lfteam/d4lf/contents/tts/saapi.cpp`)
- https://github.com/d4lfteam/d4lf/blob/main/tts/install_dll.cmd (ídem)
- https://github.com/josdemmers/Diablo4Companion
- https://github.com/josdemmers/D4TTS
- https://github.com/mxtsdev/d4-item-tooltip-ocr
- https://github.com/Lothrik/diablo4-build-calc
- https://github.com/DiabloTools/Diablo4Tools-Releases
- https://github.com/DiabloTools/d4data
- https://github.com/blizzhackers/d4data
- https://github.com/alkhdaniel/diablo-4-string-parser
- https://github.com/bytemind-de/d4-tools
- https://github.com/Dakota628/d4parse
- https://github.com/mfloob/diablo4-data-harvest
- https://github.com/ryancollingwood/diablo_4_armory_fetcher
- https://github.com/shalzuth/Diablo4DpsMeter
- https://github.com/cagartner/awesome-d4
- API de GitHub (`api.github.com/repos/...`) para estrellas, lenguaje, fecha de push y estado de archivado de todos los anteriores

**Blizzard: foros, soporte, noticias**
- https://us.forums.blizzard.com/en/blizzard/t/diablo-4-api-d4armory/45191
- https://us.forums.blizzard.com/en/d4/t/3rd-party-screen-readers-no-longer-function-in-season-12/242596
- https://us.forums.blizzard.com/en/d4/t/copy-paste-item-information-feature-proposal/137085
- https://us.forums.blizzard.com/en/d4/t/where-are-saved-game-files-located/46682
- https://us.forums.blizzard.com/en/d4/t/third-party-app-diablo-iv-overlay-is-permitted-modcheck/41715
- https://news.blizzard.com/en-us/article/23954932/combatting-demons-with-accessibility-in-diablo-iv
- https://community.developer.battle.net/documentation (redirección desde develop.battle.net)
- https://eu.support.blizzard.com/en/article/13078 (redirección desde us.battle.net/support/en/article/13078)

**Terceros**
- https://d4armory.io/ — devuelve **301 → https://diablo4.com/**
- https://www.icy-veins.com/d4/news/blizzards-stance-on-unauthorized-game-modifying-software-in-diablo-iv/
- https://www.d4lootfilter.com/

---

## No encontrado

Huecos declarados. Ninguno de estos se ha rellenado con suposiciones.

1. **Confirmación en primera persona de que el TTS emite en español.** El mecanismo debería devolver el texto en el idioma del cliente, pero **no lo he verificado**: d4lf exige inglés y el motivo (limitación de su parser, o del propio TTS) no está documentado. **Es la incógnita que más cara sale si se apuesta por esta vía.** Se resuelve en una tarde con D4TTS y un cliente en español.
2. **Estado exacto del lector de terceros hoy.** El reporte de rotura de la temporada 12 (marzo 2026) quedó sin resolver y sin respuesta de Blizzard. Que d4lf tenga push del 28-08-2026 es indicio fuerte de que funciona, pero **no he encontrado una confirmación explícita** de que la ruta SAAPI siga operativa en la temporada actual.
3. **Postura de Blizzard sobre herramientas basadas en accesibilidad.** No existe pronunciamiento, ni a favor ni en contra. No hay lista blanca. No hay oleada de baneos documentada contra d4lf o D4Companion. **El silencio no es permiso.**
4. **Contenido del portal de desarrolladores de Battle.net.** `community.developer.battle.net/documentation` es una SPA que devuelve solo el esqueleto HTML (`<app-root></app-root>`); **no he podido leer el listado real de APIs**. La conclusión de que no hay API de D4 se apoya en el hilo del foro y en la ausencia total de clientes que la usen, no en la documentación leída de primera mano.
5. **Cómo obtenía d4armory.io los datos.** Nunca se supo. Las hipótesis del foro iban de scraping a inyección; el autor de bytemind d4-tools escribió literalmente *"d4armory seems to be able to do it, but how???"*. Muerto y sin autopsia.
6. **Si existe algún log de combate.** `Diablo4DpsMeter` sugería que sí, pero **el repositorio no contiene código alguno**. No hay ninguna evidencia de que Diablo IV escriba logs de combate legibles. Lo doy por no existente, con esa reserva.
7. **Inventario exacto de `Documents/Diablo IV/`.** Confirmado `LocalPrefs.txt` y carpetas `BlizzardError/ReportedBugs/`. **No he podido enumerar la carpeta completa** ni descartar al 100 % una caché no documentada. Comprobación de 30 segundos en la máquina del jugador.
8. **Especificación del formato del código de filtro de botín.** Sé que es base64 y qué campos codifica (tipos, afijos, visibilidad, colores). **No he encontrado ninguna especificación pública del esquema binario** ni un decodificador de código abierto; los que hay (d4lootfilter.com, diablofilter.com) son servicios web cerrados.
