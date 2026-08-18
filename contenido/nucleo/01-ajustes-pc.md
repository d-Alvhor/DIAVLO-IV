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

Buenas noticias, y en esta guía son raras: **todo el dominio de "ajustes" es juego base ✅**. Gráficos, Jugabilidad (*Gameplay*), Sonido, Controles y Accesibilidad no están detrás de ninguna compra, y las dos mejoras técnicas más recientes tampoco.

::: evidencia nivel=oficial fuentes=blizzard-3-1-0
Las notas oficiales del parche 3.1.0 (30/06/2026) listan, dentro de la sección literal **"Base Game"**: *"Added XESS 3 support for Intel GPUs"* y *"Added DLSS 5X and 6X support for Nvidia GPUs"*. Estar en esa sección significa ✅ juego base.
:::

::: aviso tipo=ojo
Aviso de método: **ni Maxroll, ni Icy Veins, ni Mobalytics han publicado una guía de ajustes para esta temporada**. El hueco es de las fuentes de élite, no de la búsqueda. Lo gráfico de este capítulo descansa en guías generalistas de calidad media que se contradicen entre sí en más de una docena de puntos, y esas contradicciones van marcadas.
:::

## Pantalla y sincronización ✅

| Ajuste | Recomendación |
|---|---|
| **Display Mode** (modo de pantalla) | Ventana sin bordes (*Windowed Fullscreen*): rinde igual que pantalla completa exclusiva y no se rompe al hacer Alt-Tab. ⚠️ Hay fuentes que defienden lo contrario |
| **Resolution** | La nativa. Nunca bajes la resolución de salida: para eso está el escalador |
| **Resolution Percentage** | Sin tocar si usas escalador |
| **Vertical Sync** | Off: mete latencia. Se sustituye por un límite de FPS |
| **Max Foreground FPS** | Limitado, ver bloque. Evita *tearing* y picos térmicos |
| **Max Background FPS** | Bajo: menos consumo al hacer Alt-Tab a Discord |
| **Limit Cutscene FPS** | On. Cero impacto jugable |
| **NVIDIA Reflex Low Latency** | Activado + Boost. Baja la latencia real de entrada |
| **Sharpen Image** | A ojo ⚠️ las fuentes dan valores incompatibles |

::: evidencia nivel=disputa fuentes=switchblade-settings,charlieintel-settings,dexerto-settings,finalboss-settings
**Límite de FPS:** con G-Sync o FreeSync, capar 3-5 FPS por debajo del refresco del monitor; sin ellos, al refresco exacto. Las cifras publicadas van de 400 (Charlie INTEL) a 200 (UnGeek) a "igual al refresco" (Switchblade): no hay consenso, y el valor absoluto importa menos que el hecho de capar. **Max Background FPS:** 30. **Sharpen Image:** 90 frente a 6 en dos fuentes, escalas incompatibles.
:::

::: evidencia nivel=unica fuentes=kotaku-settings
El contador de FPS nativo se abre con `Ctrl + R` en partida ✅: medir sin instalar overlays. Dato de 2023, no recontrastado en 3.1.x.
:::

## Calidad gráfica, ajuste por ajuste ✅

::: evidencia nivel=unica fuentes=switchblade-settings
Ranking de coste en rendimiento, de mayor a menor: **Shadow Quality → Ray Tracing → Fog Quality → SSAO Quality → Geometric Complexity → Particle Quality → Screen Space Reflections**. Shadow Quality se describe como el ajuste con mayor coste unitario del juego. ⚠️ Esta fuente se fecha en mayo de 2026 pero declara cubrir la Temporada 8: incoherencia interna reconocida.
:::

| Ajuste | Perfil de empuje |
|---|---|
| **Texture Quality** | Alta, o media con poca VRAM |
| **Anisotropic Filtering** | Máximo (es prácticamente gratis) |
| **Shadow Quality** | **Media** — el primero que hay que bajar |
| **Dynamic Shadows** | On (Off solo en equipos muy justos) |
| **Soft Shadows** | **Off** ⚠️ sin consenso entre fuentes |
| **Shader Quality** | Alta — por debajo hay *pop-in* visible |
| **SSAO Quality** y **Fog Quality** | Media o baja |
| **Clutter Quality** | **Baja** — además limpia el suelo de ruido visual |
| **Water Simulation Quality** | Baja ⚠️ sin consenso |
| **Anti-Aliasing Quality** | Alta, u Off si usas escalador ⚠️ sin consenso |
| **Geometric Complexity** | Media |
| **Physics Quality** | **Baja/media si la CPU va justa** |
| **Particle Quality** | Media |
| **Screen Space Reflections** y **Distortion** | **Off** |
| **Low FX** | **On** en contenido denso |
| **Ray Tracing (todos)** | **Off** |

::: evidencia nivel=unica fuentes=switchblade-settings,informe-ajustes-pc
El trazado de rayos completo *"aproximadamente reduce a la mitad"* los FPS: una RTX 3080 que hace ~90 FPS a 4K en Ultra baja a 45-50 FPS, por debajo del objetivo de 60 FPS de Blizzard. Solo RT Shadows tiene coste asumible (15-20 %), y desde una RTX 4080. **Para leaderboard: Off.**
:::

## Escalado y generación de fotogramas ✅

Es la parte más reciente y más rentable del menú, y es toda ✅.

::: evidencia nivel=corroborado fuentes=blizzard-3-1-0,icyveins-dlss4
Escalador por marca de GPU: **Nvidia RTX → DLSS** (modelo transformer, DLSS 4 nativo con Multi Frame Generation desde julio de 2025, sin necesidad de la app de Nvidia; DLSS 5X y 6X añadidos en 3.1.0). **AMD Radeon → FSR 3.1**, modo Quality. **Intel Arc → XeSS 3** ✅ desde 3.1.0, modo Quality.
:::

::: evidencia nivel=unica fuentes=informe-ajustes-pc
Modo de DLSS según la resolución del monitor: a 1080p, **Balanced o Quality** (evita Performance: renderiza internamente a ~720p y se nota); a 1440p, **Quality**; a 4K, **Performance o Balanced**. Síntesis de guías generalistas, no de fuente de élite.
:::

::: evidencia nivel=unica fuentes=informe-ajustes-pc
Cifras de Nvidia con DLSS 4 + Multi Frame Generation a 4K con todo al máximo: RTX 5070 ~190 FPS, 5090 ~370 FPS. DLSS 4.5 añade 6X Dynamic Multi Frame Generation, que ajusta el multiplicador solo.
:::

::: aviso tipo=truco
La generación de fotogramas **inserta fotogramas sintéticos**: sube los FPS que ves sin bajar la latencia de entrada al mismo ritmo. Para farmeo, activadla. Para un intento serio de Pit alto, donde esquivar a tiempo decide si completáis o morís, valorad desactivarla dejando **Reflex + Boost** encendido. ⚠️ Razonamiento técnico, no cita: no hay medición publicada.
:::

## HDR ✅

::: evidencia nivel=unica fuentes=evezone-hdr
El HDR sufre un "filtro gris" documentado: los negros no están calibrados para todas las pantallas. Tres controles en Gráficos — **HDR Brightness**, **Black Point** (viene demasiado alto: bajadlo) y **White Point**. Si se ve raro en partida, `Win + Alt + B` reinicia el perfil de color entre Windows y el juego. Fuente única de febrero de 2026.
:::

Si el monitor no es OLED o mini-LED con buen brillo pico, **HDR en Off**: mal calibrado destruye la lectura de sombras, que es lo que necesitáis en el Pit.

## Nigromante: la pantalla llena de esbirros ✅

Aquí es donde vuestra clase os cobra el peaje que ninguna guía de ajustes menciona.

::: evidencia nivel=corroborado fuentes=datafile-3-1-0,maxroll-skill-trees
El ejército crece a partir del nivel 15, y las variantes que lo hacen crecer son ✅ juego base: ***Coven*** (+2 magos esqueléticos) a nivel 15, ***Master of Puppets*** (+3 guerreros) a nivel 16, ***Gravebloom*** (3 gólems) a nivel 20. Verificado en el fichero de datos del juego, versión 3.1.0.72698.
:::

::: evidencia nivel=sinconfirmar fuentes=informe-ajustes-pc
**No existe ni un solo benchmark que mida el coste en FPS de los esbirros del Nigromante en la Temporada 14.** Ninguna guía consultada lo aborda con números. Todo lo que sigue es razonamiento sobre hechos documentados, no medición.
:::

Los hechos: **Low FX** reduce los sistemas de partículas renderizados; **Physics Quality** es coste de CPU y cada esbirro es una entidad más que simular; **Particle Quality** gobierna la densidad de partículas, y Explosión de Cadáveres (*Corpse Explosion*) las genera a espuertas; **Display Minion Health Bars** dibuja una barra por esbirro.

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
La única enumeración completa del menú de Jugabilidad que existe por escrito es antigua y de fuente vetada aquí. Los nombres clave sí se citan en fuentes recientes, pero **la estructura de pestañas del parche vivo no está verificada**: algunos ajustes aparecen unas veces en Jugabilidad y otras en Accesibilidad. Buscadlos en las dos.
:::

| Ajuste | Valor | Por qué |
|---|---|---|
| **Advanced Tooltip Information** | **ON** | Muestra el rango de cada afijo y si un modificador es aditivo o multiplicativo. Sin esto no se puede min-maxear, y además **el filtro de botín parsea mal** |
| **Advanced Tooltip Compare** | **ON** | Al comparar, muestra lo ganado, lo perdido y el efecto sobre las habilidades |
| **Show All Damage Numbers** | ON al aprender · **OFF en Pit alto** | Os enseña qué habilidad pega de verdad; con el ejército montado tapa el suelo de cifras |
| **Show Items on Ground Behavior** | **Toggle** | Etiquetas fijas, sin mantener pulsado |
| **Item Label Duration on Drop** | Al máximo | |
| **Display Minion Health Bars** | ON aprendiendo · OFF en denso | Os avisa de que se os mueren los esqueletos, a cambio de decenas de barras encima |
| **Monster Health Bar Option** | **Always On** | Si tú no matas directamente, es la única forma de saber si el DPS de los esbirros basta |
| **Display Own Health / Resource** | ON | La Esencia (*Essence*) es vuestro limitador |
| **Display Player Highlight** | ON | |
| **Highlight Player When Obscured** | **ON** | Te contornea cuando algo te tapa. Con dos nigromantes, obligatorio |
| **Player Highlight Color** | Que no lo use el Nigromante | Nada de morado, verde veneno ni gris hueso. Naranja o cian |
| **Screen Shake Effects** | Off | Menos mareo, más precisión al esquivar |
| **Combat Hit Flash** | Off en Pit alto | Con el ejército pegando, la pantalla no para de parpadear |
| **HUD Configuration** | Probad las dos | Esquina libera centro de pantalla |

::: aviso tipo=truco
Sois dos nigromantes: **elegid colores de resaltado distintos entre vosotros**. En una nube de Explosión de Cadáveres es la diferencia entre saber quién eres tú y jugar a ciegas.
:::

::: aviso tipo=peligro
El atajo de **Show Item Labels** viene por defecto en `Alt`. Rebindeadlo. Si hablas por Discord con tu pareja y haces Alt-Tab, la tecla se queda pegada y el juego se comporta de forma errática. Ponedlo en `Tab` o en un botón lateral del ratón.
:::

## Filtro de botín (Loot Filter) ✅

::: evidencia nivel=oficial fuentes=blizzard-loh-web,icyveins-loot-filter,refutacion-comunidad-arbol
El filtro de botín es **✅ juego base**. La web oficial de Blizzard lo anuncia bajo el epígrafe *"Major Updates for all Diablo IV Players"*: *"a new Loot Filter will ease the discovery of desired items across Sanctuary"*. La verificación adversarial lo confirma: *"free universal update available to every Diablo 4 player regardless of expansion ownership"*. ⚠️ **Maxroll es el único disidente** y escribe que requiere *Lord of Hatred*: va contra la fuente primaria.
:::

::: paso n=1 obligatorio=si entitlement=base
Abrid **Opciones → Jugabilidad** y comprobad si aparece la entrada del filtro de botín. Cierra la única contradicción relevante de este capítulo. Activad también **"Enable Loot Filter shortcut on Game Menu"** y dadle atajo propio en Controles.
:::

Las reglas se evalúan **de arriba abajo** y la de más arriba manda. Podéis guardar varios filtros pero solo uno está activo. Cada regla puede **mostrar, recolorear, ocultar la etiqueta u ocultarlo todo**. No tocan las tasas de drop, solo la presentación — pero **lo oculto no se puede recoger**.

::: evidencia nivel=disputa fuentes=informe-ajustes-pc,informe-herramientas,d4lootfilter-viewer
Límite de reglas por filtro: **25** según unas fuentes, **30** según d4lootfilter.com. Sin resolver. Presupuestad 25 y no os quedaréis cortos por sorpresa.
:::

Condiciones: poder del objeto, rareza, tipo, propiedades, Afijo Superior (*Greater Affix*), afijos requeridos y opcionales, mejora de Códice y único concreto. Hay además una condición de **bonus de conjunto de Talismán 🔒 Lord of Hatred**: existe en el menú, pero sin ese sistema no os sirve. Ignoradla; el resto funciona igual ✅.

::: evidencia nivel=corroborado fuentes=maxroll-loot-filter,d4lootfilter-viewer
**Importar y exportar códigos de filtro solo funciona en PC.** Es limitación de plataforma, no de expansión: en PS5 se pueden crear y editar reglas a mano, pero no pegar un código. ⚠️ D4 Filter Forge afirma en cambio que el formato viaja con la cuenta de Battle.net; nadie lo confirma.
:::

::: paso n=2 obligatorio=no entitlement=base
Plan para el dúo: el de PC importa un filtro preconstruido pegando el código y comprobáis si aparece en la cuenta del de PS5. Si no aparece — lo más probable —, el de PS5 abre **d4lootfilter.com** en el móvil, pega ahí el mismo código, la web se lo descompone en reglas legibles y las teclea a mano. Media hora una vez por temporada, y los dos veis lo mismo en pantalla.
:::

No empecéis con un filtro estricto: mientras subís nivel necesitáis ver legendarios para extraer aspectos al Códice. Escalad de suave a estricto conforme subáis de Tormento.

Y el hermano pobre del filtro, en el menú de Sonido ✅: el **sonido de drop por rareza** se puede filtrar. Ponedlo en legendario o superior, y **el mismo umbral en las dos máquinas** — así, cuando uno diga "ha sonado algo bueno", el otro sabe de qué habla. ⚠️ El nombre del ajuste difiere entre fuentes.

## Accesibilidad ✅ — no es "para otros", es rendimiento

| Ajuste | Recomendación |
|---|---|
| **Cursor Size** y **High Contrast Cursor** | Grande y en alto contraste. Perder el cursor en una nube de Explosión de Cadáveres es una muerte |
| **HUD Font Scaling** | Subidlo |
| **Colorblind Filter** | Probadlo aunque no seáis daltónicos: cambia la paleta y puede separar los efectos del fondo |
| **Character Visibility** | Probadlo ⚠️ nombre documentado hace dos años, sin confirmar en el parche vivo |
| **Reduce Strobing** | ON si hay fotosensibilidad |

## Keybinds ✅ — la sección que más va a subir vuestro nivel

Si de todo este capítulo solo hacéis una cosa, que sea esta.

::: evidencia nivel=corroborado fuentes=iggm-keybinds,kotaku-settings
En **Opciones → Controles → Key Bindings**, el ajuste **"Combine Move/Interact/Basic Skill Slot"** viene activado por defecto: el clic izquierdo mueve, interactúa y lanza la básica a la vez. Consecuencia documentada: si clicas sin querer sobre un enemigo le atacas, y te quedas clavado cuando querías reposicionarte. **Desactivadlo** y asignad **Move & Interact** al clic izquierdo y la básica a otra tecla.
:::

Las dos funciones que separan a un jugador de otro:

- **Force Move** (movimiento forzado): mantienes la tecla y corres hacia el cursor **sin atacar ni interactuar con nada**. Se suele poner en la rueda del ratón, desactivando antes el zoom con rueda.
- **Hold Position / Stand Still**: atacas sin moverte del sitio. Por defecto, `Shift`.

**Por qué es crítico justo para vosotros:** las maldiciones y Explosión de Cadáveres se lanzan sobre el suelo, y esa nube negra tapa jugadores, botín, monstruos, efectos y cofres — queja documentada en los foros oficiales. Dentro de la nube, si no puedes moverte sin atacar ni atacar sin moverte, juegas a ciegas.

::: evidencia nivel=sinconfirmar fuentes=informe-ajustes-pc
Esquema sugerido. **No es la configuración canónica de ningún jugador top**: los vídeos de rob2628 y wudijo existen pero no se pudo extraer su contenido, y ninguna fuente escrita de élite publica un esquema para esta temporada. Síntesis de guías generalistas: Move & Interact en clic izquierdo · fundamental en clic derecho · básica en `Q` o botón lateral · resto de ranuras en `1 2 3 4` · Force Move en la rueda · Hold Position en `Shift` · Evadir en `Espacio` · poción en botón lateral · montura en `Z` · portal en `T` · Show Item Labels fuera de `Alt` · filtro de botín con atajo propio.
:::

La regla de oro sí es sólida: **lo reactivo** (evadir, poción, defensiva) va donde el dedo ya está; **lo proactivo** (invocar, buffs) puede ir lejos. Y las ranuras de la barra están abiertas ✅ desde el primer momento: dejad el mapeado hecho ya y no lo toquéis más.

::: evidencia nivel=disputa fuentes=kotaku-settings,informe-ajustes-consola
**En el mando la recomendación se invierte, o no.** Sobre el equivalente "Combine Interact and Basic Skill" hay dos posturas: dejarlo **combinado**, porque el mando tiene menos botones y separar cuesta más de lo que aporta; o ponerlo en **OFF**, calificado de crítico precisamente para Nigromante, para que Interactuar tenga botón propio. El informe dedicado a consola es el más específico y dice OFF. Que tu pareja lo pruebe en las dos.
:::

## Fuera del juego ✅

::: evidencia nivel=unica fuentes=switchblade-settings
**HAGS** (planificación de GPU por hardware) activado, plan de energía en alto rendimiento, Modo Juego en On, Integridad de Memoria desactivada si se puede, Battle.net cerrándose al arrancar, drivers al día (obligatorio para DLSS 5X/6X y XeSS 3) y SSD — en disco mecánico las transiciones de zona son un suplicio.
:::

::: aviso tipo=peligro
Sobre overlays de terceros (Diablo4Companion, d4lf, Overwolf): la EULA prohíbe el software no autorizado expresamente, no hay lista blanca ni proceso de aprobación, y **no existe ninguna declaración de Blizzard posterior a las expansiones** que actualice esa política. Con el filtro de botín ya dentro del juego, el beneficio marginal no compensa el riesgo — y en dúo, si uno pierde la cuenta se acabó el proyecto para los dos.
:::

## Lo que este capítulo no sabe

Un hueco declarado vale más que un número con buena pinta:

- **Coste real en FPS de los esbirros**: cero benchmarks. La receta es razonamiento, no medición.
- **Auto-recogida de oro, transparencia del chat y marcadores de área de habilidad**: ninguna fuente documenta esos interruptores. No se afirma que no existan; se afirma que no se han visto.
- **Estructura del menú hoy**: la única enumeración completa que existe es antigua y de fuente vetada.
- **Sincronización de ajustes entre PC y PS5**: sin fuente. Asumid que no y configurad cada máquina aparte.
