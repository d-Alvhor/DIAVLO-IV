# Ajustes óptimos de Diablo IV en PC — Season 14 "Death Awakening" / parche 3.1.3

> **Fecha de la investigación:** 18 de agosto de 2026
> **Estado del juego:** Season 14 "Season of Death Awakening" (viva desde el 30/06/2026). Parche vivo **3.1.3** (build 73224, 12/08/2026). La PTR 3.2.0 de la Season 15 corrió del 4 al 11 de agosto de 2026.
> **Perfil del jugador:** principiante absoluto, **Nigromante (Necromancer)**, **SOLO JUEGO BASE** (sin *Vessel of Hatred*, sin *Lord of Hatred*), en **dúo** con su pareja (también nigromante), uno en **PC** y otro en **consola** (cross-play). Objetivo: min-max nivel leaderboard.
>
> **Leyenda:** ✅ = funciona con el juego base · 🔒 = requiere expansión (o el contenido concreto la requiere)

---

## 0. Resumen ejecutivo (lo que hay que hacer hoy)

**La noticia buena para vosotros:** prácticamente **todo el dominio de "ajustes" es juego base** ✅. El menú de opciones (Gráficos, Jugabilidad, Sonido, Controles, Accesibilidad) no está detrás de ninguna compra, y las dos mejoras técnicas más recientes —**soporte XeSS 3 para GPU Intel** y **soporte DLSS 5X y 6X para GPU Nvidia**, ambos añadidos en el parche **3.1.0** del 30 de junio de 2026— aparecen en la sección **"Base Game"** de las notas oficiales. Es decir: ✅.

**El filtro de botín (Loot Filter) también es juego base** ✅, aunque se estrenara *junto con* la expansión *Lord of Hatred*. Esto es exactamente el tipo de dato donde las fuentes se contradicen y lo detallo en la sección 7 y en "Contradicciones".

**Los cuatro ajustes que más os van a cambiar la vida, por orden:**
1. **Advanced Tooltip Information** + **Advanced Tooltip Compare** en ON ✅ (sin el primero, el filtro de botín parsea mal).
2. **Desactivar "Combine Move/Interact/Basic Skill Slot"** ✅ y montar **Force Move** + **Hold Position**. Esto es lo que separa a un jugador que "clica bien" de uno que no.
3. **Loot Filter** ✅ configurado desde el día 1 (y ojo: el de consola se monta a mano, ver 7.4).
4. **Low FX / Particle Quality / Clutter Quality** ✅ para sobrevivir a las peleas con esbirros y Corpse Explosion en Pit alto.

---

## 1. Vigencia: qué he podido fechar y qué no

Esto es importante porque **la mayoría de guías de "mejores ajustes" que circulan son de 2023-2025** y las estoy usando solo donde el sistema no ha cambiado.

| Fuente | Fecha | Temporada/parche que cubre | Uso que le doy |
|---|---|---|---|
| Notas oficiales Blizzard (news.blizzard.com) | 12/08/2026 | 3.1.3, 3.1.2, 3.1.1, 3.1.0 | **Fuente primaria**, vigente |
| Maxroll — notas 3.1.0 | 24/06/2026 | 3.1.0 / S14 | Vigente |
| Maxroll — Loot Filter | 21/07/2026 | S14 | Vigente |
| Skycoach — best settings | 23/07/2026 | S14 | Vigente (calidad media) |
| FinalBoss.io — best settings | act. 12/08/2026 | 3.1.3 / S14 | Vigente (calidad media) |
| Switchblade Gaming — best settings | 26/05/2026 | **se declara S8 / 2.2.0** ⚠️ | Útil por el detalle técnico, **fecha y parche incoherentes** |
| PCGamesN | 18/08/2025 | pre-S14 | Solo donde el sistema no ha cambiado |
| Icy Veins — DLSS 4 nativo | sin fecha en la página | S8 aprox. | Contexto histórico |
| Kotaku — 11 ajustes esenciales | 06/06/2023 | lanzamiento | **Antiguo**, pero los nombres de opciones siguen siendo los mismos |
| Mythic Drop — gameplay settings | 15/04/2023 | lanzamiento | **Antiguo**; es la única enumeración completa del menú Jugabilidad que he encontrado |
| Game8 — ajustes de consola | 14/06/2023 | lanzamiento | **Antiguo** |
| Foros Blizzard — "Character Visibility" | 15/05/2024 | S4 | **Antiguo**, marcar |
| EveZone — HDR | 09/02/2026 | 2026 | Reciente, **fuente única** |
| Fextralife wiki — Loot Filters | menciona parches 3.0.1a / 3.0.2 | 3.0.x | Vigente-ish |

**No he encontrado** una guía dedicada de "mejores ajustes" en **Maxroll**, **Icy Veins** ni **Mobalytics** para la S14. Eso significa que **no hay fuente de élite** fechada en agosto de 2026 para los keybinds competitivos: lo que doy en la sección 9 viene de guías generalistas y de referencias a vídeos de rob2628/wudijo que **no he podido abrir** (contenido en vídeo).

---

## 2. Menú Gráficos — pantalla y sincronización ✅

Todo este bloque es **juego base** ✅.

| Ajuste (nombre en inglés) | Recomendación | Por qué |
|---|---|---|
| **Display Mode** | **Windowed Fullscreen** (ventana sin bordes) | Switchblade: "iguala el rendimiento de fullscreen exclusivo y evita la inestabilidad al hacer Alt-Tab". Charlie INTEL y Dexerto también lo recomiendan. ⚠️ 1v9 y FinalBoss recomiendan **Fullscreen exclusivo** (ver contradicciones) |
| **Resolution** | Nativa del monitor | Nunca bajes la resolución de salida: baja el *Resolution Percentage* o usa upscaler |
| **Resolution Percentage** | **100%** | Con DLSS/FSR/XeSS activos, el escalado ya lo hace el upscaler. FinalBoss sugiere 80% solo como truco competitivo extremo |
| **Vertical Sync** | **Off** | Introduce latencia de entrada. Se sustituye por un límite de FPS |
| **Max Foreground FPS** | Cap **3-5 FPS por debajo del refresco** del monitor si tienes G-Sync/FreeSync; si no, el refresco exacto | Evita tearing y picos térmicos. Las fuentes dan valores muy dispares: 400 (Charlie INTEL), 200 (UnGeek), "igual al refresco" (Switchblade) |
| **Max Background FPS** | **30** | Baja consumo al hacer Alt-Tab. Muy útil si el de PC tiene Discord/navegador abierto para hablar con la pareja |
| **Limit Cutscene FPS** | **On** (30 FPS) | Da respiro a la GPU en cinemáticas. Cero impacto jugable |
| **NVIDIA Reflex Low Latency** | **Enabled + Boost** | Reduce latencia de entrada. Requiere GPU Nvidia serie 900 o superior. **Se activa solo si habilitas Frame Generation** |
| **Sharpen Image** | ⚠️ Sin consenso | Charlie INTEL dice **90**, Dexerto dice **6**. Escalas incompatibles entre sí; ajústalo a ojo |
| **HDR** | Ver sección 5 | |

**Contador de FPS in-game:** `Ctrl + R` durante la partida ✅ (Kotaku). Es la forma nativa de medir sin overlays.

---

## 3. Menú Gráficos — calidad, ajuste por ajuste ✅

Ranking de coste de rendimiento (de mayor a menor) según Switchblade Gaming:

**Shadow Quality → Ray Tracing → Fog Quality → SSAO Quality → Geometric Complexity → Particle Quality → Screen Space Reflections**

| Ajuste | Qué hace | Coste | Recomendación **calidad** | Recomendación **FPS / Pit alto** |
|---|---|---|---|---|
| **Texture Quality** | Detalle de texturas de entorno y personajes | Ligado a VRAM, coste de cómputo casi nulo | High | **Medium si tienes ≤8 GB de VRAM** |
| **Anisotropic Filtering** | Nitidez de texturas en ángulo (el suelo) | Casi nulo | **16x** | 16x (déjalo, es gratis) |
| **Shadow Quality** | Resolución de sombras | **El coste unitario más alto del juego** | High/Highest | **Medium** — es el primer ajuste que hay que bajar |
| **Dynamic Shadows** | Sombras proyectadas por objetos móviles | Medio | On | On (Off solo en equipos muy justos) |
| **Soft Shadows** | Filtrado PCF de bordes de sombra | Alto para lo poco que aporta | On | **Off** |
| **Shader Quality** | Calidad de shaders | Medio | High | **High** — en Low/Medium hay *pop-in* de shaders visible |
| **SSAO Quality** | Oclusión ambiental (sombreado de contacto) | Alto | High | **Medium o Low**. En D4 el efecto es sutil |
| **Fog Quality** | Niebla volumétrica | Alto | High | **Medium o Low** |
| **Clutter Quality** | Escombros y detalle de suelo | Bajo-medio | Medium/High | **Low** — además **reduce ruido visual** en el suelo |
| **Fur Quality** | Pelaje | Bajo-medio | Medium/High | **Medium** |
| **Water Simulation Quality** | Simulación de agua | Medio | High | **Low** — apenas se ve en mazmorras |
| **Anti-Aliasing Quality** | Suavizado de bordes (TAA) | Bajo-medio | High | **High**, o **Off si usas DLSS/FSR/XeSS** (el upscaler ya hace AA) |
| **Geometric Complexity** | Teselado / densidad geométrica | Medio (~5-8% de GPU) | High | **Medium** |
| **Terrain Geometry Detail** | Detalle del terreno | Medio | High | Medium/High |
| **Physics Quality** | Física de ragdolls y objetos | **Coste de CPU** | High | **Low/Medium si tu CPU va justa** — relevante con muchos esbirros |
| **Particle Quality** | Densidad de partículas de hechizos | Medio | High | **Medium**. Switchblade avisa: las peleas de jefe se ven raras en Low |
| **Reflection Quality** | Calidad de reflejos | Medio | High | Medium |
| **Screen Space Reflections** | Reflejos en espacio de pantalla | **Alto en mazmorras, poco beneficio** | On | **Off** |
| **Distortion** | Distorsión de pantalla (ondas de calor, efectos) | Bajo | On | **Off** si buscas claridad en Pit (ver 11) |
| **Low FX** | "Reduce el número de sistemas de partículas renderizados" | Ahorro grande | Off | **On** — el interruptor de emergencia para nigromante (ver 10) |

### 3.1 Ray Tracing ✅

Ajustes: **Ray Traced Shadows Quality**, **Ray Traced Reflections Quality**, **Ray Traced Foliage**, **Ray Traced Particles**.

- **Recomendación general: Off.** El ray tracing "aproximadamente reduce a la mitad" los FPS. Una RTX 3080 que hace ~90 FPS a 4K Ultra baja a **45-50 FPS** con RT completo — por debajo del objetivo de 60 FPS de la propia Blizzard.
- Solo **RT Shadows** si tienes RTX 4080 o superior (coste 15-20%).
- **RT completo** solo en RTX 50 con DLSS 4 Multi Frame Generation.
- Para min-max de leaderboard: **Off, sin discusión**. Los FPS estables valen más que los reflejos.

---

## 4. Upscaling y Frame Generation ✅ — lo más actualizado del parche 3.1.0

Esta es **la parte más importante y más reciente** del dominio, y es **juego base** ✅.

Notas oficiales del parche **3.1.0** (30/06/2026), sección **Base Game**:
- *"Added XESS 3 support for Intel GPUs."*
- *"Added DLSS 5X and 6X support for Nvidia GPUs."*

Histórico previo: en julio de 2025 (Season 8) el juego recibió **DLSS 4 nativo con Multi Frame Generation**, sin necesidad de la app de Nvidia.

### 4.1 Qué upscaler usar

| GPU | Upscaler | Modo recomendado |
|---|---|---|
| **Nvidia RTX** | **DLSS** (modelo transformer, DLSS 4/4.5) | Ver tabla por resolución |
| **AMD Radeon** | **FSR** (3.1) | Quality |
| **Intel Arc** | **XeSS** (ahora **XeSS 3** ✅ desde 3.1.0) | Quality |

### 4.2 Modo de DLSS por resolución

| Resolución de pantalla | Modo DLSS | Nota |
|---|---|---|
| 1080p | **Balanced o Quality** | Evita Performance: renderiza internamente a ~720p y se nota |
| 1440p | **Quality** | Interno ~960p, escalado nítido |
| 4K | **Performance o Balanced** | Claridad aceptable con ganancia enorme |

### 4.3 Frame Generation — el matiz que importa para el leaderboard

- **Rendimiento bruto:** con DLSS 4 + Multi Frame Generation, Nvidia declara multiplicar los FPS **una media de 6,5x a 4K** con RT y todo al máximo. Cifras publicadas: RTX 5070 ~190 FPS, 5070 Ti ~230, 5080 ~270, **5090 ~370 FPS**. A 1440p maxeado se han medido hasta 445 FPS; a 1080p Ultra, ~500 FPS en 5090.
- **DLSS 4.5** (anunciado en CES 2026) trae modelo transformer de 2ª generación y **6X Dynamic Multi Frame Generation** que ajusta el multiplicador automáticamente.
- **Pero:** Frame Generation **inserta fotogramas generados por IA**, lo que sube los FPS mostrados sin bajar la latencia real de entrada al mismo ritmo. Para **empujar Pit alto**, donde esquivar a tiempo es la diferencia entre completar y morir, la recomendación defendible es: **activar Frame Generation para contenido de farmeo cómodo y valorar desactivarla en los intentos serios de leaderboard**, dejando **Reflex + Boost activo**. ⚠️ *Este último matiz es razonamiento mío a partir de cómo funciona la tecnología, no una cita de ninguna guía de D4 que haya abierto.*

---

## 5. HDR ✅

Fuente única (EveZone, 09/02/2026) — **fiabilidad media, no he podido contrastarla**.

El problema documentado es el **"filtro gris"**: el HDR de D4 se ve lavado porque *"los niveles de negro no están bien calibrados para todas las pantallas"*.

Tres controles en el menú de Gráficos:
1. **HDR Brightness** — luminancia pico general.
2. **Black Point** — *"viene demasiado alto por defecto"*; **bájalo** para eliminar el velo gris y recuperar la profundidad de las sombras.
3. **White Point** — controla el recorte de altas luces.

**Truco de sistema:** si el HDR se ve raro, pulsa **Win + Alt + B** en juego para reiniciar el "handshake" de perfil de color entre Windows y el juego.

**Método de validación:** ajusta en una zona oscura hasta que se distinga detalle en las sombras sin perder el brillo de los hechizos.

**Mi recomendación práctica para vosotros:** si el monitor no es OLED o mini-LED con buen brillo pico, **HDR en Off** y ganáis consistencia visual. El HDR mal calibrado empeora la lectura de la pantalla en Pit, que es justo lo contrario de lo que buscáis.

---

## 6. Menú Jugabilidad (Gameplay) — el oro que casi nadie toca ✅

⚠️ **Aviso de vigencia:** la enumeración completa del menú Jugabilidad que he encontrado es de **abril de 2023** (Mythic Drop). Los nombres siguen apareciendo en fuentes de 2026 (Advanced Tooltip, Display Minion Health Bars, HUD Configuration…), pero **no puedo garantizar que el menú no se haya reorganizado en 3.x** ni que no se hayan añadido opciones que ninguna fuente escrita documente.

Todo esto es **juego base** ✅.

### 6.1 Los imprescindibles

| Ajuste | Valor | Por qué es crítico |
|---|---|---|
| **Advanced Tooltip Information** | **ON** | Muestra el **rango de valores** de cada afijo, la Lucky Hit Chance y si un modificador es **aditivo o multiplicativo**. Sin esto no puedes min-maxear: no sabes si un afijo rolló alto o bajo. **Además, Maxroll advierte de que sin esta opción el parseo del filtro de botín es muy inconsistente** |
| **Advanced Tooltip Compare** | **ON** | Al comparar dos objetos muestra propiedades ganadas, perdidas y cambios en las habilidades equipadas |
| **Show All Damage Numbers** | **ON al aprender / OFF en Pit alto** | ON muestra *todo* el daño; OFF muestra solo golpes especiales (críticos). Como principiante te enseña qué habilidad pega de verdad; en Pit 100+ con esbirros es una tormenta de números que tapa el suelo |
| **Show All Tutorials** | ON al principio | Sois principiantes absolutos. Se apaga cuando dejen de aportar |

### 6.2 Etiquetas de objetos en el suelo

| Ajuste | Valor | Notas |
|---|---|---|
| **Show Items on Ground Behavior** | **Toggle** | Tres modos: *Push to show* (mantener pulsado), *Toggle* (conmutar), *display de 10 segundos*. Con **Toggle** las etiquetas se quedan fijas: es el equivalente a "always show item labels" |
| **Item Label Duration on Drop** | Slider 0-10 → **al máximo** | Cuánto tiempo permanece la etiqueta tras caer el objeto |
| **Show Item Labels** (tecla) | Por defecto **Alt** | ⚠️ **Rebindéalo**. Alt es la tecla que se usa para Alt-Tab; si hablas con tu pareja por Discord y sales del juego, se queda pegada. Kotaku lo señala explícitamente |

### 6.3 Comportamiento de habilidades y posición

| Ajuste | Opciones | Recomendación |
|---|---|---|
| **Skill Toggle Behavior** | *Hold All* / *Toggle Sustained Skills* / *Toggle All* | **Toggle Sustained Skills** para canalizadas: menos desgaste de dedo en sesiones largas |
| **Hold Position Mode** | *Hold* / *Toggle* | **Hold** (mantener) es lo estándar; *Toggle* si te cansa mantener |
| **Action Wheel Activation** | *Hold* / *Toggle* | Preferencia personal |
| **HUD Configuration** | *Centered* / *Left Corner* | **Left Corner** libera espacio central de pantalla (Kotaku). Centered es más fácil de leer de reojo para un principiante — probad ambas |

### 6.4 Barras de vida (crítico para nigromante)

| Ajuste | Valor | Por qué |
|---|---|---|
| **Display Minion Health Bars** | ⚠️ **Decisión de compromiso** | ON te dice cuándo se te están muriendo los esqueletos (información táctica real en un build de esbirros). OFF elimina **decenas de barras** superpuestas en pantalla. **Mi recomendación: ON mientras aprendéis el build, OFF cuando entréis en Pit alto** |
| **Monster Health Bar Option** | *Hover only* / **Always On** / *Always Off* | **Always On**: en un build de nigromante donde tú no matas directamente, ver la vida de los élites es la única forma de saber si el DPS de los esbirros basta |
| **Display Own Health / Display Own Resource** | **ON** | La Esencia (Essence) del nigromante es tu limitador; hay que verla siempre |

### 6.5 Resaltados (Highlights) — infravalorado

| Ajuste | Valor |
|---|---|
| **Display Player Highlight** | **ON** |
| **Highlight Player When Obscured** | **ON** — dibuja un contorno alrededor de tu personaje cuando algo lo tapa. Con dos nigromantes y ~10 esbirros en pantalla, **esto es obligatorio** |
| **Player Highlight Color** | Un color que **NO** aparezca en los efectos de nigromante (evita morados, verdes venenosos y grises hueso). Naranja o cian funcionan |
| **NPC / Enemy / Object Highlight Color** | Colores distintos entre sí y del tuyo |

**Truco de dúo:** si los dos jugáis nigromante, **elegid colores de resaltado distintos** entre vosotros para no confundir quién es quién en una nube de Corpse Explosion.

### 6.6 Efectos que conviene apagar

| Ajuste | Valor | Motivo |
|---|---|---|
| **Screen Shake Effects** | **Off** | Menos mareo, más precisión al esquivar |
| **Combat Hit Flash** | **Off** en Pit alto | El flash al golpear satura la pantalla con muchos esbirros pegando a la vez |
| **Reduce Strobing** | **On** si hay sensibilidad; opcional si no | Desactiva efectos de iluminación que causan estroboscopia |

---

## 7. Filtro de botín (Loot Filter) ✅ — juego base, confirmado

### 7.1 Disponibilidad — aquí hay contradicción entre fuentes

- **Maxroll** (21/07/2026) escribe que el filtro *"por fin se ha lanzado con la expansión Lord of Hatred"* — redacción ambigua que se lee fácilmente como "requiere la expansión".
- **Icy Veins** afirma explícitamente: *"disponible para todos los jugadores, independientemente de si poseen la expansión"*.
- **Fextralife wiki** lo confirma: *"forman parte del juego base y no requieren la propiedad de la expansión Lord of Hatred, pese a haberse introducido con ella"*.

**Conclusión: ✅ JUEGO BASE.** Se estrenó *junto a* la expansión como actualización universal gratuita (parche 3.0).

### 7.2 Cómo se accede ✅

```
Menú principal → Opciones → Jugabilidad (Gameplay) → "Open Loot Filter"
```
Y para tenerlo a mano:
```
Opciones → Jugabilidad → "Enable Loot Filter shortcut on Game Menu"
```
También se le puede asignar un **keybind** en Controles ✅.

**Requisito previo obligatorio:** **Advanced Tooltip Information en ON**, o el parseo será inconsistente (Maxroll).

### 7.3 Cómo funciona

- **Reglas evaluadas de arriba abajo**; la de más arriba manda.
- Puedes tener **varios filtros creados**, pero **solo uno activo** a la vez.
- Acciones por regla: **Show**, **Recolor** (con selector de color), **Hide Text Label**, **Hide All**.
- **Los filtros NO afectan a las tasas de drop**, solo a cómo se muestran los objetos. **Los objetos ocultos no se pueden recoger.**
- Los filtros se pueden **editar, duplicar o desactivar** sin borrarlos.

**Condiciones disponibles** (Maxroll + Fextralife):
Item Power Range · Item Rarity Match · Item Type Match · Item Properties · Greater Affix Check · Required Affixes · Has Optional Affixes · Codex Upgrade Check · Is Specific Unique · **Talisman Set Bonus** ⚠️

⚠️ **Talisman Set Bonus**: no he podido confirmar si los Talismanes son contenido de expansión. Las notas del parche 3.1.1 listan **Charms** y **Seals** bajo la sección **"War Plans"**, separada de "Base Game", lo que sugiere que parte de este ecosistema es 🔒. **Si esa condición existe pero no tenéis el sistema, simplemente no la useis: el resto del filtro funciona igual** ✅.

### 7.4 PC vs consola — CRÍTICO para vuestro dúo

| | PC ✅ | Consola ✅ |
|---|---|---|
| Importar código de filtro | **Sí**, pegando el código | **NO.** *"La función de importar/exportar filtros está disponible solo en PC"* |
| Montar el filtro | Automático desde código | **Manual, regla a regla** |
| Reglas máximas | ⚠️ 25 (Fextralife) o 30 (d4lootfilter.com) — **fuentes en conflicto** | Igual que PC |

**Plan concreto para vosotros:** el de PC importa un filtro de Maxroll con el código; el de consola usa el visor web **d4lootfilter.com** para decodificar ese mismo código y **replicar las reglas a mano** desde `Opciones → Jugabilidad → Loot Filter`. Así los dos veis lo mismo en pantalla, que en dúo importa muchísimo.

### 7.5 Filtros preconstruidos de Maxroll ✅

| Filtro | Cuándo | Qué oculta |
|---|---|---|
| **Maxroll Light** | Torment 6+ | Comunes y mágicos no ancestrales |
| **Maxroll Medium** | Torment 8+ | Añade raros y legendarios no ancestrales |
| **Maxroll Strict** | Torment 12 | Todo lo que no tenga Greater Affix, y únicos no ancestrales |

**Consejo de principiante:** **no** empecéis en Strict. Mientras subís nivel necesitáis ver legendarios para extraer aspectos al Codex. Escalad Light → Medium → Strict conforme subáis de Torment.

---

## 8. Accesibilidad ✅ — no es "para otros", es rendimiento

Todo juego base ✅.

| Ajuste | Qué hace | Recomendación |
|---|---|---|
| **Character Visibility** | Opción de contraste añadida en la S4. Los jugadores la describen como *"más vívida"* y algunos como *"un poco demasiado brillante"* | **Probadla**. ⚠️ Dato de mayo de 2024: no puedo confirmar que el nombre siga siendo exactamente ese en 3.1.3 |
| **Colorblind Filter** | Protanopia, Deuteranopia, Tritanopia + **slider de intensidad** | Solo si hace falta. **Un filtro de daltonismo puede usarse como herramienta de contraste** aunque no seas daltónico: cambia la paleta y separa efectos de suelo del fondo |
| **HUD Font Scaling** | Slider de tamaño de fuente del HUD | **Súbelo**. Sobre todo si juegas lejos de la pantalla |
| **Subtitles + tamaño y color** | Ajustables | ON |
| **Cursor Size** | Small / Medium / Large | **Large**. Perder el cursor en una nube de Corpse Explosion es una muerte |
| **High Contrast Cursor** | Cursor de alto contraste | **ON** — mismo motivo |
| **Screen Reader / Text to Speech** | Con velocidad y volumen ajustables | Solo si se necesita |
| **Screen Shake Effects** | Desactiva el temblor de pantalla | **Off** (mareo/epilepsia y precisión) |
| **Reduce Strobing** | *"Desactiva varios efectos de iluminación, reduciendo el estroboscopio"* | **On** si hay fotosensibilidad. La documentación avisa de que **puede quedar algún destello en cinemáticas** |
| **Combat Hit Flash** | Destello al golpear | **Off** para fotosensibilidad y para claridad |
| **Brightness** | Slider | 60% o superior según Game8 (dato de 2023, para consola) |

---

## 9. Keybinds — la sección que más va a subir vuestro nivel ✅

### 9.1 El ajuste que lo cambia todo

```
Opciones → Controles → Key Bindings → sección Gameplay
→ "Combine Move/Interact/Basic Skill Slot" → DESACTIVAR
```

Con esta opción **activada** (por defecto), el clic izquierdo hace tres cosas a la vez: moverse, interactuar y lanzar la habilidad básica. Resultado: *"si haces clic sin querer sobre un enemigo, le atacas"* — te quedas clavado atacando cuando querías reposicionarte. Para un nigromante que necesita mantener distancia mientras los esbirros trabajan, eso es letal.

**Con la opción desactivada** puedes asignar por separado:
- **Move & Interact** → clic izquierdo (mover y abrir cofres, sin atacar)
- **Basic Skill** → una tecla o botón de ratón aparte

### 9.2 Force Move y Hold Position

| Función | Qué hace | Recomendación |
|---|---|---|
| **Force Move** | Mantienes la tecla y corres hacia el cursor **sin atacar ni interactuar con nada** | **Bindear obligatoriamente.** Muchos jugadores lo ponen en la **rueda del ratón** (arriba y/o abajo). ⚠️ Antes hay que desactivar el zoom con rueda para liberarla |
| **Hold Position / Stand Still** | Atacas sin moverte del sitio | Por defecto **Shift + clic izquierdo**. Mantener Shift y hacer clic ataca en el sitio, tengas o no habilidad básica asignada al clic |
| **Force Attack** | Ataque forzado | Por defecto **Shift** |

**Por qué esto es crítico para un nigromante:** las curses (Iron Maiden, Decrepify) y Corpse Tendrils/Corpse Explosion se lanzan sobre el suelo, y **Corpse Explosion genera una nube negra que tapa jugadores, botín, monstruos, efectos, objetos de misión y cofres** (queja documentada en los foros oficiales). Si no puedes moverte sin atacar y no puedes atacar sin moverte, dentro de esa nube estás jugando a ciegas.

### 9.3 Esquema de teclado sugerido

⚠️ **No he encontrado una fuente de élite fechada en 2026 con un esquema canónico.** Lo siguiente es una síntesis razonable de las guías generalistas consultadas, no una cita:

| Acción | Bind sugerido |
|---|---|
| Move & Interact | Clic izquierdo |
| Habilidad básica (ej. Reap / Bone Splinters) | Clic derecho o `Q` |
| Habilidad core | Clic derecho |
| Slots 1-4 | `1 2 3 4` |
| Force Move | Rueda del ratón (arriba) |
| Hold Position | `Shift` (mantener) |
| Evade | `Espacio` |
| Poción de curación | `Q` o botón lateral del ratón |
| Montura | `Z` |
| Portal de ciudad | `T` |
| Show Item Labels | **Rebindear fuera de `Alt`** (ej. `Tab` o botón lateral) |
| Loot Filter | Bind propio ✅ |

**Regla de oro:** todo lo que sea **reactivo** (evade, poción, defensiva) va donde el dedo ya está. Todo lo que sea **proactivo** (buffs, invocar) puede ir más lejos.

### 9.4 El otro lado del sofá: mando ✅

Vuestra pareja en consola tiene el equivalente **"Combine Interact & Basic Skill"**. Aquí Kotaku recomienda **dejarlo combinado**, porque el mando tiene menos botones y separar funciones cuesta más de lo que aporta. Es la recomendación contraria a la de PC, y es correcta: son ergonomías distintas.

---

## 10. Nigromante: rendimiento con muchos esbirros ⚠️ (sección con inferencia marcada)

**Aviso de honestidad:** **no he encontrado ni un solo benchmark que mida el coste en FPS de los esbirros del nigromante en la S14.** Ninguna guía consultada aborda esto con números. Lo que sigue combina hechos documentados con razonamiento explícito.

### Hechos documentados
- **Low FX**: *"reduce el número de sistemas de partículas renderizados"*; *"activarlo puede mejorar mucho el rendimiento"*. También reduce calidad de texturas, follaje y efectos de partículas. Descrito como **"buena opción para encuentros pesados"**.
- **Physics Quality** es un ajuste de **CPU**: se recomienda bajarlo con procesadores flojos. Los esbirros son entidades adicionales que la CPU debe simular.
- **Particle Quality** controla la densidad de partículas — Corpse Explosion es un generador masivo de partículas.
- **Display Minion Health Bars** dibuja una barra por cada esbirro invocado.
- Blizzard ya hizo que **las mascotas del nigromante sean casi invisibles para los OTROS jugadores**, específicamente por visibilidad (documentado por Icy Veins). Es decir: **tu pareja no verá tus esqueletos con toda su carga visual**, pero **tú sí verás los tuyos**.

### Receta anti-caída de FPS con esbirros (razonamiento mío sobre esos hechos)
1. **Physics Quality → Low/Medium** (alivia la CPU, que es quien lleva la simulación de decenas de entidades).
2. **Particle Quality → Medium** (Corpse Explosion es lo que revienta el frametime).
3. **Low FX → On** cuando entréis en Hordas Infernales, Helltide o Pit alto.
4. **Clutter Quality → Low** (menos objetos de suelo que dibujar bajo la nube).
5. **Screen Space Reflections → Off** (coste alto en mazmorras, que es donde están los esbirros).
6. **Display Minion Health Bars → Off** en contenido denso.
7. **Shadow Quality → Medium** y **Dynamic Shadows → On/Off según CPU**: cada esbirro proyecta sombra dinámica.

---

## 11. Claridad visual en Pit alto ✅

**No existe ninguna opción de "ocultar los efectos de otros jugadores"** en Diablo IV según las fuentes consultadas. Icy Veins documenta la petición masiva de la comunidad (*"es la temporada 5, dejadnos desactivar los efectos de otros jugadores, esto es injugable"*) y confirma que **no hay toggle**. ⚠️ **La fuente es previa a *Vessel of Hatred*; no he podido confirmar si en 3.1.3 sigue sin existir.** Merece una comprobación directa en el menú.

**Mitigación disponible hoy** (combinando ajustes de secciones anteriores):

| Ajuste | Valor | Efecto sobre claridad |
|---|---|---|
| **Low FX** | On | Menos partículas propias y ajenas |
| **Clutter Quality** | Low | Suelo limpio → se ven los charcos de daño |
| **Distortion** | **Off** | ⚠️ *Inferencia mía*: quita la deformación de imagen de ondas de calor y efectos, que emborrona el suelo |
| **Screen Shake Effects** | Off | La cámara no se mueve mientras esquivas |
| **Combat Hit Flash** | Off | Se acaba el parpadeo constante |
| **Reduce Strobing** | On | Menos destellos de iluminación |
| **Highlight Player When Obscured** | On | **El ajuste individual más importante**: sabes dónde estás aunque no te veas |
| **Display Player Highlight** + color contrastado | On | Ídem |
| **Monster Health Bar Option** | Always On | Localizas al élite entre el ruido |
| **Show All Damage Numbers** | Off | Elimina la tormenta de cifras |
| **Loot Filter** | Strict | El suelo deja de estar lleno de etiquetas de basura |
| **Character Visibility** (Accesibilidad) | Probar | Sube el contraste global |
| **Colorblind Filter** | Probar como herramienta | Cambia la paleta y puede separar efectos del fondo |
| **HDR** | Off si el panel no es bueno | Un HDR con Black Point mal calibrado destruye la lectura de sombras |

---

## 12. Dúo PC + consola y cross-play ✅

- El **cross-play** es juego base ✅.
- **Las opciones de importación de filtro de botín NO están en consola** (ver 7.4). Es la única asimetría de ajustes que he podido documentar.
- **Item Drop Sounds / In-game Loot Sounds** ✅: se puede filtrar el **sonido de drop por rareza**. Game8 recomienda filtrarlo a **legendario o superior**; Kotaku sugiere ajustarlo a "solo lo que te interesa oír". **Consejo de dúo: poned los dos el mismo umbral**, para que cuando uno diga "ha sonado algo bueno" el otro sepa de qué habla. ⚠️ El nombre exacto del ajuste difiere entre fuentes ("Item Drop Sounds" vs "In-game Loot Sounds").
- **Player Audio on Error** ✅: la voz que dice "no puedo hacer eso". Kotaku recomienda ponerla en **Off** o **Simple**.
- ⚠️ **No he podido confirmar** si los ajustes se sincronizan entre plataformas vía cross-progression. Asumid que **no** y configurad cada máquina por separado.

---

## 13. Ajustes de sistema fuera del juego ✅

De Switchblade Gaming (⚠️ fuente con fecha/parche incoherentes, tratar con cautela):

- **Hardware-Accelerated GPU Scheduling (HAGS)** en Windows → **activado**
- **Plan de energía** → Alto rendimiento
- **Modo Juego de Windows** → On
- **Memory Integrity / Integridad de memoria** → desactivar si es posible
- **Battle.net** → que se cierre al arrancar el juego
- **Config oculta:** `DisablechromaEffects=1` en `Documentos\Diablo IV\LocalPrefs.txt` ⚠️ **No he podido verificar esta entrada en ninguna otra fuente. Editad ese archivo bajo vuestra responsabilidad y haced copia antes.**
- **Almacenamiento:** SSD obligatorio (~90 GB). En HDD las transiciones de zona son lentísimas.
- **Drivers de GPU al día** — sobre todo para aprovechar DLSS 5X/6X y XeSS 3 del parche 3.1.0.

⚠️ **Nota SteamOS/Steam Deck:** FinalBoss indica que el parche 3.1.0 rompió la compatibilidad con SteamOS y que se resolvió con un Proton Hotfix. Irrelevante si jugáis en Windows.

---

## 14. Checklist de configuración día 1 (imprimible)

**Jugabilidad ✅**
- [ ] Advanced Tooltip Information → ON
- [ ] Advanced Tooltip Compare → ON
- [ ] Show Items on Ground Behavior → Toggle
- [ ] Item Label Duration on Drop → máximo
- [ ] Display Minion Health Bars → ON (por ahora)
- [ ] Monster Health Bar → Always On
- [ ] Highlight Player When Obscured → ON
- [ ] Player Highlight Color → distinto al de tu pareja
- [ ] Screen Shake → Off
- [ ] Show All Damage Numbers → ON (aprendizaje)

**Controles ✅**
- [ ] Combine Move/Interact/Basic Skill Slot → **OFF**
- [ ] Move & Interact → clic izquierdo
- [ ] Force Move → rueda del ratón (desactivar antes el zoom con rueda)
- [ ] Hold Position → Shift
- [ ] Show Item Labels → sacar de `Alt`
- [ ] Loot Filter → bind propio

**Gráficos ✅**
- [ ] Display Mode → Windowed Fullscreen
- [ ] VSync → Off
- [ ] Max Foreground FPS → refresco del monitor (−3)
- [ ] Max Background FPS → 30
- [ ] Limit Cutscene FPS → On
- [ ] Upscaler según GPU, modo Quality (1440p)
- [ ] Reflex Low Latency → Enabled + Boost
- [ ] Ray Tracing → Off
- [ ] Shadow Quality → Medium · Soft Shadows → Off · SSAO → Medium · Fog → Medium · SSR → Off · Water → Low · Clutter → Low
- [ ] Low FX → listo para activar en contenido denso

**Sonido ✅**
- [ ] Item Drop Sounds → legendario o superior (el mismo umbral en ambas máquinas)
- [ ] Player Audio on Error → Off/Simple

**Filtro de botín ✅**
- [ ] PC: importar Maxroll Light
- [ ] Consola: replicar a mano vía d4lootfilter.com

---

## Incertidumbres y contradicciones

### Contradicciones entre fuentes (las reporto, no las promedio)

1. **Disponibilidad del Loot Filter.** Maxroll: *"lanzado con la expansión Lord of Hatred"*. Icy Veins y Fextralife: *"disponible para todos los jugadores independientemente de la expansión"*. **Resuelto a favor de ✅ juego base** por ser dos fuentes explícitas contra una redacción ambigua.
2. **Límite de reglas del filtro:** **25** (Fextralife) vs **30** (d4lootfilter.com). Sin resolver.
3. **Shadow Quality:** Switchblade lo llama *"el ajuste con mayor coste unitario de FPS del juego"* y recomienda **Medium**; Skycoach también Medium; PCGamesN y FinalBoss recomiendan **Highest**. Depende del objetivo (calidad vs FPS), pero la discrepancia es real.
4. **Soft Shadows:** Off (Skycoach, Switchblade) vs On (PCGamesN, FinalBoss).
5. **Display Mode:** Windowed Fullscreen (Switchblade, Charlie INTEL, Dexerto) vs Fullscreen exclusivo (1v9, FinalBoss).
6. **Anti-Aliasing con upscaler:** Switchblade dice **Off** si usas DLSS/FSR; el resto dice **High** siempre.
7. **Water Simulation:** Low (Switchblade) vs High (PCGamesN, FinalBoss).
8. **Clutter Quality:** Low (Skycoach) vs Medium (Switchblade) vs High (PCGamesN, FinalBoss).
9. **Sharpen Image:** 90 (Charlie INTEL) vs 6 (Dexerto). Escalas incompatibles; no he podido determinar el rango real del slider.
10. **Max Foreground FPS:** 400 vs 200 vs "igual al refresco".
11. **DLSS "Off (Balanced si NVIDIA)"** — redacción interna contradictoria en Charlie INTEL y Dexerto. Ignorada.
12. **1v9.gg** lista ajustes que **no aparecen con esos nombres en ninguna otra fuente** ("Crowd Density", "Volumetric Fog" como opción separada, "motion blur", "DLAA"). **Fuente de baja fiabilidad**: no he usado sus nombres de ajuste.
13. **Switchblade Gaming** se fecha 26/05/2026 pero declara cubrir **Season 8 / parche 2.2.0**. Incoherencia interna: he usado su detalle técnico (que encaja con el resto) pero marco la fuente.
14. **Nombre del ajuste de sonido de drops:** "Item Drop Sounds" (Game8) vs "In-game Loot Sounds" (Kotaku).

### Lo que NO he podido confirmar

- **Opción de auto-recoger oro.** El brief la menciona. **No he encontrado ninguna fuente que documente un toggle de "auto-pickup de oro" en el menú de opciones de Diablo IV.** No afirmo que no exista; afirmo que no lo he visto. **Comprobación directa recomendada en el menú Jugabilidad.**
- **Transparencia del chat.** Igual: ninguna fuente consultada documenta un ajuste de transparencia/opacidad del chat. Sí existe una pestaña Social, pero no tengo su contenido.
- **"Marcadores de suelo" (ground markers)** en el sentido de retículas de habilidad: solo he confirmado *Show Items on Ground Behavior*, *Item Label Duration on Drop* y los *Highlight Colors*. No he encontrado documentación de indicadores de área de habilidad configurables.
- **Toggle de efectos de otros jugadores:** confirmado como **inexistente** en una fuente **anterior a Vessel of Hatred**. No sé si en 3.1.3 sigue igual. **Comprobación directa recomendada.**
- **Estructura exacta del menú en 3.1.3.** Mi enumeración completa del menú Jugabilidad viene de **abril de 2023**. Los nombres se siguen citando en fuentes de 2026, pero pestañas y agrupaciones pueden haber cambiado. Algunos ajustes (Screen Shake, Reduce Strobing, Combat Hit Flash) aparecen unas veces bajo **Jugabilidad** y otras bajo **Accesibilidad** — probablemente porque el menú se reorganizó en algún momento.
- **"Character Visibility"**: nombre documentado en mayo de 2024. Puede haber cambiado.
- **Ajustes de HDR** (HDR Brightness / Black Point / White Point): **fuente única** de febrero de 2026, sin contrastar.
- **`DisablechromaEffects=1` en LocalPrefs.txt**: fuente única, no verificada.
- **Coste real en FPS de los esbirros del nigromante:** ningún benchmark. Toda la sección 10 es razonamiento sobre hechos documentados, marcado como tal.
- **Frame Generation y latencia en Pit alto:** mi recomendación de valorar desactivarla en intentos serios es inferencia técnica, no una cita de guía de D4.
- **Talisman Set Bonus** como condición del filtro: no he podido determinar si los Talismanes son juego base o expansión 🔒.
- **Sincronización de ajustes entre PC y consola** vía cross-progression: sin fuente.
- **Keybinds de élite (rob2628, wudijo):** existen vídeos suyos sobre el tema, pero **no he podido extraer su contenido** (formato vídeo). El esquema de la sección 9.3 es síntesis de guías generalistas, no la configuración canónica de un jugador top.
- **Ninguna guía dedicada de ajustes en Maxroll, Icy Veins ni Mobalytics para la S14.** El vacío es de las propias fuentes de élite, no de la búsqueda.

---

## Resumen ✅ / 🔒 del dominio

| Sistema | Estado |
|---|---|
| Menú de Gráficos completo (calidad, RT, upscalers) | ✅ juego base |
| **XeSS 3** (Intel) y **DLSS 5X/6X** (Nvidia), parche 3.1.0 | ✅ juego base (sección "Base Game" de las notas) |
| DLSS 4 Multi Frame Generation nativo | ✅ juego base |
| Menú de Jugabilidad (tooltips, etiquetas, barras de vida, highlights) | ✅ juego base |
| **Loot Filter** completo (reglas, recolor, ocultar) | ✅ juego base |
| Import/export de códigos de filtro | ✅ juego base, **pero solo en PC** (limitación de plataforma, no de expansión) |
| Menú de Accesibilidad completo | ✅ juego base |
| Keybinds, Force Move, Hold Position, Combine Move/Interact | ✅ juego base |
| Contador de FPS (`Ctrl+R`) | ✅ juego base |
| Sonidos de drop por rareza, Player Audio on Error | ✅ juego base |
| Modo **Solo Self-Found** (S14) | ✅ juego base, opt-in **en la creación de personaje** — **NO lo cojáis: impide agrupar y comerciar toda la temporada** |
| Condición de filtro **Talisman Set Bonus** | ⚠️ posiblemente 🔒 — sin confirmar |
| Sistemas de **War Plans / Charms / Seals** (aparecen en notas de parche como sección aparte) | ⚠️ probablemente 🔒 |
| Spiritborn, Mercenarios, Runewords, Kurast | 🔒 *Vessel of Hatred* |
| Warlock | 🔒 *Lord of Hatred* (hay prueba gratuita temporal en S14) |

---

## Fuentes

Páginas realmente abiertas con WebFetch:

1. https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes — notas oficiales 3.1.0 / 3.1.1 / 3.1.2 / 3.1.3
2. https://maxroll.gg/d4/news/diablo-4-3-1-0-patch-notes — notas 3.1.0 desglosadas (24/06/2026)
3. https://maxroll.gg/d4/resources/loot-filter — guía del filtro de botín (act. 21/07/2026)
4. https://diablo4.wiki.fextralife.com/Loot+Filters — wiki del filtro de botín
5. https://www.icy-veins.com/d4/news/after-years-of-requests-diablo-4-will-finally-get-a-loot-filter/ — disponibilidad del filtro
6. https://www.d4lootfilter.com/guide — filtros en PS5/Xbox (act. mayo 2026)
7. https://skycoach.gg/blog/diablo-4/articles/best-diablo-4-settings — ajustes S14 (23/07/2026)
8. https://finalboss.io/best-diablo-4-settings-for-smooth-gameplay-on — ajustes (act. 12/08/2026)
9. https://www.switchbladegaming.com/game-settings/diablo-4-best-settings/ — desglose técnico por ajuste
10. https://www.pcgamesn.com/diablo-4/best-settings-pc — tabla de calidad (act. 18/08/2025)
11. https://www.charlieintel.com/diablo/best-pc-settings-for-diablo-4-high-fps-graphics-visibility-requirments-more-256277/ — perfiles alto/bajo (17/12/2024)
12. https://www.dexerto.com/diablo/best-diablo-4-pc-settings-high-fps-graphics-visibility-2168173/ — perfiles alto/bajo (27/06/2024)
13. https://1v9.gg/blog/diablo-4-best-graphic-settings-guide — ⚠️ baja fiabilidad, nombres no corroborados
14. https://www.icy-veins.com/d4/news/diablo-iv-just-got-a-massive-fps-boost-with-native-dlss-4-support/ — DLSS 4 nativo
15. https://mythicdrop.com/guide/diablo-4-gameplay-settings — enumeración del menú Jugabilidad (15/04/2023)
16. https://kotaku.com/diablo-4-iv-graphics-settings-framerate-pc-ps5-xbox-1850508602 — 11 ajustes esenciales (06/06/2023)
17. https://www.iggm.com/news/diablo-4-how-to-complete-keybinds-controls-setup-force-move — keybinds y Force Move (15/05/2023)
18. https://game8.co/games/Diablo-4/archives/413979 — ajustes de consola (14/06/2023)
19. https://www.icy-veins.com/d4/news/has-disabling-other-players-effects-become-needed-for-diablo-4/ — efectos de otros jugadores
20. https://us.forums.blizzard.com/en/d4/t/what-was-that-new-setting-enabled-in-s4-to-make-contrast-better/160559 — "Character Visibility" (15/05/2024)
21. https://evezone.evetech.co.za/performance-pulse/diablo-4-hdr-fix-grey-filter-guide — HDR (09/02/2026)
22. http://www.vhpg.com/diablo-4-low-fx/ — definición de Low FX
23. https://www.shacknews.com/article/135766/diablo-4-settings-pc-console-accessibility — ajustes PC/consola/accesibilidad (parcial)
24. https://www.wowhead.com/diablo-4/news/new-visual-accessibility-options-coming-to-diablo-4-ptr-338410 — ⚠️ contenido no extraíble

Páginas que **devolvieron error** y no pude leer (las anoto por transparencia): mmopixel.com (403), dving.net (403), mp1st.com (403), diablobytes.com (403), mobalytics.gg/diablo-4/guides/patch-3-1-3-changes-and-fixes (403), sportskeeda.com (405), steamcommunity.com (rate limit).
