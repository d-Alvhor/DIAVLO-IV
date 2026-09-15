# Brujo (Warlock) — mecánica interna

> Investigado el 15 sep 2026, el mismo día del lanzamiento de la Temporada 15 "Legado del Infierno"
> (parche 3.2.1, build #73552). **Ninguna guía de mecánica del Brujo existente está escrita sobre el
> 3.2.1.** Todas las páginas de mecánica que hay (Maxroll, Icy Veins) están fechadas entre marzo y
> agosto de 2026 y describen la Temporada 14 o el RPP 3.2.0. Lo único 3.2.1 que existe hoy son las
> notas del parche. Eso condiciona TODO lo que sigue y está marcado dato a dato.

---

## Resumen (5 líneas)

1. El Brujo tiene **dos recursos**: **Ira** (Wrath) para su magia destructiva y **Dominio** (Dominance) para invocar y comandar demonios; se gastan en habilidades distintas y se generan de forma distinta.
2. Su mecánica de clase son los **Fragmentos de Alma** (nivel 30): eliges uno de cuatro y quedas atado a un **Demonio Mayor** — Ae'grom, Abodian, Laalish o Vollach — cada uno con un par *Invocar X* / *Comandar X*.
3. Las habilidades **Archifiendo** son la categoría que explota a esos demonios mayores; entrar en **Forma demoníaca** cambia tu barra a las variantes Archifiendo de Forma demoníaca.
4. **Metamorfosis** es la Definitiva que te mete en Forma demoníaca de forma sostenida y te sustituye la barra entera; tiene tres variantes de demonio: **Pecado**, **Destrucción** y **Terror**.
5. **El cambio clave del 3.2.1**: la variante **Pecado** se ha rediseñado de arriba abajo — se ha eliminado el sistema de acumular cargas dentro de la forma para gastarlas fuera, y se ha sustituido por un aumento del 50% a los máximos de recursos *dentro* de la forma más daño por cada demonio invocado activo. Es el recorte estructural del parche, no un simple ajuste de número.

---

## Hallazgos

### 1. Los dos recursos: Ira y Dominio

| Dato | Cifra | Fuente | Fecha página | Evidencia |
|---|---|---|---|---|
| El Brujo usa dos recursos en vez de uno: Ira y Dominio | — | https://maxroll.gg/d4/getting-started/warlock-class-overview ("Skills are empowered by two different Resources, Wrath and Dominance") | 18 jul 2026 (S14) | corroborado |
| La Ira es el recurso de la magia destructiva; el Dominio se gasta en invocar demonios y activar sus habilidades | — | https://www.icy-veins.com/d4/news/diablo-4s-warlock-uses-two-resources-instead-of-one/ ("Wrath is used for the Warlock's destructive magic. Dominance is spent on summoning demons and activating their abilities") | sin fecha en la página | unica |
| Las habilidades **Básicas** son de coste cero y su función es **generar Ira** | 10 de Ira por lanzamiento | https://www.icy-veins.com/d4/guides/warlock-skills/ | 26 jun 2026 (Temporada 14) | unica |
| Las habilidades **Principales** (Core) **gastan Ira** | 30–35 de Ira | https://www.icy-veins.com/d4/guides/warlock-skills/ — Bombardeo 30, Fractura infernal 35, Cadenas umbrías 35, Garras pavorosas 30, Grito llameante 35 | 26 jun 2026 (S14) | unica |
| Las habilidades **Archifiendo** **gastan Dominio** | 7–10 de Dominio: Desenfreno 10, Aliento infernal 10, Garra del tirano 7, Centinela profano 10 | https://www.icy-veins.com/d4/guides/warlock-skills/ | 26 jun 2026 (S14) | unica |
| El Dominio **se regenera solo, despacio**, y hay muy pocos modificadores (reducir coste o aumentar generación) | sin cifra publicada | https://maxroll.gg/d4/build-guides/minion-warlock-leveling-guide (vía resultado de búsqueda: "Baseline this resource will slowly regenerate over time with a very limited selection of modifiers") | S14 | unica |
| *Comandar a los caídos* ayuda a generar Dominio | sin cifra | https://maxroll.gg/d4/getting-started/warlock-class-overview ("Command Fallen can help to generate Dominance") | 18 jul 2026 (S14) | unica |
| El ataque básico que da Metamorfosis **genera Dominio** | **2 → 5** (subida del 3.2.1) | https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy — "Basic Skill Dominance Generation increased from 2 to 5" | 15 sep 2026 (3.2.1 Build #73552) | oficial |

**Lectura para el jugador:** el bucle real es doble. La Ira funciona como el recurso clásico de D4 (Básica genera, Principal gasta). El Dominio NO: no se genera pegando, se regenera con el tiempo y con un puñado de fuentes concretas. Por eso las guías de mascotas insisten en *no vaciar la barra de Dominio* — el Dominio es la economía de tus demonios, y quedarte a cero apaga la mitad de la clase. Una guía de Maxroll de S14 llega a decir literalmente que mantengas "más del 80% de tu Dominio" (https://maxroll.gg/d4/build-guides/minion-warlock-guide, 13 jul 2026, evidencia: unica).

**Sin cifra publicada:** el **máximo base de Ira** y el **máximo base de Dominio**. Ninguna fuente no vetada los da por escrito (ver Huecos).

---

### 2. La mecánica de clase: Fragmentos de Alma y Pactos Demoníacos

Al nivel 30 eliges uno de **cuatro Fragmentos de Alma**; cada uno te ata a un **Demonio Mayor** y te da un pasivo que cambia el estilo de juego.
Fuente: https://maxroll.gg/d4/news/master-hell-itself-with-the-warlock, 7 mar 2026 — evidencia: unica.

| Fragmento | Demonio Mayor atado | Texto del pasivo (literal, inglés) | Evidencia |
|---|---|---|---|
| **Legión** (Legion Shard) | **Ae'grom** | "Casting a Greater Demon Skill increases Lesser Demon Skill Cast Rate by 25% and Cooldown Rate by 20% for 10 seconds." | unica — https://maxroll.gg/d4/getting-started/warlock-class-overview, 18 jul 2026 |
| **Vanguardia** (Vanguard Shard) | **Abodian** | "While in Demonform, Casting Archfiend Skills additionally Summons the Archfiend Demon." | unica — misma URL/fecha |
| **Cerebro** (Mastermind Shard) | **Laalish** | "Recast Skills no longer break Shadowform Stealth at the cost of 2 stacks of Shadowform per Cast." | unica — misma URL/fecha |
| **Ritualista** (Ritualist Shard) | **Vollach** / **Valloch** | "Occult Skills deal x4% increased damage per 1 stack of Overpower and gain 10% increased Size per 2 stacks." | unica — misma URL/fecha |

Los nombres de los cuatro demonios mayores **están confirmados en español por Blizzard**: "Ae'grom", "Abodian", "Laalish", "Vollach" aparecen tal cual en las notas del parche en español (https://news.blizzard.com/es-es/article/24287406/notas-del-parche-de-diablo-iv — evidencia: oficial). Ojo: el mismo nombre aparece escrito **"Vollach"** y **"Valloch"** según la fuente (ver Contradicciones).

**Los nombres de los fragmentos en español no los he encontrado escritos.** "Legión / Vanguardia / Cerebro / Ritualista" son traducción mía, no texto del juego — marcado como tal.

---

### 3. Demonios Mayores, Demonios Menores y el sistema Comandar

El patrón es de **dos piezas por demonio**: una habilidad **Invocar X** que lo trae y cuesta Dominio, y una habilidad **Comandar X** que le da una orden/ataque especial.

| Dato | Fuente | Fecha | Evidencia |
|---|---|---|---|
| El Dominio "se usa específicamente para invocar Demonios Mayores" | https://maxroll.gg/d4/getting-started/warlock-class-overview | 18 jul 2026 | unica |
| **Invocar a Valloch: coste reducido de 10 a 5 de Dominio** | https://news.blizzard.com/en-us/article/24295394/... (3.2.1) | 15 sep 2026 | oficial |
| **Comandar a Abodian**: daño base del mordisco **155% → 245%**; Abodian pasa a ser "Imperturbable" (Unhindered) por los enemigos y prioriza Élites y objetivos de alta prioridad Cercanos | https://news.blizzard.com/en-us/article/24295394/... (3.2.1) | 15 sep 2026 | oficial |
| **Comandar a Ae'grom**: Ae'grom pasa a ser Imperturbable y prioriza Élites y objetivos de alta prioridad Próximos | https://news.blizzard.com/en-us/article/24295394/... (3.2.1) | 15 sep 2026 | oficial |
| **Comandar a Laalish** (vía el único *Rictus of Terror*) pasa a **contar como habilidad Definitiva** e inflige 100–120% de daño aumentado | https://news.blizzard.com/en-us/article/24295394/... (3.2.1) | 15 sep 2026 | oficial |
| Existen **Demonios Menores** (Lesser Demons) como categoría separada; el Fragmento de Legión los acelera al lanzar una habilidad de Demonio Mayor | https://maxroll.gg/d4/getting-started/warlock-class-overview | 18 jul 2026 | unica |
| El Fragmento de Legión invoca "Vile Child" (crías) como Demonios Menores | https://maxroll.gg/d4/news/master-hell-itself-with-the-warlock | 7 mar 2026 | unica |

**Lectura para el jugador:** "Demonio Mayor" y "Demonio Menor" no son sabor: son **etiquetas de habilidad** que otras cosas leen. El Fragmento de Legión es literalmente "lanza Mayor → acelera Menores". Y en el 3.2.1 Blizzard ha metido mano precisamente a esas etiquetas (siguiente apartado), lo que significa que builds que antes no disparaban un efecto ahora sí.

---

### 4. Habilidades Archifiendo: qué son y en qué se diferencian

| Dato | Fuente | Fecha | Evidencia |
|---|---|---|---|
| "La categoría Archifiendo te da la capacidad de explotar el poder de tus demonios mayores" (literal inglés: "Archfiend category provides the ability to exploit the power of your greater demons") | https://www.icy-veins.com/d4/guides/warlock-skills/ | 26 jun 2026 (S14) | corroborado (también en https://diablo4.wiki.fextralife.com — VETADA para valores, citada solo como eco de nomenclatura) |
| Las cuatro Archifiendo base: **Desenfreno** (Rampage), **Aliento infernal** (Infernal Breath), **Garra del tirano** (Tyrant's Grasp), **Centinela profano** (Profane Sentinel) | https://www.icy-veins.com/d4/guides/warlock-skills/ | 26 jun 2026 | corroborado (Icy Veins + Maxroll class overview) |
| Qué hace cada una: Desenfreno invoca un bruto que te sigue y golpea; Aliento infernal invoca una cabeza demoníaca que orbita y escupe llamas; Garra del tirano invoca manos demoníacas adicionales; Centinela profano invoca un ojo que te sigue y dispara | https://www.icy-veins.com/d4/news/diablo-4s-warlock-class-lets-you-command-hell-itself/ | sin fecha en la página | unica |
| **Gastan Dominio, no Ira** (7–10) | https://www.icy-veins.com/d4/guides/warlock-skills/ | 26 jun 2026 | unica |
| Lanzar Archifiendo **estando en Forma demoníaca** puede invocar Demonios Mayores adicionales y **cambia el comportamiento de toda tu barra** | https://maxroll.gg/d4/getting-started/warlock-class-overview | 18 jul 2026 | unica |
| Las **variantes Archifiendo de Forma demoníaca** son habilidades **Principales** y **cuestan Ira** | https://www.icy-veins.com/d4/news/can-the-warlock-stay-in-demon-form-forever-in-diablo-4/ ("Archfiend Demonform Skill Variants are Core Skills and cost Wrath") | marzo 2026 | unica |

**La diferencia que importa:** una Archifiendo **fuera** de Forma demoníaca es una invocación que cuesta **Dominio**. La misma ranura **dentro** de Forma demoníaca se convierte en su variante de Forma demoníaca, que es una habilidad **Principal** y cuesta **Ira**. Es decir: entrar en Forma demoníaca **cambia qué recurso paga tu barra**. Esto es, con diferencia, lo menos intuitivo de la clase y es exactamente donde el 3.2.1 ha metido el bisturí.

---

### 5. Forma demoníaca (Demonform)

| Dato | Cifra | Fuente | Fecha | Evidencia |
|---|---|---|---|---|
| Texto de la palabra clave: aumenta tu Vida Máxima y, mientras está activa, las muertes aumentan el daño de habilidades de Demonología | **+25% Vida Máxima**; **+1% por muerte hasta +100%** a Demonología | https://maxroll.gg/d4/getting-started/warlock-class-overview ("Increases your Maximum Life by 25%. While active, kills increase the damage of Demonology Skills by 1% up to 100%") | 18 jul 2026 (S14) | corroborado (Maxroll class overview + Maxroll reveal 7 mar 2026) |
| Estando en Forma demoníaca **pierdes 1 de Dominio por segundo por cada Demonio Mayor invocado Cercano**, para extender su duración | 1/s por demonio | https://maxroll.gg/d4/build-guides/minion-warlock-guide (vía resultado de búsqueda) | 13 jul 2026 (S14) | unica |
| Forma demoníaca aumenta el daño de habilidades de **Demonología de Fuego infernal** | **x30%** | https://maxroll.gg/d4/build-guides/minion-warlock-guide (vía resultado de búsqueda) | 13 jul 2026 (S14) | unica |
| La mayoría de variantes de Forma demoníaca son **temporales, de pocos segundos**; se encadenan con la build adecuada | — | https://www.icy-veins.com/d4/news/can-the-warlock-stay-in-demon-form-forever-in-diablo-4/ | marzo 2026 | unica |
| **Metamorfosis es la excepción**: permite estar transformado de forma permanente/sostenida | — | misma URL | marzo 2026 | unica |

**El drenaje de 1 Dominio/s por demonio es la clave económica de la clase** y explica por qué el 3.2.1 toca los máximos de Dominio (siguiente apartado): si tu forma demoníaca te está sangrando Dominio por cada demonio vivo, subir el techo de Dominio es literalmente subir cuánto tiempo aguantas con la banda entera desplegada. **Esta lectura es mía, no de una fuente** — la marco como interpretación.

---

### 6. Metamorfosis y sus tres variantes de demonio

Texto base (datamine, https://www.wowhead.com/diablo-4/skill/metamorphosis-2215096, sin fecha de página — evidencia: unica):

> "Transform into a demon and gain: Demonform, All Archfiend Demonform Skill Variants, An Ultimate Archfiend Basic attack that deals 65% damage and generates 2 Dominance."

Icy Veins da una redacción algo distinta del mismo texto (https://www.icy-veins.com/d4/guides/warlock-skills/, 26 jun 2026): "Transform into a demon and gain: Demonform, All Archfiend Demonform Skill variants, A special melee Basic attack that deals 137% damage." — **los dos números del ataque básico no coinciden** (ver Contradicciones).

Lo que sí está **corroborado por las dos** y por las notas oficiales: Metamorfosis (a) te da Forma demoníaca, (b) te sustituye la barra por las variantes Archifiendo de Forma demoníaca, y (c) te da un ataque básico propio que **genera Dominio** — y ese generador **sube de 2 a 5 en el 3.2.1** (oficial).

Las **tres variantes de demonio** (son mejoras/upgrades de Metamorfosis, se elige una):

| Variante (EN) | Variante (ES) | Qué hace | Fuente | Evidencia |
|---|---|---|---|---|
| **Sin Demon** | **Demonio del pecado** *(traducción no confirmada)* | Ver apartado 7 — rediseñada por completo en el 3.2.1 | oficial 3.2.1 | oficial |
| **Destruction Demon** | **Demonio de la destrucción** | Otorga **Volatilidad**; las habilidades de Fuego infernal aumentan el daño pero te queman | https://news.blizzard.com/es-es/article/24287406/... (nombre ES, oficial) + https://www.wowhead.com/diablo-4/skill/metamorphosis-2215096 (efecto, unica) | nombre ES: oficial / efecto: unica |
| **Terror Demon** | **Demonio del terror** *(traducción no confirmada)* | Metamorfosis pasa a ser habilidad de **Abismo** que dura 15 s; otorga cargas de **Forma sombría** y mantiene el Sigilo | https://www.wowhead.com/diablo-4/skill/metamorphosis-2215096 | unica |

Cambio del 3.2.1 a la variante de Destrucción (oficial, https://news.blizzard.com/en-us/article/24295394/...):
> "Now applies burning when any type of Skill is cast. Bonus to Hellfire Skills increased from 4% to 6%."
Traducido: ahora aplica quemadura al lanzar **cualquier tipo** de habilidad (antes solo algunas), y el bonus a habilidades de Fuego infernal sube de 4% a 6%.

---

### 7. **EL CAMBIO CLAVE DEL 3.2.1 — Pecado (Sin) y Metamorfosis, antes y después**

Fuente de los dos textos: notas del parche **3.2.1 Build #73552, 15 sep 2026**, incrustadas en
https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy
Espejo (idéntico) en https://maxroll.gg/d4/news/diablo-4-3-2-1-patch-notes, publicado 12 sep 2026.
**Evidencia: oficial.**

#### ANTES (S14 y RPP 3.2.0) — literal, inglés

> **Previous:** "Casting Archfiend Skills during Metamorphosis grants Sin, up to 20 Stacks. When you leave Metamorphosis, each Sin can be consumed by Casting Non-Archfiend Skills to generate 3 Dominance and Wrath. This can exceed up to 50% of your Maximum Resource Values."

Traducción: *"Lanzar habilidades Archifiendo durante Metamorfosis otorga Pecado, hasta 20 cargas. Al salir de Metamorfosis, cada Pecado puede consumirse lanzando habilidades No-Archifiendo para generar 3 de Dominio y de Ira. Esto puede exceder hasta un 50% tus valores máximos de recurso."*

#### AHORA (3.2.1) — literal, inglés

> **Now:** "During Metamorphosis your Maximum Wrath and Dominance are increased by 50% and you deal 5% (scaled up per Rank) increased damage for each Demon Summon you have active. When you leave Metamorphosis, casting Summon Skills reduces its Cooldown by 2 seconds."

Traducción: *"Durante Metamorfosis, tu Ira y Dominio máximos aumentan un 50% e infliges un 5% de daño aumentado (escala por rango) por cada Invocación de Demonio que tengas activa. Al salir de Metamorfosis, lanzar habilidades de Invocación reduce su Reutilización en 2 segundos."*

#### Explicado para alguien que nunca vio el sistema viejo

**Cómo funcionaba antes.** Metamorfosis era una Definitiva que te transformaba en demonio. Dentro de la forma, tu barra pasaba a variantes Archifiendo. Si habías elegido la variante **Pecado**, cada vez que lanzabas una habilidad Archifiendo **dentro** de la forma, guardabas una carga de "Pecado" — hasta 20. Las cargas **no hacían nada mientras estabas dentro**: eran una hucha. En el momento de **salir** de la forma, empezabas a lanzar habilidades **No-Archifiendo**, y cada lanzamiento consumía una carga de Pecado y te devolvía **3 de Dominio + 3 de Ira**. Y lo importante: ese relleno **podía pasarse de tu máximo hasta un +50%**. No te llenaba la barra: te la **desbordaba**.

Es decir, el bucle era: *entra en forma demoníaca → carga la hucha con Archifiendo → sal → vacía la hucha con No-Archifiendo y quédate con los recursos por encima del tope → usa esos recursos desbordados en la ventana de burst.*

**Por qué Blizzard lo mató.** Porque el juego tiene escalares que leen **cuánto recurso tienes**, no cuánto gastas. El nodo legendario **Dynamism** da daño **por Dominio**. Con el Pecado viejo podías tener un 150% de tu Dominio máximo durante la ventana de burst y multiplicar ese escalar por encima de lo diseñado. La nota del desarrollador lo dice sin rodeos (oficial):

> "In particular, the Overwhelming Aspect was scaling up too much and **Metamorphosis was interacting with several stacking mechanics in unintended ways**."

Y hay un bug de la misma familia arreglado en el mismo parche (oficial): *"Fixed an issue where Melted Heart of Selig could cause Warlock Wrath values to increase beyond intended limits when used with Metamorphosis."* — el Corazón Fundido de Selig convierte Vida en Ira, y con el desbordamiento de Pecado se iba de madre.

**Cómo funciona ahora.** No hay huchas, no hay cargas, no hay desbordamiento. La variante Pecado hace dos cosas completamente distintas:

1. **Dentro de la forma:** tu **techo** de Ira y de Dominio sube un 50%. Ojo a la diferencia: antes te *rellenaba por encima del techo*, ahora te *sube el techo*. Ya no puedes estar al 150%; puedes estar al 100% de un depósito un 50% más grande. Y ese depósito más grande solo existe mientras estás transformado.
2. **Dentro de la forma, además:** **+5% de daño por cada Invocación de Demonio activa** (escala con el rango de la habilidad). Esto es nuevo y cambia el objetivo de la variante: ya no premia lanzar Archifiendo, premia **tener demonios vivos a la vez**.
3. **Fuera de la forma:** cada habilidad con etiqueta **Invocación** que lanzas recorta **2 segundos** de la reutilización de Metamorfosis. O sea, el juego fuera de la forma ya no es "vacía la hucha", es "**acorta el camino de vuelta**".

**Qué significa esto en la práctica (interpretación mía, no de una fuente):** la variante Pecado ha pasado de ser un **motor de recursos con ventana de burst** a ser un **amplificador de invocador con motor de uptime**. El eje ya no es Archifiendo, es **Invocación**. Y eso encaja exactamente con el otro bloque de cambios del parche: el 3.2.1 ha ido **añadiendo la etiqueta Invocación a cosas que antes no la tenían** (apartado 8). Quien monte Brujo de Metamorfosis en S15 debería contar cuántas etiquetas Invocación lleva en la barra, no cuántas Archifiendo.

#### Nota del desarrollador sobre el Brujo — literal y completa (oficial, 3.2.1)

> "Warlock is performing well with many of their newly improved options. These updates focus on maintaining momentum and build diversity while pruning unintuitive or oppressive scalars. In particular, the Overwhelming Aspect was scaling up too much and Metamorphosis was interacting with several stacking mechanics in unintended ways. Along with this, we are adjusting the power of all Ultimate Skills to account for previous updates or offer alternative build options. **We are also looking to redistribute power out of Demonform**, starting with changes to the Dynamism Legendary Paragon Node, while mechanical improvements and skill tag additions for several primary attacks have been made to increase or maintain their baseline potency."

La frase "queremos **redistribuir el poder fuera de la Forma demoníaca**" es la tesis del parche para esta clase, y explica el siguiente apartado.

---

### 8. Las etiquetas de habilidad y lo que el 3.2.1 les hace

Las etiquetas del Brujo que aparecen citadas: **Fuego infernal** (Hellfire), **Archifiendo** (Archfiend), **Invocación** (Summon), **Demonología** (Demonology), **Abismo** (Abyss), **Esotérico/Oculto** (Occult), **Demonio Mayor** (Greater Demon), **Demonio Menor** (Lesser Demon), **Sigilo** (Sigil). Todas menos "Demonio Mayor/Menor" están confirmadas en español en las notas oficiales es-es (https://news.blizzard.com/es-es/article/24287406/... — evidencia: oficial; "Occult" aparece como **"habilidades esotéricas"**).

**Reetiquetados del 3.2.1** (oficial, https://news.blizzard.com/en-us/article/24295394/..., 15 sep 2026). Esto es un cambio de mecánica disfrazado de letra pequeña:

| Habilidad | Etiqueta que gana |
|---|---|
| **Bombardeo** (Bombardment), habilidad base | pasa a ser **habilidad de Invocación** |
| **Comandar a Abodian** y su ataque básico | pasan a ser **habilidades de Invocación** |
| **Garras pavorosas** (Dread Claws), base | pasa a ser **habilidad de Demonio Mayor** |
| **Aguijón daemónico** (Hellion Sting), base | pasa a ser **habilidad de Demonio Menor**; su variante *Demonic Swipe* pasa a **Archifiendo de Demonio Mayor** |
| **Prisión oscura** (Dark Prison), variante *Calamity* | pasa a contar además como **habilidad de Sigilo** |
| **Doomfire**, variante *Ritual* (estallido) | pasa a contar como **lanzamiento de habilidad de Sigilo** |
| **Grito llameante** (Blazing Scream), vía el único *Elegy* | pasa a ser **habilidad Archifiendo** |

**Por qué importa, unido al apartado 7:** la nueva variante Pecado premia (a) tener muchas Invocaciones de Demonio activas y (b) lanzar habilidades de **Invocación** fuera de la forma para recortar la reutilización. Y este parche acaba de convertir **Bombardeo** — una Principal de 30 de Ira, o sea algo que lanzas sin parar — en habilidad de Invocación. Igual con Comandar a Abodian. Eso no es cosmético: es el carril que Blizzard ha abierto para compensar el recorte. *(Conexión mía entre dos hechos oficiales, no afirmada por ninguna fuente.)*

---

### 9. Otros cambios 3.2.1 que tocan la mecánica interna (no la numerología de builds)

Todos oficiales, https://news.blizzard.com/en-us/article/24295394/..., 15 sep 2026.

- **Nodo legendario Dynamism (Paragón):** "Now also grants **85% increased Summon Skill damage while not in Demonform**. Damage per Dominance while in Demonform **reduced from 3% to 2.5%**." — Esta es la "redistribución fuera de la Forma demoníaca" en una sola línea: te quitan escalar dentro y te lo dan fuera. Y confirma que **Dynamism lee tu Dominio actual**, que es exactamente el escalar que el Pecado viejo desbordaba.
- **Aspecto Abrumador (Overwhelming Aspect):** *Previous:* "Each hit against Elite enemies deals 80-120%[x] increased damage but requires and consumes 4 stacks of Overpower." → *Now:* "Occult Skills deal 5-7% increased damage against Elite enemies per stack of Overpower. This bonus is doubled if the enemy is Hexed." (fuente del par completo: https://maxroll.gg/d4/news/diablo-4-3-2-1-patch-notes, 12 sep 2026 — evidencia: corroborado con la nota oficial que lo cita como el escalar que "escalaba demasiado").
- **Metamorfosis, saneamientos:** "Skills can no longer remain or become Volatile when they are swapped off the skill bar." / arreglo de *Melted Heart of Selig* + Ira ilimitada / arreglo de Sigilo de caos quitando Volatilidad a la variante Demonio de la destrucción / el contador de la mejora de Aturdimiento de Metamorfosis ahora se muestra en la barra y **solo los efectos de Incapacitación cuentan para él**.
- **Comandar a Laalish** (vía *Rictus of Terror*) pasa a **contar como Definitiva** — relevante porque todo lo que busca "habilidades Definitivas" ahora lo ve.
- **Invocar a Valloch:** coste **10 → 5 de Dominio**.
- **Mejoras de Demonio Menor de Archifiendo:** "Archfiend Lesser Demon Upgrades now function with Recasts" (esto venía ya del RPP 3.2.0, https://news.blizzard.com/en-us/article/24292852/the-3-2-0-ptr-what-you-need-to-know — evidencia: oficial).

---

### 10. Glosario español ↔ inglés (para jugar en español)

Confirmados en texto oficial en español (https://news.blizzard.com/es-es/article/24287406/notas-del-parche-de-diablo-iv — **oficial**):

| Español (oficial) | Inglés |
|---|---|
| Ira | Wrath |
| Dominio | Dominance |
| Forma demoníaca | Demonform |
| Metamorfosis | Metamorphosis |
| Demonio de la destrucción | Destruction Demon |
| Archifiendo | Archfiend |
| Invocación | Summon |
| Fuego infernal | Hellfire |
| Demonología | Demonology |
| Abismo | Abyss |
| (habilidades) esotéricas | Occult |
| Comandar a los caídos | Command Fallen |
| Comandar a Valloch | Command Valloch |
| Grito llameante | Blazing Scream |
| Garras pavorosas | Dread Claws |
| Aguijón daemónico | Hellion Sting |
| Bombardeo | Bombardment |
| Cadenas umbrías | Umbral Chains |
| Fractura infernal | Hell Fracture |
| Muro de agonía | Wall of Agony |
| Paso abisal | Nether Step |
| Desenfreno | Rampage |
| Aliento infernal | Infernal Breath |
| Centinela profano | Profane Sentinel |
| Enjambre terrorífico | Terror Swarm |
| Apocalipsis | Apocalypse |
| Sigilo de caos / Sigilo desestabilizador / Sigilo de invocación | Sigil of Chaos / Sigil of Subversion / Sigil of Summons |
| Ae'grom, Abodian, Laalish, Vollach | (iguales) |

**Traducciones mías, NO confirmadas en el juego** (marcadas como tales): Demonio del pecado (Sin Demon), Demonio del terror (Terror Demon), Garra del tirano (Tyrant's Grasp), Prisión oscura (Dark Prison), Desdichado torturado (Tortured Wretch), Fragmento de Alma (Soul Shard), Demonio Mayor / Demonio Menor (Greater / Lesser Demon), Volatilidad (Volatility), Forma sombría (Shadowform), Aspecto Abrumador (Overwhelming Aspect).

---

## Huecos

1. **Máximo base de Ira y de Dominio.** No lo da por escrito ninguna fuente no vetada. Importa mucho ahora, porque el nuevo Pecado sube ambos un 50% y no sabemos sobre qué base. **Se resuelve en 30 segundos en la pantalla del jugador** en cuanto entre al juego: mirar la barra de recursos con el personaje creado.
2. **Regeneración base de Dominio por segundo.** Solo tengo "se regenera despacio" cualitativo. Sin cifra.
3. **El drenaje de Forma demoníaca (1 Dominio/s por Demonio Mayor Cercano) no está verificado para 3.2.1.** Viene de una guía de S14 del 13 jul 2026. Si el parche lo tocó, no lo he visto escrito. **Verificar en pantalla.**
4. **Texto literal completo de la variante Pecado ya en juego.** Tengo el "Now" de las notas del parche, pero no el tooltip final en español dentro del cliente. La nota dice "5% (scaled up per Rank)" sin dar la progresión por rango: **no sé cuánto es a rango 5 o con rangos de equipo.**
5. **Nombre oficial en español de la variante "Sin"/"Pecado" y de la variante "Terror".** Las notas en español todavía no cubren el 3.2.1 (ver contradicción 4) y en las de 3.1.x no aparecen. "Demonio del pecado" es traducción mía.
6. **Qué cuenta exactamente como "Demon Summon activa"** para el +5% del nuevo Pecado: ¿solo Demonios Mayores? ¿también Menores? ¿mercenarios? Las notas arreglan un bug adyacente ("los rasgos de ímpetu y de misantropía trataban a mascotas y mercenarios como demonios activos" — es-es, 3.1.x), lo que sugiere que la distinción es delicada y que **mascotas y mercenarios NO cuentan**. Pero eso es sobre otros rasgos, no sobre Pecado. **Sin confirmar.**
7. **Reutilización real de Metamorfosis.** Ver contradicción 1.
8. **Ninguna guía de mecánica del Brujo posterior al 15 sep 2026 existe todavía.** Maxroll (18 jul), Icy Veins (26 jun), reveal (7 mar). Cero fuentes describen la clase *tal como es ahora*. Todo lo estructural de los apartados 1–6 hay que darlo por "válido salvo que el parche lo cambiara", y el parche cambió cosas.

---

## Contradicciones

1. **Reutilización de Metamorfosis: 5 s vs 15 s.**
   - Icy Veins, 26 jun 2026 (S14): "Cooldown: 5 seconds." — https://www.icy-veins.com/d4/guides/warlock-skills/
   - Wowhead (datamine, sin fecha): "Cooldown: 15 seconds." — https://www.wowhead.com/diablo-4/skill/metamorphosis-2215096
   - Icy Veins da además 30 s a Enjambre terrorífico, 66,6 s a Apocalipsis y 60 s a Fiendo de Abaddon, lo que hace que 5 s para Metamorfosis chirríe mucho.
   - **Evidencia: disputa.** Y ahora importa más que nunca: la nueva variante Pecado recorta 2 s de reutilización por cada habilidad de Invocación lanzada, y ese recorte significa cosas muy distintas sobre 5 s que sobre 15 s. **A confirmar en pantalla.**

2. **Daño del ataque básico de Metamorfosis: 65% vs 137%.**
   - Wowhead (datamine): "an Ultimate Archfiend Basic attack that deals 65% damage and generates 2 Dominance."
   - Icy Veins, 26 jun 2026: "A special melee Basic attack that deals 137% damage."
   - **Evidencia: disputa.** Lo que sí es oficial es que su generación de Dominio sube de 2 a 5 en 3.2.1, lo que casa con la redacción de Wowhead ("generates 2 Dominance") como estado previo.

3. **Ortografía del cuarto Demonio Mayor: "Vollach" vs "Valloch".**
   - Notas oficiales en español: **"Vollach"** y **"Comandar a Valloch"** — https://news.blizzard.com/es-es/article/24287406/...
   - Notas oficiales en inglés 3.2.1: "Summon **Valloch**: Cost reduced from 10 to 5 Dominance."
   - Maxroll (reveal, 7 mar 2026) escribe **"Vollach"**.
   - **Evidencia: disputa de nomenclatura.** Probablemente la misma criatura con dos transliteraciones; en el cliente español busca **Valloch** en las habilidades y **Vollach** en el fragmento.

4. **Las notas del parche 3.2.1 en español no existían al escribir esto.**
   - La página es-es del anuncio de temporada dice literalmente: *"Puedes consultar las notas completas del parche de la actualización 3.2.1, cuando estén disponibles, aquí."* — https://news.blizzard.com/es-es/article/24295394/...
   - La página es-es de notas del parche (24287406) solo llega hasta **3.1.3 (12 ago 2026)**.
   - **Consecuencia:** todo nombre en español de un cambio *del 3.2.1* que yo dé procede de mapear el término inglés contra el vocabulario español de 3.1.x. Lo he marcado caso por caso.

5. **Hora de lanzamiento.**
   - Maxroll (12 sep 2026) dice "Live Date: September 15, 2026 at 10:00 a.m." — https://maxroll.gg/d4/news/diablo-4-3-2-1-patch-notes
   - El briefing de este encargo dice 16:30 UTC / 18:30 CEST.
   - 10:00 PDT = 17:00 UTC, no 16:30. **Disputa de 30 minutos.** No afecta a la mecánica, pero si el plan del jugador depende de estar conectado al minuto, que lo verifique él.

6. **El estado de la mecánica en todas las guías es pre-parche, y ninguna lo avisa.**
   - Maxroll "Warlock Class Overview" (18 jul 2026) y Minion Warlock (13 jul 2026) **no mencionan el 3.2.1 en absoluto**.
   - Icy Veins "Warlock Skills Guide" (26 jun 2026) está etiquetada **Season 14**.
   - Icy Veins "Warlock Is Suddenly Diablo 4's Best Class" está escrita sobre el **RPP 3.2.0** y ella misma avisa: *"PTR values are almost certainly going to change before the season goes live"*. **Y cambiaron.** Esa página es la fuente del "Brujo es S++" y **ya no describe el juego que sale hoy.**
   - **No es una contradicción entre fuentes: es que todas están en el lado equivocado de la línea del parche.**
