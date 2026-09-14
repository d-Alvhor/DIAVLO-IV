# s15-paladin — REFUTACIÓN

**Refutador independiente. Fichero aparte; el original no se ha tocado.**
**Método:** no he leído resúmenes. Me he descargado el HTML crudo de las tres páginas citadas
(`curl` + extracción de texto propia) y he contado término a término sobre el texto real,
incluyendo el **marcado de color del HTML**, que el investigador no miró.

Artefactos de verificación (reproducibles):
`/private/tmp/claude-501/-Users-alvhor-Proyectos-DIAVLO-IV/5523afd2-a68f-4a1a-aadb-a81c7ca2a218/scratchpad/`
→ `s15.html` / `s15.txt` (Blizzard), `mx.html` / `mx.txt` (Maxroll notas), `sc.html` / `sc.txt`
(Maxroll Shield Charge), `p31.html` / `p31.txt` (Blizzard 3.1.x).

## Resumen

1. **El informe NO es sólido, pero no por lo que cabría temer.** Sus cifras son buenas: he cotejado
   las 24 parejas valor→efecto del bloque Paladín contra el HTML de Blizzard y **todas son verbatim
   correctas**. No hay ni una fuente vetada. El fallo está en el marco y en dos omisiones.
2. **Omisión que rompe la tesis:** el parche **SÍ** sube Espinas. `Razorplate` —único genérico,
   equipable por Paladín— recibe *"Chance for Thorns to deal increased damage increased from 10% to
   30%"* y *"Bonus Thorns damage range increased from 180-200% to 200-250%"*. Está **dos líneas por
   encima de Tibault's Will**, que él sí reportó, y **en sus dos fuentes**.
3. **No separó PTR de final, teniendo el separador delante.** Blizzard escribe *"PTR changes are
   highlighted in blue"* y usa `color: rgb(65,105,225)` 592 veces. Al mapear ese color:
   **Juramento de Juggernaut 80→100, Shield of Retribution y los dos "riesgos de nerf" caen DENTRO
   del bloque azul.** El escalar 1.25→1.625 **no**.
4. **Fecha equivocada en las 24 filas `oficial`.** La página de Blizzard es del **12/09/2026**
   (`datePublished`), no del 15/09: eso es el sello de build, no la fecha de página. Y su segunda
   fuente (Maxroll) es un espejo del mismo texto publicado 5 h después → su `corroborado` es `unica`.
5. **Dos huecos declarados son falsos:** el tope de Resolve y el Block Chance de Crusader's March
   están publicados con cifra en las notas 3.1.x que él mismo cita.

---

## Hallazgos

### R1. [oficial] OMISIÓN QUE ROMPE LA TESIS — Razorplate sube Espinas en 3.2.1

El informe afirma dos veces que el único retoque a Espinas es Shield of Retribution
(líneas 75-76 y tabla D). **Es falso.** Texto literal de la sección genérica de objetos únicos:

> **Razorplate**
> Chance for Thorns to deal increased damage increased from 10% to 30%.
> Bonus Thorns damage range increased from 180-200% to 200-250%.

- URL: https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy
- Fecha de página: **12/09/2026** · Evidencia: **oficial**
- Secuencia exacta en la página: `Melted Heart of Selig` → **`Razorplate`** → **`Tibault's Will`**.
  Es decir: el investigador **leyó esa lista** (de ahí sacó Tibault's Will) y saltó las dos líneas
  inmediatamente anteriores.
- Verificado también en su segunda fuente (`mx.txt`, Maxroll, 12/09/2026): mismo texto, misma
  posición. **No hay excusa de fuente incompleta: estaba en las dos.**
- Razorplate no figura en ninguna lista de restricción de clase del parche (las únicas restricciones
  a Paladín en 3.2.1 son `X'Fal's Corroded Signet` y `Banished Lord's Talisman`).

**Impacto:** para una build de espinas esto es el hallazgo más accionable del parche y el informe lo
publica como inexistente. La frase *"A tu build no la han tocado"* del Resumen queda desmentida.

### R2. [oficial] La afirmación "las demás menciones de Thorns son de Spiritborn y Brujo" es doblemente falsa

Recuento completo de las 14 apariciones de "Thorns" con su sección propietaria (`s15.txt`):

| Sección | Línea |
|---|---|
| PTR Bug Fixes | Henri's Perquisition tenía un afijo de Espinas de más |
| **Paladin Skills** | Shield of Retribution escala con rangos |
| Spiritborn (Changes/Skills/Paragon/Talisman/Bug Fixes) | 9 líneas |
| **Objetos únicos genéricos → Razorplate** | **2 líneas (ver R1)** |

- **Brujo/Warlock: 0 menciones de Thorns.** Comprobado acotando la sección Warlock: `grep -c` → `0`.
  El informe inventa una atribución que no existe.
- Razorplate no es ni Spiritborn ni Brujo.

### R3. [oficial] PTR vs final: el separador estaba en la fuente primaria y no se usó

Línea 190 del texto de Blizzard, inmediatamente bajo la cabecera de build:

> 3.2.1 Build #73552 (All Platforms)—September 15, 2026
> **PTR changes are highlighted in blue.**
> PTR Bug Fixes

En el HTML ese azul es `color: rgb(65,105,225)`, **592 apariciones**. Mapeado sobre la sección
Paladín en orden de documento:

| Bloque | Marcado |
|---|---|
| Core stat scalar 1.25→1.625 · Judgement escala con rango · Holy Bolt · Shield of Justice · Fist of the Heavens | **sin azul** |
| **Divine Lance · Zeal · Shield of Retribution (Thorns/rangos) · Shield Bash** | **AZUL** |
| Judicator Oath (efecto nuevo) | **sin azul** |
| **Disciple Oath 80→100 · Juggernaut's Oath 80→100 · Zealot Oath 25→35** | **AZUL** |
| Watkin's Law · Aspect of the Judicator · Cathedral Song · X'Fal's · Heaven's Radiant Fire | **sin azul** |
| **Cathan's Righteous Will 10→15 s** | **AZUL** |
| Bug fixes: Spear of the Heavens · Advance · Brandish · Arbiter · Fanaticism · Zenith · Wing Strikes · DoT | **sin azul** |
| **Aspect of the Indomitable · Aegis · Iron Conviction · Clash's Skirmish · Divine Lance ×3 · Shield Bash Smite** | **AZUL** |

**Consecuencia directa:** los dos buffs que el informe vende como "los que sí te llegan" están
repartidos — el escalar de Fuerza **no** es azul, pero **el Juramento de Juggernaut 80→100 SÍ**. Y el
único retoque a Espinas que él encontró (Shield of Retribution) **también es azul**. Igual sus dos
"riesgos de nerf encubierto" (Indomitable) y su "buff indirecto" (Clash's Skirmish).

Su Hueco 8 afirma: *"Los valores que doy arriba son los del texto final de 3.2.1, no los del PTR."*
**No puede sostener eso**, y además atribuye el marcado azul a Icy Veins cuando **es de Blizzard**.

> **Calibración honesta (mía):** puedo demostrar que el marcado existe y qué líneas lo llevan. **No**
> puedo demostrar si "azul" significa *"venía ya del PTR 3.2.0"* o *"cambiado respecto al PTR"*.
> Esa ambigüedad es exactamente lo que el informe debía declarar y no declaró. Evidencia: **oficial**
> para el marcado; **sinconfirmar** para su semántica.

### R4. [oficial] Fecha incorrecta en las 24 filas `oficial`, y `corroborado` que en realidad es `unica`

| Página | `datePublished` | `dateModified` | Fecha que cita el informe |
|---|---|---|---|
| Blizzard S15 (fuente primaria única) | **2026-09-12T18:15:00Z** | 2026-09-12T18:15:00Z | 15/09/2026 |
| Maxroll notas 3.2.1 | **2026-09-12T23:15:22Z** | 2026-09-12T23:46:40Z | 12/09/2026 |
| Maxroll Shield Charge | 2025-12-12 | **2026-09-14T08:21:43Z** | 14/09/2026 ✔ |

- El "15/09/2026" que repite 24 veces es el **sello de build dentro del texto**, no la fecha de la
  página. La regla de la casa ("comprueba la fecha de cada página y cítala") se incumple en bloque.
- **Independencia rota:** Maxroll publica **5 h 00 min después** de Blizzard y es un espejo literal
  (mismo texto, mismo orden, mismas cifras). Su tabla D se apoya en "Blizzard + transcripción de
  Maxroll" y la grada **`corroborado`**. Dos copias del mismo texto **no son dos fuentes**:
  esa tabla es **`unica`**.
- Matiz a mi favor y en su contra a la vez: el `dateModified` de Blizzard **no se mantiene** (el
  artículo 3.1.x declara 2026-06-23 y contiene 3.1.3 del 12/08/2026). Así que **no puedo probar** que
  la página no se haya tocado en el lanzamiento. Lo verificable es: **publicada el 12/09, antes del
  parche, y nada re-verificado tras las 16:30 UTC de hoy.**

### R5. [oficial] Entrada falsa en la tabla de ausencias + error de marco sobre Resolve

El informe (tabla D): *"**Resolve** | Una sola vez, y es un bug fix de templado"*. **Aparece dos veces:**

> L1288 · Tempering · "Fixed an issue where Maximum Resolve Stacks was uncapped when Tempering."
> L848 · **Spiritborn Bug Fixes** · "Fixed an issue where the Colossal Glyph would not increase damage
> per stack of **Resolve** for skills that apply Damage Over Time."

Y el error de marco es mayor que el recuento. **Resolve no es un recurso del Paladín: es un buff
apilable compartido por varias clases.** Verificado en las notas 3.1.x que el propio informe cita:

- Spiritborn: *"Concussive Stomp would not grant Resolve…"*
- Druida: *"Stone Burst Armor side upgrade no longer grants additional armor for each stack of Resolve."*
- Bárbaro: *"Iron Skin's Resolve stacks were removed when swapping weapons."*
- Nigromante: *"Resolve stacks from Golem's upgrade could fall off randomly."*
- Paladín: *"Clash — Seize Them Variant: Now capped at 16 stacks of Resolve."*

El fix de 3.2.1 está en la sección **Templado, agnóstica de clase**. Su glosa *"Un Juggernaut vive de
ese máximo"* presenta como propio del Paladín un mecanismo compartido. **Su conclusión de riesgo
acaba siendo correcta** (ver R6: el Resolve Temper es real y ya fue nerfeado antes), pero llega ahí
**sin la evidencia**, que existía y no buscó.

### R6. [oficial] Dos huecos declarados son falsos — la cifra está en una fuente que él mismo cita

Artículo de notas 3.1.x, https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes
(página del 23/06/2026, contiene 3.1.1–3.1.3 hasta 12/08/2026):

- **Su Hueco 4** — *"nadie publica cuál es el tope legítimo [de Resolve] ni cuánto recorta"*. Ahí está,
  con cifra: *"Clash — Seize Them Variant: **Now capped at 16 stacks of Resolve**."* Y además:
  *"Fixed an issue where the **Resolve Temper** was scaling with item types and much more than intended
  with Masterworking ranks."* → **el Resolve Temper ya fue corregido una vez en 3.1.x**; el de 3.2.1
  es el **segundo** recorte al mismo afijo. Eso es un patrón, no un hueco.
- **Su Contradicción 2 / Hueco sobre Crusader's March** — se apoya solo en la descripción cualitativa
  de Maxroll. La cifra está publicada: *"**Clash — Crusader's March Block Chance increased from 15% to
  30%**."* También: *"Fixed an issue where [skills] did not correctly apply Damage Reduction effects
  based on **Block Chance** bonuses."*

### R7. [oficial] Omisiones menores pero reales del texto oficial

- **Fist of the Heavens: se comió el nerf.** Son dos líneas y el informe las funde en una:
  *"Enemies hit by the main impact can now also be hit by one of the additional projectiles."* +
  *"**Enemies can now only be damaged by one of the additional projectiles.**"* La segunda es un tope
  nuevo. Es el único sitio donde su paráfrasis pierde información frente al original.
- **Segundo objeto retirado al Paladín, no reportado:** *"**Banished Lord's Talisman** — No longer
  dropped for or usable by Paladin, Spiritborn, or Warlock."* El informe solo cita X'Fal's.
- **Doble cómputo eliminado, no reportado:** *"Fixed an issue where **Zenith** could benefit from both
  Sunder and Sermon of Steel at once."* Es un nerf de bloqueo/defensa que no aparece en su sección F.
- **Línea de Espinas redactada de forma agnóstica y descartada:** *"Fixed an issue where effects that
  dealt damage based on your **Thorns** amount would sometimes deal less damage than intended."* Está
  archivada bajo *Spiritborn Bug Fixes*, pero **su redacción no nombra clase**. El informe descartó el
  bloque entero como "no tuyas". Podría ser un arreglo de motor que beneficie a cualquier build de
  espinas. **Evidencia: sinconfirmar** — pero es un hueco que él no declaró.

### R8. [corroborado] Lo que SÍ resiste — y no es poco

Doy fe de esto porque lo he vuelto a medir yo, no por cortesía:

- **Las 24 parejas valor→efecto del bloque Paladín son verbatim exactas.** Diff completo contra el
  HTML crudo: escalar 1.25→1.625, Juggernaut/Disciple 80→100, Zealot 25→35, Judicator +100%,
  Divine Lance 90→110 / 35→39 / 74→91 / 99→121 / 495→605, Zeal 20→35, Shield Bash 246→349 y
  287→451 / 102→307, Watkin's Law 45-65%, Judicator 40-60→60-80, Cathedral Song, X'Fal's,
  Heaven's Radiant Fire 25%[x]/20/5, Cathan's 10→15 s, Tibault's 50→25, DoT retirados. **Cero errores
  numéricos.** Ninguna cifra es paráfrasis.
- **Ausencias confirmadas (recuento propio, 0 apariciones):** Shield Charge, Defiance/Defiant,
  Block Chance, Blocked Damage, Punish, Herald of Zakarum, Mantle of the Gray(s), Fists of Fate,
  Bloodthirsting, Crusader's March. *Retribution* solo aparece dentro de "Shield of Retribution" → la
  mecánica no se menciona: **correcto**. Ojo a dos falsos positivos que yo mismo me comí y él no:
  "Condemn" aparece 2 veces pero es **Condemnation**, único de Pícaro; "Penitent" aparece 1 vez pero es
  la **dificultad Penitent**, no Penitent Greaves. **Sus dos "No" eran correctos.**
- **Ninguna fuente vetada.** Solo `news.blizzard.com`, `maxroll.gg`, `icy-veins.com`. Limpio.
- **"Las notas de 3.2.1 no tienen artículo propio": correcto.** El artículo rodante
  `/24287406/diablo-iv-patch-notes` contiene **0** apariciones de "3.2." (solo 3.1.1–3.1.3).
- **Su Contradicción 3 (contaminación 3.1.x) es impecable.** Verificadas verbatim las nueve:
  Shield Charge 90→180 y CD 10→8 s, Defiance Aura 30→50%, Stalwart 5→15%, Aegis +30% armadura,
  Juggernaut/Judicator 60→80, Disciple 50→80, Zealot 21→25 por eco, Wing Strikes 160→200. Y también
  *"Shield of Retribution Variant: Thorns damage reduced from 100% to 70%"* → efectivamente **3.1.x,
  no 3.2.1**, como él dijo.
- **Las cuatro citas verbatim de la guía Maxroll son auténticas**, incluida la de *Aspect of
  Excellence* (llegué a sospechar que la había confundido con *Aspect of the Juggernaut's Covenant*,
  que dice algo parecido dos frases antes; **no la confundió**).
- **Su lectura de la guía como "S14 re-fechada" está bien fundada:** `dateModified` 14/09/2026,
  `datePublished` 12/12/2025, dice "Season 15" 7 veces, "Season 14" 0 veces, y **"3.2.1" 0 veces**.

### R9. [unica] Hueco que él no vio en la guía viva: recomienda el objeto nerfeado

La guía Maxroll Shield Charge (14/09/2026) lista en su párrafo de equipo: Leoric's Crown,
Mantle of the Grey, **Tibault's Will**, Abyssal Splinter of Pain, Penitent Greaves, Herald of Zakarum.
El informe reproduce esa lista **omitiendo Tibault's Will y Abyssal Splinter of Pain**.

> *"**Tibault's Will** helps sustain your Faith costs and gives you a small boost in damage as well.
> Activate it with Defiance Aura or Fortress."*
> — https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide (14/09/2026)

El informe tiene los dos hechos separados —la guía viva por un lado, el nerf de Tibault's Will
50%→25% por otro— y **nunca los junta**. La única build endgame viva de S15 recomienda precisamente el
único objeto que 3.2.1 recorta a la mitad. Eso es lo primero que debía leer el jugador.

Y la misma guía desmiente que el vínculo Juramento→Espinas sea inexistente, cosa que su
Contradicción 1 deja en el aire:

> *"Aspect of Lapa's Scripture works with the **Juggernaut Oath** to grant you **Thorns** when spending
> **Resolve**."* · *"Mantle of the Grey … turns your spent Resolve into damage."* ·
> *"Aspect of Glynn's Anvil gives you … damage reduction … based on your current Resolve stacks."*

Es decir: **Resolve es el eje de esta build**, lo que eleva —no baja— la gravedad del fix de templado
de R5/R6. Su instinto era bueno; su evidencia, inexistente.

---

## Huecos (míos, declarados)

1. **No puedo determinar la semántica del azul de Blizzard** (¿"venía del PTR" o "cambiado respecto al
   PTR"?). Probado: el marcado existe y qué líneas lo llevan. No probado: qué significa.
2. **No puedo probar si la página de Blizzard se editó el 15/09.** Su `dateModified` no se mantiene
   (demostrado con el artículo 3.1.x). Solo sé que se publicó el 12/09.
3. **No he verificado la fila de Icy Veins** del informe (Blessed Shield, 13/09/2026). Es periférica a
   una build de espinas y no sostiene ninguna cifra suya.
4. **La guía Maxroll rinde solo 18 KB de texto de 489 KB de página** (resto en JS). Mis recuentos sobre
   ella (Razorplate 0, Crown of Lucion 0) valen para lo servido en HTML, no para lo que carga después.
5. **Si "Razorplate" sigue siendo equipable por Paladín en el cliente**: lo deduzco por ausencia de
   restricción en el parche, no por tooltip verificado. **sinconfirmar.**
6. **Sigue sin haber un solo dato de juego real de S15.** En esto el informe acierta de pleno y su
   aviso de estado es lo mejor que tiene.

---

## Contradicciones

**1. "El único retoque a Espinas es Shield of Retribution" (informe) vs. Razorplate (Blizzard).**
Versión del informe: *"Shield of Retribution es el ÚNICO retoque a Espinas del Paladín en todo 3.2.1"*
(línea 75) y *"Las demás menciones de Thorns del parche son de Spiritborn y Brujo, no tuyas"* (tabla D).
Versión de la fuente: `Razorplate` sube probabilidad de Espinas aumentadas 10%→30% y rango 180-200%→
200-250%, en la lista genérica de únicos, sin restricción de clase. **Gana la fuente.**

**2. "Mis valores son los finales, no los del PTR" (informe) vs. el propio azul de Blizzard.**
Versión del informe (Hueco 8): *"Los valores que doy arriba son los del texto final de 3.2.1, no los
del PTR"*, atribuyendo el marcado azul a Icy Veins.
Versión de la fuente: *"PTR changes are highlighted in blue"* — en Blizzard — con el Juramento de
Juggernaut, Shield of Retribution, Tibault's Will, Indomitable y Clash **dentro del azul**.
**Ninguna de las dos versiones está probada del todo; la del informe está además mal atribuida.**

**3. "Resolve aparece una sola vez" (informe) vs. dos apariciones y cinco clases.**
Versión del informe: una aparición, y es del Paladín-Juggernaut.
Versión de la fuente: dos apariciones en 3.2.1, y en 3.1.x Resolve se documenta en Paladín, Spiritborn,
Druida, Bárbaro y Nigromante. **Gana la fuente**; la conclusión de riesgo del informe sobrevive, su
fundamento no.

**4. Yo mismo contra mi primer recuento.** Mi `grep` inicial marcó "Condemn" y "Penitent" como
presentes y habría acusado al informe de dos falsas ausencias. Al abrir el contexto eran
**Condemnation** (único de Pícaro) y la **dificultad Penitent**. Lo dejo escrito porque es el mismo
error que el informe evitó: **contar términos sin leer el contexto**. Él lo hizo bien.

---

## Veredicto

**NO SÓLIDO — publicable solo con cuatro correcciones.** No por fabricación: es un informe con las
cifras limpias, sin fuentes vetadas y con un aviso de estado ejemplar. Falla en que **presenta una
ausencia que no existe** (Razorplate), **afirma una separación PTR/final que no hizo** teniendo el
separador en el HTML, **fecha mal sus 24 filas oficiales**, y **declara como huecos dos cifras que
están publicadas en una fuente que él mismo cita**.

Correcciones obligatorias antes de que nada de esto entre en la guía:
1. Añadir Razorplate y retirar "el único retoque a Espinas" y "las demás son de Spiritborn y Brujo".
2. Añadir la columna PTR-azul a las tablas B, C y F, y reescribir el Hueco 8.
3. Fechar las páginas por `datePublished` (12/09/2026) y bajar la tabla D de `corroborado` a `unica`.
4. Cerrar los Huecos 4 y el de Crusader's March con las cifras de 3.1.x (16 acumulaciones; 15%→30%),
   y unir en una sola frase que la guía viva de S15 recomienda Tibault's Will, el objeto nerfeado.
