# Arte previo: la herramienta de escritorio, revisada contra lo que ya existe

**Fecha:** 29 de agosto de 2026.
**Fuente:** los seis informes `crudo/arte-*.md`, sus cuatro refutaciones, y una verificación propia
(9 búsquedas, 14 páginas y ficheros abiertos, metadatos de 12 repos leídos vía `gh api` ese mismo día).
**Pregunta que gobierna todo el documento:** *de dónde salen los datos*.

**Aviso de encuadre.** Los informes previos preguntaban «¿es correcto nuestro diseño?» y la respuesta
era «sí, con matices». Preguntando en cambio «¿qué de esto está ya construido?», la respuesta cambia
de forma incómoda: **el 70 % de la herramienta existe, con licencia MIT, y no necesita OCR.** Lo que
falta es justo la pieza más frágil. Ese es el hilo del documento.

---

## ¿Hace falta OCR?

**Respuesta corta: sí, y solo para una cosa — leer tus propios 10 huecos de equipo. Todo lo demás
del diseño se resuelve sin tocar un píxel, y ya está resuelto por otros.**

### Por qué sí: las seis vías limpias están cerradas

La industria conoce siete formas de sacar estado de un juego. Diablo IV cierra las seis primeras.
Verificado hoy, no heredado:

| Vía | ¿Existe en D4? | Evidencia |
|---|---|---|
| API web oficial con OAuth | **No** | El portal de desarrolladores de Battle.net cubre WoW, **Diablo III**, SC2 y Hearthstone. No D4. Un moderador en el foro de API: *"there is no d4 api yet"* |
| API no oficial (`d4armory.io`) | **Muerta** | `curl -D` → `HTTP/2 301` → `https://diablo4.com/`. Su *fetcher* (`ryancollingwood/diablo_4_armory_fetcher`) está **archivado** |
| API local en puerto (estilo LoL 2999) | **No** | Sin equivalente documentado |
| Addons / mods | **No** | D4 no tiene sistema de addons |
| Log de partida en disco | **No** | `FenrisDebug.txt` es log de motor (TACT, `[CRASH]`), no de gameplay. No hay log de combate: es petición recurrente y sin atender en los foros oficiales |
| Portapapeles con el objeto (estilo PoE Ctrl+C) | **No** | Verificado de nuevo el 29-ago-2026: el Armory interno tiene Guardar / Cargar / Renombrar y nada más; el Ctrl+C sobre objeto sigue siendo una **propuesta de foro** de nov-2023 sin implementar |
| Eventos vía Overwolf (GEP) | Sí, **inútil** | Expone `game_info` (BattleTag, oro), `match_info` (Pozo), `location`, `me` (clase, nivel, paragón, vida). **Cero inventario, cero afijos** |

Queda el peldaño 7, captura + OCR. Y una vía gris, el lector de pantalla.

### La vía sin OCR que existe, y por qué no es nuestra

Diablo IV carga `saapi64.dll` desde su propia carpeta si está firmada, y le entrega por
`SA_SayW(const wchar_t*)` cada texto que narraría a un lector de pantalla. `d4lf` sustituye esa DLL
por una propia que reenvía el texto por una *named pipe* `\\.\pipe\d4lf`.

Tres correcciones al relato que circula, todas verificadas:

1. **No es «la interfaz de accesibilidad de Windows».** SAAPI es la API de **un solo producto
   comercial minoritario, System Access de Serotek**. Tolk tiene un driver distinto por lector: JAWS
   va por COM, NVDA por `nvdaControllerClient64.dll`. Estás suplantando a un proveedor concreto, no
   usando un estándar. Si el jugador usa System Access de verdad, le rompes su lector.
2. **No está rota.** El informe `arte-trackers` la daba por muerta desde la temporada 12; su
   refutación lo desmontó y lo he vuelto a confirmar: el README de `d4lf` (push del 28-ago-2026)
   titula su instalación *«New instructions for season 12 that must be followed!»*. Lo que Blizzard
   cambió fue **exigir firma Authenticode**; el instalador responde creando un certificado
   autofirmado y metiéndolo en el **Trusted Root del usuario**. Funciona hoy.
3. **Nadie ha demostrado que baste sola.** El README de `d4lf`, literal: *"D4LF gets item information
   by **reading the screen and** using TTS information sent for accessibility."* Es TTS **más** OCR.
   Por eso sigue exigiendo HDR apagado, escala de fuente pequeña o media y «Advanced Tooltip
   Information» activado — requisitos de *lectura de pantalla*, no de TTS. La tabla del informe
   `arte-d4-datos` que promete «cadena exacta, insensible a resolución, CPU casi nula» describe un
   sistema que **ningún proyecto verificado ha construido**.

Se descarta, y basta con una razón: es un binario nuestro corriendo dentro del proceso de Diablo IV.
Que lo cargue el juego voluntariamente no cambia dónde se ejecuta. Además exige administrador,
cerrar el juego y un certificado autofirmado en el almacén raíz del usuario — para una herramienta
personal, eso es un coste de instalación desproporcionado y una superficie de confianza que no
queremos pedirle a nadie.

### Por qué el «sí» es mucho más pequeño de lo que parece

Aquí está el hallazgo que cambia el proyecto. **Tres de las cuatro piezas del diseño no necesitan
OCR y ya están escritas:**

| Pieza del diseño | ¿Necesita OCR? | Ya existe |
|---|---|---|
| Vocabulario de afijos en español | **No** | `Affixes.esES.json` de Diablo4Companion: **891 entradas verificadas hoy** (`len()` sobre el fichero descargado), con `Description` (`+#% de daño contra enemigos de élite`) y `DescriptionClean` (`de daño contra enemigos de élite`) ya separados. Y con él vienen `Aspects`, `Uniques`, `Runes`, `Sigils`, `ItemTypes`, `ParagonBoards`, `ParagonGlyphs`, **los ocho en esES**, MIT |
| Valorador por grupos de daño | **No** | `jlian/d4-damage-calc` (MIT, TypeScript) implementa los 15 *buckets* (`CSDM`, `VDM`, `DOTM`, `ALLM`, `NONPHYS`, `ADDITIVE`, `CRITADD`, `MAINSTAT`, `WEPDMG`, `CRITCHANCE`, `SKILLRANK`, `EXTRAMULT`…) y la función `weightFor()`, que devuelve **la ganancia marginal de un roll típico en cada grupo** — literalmente «lo lleno que esté su grupo». Con escenarios (plain / vulnerable / élite) y tests |
| Perfil «rival» | **No** | `d4lf` y `Diablo4Companion` importan builds de Maxroll, D4Builds, Mobalytics, InfinityBuilds y D2Core. Texto estructurado, con parsers de referencia ya escritos |
| **Perfil «yo»: tus 10 huecos + 6 habilidades** | **Sí** | Nadie. Es el único hueco real |

Y hasta ese último «sí» hay que mirarlo de frente: son **unos 40 números que cambian tres veces por
sesión**. `d4-damage-calc` los resuelve con un formulario y un enlace compartible, y lo usa gente. La
pregunta honesta no es «¿OCR o no?», es «**¿merece la pena un pipeline de visión por computador en
español, que nadie ha construido nunca, para ahorrarte teclear 40 números?**». Puede que sí — es tu
tiempo y tu tecla. Pero eso es lo que se está comprando, y conviene decirlo antes de escribir la
primera línea, no después.

**Si la respuesta es sí, el OCR se construye *encima* de las tres piezas que ya existen, no en lugar
de ellas.** El orden correcto es: primero la calculadora funcionando con entrada manual, después el
OCR como acelerador opcional de esa entrada. Al revés, si el OCR falla en español —y no hay ni una
medición publicada que diga que no— no queda herramienta.

---

## Qué copiamos

Ordenado por relación valor/esfuerzo. Cada punto con su repo.

**1. El catálogo esES entero de Diablo4Companion. Hoy mismo.**
`https://github.com/josdemmers/Diablo4Companion` → `D4Companion/Data/*.esES.json`. MIT, `Copyright (c)
2022 Jos Demmers`, atribución obligatoria. 891 afijos con `DescriptionClean` ya limpio de números y
símbolos: es exactamente la clave contra la que emparejar. `IdSno`/`IdName` son identificadores
internos del juego, estables entre parches e idiomas — úsalos como identidad canónica, nunca el texto
en español (es la lección de `ref` del `stats.ndjson` de PoE, y aquí viene resuelta de fábrica).
*Esto elimina la tarea más aburrida y más cara del proyecto.*

**2. El motor de valoración de `jlian/d4-damage-calc`.**
`https://github.com/jlian/d4-damage-calc` → `src/calc.ts`, `src/calc.test.ts`, `src/sample-paladin.json`.
MIT. Portar, no reescribir. Y leer el aviso: está anclado a **Season 13 (Lord of Hatred)**, con push
de junio de 2026; el parche vivo del proyecto es **3.1.3 / Season 14**. Los `baseDamage` por tipo de
arma y los divisores de estadística principal hay que revalidarlos contra el parche, exactamente
igual que se hace con el resto de la guía.

**3. La captura bajo atajo, con precedente en Diablo IV.**
`https://github.com/Goosterhof/horadric-cube` (Tauri v2 + Rust + Vue, push 25-ago-2026, 0 ★). Su
pipeline es punto por punto lo que los informes recomendaban «trasplantar desde PoE», solo que ya
existe **en nuestro juego**: escucha un único atajo global (`Ctrl+Shift+H`), captura **la región de
tooltip configurada** —no la pantalla—, OCR local, parseo a JSON, y borra el PNG. Su sección *The
Horadrim's Oath* («No game memory access. No process injection. No network interception. No client
modification.») es el README que nos hace falta, ya redactado.
**Dos cosas que NO se copian:** manda el payload a un servidor remoto (`horadrim.zmuuzn.nl`) —
dependencia de red que no tenemos ni debemos adquirir; y su defensa legal es *«inherits its
safe-harbor by design proximity»* con Diablo4Companion, que no es un argumento, es una esperanza.

**4. El motor de OCR y el preprocesado medidos de `ferpgshy/d4forge`.**
`https://github.com/ferpgshy/d4forge` → `d4forge/vision/ocr.py` y `preprocess.py`. GPL-3.0 (ojo con
la licencia: leer, no copiar y pegar). Es el proyecto que más se parece a lo que necesitamos en la
capa de visión, y lo tiene **medido y comentado en el código**:
- **Caché exacta por hash de contenido:** `~0,2 ms` si ya vio esa línea, `30-90 ms` la primera vez.
  Funciona sin falsos positivos porque *el juego renderiza la misma línea con exactamente los mismos
  píxeles*, y los rolls salen de un conjunto finito, así que la caché satura con el uso.
- **Binarizar y ampliar por repetición de píxel, con margen blanco.** Motivo documentado: en escala
  de grises el OCR leía la marca de agua *«PUBLIC TEST BUILD»* junto con el texto; sin margen, el
  detector se comía las puntas y `+151 Dexterity` salía como `ext`.
- **Gris por canal máximo, no por luma ponderada**, porque el texto de D4 tira a amarillo.
- **Leer la línea entera, no trocearla fino.** Lo midieron: separar valor y nombre para cachear cada
  mitad salía más rápido y **mucho menos preciso** (`+2 to Imbuement Skills` → `to kil`). Esto
  **contradice** la recomendación de «trocear antes del OCR» de `arte-trackers`. Localizar el tooltip
  (recorte grueso) está bien respaldado; trocear en fragmentos finos tiene una medición en contra.
- **Cobertura como control de calidad:** `COVERAGE_OK = 0.95`, calibrado sobre recortes reales porque
  a 0,85 una lectura que se comía el `+1,` de `+1,431 Maximum Life` pasaba valiendo 431.
- **`CACHE_VERSION`**, que se sube cuando cambia el preprocesado o la gramática: si no, una lectura
  mala grabada en el pasado sigue volviendo lista y escapa de toda corrección posterior.
- **Fixtures PNG reales en `tests/fixtures/`** (`linha_1431_maximum_life.png`, `locked_x22_shadow_multiplier.jpg`…).
  Es el patrón de HearthSim (`python-hslog`) aplicado aquí: el parser es una librería con su batería
  de imágenes, ejecutable sin juego y sin GUI.

**5. El emparejamiento difuso como corrector del OCR, con el scorer correcto.**
`d4lf` (`src/perception/text.py`) usa `rapidfuzz` con `Levenshtein.distance`; `Diablo4Companion`
(`OcrHandler.cs`) usa `DefaultRatioScorer`. Y el comentario que hay que leer antes de elegir, textual
en el código de Diablo4Companion: `TokenSetScorer` *elige el equivocado `+#% Damage` en vez del más
largo `+#% Shadow Damage Over Time`*. **En español pasa idéntico**: «de daño» es subcadena de «de
daño de sombra a lo largo del tiempo». Ratio sobre la cadena completa, nunca token-set.
Y el patrón de los dos caminos: **el texto sin números se empareja contra el catálogo; el número se
extrae aparte** (`find_number()` / `TextToAffixValue`).

**6. El esquema del afijo, de Path of Exile.**
`https://github.com/Kvan7/Exiled-Exchange-2` → `renderer/src/assets/data/interfaces.ts`. Tres campos
que nos faltan y que valen oro: `better: -1 | 0 | +1` (**el signo, y que exista `NotComparable`**, sin
lo cual hay que inventar heurísticas para los afijos que no se comparan), `negate` (ganar/perder con
un solo afijo canónico), y `value` para los singulares donde el número está incrustado en el texto.

**7. `unknownModifiers[]` + `rawText`.**
`awakened-poe-trade`, `renderer/src/parser/ParsedItem.ts`. No tirar las líneas que no se reconocen:
guardarlas aparte **y guardar el texto crudo entero**. Un parser de vocabulario cerrado que descarta
en silencio miente sin que nadie se entere. En nuestro caso vale doble: una línea desconocida puede
ser un afijo nuevo *o* un fallo de OCR, y solo se distinguen mirando el crudo.

**8. La guarda de sanidad antes de parsear.**
`isPoeItem()` de `awakened-poe-trade` (`main/src/shortcuts/HostClipboard.ts`). Equivalente nuestro:
no aceptar una lectura que no tenga forma de tooltip de D4 en español. Y de d4forge, `plausible_line()`:
descartar lo que empieza por `.7%` o `,425`, porque una línea del juego nunca empieza así.

**9. La ROI relativa a la ventana del juego y la caché de frame.**
`d4lf`, `src/perception/capture/core.py`: localiza la ventana, guarda `{top,left,width,height}`,
captura **solo eso**, cachea el frame 40 ms, desactiva `CAPTUREBLT` (evita capas superpuestas y
acelera) y deriva la clave de resolución del tamaño de ventana.

**10. Fail-closed en la duda.**
De d4forge, y encaja con la doctrina del proyecto: *«leitura duvidosa e' marcada como tal e o engine
trata duvida como "nao trocar"»*. Una lectura dudosa no es un dato con asterisco al final: es un dato
que no se usa.

**11. El formato del filtro de botín, ya descifrado.**
`https://github.com/Upsilon72/d4-filter-generator` (MIT, HTML+JS, push 11-may-2026). Cierra el «no
encontrado» de `arte-d4-datos` sobre el esquema base64: **es Protocol Buffers binario codificado en
base64**, y hay ~80 líneas de JS vanilla que lo generan en cliente, con **77 IDs de afijo verificados**
uno a uno exportando filtros de un solo afijo desde el juego. No da tus objetos —son reglas—, pero es
una vía 100 % limpia por portapapeles hacia las **preferencias declaradas** del jugador. Aviso: 2 ★, un
autor, y los IDs de rangos de habilidad solo están confirmados para Warlock.

---

## Qué sobra de nuestro diseño

Sin rodeos, por orden de cuánto pesa.

**1. El bucle de 0,7 segundos. Fuera.**
Es la peor decisión del diseño y no tiene ni una razón que la sostenga. La justificación que quedaba
en pie —«hay una trampa de latencia»— era un artefacto: los «1-3 segundos por captura» venían de
`mivuorin/d4-ocr`, **0 ★, abandonado en febrero de 2024**, Tesseract contra pantalla completa. d4forge
mide 30-90 ms por línea. El sondeo continuo no compra velocidad; compra tres problemas: CPU quemada,
capturas que se solapan consigo mismas, y —lo importante— **te saca de la categoría que la comunidad
defiende con éxito desde hace doce años**. Una pulsación, una lectura. `horadric-cube` ya lo hace así
en Diablo IV con `Ctrl+Shift+H`, y `RegisterHotKey` ya está en el diseño para exactamente esto.

**2. La captura de pantalla completa. Fuera.**
Nadie del arte previo hace OCR sobre la pantalla entera. Ventana del juego → región del tooltip →
OCR del recorte. Es lo que hace viable cualquier presupuesto de tiempo.

**3. El checklist en vivo de 10+6 que «no termina hasta verlo todo». Fuera, y es la que más urge.**
Tiene tres defectos a la vez:
- **Es el único punto del diseño que genera patrón de comportamiento.** El riesgo real no es la
  detección en cliente (ver la sección siguiente): es el análisis del lado servidor. Una mecánica que
  empuja al jugador a barrer sus 10 huecos de forma sistemática y repetible es exactamente el perfil
  que no queremos dibujar, y **no compra nada** que no compre un formulario.
- **Fabrica un problema para venderte la solución.** El estado «me faltan 3 huecos por escanear» solo
  existe porque hemos decidido que los datos entren por la pantalla. Con entrada manual el estado es
  «hay 3 campos vacíos», que ya lo resuelve un formulario desde 1995.
- **Convierte una ayuda en una tarea.** El jugador quería saber si un objeto es mejor; le hemos dado
  deberes.

**4. Escribir nuestro propio valorador de grupos de daño. Fuera.**
Está hecho, en MIT, con tests, con escenarios y con Paladín incluido. Portar `calc.ts` y revalidar sus
constantes contra el parche 3.1.3 es trabajo de una tarde. Reimplementar la fórmula de Avarilyn desde
cero es trabajo de una semana con más superficie de error.

**5. Transcribir el vocabulario de afijos en español a mano. Fuera.**
891 entradas ya limpias, MIT. Y si algún día hiciera falta regenerarlo, la vía documentada es leer los
`.stl` de la instalación del propio jugador (`DiabloTools/Diablo4Tools-Releases` +
`alkhdaniel/diablo-4-string-parser`), que es leer ficheros de tu ordenador, no memoria del juego.

**6. El perfil «rival» por OCR. Fuera.**
Capturar la pantalla de otra persona para reconstruir su build es la peor relación esfuerzo/resultado
del proyecto. Los dos proyectos vivos de D4 importan de Maxroll, D4Builds, Mobalytics, InfinityBuilds
y D2Core. Y `d4-damage-calc` ya empaqueta un build entero en el hash de una URL: «pásame tu enlace».

**7. El parser de «vocabulario cerrado» entendido como emparejamiento estricto. Reformular.**
El vocabulario cerrado es correcto y es el consenso — pero su función no es parsear, es **corregir**.
El OCR no tiene que acertar; tiene que acercarse lo bastante a una entrada de una lista finita. Un
emparejamiento estricto convierte cada fallo de una letra en un afijo perdido en silencio; el difuso
lo convierte en un afijo correcto o en un aviso. Umbral expuesto en la interfaz, como hace
Diablo4Companion.

**8. `tkinter`. Fuera.**
Nadie del arte previo lo usa: `d4lf` va con PyQt6, `d4forge` con **PySide6 (LGPL, que es la que
quieres)**, `Diablo4Companion` con WPF, `horadric-cube` con Vue en Tauri. Y para nuestra UI concreta
—tabla comparativa de afijos, dos perfiles en paralelo— tkinter no tiene tabla decente y sale borroso
a 125/150 % de escala.

**9. El paquete `winocr` como dependencia. Fuera; el motor, discutible (ver stack).**
`GitHub30/winocr` son ~50 líneas, 25 ★, sin push desde el **25-oct-2024**. Hace `asyncio.run()` por
fotograma y serializa el resultado recorriendo `dir(o)` con `getattr` sobre cada atributo de cada
palabra. Si se usa el motor nativo, se absorben las 15 líneas contra `winrt-windows-media-ocr`, con
el `OcrEngine` creado **una sola vez**, y se elimina una dependencia huérfana.

**Lo que NO sobra y no se toca:** `RegisterHotKey` en vez de hook de teclado; ventana propia sin
overlay; nada de memoria, nada de inyección, nada de automatizar entradas; perfiles en fichero local.
Esa combinación es **más estricta que la de todo el arte previo, sin excepción**, y es lo mejor que
tiene el diseño.

---

## Dónde está la línea del baneo

### Lo primero, porque es la pregunta directa

**No existe ni un solo caso documentado de baneo sostenido por captura de pantalla + OCR en Diablo IV.**
Hay **un** caso de baneo con OCR de por medio; se revirtió en dos días con disculpa explícita; y la
evidencia nueva apunta a que **el OCR ni siquiera fue la causa**.

### El caso `diablo_qol`, y lo que nadie había cruzado

Agosto de 2023. Un jugador usa una herramienta que hace exactamente lo nuestro —captura tooltips, los
pasa por OCR, indexa alijo e inventario— y que su propio autor describe así: *"takes screenshots of
item tooltips and then uses image to text ... **and does not access game memory**"*. Baneo Error 52 el
**11 de agosto de 2023**, motivo «malicious 3rd party software». Reinstauración el **13 de agosto**,
sin apelación, con este texto de Blizzard, verificado palabra por palabra:

> "After an additional review of the evidence, we determined this closure was an error. We're
> reopening this account for play, and hope you will accept our sincere apologies for the mistake."

**El dato que cambia la lectura y que no aparece en ningún informe previo:** abrí el hilo hermano de
la misma oleada (*«Another one banned for alleged use of malicious 3rd party software today»*, mismas
fechas, mismo Error 52, misma reversión el 12 de agosto). Los baneados de ese hilo **no usaban OCR**:
identifican como sospechosos un **nodo minero de Chia (basado en Python)** y el **Easy Anti-Cheat de
una instalación de Star Citizen**, y varios confirman estar corriendo el minero al ser baneados.

Es decir: en agosto de 2023 hubo una **oleada de falsos positivos contra procesos de terceros no
relacionados**, y `diablo_qol` cayó dentro. La cadena causal «OCR → baneo» **nunca se estableció**. El
único caso que la comunidad cita como precedente contra el OCR probablemente no lo sea.

Eso no lo convierte en permiso. Lo convierte en otra cosa, más útil y más incómoda: **el riesgo real
no es que te detecten haciendo OCR, es que te barra una heurística amplia por algo que ni siquiera
tiene que ver contigo.**

### El caso en contra, y la inferencia que hay que etiquetar

Mismo mes, mismo foro: un desarrollador cuenta que su filtro hace OCR con Tesseract **y luego AutoHotkey
pulsa la barra espaciadora** para marcar el objeto como basura. La comunidad lo entierra. TheTias-1192,
28-ago-2023, cita la EULA y remata: *"avoid a ban by not using your OCR software"*.

Los informes previos concluyen que «la diferencia entre los dos casos no es el OCR, es que el segundo
enviaba pulsaciones». **Eso es una inferencia nuestra, no lo que dice la fuente**: TheTias condenó el
OCR, sin más; nadie del hilo señaló el AHK. La inferencia probablemente es correcta como modelo del
riesgo real, pero se etiqueta como lo que es. Y no hubo respuesta oficial en ese hilo tampoco.

### El resto del expediente, ordenado

| Caso | Qué hacía | Resultado | ¿Sostenido? |
|---|---|---|---|
| **TurboHUD4** (jul-2023) | **Lee memoria del proceso**, maphack | **Prohibido por Blizzard, por su nombre** | Sí. Es la única herramienta que Blizzard ha nombrado jamás |
| Macro AHK de clic derecho (jun-2023) | Bucle de clics | Baneo permanente | **Autoinformado.** Blizzard no confirmó causa ni desenlace |
| Oleadas D3 (2015-16) | Bots, TurboHUD, D3Helper **y macros AHK** | Baneos masivos | Sí, pero la fuente **no separa** macro puro de bot en la misma cuenta |
| POE Overlay (2020) | Se citaba como «baneo por overlay» | **Mal atribuido** | Los bloqueos fueron por **martillear la web de GGG con millones de peticiones diarias**. No tiene nada que ver con overlays |
| `diablo_qol` (ago-2023) | Captura + OCR, sin memoria | Baneo **revertido en 2 días**, con disculpa | No. Y probablemente ni siquiera fue por el OCR |
| **Diablo4Companion** (321 ★) | Captura + Tesseract + **dibuja overlay**, años en producción | **Cero baneos reportados** | — |
| **d4lf** (206 ★) | OCR + **DLL que el juego carga** + **automatiza el ratón** | **Cero baneos reportados** | — |
| **`RegisterHotKey`** | — | **Cero casos en cualquier juego** | — |

Ese último bloque es la señal empírica más fuerte del expediente, y va en las dos direcciones a la
vez: dos herramientas que cruzan **tres** de nuestras cuatro líneas rojas llevan años funcionando sin
una sola oleada documentada contra sus usuarios. Eso dice mucho sobre la **detección** y absolutamente
nada sobre el **permiso**.

### Lo que dice el texto, completo esta vez

De la EULA, verificado hoy contra el documento original. La cláusula de *Data Mining*, **entera**:

> "Use any unauthorized process or software that intercepts, collects, reads, or 'mines' information
> generated or stored by the Platform; **provided, however, that Blizzard may, at its sole and
> absolute discretion, allow the use of certain third-party user interfaces.**"

La primera mitad es la que un revisor hostil nos aplicaría: una captura de pantalla *lee información
generada por la Platform*, literalmente. La segunda mitad —que los informes previos citaban truncada—
es **el único punto de toda la sección 1.C que contempla explícitamente interfaces de terceros**. No
autoriza nada: es discrecional y Blizzard nunca la ha ejercido públicamente para D4. Pero desmonta la
idea de que sea la cláusula «más difícil de esquivar»: es la única que trae una válvula incorporada.

Y confirmado por búsqueda directa sobre el texto: **la EULA no menciona captura de pantalla, overlay,
OCR ni streaming en ningún punto.** El problema es el silencio, no la prohibición.

### Blizzard nunca ha dicho que sí. Tampoco ha dicho que no.

- Hilo «Third Party App: Diablo IV overlay is permitted? #ModCheck», siete páginas: **cero blue posts**.
- Hilo «I made an OCR Equipment Filter tool, is it legal?»: **cero**.
- Hilo del baneo de `diablo_qol`, con petición explícita de aclaración: **cero**.
- Hilo «Is using Diablo4Companion safe from bans?», abierto hoy para esta verificación: **cero**. Solo
  jugadores diciéndose unos a otros *«you're risking a ban, don't use it if you value your account»*,
  sin un solo análisis técnico detrás. El autor del hilo acabó escribiendo a soporte.
- La única declaración oficial (PezRadar, 26-jul-2023) prohíbe *"cheating, bots, hacks, and any other
  unauthorized software which automates, modifies, or otherwise interferes with the game"*, nombra a
  TurboHUD4 y a nadie más, y **no define ninguna categoría técnica**.
- **MissCheetah-1661**, citada por medio internet como autoridad, **es una jugadora del foro**: *"I am
  another player, not a Mod."* La frase fuerte que se le atribuye («Blizzard does not allow any third
  party software use that touches their games, in any way») **no se ha podido localizar**. Lo que sí
  dijo es más flojo y dice otra cosa: *"Blizzard will not approve any third party software"* — eso es
  «no te lo bendicen», no «no te lo permiten».

### El criterio operativo, sin atribuciones falsas

El «test del segundo ordenador» (*si te llevas los datos a otra máquina y el programa sigue
funcionando, está bien*) es una buena vara de medir y nuestro parser la pasa: dale un PNG y funciona
en una máquina sin Diablo IV. Pero **su fuente primaria devuelve 403 y nadie la ha leído**, ni el autor
del informe ni yo. Se adopta como **heurística propia del proyecto, sin atribuírsela a Chris Wilson ni
a nadie**. La declaración de GGG que sí está verificada (CoryA_GGG) dice lo mismo con menos elegancia:
*"we're unable to guarantee if a tool is allowed or would remain allowed in the future."*

### Consecuencias prácticas, sin teoría

1. **La línea que no se cruza es enviar entradas al juego.** Es lo único que separa el caso revertido
   del caso condenado, y el precedente masivo de D3 apunta ahí. No negociable.
2. **El riesgo residual es el falso positivo, no la detección.** Warden corre en modo usuario dentro
   del proceso; los bots de píxeles ni lo notan y aun así acaban baneados, por análisis de
   comportamiento del lado servidor. **Ser indetectable en cliente no es una defensa.** Lo que protege
   es no generar el patrón — y eso se consigue no automatizando nada y no sondeando en bucle.
3. **El coste del peor caso es peor de lo que se contaba.** El caso de Error 52 del 28-dic-2025 se
   revirtió el 2-ene-2026 (cinco días, no seis, y motivo nunca revelado) **y el usuario siguió sin
   poder entrar**, porque el error persistía por el lado de Steam. El peor caso realista no es «unos
   días y vuelves»; es «te lo reconocen como error y aun así no entras».
4. **`RegisterHotKey` es la mejor decisión del diseño, con un asterisco.** Cero casos en cualquier
   juego, y a diferencia de un hook global no ve todo el teclado. Pero **suprime esa tecla para la
   aplicación en primer plano**: si D4 tiene el foco, no recibe la pulsación. Es inocuo, pero no es
   «no tocar el juego en absoluto». Elegir teclas que D4 no use y documentarlo.
5. **Escribir la sección «de dónde salen los datos y de dónde no» en el README, como hacen
   `horadric-cube` y `d4-ocr`.** Y **no afirmar que está aprobado**: ni siquiera Awakened PoE Trade lo
   hace. El argumento de buena fe más fuerte que tenemos es documental: la única fuente de datos de D4
   con acuerdo de publisher (el GEP de Overwolf) expone vida, nivel y coordenadas, **y ni un solo
   afijo**. No estamos esquivando una API que existe.

---

## El stack

**Veredicto: `mss` y `RegisterHotKey` se quedan. `tkinter` se cae. `winocr` se cae como paquete y es
dudoso como motor. Y hay que decidir antes si esto es una app de escritorio o media app.**

| Pieza | Veredicto | Por qué |
|---|---|---|
| **Python** | **Se queda**, en **3.13, no 3.14** | `d4forge` lo deja anotado en su `requirements.txt`: *«Python 3.13 (el 3.14 todavía no tiene wheel de onnxruntime ni de PySide6)»*. Comprobar antes de fijar la versión |
| **`mss`** | **Se queda, con tres cambios** | Es lo que usan `d4lf` y `d4forge`. Cambios: capturar **ROI de la ventana**, cachear el frame ~40 ms, desactivar `CAPTUREBLT`. Aviso: **no captura en pantalla completa exclusiva** (sale negro); hay que exigir ventana sin bordes **y detectarlo**, no fallar en silencio. Si algún día hiciera falta más, `dxcam` (Desktop Duplication API); `d4forge` declara los dos |
| **`tkinter`** | **Fuera** | Cero precedentes en el arte previo. Sin tabla decente, borroso en HiDPI. **`PySide6` (LGPL)** es el salto obvio y es lo que usa el proyecto de visión más medido del lote (`d4forge`). `CustomTkinter` es el parche barato si asusta el coste: arregla HiDPI y aspecto, no los widgets que faltan |
| **`winocr` (paquete)** | **Fuera** | 25 ★, sin push desde oct-2024, `asyncio.run()` por frame y serialización por reflexión. Son 15 líneas contra `winrt-windows-media-ocr` |
| **`Windows.Media.Ocr` (motor)** | **Defendible para la v1, y no apostar a una sola carta** | A favor: API pública documentada de Microsoft, sin binarios de procedencia dudosa, ~2 % de CPU, y **es-ES documentado como «excelente»** por Microsoft. En contra: es una API de 2015 y **la única comparativa publicada sobre texto de juego lo puntúa «precisión media», la más baja de las cinco**. Y la letra pequeña del «sin instalar»: necesita `Language.OCR~~~es-ES~0.0.1.0`, que se instala con `Add-WindowsCapability` **como administrador**. Comprobar `IsLanguageSupported('es-ES')` **al arrancar**, con el comando exacto en pantalla si falta, y verificar `RecognizerLanguage` **después** de crear el motor (pedir `es` puede resolver a `es-MX`) |
| **La alternativa real: `rapidocr-onnxruntime`** | **Es la que yo mediría primero** | `pip install`, sin binario de sistema, sin DLLs copiadas a mano, sin administrador, offline. Y el «no encontrado» sobre el español **se cierra**: **PP-OCRv5 tiene modelo latino que cubre español**, confirmado en la lista de modelos de RapidOCR. Es lo que usa `d4forge` para medir sus 30-90 ms por línea |
| **`RegisterHotKey`** | **Se queda. Es la mejor pieza del diseño** | Cero casos de baneo en cualquier juego, sin hook global, solo escucha lo registrado. `d4lf` usa `pynput`, que en Windows sí instala hook de bajo nivel. Estamos por encima del arte previo en higiene |
| **Ventana propia sin overlay** | **Se queda** | `d4lf`, `Diablo4Companion`, `d4-ocr` y `horadric-cube` dibujan overlay. Nosotros no. Nos deja más limpios que todo el arte previo sin perder nada: comparar dos objetos no exige estar encima del juego |
| **Perfiles JSON** | **Se queda, con un añadido** | Copiar de `d4-damage-calc` el estado en **hash de URL además del fichero**: convierte «pásame tu build» en pegar un enlace, y de paso resuelve el perfil «rival» sin OCR |
| **Empaquetado** | **Carpeta + instalador, no `--onefile`** | PyInstaller `--onefile` tiene falsos positivos de antivirus bien documentados; para un usuario no técnico, eso es «no funciona». Modo carpeta, o Nuitka |

### La pregunta de stack que nadie ha hecho

Antes de elegir GUI: **¿esto tiene que ser una aplicación de escritorio?**

La calculadora —la parte con valor real— es una página estática. `jlian/d4-damage-calc` es Vite +
TypeScript, sin backend, estado en hash de URL y `localStorage`, desplegada en GitHub Pages. Funciona
en el móvil mientras juegas en el PC, se comparte con un enlace, no se instala, no puede ser confundida
con nada por ningún antivirus ni por ninguna heurística de anticheat, y **no toca el juego ni de lejos**.

Lo único que exige escritorio es el OCR. Eso sugiere partir en dos y no al revés:
- **Una página** con la calculadora y los perfiles. Cero riesgo, cero instalación, empieza a ser útil
  el primer día.
- **Un puente local mínimo**, si y solo si el OCR demuestra funcionar en español: atajo → captura de
  región → OCR → JSON al portapapeles, que se pega en la página. Sin GUI propia, sin bucle, sin
  checklist. `horadric-cube` es exactamente esa forma (menos su servidor remoto), y es lo que hace
  que su superficie sea tan pequeña.

Si al final se quiere una sola ventana, PySide6. Pero la decisión de GUI es menos importante que la de
si hace falta ventana.

---

## Lo que no se sabe

Huecos declarados. Ninguno se ha rellenado con suposiciones.

1. **Cuánto acierta cualquier motor de OCR sobre tooltips de Diablo IV en español.** Es el riesgo
   número uno del proyecto y **no existe ni un dato publicado**. La búsqueda de código en GitHub sobre
   `winocr+diablo`, `Windows.Media.Ocr+diablo` y `OcrEngine+diablo+tooltip` da **cero resultados en las
   tres**. `d4lf` exige el juego **en inglés** y no explica por qué; la hipótesis más probable, según su
   refutación, es que la limitación esté en su OCR, no en el TTS — sin confirmar. `d4-item-tooltip-ocr`
   tuvo que **entrenar un modelo propio** para PaddleOCR sobre la tipografía de D4, y era en inglés.
   **Esto se mide en casa, con veinte capturas reales en español, antes de escribir nada más.** Si
   falla, el proyecto es la calculadora y punto.
2. **Cómo se porta el emparejamiento difuso con tildes y `ñ`.** Diablo4Companion desactiva el
   preprocesador de FuzzierSharp para zh y ru, **y no lo desactiva para esES**. Los preprocesadores por
   defecto de la familia FuzzyWuzzy normalizan a alfanumérico ASCII. Hay que comprobar qué hace
   `rapidfuzz` con `daño`/`dano` antes de fiarse.
3. **Si el tooltip semitransparente rompe el umbral fijo sobre el panel de equipo.** `horadricapp`
   (D2R) lo reporta como su peor caso: *«OCR might not work properly when the item overlay pops over
   dark textures (equipped inventory seems to be the worse)»*. Nuestro caso de uso **es exactamente
   ese panel**. d4forge tiene el problema resuelto porque su panel (el Occultist) es casi negro, brillo
   medio ~4; el nuestro no lo será.
4. **Si «Advanced Tooltip Information» cambia el layout en español.** `d4lf` lo exige y avisa de que
   sin él *«item parsing will be very inconsistent and you will receive no warning something is
   wrong»*. No he verificado qué añade ni cómo se ve en esES.
5. **Cuántas combinaciones de resolución × escala de fuente × HDR hay que soportar.** Diablo4Companion,
   el proyecto con más estrellas del ecosistema, mantiene **un preset por combinación**, descargable y
   actualizable desde la app. Ese es el coste permanente del OCR, y no sabemos el nuestro. La
   alternativa —localizar el tooltip por máscara HSV y contornos, como `d4-item-tooltip-ocr`, filtrando
   por área, proporción y anchura entre el 15 % y el 30 % de la pantalla— es independiente de la
   resolución, pero está sin validar en el D4 de 2026 (ese repo lleva parado desde julio de 2023).
6. **Si el catálogo `Affixes.esES.json` está al día del parche 3.1.3 / Season 14.** He verificado que
   tiene 891 entradas y que el repo tiene push del 28-ago-2026, **no que las 891 correspondan a la
   temporada viva**. Hay que cruzarlo contra pantalla antes de fiarse.
7. **Si las constantes de `d4-damage-calc` valen para el parche vivo.** Está declarado como **Season 13
   (Lord of Hatred)** y el `baseDamage` por tipo de arma sale de una hoja de cálculo de un creador. El
   parche del proyecto es 3.1.3 / Season 14. **Portar la estructura no es portar los números.**
8. **Qué fracción del tooltip llega por el pipe del TTS, y en qué idioma.** Sigue abierto y ahora
   importa doble: nadie ha demostrado que el TTS baste solo. Se resolvería en una tarde con
   `josdemmers/D4TTS` y un cliente en español — pero solo tiene sentido hacerlo si se reabre la
   decisión sobre la DLL, y no hay motivo para reabrirla.
9. **Si Diablo IV usa Warden y si tiene componente de kernel.** No hay documentación pública
   específica de D4; todo lo que circula es de WoW y D3, extrapolado. El mejor indicio disponible es
   estructural: **D4 corre en Linux con Proton en nivel gold**, lo que es incompatible con un
   anti-cheat con driver de kernel. Indicio, no prueba.
10. **Si Warden enumera procesos o lee títulos de ventana.** Las fuentes comunitarias se contradicen
    directamente, y es justo el dato que decidiría si el nombre de nuestro ejecutable importa.
11. **El esquema completo del filtro de botín.** `d4-filter-generator` documenta protobuf + base64 y
    **77 IDs de afijo verificados**, pero es un solo autor, 2 ★, y los rangos de habilidad solo están
    confirmados para Warlock. No hay especificación oficial.
12. **Cifras reales de uso de nada.** Solo hay estrellas de GitHub, que no son usuarios. Ningún
    proyecto de D4 publica tasa de acierto por afijo, corpus de prueba ni matriz de confusión.
13. **El riesgo de baneo, honestamente.** Cero declaraciones de Blizzard sobre captura u OCR, pedidas
    al menos cuatro veces en sus propios foros. Cero oleadas documentadas contra usuarios de las
    herramientas que **sí** cruzan las líneas. Cero casos sostenidos tras apelación. **Ausencia de
    evidencia, no evidencia de seguridad** — y el único caso que existe demuestra que la heurística
    barre por cosas que no tienen nada que ver contigo.

---

## Fuentes

**Repositorios verificados hoy vía `gh api` (estrellas, lenguaje, licencia, último push)**
- https://github.com/josdemmers/Diablo4Companion — 321 ★, C#, MIT, push 2026-08-28
- https://github.com/d4lfteam/d4lf — 206 ★, Python, MIT, push 2026-08-28
- https://github.com/mxtsdev/d4-item-tooltip-ocr — 40 ★, Python, MIT, push 2023-07-18
- https://github.com/jlian/d4-damage-calc — 4 ★, TypeScript, MIT, push 2026-06-02
- https://github.com/Upsilon72/d4-filter-generator — 2 ★, HTML, MIT, push 2026-05-11
- https://github.com/Goosterhof/horadric-cube — 0 ★, TypeScript (Tauri v2), **sin licencia**, push 2026-08-25
- https://github.com/ferpgshy/d4forge — 0 ★, Python, **GPL-3.0**, push 2026-08-12
- https://github.com/brianjleepub/diablo4_item_comparer — 0 ★, Python, **sin licencia**, push 2026-01-13
- https://github.com/reikla/d4dps — 0 ★, PowerShell, push 2026-05-08
- https://github.com/NineO1/Scara-B-4 — 0 ★, JavaScript, push 2026-01-19
- https://github.com/mivuorin/d4-ocr — 0 ★, C#, MIT, push 2024-02-08
- https://github.com/GitHub30/winocr — 25 ★, Python, MIT, push 2024-10-25

**Ficheros descargados y leídos**
- https://raw.githubusercontent.com/josdemmers/Diablo4Companion/master/D4Companion/Data/Affixes.esES.json (891 entradas, contadas)
- Listado completo de `D4Companion/Data`: `Affixes`, `Aspects`, `ItemTypes`, `ParagonBoards`, `ParagonGlyphs`, `Runes`, `Sigils`, `Uniques` × 14 idiomas, incluido **esES**
- https://raw.githubusercontent.com/josdemmers/Diablo4Companion/master/README.md
- https://raw.githubusercontent.com/d4lfteam/d4lf/main/README.md
- https://raw.githubusercontent.com/jlian/d4-damage-calc/master/README.md y `src/calc.ts`
- https://raw.githubusercontent.com/ferpgshy/d4forge/master/d4forge/vision/ocr.py, `vision/preprocess.py`, `automation/safety.py`, `requirements.txt`
- https://raw.githubusercontent.com/Goosterhof/horadric-cube/main/README.md
- https://raw.githubusercontent.com/Upsilon72/d4-filter-generator/main/README.md
- https://raw.githubusercontent.com/brianjleepub/diablo4_item_comparer/main/README.md

**Blizzard y foros (abiertos hoy)**
- https://www.blizzard.com/en-us/legal/fba4d00f-c7e4-4883-b8b9-1b4500a402ea/blizzard-end-user-license-agreement — §1.C, cláusula de *Data Mining* **completa**, con la coletilla de interfaces de terceros
- https://us.forums.blizzard.com/en/d4/t/blizzard-admits-ban-was-an-error-use-of-item-search-qol-screenshot-tool/115166
- https://us.forums.blizzard.com/en/d4/t/another-one-banned-for-alleged-use-of-malicious-3rd-party-software-today/114728 — **la clave: Chia + Easy Anti-Cheat en la misma oleada**
- https://us.forums.blizzard.com/en/d4/t/is-using-diablo4companion-safe-from-bans/165759 — sin blue post
- https://us.forums.blizzard.com/en/d4/t/i-made-an-ocr-equipment-filter-tool-is-it-legal/121740
- https://us.forums.blizzard.com/en/d4/t/a-notice-regarding-unauthorized-game-modifying-software-in-diablo-iv/102121

**Técnico**
- https://rapidai.github.io/RapidOCRDocs/main/model_list/ — PP-OCRv5 «latino mixto», cubre español
- https://learn.microsoft.com/en-us/uwp/api/windows.media.ocr.ocrengine — `Language.OCR~~~es-ES~0.0.1.0`
- https://dev.overwolf.com/ow-native/live-game-data-gep/supported-games/diablo-4/ — sin inventario ni afijos

**Heredado de los informes previos y sus refutaciones** (no reverificado aquí): el código de
`tts/saapi.cpp` e `install_dll.cmd` de d4lf, los drivers de `dkager/tolk`, el pipeline de
`ScreenProcessHandler.cs`/`OcrHandler.cs` de Diablo4Companion, el esquema `stats.ndjson` de
Exiled-Exchange-2, y la redirección 301 de `d4armory.io`.
