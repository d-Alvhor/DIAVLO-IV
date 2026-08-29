# Refutación adversarial — «El arte de no ser baneado»

> Verificación del 29 de agosto de 2026 sobre `investigacion/crudo/arte-baneos.md`.
> 21 páginas abiertas, 8 búsquedas. El original **no se ha tocado**.
> Método: cada afirmación se contrasta contra la fuente primaria. Cuando la fuente primaria
> no se puede abrir, se dice — y entonces la afirmación no puede sostener una conclusión de diseño.

## Veredicto: **PARCIAL**

El esqueleto documental del original aguanta bien y en varios puntos aguanta *mejor* de lo que
el propio autor se atreve a afirmar: las citas textuales de `diablo_qol`, de TheTias-1192, de
PezRadar y de la EULA son **exactas**, y la corrección de atribución sobre MissCheetah es
**correcta y verificada al pie de la letra**. El inventario de repos es real: los ocho existen y
siete de las ocho fuentes de datos están bien atribuidas.

Pero hay **un error que tumba una conclusión de diseño**, **un error factual sobre la herramienta
que el documento propone imitar**, **una cita truncada de la EULA que le quita la mitad del
sentido a la sección 4**, y **una inferencia propia que el documento comete justo después de
reprochársela a otro**. Nada de esto invalida la recomendación final (que sigue siendo correcta),
pero sí invalida tres de los argumentos con los que se justifica.

---

## 1. Lo que se confirma sin reservas

| Afirmación del original | Estado | Verificación |
|---|---|---|
| `diablo_qol`: captura de tooltips + OCR, **sin leer memoria** | **Confirmado, textual** | El autor lo describe así: *"takes screenshots of item tooltips and then uses image to text to allow you to filter and search stash and inventory... and does not access game memory"* |
| Baneo Error 52, "malicious 3rd party software", 11 ago 2023 | **Confirmado** | Código 52 y motivo literales en el hilo |
| Cita de la reversión de Blizzard | **Confirmada palabra por palabra** | *"After an additional review of the evidence, we determined this closure was an error..."* |
| El autor **infirió** que Blizzard "está OK"; no lo dijo Blizzard | **Confirmado** | Literal: *"essentially indirectly sounds like Blizzard is OK with these type of screenshot tools that don't read game memory"*. La distinción del original es correcta |
| Filtro OCR: Tesseract 5.0 + Python + AHK enviando espacio | **Confirmado, textual** | El dev: *"if it is a junk equipment, it would send a 'space' key"* |
| TheTias-1192, 28 ago 2023, cita EULA y remata | **Confirmado** | Literal completo: *"Do yourself a favor and avoid a ban by not using your OCR software"* |
| Macro AHK: "while holding right click spam right click button", jun 2023 | **Confirmado, textual** | Post original del 16 jun 2023 |
| Oleadas D3 incluyeron AHK y macros, no solo bots | **Confirmado** | Unbanster: *"a mix of bots, TurboHUD, D3Helper, AutoHotkey and even mouse/keyboard macros"* |
| Cero casos de baneo por `RegisterHotKey` | **Confirmado como ausencia** | No aparece ni uno. El original ya lo etiqueta honestamente como ausencia de evidencia |
| Ningún blue post en los cuatro hilos | **Confirmado en los cuatro** | Verificado hilo a hilo, incluida la página 6 del #ModCheck |
| PezRadar, 26 jul 2023, nombra solo a TurboHUD4 | **Confirmado, textual** | Declaración completa verificada; no define categorías técnicas ni menciona OCR/captura |
| **MissCheetah-1661 es jugadora, no personal de Blizzard** | **Confirmado, textual** | Ella misma: *"I am another player, not a Mod."* La corrección del original es sólida |
| §1.C.vi existe y contiene "intercepts, collects, reads, or 'mines'" | **Confirmado** | Es el epígrafe **Data Mining**, sexto de la lista de 1.C |
| La EULA no menciona captura, overlay, OCR ni streaming | **Confirmado** | Ninguno de los cinco términos aparece en el documento |

**Inventario de repos — todos existen, estrellas y lenguaje correctos:**
`d4lfteam/d4lf` (206 ★, Python) · `josdemmers/Diablo4Companion` (321 ★, C#, Tesseract, umbral 80 %)
· `mxtsdev/d4-item-tooltip-ocr` (40 ★, Python, PaddleOCR con modelo propio, sin automatización ni
overlay) · `akjroller/Diablo-4-XP-and-gold-per-hour` (18 ★, Python) · `Essyer/PoETiS` (21 ★, Python,
API de GGG con session ID). El redirect `aeon0/d4lf` → `d4lfteam/d4lf` también se confirma.

El disclaimer de akjroller es literal: *"Warning! Running this could Violate Section 1.C.iii or
Section 1.C.iv of Blizzard End User License Agreement Use at your OWN RISK"*. Y el repo está
marcado **"Project no longer maintained"**.

---

## 2. Errores

### E1 — El caso «POE Overlay 2020» está mal atribuido, y de él cuelga una conclusión de diseño

Es el fallo más serio. El original lo pone en la tabla como *"Overlay que interactuaba con el
cliente → Oleada de baneos"*, y luego lo usa como una de las **dos** patas que sostienen la fila
más importante de la sección 8:

> "Ventana propia, sin overlay | **Nuestra mejor decisión** | Todos los baneos por overlay
> (TurboHUD, POE Overlay) implicaban overlay + lectura de estado"

La fuente primaria (devtrackers) devuelve **403 también para mí** — el mismo muro que encontró el
autor. Pero el resumen de esa misma página dice otra cosa: los bloqueos de cuenta de 2020 se
debieron a que la herramienta estaba **martilleando la web de GGG con del orden de millones de
peticiones diarias**, no a que dibujase un overlay ni a que leyese estado del cliente. Es decir:
un problema de abuso de API, categoría que no tiene **nada** que ver con nuestro diseño.

Consecuencia: la fila de la sección 8 se queda con **una sola** pata, TurboHUD — y TurboHUD
**lee memoria del proceso**. O sea que la evidencia disponible no separa "overlay" de "lectura de
memoria": están confundidas en el único caso que queda. **"Sin overlay" sigue siendo una decisión
prudente, pero el documento no tiene evidencia de que el overlay por sí solo haya baneado a nadie.**
No se puede llamar "nuestra mejor decisión" apoyándose en un caso mal atribuido y otro confundido.

Y hay un dato en contra dentro del propio documento que el autor no explota: `D4Companion`
(321 ★) **dibuja overlay** desde hace años y no consta oleada alguna. El original lo menciona en
la sección 7 y no lo cruza con la sección 8, donde lo contradice.

### E2 — Awakened PoE Trade **no** usa "portapapeles, exclusivamente"

El original lo repite tres veces: *"Portapapeles, exclusivamente"*, *"El modelo a imitar"*,
*"**Portapapeles**, nada más"*. Es falso. La propia documentación del proyecto incluye una
**guía de OCR**, y su sucesor para PoE 2 (Exiled Exchange 2) también. La herramienta de terceros
más tolerada de PoE **hace OCR**.

Esto no perjudica al proyecto: lo **beneficia**, y por eso el error importa. El documento se
priva del mejor argumento a favor de su propio diseño — que la herramienta comunitaria mejor
tolerada de todo el género combina portapapeles *y* OCR sin consecuencias conocidas — por
describirla mal.

### E3 — La cita de MissCheetah no se puede localizar, y el documento la propaga mientras avisa de no propagarla

El original la reproduce como *"Blizzard does not allow any third party software use that touches
their games, in any way"* y la llama *"la frase más repetida de todo este asunto"*. **No la he
encontrado**: ni en la página 1 del hilo del overlay, ni en la 6, ni por búsqueda directa de la
frase entrecomillada.

Lo que sí dice MissCheetah en ese hilo, verificado, es bastante **más flojo**:

> "Blizzard will not approve any third party software. They don't make it or control it so will
> not tell you that it is ok."

Que es una afirmación sobre **aprobación** ("no te van a bendecir"), no sobre **prohibición**
("no está permitido"). La versión fuerte que cita el original convierte un "no te lo aprueban"
en un "no te lo permiten" — y esa transformación es exactamente el fenómeno contra el que la
sección 5 avisa. El aviso de atribución es correcto; la cita que lo acompaña, no verificada.

### E4 — El baneo permanente por AHK no está "confirmado y sostenido"

El original lo pone como *"Baneo permanente | No [reversado]"* y lo eleva a *"la única técnica con
baneo confirmado y sostenido en D4 fuera de memoria/inyección"*. El hilo no sostiene ninguna de
las tres palabras:

- **"Confirmado"**: es **autoinformado por el baneado**. Blizzard no confirmó ni el motivo ni la
  causa. Que un jugador diga "me banearon por AHK" no establece que el AHK fuese la causa.
- **"Sostenido"**: el hilo **no documenta el desenlace**. No hay apelación, ni resultado, ni
  seguimiento. "No revertido" implica una no-reversión documentada; lo que hay es silencio.
- **"Única"**: sigue siendo el mejor caso disponible en su categoría, eso sí.

Corrección propuesta: *baneo permanente **autoinformado**, causa no confirmada por Blizzard,
desenlace no documentado*. Sigue apuntando en la misma dirección, con un tercio de la fuerza.

Nota relacionada: sobre las oleadas de D3, la fuente (Unbanster, un servicio comercial de
desbaneo que a su vez cita BuddyForum, un foro de botting) nombra AHK y macros, pero **no
establece que un macro puro, sin nada más, baneara a nadie**. Lo normal es que el macro
coexistiera con el bot en la misma cuenta. El original presenta la fila como si fuera precedente
limpio de "automatización de entradas sin memoria"; no lo es del todo.

### E5 — El caso de diciembre de 2025 es peor de lo que cuenta el original, y las cifras bailan

El original: *"otro caso de Error 52 del 28 de diciembre de 2025 revertido el 2 de enero de 2026
— **seis días**. Eso es el coste realista del peor caso."*

Verificado en el hilo, con tres correcciones:

1. Son **cinco** días (28 dic → 2 ene), no seis.
2. **El motivo del baneo nunca se reveló.** No hay ninguna conexión con OCR ni con captura de
   pantalla. Usarlo como referencia del coste de *nuestro* riesgo es meterlo en una categoría a
   la que no se ha demostrado que pertenezca.
3. **Y lo importante: la reversión no le devolvió el acceso.** El usuario sigue sin poder jugar
   después de que Blizzard confirmara oficialmente que levantaba la sanción, porque el error
   persiste por el lado de Steam.

Ese tercer punto **empeora** la conclusión del original. El peor caso realista no es "cinco o seis
días y vuelves"; es "te lo reconocen como error y aun así puedes seguir sin entrar". Conviene
decirlo así.

### E6 — La cita de §1.C.vi está truncada justo donde deja de convenir

El original cita:

> "Use any unauthorized process or software that intercepts, collects, reads, or 'mines'
> information generated or stored by the Platform"

y corta ahí. La cláusula **continúa**:

> "; provided, however, that Blizzard may, at its sole and absolute discretion, allow the use of
> certain third-party user interfaces."

Esa coletilla es el **único punto de toda la sección 1.C que contempla explícitamente interfaces
de terceros**. No nos autoriza nada — es discrecional y Blizzard nunca la ha ejercido públicamente
para D4 — pero desmonta la caracterización del original de que §1.C.vi es *"más específica y más
difícil de esquivar"*. Es más específica, sí; y es la **única** que trae una válvula de escape
incorporada. Omitir la segunda mitad de la frase que sostiene toda la sección 4 es un problema.

### E7 — El «test del segundo ordenador» sigue sin fuente, y la excepción documentada es otra

El original dedica la sección 3 a este criterio, lo presenta con blockquote atribuido a Chris
Wilson, lo llama *"el mejor criterio que existe"* y *"la formulación más limpia que he encontrado
en toda la investigación"*, y propone **adoptarlo como invariante de diseño**. La advertencia de
que no ha leído la fuente original está 170 líneas más abajo, en "No encontrado".

Eso es precisamente el fallo que este proyecto tiene documentado como regla: *el aviso al final no
anula la afirmación del principio*. Un criterio que se propone como invariante de diseño no puede
apoyarse en una cita que nadie ha leído.

Mis intentos: devtrackers **403** (igual que el autor); el FAQ de Awakened PoE Trade **no
contiene** ni la frase de Wilson, ni la excepción del portapapeles, ni el test del segundo
ordenador; el FAQ de Exiled Exchange 2, tampoco; el hilo oficial de PoE sobre overlays, tampoco.

Y hay un matiz que cambia el sentido: en el resumen de la fuente 403, la excepción que acompaña a
*"You may not run programs that interact with the Path of Exile game client"* no es el
portapapeles — es **leer los ficheros de log del cliente** (*"it's okay to run things that are
entirely external to the game, like ones that read the client log files"*). El original convierte
una excepción sobre logs en una excepción sobre portapapeles. Ambas son "externas al juego", pero
no son la misma frase.

**Lo que sí tengo verificado** es una declaración oficial de GGG, de CoryA_GGG, en el hilo público
sobre overlays de Overwolf:

> "In general, we do not encourage the creation or use of third-party tools because they may
> provide advantages for players that use them. I'm afraid that we're unable to guarantee if a
> tool is allowed or would remain allowed in the future."

Es menos elegante que el test del segundo ordenador, pero es real, es de GGG y dice lo mismo que
dice todo lo demás: **nadie te va a garantizar nada.** Sugiero sustituir la cita no verificada por
esta, y quedarse con el test del segundo ordenador como **heurística propia del proyecto**, sin
atribuírsela a nadie.

### E8 — El original comete la misma inferencia que reprocha

La sección 1 hace un buen trabajo señalando que el autor de `diablo_qol` **infirió** la postura de
Blizzard. Y a continuación, sobre el caso contrario, concluye:

> "La diferencia entre los dos casos **no es el OCR**. Es que el segundo **enviaba pulsaciones al
> juego**. Esa es la línea."

Eso también es una inferencia del autor, y va contra lo que dice la fuente. TheTias-1192 no
condenó las pulsaciones: citó la cláusula de *"changes and/or facilitates the gameplay"* y remató
**"avoid a ban by not using your OCR software"** — condenó el OCR, sin más. El consenso del hilo
fue contra la herramienta OCR, no contra el AHK. La lectura del original es razonable y
probablemente correcta como modelo del riesgo real, pero es **suya**, simétrica a la que critica,
y debe etiquetarse igual.

### E9 — D4LF cruza tres líneas rojas, no dos, y la tercera es la grave

El original lo describe como *"Automatiza ratón y teclado... y dibuja overlay. Cruza dos líneas
rojas nuestras"*. Ambas confirmadas. Pero falta la tercera, que está en la propia descripción de
la fuente de datos del original y no se computa:

D4LF instala un **DLL firmado (`saapi64.dll`) en el directorio de Diablo**, y **el juego lo carga
en su propio proceso**:

> "Tolk has a feature that allows custom third-party TTS DLLs to be loaded. D4 automatically loads
> the DLL, which actually just sends the text to another application rather than reading it aloud."

Eso es **código de terceros ejecutándose dentro del proceso del juego**. No es inyección clásica
—es el juego el que lo carga, por un mecanismo de accesibilidad legítimo— pero cae de lleno en la
categoría que la propia tabla de la sección 2 marca como **letal** ("firma detectable dentro del
proceso"). D4LF debería figurar como el ejemplo más agresivo del inventario, no como uno más de
la lista de "automatiza y dibuja".

Detalle operativo relevante: requiere activar *Screen Reader* y *3rd Party Screen Reader* en
Opciones → Accesibilidad del juego, lo que deja rastro de configuración en el cliente.

### E10 — Correcciones menores

| Punto | Original | Verificado |
|---|---|---|
| Reversión de `diablo_qol` | "~24 h" | Baneo 11 ago, reversión constatada el 13 ago: **~1-2 días** |
| Hilo #ModCheck | "seis páginas" | **Al menos siete** |
| akjroller = "nuestra pila exacta" | — | Coincide `mss`; **difiere el OCR** (Pytesseract vs. nuestro `winocr`) y añade OpenCV/Numpy/Pillow. Coincidencia parcial |
| Cita 1.C.iii / 1.C.iv de akjroller | Se reproduce sin comentario | **Está mal numerada en origen**: iii y iv de la lista 1.C son *Prohibited Commercial Uses* y *"esports"*. El autor del repo quiso citar las viñetas anidadas dentro de *Cheating*. En un documento que discute numeración de cláusulas, conviene señalarlo |

---

## 3. Hueco rellenado: `mivuorin/d4-ocr`

El original lo dejó honestamente en "No encontrado" (*"no abrí el repo"*). Abierto:

| Campo | Dato |
|---|---|
| Existe | Sí |
| Estrellas | **0** |
| Lenguaje | **C# / .NET** (el original conjeturaba que no lo sabía; no es Python) |
| Fuente de datos | **Captura de pantalla vía PInvoke/interop nativo de Windows + Tesseract** (`tessdata_fast`) |
| Overlay | **Sí** — usa `GameOverlay.Net` para dibujar resaltados sobre el juego |
| Estado | Prueba de concepto abandonada, 7 commits. El autor admite: *"currently it's not performing fast enough to exceed experienced players reading speed"* (1-3 s por escaneo) |
| Disclaimer | Sí, propio: *"DOES NOT MODIFY DIABLO 4 GAME IN ANY WAY"* |

O sea: **sí dibuja overlay**, y por tanto **no** es un modelo a seguir para nosotros. Conviene
meterlo en la tabla de la sección 7 con ese dato, porque tal como está ("OCR para gestión de
inventario", sin más) suena más cercano a nuestro diseño de lo que es.

---

## 4. Material nuevo que refuerza al original

**N1 — Evidencia positiva de que D4 no tiene anti-cheat de kernel.** La sección 6 del original
deja como no resuelto si D4 usa Warden y si tiene componente de kernel. Hay un indicio que no
usa: **D4 funciona en Linux con Proton (nivel gold)**. Un anti-cheat con driver de kernel sería
incompatible con esa vía. No es documentación oficial, pero es un argumento estructural mejor que
las fuentes comunitarias en contradicción que cita el original. Los títulos de Blizzard con Warden
son, además, sistemas de **modo usuario**.

**N2 — `RegisterHotKey` sí toca al juego, en un sentido concreto.** El original lo presenta como
la decisión más defendible del proyecto y, en detectabilidad, lo es. Pero falta un matiz técnico:
`RegisterHotKey` registra un atajo **a nivel de sistema** y **suprime esa tecla para la aplicación
en primer plano**. Si D4 está en primer plano y el usuario pulsa el atajo registrado, **D4 no
recibe esa tecla**. Eso es una interacción real con la entrega de entrada al cliente del juego —
inocua, pero no nula, y capaz de "comerse" un keybind del jugador si hay colisión. Implicación de
diseño: elegir atajos que no colisionen con ninguna tecla usable de D4 (F-keys altas, o con
modificador poco habitual), y documentar la supresión al usuario. El test del segundo ordenador lo
sigue pasando; la afirmación "no toca el juego en absoluto" no.

**N3 — La categoría "ficheros de log" no aparece en el documento.** En PoE, leer los logs del
cliente es la excepción explícitamente tolerada. D4 no expone logs equivalentes útiles, así que
no nos sirve — pero merece una línea en "No encontrado", porque es la única vía que un titular de
derechos ha bendecido por escrito en este género, y explica por qué el portapapeles y los logs
tienen mejor prensa que la captura de pantalla: en ambos, **el juego decide qué te entrega**. En
la captura, no.

---

## 5. Qué hay que cambiar en el original

Por orden de gravedad:

1. **Reescribir la fila «POE Overlay» de la sección 1** y **desmontar la justificación de la fila
   "sin overlay" de la sección 8**. La decisión de no usar overlay se mantiene por prudencia y por
   el test del segundo ordenador, **no** por casos de baneo: no hay ninguno limpio.
2. **Corregir Awakened PoE Trade**: portapapeles **y OCR**. Y usarlo como el argumento a favor que
   es.
3. **Completar la cita de §1.C.vi** con la coletilla de las interfaces de terceros, y ajustar la
   tesis de la sección 4 en consecuencia.
4. **Degradar el caso AHK** a "autoinformado, causa no confirmada, desenlace no documentado".
5. **Sustituir la cita de Chris Wilson** por la de CoryA_GGG (verificada) y quedarse el test del
   segundo ordenador como heurística propia, sin atribución.
6. **Retirar o marcar como no localizada la cita de MissCheetah**, sustituyéndola por la
   verificada, que dice algo más débil.
7. **Etiquetar como inferencia propia** la conclusión "la diferencia no es el OCR".
8. **Mover D4LF** a la categoría más grave del inventario (DLL cargado en el proceso).
9. **Corregir el caso de dic-2025**: cinco días, motivo desconocido, sin relación con OCR — y
   añadir que la reversión no restauró el acceso.
10. Rellenar `mivuorin/d4-ocr` con los datos de la sección 3 de este documento (**dibuja overlay**).

**Lo que NO cambia:** la recomendación de diseño del original es correcta y sale reforzada de la
verificación. Captura + OCR sin memoria, sin inyección, sin overlay y **sin enviar entradas al
juego** sigue siendo la configuración con menos exposición documentada del género. La fila
*"Sin enviar entradas al juego — Crítico, no negociar"* es la conclusión mejor sostenida del
documento y la verificación la deja intacta. También se confirma que **no existe permiso, no
existe lista blanca y no existe proceso de aprobación** — y que el riesgo residual real es el
falso positivo en una oleada, no la detección.

---

## Fuentes de esta verificación

Abiertas y leídas (21):

1. https://www.blizzard.com/en-us/legal/fba4d00f-c7e4-4883-b8b9-1b4500a402ea/blizzard-end-user-license-agreement (dos pasadas: estructura de 1.C y texto de Data Mining)
2. https://us.forums.blizzard.com/en/d4/t/blizzard-admits-ban-was-an-error-use-of-item-search-qol-screenshot-tool/115166
3. https://us.forums.blizzard.com/en/d4/t/i-made-an-ocr-equipment-filter-tool-is-it-legal/121740
4. https://us.forums.blizzard.com/en/d4/t/a-notice-regarding-unauthorized-game-modifying-software-in-diablo-iv/102121
5. https://us.forums.blizzard.com/en/d4/t/third-party-app-diablo-iv-overlay-is-permitted-modcheck/41715
6. https://us.forums.blizzard.com/en/d4/t/third-party-app-diablo-iv-overlay-is-permitted-modcheck/41715?page=6
7. https://us.forums.blizzard.com/en/d4/t/got-banned-for-autohotkey/52417
8. https://us.forums.blizzard.com/en/d4/t/problem-with-error-code-52/240711
9. https://us.forums.blizzard.com/en/d4/t/diablo-4-account-unban-appeal/240868
10. https://github.com/d4lfteam/d4lf
11. https://github.com/josdemmers/Diablo4Companion
12. https://github.com/mxtsdev/d4-item-tooltip-ocr
13. https://github.com/mivuorin/d4-ocr
14. https://github.com/akjroller/Diablo-4-XP-and-gold-per-hour
15. https://github.com/Essyer/PoETiS
16. https://snosme.github.io/awakened-poe-trade/faq
17. https://kvan7.github.io/Exiled-Exchange-2/faq
18. https://www.pathofexile.com/forum/view-thread/3637217
19. https://www.poeoverlay.com/about
20. https://www.poeoverlay.com/faq
21. https://unbanster.com/diablo-3-season-5-ban-wave-aftermath/

Búsquedas (8): cita de MissCheetah · oleadas D3 2015-2016 con AHK · `RegisterHotKey` vs hook y
anti-cheat · cita de Chris Wilson y test del segundo ordenador · Error 52 dic-2025/ene-2026 ·
redirect `aeon0/d4lf` · baneos a usuarios de D4LF/D4Companion · oleada PoE Overlay 2020.

Bloqueada (403), igual que para el autor del original:
- https://devtrackers.gg/pathofexile/p/cdea4d78-psa-waves-of-players-being-banned-for-use-of-third-party-tool-poe-overlay

## No encontrado (sigue sin resolverse)

- **El post original de Chris Wilson.** Cuatro rutas alternativas intentadas, ninguna lo contiene.
  El test del segundo ordenador **no tiene fuente primaria legible**.
- **La frase fuerte atribuida a MissCheetah.** No localizada en el hilo ni por búsqueda directa.
- **Baneos a usuarios de D4LF o D4Companion.** Ninguno reportado, pese a que ambos automatizan y/o
  dibujan overlay. Refuerza el argumento de detección del original — y debilita el de permiso.
- **Confirmación de que D4 usa Warden.** Sigue sin documentación pública específica. El indicio de
  Proton (N1) es lo mejor disponible.
- **Si un macro puro, sin bot asociado, baneó a alguien en D3.** La fuente no lo separa.
- **Causa real del baneo de dic-2025.** Nunca revelada.
