# Refutación adversarial: `crudo/arte-d4-datos.md`

**Fecha de la verificación:** 29 de agosto de 2026.
**Método:** `gh api` sobre los 18 repos citados (estrellas, lenguaje, push, archivado, fork), lectura del
código fuente real de `d4lf/tts/*` y de `dkager/tolk/src/*`, `curl -D` sobre d4armory.io, 6 búsquedas
web y 9 páginas abiertas.
**Veredicto:** **PARCIAL** — el núcleo está mejor verificado de lo habitual (las citas de código son
literales y los 18 repos existen con metadatos exactos), pero hay **un error técnico de mecanismo**,
**una inflación de autoridad de fuente** y **un titular que la propia evidencia del documento
contradice**.

---

## Resumen: qué aguanta y qué no

| | Nº de afirmaciones | |
|---|---|---|
| Confirmadas literalmente (código, citas, metadatos) | 22 | ✅ |
| Errores sustantivos | 3 | ❌ |
| Imprecisiones que hay que corregir | 6 | ⚠️ |
| Afirmaciones que además he **reforzado** con evidencia nueva | 3 | ➕ |

---

## ❌ ERROR 1 (el grave) — "SAAPI … **la misma que usan JAWS y NVDA**" es falso

El documento afirma: *"Es la interfaz System Access API (SAAPI) vía Tolk, la misma que usan JAWS y NVDA."*

**Refutado por el código fuente de Tolk.** Tolk no tiene *una* interfaz: tiene **un driver distinto por
lector de pantalla**. Listado real de `github.com/dkager/tolk/contents/src`:

```
ScreenReaderDriverJAWS.cpp    ScreenReaderDriverNVDA.cpp    ScreenReaderDriverSA.cpp
ScreenReaderDriverSAPI.cpp    ScreenReaderDriverSNova.cpp   ScreenReaderDriverWE.cpp
ScreenReaderDriverZT.cpp
```

Y cada uno carga cosas distintas:

| Driver | Mecanismo real (leído en el `.cpp`) |
|---|---|
| **SA** (System Access) | `LoadLibrary(L"SAAPI64.dll")` → `GetProcAddress(..., "SA_SayW")` |
| **NVDA** | `LoadLibrary(L"nvdaControllerClient64.dll")` → `nvdaController_speakText` |
| **JAWS** | Objeto **COM**, `controller->SayString(bstr, flush, &result)` — ni siquiera es una DLL cargada por nombre |

**SAAPI es la API de un único producto: System Access, de Serotek.** No es un estándar de
accesibilidad ni la vía de JAWS ni la de NVDA.

**Por qué importa para el encargo, no es un detalle de erudito:**

1. La vía no es "la interfaz estándar de accesibilidad de Windows". Es **suplantar a un lector de
   pantalla comercial concreto y minoritario**. Eso empeora el argumento de legitimidad que el
   documento construye en §2 ("ruta de accesibilidad oficial"): la ruta es oficial, pero el rol que
   usurpas es el de un proveedor específico.
2. Consecuencia práctica no mencionada: si el jugador **usa de verdad** System Access, instalar
   nuestra DLL le rompe su lector. Con JAWS o NVDA no pasaría — porque no pasan por ahí.
3. El artículo de Blizzard que el documento cita **dice JAWS y NVDA y no dice SAAPI ni Tolk**. He
   comprobado el texto: *"Diablo IV contains a built-in screen reader and supports JAWS, NVDA, and
   other third-party screen reading software."* La cadena SAAPI/Tolk sale del README de d4lf, no de
   Blizzard. El documento fusiona dos fuentes en una frase y produce una afirmación que ninguna de
   las dos sostiene.

**Corrección:** *"Es la interfaz System Access API (SAAPI), una de las siete que envuelve Tolk — la de
System Access, no la de JAWS (COM) ni la de NVDA (`nvdaControllerClient64.dll`)."*

---

## ❌ ERROR 2 — "Foro oficial de Blizzard" cuando quien habla es un usuario cualquiera

El documento presenta la prueba de la fila (a) como *"Foro oficial de Blizzard: 'Characters are not
stored locally no' · 'Even your settings are stored on bnet'"*, y le pone **Confianza: Alta**.

Las dos citas **existen literalmente**. Pero son de:

- `Sonez-1486` — usuario corriente.
- `CommandoCat-1409` — usuario corriente.

**No hay post azul en ese hilo.** "Foro oficial de Blizzard" hace pasar el sitio donde se publicó por
la autoridad de quien publicó.

Lo que lo convierte en error y no en descuido: **el propio documento aplica el criterio correcto 40
líneas más abajo**, cuando marca la cita de la EULA como *"(foro de Blizzard, usuario veterano — **no
hay post azul**)"*. Usa dos varas de medir para dos citas del mismo foro, y la vara laxa cae
justamente sobre la afirmación que sostiene toda la conclusión (a).

**Nota justa:** la conclusión (que no hay datos del personaje en local) **la doy por buena** — la he
reforzado por otra vía (ver ➕1). Lo que se cae es el "Alta" apoyado en dos posts anónimos.

---

## ❌ ERROR 3 — El titular "VÍA **SIN OCR** CONFIRMADA Y VIVA" lo desmiente la propia herramienta citada

El README de d4lf, textualmente:

> *"D4LF gets item information by **reading the screen and** using TTS information sent for accessibility."*

Es decir: **d4lf no es una vía sin OCR. Es OCR + TTS.** Por eso sigue exigiendo, en la misma página,
HDR desactivado, escala de fuente pequeña o media, y "Advanced Tooltip Information" activado — todo
eso son requisitos *de lectura de pantalla*, no de TTS.

El documento **sabe esto** (su tabla §3 dice "TTS … + lectura de pantalla", y §4 remata "d4lf, que ya
usa TTS, aun así exige…"), pero el veredicto de la primera línea y la tabla comparativa de §2
("Fidelidad: cadena exacta" · "Sensible a resolución: No" · "Coste en CPU: casi nulo") describen un
sistema **solo-TTS que ningún proyecto verificado ha demostrado**.

**Estado real de la afirmación:** la vía SAAPI está confirmada y viva **como complemento**. Que baste
por sí sola para cubrir 10 huecos de equipo y 6 habilidades **no lo demuestra ninguna herramienta
existente**. Debería estar en "No encontrado", no en el veredicto.

---

## ⚠️ Imprecisiones a corregir

**⚠️1 — `LocalPrefs.txt` no son "ajustes gráficos".** Está en
`%userprofile%\Documents\Diablo IV\LocalPrefs.txt` y contiene **todos** los ajustes: gráficos, audio,
controles y jugabilidad. Efecto colateral: la cita que el documento usa como prueba ("Even your
settings are stored on bnet") **es falsa tal cual**, y el propio documento la contradice dos columnas
después al reconocer que `LocalPrefs.txt` existe en local.

**⚠️2 — Contradicción interna sobre el portal de desarrolladores.** La fila (c) afirma *"No hay D4 en
el portal de desarrolladores de Battle.net (solo D3, WoW, SC2, Hearthstone)"* con **Confianza: Alta**,
mientras que "No encontrado #4" confiesa que **nunca llegó a leer el portal** (SPA con
`<app-root></app-root>`). No se puede puntuar Alta una afirmación cuya fuente se declara ilegible en
la misma página. *(La conclusión, sin embargo, la he corroborado por fuera — ver ➕2.)*

**⚠️3 — El paso 6 del instalador es un `fallback`, no un paso fijo.** La descarga de
`Microsoft.Windows.SDK.BuildTools` desde NuGet solo ocurre si `Resolve-SignTool` **no encuentra**
`signtool.exe` en `.tools`, en `C:\Program Files (x86)\Windows Kits\10\bin\` ni en el PATH. Igual el
paso 2: `Stop-D4ProcessIfRunning` solo se invoca cuando la DLL de origen y la de destino son
distintas, es decir, cuando hay que copiar de verdad. Enumerarlos como seis pasos incondicionales
exagera un poco el coste — que ya es alto de por sí sin exagerarlo.

**⚠️4 — Precisión que el documento acierta y conviene no perder al reescribir:** el certificado se
instala en `Cert:\CurrentUser\Root` (**Trusted Root del usuario**, vía `X509Store` con
`StoreLocation::CurrentUser`), no en el de la máquina. El documento lo dice bien; que no se degrade a
"Trusted Root" a secas, porque el matiz cambia el alcance del riesgo.

**⚠️5 — Inventario de `Diablo4DpsMeter` incompleto.** El documento dice *"solo README, LICENSE y
.gitignore"*. El listado real es `.gitattributes`, `.github/`, `.gitignore`, `LICENSE`, `README.md`
(39 bytes), con **dos commits**: "Initial commit" y "Create FUNDING.yml". La conclusión —**no hay
código**— es correcta; la enumeración no.

**⚠️6 — Dos etiquetas de la tabla §3.** `wenqu/diablo4trading-ocr` figura como "JS": la API de GitHub
devuelve `language: null`. Y `DiabloTools/d4data` es literalmente un **fork** (`fork: true`) de
`blizzhackers/d4data`, dato que refuerza el "sucesor" pero que no aparece.

---

## ✅ Confirmado literalmente (lo que NO hay que tocar)

**Código, verificado byte a byte:**

- `tts/saapi.cpp` — la cita del documento es **exacta**. `InitPipe()` hace `CreateFile` sobre
  `\\.\pipe\d4lf`; `SA_SayW` convierte con `WideCharToMultiByte(CP_UTF8, …)` y hace `WriteFile`,
  reintentando `InitPipe()` si falla. Los otros tres exports (`SA_BrlShowTextW`, `SA_IsRunning`,
  `SA_StopAudio`) son stubs que devuelven `true`. **No sintetiza voz: correcto.** Y son ~50 líneas:
  correcto.
- `tts/install_dll.cmd` — los seis pasos existen: elevación (`net session` + `Start-Process -Verb
  RunAs`), `Stop-Process -Force` sobre "Diablo IV", copia de `saapi64.dll` al directorio del juego,
  `New-SelfSignedCertificate -Type CodeSigningCert -Subject "CN=Cert for D4LF" -NotAfter
  (Get-Date).AddYears(10)`, alta en el almacén Root de CurrentUser, y `signtool sign /fd SHA256 /n
  "Cert for D4LF"`. **La parte incómoda del documento es real y está bien leída.**
- Los cuatro símbolos que exporta la DLL de d4lf son exactamente los cuatro que
  `ScreenReaderDriverSA.cpp` de Tolk busca con `GetProcAddress`. El encaje es perfecto: es una
  suplantación deliberada y correcta de System Access.

**Metadatos de los 18 repos: coinciden los 18** (estrellas, lenguaje, push, archivado). Muestra:
d4lf 206★ Python push 2026-08-28 · Diablo4Companion 321★ C# push 2026-08-28 · diablo4-build-calc 221★ ·
blizzhackers/d4data 101★ **archivado** · diablo_4_armory_fetcher 17★ **archivado** ·
diablo4-data-harvest 39★ **archivado**. **Ningún repo inventado.**

**Citas verbatim confirmadas:**

- d4lf release **v9.3.6 (2026-07-06)**: *"Items in the armory, especially seals, should now be
  properly parsed"* — julio de 2026, correcto.
- bytemind/d4-tools: *"Read the data from your actual account via some Blizzard API (d4armory seems
  to be able to do it, but how???)"* — literal, y su README confirma los *buckets* aditivo/
  multiplicativo y el `localStorage` + export JSON.
- Blizzard sobre TurboHUD4: *"TurboHUD4, like any game-modifying software, is prohibited…"* — literal.
- Noticia de accesibilidad: *"grasp an understanding of the gear they are using"* — el sentido que le
  da el documento es correcto.
- Hilo de rotura: **11 de marzo de 2026**, autor `cjshrader-1577`, **sin respuesta azul**, sin
  resolver. Correcto.
- Hilo de CTRL+C: **7 de noviembre de 2023**, sin respuesta azul. Correcto.

**Comprobaciones de red y de producto:**

- `curl -D` sobre `https://d4armory.io/` → **`HTTP/2 301` · `location: https://diablo4.com/`**. Exacto.
- Armory interno: **5 loadouts**, guarda equipo, tablero de Paragón + glifos, habilidades y mecánica
  de clase; sin exportación al exterior. Correcto.
- **Lord of Hatred: 28 de abril de 2026**, actualización universal y gratuita con filtro de botín.
  Correcto.
- Exportación del filtro: **botón de tres puntos** junto al nombre del filtro → Rename / Duplicate /
  **Export** / Delete → **copia la cadena al portapapeles**; Maxroll publica los códigos en base64.
  Correcto. *(Dato nuevo que el documento no tiene: **import/export solo está en PC**, no en consola.)*
- D4Companion: `OcrHandler.cs`, `ScreenCaptureHandler.cs`, `ScreenProcessHandler.cs`,
  `SystemPresetManager.cs` en el repo; README confirma **TesseractOCR + Emgu CV**, overlay, presets por
  resolución/fuente/HDR y **README.esES.md** propio. Atribución correcta.
- `awesome-d4`: en `readme.md` (minúsculas) aparece *"[D4 Armory](https://d4armory.io/) - Unofficial
  leaderboard and character profile lookup tool"* **sin marca de muerto**. Correcto — y de paso
  confirma que d4armory **sí servía perfiles de personaje**.
- Importación desde planificadores: d4lf (README: maxroll/d4builds/mobalytics/infinitybuilds) y
  D4Companion (`BuildsManagerMaxroll.cs`, `…D4Builds`, `…Mobalytics`, `…InfinityBuilds`,
  `…D2Core`). Correcto.

---

## ➕ Evidencia nueva que refuerza el documento

**➕1 — El "No encontrado #6" (log de combate) se puede cerrar.** El documento se reserva el juicio
porque `Diablo4DpsMeter` está vacío. Hay evidencia positiva independiente: Diablo IV **no tiene log de
combate**, y es una petición recurrente y sin atender en los foros oficiales (US y EU, varios hilos).
Lo único que existe son las "Combat Text Options" — números flotantes en pantalla, no un fichero.
**Puede pasar de "reserva" a NO firme.**

**➕2 — El "No encontrado #4" (portal de desarrolladores) también.** Sin depender de la SPA: fuentes
independientes describen el ecosistema del portal como WoW, **Diablo III**, StarCraft II y Hearthstone.
No hay API pública de Diablo IV a agosto de 2026. La conclusión (c) se sostiene por otra vía.

**➕3 — El "No encontrado #2" (¿sigue viva la ruta SAAPI?) está medio resuelto en el README que el
documento ya citó.** El apartado de instalación de d4lf se titula *"New instructions for **season 12**
that must be followed!"*: **el procedimiento de firma Authenticode ES la respuesta a la rotura de la
temporada 12**. Lo que Blizzard cambió en marzo de 2026 fue **exigir que la DLL estuviera firmada** —
por eso el instalador monta el certificado y el `signtool`. Dos lecturas, ambas útiles:

- **A favor:** la vía no quedó rota; se adaptó, y sigue funcionando con la carga de instalación actual.
- **En contra (y es lo que pesa):** **Blizzard ya apretó esa tuerca una vez**, y el precio de seguir
  dentro fue pasar de "copiar una DLL" a "meter un certificado autofirmado en el Trusted Root del
  usuario". El siguiente apretón puede costar más. La fragilidad que el documento intuye es real, pero
  el mecanismo es otro: no es que se rompa sola, es que **Blizzard endurece los requisitos y cada
  vuelta de tuerca sube el coste de instalación**.

---

## Efecto sobre las recomendaciones del §8

| # | Recomendación | Estado tras verificar |
|---|---|---|
| 1 | `.stl` como origen del vocabulario | **Intacta.** Es la mejor idea del documento y no cruza ninguna línea |
| 2 | Contrato imagen → JSON de d4-item-tooltip-ocr | **Intacta** |
| 3 | *Buckets* de daño de bytemind | **Intacta**, cita verificada |
| 4 | "Vision Mode Only" como principio | **Intacta** |
| 5 | Presets de D4Companion como presupuesto | **Intacta** |
| 6 | Importar el rival desde planificadores | **Intacta** |
| 7 | D4TTS como prueba de concepto de una tarde | **Reforzada, y ahora es obligatoria antes de decidir** — porque el ERROR 3 significa que nadie ha demostrado que el TTS baste solo. La prueba de concepto no es "confirmar el español": es **medir qué fracción del tooltip llega por el pipe sin mirar la pantalla** |
| 8 | Leer el código del filtro de botín del portapapeles | **Intacta**, con el matiz nuevo de que es solo-PC |

---

## Fuentes de esta verificación

**Código leído directamente (`gh api …/contents/…`)**
- https://github.com/d4lfteam/d4lf/blob/main/tts/saapi.cpp
- https://github.com/d4lfteam/d4lf/blob/main/tts/install_dll.cmd
- https://github.com/d4lfteam/d4lf/blob/main/README.md
- https://github.com/dkager/tolk/tree/master/src (`ScreenReaderDriverSA.cpp`, `…JAWS.cpp`, `…NVDA.cpp`)
- https://github.com/josdemmers/Diablo4Companion (árbol de `D4Companion.Services`, `csproj`)
- https://github.com/bytemind-de/d4-tools/blob/main/README.md
- https://github.com/cagartner/awesome-d4/blob/main/readme.md
- https://github.com/shalzuth/Diablo4DpsMeter (contenidos y commits)
- `gh api repos/<owner>/<repo>` sobre los 18 repos del documento

**Web**
- https://news.blizzard.com/en-us/article/23954932/combatting-demons-with-accessibility-in-diablo-iv
- https://us.forums.blizzard.com/en/d4/t/3rd-party-screen-readers-no-longer-function-in-season-12/242596
- https://us.forums.blizzard.com/en/d4/t/where-are-saved-game-files-located/46682
- https://us.forums.blizzard.com/en/d4/t/copy-paste-item-information-feature-proposal/137085
- https://us.forums.blizzard.com/en/blizzard/t/diablo-4-api-d4armory/45191
- https://www.icy-veins.com/d4/news/blizzards-stance-on-unauthorized-game-modifying-software-in-diablo-iv/
- https://maxroll.gg/d4/resources/loot-filter
- https://maxroll.gg/d4/resources/armory
- https://en.wikipedia.org/wiki/Diablo_IV:_Lord_of_Hatred
- https://community.developer.battle.net/documentation/guides/game-data-apis
- `curl -sS -D - https://d4armory.io/` → 301 → https://diablo4.com/

---

## No verificable desde aquí

1. **Si el pipe TTS emite en español.** Sigue abierto, igual que en el original. Y ahora importa más,
   porque el ERROR 3 añade una segunda incógnita al mismo experimento: **cuánto** del tooltip llega
   por TTS, no solo en qué idioma.
2. **Por qué d4lf exige inglés.** El README lo impone sin explicarlo. Con el ERROR 3 en la mano, la
   hipótesis más probable ya no es "el TTS solo habla inglés" sino **"su OCR solo lee inglés"** — lo
   cual sería una buena noticia para nosotros. No lo he podido confirmar.
3. **Contenido completo de `Documents/Diablo IV/`.** Sigue sin enumerar. 30 segundos en la máquina del
   jugador.
4. **Esquema del código base64 del filtro de botín.** Sin especificación pública. Confirmado que los
   decodificadores son servicios web cerrados.
