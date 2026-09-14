# Refutación — s15-endgame (parche 3.2.1, Temporada 15)

> Veredicto sobre `/Users/alvhor/Proyectos/DIAVLO IV/investigacion/crudo/s15-endgame.md`.
> Redactado el 15 de septiembre de 2026. Fichero aparte: el original no se toca.

## Resumen

1. **El núcleo del informe aguanta.** He recomprobado contra fuente primaria las citas literales de las
   notas oficiales, las cuatro fechas de Maxroll, el tope 150, el Paragón 300/342, las Hordas y las dos
   páginas de Icy Veins. Todas coinciden **palabra por palabra**. Cero fuentes vetadas.
2. **Su hallazgo estrella (C5) es correcto y lo confirmo por cálculo independiente**: el tramo declarado
   "4–10 → +26,5% de vida" es falso a partir del tier 8. Pero el informe **se paró un nivel antes** de
   llegar al fondo del marco (ver R4).
3. **Defecto grave: F20 no está corroborado.** El reseteo semanal y toda la escalera de recompensas salen
   de **una sola** fuente, y esa fuente se apoya en **un anuncio de PTR**. Maxroll no dice "semanal" ni una vez.
4. **Defecto grave: la fecha "12 sep 2026" no está en la página de Blizzard.** Se cita así 22 veces. La
   única fecha visible en esa página es **15 de septiembre de 2026**.
5. **Hueco oculto: las notas marcan los cambios de PTR en COLOR** ("PTR changes are highlighted in blue").
   Ninguna extracción de texto lo ve. El informe dice haberlas leído enteras y no declara esta ceguera.

---

## Hallazgos de la refutación

### R1 — La fecha atribuida a las notas oficiales no está en las notas oficiales
**Gravedad: alta (afecta a 22 citas).**
El informe escribe `(publicado 12 sep 2026)` junto a la URL de Blizzard en las 22 apariciones.
Comprobado directamente: la página **no muestra ninguna fecha de publicación**. Lo único fechado es la
cabecera del parche, literal: *"3.2.1 Build #73552 (All Platforms)—September 15, 2026"*.

El 12 de septiembre **sí existe**, pero es la fecha de **otra página**: el espejo de Maxroll
(*"Last Updated: September 12, 2026"*), que el informe **no cita en ningún sitio**.
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (sin fecha visible; cabecera de parche: 15 sep 2026)
- https://maxroll.gg/d4/news/diablo-4-3-2-1-patch-notes (12 sep 2026) — **fuente preferente no consultada**
- Evidencia: **oficial** (por inspección directa de ambas páginas)

**Corrección:** citar la fecha como *"cabecera de parche 15 sep 2026; notas espejadas por Maxroll el 12 sep 2026"*.
Regla 3 del encargo: se comprueba y se cita la fecha **de cada página**, no una fecha prestada de otra.

### R2 — Las notas distinguen PTR de live **por color**, y el informe no declara que no puede verlo
**Gravedad: alta (metodológica).**
Cita literal del cuerpo de las notas, justo antes del encabezado `PTR Bug Fixes`:
*"PTR changes are highlighted in blue."*

Es decir: el documento **sí** separa lo que venía del PTR 3.2.0 de lo añadido después, pero lo codifica
en un atributo visual que **desaparece en cualquier conversión a texto o markdown**. El informe afirma
*"las he leído enteras, no por resumen"* y presenta cada línea (F26, F35, F43–F46) como cambio vivo de
3.2.1 sin advertir que hay una capa del documento que su canal de lectura no alcanza.

Matiz honesto: **no es un error de hecho** —todo lo que está en las notas de 3.2.1 está en 3.2.1—, pero
la regla 6 del encargo pide distinguir PTR de final, y aquí no se puede. Debe ir a Huecos.
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy
- Evidencia: **oficial** (cita literal)

### R3 — F20 está mal etiquetado: no es "corroborado", es fuente única de origen PTR
**Gravedad: alta. Es el fallo más serio del informe.**

El informe marca F20 (reseteo semanal + escalera de recompensas) como **corroborado**, apoyándose en dos
fuentes. Las he separado y no sostienen lo mismo:

- **Maxroll (tower-guide, 29 jul 2026)**: buscado explícitamente, **no contiene las palabras "weekly",
  "week" ni ninguna referencia al tier 100**. Lo único que aporta es *"These start on Thursdays, leaving
  time after a new season and patch are launched"* — que habla del **día de arranque de las rondas**, no
  de la **cadencia**. Sobre reseteo solo dice: *"These are kept the whole Season, but are reset once the
  next season begins"* (reseteo **estacional**, no semanal).
- **Icy Veins (noticia S14)**: es la **única** fuente de "semanal" y de toda la escalera (jugado esta
  semana / tier 100+ / top 1.000-500-100-10-1 → halo, título de prestigio, alijo). Y su propia línea de
  atribución apunta a:
  `https://news.blizzard.com/en-us/article/24259077/the-3-1-ptr-what-you-need-to-know#Tower`
  → **un anuncio de PTR**, no una nota de parche final.

**La ironía es el hallazgo:** en C6 el informe descarta con razón el anuncio de la beta de S11 por ser
*"marco oficial caducado"*… y lo sustituye por un marco sacado de **otro anuncio prospectivo de PTR**,
sin darse cuenta. Escepticismo asimétrico: duro con la fuente vieja, blando con la que le da la razón.
- Evidencia: **disputa** → F20 debe bajar a **unica**, con la advertencia "origen PTR 3.1, sin confirmación en parche vivo".

**Salvedad justa:** la mitad de F21 (títulos y halos duran la temporada y caen en la siguiente) **sí**
está corroborada por Maxroll de forma independiente. Lo que no lo está es el **Emblema** de la temporada
siguiente, que también viene solo del post de Icy Veins / PTR 3.1.

### R4 — La verificación del marco (C5) es correcta pero se queda corta
**Gravedad: media. El informe acierta y aun así no toca fondo.**

Primero, **confirmo su cálculo**. Rehechos los acumulados de la propia página y sacado el factor por tier
entre filas consecutivas:

| Tramo | Factor por tier implicado |
|---|---|
| Falla 3 → 5 | ×1,26491 (**+26,49%**) |
| Falla 5 → 7 | ×1,26491 (**+26,49%**) |
| Falla 7 → 10 | ×1,16961 (**+16,96%**) |
| Falla 10 → 100 (todas las filas) | ×1,17000 (**+17,00%** exacto) |

El informe tiene razón: el tramo "4–10 a +26,5%" se rompe en el tier 8. Buen trabajo, y es exactamente el
tipo de comprobación que pedía la regla 5.

**Pero hay un piso más abajo que no pisó.** Los multiplicadores acumulados pre-Tormento son
×2,0 → ×3,2 → ×5,12 → ×8,192: **cada escalón es exactamente ×1,6**, y esos escalones abarcan
**2, 2 y 3 niveles de Falla** respectivamente. O sea: la tabla no está construida *por tier*, está
construida **por escalón de dificultad** (×1,6 cada uno), y la columna "Pit Level" es una **etiqueta de
equivalencia aproximada**, no la variable de la función.

Consecuencia: de esas filas **no se puede derivar ningún porcentaje por tier**, ni +26,5% ni +17%. El
+16,96% del tramo 7→10 no es "el juego cambia de tasa en el tier 8": es el artefacto de repartir un
escalón de ×1,6 entre 3 tiers en vez de 2. El informe cambia una lectura por tier por **otra lectura por
tier**, cuando el dato dice que el eje no es el tier.

De Tormento 1 (Falla 10) hacia arriba el +17%/tier **sí** es genuino y consistente en las 11 filas: esa
parte del informe es sólida.
- https://maxroll.gg/d4/resources/difficulty-overview (26 jun 2026)
- Evidencia: **disputa** (recálculo propio sobre las cifras de la fuente)

**Corrección:** C5 debe decir *"por debajo de Tormento 1 la tabla no permite derivar tasa por tier; de
Tormento 1 en adelante, +17%/tier verificado"*, en vez de *"el tramo bueno es 4–7 a +26,5%"*.

### R5 — F39: el desglose "300 + 42 = 342" es reconstrucción del investigador, no cita
**Gravedad: media.** (Check 3 del encargo: cada par valor→efecto debe salir de cita literal.)

Lo que dicen las fuentes, literal:
- Blizzard: *"Up to 42 Paragon points"*.
- Maxroll: *"Leveling from Paragon 1 to 300 after reaching level 70"*, *"When you complete all of these
  objectives, you gain up to 342 Paragon Points"* — y antes: **"There are only three ways to gain them"**.

**Ninguna de las dos publica el desglose.** El informe lo arma él (300 + 42) y presenta el encaje exacto
como confirmación mutua (*"encajan exactamente: 300 + 42 = 342"*). Pero si Maxroll dice que hay **tres**
vías y 300 + 42 ya agota los 342, la tercera vía aporta 0 puntos — lo cual es improbable — o el desglose
está mal repartido. El encaje perfecto no es prueba: es lo que pasa cuando eliges dos sumandos que dan el
total conocido.
- https://maxroll.gg/d4/resources/paragon-boards (9 jul 2026)
- Evidencia: **unica**, no corroborado. El **342** y el **300** son citables; el **desglose no lo es**.

### R6 — C8 se resuelve bien pero se extrae la lección equivocada
**Gravedad: media (contagia a F23 y F24).**
El informe dice que la lista de 6 clases de Icy Veins es *"un descuido suyo"*. No lo es. La lista
verificada es: *"Barbarian, Necromancer, Sorcerer, Rogue, Druid, Spiritborn"* — exactamente el elenco de
clases **anterior a la expansión Lord of Hatred** (incluye Espiritista, excluye Paladín y Brujo).

No es una errata: es **texto anterior a la expansión que nunca se actualizó**. Y eso cambia el diagnóstico
de toda la página, no solo de esa línea. F23 (filtro de plataforma) y F24 (Espectro Vampírico y "Sower of
Decay" excluidos), ambos marcados **unica** y ambos con esa página como única fuente, heredan la sospecha
de obsolescencia. He confirmado que las dos citas **existen literalmente**; lo que está en duda es su
vigencia, no su existencia.
- https://www.icy-veins.com/d4/guides/tower-leaderboards/ (sin fecha visible)
- Evidencia: **disputa**

### R7 — Huecos ocultos: dos páginas preferentes fechadas DENTRO de la ventana del parche, sin consultar
**Gravedad: baja-media.**
El informe da a entender que no existe fuente preferente fechada en el parche vivo. Existen dos:
- https://maxroll.gg/d4/news/diablo-4-season-15-compendium-season-launch-update (**14 sep 2026**)
- https://maxroll.gg/d4/resources/season-guide (**13 sep 2026**)

Comprobadas: **no añaden mecánica de endgame** —lo que en realidad **refuerza F16** (S15 no toca la Torre)—
pero la season-guide **corrobora de forma independiente** dos cosas que el informe daba por fuente única
oficial: *"Mephisto's Splinter of Hatred modifies The Pit and Nightmare Dungeons"* (F34) y
*"Up to 42 Paragon points"* (F41). Y ninguna de las dos menciona Torre ni Leaderboards.

Se suma la tercera no citada de R1 (el espejo de las notas 3.2.1 en Maxroll).
- Evidencia: **corroborado**

### R8 — El tramo 111+ es implausible de cara y no se señala como tal
**Gravedad: baja.**
El informe declara honestamente que el tramo 111–150 no se puede cruzar contra nada (hueco correcto).
Pero no señala que la fila es **sospechosa por su propia forma**: la vida por tier **sube** (17% → 32%)
mientras el daño por tier **baja exactamente a la mitad** (4,74% → 2,37%), justo en el punto donde la
tabla de acumulados se corta. Un hueco declarado está bien; un hueco declarado **más** la señal de alarma
está mejor.
- Evidencia: **sinconfirmar**

---

## Lo que NO he conseguido tumbar (verificado y en pie)

- **Sección "The Pit" de las notas**: reproducida palabra por palabra desde **dos** renderizados
  independientes (Blizzard directo y espejo de Maxroll). Coincide exactamente con F2–F5, incluidas las
  4 correcciones y el literal *"Example: Pit Tier 150 increased from 1800% to 2700%."* El recuento
  "2 de experiencia + 4 correcciones" es correcto (la línea "Example" es sub-viñeta de la segunda).
- **F16 — cero menciones a Tower/Leaderboard**: confirmado en los dos renderizados. La afirmación por
  ausencia es legítima y está bien hecha.
- **Fechas de Maxroll**: las cuatro que comprobé son **exactas** (pit-guide 16 jul, tower-guide 29 jul,
  difficulty-overview 26 jun, paragon-boards 9 jul). El informe no infla ni redondea fechas.
- **C1 (15 vs 10 minutos)**: real y bien planteada. Maxroll literal *"before the 15-minute timer runs
  out"*; Icy Veins habla de 10. Dejarla sin resolver es lo correcto.
- **F11 (9 intentos de glifo)**: literal *"4 attempts... 1 extra if you do not die... Up to 4 extra from
  nodes in the Pit Skill Tree from War Plans."* Correcto.
- **Hueco "Masteries"**: honesto. Confirmo que la palabra *"Mastery"* **no aparece** en la guía de la
  Falla de Maxroll, pese a que las notas oficiales nombran "Survival Mastery".
- **F27 y C9 (Hordas)**: literales verificados (400 / 1.000 / 666 Éter, 6-8-10 oleadas, 60 s, *"Further
  Infernal Hordes Compass can not be crafted"*). La resolución a favor de lo oficial es correcta.
- **F13, F39 (cifras), F42**: *"Glyphs can be upgraded all the way to level 150"*, *"15k gem fragments"*,
  *"up to 342 Paragon Points"*, *"9 unique Paragon Boards... maximum of 5 boards"*. Todos literales.
- **Ninguna fuente vetada.** Las 14 URLs son news.blizzard.com, maxroll.gg o icy-veins.com. Ni una de
  fextralife, primagames, beebom, gamespot, segmentnext, studioloot, gamerguides, pcgamesn o mythicdrop.
- **Fuera de parche declarado**: todas las páginas de Maxroll llevan su fecha citada y reconocida como
  anterior al parche; las de Icy Veins van marcadas *"sin fecha visible"*. En el check 2 el informe está
  limpio, salvo por R1.

---

## Contradicciones entre este refutador y el informe

**X1 — F20: "corroborado" (informe) vs "unica, de origen PTR" (yo).**
El informe cuenta dos fuentes; yo he comprobado que Maxroll no contiene la palabra "weekly" ni el umbral
de tier 100, y que la única fuente que sí los tiene se apoya en el anuncio del **PTR 3.1**. **Mi versión.**

**X2 — C5: "el tramo bueno es 4–7 a +26,5%" (informe) vs "de ese tramo no se deriva tasa por tier" (yo).**
Coincidimos en que la página se contradice y en el +17% de Tormento 1 hacia arriba. Discrepamos en la
lectura: él reubica la frontera del tramo, yo sostengo que los escalones son de ×1,6 por **dificultad**
(2, 2 y 3 tiers) y que la columna de Falla es etiqueta, no variable. **Mi versión, pero la suya no es
absurda:** ambas explican los números; la mía explica además por qué la frontera cae donde cae.

**X3 — Fecha de las notas: "12 sep 2026" (informe) vs "sin fecha visible; cabecera 15 sep 2026" (yo).**
**Mi versión**, por inspección directa. El 12 de septiembre pertenece al espejo de Maxroll.

**X4 — C8: "descuido de Icy Veins" (informe) vs "página pre-expansión sin actualizar" (yo).**
Misma conclusión práctica (gana la lista de 8 de Maxroll), distinta causa y distinta consecuencia: mi
lectura obliga a degradar F23 y F24. **Mi versión.**

**X5 — C11 (hora de lanzamiento).** El informe la deja sin resolver entre 16:30 UTC (briefing) y 17:00 UTC
(Icy Veins). Anoto sin resolverla que Maxroll también apunta a *"September 15, at 10:00 a.m."* (= 17:00
UTC), o sea **dos** preferentes contra el briefing. No afecta a ningún dato de endgame. **Sin resolver.**

---

## Correcciones concretas que pido antes de publicar

1. Sustituir las 22 apariciones de `(publicado 12 sep 2026)` por
   `(cabecera de parche: 15 sep 2026; espejo Maxroll fechado 12 sep 2026)`.
2. Bajar **F20** de `corroborado` a `unica` y añadir: *"la cadencia semanal y la escalera de recompensas
   proceden del anuncio del PTR 3.1, no de una nota de parche final"*. Partir **F21**: persistencia
   estacional = corroborado; Emblema = unica/PTR.
3. Añadir a **Huecos**: *"Las notas oficiales marcan los cambios de PTR en color ('PTR changes are
   highlighted in blue'). Leídas como texto, esa marca se pierde: no puedo decir de ninguna línea
   concreta si venía del PTR 3.2.0 o se añadió después."*
4. Reescribir la conclusión de **C5** según R4 (escalones de ×1,6 por dificultad; +17%/tier verificado
   solo de Tormento 1 hacia arriba).
5. En **F39**, marcar el desglose 300+42 como reconstrucción propia y anotar que Maxroll declara **tres**
   vías de puntos, no dos.
6. En **C8**, cambiar "descuido" por "texto anterior a Lord of Hatred", y marcar **F23** y **F24** con
   *"fuente posiblemente pre-expansión"*.
7. Añadir a fuentes las tres páginas preferentes no consultadas (notas 3.2.1 en Maxroll, compendio S15,
   season-guide) y usar las dos últimas para corroborar F34 y F41.
8. Opcional: anotar en el hueco del tramo 111+ que la fila es implausible por forma (vida acelera mientras
   el daño se reduce a la mitad).
