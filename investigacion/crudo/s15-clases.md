# Balance de clases — parche 3.2.1 (Temporada 15, "Hell's Legacy")

> **Estado del encargo:** informe escrito el 15 de septiembre de 2026, **antes** de que la S15 se
> abriera (16:30 UTC). Las notas de parche son hecho verificable; **no existe un solo dato de juego
> real de la S15**. Todo lo que se parezca a "la mejor build" hoy es predicción.

## Resumen

1. El cambio grande no es una habilidad: es el **core stat scalar**, un único mando que Blizzard mueve por clase. Bárbaro baja 1.1 → 0.8; Druida, Nigromante, Paladín y Hechicera suben 1.25 → 1.625; **Pícaro, Espiritado y Brujo no se tocan**.
2. Blizzard declara intención explícita en dos casos: Bárbaro ("han estado fuertes las últimas temporadas") y Paladín ("se ha quedado atrás respecto a otras clases").
3. Espiritado pierde un bug (runa Tzic) que le daba daño masivo y el tope de Aspecto de Supremacía baja de 30 a 15 acumulaciones; Blizzard compensa con subidas amplias a Paragón, Core y armas únicas.
4. Brujo va en dirección contraria: "rinde bien", así que le podan escaladores (Aspecto Abrumador, Metamorfosis, Dynamism/Demonform) manteniendo diversidad.
5. **Ninguna tier list de fuente preferente refleja la S15 jugada.** La de Maxroll es del 14 de septiembre (un día antes del lanzamiento); la de clases de Icy Veins es del **4 de julio de 2026**, anterior incluso al PTR. Detalle en la sección de tier lists y en Contradicciones.

---

## Hallazgos

### A. El mando principal: core stat scalar

Fuente primaria de toda esta sección: notas oficiales 3.2.1, build #73552, 15 sep 2026, publicadas dentro del artículo de temporada:
https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy#Patch

| Clase | Stat | Antes | Después | Variación | Evidencia |
|---|---|---|---|---|---|
| Bárbaro | Fuerza | 1.1 | **0.8** | −27,3 % | oficial |
| Druida | Voluntad | 1.25 | **1.625** | +30 % | oficial |
| Nigromante | Inteligencia | 1.25 | **1.625** | +30 % | oficial |
| Paladín | Fuerza | 1.25 | **1.625** | +30 % | oficial |
| Hechicera | Inteligencia | 1.25 | **1.625** | +30 % | oficial |
| **Pícaro** | Destreza | 1.25 | **sin cambio** | 0 % | oficial (ausencia de línea) |
| **Espiritado** | — | 1.25 | **sin cambio** | 0 % | oficial (ausencia de línea) |
| **Brujo** | — | 1.25 | **sin cambio** | 0 % | oficial (ausencia de línea) |

- El valor se lee como "daño por cada 10 puntos de stat principal": Bárbaro pasa de 1,1 % a 0,8 % por 10 de Fuerza; los cuatro subidos pasan de 1,25 % a 1,625 %. *Oficial*, texto del dev note.
- El mismo cambio ya estaba en el **PTR 3.2.0, build #73123, 4 ago 2026** (PTR abierto del 4 al 11 de agosto), con cifras idénticas: https://news.blizzard.com/en-us/article/24292852/the-3-2-0-ptr-what-you-need-to-know — *oficial*. **No es un artefacto de PTR: sobrevivió a la versión final.**
- Corroboración secundaria de las mismas cifras en Maxroll, página fechada **12 sep 2026**: https://maxroll.gg/d4/news/diablo-4-3-2-1-patch-notes — *corroborado*.

**De dónde sale el 1.25 de base (verificación del marco).** Blizzard nunca imprime el valor de las clases que no toca. La guía de daño de Maxroll (última actualización **12 jun 2026**, etiquetada Temporada 13) documenta el coeficiente previo: Bárbaro necesita **9,0991 de stat principal por 1 % de daño de habilidad** (= 1,099 % por 10 ≈ 1.1) y **el resto de clases 8 por 1 %** (= 1,25 % por 10 ≈ 1.25). https://maxroll.gg/d4/resources/in-depth-damage-guide — *unica*, y además página fuera del parche vivo; la uso solo para fijar el estado **anterior**, que es justo lo que los "antes" de las notas oficiales confirman.

**Lectura del marco (esto es análisis mío, no fuente).** Las fuentes no preferentes cuentan esto como "al Pícaro no le tocan nada, así que se queda arriba". En este eje concreto eso está del revés: no recibir el +30 % cuando cuatro clases sí lo reciben es **perder 23,1 % de posición relativa** en ese bucket (1,25 / 1,625 = 0,769). Y el Bárbaro no cae 27 %, cae **44 % de posición relativa** frente a las cuatro subidas (antes 1,1/1,25 = 0,88; después 0,8/1,625 = 0,49).
**Aviso de modelo, importante:** el core stat scalar alimenta el bucket **aditivo** de daño por stat principal, no el daño total. **+30 % de escalar ≠ +30 % de DPS.** El efecto real depende de cuánto pese ese sumando frente al resto de aditivos del build, y eso no lo dice ninguna fuente. Cualquiera que traduzca "1.25 → 1.625" a "+30 % de daño" está inventando.

### B. Clase por clase

Todas las cifras de esta sección están leídas en las notas oficiales (URL de A) salvo donde se indique. Nivel: *oficial*.

#### Bárbaro — nerf declarado
Dev note textual: *"Barbarians have been strong for the past couple seasons, so we're going to adjust the class while improving some Core skills."*
- Core stat scalar 1.1 → **0.8**.
- Grito de Reunión (variante Madawc): 200 % → **100 %**.
- Llamada de los Ancestros (Madawc): 240 % → **120 %**.
- Pericia de espada a dos manos, bonus de Sangrado: 30 %[x] → **15 %[x]**.
- Glifo Destripar: 20 %[x] → **15 %[x]**. Glifo Triturador: 20 %[x] → **15 %[x]**.
- Nodo legendario Hemorragia: 75 %[x] → **60 %[x]**. Nodo Furia Sanguinaria: 60 %[x] → **45 %[x]**.
- Aspecto Serpenteante: 7,5-12,5 %[x] → **6-9 %[x]**. Aspecto Belicoso: 15-20 % → **10-15 %**.
- Anillo del Voraz: ahora solo aplica **1** acumulación de Desgarro; cooldown 1 s → **0,5 s**.
- Anillo del Furor Rojo: requisito de Furia 100 → **30** (esto sí es mejora).
- Ramaladni's Magnum Opus: 10 Furia/s → **7 % de Furia máxima**, solo en combate (*unica*: Maxroll 12 sep; el matiz "10 % → 7 %" aparece en Icy Veins).
**Neto: el único paquete de nerfs coordinado del parche.** Escalar, Paragón, aspectos, pericia y sangrado, todo a la baja a la vez.

#### Paladín — buff declarado
Dev note textual: *"Paladin has fallen behind other classes in the late game, so many of these updates are aimed at bringing up the class as a whole... Judgement builds in particular have struggled to keep pace with other builds, so Judgement will now scale with the Skill Rank of the applying Skill, opening up a new scaling vector for these builds."*
- Core stat scalar 1.25 → **1.625**.
- **Juicio ahora escala con el rango de la habilidad que lo aplicó** (vector de escalado nuevo, no un número).
- Lanza Divina: 90 % → **110 %**; Punta de la Lanza: 35 % → **39 %**.
- Celo, golpe adicional: 20 % → **35 %**.
- Juramento del Juzgador: añade *"si Juicio golpea a un solo enemigo, inflige 100 % más daño"*.
- Juramento del Discípulo: 80 % → **100 %**. Juramento del Fanático: 25 % → **35 %** por acumulación de Fervor.
- Canto de la Catedral: consumir Juicio 100 veces invoca Lanza de los Cielos.
- Talismanes Heaven's Radiant Fire y Cathan's Righteous Will ajustados para consistencia y uptime.

#### Nigromante — subida amplia de Core
Dev note textual (resumido, cita literal en las notas): los top builds giraban en torno a Oleada de Sangre y Espíritu Óseo, *"meaning many of their other Core skills underperformed"*; Explosión de Cadáveres *"has not been close to the meta recently"*; Desgarro de Almas *"has also lacked an identity"*. Y rediseño declarado del bucle de Arrollar: de acumular y mantener máximo, a **"generar y gastar"**.
- Core stat scalar 1.25 → **1.625**.
- Lanza Sanguinaria: 130 % → **160 %**; variante Blood Seeker: +50 %[x] por enemigo lanceado y +50 %[x] extra al primero.
- Explosión de Cadáveres: 110 % → **180 %**; Miasma 210 % → **350 %**; Shrapnel 110 % → **180 %**.
- Desgarro de Almas: 300 % → **350 %**, cooldown 50 s → **40 s**.
- Oleada de Sangre, Senda de Oscuridad (suelo profanado): 600 % → **800 %**.
- The Unmaker: 200-250 % → **300-350 %**.
- Red Blessing **rediseñado**: antes 2 de Arrollar máx. + 8-10 % por acumulación; ahora *"tus habilidades de Sangre consumen 1 acumulación de Arrollar para infligir 130-150 %[x] más daño"*.
- Deathless Visage: 40-50 %[x] → **60-70 %[x]**. Hangman's Hand: 10-15 %[x] → **35-50 %[x]**.
- Ejército de los Muertos ahora **acumula** si se lanza varias veces. Talismán Rathma's Waking Touch pasa de daño de Esbirro a **daño de Invocación** (más amplio).

#### Hechicera — el arquetipo Frío es el objetivo
Dev note textual: *"We are buffing the Cold archetype for Sorcerer, since Lightning and Fire have been dominating the past couple of seasons, while buffing up other areas that felt like they were behind."*
- Core stat scalar 1.25 → **1.625**.
- Bola de Relámpagos (variante Orbital): **ahora se puede lanzar en movimiento** (cambio de calidad de vida con impacto real en uptime).
- Meteorito: impacto 180 % → **240 %**; Estrella Fugaz 306 % → **408 %**.
- Esquirlas de Hielo, Frío Penetrante: añade **+50 %[x]**.
- Blue Rose: 40-60 %[x] → **80-100 %[x]**.
- Glifo Pirómano: 18 %[x] → **15 %[x]** (único recorte). Glifo Eliminador: 10 % → **18 %**. Nodo Icefall: 50 %[x] → **60 %[x]**.
- Cuchillas de Hielo (Blazing): pasa de cooldown a **coste de 20 de Maná**.

#### Druida — talismanes y únicos, subidas grandes
Dev note textual: cambios de calidad de vida en talismanes sin obligar a rehabilitar bonus de 5 piezas; *"Storm Shepherd's Call redesign resulted in a nerf from its previous iteration, so we'll continue to monitor its performance in the future"* — **Blizzard admite que ese rediseño es un nerf**.
- Core stat scalar 1.25 → **1.625**.
- Greatstaff of the Crone: 60-80 %[x] → **120-150 %[x]**.
- Fleshrender (daño de Tornado): 40-50 %[x] → **100-135 %[x]**.
- Airidah's Inexorable Will: 7-10 %[x] → **30-45 %[x]**.
- Dolmen Stone: 75-90 %[x] → **113-135 %[x]**.
- Forma Humana: gana 15 % regeneración de recurso y 15 % reducción de cooldown (*unica*: Maxroll 12 sep).
- Furia Grizzly: 150 %[x] integrado; variante Cornered Beast → 200 %[x] (*unica*: Maxroll 12 sep).

#### Pícaro — la intervención más pequeña
Dev note textual: *"Rogues have a decent variety of builds available to them, but specific Cutthroat builds could use more power and quality changes."* — **no hay declaración de que esté fuerte ni de que esté flojo.**
- **Sin cambio de core stat scalar.**
- Andanada (Encircling Blades): 294 % → **343 %**.
- Granada de Humo (Shade Grenade): ahora gana daño de Puntos de Combo y bonus de Sombra si usas Puntos de Combo.
- Nodo raro Surgical: pasa de daño de Cutthroat a **todo el daño**. Nodo legendario Tricks of the Trade: 20 %[x].
- Aspecto del Granadero: 35-50 %[x] → **45-60 %[x]**; y 52,5-75 %[x] → **75-100 %[x]**.
- Pitfighter's Gull: 7,5-10 %[x] → **15-20 %[x]**.
- Condemnation: añade generar Puntos de Combo equivalentes durante 1,5 s al gastarlos.
- Talismán Applied Alchemy 5 piezas: 200 %[x] → **250 %[x]**.
- Templado "daño por Punto de Combo gastado": 3-4,5 % → **10-15 %** (*unica*: Maxroll 12 sep + Icy Veins).
**Neto: buffs reales y cero nerfs de clase, pero sin el +30 % de escalar.**

#### Espiritado — corrección de bug, compensada
Dev note textual: *"We are fixing a bug with the Tzic Rune that incorrectly gave a massive damage increase, as well as reducing the maximum stacks on Aspect of Supremacy. To help offset these changes, we are significantly buffing Spiritborn's Paragon boards, Core Skills, Potency Skills, and Unique weapons."*
- **Sin cambio de core stat scalar.**
- Runa Tzic: corregido que aumentara el daño de **todas** las habilidades.
- Aspecto de Supremacía: tope 30 → **15** acumulaciones.
- Compensación (cifras *unica*, Maxroll 12 sep): Rock Splitter 3.º golpe 80 % → 110 %; Thunderspike 3.º golpe 65 % → 90 %; Withering Fist (Fist of Forest) 50 % → **150 %**; Razor Wings 95 % → 120 %; tablero nuevo **Swarm of Storms**; glifo Talon 15 % → 25 %; Bitter Medicine 80 %[x] → 140 %[x]; Convergence 60 %[x] → 100 %[x]; Drive 6 %[x] → 10 %[x] por acumulación; Spiney Skin 60 % → 100 % Espinas; Sunbird's Gorget 8 s → 12 s; Sepazontec 140-180 % → 180-220 %; Rod of Kepeleke 0,85-1,05 % → 1-1,2 % por Vigor.
- El Aspecto de Fuerza Celestial pasa a estar **disponible para Espiritado** (antes restringido), con su daño reducido de 30-40 % a 20-30 %.
**Aviso:** el tamaño real del nerf de Tzic no está publicado. Fuentes no preferentes hablan de ~600 % de daño extra en S14; **no lo he podido verificar en fuente preferente ni oficial**.

#### Brujo — poda por estar fuerte
Dev note textual: *"Warlock is performing well with many of their newly improved options. These updates focus on maintaining momentum and build diversity while pruning unintuitive or oppressive scalars. In particular, the Overwhelming Aspect was scaling up too much and Metamorphosis was interacting with several stacking mechanics in unintended ways... We are also looking to redistribute power out of Demonform."*
- **Sin cambio de core stat scalar.**
- Aspecto Abrumador **rediseñado**: antes 80-120 %[x] contra élites consumiendo 4 de Arrollar; ahora **5-7 % por acumulación de Arrollar** contra élites en habilidades Ocultas.
- Metamorfosis: generación de Dominio con básicas 2 → **5**; variante Sin Demon deja de acumular hasta 20 y pasa a **+50 % de Ira y Dominio máximos** durante la forma.
- Nodo Dynamism: añade **+85 % daño de Invocación fuera de Demonform**; daño por Dominio **dentro** de Demonform 3 % → **2,5 %**.
- Scepter of the Three: permite equipar todas las Definitivas base; acumula 1,7-2,5 % por golpe no-definitivo (antes 4-5 % atacando sin Definitiva activa).
- Buffs de habilidad (*unica*, Maxroll 12 sep): Bombardment 40 % → 55 % y pasa a ser habilidad de Invocación; Dread Claws 50 % → 70 %; Ravenous Jaws 125 % → **500 %** (Eviscerate); Infernal Breath 20 % → 30 %, Explosive Death 100 % → 200 %; Sigil of Chaos 30 % → 50 %; Terror Swarm 100 % → 130 %/s y estallido 500 % → 650 %; Hellhound's Sabatons 80-100 %[x] → **200-280 %[x]**; Bridle of Tor'baalos 120-160 % → 160-200 %; Infernal Homunculus 50-70 %[x] → 80-110 %[x]; glifo nuevo **Superiority**.
**Neto: mezcla. Le quitan los escaladores que Blizzard llama "opresivos" y le devuelven potencia repartida fuera de Demonform.**

### C. Nerfs que cruzan todas las clases

- **Melted Heart of Selig:** recurso principal 102-154 % → **58-77 %**. *oficial*.
- **Tibault's Will:** regeneración de recurso 50 % → **25 %**. *oficial*.
- Wendigo Brand: rediseñado, da 1 % de velocidad de ataque en vez de vida máxima. *oficial*.
- Aspecto de Fuerza Celestial: reducción de daño 30-40 % → **20-30 %**, y se abre a Espiritado. *oficial*.
- Aspecto del Expectante: 4-6 % → **6-8 %** por golpe básico (hasta 10). Aspecto Embattled: drenaje de Fortificar 100-150 % → 150-200 %. *oficial*.
- **Resistencias:** los afijos de resistencia única pasan a valer **7 veces** el de Todas las Resistencias. *oficial*. (Cambio de itemización, no de clase, pero mueve el equipamiento defensivo de todo el mundo.)

Selig y Tibault's Will son los dos objetos que sostienen builds de alto gasto de recurso en varias clases a la vez. Que caigan ~45 % y 50 % respectivamente es, en la práctica, un nerf transversal que ninguna tier list previa al lanzamiento ha podido medir.

---

## Tier lists: leer esto antes de mirar ninguna

> ### AVISO PRINCIPAL
> **A día de hoy (15 sep 2026, antes de las 16:30 UTC) no existe ninguna tier list basada en la
> Temporada 15 jugada.** Cero leaderboards, cero Pit pusheado, cero horas de 3.2.1 en vivo.
> Todo lo de abajo es (b) **teorycrafting**, nunca (a) hecho verificable — por buena que sea la casa.

**Maxroll — Overall Endgame Builds Tier List.** Última actualización **14 sep 2026**, etiquetada "Season 15". https://maxroll.gg/d4/tierlists/endgame-tier-list — *unica*.
- S-Tier declarado: Firewall Hechicera, Blood Wave Nigromante, Counterswarm y Stinger Espiritado, **Whirlwind Bárbaro**, Dance of Knives Pícaro.
- Paladín: nada en S; A-Tier (Shield Charge, Divine Lance), B y C el resto.
- Brujo: nada en S; A-Tier (Minion, Apocalypse, Lunatic).
- **La página no lleva ningún aviso de que sea preliminar o teórica.** Se presenta como lista cerrada.
- Fecha 14 sep = **un día antes** del lanzamiento. Imposible que contenga datos de juego real.

**Maxroll — Compendio S15.** 14 sep 2026. https://maxroll.gg/d4/news/diablo-4-season-15-compendium-season-launch-update — *unica*. Sí reconoce el problema, en una frase que conviene citar: *"Please be patient as some guides, while updated, require the start of the season to verify information."* Es decir: **la propia Maxroll admite que parte de sus guías están sin verificar**, aunque su tier list no lo diga.

**Icy Veins — Class Tier List.** Última actualización **4 de julio de 2026**. https://www.icy-veins.com/d4/guides/class-tier-list/ — *unica*, y **caducada**.
- Orden que publica: S-Tier Pícaro, Bárbaro, Druida, Brujo; A-Tier Espiritado, Hechicera, Nigromante, Paladín.
- **El 4 de julio es anterior al PTR 3.2.0 (4 de agosto).** Esta lista no puede haber visto ni una sola línea de las notas de la S15. Ranquea al Bárbaro en S justo antes del único paquete de nerfs coordinado del parche, y al Paladín en A pese a que Blizzard dice por escrito que se ha quedado atrás.
- Ver Contradicciones: la página se autodenomina "Season 15" mientras el índice de Icy Veins la etiqueta "Season 13".

**Icy Veins — resto de tier lists** (Endgame, Speed Farming, Boss Killer, Leveling, Nightmare Dungeon): todas etiquetadas **Season 14**. https://www.icy-veins.com/d4/guides/tier-lists/ — *unica*. No aplican a 3.2.1.

### Qué se puede decir con honestidad sobre "quién está más fuerte"

Separando lo que dicen las notas de lo que predice nadie:

**(a) Hecho verificable, de las notas de parche.** Blizzard ha empujado **al alza y de forma explícita a Paladín** (único caso con declaración textual de "se ha quedado atrás" + escalar +30 % + vector de escalado nuevo para Juicio), ha subido el escalar a Druida, Nigromante y Hechicera, y ha aplicado **al Bárbaro el único nerf coordinado** (escalar −27 %, más Paragón, aspectos, pericia y sangrado). Espiritado pierde un bug de daño masivo. Brujo pierde escaladores por estar fuerte. Pícaro es la clase menos tocada: buffs pequeños, cero nerfs, y **cero subida de escalar**.

**(b) Opinión / teorycrafting.** Cualquier orden concreto de clases. Yo no lo firmo y las fuentes preferentes tampoco lo han podido medir.

---

## Huecos

- **Valor del core stat scalar de Pícaro, Espiritado y Brujo tras 3.2.1: no publicado.** Deduzco 1.25 porque Blizzard no imprime línea de cambio y porque la guía de daño de Maxroll fija 8 de stat por 1 % (= 1,25 % por 10) para todas las no-Bárbaro. **Es inferencia, no dato leído.** Además esa guía de Maxroll es de junio 2026 / S13 y **no lista Paladín ni Brujo por separado**, así que para esas dos clases el "antes" solo lo respalda el propio "from 1.25" de las notas.
- **Cuál es el stat principal del Brujo:** no lo he visto escrito en fuente preferente. No lo afirmo.
- **Peso real del core stat scalar en el DPS total:** ninguna fuente publica qué fracción del daño sale del bucket de stat principal. Sin eso, "+30 % de escalar" no se puede convertir en porcentaje de DPS. Hueco central del informe.
- **Magnitud del bug de la runa Tzic:** Blizzard dice "massive" sin cifra. El ~600 % que circula procede de fuentes no preferentes; no verificado.
- **Valores de los Soul Splinters y de Leoric's Crown:** los propios foristas señalan que las notas no publican los números. Sin confirmar.
- **Ramaladni's Magnum Opus (10 → 7):** aparece como "10 Furia/s → 7 % de Furia máxima" en Maxroll y como "10 % → 7 %" en Icy Veins. No he podido fijar la redacción oficial exacta.
- **No he verificado línea por línea** contra el texto oficial los números marcados *unica* de Druida (Forma Humana, Furia Grizzly), Espiritado y Brujo. Los de Bárbaro, Pícaro, Nigromante, Paladín y Hechicera sí están leídos en las notas oficiales.
- **Cambios de Paragón y glifos globales** más allá de los citados: no revisados en profundidad.
- **Nada sobre rendimiento real:** sin leaderboards, sin tiempos de Pit, sin tasas de uso. Por definición, hasta pasadas las 16:30 UTC de hoy.

---

## Contradicciones

**1. ¿Recibió el Brujo el +30 % de escalar?**
- *Versión A:* una lectura del artículo oficial devuelve "Core stat scalar increased from 1.25 to 1.625 (Druid, Necromancer, Paladin, Sorcerer, **and Warlock**)".
- *Versión B:* una relectura dirigida del **mismo artículo oficial**, preguntando clase por clase, devuelve que Brujo **no tiene línea de core stat scalar**. Maxroll (12 sep) tampoco se la asigna, y el PTR 3.2.0 (4 ago) enumera exactamente cuatro clases subidas: Druida, Nigromante, Paladín, Hechicera.
- **Resolución: B.** El Brujo no cambia. Lo dejo escrito porque es justo el tipo de error que se propaga: una enumeración mal cerrada convierte a una clase no tocada en clase buffeada, y de ahí pasa a una tier list.

**2. Icy Veins se etiqueta a sí misma con tres temporadas distintas.**
- La página de Class Tier List dice "Season 15 Rankings" y *"Last updated: July 4th, 2026. This tier list is regularly reviewed to reflect the latest balance changes and class meta shifts in the current Season 15."*
- El índice de tier lists de la propia Icy Veins etiqueta esa misma lista como **"Season 13"**.
- Los buscadores la indexan como **"Season 14 Rankings"**.
- **Tres etiquetas para una sola página.** El rótulo de temporada se actualiza solo; el contenido, del 4 de julio, no. La afirmación "refleja los últimos cambios de balance de la Season 15" es **falsa de forma comprobable**: el PTR con esos cambios se publicó un mes después. No usar esta lista para 3.2.1.

**3. Maxroll pone Whirlwind Bárbaro en S-Tier el día antes de que entre el nerf al Bárbaro.**
- Notas oficiales: Bárbaro es la única clase con el escalar a la baja (−27 %), más recortes en dos glifos, dos nodos legendarios, dos aspectos, la pericia de espada a dos manos y el Anillo del Voraz.
- Maxroll (14 sep, "actualizado para Season 15"): Whirlwind Bárbaro en S-Tier, sin aviso de provisionalidad.
- No son necesariamente incompatibles (Whirlwind podría aguantar igual), pero **la lista no explica cómo sobrevive a ese paquete**, y está fechada antes de que nadie pudiera comprobarlo.

**4. El marco "al Pícaro no le tocan nada, luego el Pícaro manda".**
- Lo sostienen fuentes no preferentes, y encaja con que Icy Veins lo tuviera en S-Tier... en julio.
- Contra ese marco: en el eje del escalar, no ser tocado mientras cuatro clases suben un 30 % es **perder** terreno relativo, no ganarlo. El Pícaro sí recibe buffs propios (Granadero, Pitfighter's Gull, templado de Puntos de Combo, Applied Alchemy), así que "se queda arriba" es defendible; pero **el argumento "porque no lo tocaron" es el argumento equivocado**, y es el que más se repite.
- Ninguna de las dos versiones es verificable hoy.

**5. Notas del PTR frente a notas finales.**
- Icy Veins informa de que, entre el PTR 3.2.0 y las notas finales, **Nigromante, Paladín y Espiritado recibieron ayuda adicional**: Necro descrito como *"perhaps the biggest winner"*, Paladín con ajustes a Heaven's Radiant Fire y Cathan's Righteous Will, y Espiritado con Paragón, Core, Potencia y armas únicas "significantly buffed". https://www.icy-veins.com/d4/news/necromancer-paladin-and-spiritborn-get-more-help-in-diablo-4s-updated-patch-notes/ — *unica* (la página no publica fecha; se sitúa por su referencia a "hace dos semanas" respecto al PTR).
- Lo que **sí** he verificado como idéntico entre PTR y final son los core stat scalars: mismas cifras el 4 de agosto y el 15 de septiembre.
- Consecuencia práctica: **cualquier análisis escrito entre el 4 y el 11 de agosto (ventana del PTR) está desactualizado para esas tres clases.** Y ahí cae buena parte del teorycrafting que circula.
