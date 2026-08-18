---
titulo: Ajustes de PC
capa: nucleo
parche: todas
temporada: todas
estado: vivo
entitlement: base
verificado: 2026-08-19
revisar_despues: 2026-10-15
---

## Lo primero: el menú entero es vuestro ✅

Buenas noticias, y en esta guía son raras: **todo el dominio de "ajustes" es juego base ✅**. Gráficos, Jugabilidad (*Gameplay*), Sonido, Controles y Accesibilidad no están detrás de ninguna compra. Tampoco lo están las dos mejoras técnicas más recientes.

::: evidencia nivel=oficial fuentes=blizzard-3-1-0
Las notas oficiales del parche 3.1.0 (30/06/2026) listan, dentro de la sección literal **"Base Game"**: *"Added XESS 3 support for Intel GPUs"* y *"Added DLSS 5X and 6X support for Nvidia GPUs"*. Estar en esa sección significa ✅ juego base.
:::

::: aviso tipo=ojo
Aviso de método, porque condiciona todo lo gráfico que viene después: **no existe ninguna guía de ajustes de Diablo IV publicada por Maxroll, Icy Veins ni Mobalytics para la Temporada 14**. El hueco es de las fuentes de élite, no de la búsqueda. Lo gráfico de este capítulo descansa en guías generalistas de calidad media que se contradicen entre sí en más de una docena de puntos, y esas contradicciones van marcadas. Nada de esto es "la configuración canónica de un top del ladder": esa configuración no está publicada por escrito en ninguna parte, solo en vídeo.
:::

## Pantalla y sincronización ✅

| Ajuste | Recomendación | Por qué |
|---|---|---|
| **Display Mode** (modo de pantalla) | Ventana sin bordes (*Windowed Fullscreen*) | Rinde igual que pantalla completa exclusiva y no se rompe al hacer Alt-Tab. ⚠️ Hay fuentes que defienden lo contrario |
| **Resolution** | La nativa del monitor | Nunca bajes la resolución de salida: se usa un escalador |
| **Resolution Percentage** | Sin tocar | Con escalador activo, el escalado ya lo hace él |
| **Vertical Sync** | Off | Mete latencia. Se sustituye por un límite de FPS |
| **Max Foreground FPS** | Limitado, ver bloque | Evita *tearing* y picos térmicos |
| **Max Background FPS** | Bajo | Menos consumo al hacer Alt-Tab a Discord |
| **Limit Cutscene FPS** | On | Respiro para la GPU, cero impacto jugable |
| **NVIDIA Reflex Low Latency** | Activado + Boost | Baja la latencia real de entrada |
| **Sharpen Image** | A ojo | ⚠️ Las fuentes dan valores incompatibles |

::: evidencia nivel=disputa fuentes=switchblade-settings,charlieintel-settings,dexerto-settings,finalboss-settings
**Límite de FPS:** con G-Sync o FreeSync, capar 3-5 FPS por debajo del refresco del monitor; sin ellos, al refresco exacto. Las cifras publicadas van de 400 (Charlie INTEL) a 200 (UnGeek) a "igual al refresco" (Switchblade): no hay consenso, y el valor absoluto importa menos que el hecho de capar. **Max Background FPS:** 30. **Sharpen Image:** Charlie INTEL dice 90 y Dexerto dice 6 — escalas incompatibles, ninguna fuente documenta el rango real del deslizador.
:::

::: evidencia nivel=unica fuentes=kotaku-settings
El contador de FPS nativo del juego se abre con `Ctrl + R` en partida ✅. Es la forma de medir sin instalar overlays. Dato de 2023, no recontrastado en 3.1.x.
:::

## Calidad gráfica, ajuste por ajuste ✅

::: evidencia nivel=unica fuentes=switchblade-settings
Ranking de coste en rendimiento, de mayor a menor: **Shadow Quality → Ray Tracing → Fog Quality → SSAO Quality → Geometric Complexity → Particle Quality → Screen Space Reflections**. Shadow Quality se describe como el ajuste con mayor coste unitario del juego. ⚠️ Esta fuente se fecha en mayo de 2026 pero declara cubrir la Temporada 8: incoherencia interna reconocida.
:::

| Ajuste | Perfil calidad | Perfil FPS / Pit alto |
|---|---|---|
| **Texture Quality** | Alta | Media si tienes poca VRAM |
| **Anisotropic Filtering** | Máximo | Máximo (es prácticamente gratis) |
| **Shadow Quality** | Alta | **Media** — el primero que hay que bajar |
| **Dynamic Shadows** | On | On (Off solo en equipos muy justos) |
| **Soft Shadows** | On | **Off** ⚠️ sin consenso entre fuentes |
| **Shader Quality** | Alta | Alta — por debajo hay *pop-in* visible |
| **SSAO Quality** | Alta | Media o baja |
| **Fog Quality** | Alta | Media o baja |
| **Clutter Quality** | Media/alta | **Baja** — además limpia el suelo de ruido visual |
| **Water Simulation Quality** | Alta | Baja ⚠️ sin consenso |
| **Anti-Aliasing Quality** | Alta | Alta, u Off si usas escalador ⚠️ sin consenso |
| **Geometric Complexity** | Alta | Media |
| **Physics Quality** | Alta | **Baja/media si la CPU va justa** |
| **Particle Quality** | Alta | Media |
| **Screen Space Reflections** | On | **Off** |
| **Distortion** | On | Off |
| **Low FX** | Off | **On** en contenido denso |
| **Ray Tracing (todos)** | Off | **Off** |

::: evidencia nivel=unica fuentes=switchblade-settings,informe-ajustes-pc
El trazado de rayos completo *"aproximadamente reduce a la mitad"* los FPS: una RTX 3080 que hace ~90 FPS a 4K en Ultra baja a 45-50 FPS con RT completo, por debajo del objetivo de 60 FPS de la propia Blizzard. Solo RT Shadows tiene coste asumible (15-20 %) y solo desde una RTX 4080. **Para empuje de leaderboard: Off, sin discusión.**
:::

## Escalado y generación de fotogramas ✅

Es la parte más reciente y más rentable del menú, y es toda juego base ✅.

::: evidencia nivel=corroborado fuentes=blizzard-3-1-0,icyveins-dlss4
Escalador por marca de GPU: **Nvidia RTX → DLSS** (modelo transformer, DLSS 4 nativo con Multi Frame Generation desde julio de 2025, sin necesidad de la app de Nvidia; DLSS 5X y 6X añadidos en 3.1.0). **AMD Radeon → FSR 3.1**, modo Quality. **Intel Arc → XeSS 3** ✅ desde 3.1.0, modo Quality.
:::

::: evidencia nivel=unica fuentes=informe-ajustes-pc
Modo de DLSS según la resolución del monitor: a 1080p, **Balanced o Quality** (evita Performance: renderiza internamente a ~720p y se nota); a 1440p, **Quality**; a 4K, **Performance o Balanced**. Síntesis de guías generalistas, no de fuente de élite.
:::

::: evidencia nivel=unica fuentes=informe-ajustes-pc
Cifras publicadas de Nvidia con DLSS 4 + Multi Frame Generation a 4K con todo al máximo: RTX 5070 ~190 FPS, 5070 Ti ~230, 5080 ~270, 5090 ~370. DLSS 4.5 añade 6X Dynamic Multi Frame Generation, que ajusta el multiplicador solo.
:::

::: aviso tipo=truco
La generación de fotogramas **inserta fotogramas sintéticos**: sube los FPS que ves sin bajar la latencia de entrada al mismo ritmo. Para farmeo cómodo, activadla. Para un intento serio de Pit alto, donde esquivar a tiempo decide si completáis o morís, valorad desactivarla y dejar **Reflex + Boost** encendido. ⚠️ Este matiz es razonamiento técnico del expediente, no una cita de ninguna guía de Diablo IV: no hay medición publicada.
:::

## HDR ✅

::: evidencia nivel=unica fuentes=evezone-hdr
El HDR de Diablo IV sufre un "filtro gris" documentado: los niveles de negro no están calibrados para todas las pantallas. Hay tres controles en Gráficos — **HDR Brightness**, **Black Point** (viene demasiado alto por defecto: bajadlo) y **White Point**. Si el HDR se ve raro en mitad de la partida, `Win + Alt + B` reinicia el intercambio de perfil de color entre Windows y el juego. Fuente única de febrero de 2026, sin contrastar.
:::

Recomendación práctica: si el monitor no es OLED o mini-LED con buen brillo pico, **HDR en Off**. Un HDR mal calibrado destruye la lectura de sombras, que es justo lo que necesitáis en el Pit.

## Nigromante: la pantalla llena de esbirros

Aquí es donde vuestra clase os cobra el peaje que ninguna guía de ajustes menciona.

::: evidencia nivel=corroborado fuentes=datafile-3-1-0,maxroll-skill-trees
El ejército crece a partir del nivel 15, y las variantes que lo hacen crecer son ✅ juego base: ***Coven*** (+2 magos esqueléticos) a nivel 15, ***Master of Puppets*** (+3 guerreros esqueléticos) a nivel 16, ***Gravebloom*** (3 gólems) a nivel 20. Verificado en el fichero de datos del juego, versión 3.1.0.72698, y en la tabla publicada de árboles de habilidades.
:::

::: evidencia nivel=sinconfirmar fuentes=informe-ajustes-pc
**No existe ni un solo benchmark que mida el coste en FPS de los esbirros del Nigromante en la Temporada 14.** Ninguna guía consultada lo aborda con números. Todo lo que sigue es razonamiento sobre hechos documentados, no medición.
:::

Los hechos sobre los que se razona: **Low FX** reduce el número de sistemas de partículas renderizados y se describe como buena opción para encuentros pesados; **Physics Quality** es un ajuste de CPU y cada esbirro es una entidad más que simular; **Particle Quality** gobierna la densidad de partículas, y Explosión de Cadáveres (*Corpse Explosion*) es un generador masivo de ellas; **Display Minion Health Bars** dibuja una barra por esbirro invocado.

Receta, en este orden:

1. **Physics Quality → Baja/Media.** Alivia la CPU, que simula cada entidad.
2. **Particle Quality → Media.** Explosión de Cadáveres revienta el *frametime*.
3. **Low FX → On** en Hordas Infernales, Marea Infernal y Pit alto.
4. **Clutter Quality → Baja.** Menos suelo que dibujar bajo la nube.
5. **Screen Space Reflections → Off.** Coste alto justo en mazmorras.
6. **Display Minion Health Bars → Off** en contenido denso.
7. **Shadow Quality → Media.** Cada esbirro proyecta sombra dinámica.

::: evidencia nivel=unica fuentes=icyveins-efectos-jugadores
Blizzard ya hizo que las mascotas del Nigromante sean casi invisibles **para los otros jugadores**, específicamente por visibilidad. Traducción para vuestro dúo: tu pareja no verá tus esqueletos con toda su carga visual, pero **tú sí ves los tuyos**. El coste de rendimiento es individual, no compartido.
:::

::: evidencia nivel=unica fuentes=icyveins-efectos-jugadores
**No existe ninguna opción para desactivar los efectos visuales de otros jugadores.** Icy Veins documenta la petición masiva de la comunidad y confirma que no hay interruptor. ⚠️ La fuente es anterior a *Vessel of Hatred*: no se ha podido confirmar si en 3.1.3 sigue igual. Comprobadlo vosotros en el menú.
:::

## Jugabilidad: el oro que casi nadie toca ✅

::: aviso tipo=ojo
La única enumeración completa del menú de Jugabilidad que existe por escrito es de abril de 2023 y viene de una fuente vetada en este proyecto. Los nombres de los ajustes clave (Advanced Tooltip, Display Minion Health Bars, HUD Configuration) sí se siguen citando en fuentes de 2026, pero **la estructura exacta de pestañas en 3.1.3 no está verificada**. Algunos ajustes aparecen unas veces en Jugabilidad y otras en Accesibilidad. Buscadlos en las dos.
:::

| Ajuste | Valor | Por qué |
|---|---|---|
| **Advanced Tooltip Information** | **ON** | Muestra el rango de cada afijo y si un modificador es aditivo o multiplicativo. Sin esto no se puede min-maxear, y además **el filtro de botín parsea mal** |
| **Advanced Tooltip Compare** | **ON** | Al comparar muestra lo ganado, lo perdido y el efecto sobre las habilidades equipadas |
| **Show All Damage Numbers** | ON al aprender · **OFF en Pit alto** | Os enseña qué habilidad pega de verdad; con el ejército montado tapa el suelo de cifras |
| **Show Items on Ground Behavior** | **Toggle** | Etiquetas fijas en vez de mantener pulsado |
| **Item Label Duration on Drop** | Al máximo | Duración de la etiqueta tras caer el objeto |
| **Display Minion Health Bars** | ON aprendiendo · OFF en denso | Os avisa de que se os mueren los esqueletos, a cambio de decenas de barras superpuestas |
| **Monster Health Bar Option** | **Always On** | Si tú no matas directamente, es la única forma de saber si el DPS de los esbirros basta |
| **Display Own Health / Resource** | ON | La Esencia (*Essence*) es vuestro limitador |
| **Display Player Highlight** | ON | |
| **Highlight Player When Obscured** | **ON** | Te contornea cuando algo te tapa. Con dos nigromantes, obligatorio |
| **Player Highlight Color** | Que no lo use el Nigromante | Nada de morado, verde veneno ni gris hueso. Naranja o cian |
| **Screen Shake Effects** | Off | Menos mareo, más precisión al esquivar |
| **Combat Hit Flash** | Off en Pit alto | Con el ejército pegando, la pantalla no para de parpadear |
| **HUD Configuration** | Probad las dos | Esquina libera centro; centrado se lee mejor de reojo |

::: aviso tipo=truco
Sois dos nigromantes: **elegid colores de resaltado distintos entre vosotros**. En una nube de Explosión de Cadáveres es la diferencia entre saber quién eres tú y jugar a ciegas.
:::

::: aviso tipo=peligro
El atajo de **Show Item Labels** viene por defecto en `Alt`. Rebindeadlo. Si hablas por Discord con tu pareja y haces Alt-Tab, la tecla se queda pegada y el juego se comporta de forma errática. Ponedlo en `Tab` o en un botón lateral del ratón.
:::

## Filtro de botín (Loot Filter) ✅

::: evidencia nivel=oficial fuentes=blizzard-loh-web,icyveins-loot-filter,refutacion-comunidad-arbol
El filtro de botín es **✅ juego base**. La web oficial de Blizzard lo anuncia en un apartado titulado *"Major Updates for all Diablo IV Players"*: *"a new Loot Filter will ease the discovery of desired items across Sanctuary"*. La verificación adversarial de este expediente lo confirma como *"free universal update available to every Diablo 4 player regardless of expansion ownership"*. ⚠️ **Maxroll es el único disidente**: escribe que requiere *Lord of Hatred* y que no está en el juego base. Va contra la fuente primaria y contra el resto del expediente.
:::

::: paso n=1 obligatorio=si entitlement=base
Abrid **Opciones → Jugabilidad** y comprobad si aparece la entrada del filtro de botín. Son treinta segundos y cierran la única contradicción relevante de este capítulo. Activad también **"Enable Loot Filter shortcut on Game Menu"** y dadle un atajo de teclado propio en Controles.
:::

Cómo funciona: las reglas se evalúan **de arriba abajo** y la de más arriba manda. Podéis guardar varios filtros pero solo uno está activo. Cada regla puede **mostrar, recolorear, ocultar la etiqueta u ocultarlo todo**. Los filtros **no tocan las tasas de drop**, solo la presentación — pero **lo que está oculto no se puede recoger**.

::: evidencia nivel=disputa fuentes=informe-ajustes-pc,informe-herramientas,d4lootfilter-viewer
Límite de reglas por filtro: **25** según unas fuentes, **30** según d4lootfilter.com. Sin resolver. Presupuestad 25 y no os quedaréis cortos por sorpresa.
:::

Condiciones disponibles: rango de poder del objeto, rareza, tipo, propiedades, comprobación de Afijo Superior (*Greater Affix*), afijos requeridos y opcionales, mejora de Códice, y si es un único concreto. Hay además una condición de **bonus de conjunto de Talismán 🔒 Lord of Hatred**: existe en el menú, pero sin el sistema de Talismán y Charms no os sirve de nada. Ignoradla; el resto del filtro funciona igual ✅.

::: evidencia nivel=corroborado fuentes=maxroll-loot-filter,d4lootfilter-viewer
**Importar y exportar códigos de filtro solo funciona en PC.** Es una limitación de plataforma, no de expansión: en PS5 y Xbox se pueden crear y editar reglas a mano en el menú, pero no hay forma de pegar un código. ⚠️ D4 Filter Forge afirma en cambio que el formato es multiplataforma y viaja con la cuenta de Battle.net; nadie lo confirma explícitamente.
:::

::: paso n=2 obligatorio=no entitlement=base
Plan para vuestro dúo: el de PC importa un filtro preconstruido pegando el código. Después comprobáis si aparece en la cuenta del de PS5 (dos minutos, y si funciona os ahorra media hora). Si no aparece — lo más probable —, el de PS5 abre **d4lootfilter.com** en el móvil, pega ahí el mismo código y la web le descompone el filtro en la lista completa de reglas legibles. Luego las teclea a mano. Media hora, una vez por temporada, y los dos veis exactamente lo mismo en pantalla.
:::

No empecéis con un filtro estricto. Mientras subís nivel necesitáis ver legendarios para extraer aspectos al Códice. Escalad de suave a estricto conforme subáis de Tormento.

## Accesibilidad ✅ — no es "para otros", es rendimiento

| Ajuste | Recomendación |
|---|---|
| **Cursor Size** y **High Contrast Cursor** | Grande y en alto contraste. Perder el cursor en una nube de Explosión de Cadáveres es una muerte |
| **HUD Font Scaling** | Subidlo |
| **Colorblind Filter** | Probadlo aunque no seáis daltónicos: cambia la paleta y puede separar los efectos del fondo |
| **Character Visibility** | Probadlo. ⚠️ Nombre documentado en 2024, sin confirmar en 3.1.3 |
| **Reduce Strobing** | ON si hay fotosensibilidad; puede quedar algún destello en cinemáticas |

## Keybinds ✅ — la sección que más va a subir vuestro nivel

Si de todo este capítulo solo hacéis una cosa, que sea esta.

::: evidencia nivel=corroborado fuentes=iggm-keybinds,kotaku-settings
En **Opciones → Controles → Key Bindings**, el ajuste **"Combine Move/Interact/Basic Skill Slot"** viene activado por defecto: el clic izquierdo mueve, interactúa y lanza la habilidad básica a la vez. Consecuencia documentada: si clicas sin querer sobre un enemigo, le atacas, y te quedas clavado atacando cuando querías reposicionarte. **Desactivadlo** y asignad **Move & Interact** al clic izquierdo y la habilidad básica a otra tecla.
:::

Las dos funciones que separan a un jugador de otro:

- **Force Move** (movimiento forzado): mantienes la tecla y corres hacia el cursor **sin atacar ni interactuar con nada**. Muchos jugadores lo ponen en la rueda del ratón; hay que desactivar antes el zoom con rueda para liberarla.
- **Hold Position / Stand Still** (mantener posición): atacas sin moverte del sitio. Por defecto está en `Shift`.

**Por qué esto es crítico justo para vosotros:** las maldiciones (Doncella de Hierro, Decrepitud) y Tentáculos y Explosión de Cadáveres se lanzan sobre el suelo, y la nube negra de Explosión de Cadáveres tapa jugadores, botín, monstruos, efectos, objetos de misión y cofres — es queja documentada en los foros oficiales. Dentro de esa nube, si no puedes moverte sin atacar ni atacar sin moverte, estás jugando a ciegas.

::: evidencia nivel=sinconfirmar fuentes=informe-ajustes-pc
Esquema de teclado sugerido. **No es la configuración canónica de ningún jugador top**: los vídeos de rob2628 y wudijo sobre keybinds existen pero no se pudo extraer su contenido, y ninguna fuente escrita de élite publica un esquema para la Temporada 14. Esto es síntesis de guías generalistas: Move & Interact en clic izquierdo · habilidad fundamental en clic derecho · básica en `Q` o botón lateral · ranuras restantes en `1 2 3 4` · Force Move en la rueda del ratón · Hold Position en `Shift` · Evadir en `Espacio` · poción en botón lateral · montura en `Z` · portal en `T` · Show Item Labels fuera de `Alt` · filtro de botín con atajo propio.
:::

La regla de oro sí es sólida: **todo lo reactivo** (evadir, poción, defensiva) va donde el dedo ya está; **todo lo proactivo** (invocar, buffs) puede ir más lejos. Y las seis ranuras de la barra están abiertas desde el nivel 1 ✅, así que podéis dejar el mapeado hecho desde el primer minuto y no volver a tocarlo.

::: evidencia nivel=disputa fuentes=kotaku-settings,informe-ajustes-consola
**Y en el mando la recomendación se invierte, o no.** Sobre el equivalente "Combine Interact and Basic Skill" en consola hay dos posturas en el expediente: dejarlo **combinado**, porque el mando tiene menos botones y separar funciones cuesta más de lo que aporta; o ponerlo en **OFF**, calificado como crítico precisamente para Nigromante, para que Interactuar tenga botón propio. El informe dedicado a consola es la fuente más específica y dice OFF. Que tu pareja lo pruebe en las dos posiciones antes de decidir.
:::

## Fuera del juego ✅

::: evidencia nivel=unica fuentes=switchblade-settings
Ajustes de sistema: **HAGS** (planificación de GPU por hardware) activado, plan de energía en alto rendimiento, Modo Juego en On, Integridad de Memoria desactivada si se puede, Battle.net cerrándose al arrancar, drivers de GPU al día (obligatorio para DLSS 5X/6X y XeSS 3) y SSD — en disco mecánico las transiciones de zona son insufribles.
:::

::: aviso tipo=peligro
Sobre overlays de terceros (Diablo4Companion, d4lf, Overwolf): la EULA de Blizzard prohíbe el software no autorizado expresamente, no hay lista blanca ni proceso de aprobación, y **no existe ninguna declaración de Blizzard de 2026** que actualice esa política. Con el filtro de botín ya dentro del juego, el beneficio marginal no compensa el riesgo — y en dúo, si uno pierde la cuenta se acabó el proyecto para los dos. Lo mismo para el truco de editar `LocalPrefs.txt`: fuente única, sin verificar.
:::

## Lo que este capítulo no sabe

Dicho a la cara, porque un hueco declarado vale más que un número con buena pinta:

- **Coste real en FPS de los esbirros**: cero benchmarks. La receta es razonamiento, no medición.
- **Auto-recogida de oro, transparencia del chat y marcadores de área de habilidad**: ninguna fuente documenta esos interruptores. No se afirma que no existan; se afirma que no se han visto.
- **Estructura del menú en 3.1.3**: la enumeración completa disponible es de 2023 y de fuente vetada.
- **Sincronización de ajustes entre PC y PS5**: sin fuente. Asumid que no y configurad cada máquina aparte.
