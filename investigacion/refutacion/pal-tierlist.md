# Refutación adversarial — `crudo/pal-tierlist.md`

**Verificador:** pasada adversarial independiente.
**Fecha:** 19 de agosto de 2026.
**Parche vivo de referencia:** 3.1.3 (build 73224, 12/08/2026).
**Veredicto:** **PARCIAL** — las 12 afirmaciones principales resisten; el aparato que las rodea tiene 5 defectos reales, uno de ellos un número mal citado.

---

## 0. Resumen ejecutivo

He intentado tirar abajo el informe. **No he podido tumbar ninguna de las 12 afirmaciones que declara haber
confirmado.** Las he reabierto una por una y salen idénticas, letra por letra y fecha por fecha.

Lo que sí he encontrado son fallos en los márgenes, y dos de ellos son del tipo que este proyecto ya se ha
comido antes:

| # | Defecto | Gravedad |
|---|---|---|
| E1 | **Número mal citado:** Juramento Juggernaut "60-50% → 80%". El parche dice **60% → 80%**. El "50%" es de **otro** juramento (Disciple). | **Alta** — es un par valor→efecto incorrecto |
| E2 | **"No encontrado" #6 es falso.** El tope de Resolución 30, Glynn's Anvil y el set Phoba **están literalmente en la guía de Maxroll** que el informe dice haber abierto. | **Alta** — contradice su propia declaración de cobertura |
| E3 | **"No encontrado" #9 es falso.** Sí existen tier lists explícitamente de PTR para S14, y dicen lo contrario que el parche vivo. | **Alta** — es justo la trampa que el encargo mandaba cazar |
| E4 | **Mala atribución:** el informe carga a vortexgaming.io una lista de objetos que esa página **no contiene**. | Media |
| E5 | **Error de recuento:** "cuatro de Bárbaro" en la S global de empuje. Son **cinco**. | Baja |

Ningún defecto es una invención de dato a favor de una conclusión. El informe peca de **falso pesimismo**
(declara no verificado lo que sí estaba a la vista) más que de exceso de confianza. Es el fallo menos peligroso
de los dos, pero sigue siendo un fallo.

---

## 1. Lo que NO he podido refutar (todo verificado de nuevo)

Reabrí cada página y comparé contra el informe. Coincidencia exacta en los 12 puntos.

### 1.1 Listas por clase de Paladín — las cuatro, clavadas

| Lista | Fecha declarada | ¿Coincide mi lectura? |
|---|---|---|
| `paladin-endgame-tier-list` | 22/07/2026 | **Sí, exacta.** S vacía; A = solo Shield Charge; B = Divine Lance, Clash, Shield of Retribution, Blessed Hammer; C = Zeal, Wing Strikes, Brandish, Auradin, Shield Bash; D = Zenith, Judgement |
| `paladin-push-tier-list` | 22/07/2026 | **Sí, exacta.** S = Support zDPS; A = Shield Charge, Clash; B = Shield of Retribution, Zeal, Blessed Hammer, Divine Lance; C = Brandish, Zenith, Shield Bash; D = Wing Strikes, Judgement, Auradin |
| `paladin-speedfarming-tier-list` | 22/07/2026 | **Sí, exacta.** S = Wing Strikes, Blessed Hammer; A = Auradin, Shield Charge, Divine Lance, Zeal; B = Zenith, Brandish; C = Clash, Shield of Retribution, Shield Bash; D = Judgement |
| `paladin-leveling-tier-list` | 30/06/2026 | **Sí, exacta.** S = Shield of Retribution; A = Blessed Hammer; B = Zeal, Judgement. C y D vacías. Shield Charge no aparece |

**El changelog "Added Shield Charge — July 20, 2026" existe** y está tanto en la lista de endgame de Paladín
como en la de push. El informe lo cita en la de push: correcto.

**La cita de criterios de leveling es literal y correcta.** Verbatim de la página:
> "This tier list ranks Paladin builds by the most important factors of leveling: Movement speed, survivability,
> ease of play, damage output and total time to reach level 70 in a season start scenario without resources,
> tempers or aspects unlocked."

### 1.2 Listas globales — las cuatro, clavadas

| Lista | Fecha | Shield Charge | Las tres de Bárbaro |
|---|---|---|---|
| `endgame-tier-list` | 22/07/2026 | **A** | Whirlwind, Mighty Throw, Minion → **S** (la S tiene 4: esas tres + Evade Counterswarm Spiritborn) |
| `push-tier-list` | 23/07/2026 | **A** | Las tres en **S**; la S tiene 11 builds |
| `bossing-builds-tier-list` | 22/07/2026 | **S** ← empate confirmado | Las tres en **S**; la S tiene 15 |
| `speedfarming-tier-list` | 22/07/2026 | **A** | Las tres en **S** |

**El empate en bossing es real.** La S de bossing incluye, verificado: Whirlwind Barb, Minion Barb,
**Shield Charge Paladin**, Firewall Sorc, Flame Charge Barb, Mighty Throw Barb, Golem Necro, Blood Wave Necro,
Army of the Dead Necro, **Shield of Retribution Paladin**, Rapid Fire Rogue, Heartseeker Rogue, Rain of Arrows
Rogue, Evade Counterswarm Spiritborn, Death Trap Rogue.

> **Falso positivo mío, declarado:** en mi primera lectura de la lista de bossing me salió que Divine Lance y
> Brandish estaban en D, lo que habría contradicho el "C" del informe. Al releer la página pidiendo el desglose
> completo de B/C/D, **el informe tiene razón: ambas están en C.** Mi primera lectura era incompleta. Lo dejo
> escrito para que no se me cuele como hallazgo lo que era ruido de mi propia extracción.

### 1.3 Míticos — orden exacto, ambas variantes

Reabierta `shield-charge-paladin-guide` (25/07/2026, "Season 14 - Death Awakening"):

- **Endgame:** "1. Mantle of the Grey 2. Tibault's Will 3. Herald of Zakarum" ✅
- **Push:** "1. Mantle of the Grey 2. Blood-Mad Idol (only for Push variant) 3. Tibault's Will 4. Herald of Zakarum" ✅

### 1.4 La regla del Mítico fabricado — literal y corroborada

Verbatim en `shield-of-retribution-paladin-guide` (27/07/2026):
> "You can only equip one Mythic item that you have crafted through the Horadric Cube, but are able to equip
> all Mythics that are acquired elsewhere."

Verbatim en `minion-barbarian-guide` (18/07/2026):
> "Note: You can only equip one Mythic that you craft in the Horadric Cube with Pandemonium Fragments."

**Hallazgo a favor del informe que el informe no se apuntó:** la misma frase está **también en la propia guía de
Shield Charge**. Es decir, la regla está corroborada en **tres** guías de Maxroll, no en dos. El informe se
infravaloró aquí.

Su cautela de fondo sigue siendo correcta: **no aparece en las notas oficiales de Blizzard.** Sigue siendo nota
editorial de Maxroll.

### 1.5 El 5→4 de Fragmentos de Pandemónium — confirmado, y por partida doble

Verbatim en las notas oficiales, parche 3.1.1:
> "Reduced the cost of the Upgrade to Mythic recipe on the Horadric Cube from 5 to 4 Pandemonium Fragments."

Corroborado además por fuentes secundarias independientes que fechan el 3.1.1 el 14/07/2026.

### 1.6 La cadena metodológica "no hay balance desde el 3.1.0" — aguanta

Es el argumento que sostiene todo el informe (tier lists de julio válidas en agosto). Lo he atacado por fuera de
Maxroll y **resiste**:

- **3.1.2 (28/07/2026):** verificado en la noticia de Maxroll. Solo bugs; el único arreglo de clase es de Pícaro
  ("Fixed an issue where Rogue's Dash could deal an incorrect amount of damage..."). Sin balance.
- **3.1.3 (12/08/2026):** verificado **en Icy Veins**, fuente preferente e independiente de Maxroll. Confirma
  cero cambios de balance: solo arreglos de Druida (Petrify), Nigromante (skills de Sombra) y Brujo (Dark Prison).
  **Paladín y Bárbaro: ningún cambio.**

**La conclusión metodológica del informe es sólida y ahora tiene corroboración externa.**

### 1.7 Páginas bloqueadas — confirmadas, y peor de lo que dice

- `mobalytics.gg/diablo-4/paladin-builds-tier-list` → **403 confirmado.**
- **Añado:** también dan 403 `mobalytics.gg/diablo-4/builds/paladin-shield-charge-endgame-build-guide` y otras
  rutas del dominio. **Mobalytics está bloqueado a nivel de sitio**, no solo esa URL. El informe se quedó corto.
- `wowhead.com/.../shield-charge-build-overview` → **confirmado: solo navegación.** Además su cabecera pone
  "Updated: 2026/03/08", **anterior al lanzamiento del Paladín** (3.0, 28/04/2026). Inservible, sí.
- **Maxroll no dio 403 en mi sesión tampoco.** La regla 4 del encargo no se activó esta vez, para ninguno de los dos.

### 1.8 Comprobaciones de higiene que pasa limpio

- **Ninguna fuente vetada respalda ningún número del informe.** Repasadas las 20 fuentes: ni fextralife, ni
  primagames, ni beebom, ni gamespot, ni segmentnext, ni studioloot, ni gamerguides, ni pcgamesn, ni mythicdrop.
  **Limpio.**
- **Ningún dato de PTR presentado como parche vivo.** Los números publicados salen de notas oficiales y de
  páginas de Maxroll fechadas en parche vivo. (El fallo relacionado es de omisión, no de contaminación: ver E3.)
- **Pros y contras:** las cuatro tablas de la sección 4.6 son citas literales correctas. Verificadas una a una
  en Whirlwind (12/08/2026), Mighty Throw (05/07/2026) y Minion Barb (18/07/2026).
- **La rotación de Mighty Throw** que el informe describe ("mantener pulsado Torbellino y soltar de vez en cuando
  defensivas/utilidad") es correcta pese a sonar rara en una build llamada Mighty Throw. La guía dice literalmente
  "Hold-down (all the time): Whirlwind" y "Cast every 4 sec: Rallying Cry".
- **"No existe marcador numérico en las guías de Maxroll":** confirmado. Ni la de Shield Charge ni la de Mighty
  Throw tienen panel de puntuaciones. El informe acierta.
- **"Las listas de Maxroll no dan números de Foso":** confirmado, y ampliado. Comprobé además
  `barbarian-push-tier-list`, la lista donde más cabría esperarlos: **solo letras**. Su criterio, verbatim:
  "This Tier List defines the performance of Barbarian builds with a particular focus on pushing the Pit and
  Tower to the highest tiers possible..." — describe el eje, no publica cifras.
- **Índice de guías de Paladín:** 13 de endgame y 5 de leveling, con las fechas que da el informe. Correcto.
  **No existe guía de leveling de Shield Charge para S14**: confirmado.
- **d4guides.gg:** confirmada la caracterización del informe. Fechada 16/08/2026, mezcla alemán e inglés
  ("Flügelschlag / Wing Strikes", "Gesegneter Schild / Blessed Shield"), atribuye builds a usuarios
  (**incluido "Foxman"**, tal cual lo cita el informe) y coloca Shield Charge solo como S-tier de **leveling**.
  Es repositorio de comunidad, no lista editorial. **El informe la descarta con criterio correcto.**

---

## 2. Los defectos reales

### E1 — Juggernaut "60-50% → 80%" es un número mal citado *(gravedad alta)*

**Dónde:** "No encontrado" #8.
> "el parche buffeó Wing Strikes, Defiance, Aegis y los Juramentos (incluido **Juggernaut, 60-50% → 80%**...)"

**Lo que dice el parche 3.1.0, verbatim:**
> "Juggernaut Oath - Damage increased from **60% to 80%**."
> "Disciple Oath - Damage increased from **50% to 80%**."

**Diagnóstico:** el informe **fusionó dos entradas distintas en una**. El "50" no es de Juggernaut, es de
Disciple. Pregunté explícitamente si algún juramento se escribe "from 60-50% to 80%" y la respuesta fue que
**ninguno**: el formato de las notas es uniforme "from X% to Y%".

**Por qué importa aquí:** Juggernaut es un juramento que **la build de Shield Charge sí usa** (el propio informe
lo dice en 5.3). Es un par valor→efecto tocando la build del jugador. Es exactamente lo que la regla 5 del
encargo prohíbe: un número que no sale literal de su fuente.

**Corrección:** Juggernaut 60% → 80%. Y si se quiere citar el 50%, es Disciple 50% → 80%.

**Verificado de paso:** los demás números de 3.1.0 que cita el informe **sí** son correctos —
Wing Strikes "Base damage increased from 160% to 200%" ✅ y Defiance "Bonus Armor and Resistances increased
from 30% to 50%" ✅. El fallo es puntual, no sistemático.

### E2 — "No encontrado" #6 declara no verificado lo que estaba en la propia guía *(gravedad alta)*

**Dónde:** aviso al final de 5.3 y "No encontrado" #6.
> "esto aparece en extractos de buscador y en una fuente secundaria sin fecha (...). **No he podido verificarlo
> en la página de Maxroll abierta directamente.** Trátalo como pista de por dónde mirar, no como dato confirmado."

**Refutación.** Abrí `shield-charge-paladin-guide` y pedí explícitamente esos términos. Están, **verbatim**:

> "Reach the **Resolve cap of 30** by tempering '+4 Maximum Resolve Stacks' on Helm, Chest and Pants."

> "Aspect of **Glynn's Anvil** and the **Phoba of Righteous Will** set to reach exactly 30 Maximum Resolve."

Y la mecánica de Espinas, también literal:
> "Shield Charge to deal Physical **Thorns** damage to your enemies through direct hits and **Retribution**
> pulsing around you everytime you block."

**Diagnóstico:** el tope de Resolución 30, Glynn's Anvil y el set Phoba **no son "pistas sin verificar": son
dato de fuente primaria en la guía viva.** El informe los mandó a "No encontrado" por error.

**Esto además contradice al propio informe.** En la sección 7 afirma: *"Maxroll NO dio 403 en esta sesión. Las 20
páginas de Maxroll que cito las he abierto de verdad."* Si abrió esa guía —y de ella sacó el orden de Míticos y
los pros/contras—, el párrafo de Resolución estaba en la misma página. **O no la leyó entera, o la declaración de
cobertura de la sección 7 es más generosa que la lectura real.** No es un dato falso publicado, pero sí una
declaración de método que no se sostiene.

**Nota:** de la lista discutida, lo que sigue **sin** confirmar es *Rite of Thorns*, *Punishment*, *Impunity* y
*Aspect of Lapa's Scripture*. Y hay una razón estructural que el informe no detectó y que sí conviene decirle al
jugador: la guía **no enumera el equipo en texto**, lo mete en el planificador D4Planner incrustado. Verbatim de
lo que sí hay en texto: *"Armor and Maximum Life and the Aspects provided in the planner"*. Para la lista completa
de piezas hay que ir al planificador, no a la prosa de la guía. Eso es un hueco real; el que declaró el informe
era el hueco equivocado.

### E3 — "No encontrado" #9 es falso: las tier lists de PTR existen y dicen lo contrario *(gravedad alta)*

**Dónde:** "No encontrado" #9.
> "Encontré la advertencia general de que mucho material de Paladín es de la beta, pero **no localicé ninguna
> tier list explícitamente de PTR** que pudiera contrastar. (...) No hay nada marcado ⚠️ por PTR en este informe
> **porque no encontré nada de PTR que citar**, no porque lo haya descartado."

**Refutación.** Aparecen a la primera búsqueda, y son abundantes:

| Fuente PTR | Qué afirma |
|---|---|
| u4gm — "Diablo 4 Season 14 **PTR** Paladin Dominates the Meta with S Tier Power" | "the Paladin is the absolute king of the patch"; "this class has secured **multiple S-Tier builds**" |
| mmoexp — mismo titular, réplica | ídem |
| u4gm — "Diablo 4 Season 14 **PTR** Build Tier List: Best Classes and Builds" | tier list de PTR completa |
| iggm — "Diablo 4 Season 14 **PTR** 3.1 Meta Builds for Every Class \| 30 Layers Separate Best from Worst" | meta por clase en PTR |
| mmonice — "Class Tier List: Best Builds, **PTR Results**, and Meta Predictions" | mezcla PTR y predicciones |

**Y contradicen frontalmente al parche vivo.** El PTR decía "Paladín rey del parche, **varias builds S**"; la
lista viva de Maxroll de endgame de Paladín tiene **la S vacía**. Icy Veins lo dice en la misma dirección:
> "early projections give Paladins little hope to be competitive in the S tier once again, with only Arbiter
> Wing Strike showing some promise."

**Por qué importa:** la regla 6 del encargo pedía literalmente distinguir PTR de parche vivo y marcar lo de PTR.
El informe no solo no lo encontró, sino que **afirmó positivamente que no existía**. Ese es el hueco por donde
entra el próximo dato muerto: si el jugador busca "Paladin S tier Season 14" se va a topar de frente con estos
titulares de PTR, que son entusiastas y falsos para el parche vivo, y el informe **no le ha dejado el aviso**.

**Matiz justo, y no menor:** este fallo **no contamina ningún número publicado**. El informe no citó nada de PTR.
Es un fallo de cobertura y de aviso al jugador, no de dato sucio. La conclusión de fondo del informe —Shield
Charge en A, sin S de Paladín en endgame— es **la del parche vivo, y es la correcta**; el material de PTR es
precisamente lo que habría que descartar.

### E4 — Mala atribución de la lista de objetos a vortexgaming.io *(gravedad media)*

**Dónde:** aviso de 5.3 y "No encontrado" #6, que atribuyen a `vortexgaming.io/en/postdetail/1228640` los nombres
"Rite of Thorns, Punishment, Impunity, Aspect of Lapa's Scripture, Glynn's Anvil, set Phoba, Resolución 30".

**Refutación.** Abrí esa página pidiendo esos términos uno a uno: **no están.** Los únicos objetos que nombra son
**"Tibault's Will pants"** y **"Crucifix of the False Prophet"** — este último ni siquiera aparece en el informe.
Sí insiste en priorizar la estadística "Thorns", eso sí.

**Diagnóstico:** el informe atribuyó a una URL concreta un contenido que esa URL no tiene. La lista debía venir
solo de extractos de buscador. **Citar una fuente por un contenido que no contiene es el mismo defecto que
inventar el dato**, aunque aquí sea por descuido y sobre material que el propio informe marcó como no fiable.

**Además, dos de las cuatro razones para descartarla están mal:**
- Dice "**El artículo no tiene fecha.** Imposible saber a qué parche se refiere." → No tiene fecha de publicación,
  cierto, pero **se autoidentifica como "Season 14" y referencia "a July 28th patch"** (el 3.1.2). Es datable a
  partir del 28/07/2026, y es material de parche vivo.
- Dice "**No distingue PTR de parche vivo.**" → Al referenciar el parche del 28 de julio, sí queda del lado vivo.

**La decisión de descartar el número sigue siendo correcta** por las razones 3 y 4, que sí aguantan: "Abyssal
Depths Tier 130" no es terminología confirmable en fuentes preferentes, y "de decenas a cientos de billones" es
un rango de un orden de magnitud, no un dato. **El veredicto es bueno; dos de los cuatro argumentos, no.**

### E5 — Recuento erróneo en 4.2 *(gravedad baja)*

**Dónde:** sección 4.2.
> "La S global de empuje tiene 11 builds e incluye **cuatro de Bárbaro** (Flame Charge, Rend, Whirlwind, Minion)
> más Mighty Throw."

**Son cinco de Bárbaro, no cuatro.** La propia frase nombra cuatro y luego añade una quinta. Confirmado por dos
vías: la S global de empuje (11 builds, de las cuales Flame Charge, Rend, Whirlwind, Minion y Mighty Throw son
Bárbaro) y `barbarian-push-tier-list` (19/07/2026), cuya S es exactamente esas cinco.

Erratum de redacción, no de fuente. Pero refuerza la tesis del informe en lugar de debilitarla: **cinco de las
once builds S de empuje del juego son Bárbaro.**

---

## 3. Omisión que sesga (no es error, pero conviene arreglarla)

**Sección 4.4, farmeo rápido global.** El informe resume: *"Whirlwind S, Mighty Throw S, Minion Barb S,
Shield Charge A"*. Es cierto pero **incompleto de una forma que favorece su propia narrativa**.

La S global de farmeo rápido (22/07/2026) contiene **dos builds de Paladín**: **Wing Strikes Paladin** y
**Blessed Hammer Paladin**. Es decir: en ese eje **el Paladín sí tiene builds S globales** — solo que no es
Shield Charge la que las tiene.

La tabla de veredicto 4.5 ("las tres de Bárbaro un escalón por encima en tres de cuatro ejes") es correcta
**para Shield Charge**, pero leerla como "el Paladín va un escalón por detrás del Bárbaro" sería falso en
farmeo. Dado que el jugador es principiante y juega en dúo, esa distinción es práctica, no académica: si algún
día quiere farmear rápido, su clase tiene opciones S sin cambiar de personaje.

---

## 4. Cosas que el informe hace bien y merecen quedar dichas

Como verificador adversarial es tan relevante lo que no logré tumbar:

1. **La distinción listas-por-clase vs. listas-globales (sección 1) es metodológicamente correcta** y es
   el núcleo del valor del informe. Comparar la A de la lista de Paladín con la S de la de Bárbaro sería
   efectivamente un error de escala. El informe usa las globales para comparar. **Bien.**
2. **La reconstrucción del historial de parches** para justificar que las listas de julio siguen vivas en agosto
   es el tipo de comprobación que este proyecto necesitaba, y **la he podido corroborar por fuera de Maxroll**
   (Icy Veins para el 3.1.3).
3. **La trampa de la guía de Season 12** está bien cazada y bien avisada. Existe, sale arriba en Google, y no
   hay guía de leveling de Shield Charge para S14. Confirmado.
4. **El descarte del número de vortexgaming** ("decenas a cientos de billones") es la decisión correcta, aunque
   dos de sus cuatro argumentos fallen.
5. **El aviso sobre Icy Veins** (fechada 04/07, anterior a la publicación de la guía de Shield Charge del 20-25/07,
   por lo que su "A" para Paladín no valora esa build) es un matiz honesto y correcto. Fecha verificada: 4 de
   julio de 2026. Tabla verificada: Paladín S/S/A, Bárbaro B/S/S. Y sí, **Icy Veins no publica tiers por build
   individual** en esa página, como dice el informe.
6. **El descarte del support zDPS para un jugador en dúo** es criterio, no dato, y es criterio correcto.

---

## 5. Detalles menores sin confirmar (no llegan a defecto)

Dos frases de la sección 5.3 no las he podido corroborar con cita literal en ninguna fuente que haya abierto:

- *"Relentless Charge convierte Shield Charge en habilidad Core canalizable de forma continua, **a coste de Fe
  creciente**"* — el "Core" y el canalizado continuo están confirmados; **el coste de Fe creciente, no.**
- *"**Rally - Words of Sacrifice** te deja usar la vida como recurso"* — no localizado en texto literal.

No los marco como error porque son plausibles y de bajo riesgo, pero si el informe pasa a guía final deberían
llevar cita o caer.

---

## 6. Veredicto

**PARCIAL.**

- **Las 12 afirmaciones que el informe declara haber confirmado: confirmadas las 12.** Fechas, letras de tier,
  orden de Míticos y citas literales coinciden exactamente. No he encontrado ningún número inventado, ninguna
  fuente vetada respaldando un dato, ni ningún dato de PTR presentado como parche vivo.
- **La conclusión práctica del informe es correcta y utilizable:** Shield Charge es la mejor build de Paladín
  para uso general en el parche vivo, empata con lo mejor del juego en jefes, va un escalón por debajo de las
  tres de Bárbaro en los otros tres ejes, y Mantle of the Grey es el Mítico número 1.
- **Pero hay un número mal citado (Juggernaut) y dos "No encontrado" falsos**, uno de ellos precisamente sobre
  la contaminación de PTR que el encargo mandaba vigilar.

**Qué hay que arreglar antes de publicar:**

1. Corregir Juggernaut a **60% → 80%** (y, si se cita el 50%, atribuirlo a **Disciple**).
2. Sacar de "No encontrado" el **tope de Resolución 30, Glynn's Anvil y el set Phoba de Righteous Will**: están
   verbatim en la guía. Sustituir ese hueco por el real: **la guía mete el equipo en el planificador incrustado,
   no en texto.**
3. Reescribir "No encontrado" #9: **sí hay tier lists de PTR**, dicen "Paladín rey con varias builds S", y son
   **falsas para el parche vivo**. Convertirlo en aviso al jugador en vez de en hueco.
4. Quitar la atribución a vortexgaming de una lista de objetos que esa página no contiene, y corregir las dos
   razones de descarte que no se sostienen.
5. "Cuatro de Bárbaro" → **cinco**.
6. Completar 4.4: en farmeo rápido global, **Wing Strikes y Blessed Hammer (Paladín) también son S**.

---

## Fuentes abiertas en esta verificación

**Oficiales**
1. https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes — tres lecturas distintas: contenido de 3.1.x, sección completa de balance de Paladín del 3.1.0, y consulta dirigida sobre Juggernaut/Disciple.

**Maxroll — tier lists globales**
2. https://maxroll.gg/d4/tierlists/endgame-tier-list
3. https://maxroll.gg/d4/tierlists/push-tier-list
4. https://maxroll.gg/d4/tierlists/bossing-builds-tier-list — dos lecturas (S/A, y desglose completo B/C/D)
5. https://maxroll.gg/d4/tierlists/speedfarming-tier-list

**Maxroll — tier lists por clase**
6. https://maxroll.gg/d4/tierlists/paladin-endgame-tier-list
7. https://maxroll.gg/d4/tierlists/paladin-push-tier-list
8. https://maxroll.gg/d4/tierlists/paladin-speedfarming-tier-list
9. https://maxroll.gg/d4/tierlists/paladin-leveling-tier-list
10. https://maxroll.gg/d4/tierlists/barbarian-endgame-tier-list
11. https://maxroll.gg/d4/tierlists/barbarian-push-tier-list — **nueva**, no estaba en el informe. Confirma ausencia de números de Foso y la S de cinco Bárbaros.

**Maxroll — guías**
12. https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide — dos lecturas: Míticos/pros-contras, y consulta dirigida sobre Resolución/Glynn's/Phoba/panel numérico
13. https://maxroll.gg/d4/build-guides/shield-of-retribution-paladin-guide
14. https://maxroll.gg/d4/build-guides/whirlwind-barbarian-guide
15. https://maxroll.gg/d4/build-guides/mighty-throw-barbarian-guide
16. https://maxroll.gg/d4/build-guides/minion-barbarian-guide
17. https://maxroll.gg/d4/build-guides/paladin

**Maxroll — noticias**
18. https://maxroll.gg/d4/news/lord-of-hatred-3-1-2-patch-notes

**Icy Veins (corroboración independiente)**
19. https://www.icy-veins.com/d4/guides/class-tier-list/ — 04/07/2026
20. https://www.icy-veins.com/d4/news/diablo-4-3-1-3-patch-notes-easier-season-objectives-and-echo-of-mephisto-portal-fix/ — **nueva**. Corrobora por fuera de Maxroll que el 3.1.3 no trae balance.
21. https://www.icy-veins.com/d4/news/diablo-4-season-14-meta-is-already-taking-shape-after-class-tuning/ — **nueva**. Sin fecha visible; mezcla PTR y parche. Citada solo por su frase sobre el Paladín y la S.

**Bloqueadas (403 verificado)**
22. https://mobalytics.gg/diablo-4/paladin-builds-tier-list
23. https://mobalytics.gg/diablo-4/builds/paladin-shield-charge-endgame-build-guide — **nueva**; demuestra que el bloqueo es de dominio
24. https://www.u4gm.com/diablo-iv/blog-diablo-4-season-14-ptr-paladin-dominates-the-meta-with-s-tier-power — 403 al abrir; su contenido consta por extracto de buscador y así se marca

**Sin contenido**
25. https://www.wowhead.com/diablo-4/guide/classes/paladin/shield-charge-build-overview — solo navegación; cabecera "Updated: 2026/03/08", anterior al lanzamiento de la clase

**En conflicto / descartadas**
26. https://d4guides.gg/en/builds/paladin — 16/08/2026. Confirmada la caracterización del informe.
27. https://vortexgaming.io/en/postdetail/1228640 — **no contiene** la lista de objetos que el informe le atribuye.
