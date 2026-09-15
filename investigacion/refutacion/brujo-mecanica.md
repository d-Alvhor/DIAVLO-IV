# Brujo (Warlock) — mecánica interna · REFUTACIÓN

> Refutación adversarial del informe `investigacion/crudo/brujo-mecanica.md`, hecha el 15 sep 2026.
> He vuelto a abrir **una por una** las páginas que cita el informe y he pedido la cita literal.
> Resultado corto: **la capa oficial del 3.2.1 aguanta entera** (ocho citas comprobadas palabra por
> palabra, cero desviaciones). **La capa de mecánica base no**: hay tres citas que no están en la
> página que se les atribuye, una afirmación marcada "oficial" que es falsa, y dos de los pasos
> accionables se caen con ellas.

---

## Resumen (5 líneas)

1. **Se cae el paso accionable nº2, el de "la trampa de la Forma demoníaca".** La frase que lo sostiene ("Archfiend Demonform Skill Variants are Core Skills and cost Wrath") **no está en la URL que el informe cita**, y donde sí está es **dentro del texto de un objeto único** (*Anathema of the Primes*) — o sea describe lo que el objeto **convierte**, no la regla base de la clase. Es probable que la regla base sea justo la contraria.
2. **Dos cifras de la sección 5 no existen en su fuente.** Ni el drenaje de "1 de Dominio/s por demonio" ni el "x30% a Demonología de Fuego infernal" aparecen en `maxroll.gg/d4/build-guides/minion-warlock-guide`. Venían de un resumen de buscador, no de la página. La **mecánica** del drenaje sí existe (reveal del 7 mar), pero **sin número**.
3. **Es falso que los cuatro demonios estén confirmados en español por Blizzard.** En las notas es-es citadas solo aparecen **Ae'grom** y **Valloch**. "Vollach", "Abodian", "Laalish", "Archifiendo" y "Demonio de la destrucción" **no están en ese documento**. Media tabla del glosario marcada "oficial" no lo es.
4. **"Dynamism lee tu Dominio ACTUAL" está etiquetado oficial y no lo es**: la nota literal del 3.2.1 dice "Damage per Dominance", nunca "current". La palabra "currently" solo la ponen fextralife y game8 — vetada la primera, no preferente la segunda.
5. **El informe se dejó una fuente refechada de manual**: la tier list de Maxroll, **actualizada el 14 sep 2026, etiquetada "Season 15 – Hell's Legacy" y sin una sola mención del 3.2.1**, que pone Minion/Apocalipsis/Lunatic Brujo en tier A. Es exactamente el caso que el encargo manda señalar, y además desmiente el "ninguna fuente posterior existe".

---

## Hallazgos

### A. REFUTADO — La regla de "qué recurso paga tu barra" es texto de un único, mal atribuido

| Qué afirma el informe | Qué he encontrado |
|---|---|
| Línea 87 y paso accionable nº2: *"Las variantes Archifiendo de Forma demoníaca son habilidades Principales y cuestan Ira"*, atribuido a `https://www.icy-veins.com/d4/news/can-the-warlock-stay-in-demon-form-forever-in-diablo-4/` (fecha dada: "marzo 2026") | Abierta esa página el 15 sep 2026: **esa frase no aparece en ella**. Lo que sí contiene, literal: *"most Demon Form variants are temporary and usually only last a few seconds"* y *"The big exception is Metamorphosis, the Warlock's ultimate. In its base version, it lets you swap into Demon Form permanently."* Y **la página no lleva fecha**: el "marzo 2026" es atribuido, no leído. |

**Dónde sí está la frase.** En `https://maxroll.gg/d4/news/master-hell-itself-with-the-warlock` (7 mar 2026), dentro de la descripción del **único *Anathema of the Primes***, texto completo literal:

> "Hitting enemies with a Core Skill increases the damage they take from you per Skill, up to a maximum. **Archfiend Demonform Skill Variants are Core Skills and cost Wrath.**"

Y preguntado expresamente si es efecto del objeto o enunciado general, la página responde que **es parte del efecto concedido por el objeto**. Preguntadas las otras dos fuentes de mecánica por un enunciado general equivalente: `maxroll.gg/.../warlock-class-overview` **no lo tiene**, `icy-veins.com/.../lets-you-command-hell-itself` **no lo tiene**.

**Por qué esto tumba el paso, no lo matiza.** Si hace falta un único para que las variantes Archifiendo de Forma demoníaca *pasen a ser* Principales y *pasen a costar* Ira, lo razonable es que **de base no lo sean** — es decir, que sigan costando Dominio. El informe convirtió un efecto de objeto en la "rareza de la clase" y construyó sobre ella su segundo consejo. Nivel real de ese par valor→efecto: **sinconfirmar**, y el consejo debe retirarse hasta ver el tooltip en pantalla.

*(Corolario: la frase del resumen del informe "una Archifiendo fuera de la forma cuesta Dominio, y su variante de Forma demoníaca es una habilidad Principal que cuesta Ira" pierde su respaldo por completo.)*

---

### B. REFUTADO — Dos cifras de la sección 5 no están en la página que las firma

Ambas están en el informe como "unica" con fuente `https://maxroll.gg/d4/build-guides/minion-warlock-guide`, ambas marcadas por el propio informe como obtenidas "*vía resultado de búsqueda*". Abierta la página (última actualización **13 jul 2026**, etiqueta **"Season 14 – Death Awakening"**, **no menciona 3.2.1**):

| Cifra del informe | Comprobación en la página |
|---|---|
| "pierdes **1 de Dominio por segundo** por cada Demonio Mayor invocado Cercano" | **No aparece.** La página no contiene información sobre pérdida de Dominio por segundo en Forma demoníaca. |
| Forma demoníaca aumenta Demonología de Fuego infernal **x30%** | **No aparece.** La página no da ninguna cifra porcentual para eso. |
| "keep greater than 80% of your Dominance remaining" | **Sí aparece, literal**: *"Drop as many Tortured Wretch as you need to survive, but try to keep greater than 80% of your Dominance remaining."* ✓ El informe cita bien esta. |

**La mecánica del drenaje sí existe — el número no.** El reveal de Maxroll (7 mar 2026) tiene la línea, y está rota/truncada en el propio origen: *"While in Demonform, lose Dominance per second Close Summons Greater Demon to extend their durations."* **Sin cifra.** Corrección: el drenaje pasa a **unica sin valor**; el "1/s" pasa a **no encontrado**. Y con él se cae el párrafo del informe que lo llama "la clave económica de la clase" y lo usa para explicar por qué el parche sube los máximos de Dominio — esa explicación queda sin suelo numérico.

---

### C. REFUTADO — "Los cuatro nombres están confirmados en español por Blizzard" es falso

El informe, línea 54, evidencia **oficial**: *"'Ae'grom', 'Abodian', 'Laalish', 'Vollach' aparecen tal cual en las notas del parche en español"*, URL `https://news.blizzard.com/es-es/article/24287406/notas-del-parche-de-diablo-iv`.

Abierta esa página (cubre hasta **3.1.3, build #73224, 12 ago 2026**; **no cubre 3.2.1** — eso sí lo acierta el informe):

| Término buscado | ¿Está? |
|---|---|
| Ae'grom | **Sí** — "Cisma de Ae'grom"; "Bonus de conjunto de 2 piezas: Bonus de Ae'grom reducido del 15 % al 10 %." |
| Valloch | **Sí** — "Se ha corregido un error que impedía que Valloch se considerara una habilidad esotérica." |
| **Vollach** | **NO** |
| **Abodian** | **NO** |
| **Laalish** | **NO** |
| **Archifiendo** | **NO** |
| **Demonio de la destrucción** | **NO** |

**Consecuencias:**
1. La afirmación "los cuatro demonios mayores están confirmados en español por Blizzard" es **falsa**: solo dos, y uno de ellos con la grafía **Valloch**, no Vollach.
2. La **Contradicción 3** del informe se desmonta por la mitad: dice *"Notas oficiales en español: **'Vollach'** y 'Comandar a Valloch'"*. En es-es solo hay **Valloch**. No hay disputa de grafía dentro del español oficial: la disputa es entre **Maxroll (Vollach)** y **Blizzard (Valloch)**, y gana Blizzard. Consejo corregido para el jugador: **busca "Valloch" en el cliente español, en habilidades y en fragmento**.
3. Del glosario de la sección 10, marcado en bloque "**Confirmados en texto oficial en español**" con esa URL, al menos **"Archifiendo"** y **"Demonio de la destrucción"** no lo están. El resto del glosario no lo he podido verificar entrada por entrada, así que **todo el bloque baja de oficial a sinconfirmar** salvo las que se vuelvan a comprobar de una en una.

---

### D. REFUTADO — "Dynamism lee tu Dominio ACTUAL" no es oficial

El informe lo afirma dos veces (paso accionable nº6 y línea 202) con etiqueta **oficial**: *"Además confirma que Dynamism lee tu Dominio ACTUAL — que es justo el escalar que el Pecado viejo desbordaba."*

Texto oficial 3.2.1, verificado literal **dos veces** (Blizzard `news.blizzard.com/en-us/article/24295394/...` + espejo `maxroll.gg/d4/news/diablo-4-3-2-1-patch-notes`, 12 sep 2026):

> "Now also grants 85% increased Summon Skill damage while not in Demonform. Damage per Dominance while in Demonform reduced from 3% to 2.5%."

**No dice "current".** Dice "per Dominance". La palabra "currently" aparece en las descripciones del nodo base que circulan por **diablo4.wiki.fextralife.com** (vetada) y **game8.co** (no preferente): *"your Demonology Skill damage is increased by 3% for every point of Dominance you currently have"*. O sea: **el único apoyo textual de la afirmación viene de una fuente vetada**. Baja a **sinconfirmar**.

Y con ella cae, de "explicación" a "hipótesis", toda la historia causal del apartado 7 ("por qué Blizzard lo mató": el desbordamiento de Pecado multiplicaba Dynamism). El informe ya marca esa lectura como interpretación en el apartado 7, pero **no en el paso accionable nº6**, donde va etiquetada oficial. Ahí hay que corregirla.

*Dato adicional del mismo texto vetado, útil solo como pista:* el nodo parece aplicar a **daño de habilidades de Demonología**, no a daño genérico. El informe dice "3% de daño por Dominio" a secas. **Verificar en el tablero de Paragón.**

---

### E. REFUTADO — "Metamorfosis te sustituye la barra entera" no vale para dos de las tres variantes

El informe, línea 115, presenta como **corroborado por las dos fuentes y las notas oficiales**: *"Metamorfosis (a) te da Forma demoníaca, (b) **te sustituye la barra** por las variantes Archifiendo de Forma demoníaca"*. Y el resumen lo repite como propiedad de la Definitiva.

Wowhead `https://www.wowhead.com/diablo-4/skill/metamorphosis-2215096` — **la misma página que cita el informe** — dice literalmente de dos de las tres variantes:

- **Destruction Demon:** "Metamorphosis **does not replace any Skills** and grants Volatility while active. Each Hellfire Skill cast increases your Hellfire damage by 4.00% but Burns you for 8% Maximum Life over 3 seconds."
- **Terror Demon:** "Metamorphosis becomes an Abyss Skill that **does not replace any Skills** and lasts for 15.00 seconds. Metamorphosis grants 4 Shadowform stacks every second."

**Consecuencia:** la sustitución de barra es propiedad de la **versión base / Pecado**, no de Metamorfosis en general. Quien elija Destrucción o Terror **conserva su barra**, y por tanto ni le cambia el recurso ni le aplica nada de lo que el informe cuenta en el apartado 4. Esto refuerza el punto A: la "trampa" del cambio de recurso es, como mucho, un caso particular de una variante concreta más un objeto único.

*Detalle menor del mismo bloque:* el informe describe Terror como *"otorga cargas de Forma sombría y **mantiene el Sigilo**"*. Lo del sigilo no está en el texto de la variante — es el pasivo del fragmento **Cerebro** ("Recast Skills no longer break Shadowform Stealth..."). Dos mecánicas distintas pegadas en una línea.

---

### F. CONTRADICCIÓN NO REGISTRADA — El fragmento Cerebro puede no atar a Laalish

Paso accionable nº3: *"Cerebro -> Laalish"*, fuente `maxroll.gg/d4/getting-started/warlock-class-overview` (18 jul 2026).

Preguntada esa misma página por el vínculo fragmento→demonio:

- Legión → **"Grants the Summon Ae'Grom Skill."**
- Vanguardia → **"Grants the Summon Abodian skill."**
- Cerebro → **"Grants the Summon Taz'rauth skill."**  ← **no Laalish**
- Ritualista → **"Grants the Summon Vollach skill."**

y añade: *"The content does not mention demons named 'Laalish' or 'Valloch'"*.

El reveal de Maxroll (7 mar 2026) **sí** dice Cerebro → Laalish. Y las notas 3.2.1 hablan de **"Command Laalish"** (vía *Rictus of Terror*), luego Laalish existe y es comandable.

**Lectura honesta:** es perfectamente posible que el fragmento Cerebro **invoque a Taz'rauth** y **comande a Laalish**, o que Maxroll haya cambiado de nombre entre marzo y julio. No lo puedo resolver desde fuera. Lo que no vale es lo que hace el informe: dar una lista cerrada de cuatro demonios mayores como hecho establecido **sin mencionar que Taz'rauth aparece en la misma casa**. Nivel correcto: **disputa**. Quinta cosa que el jugador debe mirar en pantalla al llegar a nivel 30.

---

### G. Paráfrasis que no resiste la cita literal

| Informe (línea 84) | Texto literal (Icy Veins, `.../warlock-class-lets-you-command-hell-itself/`) |
|---|---|
| "Garra del tirano invoca **manos demoníacas adicionales**" | "Summon a Demon hand that **Pulls enemies away from you**, dealing damage." |
| "Centinela profano invoca un ojo que te sigue y dispara" | "Summon a demonic eye for a duration that focuses upon enemies with a beam that **makes them Vulnerable** and periodically blasts them." (el informe omite la **Vulnerabilidad**, que es lo que importa de la habilidad) |
| "Desenfreno invoca un bruto que te sigue y golpea" | "Summon a rampaging brute for a duration that smashes wildly, dealing damage **with a chance to Eviscerate**." (omite Eviscerar) |
| "Aliento infernal invoca una cabeza demoníaca que **orbita** y escupe llamas" | "Summon a demonic head for a duration that breathes fire on enemies dealing damage per hit." (no dice que orbite) |

Ninguna es grave por sí sola, pero el informe presenta estas cuatro como "unica" citando una fuente concreta, y la fuente no dice eso. La de Garra del tirano cambia el uso de la habilidad (es un **tirón**, no más manos).

*Corrección a favor del jugador, en la dirección contraria:* el informe suaviza Maxroll. Literal: *"**Only** Command Fallen can help to generate Dominance, and often it is the automatically included option on builds."* El informe escribe "Comandar a los caídos **ayuda** a generar Dominio". El "**Only**" es la información útil: si quieres Dominio pegando, **esa es la única puerta**.

---

### H. Fuentes vetadas: una, admitida, pero inflando un nivel de evidencia

**Barrido completo del informe:** la **única** fuente vetada citada es `diablo4.wiki.fextralife.com`, línea 82, y el informe la marca explícitamente como "VETADA para valores, citada solo como eco de nomenclatura". **Cero tiendas de oro o boosting** (iggm, mmoexp, u4gm, aoeah, mmogah, expcarry, u4n, mtmmo, d4gold, grindout, leprestore, timesaver, measurecentre, mythic-store, accountshark) sosteniendo nada. Eso lo doy por **limpio**, y no es trivial: mis propias búsquedas de "3.2.1 patch notes" devolvieron **mmoexp** en primera página y las de Dynamism devolvieron **fextralife** en el puesto 1. El informe esquivó ambas.

**Pero:** el nivel de evidencia de esa línea es "**corroborado**" y se construye contando fextralife como segunda fuente. La frase corroborada ("the Archfiend category provides the ability to exploit the power of your greater demons") es una descripción de **qué hace** una categoría, no un nombre. Sin fextralife queda **una sola fuente**. Corrección: **unica**.

**Wowhead** no está en la lista de vetados y lo uso yo también, pero conviene decirlo con todas las letras: `wowhead.com/diablo-4/skill/metamorphosis-2215096` **no tiene fecha ni número de build**, y su texto de Pecado es **exactamente el "Previous" del parche 3.2.1** — o sea, es una página pre-parche. Sirve para el estado viejo, no para el actual. El informe la usa bien pero la llama "datamine, sin fecha" sin extraer esa consecuencia.

---

### I. Guías refechadas / que no citan un solo cambio del 3.2.1

Comprobado una por una, preguntando expresamente por 3.2.1:

| Página | Fecha en la página | ¿Cita el 3.2.1? | Veredicto |
|---|---|---|---|
| `maxroll.gg/d4/tierlists/endgame-tier-list` | **14 sep 2026**, etiquetada **"Season 15 – Hell's Legacy"** | **NO** | **REFECHADA. El caso de manual.** Actualizada la víspera, con etiqueta de S15, cero menciones del parche. Pone Brujo: **A** — Minion, Apocalipsis, Lunatic; **B** — Fractura infernal, Grito llameante; **C** — Garra del tirano, Garras pavorosas, Eviscerar. **Ese tier A de Apocalipsis está escrito antes de los recortes a Hands of the Worldbreaker y Cage of Madness. No usar.** El informe original no la menciona. |
| `icy-veins.com/d4/news/warlock-is-suddenly-diablo-4s-best-class...` | **sin fecha en la página** | **NO** — habla del **PTR S15 (3.2.0)** | Caducada, y ella misma lo avisa: *"As always, PTR values are almost certainly going to change before the season goes live."* Da **S++**, *"Warlock easily demolishing Pit 150"*, *"Apocalypse once again appears to be the strongest build"*. **Solo menciona subidas a Hands of the Worldbreaker y Cage of Madness; ni una palabra de los recortes.** El informe acierta de pleno aquí. |
| `maxroll.gg/d4/getting-started/warlock-class-overview` | 18 jul 2026, S14 | **NO** | Confirmado pre-parche. |
| `icy-veins.com/d4/guides/warlock-skills/` | *"June 26th, 2026: Guide updated for Season 14."* | **NO** | Confirmado pre-parche. |
| `maxroll.gg/d4/build-guides/minion-warlock-guide` | 13 jul 2026, "Season 14 – Death Awakening" | **NO** | Confirmado pre-parche. |
| `wowhead.com/diablo-4/skill/metamorphosis-2215096` | **ninguna** | **NO** | Pre-parche (contiene el Pecado viejo). |
| `maxroll.gg/d4/news/diablo-4-3-2-1-patch-notes` | 12 sep 2026 | **SÍ** | **Válida.** Espejo fiel de las notas. |
| `news.blizzard.com/en-us/article/24295394/...` | 15 sep 2026 | **SÍ** | **Válida.** Notas 3.2.1 incrustadas en la propia página (no solo enlazadas). |

**Matiz al "no existe nada posterior al parche":** existe una **tier list de S15 del 14 sep** y Maxroll anuncia un "Season 15 Compendium" con guías actualizadas. Lo correcto no es "no hay nada", es "**hay cosas etiquetadas S15 que no citan el parche, y son peores que nada porque parecen actuales**".

---

### J. Lo que SÍ aguanta (comprobado por mí, cita a cita)

Toda la capa oficial del 3.2.1. Ocho comprobaciones literales, cero desviaciones:

| Afirmación del informe | Verificación |
|---|---|
| Texto "Now" de Pecado, completo | **Literal exacto**, Blizzard 24295394, 15 sep 2026: *"During Metamorphosis your Maximum Wrath and Dominance are increased by 50% and you deal 5% (scaled up per Rank) increased damage for each Demon Summon you have active. When you leave Metamorphosis, casting Summon Skills reduces its Cooldown by 2 seconds."* ✓ |
| Texto "Previous" de Pecado | **Literal exacto** ✓ — y además corroborado en Icy Veins `warlock-skills` (26 jun), que describe el sistema viejo con el mismo texto incluida la coletilla *"This can exceed up to 50% of your Maximum Resource values."* **Doble confirmación de que el desbordamiento existía.** |
| Dynamism: +85% fuera / 3%→2,5% dentro | **Literal exacto**, Blizzard + espejo Maxroll ✓ |
| "Basic Skill Dominance Generation increased from 2 to 5." | **Literal exacto** ✓ |
| "Summon Valloch: Cost reduced from 10 to 5 Dominance." | **Literal exacto** ✓ |
| Reetiquetados | **Literales exactos** ✓ — Bombardment "Base Skill is now a Summon Skill"; Dread Claws "…now a Greater Demon Skill"; Hellion Sting "…now a Lesser Demon Skill"; Dark Prison Calamity "Variant Is now also a Sigil Skill"; Doomfire Ritual "Burst is now considered a Sigil Skill cast"; Blazing Scream (Elegy) "Blazing Scream is now an Archfiend Skill" |
| Aspecto Abrumador previous→now | **Literal exacto** ✓ |
| Nota del desarrollador | **Literal exacto**, incluido *"We are also looking to redistribute power out of Demonform"* ✓ |
| Costes de recursos de Icy Veins | **Literales en la página** ✓ — "Wrath Generation: 10"; Bombardment 30 / Hell Fracture 35 / Umbral Chains 35 / Dread Claws 30 / Blazing Scream 35; Rampage 10 / Infernal Breath 10 / Tyrant's Grasp 7 / Profane Sentinel 10 |
| Disputa 5s vs 15s y 65% vs 137% | **Ambos extremos verificados** ✓ Icy Veins "Cooldown: 5 seconds" + "137% damage"; Wowhead "Cooldown: 15 seconds" + "65% damage and generates 2 Dominance". La disputa es real. |
| Demonform: +25% Vida, +1%/muerte hasta 100% a Demonología | **Literal exacto** en class overview ✓ |
| Los cuatro pasivos de fragmento | **Literales exactos** en class overview ✓ |
| Hueco del máximo base de Ira/Dominio | **Confirmado real**: ni Icy Veins ni Maxroll ni el artículo de los dos recursos publican esas cifras ✓ |

**La tesis central del informe queda intacta y la suscribo:** el eje de la variante Pecado pasa de **Archifiendo** a **Invocación**, y los reetiquetados del mismo parche (Bombardeo → Invocación, Comandar a Abodian → Invocación) son el carril compensatorio. Los dos hechos son oficiales y literales; la conexión es inferencia, y el informe lo marca como tal. **Correcto.**

---

## Huecos

*(de la refutación, no del informe original)*

1. **No he podido determinar qué recurso cuestan de base las variantes Archifiendo de Forma demoníaca.** Ninguna de las tres fuentes de mecánica lo enuncia como regla general. Solo existe la frase del único *Anathema of the Primes*. Queda como el hueco más importante del dominio entero.
2. **No he podido resolver Cerebro → Laalish vs Taz'rauth.** Dos páginas de Maxroll se contradicen y no tengo una tercera fuente no vetada.
3. **No he verificado el glosario español entrada por entrada.** Solo las siete que probé, de las cuales cinco fallaron. Las otras ~15 quedan sin comprobar y por tanto sin poder llamarse oficiales.
4. **No he podido leer la progresión por rango del +5% del nuevo Pecado.** Confirmo el hueco del informe.
5. **No he podido ver el contexto de una línea oficial en español que el informe da por inexistente** — ver Contradicción 4.

---

## Contradicciones

1. **La frase clave de la mecánica está atribuida a una página que no la contiene.** El informe la firma con Icy Veins `can-the-warlock-stay-in-demon-form-forever`; está en Maxroll `master-hell-itself-with-the-warlock`, dentro de un objeto único. **Evidencia: refutado.**

2. **Dos cifras de la sección 5 no están en su fuente.** "1 Dominio/s por demonio" y "x30% Demonología de Fuego infernal" no aparecen en `minion-warlock-guide`. **Evidencia: no encontrado** (deben salir del informe como cifras).

3. **"Confirmados en español por Blizzard" es falso para Vollach, Abodian, Laalish, Archifiendo y Demonio de la destrucción.** Solo Ae'grom y **Valloch** están en las notas es-es. **Evidencia: refutado.** Y la grafía correcta en español oficial es **Valloch**, no Vollach: la disputa del informe estaba mal planteada.

4. **Hay una cifra de generación de Dominio en texto oficial en español que el informe declara inexistente.** Notas es-es 3.1.3 (12 ago 2026): *"Generación de dominio aumentada a 2 cada 1 s"*. **No sé a qué pertenece** — puede ser un nodo, un aspecto o un objeto, no necesariamente la regeneración base. Pero el Hueco 2 del informe ("solo tengo 'se regenera despacio' cualitativo, sin cifra") es demasiado rotundo. **Evidencia: sinconfirmar — hay que leer el contexto de esa línea.**

5. **"Metamorfosis te sustituye la barra" contra su propia fuente.** Wowhead, la página que el informe cita, dice que Destrucción y Terror **no sustituyen ninguna habilidad**. **Evidencia: refutado como propiedad general.**

6. **El informe dice que no existe ninguna fuente posterior al parche; existe una y es peor que ninguna.** Tier list de Maxroll, 14 sep 2026, etiqueta "Season 15", **sin una sola mención del 3.2.1**, con Apocalipsis Brujo en tier **A**. Es la fuente que más probabilidades tiene de engañar al jugador esta semana, precisamente porque lleva la etiqueta correcta. **Evidencia: corroborado (fecha y etiqueta leídas en la página).**

7. **Detalles del 3.2.1 que el informe no recoge** (menores, todos de la misma fuente oficial ya validada):
   - *Dark Prison*, variante Calamity: además del reetiquetado a Sigilo, **se arregló que no estuviera previniendo muertes**. Cambio funcional, no cosmético.
   - **Grito llameante** acumula, según Maxroll, etiquetas de **Demonio Mayor y Menor a la vez**, además de Fuego infernal, Demonología, daño de Fuego y Principal — y el único *Elegy* le añade Archifiendo encima. El informe solo registra lo último. Para una build que lea etiquetas, ese apilamiento es la información valiosa.

---

## Veredicto

**El informe no es publicable tal cual.** Su capa oficial es excelente y la he validado entera; su capa de mecánica base tiene dos pasos accionables que se apoyan en citas mal atribuidas o inexistentes, y una afirmación de nomenclatura marcada "oficial" que es directamente falsa.

**Qué hay que arreglar antes de publicar, por orden:**

1. **Retirar o reescribir el paso nº2** ("la trampa de la Forma demoníaca"). Pasa de "así funciona la clase" a "así funciona **con el único *Anathema of the Primes***, y de base no lo sabemos — míralo en el tooltip".
2. **Quitar el "1/s" y el "x30%"** de la sección 5 y del paso nº2. Dejar la mecánica del drenaje sin número, citando el reveal del 7 mar, no la guía de minions.
3. **Corregir el paso nº3**: añadir que Maxroll se contradice a sí misma (Laalish vs **Taz'rauth**) y que el vínculo fragmento→demonio es **disputa**, no dato.
4. **Bajar "Dynamism lee tu Dominio actual" de oficial a sinconfirmar** en el paso nº6, y decir que la única fuente que usa la palabra "actual" está vetada.
5. **Rehacer la afirmación de nomenclatura española**: solo Ae'grom y **Valloch** están confirmados. Todo el glosario baja a sinconfirmar salvo reverificación una a una. Y la grafía que el jugador debe buscar es **Valloch**.
6. **Añadir la tier list del 14 sep a la lista negra de fuentes caducadas**, con nombre y apellidos: está etiquetada S15 y no cita el parche.
7. **Añadir una quinta cosa a verificar en pantalla**: a qué demonio te ata realmente el fragmento Cerebro.
8. **Ampliar el aviso sobre Metamorfosis**: la sustitución de barra es de la versión base/Pecado; Destrucción y Terror conservan la barra.
