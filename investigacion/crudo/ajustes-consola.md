# Diablo IV en consola: ajustes óptimos, mando y cross-play

**Fecha de investigación:** 18 de agosto de 2026
**Estado del juego asumido:** Season 14 "Death Awakening" (viva desde 30/06/2026) · Parche **3.1.3, build 73224 (12/08/2026)**
**Perfil del jugador:** principiante, **Nigromante (Necromancer)**, **SOLO JUEGO BASE** (sin *Vessel of Hatred*, sin *Lord of Hatred*), en **dúo** con su pareja (también nigromante), **uno en PC y otro en consola** (cross-play), objetivo min-max / leaderboard.

**Leyenda obligatoria:**
- ✅ = funciona con el **juego base**, sin comprar nada.
- 🔒 = **requiere expansión** (se indica cuál).
- ⚠️ = no he podido confirmarlo con fuente fiable y fechada; ver "Incertidumbres".

---

## 0. Resumen ejecutivo (lee esto si no lees nada más)

1. **En consola no eliges "modo rendimiento vs calidad" como en otros juegos.** Diablo IV salió con un único objetivo de **60 fps** en PS5 / Xbox Series X|S, y lo que hay es un **interruptor llamado "Enhanced Visuals" (Visuales Mejoradas)** que activa *ray tracing* y **bloquea el juego a 30 fps**. ✅ (juego base)
2. **Para min-max: "Enhanced Visuals" = OFF, siempre.** 60 fps estables valen infinitamente más que reflejos con trazado de rayos en un ARPG de pantallas llenas de mobs. La propia comunidad lo confirmó con caídas por debajo de 30 fps en zonas cargadas.
3. **El mando por defecto es malo para nigromante.** Hay que separar "Interact" de "Basic Skill", desactivar *Hold to Lock Target* y *Persist Target Lock*, dejar *Cycle Locked Target* en ON, y (si hay levas traseras) mover Evade y Skill 4 ahí. ✅
4. **El límite real de la consola no es gráfico, es de información:** no puedes importar códigos de **filtro de loot (loot filter)**, no puedes tener planner/overlay en segunda pantalla, y comerciar es lentísimo. Se compensa con tablet/móvil al lado y con decodificadores web de filtros.
5. **Cross-play y cross-progression funcionan y son gratis** ✅, pero **la licencia no viaja**: si algún día queréis jugar en la otra plataforma hay que comprar el juego otra vez ahí.
6. **PELIGRO para vuestro dúo:** el modo **Solo Self-Found (SSF)** nuevo de la S14 ✅ **prohíbe agrupar**. Si uno de los dos lo elige por error, no podéis jugar juntos con ese personaje **durante toda la temporada**. NO lo elijáis.
7. **Las builds top de nigromante de la S14 dependen de contenido de expansión.** Blood Wave (A tier) requiere Runewords 🔒 y Mercenarios 🔒. Con juego base sois viables con **Minion / Bone Spear / Bone Spirit** en su versión "sin runas ni mercenarios", asumiendo pérdida de techo.

---

## 1. Rendimiento y gráficos en consola

### 1.1 Qué modos existen realmente

Diablo IV **no lanzó con modos "Calidad/Rendimiento/Equilibrado"**. Blizzard priorizó 60 fps por el ritmo del combate y no ofreció alternativa de 30 fps con mejores gráficos. Lo que sí llegó después, en el **parche 1.3.5 (marzo de 2024)**, fue la opción **"Enhanced Visuals"** dentro de la pestaña **Graphics (Gráficos)** de consola, que añade:

- Sombras con trazado de rayos (*ray traced shadows*)
- Reflejos con trazado de rayos (*ray traced reflections*)
- Mejoras de oclusión ambiental (*ambient occlusion*)
- Cambios en *contact shadows*

...y **bloquea el juego a 30 fps por diseño**. ✅ (es una opción del cliente base, no de expansión)

### 1.2 Tabla de rendimiento por plataforma

| Plataforma | Resolución | FPS objetivo | Enhanced Visuals (RT) | Notas |
|---|---|---|---|---|
| PS5 | 4K | 60 | Sí → baja a 30 fps | Soporta VRR por HDMI 2.1 ⚠️ |
| Xbox Series X | 4K | 60 | Sí → baja a 30 fps | Reportes de caídas por debajo de 30 con RT |
| Xbox Series S | 1080p | 60 | Probablemente no ⚠️ | Pure Xbox: "no hemos visto mención específica de Series S" |
| PS4 | 1080p | 30 | No | Gen anterior |
| Xbox One | 900p | 30 | No | Gen anterior |
| PS5 Pro | ⚠️ | ⚠️ | ⚠️ | Rod Fergusson confirmó parche PS5 Pro; detalles concretos no confirmados por fuente primaria |

### 1.3 Recomendación de min-max

| Ajuste (pestaña Graphics) | Valor recomendado | Por qué |
|---|---|---|
| **Enhanced Visuals** | **OFF** | Duplica tu framerate (30 → 60). En Pit / Infernal Hordes / Ruptures, los fps son supervivencia. |
| VRR (a nivel de consola) | **ON** si tu tele lo soporta | Elimina *tearing* y suaviza las caídas de los 60 |
| 120 Hz / modo 120 fps | **No existe modo 120 fps dedicado** ⚠️ | Ninguna fuente confirma un modo 120 en 2026 |
| Color Blind Filter | Off salvo necesidad | Opciones: Protanopia, Deuteranopia, Tritanopia ✅ |

> **Nota de contradicción:** algunas fuentes de 2026 (nerdburglars, vía resultados de búsqueda) afirman que en PS5 "puedes cambiar entre Performance y Fidelity sobre la marcha". No he podido abrir esa página (403). La nomenclatura que **sí** he confirmado en fuentes abiertas es **"Enhanced Visuals"**, no "Performance/Fidelity". Trato "Performance/Fidelity" como no confirmado.

---

## 2. Pantalla, brillo y HDR

Esto es lo que más gente hace mal en consola, porque Diablo IV tiene un problema **conocido de niveles de negro en HDR**: la imagen sale grisácea y lavada incluso con el *Black Point* al mínimo.

### 2.1 Orden correcto de calibración (hazlo en este orden)

**Paso 1 — Calibra HDR a nivel de consola** (antes de tocar el juego):
- **PS5:** `Ajustes > Pantalla y vídeo > Salida de vídeo > Ajustar HDR`
- **Xbox Series X|S:** `Configuración > General > Opciones de TV y pantalla > Calibrar HDR para juegos`

**Paso 2 — Calibra dentro del juego:**
- `Opciones > pestaña Graphics (Gráficos)` → **"Calibrate Brightness" (Calibrar brillo)**
- Verás tres controles con tres imágenes de referencia. **Orden correcto:**
  1. **Black Point (Punto de negro)** — usa la imagen de la **izquierda**. Bájalo. El valor por defecto suele estar demasiado alto y es la causa del velo gris.
  2. **White Point (Punto de blanco)** — usa la imagen de la **derecha**. Ajústalo al **pico de brillo real de tu tele**, pero juzga con la imagen real del juego, no con la de test.
  3. **Brightness (Brillo)** — imagen central, a gusto.
- Game8 recomienda **Brightness al 60% o superior** para consola/TV a distancia.

**Paso 3 — Si el HDR sigue sin convencerte:** desactívalo y juega en SDR. Es una opción legítima y muy defendida por la comunidad de HDR.
- **PS5:** `Ajustes > Pantalla y vídeo > Salida de vídeo > HDR` (desactivar)
- **Xbox:** `Configuración > General > Opciones de TV y pantalla > Modos de vídeo` → desactivar *Allow HDR10*, *Auto HDR* y *Allow Dolby Vision for Gaming*

**Paso 4 — Compensa en la tele.** Como el juego no arregla del todo los negros, usa el ajuste de tu televisor tipo *Fine Tune Dark Areas* / *Ajuste fino de zonas oscuras*.

> **Aviso:** hay que **recalibrar si cambias de entorno de luz** (jugar de día vs de noche). Diablo IV es un juego oscurísimo y esto importa de verdad en Ruptures y mazmorras.

---

## 3. Ajustes de jugabilidad, interfaz y accesibilidad (equivalentes a PC)

Todo lo de esta sección es ✅ **juego base**.

### 3.1 Pestaña Gameplay (Jugabilidad)

| Opción (inglés) | Valor recomendado | Motivo (min-max) |
|---|---|---|
| **Combat Hit Flash** | ON | Feedback visual de impacto; en consola, a distancia de sofá, es clave |
| **Advanced Tooltip Information** | ON | Muestra **rangos de stats** en el gear: sabes al instante si una tirada es baja, media o máxima. **Imprescindible para min-max** |
| **Advanced Tooltip Compare** | ON | Comparar objetos directamente (en mando se activa manteniendo **Y / Triángulo**) |
| **Screen Shake Effects** | OFF | Claridad visual en combates cargados; menos mareo |
| **Damage Numbers / Combat Text** | Filtrar | Puedes elegir qué tipos de daño se muestran. Menos ruido = mejor lectura de pantalla |
| **Item Drop Sounds** | "Legendary and higher" | Reduce el ruido de loot basura |
| **Highlight Character When Obscured** | ON | Contorno permanente del personaje: no lo pierdes de vista cuando te rodean 40 esqueletos (tuyos y suyos) |
| **Combine Interact and Basic Skill** | **OFF** | **Crítico para nigromante.** Ver sección 4.3 |
| **Skill Toggle Behavior** | "Toggle All" ⚠️ | Varias fuentes lo describen como el ajuste de "auto-apuntado". Ver Incertidumbres |
| **Loot Filter** (Filtro de botín) | Configurar a mano | `Opciones > Gameplay > Loot Filter` en PS5. Ver sección 6 |

### 3.2 Accesibilidad / Interfaz — lo que sí cambia la vida en consola

Diablo IV tiene **más de 50 funciones de accesibilidad**. Estas son las que un jugador de consola debería tocar aunque no tenga ninguna necesidad de accesibilidad:

| Opción | Valor | Motivo |
|---|---|---|
| **Font Scale (Escala de fuente)** | **Large** | El tamaño "Medium" solo vale pegado a un monitor. En TV, subtítulos, chat y menús son ilegibles |
| **Character Highlight** | ON | Duplicado a propósito: es el ajuste #1 de consola |
| **Loot audio cues / Ambient loot audio** | ON | Los objetos en el suelo emiten sonido ambiental **según su rareza**. En consola, donde no puedes barrer con el ratón, esto sustituye al escaneo visual |
| **HUD Compass / Quest Arrow** | ON | Flecha de objetivo; en `Accessibility > HUD` |
| **High-Contrast Cursor** | ON | Relevante sobre todo si el compañero de PC lo activa |
| **Subtitles (Subtítulos)** | ON + personalizados | En `Sound` o `Accessibility` |
| **Toggle for button holds** | ON si te molestan los mantenidos | Convierte "mantener" en "pulsar". Menos fatiga de mano en sesiones largas |
| **Screen Reader / Text to Speech** | Off por defecto | Velocidad y volumen ajustables |
| **Enemy / NPC highlighting** | ON | Muy usado incluso por streamers |

**Mención especial:** la lista oficial de accesibilidad incluye **"asistencia de mercenarios en combate"** — ojo, **los Mercenarios son 🔒 Vessel of Hatred**. Esa entrada no te aplica.

---

## 4. Mando: esquema de botones y pilotaje

### 4.1 Esquema por defecto (PS y Xbox)

| Acción | PlayStation | Xbox |
|---|---|---|
| Moverse | Stick izquierdo | Stick izquierdo |
| **Interact / Basic Skill** (combinados) | **X** | **A** |
| Core Skill | Cuadrado | X |
| Skill Slot 1 | Triángulo | Y |
| Skill Slot 2 | R1 | RB |
| Skill Slot 3 | L2 | LT |
| Skill Slot 4 | R2 | RT |
| **Evade (Esquiva)** | **Círculo** | **B** |
| Usar poción | L1 | LB |
| Portal a ciudad | Cruceta ↓ | Cruceta ↓ |
| Montura | Cruceta → | Cruceta → |
| Espolear montura | R2 | RT |
| Desmontar | Círculo | B |
| **Lock Target** | **R3** (pulsar stick derecho) | **Pulsar stick derecho** |
| Panel de personaje | Options | Start |
| Mapa | Touchpad | Botón Options/View |
| Action Wheel | Cruceta ↑ | Cruceta ↑ |
| Responder petición social | Cruceta ← | Cruceta ← |
| **Show Item Labels** | **L3** | Pulsar stick izquierdo |

### 4.2 Remapeo recomendado (min-max)

La configuración que recomienda KontrolFreek —y que es la más citada— reorganiza el mando para que **nunca sueltes el stick izquierdo**:

| Acción | Binding recomendado (PS) | Razón |
|---|---|---|
| Interact | X | Separado de Basic Skill |
| **Basic Skill** | **L2** | Gatillo, se puede mantener sin soltar el pulgar |
| **Core Skill** | **R2** | Igual: gatillo = *spam* cómodo |
| Skills 1-4 | Cuadrado, Triángulo, Círculo, R1 | Los botones frontales quedan para cooldowns |
| **Evade** | **L3** (o leva trasera) | Ver aviso abajo |
| Usar poción | L1 | Accesible sin soltar sticks |
| Mount Combat / Dismount | L2 | |

**Ajustes numéricos del mando:**

| Ajuste | Valor | Nota |
|---|---|---|
| **Vibration (Vibración)** | ON | Feedback; desactívala si te molesta o quieres batería |
| **Cursor Sensitivity** | **6** | Punto de partida citado; es preferencia personal |
| **Dead Zone (Zona muerta)** | **Lo más pequeña posible sin drift** | Zona muerta grande = input lag percibido. Súbela solo si tu stick deriva |

> **Aviso sobre Evade:** hay **contradicción directa entre fuentes**. KontrolFreek propone mover Evade a **L3** o a una leva trasera; el esquema por defecto lo tiene en **Círculo / B**. Círculo/B es más rápido de pulsar pero te obliga a soltar el pulgar derecho (que en consola no controla la puntería, así que el coste es bajo). **Mi lectura:** si tienes mando con levas (DualSense Edge, Xbox Elite, Scuf), Evade a leva trasera es objetivamente superior. Si no, **déjalo en Círculo/B**, no en L3 — pulsar el stick para esquivar es propenso a error bajo presión.

### 4.3 Stick vs apuntado: cómo funciona realmente la puntería en consola

Esta es la diferencia más grande respecto a PC y hay que entenderla bien:

- **En PC apuntas con el cursor del ratón**: la dirección de un Bone Spear, un Corpse Tendrils o un Blood Wave es exactamente donde está el puntero, con precisión de píxel.
- **En consola no hay cursor libre.** El personaje lanza **en la dirección del stick izquierdo** (o hacia el objetivo bloqueado). El stick derecho **no apunta**: sirve para el **target lock** y para ciclar objetivos.

Consecuencias prácticas:

1. **Las skills de área centradas en ti (Blood Surge, Blood Mist, Bone Storm) son idénticas en mando y en teclado.** Coste cero.
2. **Las skills direccionales (Bone Spear, Sever, Blood Wave, Bone Prison) pierden precisión.** Puedes lanzarlas en 8-16 direcciones cómodas, no en 360 grados finos.
3. **Las skills de posicionamiento remoto (Corpse Explosion, Corpse Tendrils) son el punto débil real.** Requieren seleccionar un cadáver concreto a distancia. En PC es un clic; en mando es "el que el juego decida".

### 4.4 Target Lock: la configuración correcta

Las tres opciones viven en `Opciones > Controls (Controles) > Controller`:

| Opción | Valor recomendado | Motivo |
|---|---|---|
| **Hold to Lock Target** | **OFF** | Ver bug abajo |
| **Persist Target Lock** | **OFF** | Si está ON, el lock persiste entre encuentros y acabas pegándole a un enemigo lejano mientras te comen |
| **Use Right Stick to Cycle Locked Target** | **ON** | Es lo que hace que el sistema sea útil: pulsas R3 para fijar y mueves el stick derecho para cambiar de objetivo |

Con esta config: **R3 fija/suelta objetivo manualmente**, y el stick derecho cicla. Es el mejor compromiso para boss fights (fijas al jefe) sin quedarte pegado en trash.

> **⚠️ BUG CONOCIDO (reportado 22/06/2023, sin confirmación de fix):** si activas **Hold to Lock Target** *y* **Use Right Stick to Cycle Locked Target** a la vez, y mueves el stick derecho mientras mantienes el botón de lock, **el objetivo se queda bloqueado y no puedes soltarlo hasta que termina el encuentro**. Reportado en Xbox y confirmado por otro jugador. **No he encontrado constancia de que se haya arreglado**, lo que refuerza la recomendación de Hold to Lock Target = OFF.

### 4.5 El truco de nigromante que nadie te cuenta

**Problema específico de la clase:** si tienes una **skill de cadáver (Corpse Skill)** — Corpse Explosion o Corpse Tendrils — asignada al botón que también hace **Interact**, al querer **recoger un objeto del suelo tendrás que ciclar por TODOS los cadáveres** antes de que el juego te deje interactuar con el ítem.

**Soluciones (elige una):**
1. Poner **Combine Interact and Basic Skill = OFF** para que Interact tenga botón propio.
2. Desemparejar la skill de cadáver del botón de interacción.
3. Asignar una skill **que no sea de cadáver** a ese botón.

Para un nigromante de consola esto no es opcional: es la diferencia entre farmear y pelearte con el menú.

---

## 5. Nigromante con mando: qué builds son cómodas y cuáles son un infierno

### 5.1 Tier list endgame S14 (Maxroll, actualizada 29/06/2026) cruzada con "comodidad de mando" y "requisito de expansión"

| Build | Tier Maxroll S14 | Exigencia de apuntado con mando | ¿Juego base? |
|---|---|---|---|
| **Blood Wave** | **A** | Media (direccional + posicionarte dentro de Bone Prison) | 🔒 **NO** — requiere Runewords, Talismanes y recomienda Mercenarios |
| **Bone Spirit** | **A** | Media (proyectil buscador; genera con Bone Spear/otra) | ⚠️ parcial — ver nota |
| **Minion (Esbirros)** | B | **Muy baja** — los esbirros auto-apuntan vía comandos | ✅ **SÍ** en su núcleo (Mercenarios y Runewords son 🔒 y opcionales) |
| **Golem** | B | Baja | ✅ probable ⚠️ |
| **Sever** | B | Media-baja (direccional pero perdonador) | ✅ probable ⚠️ |
| **Blood Surge** | B | **Muy baja** — es AoE centrado en ti | ✅ probable ⚠️ |
| **Blight** | C | Media | ⚠️ |
| **Army of the Dead (AotD)** | C | Baja | ⚠️ |
| **Bone Spear** | C | **Alta** — proyectil direccional que hay que enfilar | ⚠️ parcial — usa Talismanes y Mercenarios |
| **Blood Lance** | C | Media-alta | ⚠️ |

### 5.2 Lectura para vuestro caso concreto (dos nigromantes, juego base, uno con mando)

**Lo cómodo con mando, por orden:**
1. **Minion Necromancer** — el guía de Maxroll dice literalmente que los esbirros van **auto-apuntados mediante comandos** y que el sistema de comandos es directo con mando. Solo requiere **posicionamiento**, no puntería. Es la build de consola por excelencia.
2. **Blood Surge** — AoE centrado en el personaje, explosiones rojas alrededor. No hay nada que apuntar. Además es de las builds "más chulas visualmente" según Maxroll.
3. **Golem / Army of the Dead** — misma lógica de invocación.

**Lo incómodo con mando:**
- **Bone Spear** es el caso claro: proyectil direccional que exige enfilar líneas de enemigos. Con ratón es trivial; con stick pierdes DPS efectivo constantemente. Es además la build "canónica" de nigromante en las guías, lo que crea la trampa clásica: *el que juega en PC puede llevarla, el de consola sufrirá*.
- **Blood Lance** y **Blight** heredan el mismo problema en menor grado.

**Recomendación de dúo:** que **el de consola lleve Minion o Blood Surge** y el de PC lleve lo que quiera. Si queréis llevar la misma build por eficiencia de loot compartido, **llevad los dos Minion**: es la que menos penaliza al mando y a la vez la más amigable para principiantes.

### 5.3 El aviso importante sobre el techo de leaderboard

Vuestro objetivo declarado es leaderboard. Hay que decirlo claro:

- **Blood Wave (A tier)** depende de **Runewords** 🔒 (*Vessel of Hatred*), **Talismanes/charms** ⚠️ y **Mercenarios** 🔒 (*Vessel of Hatred*). **No es alcanzable con juego base.**
- **Bone Spear (C tier)** en su versión de Maxroll usa **Talismanes** y **Mercenarios** 🔒.
- **Minion (B tier)** en su versión de Maxroll recomienda **Mercenarios** 🔒 (Subo, Aldkin, Raheir) y **Runewords** 🔒 (Cir+Ceh, Cem+Gar) — pero su **núcleo** (Book of the Dead ✅, árbol de habilidades ✅, uniques como Deathgrip / The Undercrown / Blood Moon Breeches / Pact of Bone) es de juego base.

Conclusión honesta: **con juego base podéis llegar muy lejos, pero el techo absoluto de leaderboard en la S14 pasa por contenido de expansión.** No es una opinión mía: es lo que dicen las propias guías top al listar sus requisitos.

**Sistemas 🔒 confirmados que NO tenéis:**
- **Vessel of Hatred:** Spiritborn, **Mercenarios**, **Runewords/Runas**, Kurast, **Dark Citadel**, la ultimate de nigromante **Soulrift**, la pasiva clave **Affliction**, las pasivas *Necrotic Fortitude / Finality / Titan's Fall / Precision Decay*, el tablero de Paragón **Frailty**, los aspectos *Reaping Lotus' / Phasing Poltergeist's / Fel Gluttony*, el yelmo único **The Unmaker**.
- **Lord of Hatred:** Warlock (aunque hay **prueba gratuita de Warlock** en la S14 ✅ como evento temporal), Skovos Isles, crafteo del Horadric Cube ⚠️, Paladin ⚠️ (ver contradicciones).
- **Blood Wave sí es de juego base como habilidad** ✅ (existía antes de VoH; las expansiones solo la modificaron) — pero la **build** competitiva de S14 no lo es.

---

## 6. Cross-play y cross-progression: PC + consola

### 6.1 Cómo se monta (ambos son gratis y automáticos) ✅

1. **Crear/usar una cuenta Battle.net** — la misma persona debe usar **la misma cuenta Battle.net** en todas sus plataformas. Si inicias sesión con otra cuenta, te sale una partida completamente distinta.
2. **En consola:** al lanzar Diablo IV aparece un aviso de login → **vincular la cuenta de PSN / Xbox Live con Battle.net**.
3. **Verificar:** entra en `battle.net > Connections (Conexiones)` y confirma que los enlaces están.
4. **En el juego:** `Esc > Options (Opciones) > Social` → **Cross-Network Play** y **Cross-Network Communication** en **ON** (vienen activados por defecto).

### 6.2 Qué viaja y qué no

| Viaja entre plataformas ✅ | NO viaja ❌ |
|---|---|
| Personajes y su nivel | **La licencia del juego**: si quieres jugar en una plataforma nueva, hay que **comprar el juego otra vez ahí** |
| Gear / equipo | Progreso de betas (histórico) |
| Puntos de Paragón | |
| Cosméticos, monturas, títulos | |
| Logros y progreso de cuenta | |
| Progreso de **Battle Pass** | |
| Progreso estacional | |

**Plataformas que pueden jugar juntas:** PC, PS4, PS5, Xbox One, Xbox Series X|S. Vuestro caso (PC + consola) está soportado de serie.

### 6.3 Avisos para vuestro dúo

- **Cross-Network Play se puede DESACTIVAR** — y de hecho una guía de Icy Veins lo sugiere como truco para **reducir la población de la zona** y farmear más tranquilo. **Si lo desactiváis, dejáis de poder jugar juntos.** Solo tiene sentido en sesiones solitarias.
- **Todo el progreso está en servidor**, no hay modo offline. Si se cae Battle.net, no jugáis.
- **Couch co-op (pantalla partida) es de 2 jugadores y es cosa de consola**, no aplica a un dúo PC+consola. Y el modo SSF lo desactiva.
- **⛔ NO ELIJÁIS SOLO SELF-FOUND (SSF)** ✅ (modo nuevo de la S14, disponible con juego base): bloquea **agrupar**, **comerciar**, **couch co-op**, **Party Finder** y **Dark Citadel** 🔒. Es **permanente para ese personaje toda la temporada** (solo pierde la restricción al pasar a Eternal al acabar la season). No da ningún bonus de drop; solo da acceso a **leaderboards SSF exclusivos de la Torre**. Sí seguís **viendo** a otra gente en mundo abierto, Helltides y World Bosses — pero no podéis unir party.

---

## 7. Lo que NO puedes hacer en consola (y cómo compensarlo)

| Limitación de consola | Impacto en min-max | Compensación |
|---|---|---|
| **No puedes importar códigos de Loot Filter** (solo PC) | **Alto.** El filtro de botín es la herramienta #1 de eficiencia en endgame | Usa un **decodificador web** (p. ej. d4lootfilter.com): pegas el código de Maxroll, te lo convierte en reglas legibles, y las **tecleas a mano** en `Opciones > Gameplay > Loot Filter`. Tedioso pero se hace una vez |
| **El menú del Loot Filter está enterrado** | Medio | La comunidad pide un acceso rápido/rueda; de momento no existe. Configúralo bien una vez y no lo toques |
| **No hay overlays ni segundas ventanas** (no puedes tener Maxroll encima del juego) | Medio-alto | **Tablet o móvil al lado del sofá** con el planner abierto. Es la solución estándar. Los planners de Maxroll / D4Builds son web y funcionan en móvil |
| **No hay addons ni mods** | Bajo (D4 no tiene ecosistema de addons ni en PC) | — |
| **Comerciar es lentísimo** | Medio | Reportes de **40 minutos para 3 trades** y de gente **expulsada del servidor por AFK** en mitad del trade por lo que tarda en teclear. Blizzard **no lo había reconocido formalmente** a fecha del reportaje (nov. 2023) ⚠️. Compensación: haced los trades entre vosotros dos, y si hay que teclear cantidades de oro, hacedlo desde el PC |
| **Teclear texto (chat, nombres, cantidades) es un suplicio** | Medio | **Teclado USB/Bluetooth conectado a la consola** — PS5 y Xbox lo soportan a nivel de sistema para introducir texto |
| **No hay chat de comercio ni chat global en el juego** ⚠️ | Bajo | Discord por voz. Es lo que hace todo el mundo |

---

## 8. Latencia e input lag en consola

Diablo IV no expone ajustes de latencia propios en consola (no hay "Reflex" ni equivalente). Todo lo que puedes hacer está **fuera del juego**:

| Ajuste | Dónde | Ganancia |
|---|---|---|
| **Game Mode (Modo Juego) del televisor** | Menú de la TV | **La más grande.** Desactiva interpolación de movimiento, suavizados y nitidez artificial, que añaden **20-80 ms** |
| **ALLM (Auto Low Latency Mode)** | Ajustes de consola, dejarlo **ON** | La consola le dice a la tele que entre sola en su modo de menor latencia. Requiere HDMI 2.1 |
| **VRR ON + 120 Hz de salida** | Ajustes de consola | Suaviza variaciones. Ojo: aunque el juego no tenga modo 120 fps, sacar la señal a 120 Hz reduce latencia de presentación |
| **Cable HDMI 2.1 Ultra High Speed** | Físico | Necesario para 4K/120 + VRR + ALLM simultáneos |
| **Desactivar motion blur / smoothing / post-proceso de la TV** | Menú de la TV | Otros **30-100 ms** de penalización eliminados |
| **Zona muerta del mando lo más baja posible** | Dentro del juego | No es input lag real, pero se percibe como respuesta más inmediata |
| **Ethernet en vez de WiFi** | Físico | D4 es siempre-online; el lag de red se percibe como input lag |

> **Ojo con la trampa:** de todos estos, **ninguno está dentro de Diablo IV**. Un jugador de consola que se queja de "input lag en D4" casi siempre tiene el **Modo Juego de la tele apagado**. Compruébalo antes que nada.

---

## 9. Checklist de configuración inicial (imprimible)

**A nivel de consola, una vez:**
- [ ] Modo Juego de la TV: **ON**
- [ ] ALLM: **ON** · VRR: **ON** · salida 120 Hz si la tele lo permite
- [ ] Cable HDMI 2.1 Ultra High Speed
- [ ] Motion blur / suavizado / nitidez de la TV: **OFF**
- [ ] Calibrar HDR del sistema (PS5: Ajustar HDR · Xbox: Calibrar HDR para juegos)
- [ ] Ethernet si es posible
- [ ] Teclado USB/BT conectado (para chat y trades)

**Dentro de Diablo IV — Graphics:**
- [ ] **Enhanced Visuals: OFF**
- [ ] Calibrate Brightness → Black Point (bajar) → White Point → Brightness (~60%+)
- [ ] Color Blind Filter según necesidad

**Gameplay:**
- [ ] Combat Hit Flash: ON
- [ ] Advanced Tooltip Information: ON
- [ ] Advanced Tooltip Compare: ON
- [ ] Screen Shake: OFF
- [ ] **Combine Interact and Basic Skill: OFF**
- [ ] Item Drop Sounds: Legendary and higher
- [ ] Loot Filter: configurar a mano desde un código decodificado

**Accessibility / Interface:**
- [ ] Font Scale: **Large**
- [ ] Character Highlight: ON
- [ ] Loot audio cues: ON
- [ ] HUD Compass / Quest Arrow: ON
- [ ] Subtítulos: ON

**Controls / Controller:**
- [ ] Hold to Lock Target: **OFF**
- [ ] Persist Target Lock: **OFF**
- [ ] Use Right Stick to Cycle Locked Target: **ON**
- [ ] Dead Zone: mínima sin drift
- [ ] Cursor Sensitivity: ~6
- [ ] Vibration: a gusto
- [ ] Basic Skill → L2/LT · Core Skill → R2/RT
- [ ] Evade en Círculo/B (o leva trasera si tienes)
- [ ] Cruceta: ↑ Action Wheel · → Montura · ↓ Portal · ← Petición social
- [ ] Verificar que ninguna Corpse Skill comparte botón con Interact

**Social:**
- [ ] Cross-Network Play: **ON** (obligatorio para el dúo)
- [ ] Cross-Network Communication: ON
- [ ] Cuenta de consola vinculada a Battle.net · verificado en battle.net > Connections
- [ ] **NO** crear personaje en Solo Self-Found

---

## Incertidumbres y contradicciones

### Contradicciones detectadas entre fuentes (las reporto, no las promedio)

1. **Nombres de los modos gráficos de consola.** Fuentes abiertas (Pure Xbox, foros de Blizzard) hablan solo de **"Enhanced Visuals"** como interruptor de ray tracing que baja a 30 fps. Otras fuentes de 2026 (nerdburglars, vía snippet de búsqueda — página no accesible, HTTP 403) hablan de alternar **"Performance" y "Fidelity"** sobre la marcha en PS5. **No he podido reconciliarlo.** Es posible que Blizzard renombrara las opciones en algún parche entre 2024 y 2026, o que la fuente use terminología genérica. **Trata "Enhanced Visuals" como el nombre confirmado y busca ambos en el menú.**
2. **Asignación de Evade.** El esquema por defecto lo pone en **Círculo/B**; KontrolFreek recomienda **L3 o leva trasera**. Ambas son defendibles; he dado mi criterio en §4.2 pero es criterio, no dato.
3. **Ray tracing en Xbox Series S.** Pure Xbox dice que "no hay mención específica de Series S" y supone que se queda fuera. No hay confirmación oficial en ninguna dirección.
4. **Paladín en Lord of Hatred.** Wikipedia afirma que *Lord of Hatred* (28/04/2026) añade **Paladin y Warlock**, y que el Paladín "pasó a ser jugable en el juego base para quienes reservaron". El contexto que me han dado dice solo "Warlock". **No he podido verificar el estado del Paladín con una fuente primaria de Blizzard.** Queda fuera de mi dominio pero lo señalo porque afecta a "qué tengo con juego base".

### Cosas que NO he podido confirmar

- **Modo 120 fps / 120 Hz nativo en consola en 2026.** Ninguna fuente abierta lo confirma. Solo hay peticiones de la comunidad desde la beta.
- **PS5 Pro:** confirmada la intención de parche por Rod Fergusson, pero **sin especificaciones oficiales** (resolución, fps, PSSR, ray tracing). La página que las detallaba devolvió 403.
- **A qué expansión pertenece el sistema de Talismanes / Charms.** Aparece como contenido *core* en las guías de Blood Wave (Icy Veins) y Bone Spear (Maxroll) de la S14, pero **no he encontrado una fuente que diga si requiere expansión o viene con el juego base**. Dado que aparece junto a Runewords y Mercenarios (ambos 🔒 VoH) y que *Lord of Hatred* trajo "nuevo crafteo con el Cubo Horadrico", **sospecho que es de expansión, pero es sospecha, no dato.** Verificadlo en el juego: si no os aparece la pestaña, es de expansión.
- **Qué parche/temporada introdujo el Loot Filter.** Hay un artículo de mayo de 2026 sobre quejas del filtro, y el decodificador web menciona "Season 13 (también referida como Season 8)" — una inconsistencia de numeración en la propia fuente. **La función existe y funciona en consola; la fecha exacta de introducción no la he podido fijar.**
- **Si el bug de "Hold to Lock Target" + "Cycle Locked Target" se arregló.** Reportado el 22/06/2023 en Xbox, confirmado por otro jugador, **sin respuesta de Blizzard ni nota de parche que lo mencione**. Recomiendo la config que lo evita.
- **La lista completa y literal del menú Controls en consola en 2026.** Ninguna fuente abierta lo enumera exhaustivamente. He compuesto la lista a partir de KontrolFreek, Game8 y los foros; **puede haber opciones nuevas que no aparezcan aquí**.
- **"Skill Toggle Behavior" = "Toggle All" como auto-apuntado.** Lo afirman gamertweak y mmoexp. Las guías de Maxroll/Icy Veins no lo mencionan. Es plausible pero está mal documentado, y el artículo de mmoexp habla claramente en clave PC (rueda del ratón, teclas numpad).
- **Requisito de expansión de las builds C/B menos documentadas** (Golem, Sever, Blood Surge, Blight, AotD, Blood Lance): no abrí sus guías individuales, solo la tier list. Marcados ⚠️.
- **Ausencia de chat global / de comercio.** Lo afirma una fuente secundaria; no verificado en fuente primaria, y podría haber cambiado.
- **Fuentes de fechado dudoso:** ggrecon (mayo 2023), altchar (prelanzamiento), dexerto (nov. 2023), foros de Blizzard (2023-2024), hdrgamer (junio 2023), diablo4.wiki.fextralife (sin fecha). **Los datos de resolución/fps y de esquema de botones son de lanzamiento.** Los doy por vigentes porque ninguna fuente de 2026 los contradice y porque el parche 3.1.3 no toca nada de consola, pero **es una inferencia, no una confirmación.**

### Qué sí está sólidamente fechado en 2026

- Parche **3.1.3, build 73224, 12/08/2026** (news.blizzard.com + Icy Veins): confirmado que **no contiene ningún cambio de consola, mando, rendimiento, gráficos, accesibilidad, UI, cross-play ni loot filter**. Es un parche de bugs de la S14.
- Tier list de nigromante endgame S14 de Maxroll: **29/06/2026**.
- Guías de nigromante S14 de Maxroll: Blood Surge 13/08/2026, AotD 12/08/2026, Bone Spear 12/08/2026, Bone Spirit 12/08/2026, Sever 28/07/2026, Minion 22/07/2026, Blood Wave 17/07/2026, Blight 11/07/2026, Golem 09/07/2026, Blood Lance 29/06/2026.
- Blood Wave necro de Icy Veins: **27/06/2026**.
- Descripciones de Solo Self-Found de la S14: **01/06/2026**.

---

## Fuentes

Páginas realmente abiertas con WebFetch:

- https://game8.co/games/Diablo-4/archives/413979 — Best Settings for Console
- https://game8.co/games/Diablo-4/archives/413362 — List of Controls (mapeo PS/Xbox)
- https://www.kontrolfreek.com/blogs/kfb/diablo-iv-best-controller-upgrades-and-settings — ajustes de mando y remapeo
- https://us.forums.blizzard.com/en/d4/t/hold-to-lock-target-feature-breaks-when-use-right-stick-to-cycle-locked-target-is-enabled/60846 — bug de target lock
- https://us.forums.blizzard.com/en/d4/t/ray-tracing-kills-performance-on-xbox-series-x/155437 — Enhanced Visuals y 30 fps en Series X
- https://www.purexbox.com/news/2024/03/diablo-4-adds-console-ray-tracing-ahead-of-xbox-game-pass-debut — parche 1.3.5, ray tracing en consola
- https://www.altchar.com/game-news/diablo-4-xbox-series-x-and-s-performance-modes-explained-aXp9s2R2J2Qa — objetivos Series X/S
- https://www.ggrecon.com/guides/diablo-4-console-performance/ — resoluciones y fps por plataforma
- https://www.hdrgamer.com/2023/06/diablo-iv-hdr-settings.html — sliders HDR y problema de niveles de negro
- https://seekingtech.com/how-to-fix-diablo-iv-brightness-issues-on-ps5-xbox-series-x-and-s/ — rutas de calibración PS5/Xbox
- https://www.icy-veins.com/d4/news/hell-welcomes-all-diablo-ivs-accessibility-journey-two-years-on/ — accesibilidad
- https://www.icy-veins.com/d4/news/how-to-make-diablo-4-even-better-7-hidden-things-you-should-do/ — ajustes ocultos
- https://www.shacknews.com/article/135766/diablo-4-settings-pc-console-accessibility — font scale, character highlight, tooltips
- https://www.d4lootfilter.com/ — limitación del loot filter en consola y workaround
- https://www.dexerto.com/diablo/diablo-4-console-players-long-trading-times-solution-2396412/ — trading en consola
- https://www.denofgeek.com/games/diablo-4-cross-play-cross-progression-explained/ — cross-play/cross-progression
- https://www.pcgamesn.com/diablo-4/cross-progression — cross-progression
- https://www.diabloz.net/2026/06/diablo-4-solo-self-found-not-fully-alone-season-14.html — restricciones SSF S14
- https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes — notas oficiales 3.1.3
- https://www.icy-veins.com/d4/news/diablo-4-3-1-3-patch-notes-easier-season-objectives-and-echo-of-mephisto-portal-fix/ — 3.1.3
- https://maxroll.gg/d4/tierlists/necromancer-endgame-tier-list — tier list S14
- https://maxroll.gg/d4/build-guides/necromancer — índice de builds S14 con fechas
- https://maxroll.gg/d4/build-guides/minion-necromancer-guide — Minion endgame (mercenarios 🔒, auto-target)
- https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide — Minion leveling (base vs expansión)
- https://maxroll.gg/d4/build-guides/bone-spear-necromancer-guide — Bone Spear (talismanes, mercenarios)
- https://www.icy-veins.com/d4/guides/blood-wave-necromancer-build/ — Blood Wave (runewords 🔒)
- https://fextralife.com/the-new-necromancer-in-diablo-4-vessel-of-hatred-patch-2-0/ — contenido 🔒 de nigromante en VoH
- https://en.wikipedia.org/wiki/Diablo_IV:_Lord_of_Hatred — contenido de Lord of Hatred
- https://diablo4.wiki.fextralife.com/Controls — controles (solo devolvió PC)
- https://skycoach.gg/blog/diablo-4/articles/best-diablo-4-settings — verificado que NO tiene contenido de consola
- https://www.mmoexp.com/News/diablo-4-gameplay-essential-control-settings-and-tricks.html — Skill Toggle Behavior (⚠️ enfoque PC)

**No accesibles (HTTP 403/404), citadas solo como indicio:**
- https://nerdburglars.net/diablo-4-ps5-pro-performance-is-the-upgrade-worth-it/ (403)
- https://www.gamespot.com/articles/diablo-4-cross-play-cross-progression-and-co-op-explained/1100-6514684/ (403)
- https://dotesports.com/diablo/news/how-to-use-loot-filter-in-diablo-4 (403)
- https://maxroll.gg/d4/resources/talismans (404)
- https://www.wowhead.com/diablo-4/guide/talisman-charms-system (404)
