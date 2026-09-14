# s15-clases — REFUTACIÓN

> **Rol:** refutador adversarial. Este fichero NO edita el original
> (`investigacion/crudo/s15-clases.md`); lo contradice donde procede y lo confirma donde el original
> aguanta. Escrito el 15 de septiembre de 2026, antes de las 16:30 UTC, igual que el original:
> sigue sin existir un solo dato de juego real de la S15.
>
> **Método:** he vuelto a leer las fuentes yo mismo, sin fiarme de las citas del original. Cada
> verificación de abajo es una lectura nueva de la página, no una relectura del informe.

## Resumen

1. **Los datos de parche del original aguantan.** He reverificado uno por uno los valores más cargados (escalares, Supremacía, Metamorfosis, Selig, Tibault, resistencias, Tzic, Granadero) contra Blizzard y contra Maxroll: **coinciden**. Cero fuentes vetadas. Cero números inventados.
2. **Pero la "corrección de marco" estrella del informe está del revés.** El original afirma que el core stat scalar alimenta el **bucket aditivo**. Su propia fuente —la guía de daño de Maxroll, la misma página que usa para fijar el 1.25— dice literalmente lo contrario: el stat principal es **un multiplicador separado e independiente**.
3. **De ahí sale un hueco falso.** El informe declara "hueco central: ninguna fuente publica el peso de ese bucket". Sí lo publica: Maxroll da el coeficiente **y la fórmula**. El efecto es calculable, y lo he calculado.
4. **Las cifras de "posición relativa" (−23,1 % Pícaro, −44 % Bárbaro) son el límite asintótico** (stat principal → ∞) presentado como si fuera el valor real. A stat principal realista salen **−16 % a −19 %** y **−31 % a −36 %**.
5. **La tier list de clases de Icy Veins son TRES listas, no una.** El informe publica solo la de Endgame Push como "el orden que publica", y con ella construye un reproche que se cae: en la lista de Leveling **Paladín sí está en S-Tier**.

---

## Hallazgos

### 1. [GRAVE] El marco aditivo/multiplicativo está invertido — y lo desmiente su propia fuente

**Lo que dice el original** (sección A, "Aviso de modelo, importante"):
> "el core stat scalar alimenta el bucket **aditivo** de daño por stat principal, no el daño total."

**Lo que dice la fuente que él mismo cita**, cita literal de la guía de daño de Maxroll:
> *"This functions as a separate multiplier and is not to be confused with [Skill %]. In other words, in the damage formula, [Skill %] and [Main Stat] function as two separate and completely independent multipliers."*

Y da la fórmula:
> *"our [Main Stat Multiplier] is equal to [100% + (Total Main Stat/Class Coefficient)] in the damage formula."*

- URL: https://maxroll.gg/d4/resources/in-depth-damage-guide
- Fecha de la página: **12 jun 2026** (etiquetada Temporada 13) — fuera del parche vivo
- Evidencia: **unica** (una sola fuente preferente), pero es **la misma y única** fuente con la que el original fija el 1.25 de base. No se puede aceptar la página para el número y rechazarla para el modelo.

**Por qué importa:** el original usa el marco aditivo para concluir que el efecto es incognoscible. Con el marco correcto (multiplicador propio) el stat principal **no compite con los aditivos del build**: el cambio de escalar es un multiplicador casi global sobre el daño total, y su magnitud depende de **una sola variable que el jugador lee en su propia hoja de personaje**: el total de stat principal.

### 2. [GRAVE] "Hueco central del informe" que no es un hueco

**Lo que dice el original** (sección Huecos):
> "**Peso real del core stat scalar en el DPS total:** ninguna fuente publica qué fracción del daño sale del bucket de stat principal. Sin eso, '+30 % de escalar' no se puede convertir en porcentaje de DPS. Hueco central del informe."

Es falso. Maxroll publica el coeficiente (**8 de stat principal por 1 % para todas las clases salvo Bárbaro; 9,0991 para Bárbaro**) y la fórmula (`M = 1 + StatPrincipal/Coeficiente`). El informe cita la primera mitad y omite la segunda.

Verificación de que la fórmula es la correcta: la propia guía da un ejemplo trabajado —*"A Necromancer with 700 Main Stat: (700 ÷ 800) = 87.5% Skill Damage, multiplier 1.875×"*— y mi reconstrucción `M = 1 + 1,25·700/1000 = 1,875` lo reproduce exactamente. El modelo encaja.

- URL: https://maxroll.gg/d4/resources/in-depth-damage-guide · fecha **12 jun 2026** · evidencia **unica** (y fuera del parche vivo: ver Huecos)

### 3. [GRAVE] Las cifras de posición relativa son el límite asintótico, no el valor

El original escribe, en prosa y sin caveat adjunto:
> "no recibir el +30 % cuando cuatro clases sí lo reciben es **perder 23,1 % de posición relativa**"
> "el Bárbaro no cae 27 %, cae **44 % de posición relativa**"

Esos dos números son exactamente `1,25/1,625 = 0,769` y `(0,8/1,625)/(1,1/1,25) = 0,559`, es decir, el cociente **de los escalares desnudos**. Eso solo es válido si el stat principal tiende a infinito, porque solo entonces el `1 +` de la fórmula deja de contar. A valores reales de stat principal el efecto es **notablemente menor**:

| Stat principal | Buff real de las 4 subidas | Bárbaro, daño propio | Pícaro, pérdida relativa | Bárbaro, pérdida relativa |
|---:|---:|---:|---:|---:|
| 1000 | +16,7 % | −14,3 % | −14,3 % | −26,5 % |
| 1500 | +19,6 % | −17,0 % | −16,4 % | −30,6 % |
| 2000 | +21,4 % | −18,8 % | −17,6 % | −33,1 % |
| 2500 | +22,7 % | −20,0 % | −18,5 % | −34,8 % |
| 3000 | +23,7 % | −20,9 % | −19,1 % | −36,1 % |
| **→ ∞** | **+30,0 %** | **−27,3 %** | **−23,1 %** | **−44,1 %** |

- Derivado de la fórmula de https://maxroll.gg/d4/resources/in-depth-damage-guide (12 jun 2026) aplicada a los escalares oficiales de https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (notas 3.2.1, build #73552)
- Evidencia: **unica** en cuanto al modelo; **oficial** en cuanto a los escalares. El cálculo es mío.

**La ironía:** el original tenía razón en el titular ("+30 % de escalar ≠ +30 % de DPS") y razón en la dirección del argumento del Pícaro. Se equivoca en el porqué, y luego publica precisamente los números del caso límite que su propio aviso desaconseja usar. La columna "Variación" de su tabla (−27,3 % / +30 %) tampoco es variación de daño: es variación del escalar.

### 4. [MEDIO] La tier list de clases de Icy Veins son tres listas; el informe enseña una

El original escribe: *"Orden que publica: S-Tier Pícaro, Bárbaro, Druida, Brujo; A-Tier Espiritado, Hechicera, Nigromante, Paladín."*

Lo que hay realmente en la página son **tres rankings separados**:

| Ranking | S-Tier | A-Tier |
|---|---|---|
| Leveling | Pícaro, Espiritado, **Paladín**, Druida | Brujo, Nigromante, Hechicera |
| Speed Farming | Pícaro, Druida, Hechicera, Paladín, Bárbaro, Espiritado, Brujo | (ninguno) |
| Endgame Push | Pícaro, Bárbaro, Druida, Brujo | Espiritado, Hechicera, Nigromante, Paladín |

- URL: https://www.icy-veins.com/d4/guides/class-tier-list/ · fecha de la página: **4 jul 2026** · evidencia **unica**

**Dos consecuencias.** (a) El informe presenta la fila de Endgame Push como "el orden que publica" la página, sin decir que ha elegido una de tres. (b) El reproche que construye con ella —*"ranquea… al Paladín en A pese a que Blizzard dice por escrito que se ha quedado atrás"*— **solo es cierto en una de las tres listas**: en Leveling, Paladín está en S. El argumento no se cae del todo (Blizzard habla explícitamente del *late game*, y ahí Paladín sí está en A), pero el informe no hace esa distinción y su cita queda más contundente de lo que la página permite.

### 5. [MEDIO] "Aspecto de Supremacía: tope 30 → 15" es una paráfrasis que se come la condición

**Cita literal de las notas oficiales:**
> *"Bonus stacks once an Ultimate Skill ends now cap at 15 total stacks, down from 30."*

**Lo que escribe el informe:** "Aspecto de Supremacía: tope 30 → **15** acumulaciones."

El recorte no es del tope del aspecto en general: es del tope de las acumulaciones **una vez termina una habilidad Definitiva**. El informe elimina la cláusula condicional, que es justo la que determina a qué builds de Espiritado les duele. Este es el patrón que la regla 3 del encargo persigue: par valor→efecto derivado de paráfrasis, no de cita.

- URL: https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy · notas 3.2.1 build #73552 · evidencia **oficial**

### 6. [MEDIO] El dev note del Bárbaro está truncado sin marca de corte

El informe presenta como cita cerrada (punto y comillas, sin elipsis):
> *"Barbarians have been strong for the past couple seasons, so we're going to adjust the class while improving some Core skills."*

**El texto oficial completo tiene una segunda frase:**
> *"Barbarians have been strong for the past couple seasons, so we're going to adjust the class while improving some Core skills. **We are also fixing issues that prevented other builds from reaching their full potential.**"*

Importa porque el informe titula esa sección "**el único paquete de nerfs coordinado del parche**". La frase suprimida es la que Blizzard usa para enmarcarlo como reajuste-con-apertura, no como poda. En el resto de citas el informe sí usa elipsis ("…") cuando corta; aquí no.

- URL: https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy · evidencia **oficial**

### 7. [MENOR] La fecha de la fuente principal se contradice con el fichero hermano del expediente

- `crudo/s15-clases.md` encabeza la sección A: *"notas oficiales 3.2.1, build #73552, **15 sep 2026**"*.
- `crudo/s15-anclaje.md`, mismo expediente, misma URL, la fecha como *"**12 sep 2026** (según réplica de Maxroll)"*.

El 15 de septiembre es la fecha de **despliegue del parche** que aparece en la cabecera del bloque de notas ("Build #73552 (All Platforms) — September 15, 2026"), no la fecha de publicación del artículo. El formato del encargo pide "fecha de la página", y el informe pone la del parche. Mi propia lectura de la página no devuelve ningún sello de publicación visible, así que **la fecha de publicación real no está confirmada por mí** — pero los dos ficheros del mismo expediente no pueden decir cosas distintas del mismo campo.

### 8. [MENOR] Números atribuidos a Icy Veins sin URL

Dos valores se corroboran "con Icy Veins" sin dar la URL, contra la regla 4 ("cada número lleva su URL al lado"):
- Ramaladni's Magnum Opus: *"el matiz '10 % → 7 %' aparece en Icy Veins"*.
- Templado de daño por Punto de Combo gastado: *"(unica: Maxroll 12 sep + Icy Veins)"*.

El informe declara el primero como hueco, lo cual lo salva a medias. El segundo se presenta como corroborado por dos casas y solo una es citable.

### 9. [NO REPRODUCIDO] Aspecto de Fuerza Celestial

El informe lo da como **oficial** dos veces (30-40 % → 20-30 %, y apertura a Espiritado). Al pedir esa línea explícitamente a la página oficial, **no me la devuelve**. No afirmo que sea falsa —una lectura que no encuentra algo no prueba su ausencia, y el artículo es enorme—, pero **no he podido reproducirla** y queda marcada como pendiente de confirmar, no como oficial.

---

## Lo que el informe SÍ resiste (verificado de nuevo, por mí)

No todo es refutación. Esto lo he vuelto a leer en la fuente y **coincide**:

| Afirmación del informe | Resultado de mi verificación | Nivel |
|---|---|---|
| Bárbaro 1.1 → 0.8; Druida/Nigro/Paladín/Hechicera 1.25 → 1.625 | Confirmado **tres veces**: notas 3.2.1, notas PTR 3.2.0 y réplica de Maxroll | oficial |
| Pícaro, Espiritado y Brujo **no** tienen línea de escalar | Confirmado en dos lecturas independientes de la página oficial. La "Versión A" de su Contradicción 1 (que incluía a Brujo) **no aparece en el texto**: su resolución B es la correcta | oficial |
| Escalares idénticos en PTR 3.2.0 (4 ago, build #73123) y en final | Confirmado, cifra por cifra. **No es artefacto de PTR** | oficial |
| Lectura "% por 10 puntos de stat" | Confirmada **en el texto oficial**, no solo en Maxroll: *"This change increases Damage per 10 points of Willpower from 1.25% to 1.625%"* | oficial |
| Base 1.25 = 8 de stat por 1 % | Aritmética correcta: 8/1 % → 1,25 % por 10; 9,0991/1 % → 1,099 % por 10 ≈ 1.1. La inferencia es sólida | unica |
| Metamorfosis: Dominance 2 → 5; Sin Demon rediseñado (antes hasta 20 acum.; ahora +50 % Ira y Dominio máx.) | Confirmado literal | oficial |
| Nodo Dynamism +85 % daño de Invocación fuera de Demonform; 3 % → 2,5 % dentro | Confirmado literal | oficial |
| Aspecto Abrumador: *"Occult Skills deal 5-7% increased damage against Elite enemies per stack of Overpower"* | Confirmado literal | oficial |
| Paladín: Lanza Divina 90 % → 110 %; Juicio escala con el rango de la habilidad que lo aplica | Confirmado literal | oficial |
| Pícaro: Granadero 35-50→45-60 y 52,5-75→75-100; Pitfighter's Gull 7,5-10 → 15-20 | Confirmado literal | oficial |
| Selig 102-154 % → 58-77 %; Tibault's Will 50 % → 25 %; resistencia única = **7×** la de Todas las Resistencias | Confirmado literal | oficial |
| Runa Tzic: *"Fixed an issue where the Tzic Rune could incorrectly increase the damage of all skills"* | Confirmado literal | oficial |
| Maxroll tier list: 14 sep 2026, S-Tier tal cual lo lista, **y sin ningún aviso de provisionalidad** | Confirmado, incluido el negativo | unica |
| Icy Veins Class Tier List: 4 jul 2026, se autodenomina "Season 15", el índice la etiqueta **"Season 13"** | Confirmado ambas cosas | unica |
| Cita del compendio de Maxroll pidiendo paciencia | Confirmada literal, **y hay una segunda frase** que el informe no cita: *"This could take a day or two, a few hours, or just minutes once the season goes live."* | unica |

**Cero fuentes vetadas.** Las nueve URLs del informe son Blizzard (2), Maxroll (4) e Icy Veins (3). Ninguna de fextralife, primagames, beebom, gamespot, segmentnext, studioloot, gamerguides, pcgamesn ni mythicdrop. En este eje el informe está limpio.

**El aviso principal sobre tier lists es correcto y debe mantenerse.** Ninguna fuente preferente tiene datos de la S15 jugada, y la crítica a Icy Veins (contenido del 4 de julio bajo rótulo "Season 15") es comprobable y grave.

---

## Huecos

Míos, no suyos:

- **El modelo de daño que uso para refutar está fuera del parche vivo.** La guía de Maxroll es del 12 jun 2026 / S13. Que el stat principal sea multiplicador separado pudo cambiar en 3.2.1 y **no tengo confirmación dentro del parche vivo**. Lo que sí es seguro es que el informe no puede sostener el marco aditivo: ninguna fuente lo respalda, ni siquiera la suya.
- **No he podido verificar el coeficiente base de Paladín ni de Brujo en ninguna fuente.** La guía de Maxroll enumera Bárbaro, Nigromante, Hechicera, Pícaro, Espiritado y Druida — **no lista Paladín ni Brujo**. El informe ya lo declara; lo confirmo y lo subrayo, porque para el Brujo (no tocado) el 1.25 es inferencia pura.
- **Valores de stat principal realistas en 3.2.1: no verificados.** Mi tabla de la sección 3 es paramétrica a propósito. No he encontrado fuente preferente dentro del parche vivo que publique rangos típicos de stat principal en el endgame de la S15. El jugador tiene que leer el suyo.
- **No he verificado** las listas largas marcadas *unica* del informe (compensaciones de Espiritado, buffs de Brujo, Druida Forma Humana / Furia Grizzly). El informe ya las declara sin verificar línea por línea; no he mejorado ese hueco.
- **Aspecto de Fuerza Celestial:** ver hallazgo 9. Pendiente.
- **La fecha de publicación del artículo oficial** no me consta con sello visible. Ver hallazgo 7.
- **Nada sobre juego real.** Igual que el original, y por el mismo motivo: son las 15 de septiembre antes de las 16:30 UTC.

---

## Contradicciones

**1. Aditivo o multiplicador propio — el informe contra su propia fuente.**
- *Versión A (el informe):* el core stat scalar alimenta el bucket **aditivo**; por tanto su peso depende del resto de aditivos del build y **ninguna fuente lo publica**.
- *Versión B (Maxroll, la fuente que él cita para el 1.25):* el stat principal es *"a separate multiplier… two separate and completely independent multipliers"*, con fórmula `100% + (Stat/Coeficiente)` y ejemplo numérico.
- **Resolución: B.** No hay fuente para A. Y B es autoconsistente: su ejemplo trabajado (700 Int → 1,875×) se reproduce con la fórmula. El informe llegó a la conclusión correcta ("+30 % ≠ +30 % de DPS") por un camino que ninguna fuente respalda, y de paso se inventó un hueco.

**2. −23,1 % / −44 % (informe) contra −17,6 % / −33,1 % (cálculo con el modelo correcto, stat 2000).**
- Ambas salen de los mismos escalares oficiales. La diferencia es entera del marco: el informe divide escalares, el modelo exige dividir multiplicadores `1 + escalar·Stat/1000`.
- **Resolución: las del informe son el caso límite.** Solo son correctas si el stat principal tiende a infinito. Como cifras publicables, exageran el efecto entre 6 y 11 puntos porcentuales en el rango plausible. Dicho esto: **el signo y el sentido del argumento del Pícaro siguen siendo correctos** — no recibir el buff mientras cuatro clases lo reciben sí es perder terreno.

**3. "El orden que publica Icy Veins" — una lista contra tres.**
- *Versión A (el informe):* S-Tier Pícaro, Bárbaro, Druida, Brujo; A-Tier Espiritado, Hechicera, Nigromante, Paladín.
- *Versión B (la página):* eso es **únicamente** la tabla de Endgame Push. Hay además Leveling (Paladín en **S**) y Speed Farming (siete clases en S, Bárbaro incluido).
- **Resolución: B.** El informe no miente en los valores, pero recorta el objeto. Su reproche sobre Paladín se sostiene solo para el *late game* —que es, en su descargo, justo de lo que habla el dev note de Blizzard—, y esa precisión falta en el texto.

**4. Fecha de la fuente principal: 15 sep (este informe) contra 12 sep (`s15-anclaje.md`).**
- No resuelta. Una es fecha de despliegue del parche, la otra pretende ser fecha de publicación del artículo. **Ninguna de las dos está verificada por mí con un sello visible en la página.** El expediente debe unificar el criterio antes de publicar.

---

## Veredicto

**El informe NO es sólido tal cual está, pero su base fáctica sí lo es.**

Lo que hay que corregir antes de que esto llegue a la guía:

1. **Invertir el aviso de modelo:** el stat principal es multiplicador propio, no bucket aditivo.
2. **Retirar el "hueco central":** el peso sí está publicado; sustituirlo por la fórmula y la tabla paramétrica.
3. **Sustituir −23,1 % y −44 %** por el rango real, o etiquetarlos explícitamente como caso límite.
4. **Restaurar la condición** en Aspecto de Supremacía ("una vez termina una Definitiva").
5. **Restaurar la segunda frase** del dev note del Bárbaro, o marcar el corte.
6. **Decir que la tier list de clases de Icy Veins son tres listas**, y acotar el reproche a Paladín al late game.
7. **Unificar la fecha** de la fuente oficial con `s15-anclaje.md`.
8. **Degradar el Aspecto de Fuerza Celestial** de *oficial* a *sinconfirmar* hasta releerlo.

Lo que hay que **conservar intacto**: todos los valores de parche, la resolución de la Contradicción 1 (Brujo no sube), la verificación PTR-vs-final, el aviso de que ninguna tier list ha visto la S15 jugada, y la observación de que Maxroll publica una lista cerrada el día antes del lanzamiento sin avisar de que es teórica. Eso último es el mejor hallazgo del informe y lo he confirmado yo mismo.
