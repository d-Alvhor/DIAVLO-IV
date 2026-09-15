# Refutación de `crudo/brujo-build.md` — Build de Brujo, S15 / parche 3.2.1

> Escrito el **15 sep 2026**, antes del arranque (18:30 CEST). Fichero aparte; el original no se toca.
> Lo que sigue son comprobaciones **independientes** contra las fuentes preferentes, no una relectura.

## Resumen (5 líneas)

**El informe NO es sólido.** Cuatro fallos graves, tres de ellos en las frases que sostienen sus
recomendaciones. (1) El número que el propio informe llama "del que depende todo el veredicto" —el punto
de empate del Aspecto Abrumador en 16-17 cargas— está calculado sobre una **cita mutilada**: el texto
antiguo **consumía 4 cargas por golpe** y el nuevo **se dobla contra enemigos Hexados**, dos cláusulas
que el informe omite y que invalidan la aritmética. (2) Afirma que Cage of Madness perdió la escalada
"cada segundo": el texto oficial **la conserva** (100% → **100-200% por segundo**), así que el
"descartar Lunático" se apoya en un recorte que no existe. (3) Su titular "cero guías citan el 3.2.1"
es **falso**: la guía S15 de Grito Ardiente dice literal *"The new Elegy changes add another Skilltag to
Blazing Scream: Archfiend!"*. (4) Los "DOS impactos" a Apocalipsis son **uno**: el Aspecto Abrumador no
está en la build de Maxroll y en Icy Veins es el **suplente** de El Abuelo para armas raras.
**Lo que sí aguanta:** ninguna fuente vetada respalda ni un número, las citas oficiales que verifiqué son
exactas (incluido el "200% longer durations" que yo dudaba), y la recomendación final —no comprometerse
hasta ver clasificación— sobrevive intacta, aunque por razones distintas a las que da.

## Hallazgos

### R1 — GRAVE · El cálculo del Aspecto Abrumador está hecho sobre una cita recortada

El informe escribe que el aspecto pasó *"de un bloque plano de 80-120%"* a *"5-7% por carga"*, y de ahí
saca su cifra estrella: *"El punto de empate está en ~16-17 cargas (80÷5 = 16; 120÷7 ≈ 17,1)"*, repetida
en el Resumen y en un accionable como **"el número del que depende todo el veredicto"**.

Texto **verbatim** de las notas 3.2.1 (https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy, **12 sep 2026**):

> **Antes:** "Each hit against Elite enemies deals 80-120%[x] increased damage but **requires and consumes 4 stacks of Overpower**."
>
> **Ahora:** "Occult Skills deal 5-7% increased damage against Elite enemies per stack of Overpower you have. **This bonus is doubled if the enemy is Hexed**."

Corroborado en el espejo de Maxroll (https://maxroll.gg/d4/news/diablo-4-3-2-1-patch-notes, **12 sep 2026**):
*"Changed from '80-120%[x] increased damage' per 4 Overpower stacks to '5-7% increased damage per stack', doubled if hexed."*

**Dos cláusulas omitidas, cada una rompe el cálculo por su lado:**

1. **"requires and consumes 4 stacks"** — el bloque viejo **no era plano**: estaba **capado a 4 cargas y
   las gastaba en cada golpe**. Comparar "80-120% plano" contra "5-7% × N cargas" es comparar una cosa
   con otra. No hay punto de empate porque el viejo no escalaba con cargas retenidas: escalaba con la
   **tasa de generación** de Sobrepoder. El eje correcto es *cargas acumuladas y retenidas* (nuevo)
   contra *golpes con 4 cargas disponibles* (viejo), y eso el informe no lo plantea.
2. **"doubled if the enemy is Hexed"** — el nuevo da **10-14% por carga** contra Hexados, no 5-7%.
   Y **la build de Apocalipsis de Maxroll usa Hex**: sección de palabras clave, literal,
   *"Hex: Sigil of Subversion (triggered by Rite of the Nameless)"*
   (https://maxroll.gg/d4/build-guides/apocalypse-warlock-guide, **30 jun 2026**).
   Con el doblado, el empate contra 80-120% caería a **~8-9 cargas** (80÷10 = 8; 120÷14 ≈ 8,6), no 16-17.
   **El informe publica la cifra con el doble del valor real** en el escenario que su propia fuente describe.

Añado un tercer punto que el informe tampoco toca y que pesa más que el empate: el viejo era **[x]
multiplicativo** y el nuevo dice **"increased"** a secas. Aditivo contra multiplicativo decide el
veredicto antes que cualquier recuento de cargas, y nadie lo ha comprobado.

**Nivel: oficial** (las dos citas) / **derivado** (mi aritmética del empate a 8-9).
**Consecuencia:** el accionable *"contar las cargas de Sobrepoder antes que nada"* apunta a la variable
correcta con el umbral equivocado. Hay que reescribir el umbral o retirarlo.

### R2 — GRAVE · "Cage of Madness perdió la escalada cada segundo" es falso

El informe (Contradicción 6 y el accionable *"descartar Lunático"*) sostiene: *"aparentemente sin la
escalada 'cada segundo' que tenía en el RPP"* y *"la pérdida real es **mucho mayor** que la que sugiere
comparar 300-340% con 100-200%"*.

Texto **verbatim** de las notas 3.2.1 (Blizzard, 12 sep 2026):

> **Antes:** "Your Evade transforms you into an angry Lunatic for up to 15 seconds that explodes dealing Command Fallen's damage and **increasing by 100% for every second** you're transformed."
>
> **Ahora:** "...explodes, dealing Command Fallen's **Base** damage, and you gain **100-200% increased Command Fallen damage every second**."

**El "every second" está en las dos versiones.** Por segundo, el objeto pasa de **100%** a **100-200%**:
en el rango alto es una **subida**, en el bajo un empate. Lo que cambia de verdad es que la explosión
ahora usa **Base damage** (eso sí puede ser un recorte, y es lo que habría que haber señalado). El espejo
de Maxroll añade además un cambio que el informe **no menciona en ningún sitio**: *"final explosion radius
increased 66%"* — una subida.

**Nivel: oficial.**
**Consecuencia:** de los *"TRES recortes a la vez"* que el informe le cuelga a Lunático, **el que presenta
como más grave no es un recorte**. El accionable "descartar Lunático para empujar" queda sin su pata
principal. No digo que Lunático esté bien; digo que el informe no ha demostrado que esté mal.

### R3 — GRAVE · "Ninguna guía de Brujo cita el 3.2.1" es falso

Es el titular del Resumen y la premisa de la que cuelga todo lo demás. La guía S15 de Grito Ardiente
(https://maxroll.gg/d4/build-guides/blazing-scream-warlock-guide, **S15 Hell's Legacy, 14 sep 2026**) dice
**literal**:

> "**The new Elegy changes** add another Skilltag to Blazing Scream: Archfiend!"

Eso **es** citar un cambio del 3.2.1 — el cambio de Elegy es una de las entradas del parche. El informe
marca esa fila con un **"NO"** en su tabla de auditoría.

El fallo es de método: el informe aplicó el test **"¿aparece la cadena '3.2.1' en la página?"** cuando el
encargo pedía el test **"¿menciona algún cambio del parche?"**. Son pruebas distintas y dan resultados
opuestos en la fuente que más importa.

**Nivel: oficial** (cita literal de la página).
**Consecuencia:** la acusación de "S14 re-fechada" **no aplica** a la guía de Grito Ardiente. Está escrita
sobre el 3.2.1. Paradójicamente esto **refuerza** la recomendación del informe de apuntar a Grito Ardiente
— pero por una razón que el informe no vio y contra la premisa que él mismo defiende.

### R4 — GRAVE · Los "DOS impactos" a Apocalipsis son uno; el Aspecto Abrumador no está en la build

Resumen del informe: *"Apocalipsis recibe DOS impactos directos (Hands of the Worldbreaker ... y Aspecto
Abrumador ..., que es el aspecto que Icy Veins **graba en su arma**)"*.

Comprobado en las dos fuentes:

- **Maxroll**, guía de Apocalipsis (30 jun 2026): la lista de aspectos **no incluye el Aspecto Abrumador**.
  El arma es **El Abuelo / The Grandfather** (*"The Grandfather only slightly beats Cremator's Aspect"*).
- **Icy Veins** (https://www.icy-veins.com/d4/guides/hellfire-apocalypse-warlock-build/, **26 jun 2026**):
  tabla de equipo literal — *"Weapon 2H | Royal Ruby | **1. The Grandfather 2. Overwhelming Aspect**"*,
  descrito como **la opción para armas raras cuando no tienes El Abuelo**.

El propio §4.2 del informe lo escribe bien —*"Aspecto Abrumador (arma 2M, **alternativa a El Abuelo**)"*—
y luego, en el Resumen y en el accionable, **asciende al suplente a titular**. Eso es exactamente lo que el
encargo prohíbe: un par valor→efecto sostenido por una **paráfrasis propia**, no por la cita.

**Agravante encontrado de paso:** la ficha de Icy Veins describe el Aspecto Abrumador como
*"Increases your Critical Strike Damage by x150%"* — que **no coincide ni con el texto viejo ni con el
nuevo** de las notas 3.2.1. La página en la que el informe se apoya para este punto **ni siquiera describe
bien el objeto**.

**Nivel: oficial** (las dos tablas de equipo).
**Consecuencia:** para la build publicada, Apocalipsis recibe **un** impacto — Hands of the Worldbreaker —
y el informe admite que **su valor previo es un hueco**. Es decir: el tamaño del recorte a Apocalipsis no
está "sin medir", está **sin acotar** con la evidencia que el propio informe reúne. El veredicto "golpeada
dos veces" no se sostiene.

### R5 — MEDIA · "Grito Ardiente recibe CERO impactos" contradice al propio informe

El Resumen dice **"CERO impactos"**. El §4.1 dice *"Su único punto de exposición es el rediseño de
Metamorfosis/Pecado, porque la build usa Metamorfosis"*. No pueden ser las dos cosas.

Y el texto oficial de Metamorfosis contiene una línea que el informe **no cita en ningún sitio**:

> "**Skills can no longer remain or become Volatile when they are swapped off the skill bar.**"

Además, el rediseño de Pecado cambia de beneficiar a las habilidades **No-Archidemonio** a dar
*"5% (scaled up per Rank) increased damage **for each Demon Summon you have active**"* — es decir, mueve
el premio hacia builds de **invocación**. Grito Ardiente **no es** una build de invocación, así que el
rediseño es plausiblemente una **pérdida neta** para ella. El informe lo despacha con "Sí, y reforzada".

**Nivel: oficial** (las citas) / **sinconfirmar** (que sea pérdida neta: nadie lo ha medido).

### R6 — MEDIA · Descalifica las listas S15 con un criterio que Maxroll contradice por escrito

El informe ordena: *"Trátalas como predicción sobre el RPP, no como veredicto sobre el parche vivo"*,
y lo justifica así: *"su registro de cambios no lo menciona (las entradas fechadas del historial de la
lista de empuje son de julio)"*.

**Eso es factualmente falso.** Registro de cambios de https://maxroll.gg/d4/tierlists/push-tier-list
(comprobado hoy), entrada más reciente:

> "**September 14, 2026 — Updated for Season 15.**"
> (las siguientes: 23 jul "Added Shield Charge", 14 jul "Storm Set snapshot fix")

Igual en https://maxroll.gg/d4/tierlists/endgame-tier-list: entrada del **14 sep 2026, "Updated for Season 15"**.

Y el compendio que el propio informe cita en su cabecera
(https://maxroll.gg/d4/news/diablo-4-season-15-compendium-season-launch-update, **14 sep 2026**) publica la
convención de la casa, **literal**:

> "An easy way to tell if a guide has been **fully updated** is by seeing the '**Season 15 - Hell's Legacy**' tag at the top of a guide."

**Nivel: oficial.**
**Consecuencia:** el Hueco 5 del informe ("Si las listas de la S15 del 14 sep incorporan o no el 3.2.1.
**No lo dicen**") está **respondido por la propia fuente** y el informe no fue a mirarlo. La etiqueta S15
es, según Maxroll, la señal de "actualizada del todo". Eso no convierte las listas en verdad medida —
siguen siendo predicción sin clasificación— pero **sí desmonta la razón que el informe da** para
degradarlas a "RPP".

### R7 — MEDIA · El accionable del planificador está muerto

El informe remata el hueco de las mejoras de habilidad con: *"hay que abrirlas en **el planificador de
Maxroll** o en el árbol del juego"*.

Compendio de Maxroll, **14 sep 2026**, literal:

> "**D4Planner will be updated as soon as possible with all the data from the 3.2.1 Patch!**"

El planificador **todavía no tiene los datos del 3.2.1**. La mitad de ese accionable no sirve hoy: solo
vale el árbol dentro del juego.

**Nivel: oficial.**

### R8 — MENOR · Datos oficiales omitidos, y uno infravalorado a la baja

| Pieza | Lo que falta en el informe | Por qué importa | Nivel |
|---|---|---|---|
| **Hellhound's Sabatons** | *"Command Abodian periodically triggers your Non-Archfiend Hellfire Skills while moving"* está **en las notas oficiales 3.2.1** | El informe se lo atribuye a Icy Veins y lo marca ***"unica, y es RPP"***. Es **oficial**. Se degradó a sí mismo su mejor prueba: el "Brujo de un botón" tiene base oficial, no solo una nota de RPP | oficial |
| **Fiend of Abaddon** | *"each active Fiend grants 30%[x] Lesser Demon damage"* | Refuerza la tesis de Esbirros que el informe marca como "derivado mío" | corroborado (espejo) |
| **Metamorfosis** | *"Basic Skill Dominance Generation increased from 2 to 5"* | Es una **subida** real y no aparece en ninguna de las dos tablas del informe | oficial |
| **Cage of Madness** | *"final explosion radius increased 66%"* | Subida a Lunático, la build que el informe manda descartar | corroborado (espejo) |
| **Nails of the Gore-Crowned** | *"Hellion Sting gains 0.5-2.5% Eviscerate Chance each second it has not Eviscerated"* | Cierra el bucle del rediseño | oficial |

### R9 — MENOR · Un "hueco" que no es hueco

Hueco 1 del informe: el "desde" de Cage of Madness *"no lo he podido verificar de forma independiente"*.
El espejo de Maxroll lo publica: *"Command Fallen now deals '100-200% increased damage' (**previously
300-340%**)"*. La cifra del encargo queda **corroborada**.
(El hueco de **Hands of the Worldbreaker** sí es real y sigue en pie: las notas dicen "reduced **to**
290%-350%" y el "desde" no aparece en ninguna fuente que yo haya podido leer.)

### R10 — Lo que el informe hace BIEN y aguanta la refutación

Por honestidad, y porque el encargo pide comprobarlo:

- **Fuentes vetadas: CERO.** Repasé las 17 URLs del informe. Solo hay `news.blizzard.com`, `maxroll.gg` e
  `icy-veins.com`. **Ninguna tienda de oro, ninguna wiki vetada respalda ningún número.** Limpio.
- **El "200% longer durations" del Homúnculo Infernal es real.** Dudé de él porque el espejo de Maxroll lo
  omite; el texto oficial de Blizzard **sí lo lleva**: *"...activates all their Lesser Demon Upgrades for
  free **with 200% longer durations**"*. El informe acertó.
- Verificadas una por una y **exactas**: Grito Ardiente base 40→55%; tope de Brimstone Hunger 25→50%;
  Elegy; Gauntlets of Sheol; Dynamism *"85% increased Summon Skill damage while not in Demonform"*;
  Hands of the Worldbreaker "reduced to 290%-350%".
- **Escalar de estadística principal:** confirmado que el Brujo **no aparece** en la tabla de cambios
  (Druida/Nigromante/Paladín/Hechicera 1.25→1.625; Bárbaro 1.1→0.8). El informe lo etiqueta
  correctamente como *"oficial por ausencia"*, que es una inferencia bien marcada, no un dato robado.
- **Fechas y tiers verificados uno a uno:** lista de EMPUJE (S15, 14 sep) = Apocalipsis **S**, Grito
  Ardiente **S**, Lunático A, Tyrant's/Esbirros B, Dread Claws/Hell Fracture/Eviscerate C. Lista de
  endgame (S15, 14 sep) = **ningún Brujo en S**, Grito Ardiente **B**. Guía de Grito Ardiente = 14 sep,
  *"Created for Season 15"*. Guía de Apocalipsis = 30 jun, cita 3.1.0. Icy Veins Apocalipsis = 26 jun,
  S14 y con la etiqueta de temporada mal puesta. **Todo correcto.**
- **La recomendación final sobrevive.** "No comprometerse con una build de empuje hoy; subir a 70 y decidir
  con la clasificación de las primeras 48-72 h" sigue siendo lo correcto — de hecho **más** correcto
  después de esta refutación, porque los dos cálculos que el informe ofrecía como sustituto de la
  clasificación (el empate a 16-17 cargas y el triple recorte a Lunático) **no son utilizables**.

### R11 — Peligro nuevo detectado para quien repita esta búsqueda

Al buscar yo mismo los valores del Aspecto Abrumador, **el resultado son casi exclusivamente tiendas de
oro vetadas** (mmoexp, aoeah, mmogah, mtmmo). Y publican un número **falso**: afirman *"17% increased
occult damage per Overpower stack, doubling to 34% for hexed"*. El texto oficial dice **5-7%** (10-14%
hexado). Es un **inflado de ~2,4x**.

**Aviso para la capa de redacción:** este es el dato exacto donde la búsqueda te empuja a una fuente vetada
con una cifra inventada. Cualquier "17%" que aparezca en una revisión posterior viene de ahí. Vale 5-7%.

## Huecos (de mi propia refutación)

1. **No comprobé la lista de farmeo rápido** (`maxroll.gg/d4/tierlists/speedfarming-tier-list`). Las
   afirmaciones del informe sobre ella quedan **sin verificar por mí** (no refutadas, tampoco confirmadas).
2. **No abrí las guías de Lunático, Esbirros, Hell Fracture, Tyrant's Grasp ni Dread Claws.** Sus fechas y
   contenidos siguen siendo palabra del informe. En particular, **no he verificado la cita de Lunático**
   *"With Dynamism you lose damage by spending Dominance"*.
3. **Aditivo contra multiplicativo en el nuevo Aspecto Abrumador.** El viejo era `[x]`; el nuevo dice
   "increased" sin marcador. No he encontrado fuente que lo aclare, y decide más que el punto de empate.
4. **El "desde" de Hands of the Worldbreaker sigue sin aparecer.** Busqué; lo único que sale son tiendas
   vetadas. Confirmo el hueco del informe.
5. **La noticia sin fecha de Icy Veins** no la he vuelto a abrir; no puedo fecharla mejor que el informe.
6. **Nada de esto es medición.** Igual que el original: no hay clasificación, no hay parche vivo. Mis
   correcciones son de **texto y de aritmética**, no de rendimiento real.

## Contradicciones

1. **El informe contra sí mismo, en Apocalipsis.** §4.2 escribe "Aspecto Abrumador (arma 2M, **alternativa
   a El Abuelo**)". El Resumen escribe "es el aspecto que Icy Veins **graba en su arma**" y cuenta "DOS
   impactos". El cuerpo es correcto; el resumen exagera al cuerpo. **Manda el cuerpo.**
2. **El informe contra sí mismo, en Grito Ardiente.** "CERO impactos" (Resumen) contra "su único punto de
   exposición es el rediseño de Metamorfosis/Pecado" (§4.1). **Manda el cuerpo:** no son cero.
3. **El informe contra Maxroll, sobre el registro de cambios.** Dice que el historial de la lista de empuje
   es de julio; la entrada de cabecera es del **14 sep 2026, "Updated for Season 15"**. **Manda Maxroll.**
4. **El informe contra la guía de Grito Ardiente.** La marca "no cita el 3.2.1"; la guía dice "The new
   Elegy changes". **Manda la guía.**
5. **Espejo de Maxroll contra notas de Blizzard, en el Homúnculo Infernal.** Maxroll omite el "with 200%
   longer durations"; Blizzard lo incluye. **Manda Blizzard** (fuente primaria). Nota de método: el espejo
   de Maxroll **abrevia** — no sirve para argumentar por ausencia.
6. **Icy Veins contra las notas del parche, en el propio Aspecto Abrumador.** Icy Veins lo describe como
   "+150% de Daño Crítico"; las notas describen un efecto completamente distinto en las dos versiones.
   O es un objeto distinto con nombre parecido, o la ficha está mal. **Sin resolver** — pero inhabilita esa
   página como soporte para cualquier afirmación sobre ese aspecto.
7. **Tiendas de oro contra Blizzard.** 17%/34% por carga contra 5-7%/10-14%. **Manda Blizzard**; las
   tiendas quedan como ejemplo de por qué están vetadas.

## Veredicto

**No sólido.** El armazón documental es honesto y está limpio de fuentes vetadas, y el reflejo de "no me
comprometo sin clasificación" es el correcto. Pero **las tres cifras y la premisa que el informe ofrece
como su aportación propia —el empate a 16-17 cargas, el triple recorte a Lunático, los dos impactos a
Apocalipsis y el "cero guías citan el parche"— no sobreviven al contraste con el texto oficial.**

**Antes de publicar nada hay que:** retirar el umbral de 16-17 cargas (o rehacerlo a ~8-9 con el doblado
por Hex, advirtiendo de que el eje viejo era otro); retirar el "descartar Lunático" por Cage of Madness;
rebajar Apocalipsis de "golpeada dos veces" a "golpeada una vez, de tamaño desconocido"; corregir el
titular a "ninguna guía cita el **número** del parche, pero la de Grito Ardiente **sí cita el cambio de
Elegy**"; y borrar la recomendación de usar el planificador de Maxroll hasta que cargue los datos del 3.2.1.
