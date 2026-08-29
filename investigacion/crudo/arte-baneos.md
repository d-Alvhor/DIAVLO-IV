# El arte de no ser baneado — dónde está la línea en la práctica

> Investigación de campo, 29 de agosto de 2026. Dominio: riesgo real con casos documentados.
> Regla de esta nota: **un caso documentado vale más que una opinión de foro**, y una opinión de
> foro con nombre y fecha vale más que un "todo el mundo sabe". Cuando no hay caso, lo digo.

## 0. Conclusión primero

La línea real **no está donde la comunidad cree**. La comunidad repite "si no lees memoria estás
bien". Eso es aproximadamente cierto para la **detección** y aproximadamente falso para el
**permiso**. Son dos ejes distintos y conviene no confundirlos nunca:

| Eje | Pregunta | Quién decide |
|---|---|---|
| **Detectabilidad** | ¿Pueden verme? | Warden / telemetría / detección servidor |
| **Permisibilidad** | ¿Me está permitido? | EULA + criterio discrecional de Blizzard |

Nuestro diseño (captura + OCR, sin memoria, sin inyección, sin overlay, sin automatizar entradas)
sale **muy bien en detectabilidad** y **en gris en permisibilidad**. El riesgo residual no es que
nos pillen: es un **falso positivo** en una oleada de baneos, exactamente lo que le pasó a
`diablo_qol` en agosto de 2023.

Y hay una cláusula de la EULA que la comunidad casi nunca cita y que nos toca más de cerca que la
famosa de los bots. Está en la sección 4.

---

## 1. Casos documentados, ordenados por lo que nos importan

| Caso | Juego | Qué hacía la herramienta | Resultado | ¿Reversado? |
|---|---|---|---|---|
| **`diablo_qol`** (ago 2023) | D4 | Captura de pantalla de tooltips + OCR para buscar/filtrar alijo e inventario. **No lee memoria** | Baneo **Error 52**, "malicious 3rd party software" | **Sí, en ~24 h**, admitido como error |
| **Filtro OCR + AutoHotkey** (ago 2023) | D4 | OCR con Tesseract 5.0 + Python, y **AHK enviaba espacio** para marcar basura | Sin baneo reportado; consenso: prohibido | N/A — nadie de Blizzard respondió |
| **Macro AHK de clic derecho** (jun 2023) | D4 | "Mientras mantienes clic derecho, spamea clic derecho" (bucle) | **Baneo permanente** | No |
| **TurboHUD4** (jul 2023) | D4 | Overlay que lee estado del juego; maphack | Señalado **por su nombre** por Blizzard; riesgo de suspensión permanente | N/A |
| **Oleadas D3** (2015-2016) | D3 | Mezcla: bots (RoS-Bot, DemonBuddy), TurboHUD, D3Helper **y macros de AutoHotkey** | Baneos masivos; muchos en leaderboards | No |
| **POE Overlay** (2020) | PoE | Overlay que interactuaba con el cliente | Oleada de baneos | No |
| **Awakened PoE Trade** (vivo) | PoE | **Portapapeles**, nada más | Sin baneos; tolerado de facto | N/A |
| **Glider / MDY** (2008-2011) | WoW | Bot que leía memoria; evadía Warden | Demanda; Blizzard gana en el 9.º Circuito | N/A |

### Los dos casos que definen la línea

**A favor nuestro — `diablo_qol`.** Un jugador usó una herramienta que hace *exactamente* lo que
haremos: capturar el tooltip, pasarlo por OCR, indexar. Lo banearon el 11 de agosto de 2023 con
Error 52. Apeló. Blizzard le devolvió la cuenta con este texto:

> "After an additional review of the evidence, we determined this closure was an error. We're
> reopening this account for play, and hope you will accept our sincere apologies for the mistake."

El autor del hilo concluyó que esto "suena indirectamente a que Blizzard está OK con este tipo de
herramientas de captura que no leen memoria". **Eso es una inferencia suya, no una declaración de
Blizzard.** Otros usuarios del hilo pidieron aclaración oficial y no la hubo. Es el dato más
favorable que existe y aun así es un dato negativo disfrazado: **el baneo llegó a producirse.**

**En contra — el filtro OCR con AutoHotkey.** Mismo mes, mismo foro. Un desarrollador contó que su
herramienta hacía OCR con Tesseract y luego **AHK pulsaba la barra espaciadora** para marcar el
objeto como basura. La comunidad lo enterró. TheTias-1192 (28 ago 2023) citó la EULA contra
"any code and/or software...that changes and/or facilitates" el juego y remató:

> "avoid a ban by not using your OCR software"

La diferencia entre los dos casos **no es el OCR**. Es que el segundo **enviaba pulsaciones al
juego**. Esa es la línea.

---

## 2. Taxonomía de riesgo por técnica

| Técnica | ¿Casos de baneo? | Riesgo | Nota |
|---|---|---|---|
| Lectura de memoria del proceso | Sí, masivos | **Letal** | Núcleo de Glider, TurboHUD, bots. Detectable por Warden |
| Inyección de DLL | Sí, masivos | **Letal** | Firma detectable dentro del proceso |
| Automatización de entradas (bucles, multi-acción) | **Sí — AHK, permanente** | **Muy alto** | El macro de clic derecho en bucle acabó en baneo permanente |
| Overlay dibujado que lee estado del juego | Sí (TurboHUD, POE Overlay) | **Alto** | Blizzard señaló TurboHUD4 por su nombre |
| Bots de píxeles (leen pantalla + envían input) | Sí, por detección **servidor** | **Alto** | Warden no los ve; el análisis de comportamiento sí |
| **Captura de pantalla + OCR, solo lectura** | **Uno — y reversado** | **Bajo-medio** | `diablo_qol`. Zona gris real |
| Hook de teclado de bajo nivel | Detectado por otros anti-cheat (XIGNCode con AHK) | **Medio** | Se comporta como keylogger: ve todas las teclas |
| **`RegisterHotKey`** | **Ninguno encontrado** | **Bajo** | API oficial, sin hook global, solo escucha lo registrado |

Sobre `RegisterHotKey` frente al hook: la distinción está documentada técnicamente —
`RegisterHotKey` usa la Win32 API directamente, **sin hooks globales**, y solo escucha las teclas
que le registras; un hook global escucha *todas*, "igual que un keylogger". No he encontrado **ni
un solo caso** de baneo atribuido a `RegisterHotKey` en ningún juego. Nuestra elección de diseño
aquí es correcta y es la más defendible de todo el proyecto.

---

## 3. El mejor criterio que existe: el test del segundo ordenador

Viene de Path of Exile, no de Blizzard, pero es la formulación más limpia que he encontrado en toda
la investigación. Chris Wilson (GGG), sobre una política que llevaba ocho años sin cambiar:

> "You may not run programs that interact with the Path of Exile game client."

Con una excepción explícita: leer datos del portapapeles está permitido, y el criterio operativo es
este — **si te llevas esos datos a un segundo ordenador y el programa sigue funcionando, está
bien.**

Nuestro parser de tooltips **pasa ese test**: dale un PNG de un tooltip y funciona en una máquina
sin Diablo IV instalado. Eso no es una autorización de Blizzard (Blizzard no ha adoptado este
criterio), pero es la mejor vara de medir disponible y conviene adoptarla como invariante de diseño.

El FAQ de Awakened PoE Trade, la herramienta de terceros más usada de PoE, lo dice así:

> "There are no approved apps created by community. If app complies with the [game ToS], does one
> server action per button press and doesn't interact with the game client itself (injecting into
> the process, changing the process memory aka cheats) it can be considered safe."

Nota importante: **"una acción por pulsación"** es política razonablemente asentada en GGG. En
Blizzard **no la he podido verificar como declaración oficial**. Aparece repetida en los foros de
D2R como "la política de siempre", pero en el hilo que la contiene está etiquetada explícitamente
como *especulación*, no como blue post. No la citemos como si fuera de Blizzard.

---

## 4. Lo que dice literalmente la EULA (y la cláusula que nadie cita)

La cláusula famosa, **§1.C.ii**, prohíbe:

> "bots; i.e. any code and/or software, not expressly authorized by Blizzard, that allows the
> automated control of a Game"

y

> "any code and/or software, not expressly authorized by Blizzard, that can be used in connection
> with the Platform and/or any component or feature thereof which changes and/or facilitates the
> gameplay or other functionality"

Ese "**facilitates**" es deliberadamente enorme. Cualquier herramienta de ayuda "facilita" algo.

Pero la que de verdad nos apunta es **§1.C.vi**:

> "Use any unauthorized process or software that intercepts, collects, reads, or 'mines'
> information generated or stored by the Platform"

Una captura de pantalla del cliente **lee información generada por la Platform**, literalmente.
Esta es la cláusula bajo la que un revisor hostil encuadraría nuestra herramienta, y es más
específica y más difícil de esquivar que la de los bots. No la vi citada en ninguno de los hilos
donde la comunidad discutía OCR.

Dato relevante: la EULA **no menciona en ningún punto** captura de pantalla, overlays ni streaming.
No hay ni permiso ni prohibición explícita. El silencio es el problema.

Y la declaración oficial de Blizzard sobre D4 (PezRadar, 26 de julio de 2023) es igual de amplia:

> "The Blizzard EULA explicitly prohibits cheating, bots, hacks, and any other unauthorized
> software which automates, modifies, or otherwise interferes with the game."

Nombra a **TurboHUD4** y a nadie más. No define categorías técnicas. La discrecionalidad es total.

---

## 5. Blizzard nunca ha dicho que sí. Ni una vez.

Esto merece su propia sección porque es el hallazgo más incómodo.

- Hilo "**Third Party App: Diablo IV overlay is permitted? #ModCheck**" — seis páginas preguntando
  si un overlay está permitido. **Ningún empleado de Blizzard respondió jamás.**
- Hilo "**I made an OCR Equipment Filter tool, is it legal?**" — **ninguna respuesta oficial.**
- Hilo del baneo de `diablo_qol` — se pidió aclaración explícita. **No la hubo.**
- Hilo "**Got banned for autohotkey?**", más de 30 páginas — **ningún blue post.**

**Aviso de atribución:** MissCheetah-1661, citada por medio internet como si fuera autoridad de
Blizzard ("Blizzard does not allow any third party software use that touches their games, in any
way"), es **una jugadora del foro, no personal de Blizzard**. En el hilo del overlay se la
identifica explícitamente como jugadora, no moderadora. Es la frase más repetida de todo este
asunto y **no tiene rango oficial**. No la usemos como fuente de política.

Consecuencia práctica: **no existe lista blanca, no existe proceso de aprobación, y no existe
ningún caso de Blizzard bendiciendo una herramienta.** El único gesto favorable documentado es
revertir un baneo y llamarlo error.

---

## 6. Cómo detecta Blizzard (y por qué la detección no nos salva)

Warden, según documentación comunitaria consolidada:

- Corre **en modo usuario, dentro del proceso del juego**. No instala driver de kernel.
- Escanea la memoria del proceso buscando firmas de cheats conocidos.
- Verifica hashes de módulos y DLLs.
- Descarga módulos de escaneo nuevos desde los servidores: **lo que comprueba hoy no es lo que
  comprobaba el mes pasado.**
- Hay contradicción entre fuentes sobre si lee títulos de ventana o enumera procesos. Unas dicen
  que sí, otras que "nunca sale del espacio del proceso de WoW". **No resuelto.**

Los bots de píxeles ilustran el punto: no tocan memoria, "leen la pantalla igual que tus ojos y
simulan clics igual que tu mano", y **Warden no los ve** — pero sus usuarios sí acaban baneados,
por análisis de comportamiento del lado servidor. Traducción para nosotros: **ser indetectable en
cliente no es una defensa.** Lo que nos protege de verdad es no generar el patrón de comportamiento
que dispara la revisión, y eso lo conseguimos no automatizando nada.

---

## 7. Herramientas reales, con su fuente de datos

| Nombre | Repo | Lenguaje | **Fuente de datos** | Nota |
|---|---|---|---|---|
| **D4LF (Diablo 4 Loot Filter)** | `github.com/d4lfteam/d4lf` (antes `aeon0/d4lf`) | Python, 206 ★ | **TTS de accesibilidad** vía Tolk + DLL `saapi64.dll` que intercepta la salida, más OCR y capturas | **Automatiza ratón y teclado** (mueve objetos, marca favoritos/basura) y **dibuja overlay**. Sin disclaimer de EULA. Cruza dos líneas rojas nuestras |
| **Diablo4Companion (D4Companion)** | `github.com/josdemmers/Diablo4Companion` | C#/.NET, 321 ★ | **Captura de pantalla + Tesseract OCR**, umbral de coincidencia 80 % | **Dibuja overlay** sobre el juego. Sin disclaimer de EULA. Lleva años vivo sin oleada de baneos conocida |
| **d4-item-tooltip-ocr** | `github.com/mxtsdev/d4-item-tooltip-ocr` | Python, 40 ★ | **PaddleOCR con modelo entrenado a medida para D4**; acepta capturas o imágenes sueltas | **No automatiza input, no dibuja overlay.** El más cercano a nuestro diseño. Pasa el test del segundo ordenador |
| **Diablo-4-XP-and-gold-per-hour** | `github.com/akjroller/Diablo-4-XP-and-gold-per-hour` | Python, 18 ★ | **`mss` + Tesseract OCR** — nuestra pila exacta | Único repo que se autodenuncia: *"Warning! Running this could Violate Section 1.C.iii or Section 1.C.iv of Blizzard End User License Agreement Use at your OWN RISK"*. Sin mantenimiento |
| **d4-ocr** | `github.com/mivuorin/d4-ocr` | No verificado | OCR para gestión de inventario | Encontrado en búsqueda; **no abrí el repo**, no confirmo detalles |
| **Awakened PoE Trade** | `snosme.github.io/awakened-poe-trade` | TypeScript/Electron | **Portapapeles**, exclusivamente | El modelo a imitar. Tolerado de facto en PoE durante años |
| **PoETiS** | `github.com/Essyer/PoETiS` | Python (PyQt5), 21 ★ | **API oficial de GGG** con session ID | Irrelevante para D4: **Blizzard no expone API equivalente** |
| **TurboHUD4** | Sin repo público verificado | — | **Lectura de memoria del proceso** | Señalado por su nombre por Blizzard. Lo que **no** hay que hacer |

Observación estratégica: `D4Companion` (321 ★) lleva años haciendo OCR **con overlay dibujado** y no
hay constancia de una oleada de baneos contra sus usuarios. Es tranquilizador en cuanto a
detección. No es un permiso.

---

## 8. Riesgo residual de nuestro diseño, punto por punto

| Decisión nuestra | Veredicto | Fundamento |
|---|---|---|
| `mss`, captura cada 0,7 s | **Zona gris tolerada** | `diablo_qol` fue baneado y reversado. `akjroller` usa `mss` y avisa de §1.C |
| `winocr` (Windows.Media.Ocr) | **Mejor que Tesseract** | Componente del SO, no binario de terceros descargado. Menos superficie de "software no autorizado" |
| Ventana propia, **sin overlay** | **Nuestra mejor decisión** | Todos los baneos por overlay (TurboHUD, POE Overlay) implicaban overlay + lectura de estado |
| Sin lectura de memoria | **Correcto e imprescindible** | Es la única línea con casos masivos y con precedente judicial |
| `RegisterHotKey`, sin hook | **Correcto** | Cero casos documentados. El hook sí tiene detecciones en otros anti-cheat |
| **Sin enviar entradas al juego** | **Crítico — no negociar** | Es lo que separa `diablo_qol` (reversado) del filtro OCR+AHK (condenado) y del macro AHK (baneo permanente) |
| Checklist "no termina hasta verlo todo" | **Revisar** | Si empuja al usuario a barridos sistemáticos y repetitivos, genera patrón de comportamiento. El riesgo servidor es conductual |
| Perfiles JSON locales | **Sin riesgo** | No toca el juego |

**El escenario que debe preocuparnos** no es "nos detectan y nos banean por diseño". Es: oleada de
baneos automatizada, heurística amplia, falso positivo, cuenta cerrada, y varios días de apelación
con un resultado que depende de que un humano en Blizzard revise bien. Le pasó a `diablo_qol` en
2023 y la reversión tardó 24 horas; hay otro caso de Error 52 del 28 de diciembre de 2025 revertido
el 2 de enero de 2026 — **seis días**. Eso es el coste realista del peor caso.

---

## Fuentes

Páginas abiertas y leídas de verdad para esta nota:

1. https://us.forums.blizzard.com/en/d4/t/blizzard-admits-ban-was-an-error-use-of-item-search-qol-screenshot-tool/115166
2. https://us.forums.blizzard.com/en/d4/t/i-made-an-ocr-equipment-filter-tool-is-it-legal/121740
3. https://us.forums.blizzard.com/en/d4/t/a-notice-regarding-unauthorized-game-modifying-software-in-diablo-iv/102121
4. https://us.forums.blizzard.com/en/d4/t/overwolf-overlay-for-diablo-4-ban/133128/28
5. https://us.forums.blizzard.com/en/d4/t/third-party-app-diablo-iv-overlay-is-permitted-modcheck/41715
6. https://us.forums.blizzard.com/en/d4/t/got-banned-for-autohotkey/52417
7. https://us.forums.blizzard.com/en/d2r/t/no-more-mouse-clicks-autohotkey-and-diablo-2-bannable/5517
8. https://us.forums.blizzard.com/en/d3/t/turbohud-bannable-or-not/8943
9. https://www.blizzard.com/en-us/legal/fba4d00f-c7e4-4883-b8b9-1b4500a402ea/blizzard-end-user-license-agreement
10. https://github.com/josdemmers/Diablo4Companion/blob/master/README.md
11. https://github.com/d4lfteam/d4lf
12. https://github.com/aeon0/d4lf/blob/main/README.md
13. https://github.com/mxtsdev/d4-item-tooltip-ocr
14. https://github.com/akjroller/Diablo-4-XP-and-gold-per-hour/blob/main/README.md
15. https://github.com/Essyer/PoETiS
16. https://snosme.github.io/awakened-poe-trade/faq
17. https://www.icy-veins.com/d4/news/blizzards-stance-on-unauthorized-game-modifying-software-in-diablo-iv/

Intentadas y bloqueadas (HTTP 403), citadas solo por resumen de buscador:
- https://devtrackers.gg/pathofexile/p/cdea4d78-psa-waves-of-players-being-banned-for-use-of-third-party-tool-poe-overlay
- https://www.ownedcore.com/forums/diablo-4/diablo-4-bots-programs/998443-d4-loot-filter.html

## No encontrado

- **Ningún caso de baneo atribuido a `RegisterHotKey`** en ningún juego. Ni a favor ni en contra:
  simplemente no existe el caso. Es ausencia de evidencia, no evidencia de seguridad.
- **Ninguna declaración oficial de Blizzard sobre captura de pantalla u OCR.** Cero. La pregunta se
  hizo al menos tres veces en sus propios foros y nunca se respondió.
- **Ningún caso de baneo por OCR/captura que se haya mantenido tras apelación.** El único
  documentado (`diablo_qol`) fue revertido.
- **Cita textual de Chris Wilson** sobre el portapapeles y el test del segundo ordenador: la fuente
  primaria (devtrackers) devolvió 403. Tengo el contenido por resumen de buscador y es consistente
  entre varias búsquedas, pero **no he leído el post original**. Tratar como fiable-no-verificado.
- **Detalles del anti-cheat concreto de Diablo IV** (¿usa Warden?, ¿tiene componente de kernel?). No
  hay documentación pública específica de D4. Todo lo de la sección 6 es de WoW/D3 y se extrapola.
- **"Una pulsación, una acción" como política oficial de Blizzard.** Circula por todas partes; el
  único sitio donde la encontré escrita la etiqueta como especulación de un jugador. En GGG sí es
  política; en Blizzard **no verificada**.
- **Si Warden enumera procesos o lee títulos de ventana.** Fuentes comunitarias en contradicción
  directa. Sin resolver — y es justo el dato que decidiría si el nombre de nuestro ejecutable
  importa.
- **`mivuorin/d4-ocr`**: aparece en resultados de búsqueda pero no abrí el repo. No confirmo
  lenguaje, estrellas ni método.
- **Recuento de baneos de las oleadas de D4.** Se habla de "miles" en prensa de 2023, sin cifra
  oficial de Blizzard.
