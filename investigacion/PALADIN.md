# PALADÍN — Shield Charge, de cero a Tormento

**Parche vivo:** Diablo IV **3.1.3, build 73224 (12/08/2026)** · Temporada 14 "Death Awakening" (desde 30/06/2026)
**Fin de temporada estimado:** ~15/09/2026 → **te quedan unas 4 semanas**
**Documento consolidado el:** 24/08/2026, a partir de 6 informes crudos y 4 refutaciones adversariales

---

## 0. Antes de leer nada: en qué te puedes fiar de este documento

Este texto no es una guía copiada. Sale de seis investigaciones (`pal-clase`, `pal-shield-charge`, `pal-miticos`, `pal-tierlist`, `pal-leveling`, `pal-equipo`) y de cuatro refutaciones que las atacaron con la fuente primaria delante. **Donde la refutación tumbó un número, aquí va el número corregido, no el original.**

| Informe | ¿Refutado? | Veredicto | Qué significa para ti |
|---|---|---|---|
| `pal-clase` | Sí | PARCIAL | 2 enfriamientos muertos corregidos (uno era el de Shield Charge) |
| `pal-shield-charge` | Sí | PARCIAL | 11 errores, **uno invertía la recomendación central** (ver §3) |
| `pal-miticos` | Sí | PARCIAL | 6 errores; las 5 decisiones que mueven material resisten |
| `pal-tierlist` | Sí | PARCIAL | 1 número mal citado, 2 huecos falsos |
| `pal-leveling` | **NO** | — | **Sin auditar. Trátalo con una pizca menos de confianza.** |
| `pal-equipo` | **NO** | — | **Sin auditar. Ídem.** |

**Tres avisos de método que condicionan todo lo que sigue:**

1. **Hay datamining declarado.** Buena parte de los números vienen del fichero de datos que sirve el planificador de Maxroll (`assets-ng.maxroll.gg/d4-tools/game/data.min.json`, 11 606 292 bytes, campo `version` = **`3.1.0.72698`**). **Eso es parche 3.1.0, build 72698 — tres revisiones por detrás de tu 3.1.3.** Pero: la refutación de `pal-clase` recorrió las notas oficiales entera y **el Paladín no aparece ni una sola vez en 3.1.1, 3.1.2 ni 3.1.3** (salvo un fallo cosmético de "Damage with Holy" en la pestaña de estadísticas). **Entre el fichero y tu partida no hay cambios de equilibrio del Paladín. Confianza alta.**
2. **La trampa de la fecha reciente.** La página de habilidades del Paladín de Icy Veins está fechada el **29/06/2026**… y el parche 3.1.0 salió el **30/06/2026**. Es una página **pre-parche** con fecha de aspecto fresco. De ahí salieron los dos enfriamientos muertos. **Regla nueva del proyecto: una fecha reciente no basta; hay que compararla con la fecha del parche, no con la de la temporada.**
3. **El Paladín es clase de abril de 2026 y hay muchísimo material de PTR y beta circulando.** Si buscas "Paladin S tier Season 14" te vas a topar con titulares del tipo *"Paladin Dominates the Meta with S Tier Power"*. **Son del PTR y son falsos para el parche vivo**: en la lista de endgame de Paladín de Maxroll **la S está vacía**. Cualquier página del Paladín anterior al **28/04/2026** describe un árbol de habilidades que ya no existe.

---

## 1. Qué haces ahora mismo

### 1.1 Primero: qué hereda tu Paladín nuevo de la cuenta

Antes de mover un dedo, esto es lo que ya tienes hecho y lo que no. Hay **una trampa gorda**.

| Cosa | ¿La hereda el Paladín? | Nota |
|---|---|---|
| **Renombre (Renown)** | ✅ Sí | El planificador de la build asume **14 puntos de habilidad y 42 de Paragón de Renombre** ya cobrados |
| **Altares de Lilith** | ✅ Sí | |
| **Mapa descubierto y santuarios de viaje** | ✅ Sí | |
| **Montura** | ✅ Sí | |
| **Alijo, oro y materiales** | ✅ Sí, compartidos por modo de juego | Fuente sin fecha visible (Wowhead) — **compruébalo en pantalla** |
| **Rango de Temporada (Season Rank)** | ✅ Sí, es de cuenta dentro de la temporada | El progreso del nigromante cuenta |
| **Desbloqueo de El Foso y La Torre** | ✅ Sí (van por Rango de Temporada 2) | |
| **Ciudad Subterránea de Kurast** | ✅ Sí, **desde nivel 1** una vez desbloqueada en la cuenta | Requiere Vessel of Hatred |
| **Acceso a Planes de Guerra (War Plans)** | ✅ Sí, **si alguien completó la campaña de Lord of Hatred** | |
| 🔴 **Rango y árboles de Planes de Guerra** | ❌ **NO. Son POR PERSONAJE en la S14** | Blizzard lo reconoció y dijo que **no lo cambia esta temporada** |
| **Nivel, equipo, Paragón** | ❌ No | Empiezas a 1 |
| **Progreso de campaña / salto de campaña** | ✅ De cuenta, pero **por campaña separada** | Base, VoH y LoH son tres campañas distintas |

**Conflicto declarado sobre los puntos de habilidad:** Maxroll (`season-journey`, 13/07/2026) dice *"netting you a total of 14 Skill Points"* y el planificador de la build también pone 14. **Pero el anuncio oficial de la Temporada 14 de Blizzard dice "up to 12 skill points".** Los 14 cuadran con el total oficial de **83** (69 por niveles + 14), así que uso 14; el 12 queda anotado como fuente en conflicto.

### 1.2 Si aún estás subiendo (o todavía no has creado el Paladín)

**Haz esto en este orden.**

1. **Comprueba la campaña ANTES de crear al Paladín.** Ve a la pantalla de creación de personaje y mira si aparecen los interruptores de "saltar campaña" para las tres campañas (base, Vessel of Hatred, Lord of Hatred). No confirmes, solo mira. Son 30 segundos y deciden si tu subida dura 6 horas o 20.
2. **Si falta alguna campaña: hazla con el NIGROMANTE de 70, no con un Paladín de nivel 1.** El desbloqueo es **de cuenta**, y un personaje de 70 mal equipado atraviesa la campaña mucho más rápido que uno de nivel 1. La campaña de Lord of Hatred es la que abre **Planes de Guerra, Talismán y Cubo Horádrico**; la de Vessel of Hatred abre **Nahantu, Ciudad Subterránea, mercenarios y palabras rúnicas**.
   ⚠️ **Y hazlo antes de crear el Paladín.** Icy Veins dice que el acceso a Planes de Guerra lo reciben *"any future characters"* — **no hay ninguna fuente que confirme que un personaje YA CREADO lo recibe retroactivamente**. Ese orden te cubre en los dos casos.
3. **Crea el Paladín con salto de campaña activado.** Saltar te da además todos los santuarios de viaje de las regiones correspondientes.
4. 🔴 **NO subas con la guía de leveling de Shield Charge de Maxroll.** Está fechada el **24/04/2026**, con banner **"Season 12 - Slaughter"**, y su propio changelog dice *"Build archived prior to Lord of Hatred release"*. Es **cuatro días anterior al lanzamiento de la clase**. Sale la primera en Google.
5. **Sube con Shield of Retribution Paladin.** Es **S-tier** en la lista de leveling de Paladín de Maxroll y es la que la propia guía de endgame de Shield Charge te manda usar: *"To get there, level up with one of our Paladin Leveling Guides"*. Sus pros literales son *"Super Fast"*, *"Can Ignore Items"* y *"Easy Endgame Transition"*. Ese **"Can Ignore Items"** es exactamente lo que necesita un principiante: subes sin pelearte con el botín. Y es la misma familia (escudo, bloqueo, Espinas), así que **el equipo que juntes no se tira**.
6. **Dificultad: Difícil (Hard).** Icy Veins lo recomienda explícitamente para el Paladín, y Difícil da **+75 % de experiencia y oro** frente a Normal (Experto +125 %, Penitente +175 %). Si mueres más de una vez cada 20 minutos, baja; si los paquetes se derriten, sube.
7. **Nivel 4: mete Defiance Aura cuanto antes.** Es probablemente el mejor punto por euro de todo tu árbol temprano: **+50 % de armadura y +50 % a todas las resistencias**, y el texto del juego dice literalmente *"you and your allies"* — **tu pareja también lo recibe**.
8. **Nivel 15: eliges Juramento (Oath). Es Juggernaut.** No hay debate: Shield Charge lleva la etiqueta interna `Skill_Juggernaut` y toda la build se construye sobre Resolve, que es el recurso de ese Juramento. La elección no es "definitoria de build" — la build la elige por ti.
9. **Planes de Guerra: pesca los planes de Oleada Infernal (Helltide)** hasta desbloquear **Hellmouth** y **Writhe and Rot** (⚠️ en el juego se escribe **"Writhe and Rot"**, sin "e" final; Maxroll y d4builds escriben "Rote" y se equivocan). Esos dos nodos convierten cada Hellwyrm en una bolsa de orbes de experiencia. Es el motor de XP de la temporada.
10. **Nivel 25: fuerza planes de Ciudad Subterránea** hasta sacar **Jade Epiphany** (orbes de experiencia al ganar nivel de Sintonía). A partir de ahí alternas Oleadas Infernales ↔ Subterránea hasta 70.
11. **Errores que cuestan horas:** limpiar mazmorras al 100 % (limpia el ~80 %), priorizar Hordas Infernales (van al final), quedarse en Normal "por seguridad", farmear objetos mientras subes, separaros más de 90 m en dúo.
12. **A nivel 70: Penitente → El Foso hasta nivel 10 → Tormento I.** Y ahí empieza el juego de verdad.

**Cuánto tarda:** ninguna fuente preferente publica un tiempo 1→70. Todo lo que circula ("una hora", "menos de dos horas") viene de sitios de venta de oro y boosting. La estimación razonada del informe, marcada como **estimación**: **6–10 h** con las campañas hechas y salto activo; **12–20 h** sin Planes de Guerra. Con 4 semanas, incluso el peor caso cabe de sobra. **Lo que no cabe es hacer las campañas dos veces.**

### 1.3 Si ya estás a 70

1. **Llega a Tormento I (El Foso nivel 10). Es la puerta real.** Por debajo no caen objetos **Ancestrales**, no hay nada que masterworkear, y **la receta de Mítico del Cubo ni siquiera aparece** (exige nivel 70 y Tormento I o superior).
2. **Reasigna el árbol a la plantilla de Shield Charge.** Reasignar puntos de habilidad es **gratis**. Y hay una buena noticia verificada nodo a nodo: **el árbol es IDÉNTICO en arranque, intermedia y endgame — diferencia cero.** Lo pones una vez y no lo tocas más.
   - **Rangos:** Shield Charge **15/15** · Defiance Aura **15/15** · Fanaticism Aura **15/15** · Fortress **15/15** · Clash **4/15** · Condemn **1/15**. Total 83.
   - **Nodos de Shield Charge (los tres, imprescindibles):** **Hit Count As Blocking** (los impactos cuentan como bloqueos — el corazón de la build), **Relentless Charge** (la convierte en habilidad Core: 20 de Fe + 1/s, canalizable sin límite de enfriamiento) y **Damage Bonus** (+10 %[x] por golpear, hasta 30 %[x]).
   - **Barra:** Clash · Shield Charge · Defiance Aura · Condemn · Fanaticism Aura · Fortress.
3. 🔴 **NO abras las Cachés de Mítico del Rango de Temporada con el nigromante.** Maxroll dice que los Míticos que dan son **"class-specific"** y no aclara si eso significa "de la clase que la abre". Son **5 cachés** (rangos 3, 7, 8 y 9×2) y tu nigromante probablemente ya las tiene desbloqueadas. **El coste de esperar es cero; el de equivocarte, la temporada.** Ábrelas con el Paladín delante, y solo después de comprobar en pantalla.
4. **Imprime los 10 aspectos** (§3). Es lo más barato y la build no funciona sin ellos.
5. **Templa "+Máximo de acumulaciones de Resolve" en casco, pecho y pantalones.** Es el temple que más daño te da, por el 4 %[x] de daño por acumulación de Resolve que da Fortress.
6. **NO gastes Obducita hasta Tormento V.** Maxroll, textual, en el tramo de Tormento 1: *"Temper these items instantly, but don't bother with Masterworking yet"*; y en el de Tormento 5: *"Masterwork the rest of your items to 25 Quality"*. **Única excepción: el arma.** Un arma ancestral con buen daño base te dura hasta el final; una pechera de 850 no.
7. **Tu cuello de botella en Tormento I–IV no es la Obducita: son las Almas Olvidadas.** Cada tirada de temple en una pieza ancestral cuesta **25 Almas Olvidadas**; tres cargas = 75 por pieza; diez piezas = **750 Almas Olvidadas** antes de tocar la Maestría.
8. **Glifo Sentinel a tope, primero.** Es el glifo de daño de la build (`DamageWithJuggernautSkills` + daño a enemigos cercanos). Orden completo: **Sentinel → Spirit → Honed → Outmatch → Revenge**.
9. **Farmea el Corrupted Reaper** (Zarbinzet, Hawezar — el "Pandemonium Threshold"). Es la mejor fuente única de **Míticos y de Fragmentos de Pandemónium** de toda la temporada, y el hotfix 3.1.1a le subió las tasas.
10. **Con 4 Fragmentos: al Cubo.** Ver §4 — pero ojo, el orden y las reglas no son los que dice la guía de Maxroll.

---

## 2. Cómo se pilota (dos minutos de lectura que valen más que toda la tabla de aspectos)

**En una frase:** tu escudo es el arma. Cargas sin parar; **cada impacto cuenta como un bloqueo**, y cada bloqueo dispara **Retribution**, una nova de **Espinas (Thorns)** físicas a tu alrededor. No hay rotación de DPS: hay conducción.

**Las cinco reglas duras:**

1. **Clash al menos una vez cada 6 segundos.** Literal del autor de la build. Te da **Marcha del Cruzado** (+30 % de probabilidad de bloqueo), **2 acumulaciones de Resolve por golpe** y **20 de Fe** (⚠️ **20 exactos** — el nodo de "+10 de Fe adicional" es *Faith Generation* y **esta build no lo coge**; si has leído "30 con la mejora", es un error corregido en la refutación).
2. **Shield Charge en canalización continua.** Es tu botón de daño **y** de movimiento.
3. **Condemn para agrupar.** Atrae enemigos, aplica **Vulnerable** y **Debilitar**, y te vuelve **Sin Obstáculos** mientras lo lanzas.
4. **Fortress contra jefes y apuros.** Inmune **3 s** + zona defensiva; dentro ganas **4,0 %[x] de daño por cada acumulación de Resolve** (con 30 de Resolve eso es enorme) y **Rampart of Thorns** hace **500 % de tu daño de Espinas por segundo** a los de dentro. Enfriamiento **60 s**.
5. **Las dos auras van siempre puestas** (son pasivas). Sus activas son botones aparte: Defiance → **Imparable 2 s**; Fanaticism → **Debilitar en área**.

**La única habilidad mecánica real de la build**, literal del autor: *"maximiza la cantidad de enemigos que golpeas con Shield Charge posicionándote adecuadamente para disparar Hit Count As Blocking tan a menudo como sea posible."*
👉 **No cargues por el borde del grupo. Atraviésalo por el centro.** Eso es todo el pilotaje.

⚠️ **El campo de "rotación" del planificador está VACÍO.** No existe una rotación oficial escrita. Lo de arriba son las reglas explícitas del autor más el texto del juego, no una secuencia inventada.

**Números vivos de Shield Charge, corregidos** (el informe original traía dos valores muertos de Icy Veins):

| Dato | Valor vivo | Origen |
|---|---|---|
| Enfriamiento | **8 s** (no 10) | Notas oficiales 3.1.0: *"Cooldown reduced from 10 to 8 seconds"* + fichero de datos |
| Armadura mientras canalizas | **+60 %** (no "40 % de reducción de daño") | Notas oficiales 3.1.0: *"increased from 40% to 60%"* |
| Daño base | **180 %** (subió desde 90 %) | Notas oficiales 3.1.0 |
| Probabilidad de golpe de suerte | 35 % | Fichero de datos |
| Coste de Fe | **La habilidad base NO cuesta Fe** (va por enfriamiento). Los **20 + 1/s** aparecen **solo con la variante Relentless Charge** | Fichero de datos |

**Y de paso: Heaven's Fury tiene 15 s de enfriamiento, no 30.** Cambia la lectura de "la clase vive de los enfriamientos": con Shield Charge a 8 s y Heaven's Fury a 15 s, el Paladín es bastante menos "botón en enfriamiento" de lo que dicen sus propias fichas.

**Niveles a los que se abre lo tuyo** (datamining, encaja con la escalera genérica publicada por Maxroll):
Shield Charge es habilidad de **Valor → nivel 8**. Su **variante** (donde la build existe de verdad) **nivel 20**. *Phalanx Charge*, **nivel 36**. **Entre el 8 y el 20 juegas con la habilidad cruda: no te frustres.**

**El número que gobierna todo: Resolve.** Base **8**, tope **30**. La aritmética exacta del autor:

| Fuente | Resolve |
|---|---|
| Base | 8 |
| 3 × temple "+6 Máx. Resolve" (casco, pecho, pantalones) | +18 |
| Aspecto del Yunque de Glynn (Glynn's Anvil) | +2 |
| Conjunto Cathan's Righteous Will, 3 piezas | +2 |
| **Total** | **30** |

⚠️ **El temple sale a "+4" de base.** Para llegar a **+6** necesita **crítico de temple Y crítico de Maestría**, literal del autor. Y el "crítico de Maestría" es el **capstone de Calidad 25**, que da **+50 % a un afijo aleatorio**: 4 × 1,5 = 6. Cuadra exacto. **Consecuencia cara: casco, pecho y pantalones tienen que llegar a Calidad 25 Y el capstone tiene que caer justo en ese temple.** Recolocarlo cuesta 100–200 de Obducita + 10 000 000 de oro por intento y por pieza. **Presupuesta eso como tu mayor gasto de Obducita de la temporada, y con 4 semanas apunta a dos de las tres piezas, no a las tres.**

---

## 3. Shield Charge en tres presupuestos

Todo el equipo de esta build vive **dentro del planificador incrustado de Maxroll**, no en el texto de la guía. Los valores de abajo salen del **JSON crudo del planificador** (167 015 bytes, descargado y verificado dos veces de forma independiente).

### 3.1 El árbol y las auras son los mismos en los tres. Lo que cambia es el equipo.

### 🥉 ARRANQUE — recién llegado a 70, cero únicos de equipo

**Qué llevas:** legendarios genéricos a **poder de objeto 850**, **Maestría 0**, con los **10 aspectos** impresos. Temples de Resolve a **+3**. Conjunto de encantos a 2 piezas.
**Resolve alcanzado: ~19.** Es normal.

**Los 10 aspectos y qué hacen** (texto real del cliente):

| Hueco | Aspecto | Efecto |
|---|---|---|
| Casco | **Glynn's Anvil** | Resolve máximo **+2**; **4 % de reducción de daño por Resolve, hasta 40 %** |
| Pecho | **of the Indomitable** | Armadura y reducción de impedimentos = **45 % de tu probabilidad de bloqueo** |
| Escudo | **of Chastisement** | Tus habilidades **Juggernaut** hacen **+75 %[x]** a **jefes y enemigos con control de masas** |
| Arma (Mayal) | **Crushing** | Mientras estás **Fortificado**, **+65 %[x]** de daño |
| Guantes | **of Channeling** | Mientras **canalizas**, **+70 %[x]** a todo el daño ← *Shield Charge canaliza* |
| Pantalones | **of Layered Wards** | Tu reducción de daño bloqueado **+40 %** |
| Botas | **Sticker-thought** | Ganas Espinas mientras canalizas **y 3 s después** |
| Anillo 1 | **of the Juggernaut's Covenant** | Consumir Resolve con el Juramento Juggernaut da **+100 %[x] de daño** |
| Anillo 2 | **of Redirected Force** | Daño de crítico = **60 %[x] de tu probabilidad de bloqueo**. **Bloquear lo duplica 10 s** |
| Amuleto | **of Lapa's Scripture** | **Perder Resolve** te da Espinas 10 s, hasta **20 acumulaciones** |

**No hay ni un aspecto de relleno:** los diez apuntan a Espinas, Bloqueo→Armadura, Bloqueo→Crítico, Canalización→daño y Resolve→daño.

**Cómo se consiguen:** los aspectos legendarios de Paladín **no están en el Códice por mazmorra**. Caen aleatoriamente en legendarios, los **extraes en el Herrero** (queda guardado en el Códice) y los **imprimes en el Ocultista**. Atajo barato: **apostar Óbolos en el Purveyor of Curiosities** eligiendo el tipo de pieza (los **pantalones solo pueden llevar aspectos defensivos**, lo que estrecha muchísimo la lotería para *Glynn's Anvil*; **botas** para *Sticker-thought*). ⚠️ Los costes en Óbolos vienen de extracto de buscador — **míralo en pantalla antes de vaciar el monedero**.

**Runas:** **Cir + Ceh** (pecho) y **Moni + Kry** (pantalones). Solo puedes llevar **2 palabras rúnicas por personaje**.

**Qué hacer, en orden:** (1) imprime los 10 aspectos · (2) templa Resolve en casco/pecho/pantalones · (3) consigue un **Sello Horádrico Legendario** (5 huecos de encanto; con el afijo *"of Glory"* llegan a 6) · (4) empieza a juntar el conjunto **Cathan's Righteous Will**.

> ### 🔓 EL OBJETO QUE ABRE EL SALTO A INTERMEDIA
> ## **Mantle of the Grey** (pecho)
> *"El Juramento Juggernaut hace tus habilidades Juggernaut **25 % más grandes** pero **consume hasta 16 de Resolve**, otorgando **6 %[x] de daño de habilidad Juggernaut por cada punto consumido**."*
> **A 16 puntos consumidos son ~96 %[x]. Es, con diferencia, el mayor multiplicador de la build.**
> **Dónde se farmea:** ⚠️ **conflicto de fuentes declarado.** Un informe lo sitúa en **Duriel** (Icy Veins, página **sin fecha**); el otro en el **Harbinger of Hatred** (fuente secundaria, 18/07/2026). Los dos son jefes de **escalón 2 (Llave de Guarida Mayor)**, así que farmear ese escalón te cubre en ambos casos. **La vía dirigida y fiable es el Cubo Horádrico sobre un ÚNICO DE PECHO** (§4).

---

### 🥈 INTERMEDIA — con los aspectos y los tres únicos clave

| Hueco | Antes | Ahora | Qué ganas |
|---|---|---|---|
| **Pecho** | *of the Indomitable* | **Mantle of the Grey** | hasta **~96 %[x]** |
| **Escudo** | *of Chastisement* | **Herald of Zakarum** | **+50 %** de Fuerza, Resistencia, Armadura y prob. de Retribution · Retribution **+50 % de tamaño** · implícito **+40 % de bloqueo** · **Indestructible** |
| **Pantalones** | *of Layered Wards* | **Tibault's Will** | **+20 %[x]** de daño y +50 de regeneración de recurso **mientras eres Imparable y 5 s después** |
| Poder de objeto | 850 | **900** | Los 900 son los que traen probabilidad de **Afijo Mayor** |
| **Maestría** | 0 | **25** | **+25 % a todos los afijos** + el capstone |
| Temples de Resolve | +3 | **+5** | |
| Runas | CirCeh / MoniKry | **MoniYom / IgniKry** | |
| Encantos | 2 pz + 2 pz | **3 pz Cathan's Righteous Will** | +2/+2 Resolve, reducción de daño |

🔴 **Corrección importante frente al informe original: en INTERMEDIA llegas a Resolve 27, no a 30.** Los temples del perfil intermedio son **+5**, no +6 (8 + 15 + 2 + 2 = 27). **Los 30 son objetivo de endgame.**

**Por qué Tibault's Will es tan bueno aquí y no es obvio:** eres **Imparable casi todo el rato** — te lo dan *Fortress → Unstoppable*, la activa de *Defiance Aura* (2 s) y *Condemn*. Ese 20 %[x] está casi siempre encendido. ⚠️ **En dúo pierdes una fuente más**: *Bastion* de Raheir también da Imparable 1 s a los aliados, y Raheir no aparece en grupo (§6).

**Qué hacer, en orden:** (1) **Maestría a 25**, enfocando los críticos de Maestría en **Probabilidad de Golpe Crítico** — pero recuerda: **casco, pecho y pantalones primero, y ahí el capstone tiene que caer en el temple de Resolve** · (2) re-templar Resolve a +6 · (3) **Andariel / Harbinger of Hatred** para el escudo · (4) Cubo sobre **pantalones** para Tibault's Will · (5) convertir encantos duplicados con la receta **"Reroll Set Charm"** del Cubo hasta tener **Phoba + Mlor + Linta** distintos · (6) subir las runas **Yom** (500 de Ofrenda) y **Kry** (300).

**Prioridad de estadísticas, literal del autor:** *"El valor del multiplicador de Daño de Golpe Crítico sube cuanta más Probabilidad de Golpe Crítico consigas. **Si tienes muy poca Probabilidad de Crítico, los multiplicadores de Daño Físico, Daño a Vulnerables o Daño General valen más.**"*
👉 **Al principio: Daño Físico / a Vulnerables / General. Cuando el crítico suba, invierte el orden.**

**Temples exactos:** casco/pecho/pantalones → **Máx. Resolve**; escudo y arma → **Prob. de Crítico** (+5 % → +10 %); guantes → **Daño Físico** (+40 % → +50 %); botas → **Potencia de Aura** (+10 % → +20 %); anillos y amuleto → **Reducción de Recarga** (+6 % → +7,5 %).

**Los manuales de temple que definen la build** (datamining; ninguna guía los publica así): **`Juggernaut Augments`** (daño de Shield Charge y de Retribution), **`Paladin Resolve`** (máximo de acumulaciones de Resolve) y **`Paladin Perseverance` / `Paladin Guard`** (probabilidad de bloqueo). Los manuales **legendarios** empiezan a caer con más frecuencia **a partir de Tormento II** — es una razón para no quedarse en T I más de lo necesario.

> ### 🔓 EL OBJETO QUE ABRE EL SALTO A ENDGAME
> ## No es un objeto: son **los glifos a 150 y los Afijos Mayores**
> El endgame **no es otra build, es la misma afinada.** Mismo árbol, mismos aspectos, mismos únicos, mismas runas, mismo Paragón. Lo que cambia son valores.
> *(El informe original ponía aquí "el Mítico crafteado, y solo UNO". **Esa recomendación era falsa** — ver §4.)*

---

### 🥇 ASPIRACIONAL (endgame) — el mismo equipo, exprimido

Diferencias reales respecto a intermedia, verificadas en el planificador:

- **Afijo extra *"of Steel"* en las 10 piezas** (daño físico, valor 0,125) — ausente en intermedia.
- Valores de afijo mucho más altos (Espinas 915 → **1 907**; *of Vigor* 1 225 → **1 812**).
- **Temples de Resolve a +6 → Resolve 30 por fin.**
- **Glifos a nivel 150** (no 100).
- **5 encantos del conjunto** (3 piezas distintas: Phoba, Mlor, Linta) + **Griswold's Opus**.

**Paragón — 5 tableros en este orden exacto:**

| # | Tablero | Glifo |
|---|---|---|
| 0 | Start | **Revenge** |
| 1 | **Relentless** | **Outmatch** |
| 2 | **Beacon** | **Honed** |
| 3 | **Castle** | **Spirit** |
| 4 | **Shield Bearer** | **Sentinel** |

🔴 **Dos correcciones sobre el informe original:** el planificador guarda **cuatro** pasos, no tres, y **los glifos llegan a 150, no a 100**. Y Shield Bearer a glifo 100 activa **75 nodos** (el informe ponía un guion).

⚠️ **Trampa de nombres:** hay **tres glifos distintos llamados Spirit**, tres llamados Outmatch y tres llamados Revenge. Los correctos son **Spirit de Voluntad (Willpower)**, **Outmatch de Fuerza** y **Revenge de Inteligencia**. **Si coges el Spirit de Destreza te equivocas.**

**Qué hacer:** (1) glifos a 150 en el orden **Sentinel → Spirit → Honed → Outmatch → Revenge** · (2) cazar **Afijos Mayores** en las piezas clave · (3) completar el capstone de Maestría en cada pieza.

**Encanto único de la build: Griswold's Opus.** 🔴 **Sus números estaban inflados ×3 en el informe original.** Lo real: **1 %[x] de Daño de Golpe Crítico por cada enemigo golpeado en 10 s, hasta 50 %[x]** (el "150" es la **Vida curada** del efecto de Golpe de Suerte, no un tope de daño). Y ⚠️ **es un ENCANTO, no la espada del mismo nombre**: la ruta de caída "Duriel / Harbinger" que circula es la **de la espada**. **La fuente de caída del encanto está sin verificar.** Sigue mereciendo la pena, pero **no es prioridad 3 como decía el informe**.

**Solo si empujas Foso alto (variante Push):** sello **Seal of the Diamond Mind** (6 huecos), amuleto **Blood-Mad Idol**, botas con *Exploiter's Aspect*, y el árbol reconfigurado (Clash 4→10, sin las 6 mejoras de Aura). **No es para ti todavía.**

---

## 4. Los Míticos, en orden

*(Esta es la pregunta que hiciste. Léela entera antes de gastar un solo fragmento.)*

### 4.1 Tres cosas que cambian la respuesta y que casi toda la web sigue contando mal

**🔴 (1) La regla del "solo puedes equipar UN Mítico crafteado" YA NO EXISTE.**
Blizzard la eliminó en el hotfix **3.1.1a del 16/07/2026**, literal en el foro oficial:
> *"Removed the 'one-crafted Mythic' equipment restriction on Mythic items."*

Corroborado por Icy Veins (16/07/2026) y confirmado: **ni 3.1.2 ni 3.1.3 la reintroducen.**
**La guía de tu build en Maxroll (act. 25/07/2026) sigue diciendo lo contrario** — el autor guardó el planificador **nueve días después** de que la regla desapareciera. La misma frase muerta está en **tres** guías de Maxroll y en dos de los informes de este proyecto.
👉 **Puedes craftear y equipar los TRES.** Esto cambia por completo el plan de farmeo de tus 4 semanas.
⚠️ **Ventana temporal:** en la Temporada 15 está previsto que el límite **vuelva** para lo hecho en el Cubo (fuente: PTR 3.2, **no está vivo**). **Craftea ahora.**

**🔴 (2) El Cubo te da un Mítico ALEATORIO de la ranura, no el objeto que quieres.**
Metes un único de pecho, sale **un mítico de pecho cualquiera**. Confirmado en notas oficiales (*"now always creates an item for the same gear slot"*) y en Maxroll (*"the upgrade yields a random item of the same slot"*).
👉 **"Ir a por Mantle of the Grey" significa en realidad "gastar los fragmentos metiendo únicos de PECHO".** El orden de abajo es un **orden de ranuras**, no una lista de la compra.

**🔴 (3) Mítico ya no es una rareza: es una CALIDAD de objeto.**
Cualquier Único puede ser Mítico. Todo Mítico es **Ancestral**, su **Poder Único sube un +30 %** y **el resto de afijos salen al valor máximo**. Por eso *Mantle of the Grey*, *Tibault's Will* y *Herald of Zakarum* aparecen en el fichero como **Únicos normales**: lo que persigues es su **versión Mítica**.

### 4.2 El orden, y por qué

Es el orden de la guía de la build (Maxroll, 25/07/2026), y para el primer puesto hay además un argumento de datos.

| Orden | Objetivo | **Ranura donde gastas** | Qué te da |
|:--:|---|---|---|
| **1º** | **Mantle of the Grey** | **PECHO** | ~96 %[x] en versión Única · **~124,8 %[x] en versión Mítica** |
| **2º** | **Tibault's Will** | **PANTALONES** | **+20 %[x]** casi permanente (eres Imparable casi siempre) |
| **3º** | **Herald of Zakarum** | **ESCUDO** | +50 % Fuerza/Resistencia/Armadura/prob. Retribution · +40 % bloqueo · Indestructible |
| *(solo variante Push)* | Blood-Mad Idol | Amuleto | No es para ti |

**Por qué Mantle of the Grey es el primero — argumento de datos, no de opinión.**
De las **6 196 entradas de afijo** del fichero del juego, **solo DOS** usan la fórmula `S14_Mythic_UniquePotency`, que **sustituye la tirada aleatoria por el tope multiplicado por la potencia Mítica**. Una es *Protean Heart* (Espiritista). **La otra es Mantle of the Grey.**

| Versión | Por punto de Resolve | ×16 puntos consumidos |
|---|---|---|
| Único con mala tirada | 4 %[x] | ~64 %[x] |
| Único con tirada perfecta | 6 %[x] | ~96 %[x] |
| **Mítico** | **7,8 %[x]** | **~124,8 %[x]** |

*(El 7,8 % sale de aplicar el +30 % oficial a la fórmula datamineada, y el fichero corrobora las unidades. Marcado como **cálculo**, no como cifra leída en pantalla.)*
⚠️ **Corrección de método:** el informe original decía que solo dos objetos llevan la etiqueta `{if:IsMythic}`. **Falso: la llevan 279.** La etiqueta exclusiva de dos es la otra. **La conclusión aguanta; la prueba citada, no.**

### 4.3 La receta, los materiales y la dificultad mínima

| Concepto | Valor | Fuente |
|---|---|---|
| **Ingrediente 1** | 1 Único **de la ranura que quieras**, **850+ de Poder de Objeto** | Maxroll, 24/06/2026 |
| **Ingrediente 2** | **4 Fragmentos de Pandemónium** | **Oficial, parche 3.1.1 (14/07/2026)**: *"Reduced the cost… from 5 to 4 Pandemonium Fragments"* |
| **Nivel mínimo** | **70** | Maxroll |
| **Dificultad mínima** | **Tormento I o superior** — *"the recipe does not show up if you don't meet those criteria"* | Maxroll, 24/06/2026 |
| Nombre de la receta | **"Craft"** (antes "Upgrade") | Oficial, 3.1.2 |
| Restricción | Un Mítico **no** puede usarse como ingrediente | Oficial, 3.1.0 |
| Restricción | **Encantos y Sellos ya NO admiten calidad Mítica en el Cubo** | Oficial, hotfix 3.1.1a |

⚠️ **Si ves "5 fragmentos" por ahí, es dato muerto**: dos páginas de Maxroll (13 y 16/07) publican el 5 porque son de la víspera del parche. **Gana Blizzard: son 4.**

**De dónde salen los Fragmentos de Pandemónium:**

| Origen | Detalle |
|---|---|
| **Corrupted Reaper** (jefe estacional, Zarbinzet/Hawezar) | **Hasta 2 por muerte, escalando con el Tormento** (oficial, 3.1.1). **La mejor fuente del juego**, y 3.1.1a le subió las tasas de Mítico |
| **"Glints of Hope"** (recompensa repetible del tablero de reputación) | **Garantiza 1** (oficial, 3.1.1) |
| Rupturas de Pandemonio y Cachés Resplandecientes | Maxroll |

**Cuenta de la vieja:** 4 fragmentos por crafteo, hasta 2 por Reaper → **entre 2 y 4 runs del Reaper por Mítico**. Con las tres ranuras, presupuesta **6–12 runs**. Cabe en 4 semanas.

**La escalera de llaves — y una trampa de traducción que te manda a farmear al jefe equivocado:**

| Llave (inglés) | **Español correcto** | Abre |
|---|---|---|
| Lair Key | **Llave de Guarida** | Varshan, Grigoire, Beast in the Ice, Lord Zir, Urivar |
| Greater Lair Key | **Llave de Guarida MAYOR** | **Duriel, Andariel, Harbinger of Hatred**, Bloody Butcher |
| Superior Lair Key | **Llave de Guarida SUPERIOR** | Belial · **Corrupted Reaper** |

🔴 **"Betrayer's Husk" ya no existe con ese nombre.** Notas oficiales: *"Betrayer's Husks… are now known as **Superior Lair Keys**"*. Cualquier guía que te pida 2 Husks para Belial es anterior al cambio.
**Las Llaves Superiores** salen de las **Cámaras Deathtoll** (*"will always reward at least one Superior Lair Key **in high Torment levels**"* — ojo al condicional), de la emboscada de Belial, y de los **anillos de llaves del Rango de Temporada**.
**Las Llaves Mayores caen con más frecuencia a partir de Tormento VI** — y son las de los tres jefes que sueltan tus tres únicos. Ese es tu objetivo intermedio entre T V (Obducita) y T VII (Polvo Volátil).

### 4.4 La vía gratis que casi nadie aprovecha: el Rango de Temporada

**5 Cachés de Mítico** en los rangos **3, 7, 8 y 9 (×2)**, más **Chispas Resplandecientes** en 6, 8 y 9. El Rango de Temporada es **progreso de cuenta**, así que tu nigromante ya te ha desbloqueado parte.
🔴 **Y aquí está la acción más urgente de todo el documento: no las abras con el nigromante.** Maxroll dice que los Míticos son **"class-specific"** y **ninguna fuente fiable aclara si depende de la clase que la abre**. Si depende, abrirlas con el nigromante te tira **cinco Míticos de Paladín** a la basura.

### 4.5 La vía de las Chispas Resplandecientes — léela en pantalla antes de gastar

Las fuentes se contradicen. Lo que dice la chuleta de crafteo de Maxroll (14/07/2026), según la lectura de la refutación:

| Receta | Vendedor | Coste | Resultado |
|---|---|---|---|
| Random Mythic **Item** (por tipo) | **Herrero** | **3** Chispas + 3 runas + **5 000 000** de oro | Mítico aleatorio de ese tipo |
| Random Mythic **Unique** | **Herrero** | **2** Chispas + **50 000 000** de oro | **Un Icónico del pool de 13** |

⚠️ Uno de los informes atribuyó la segunda receta al **Joyero**; la refutación lo corrige al **Herrero** (y el propio fichero del juego llama a la caché `BlackSmith_MythicCrafting`). **Contradicción declarada: lee la receta en pantalla antes de gastar.**
⚠️ Y **no tomes esa decisión con el artículo de Icy Veins "Do Not Waste Resplendent Sparks"**: su razonamiento se apoyaba explícitamente en el límite de un Mítico crafteado, que **ya no existe**.

### 4.6 ¿Y los Míticos "clásicos" (Shako, Grandfather, Starless…)?

Hay **13 Míticos Icónicos**; el Paladín puede llevar **10**. Pero **la guía de tu build no recomienda ninguno**, y tiene sentido estructural: tu daño sale de **Espinas y Resolve**, no de multiplicadores genéricos de crítico o de recurso.

- **The Grandfather** es espada a dos manos → **te quita el escudo, que es tu build entera**. Descártalo pese a su fama.
- **Melted Heart of Selig** te quita el **75 % de la Vida**.
- **Ring of Starless Skies** premia gastar recurso; tú apenas gastas.
- **Tyrael's Might** (+20 % reducción de daño) **compite con Mantle of the Grey por el pecho**: gana Mantle.
- **Harlequin Crest (Shako)** (+6 rangos a todas las habilidades) va al **casco** y **no compite con nada tuyo**. Si te cae gratis, póntelo.
- **El'Druin, Sword of Justice** es Mítico de espada a una mano, el Paladín puede llevarla, y se añadió a la caché del Herrero en 3.1.1. Es el candidato natural de arma si aparece.

👉 **Regla: no los persigas, pero no los deseches si caen.**

---

## 5. ¿Shield Charge o las de bárbaro?

### 5.1 Lo primero: cómo NO comparar

Maxroll publica **dos familias de listas distintas**: las **por clase** (ordenan builds de Paladín entre ellas) y las **globales** (ordenan todas las builds de todas las clases). **Comparar la "A" de la lista de Paladín con la "S" de la de Bárbaro es un error de escala.** Todo lo de abajo usa **listas globales**.

### 5.2 La comparación directa que sí existe

**Maxroll, listas globales, todas fechadas 22–23/07/2026, Temporada 14:**

| Eje | Whirlwind Barb | Mighty Throw Barb | Minion Barb | **Shield Charge Pal** |
|---|:--:|:--:|:--:|:--:|
| Endgame general | **S** | **S** | **S** | **A** |
| Empuje de Foso | **S** | **S** | **S** | **A** |
| **Jefes (bossing)** | **S** | **S** | **S** | **S ← empate** |
| Farmeo rápido | **S** | **S** | **S** | **A** |

**Segunda fuente, independiente, a nivel de clase:** Icy Veins, lista de clases (04/07/2026) — Paladín **A** / Bárbaro **S** en empuje de endgame. **El mismo hueco de un escalón, obtenido por otra redacción.**
⚠️ **Matiz honesto:** esa página es del 04/07, **anterior a que se publicara la guía de Shield Charge** (20-25/07). Valora la clase *sin* tu build. Corrobora la tendencia, no la posición exacta.

### 5.3 La respuesta, sin adornos

**Sí hay una comparación directa publicada, y sí dice que las tres de Bárbaro están por delante** — un escalón, en tres de los cuatro ejes, según el mismo equipo editorial y en la misma escala. **Empatan en jefes.**

**Pero lo que NO existe, y no me lo voy a inventar:**
- **Ninguna cifra de DPS comparando Shield Charge con las builds de Bárbaro.** Ninguna fuente abierta la publica.
- **Ningún número de Foso** ("aguanta Foso 110") en ninguna de las ocho listas consultadas. **Solo ordenan por letra.** Si alguien te da un número de Foso, pídele la URL.
- **Ningún marcador numérico de dificultad** (tipo "3/5 en complejidad"). Las guías de Maxroll **no lo tienen** en S14; solo Pros y Contras en texto.

### 5.4 Lo que sí dicen las guías, palabra por palabra, sobre facilidad

| Build | Pros (literal) | Contras (literal) |
|---|---|---|
| **Shield Charge Pal** | *"Zoomy zommy"*, *"Hits enemies with a Shield"* | *"Short range"*, ***"Requires good positioning"*** |
| **Whirlwind Barb** | *"Incredible AoE Clear"*, *"Super Fast"*, *"Spin2Win"* | ***"Endgame Gearing"***, *"High Cooldown Requirement"* |
| **Mighty Throw Barb** | *"Extremely Tanky"*, ***"Super easy to play"***, *"Very fast"*, ***"Low gear requirements"*** | *"Maximal screen clutter"* |
| **Minion Barb** | *"High Mobility"*, ***"Very Easy to Play"***, ***"Strong Without Mythics"*** | *"Gear Reliant"*, ***"Many Buttons"***, *"Screen Clutter"* |

**Lectura para tu caso concreto (principiante, 4 semanas, quiere daño alto sin rotaciones imposibles):**

- **Mighty Throw Barb es, por escrito y de forma explícita, la más fácil.** Es la **única** de las cuatro cuya propia guía dice a la vez *"super fácil de jugar"* y *"pocos requisitos de equipo"*. Si tu único criterio fuera "máximo daño con mínimo esfuerzo", esa es la respuesta que dan las fuentes.
- **Shield Charge no reclama facilidad en ningún sitio.** Su contra es **"requiere buen posicionamiento"** y **alcance corto**. **No es difícil de pulsar; es exigente de colocar.** Fallar el ángulo es perder el daño.
- **Whirlwind** avisa de **equipo de endgame exigente**: con 4 semanas, es la que más te va a pedir farmear.
- **Minion Barb** dice "muy fácil" pero también **"muchos botones"**. Se contradice para alguien que empieza.

**Y tres cosas que las tier lists no capturan y sí valen para ti** *(esto es criterio, no dato citado, y lo marco como tal)*:

1. **Cambiar a Bárbaro es empezar otro personaje de cero** — y tú acabas de decidir jugar Paladín.
2. **Shield Charge empata en S para jefes**, que es exactamente donde vas a pasar las últimas semanas (Duriel, Andariel, Harbinger, Corrupted Reaper).
3. **En dúo, el Paladín aporta lo que el Bárbaro no**: las tres auras dicen literalmente *"and your allies"*. Tu pareja recibe **+50 % de armadura, +50 % de resistencias, +15 % de vida máxima, velocidad de ataque, probabilidad de crítico, daño de crítico y +25 % de generación de recurso**. Media de tu tiempo de juego es en dúo. Eso no aparece en ninguna lista.

**Y un aviso más, dentro del propio Paladín:** en **farmeo rápido global**, el Paladín **sí tiene builds S** — **Wing Strikes** y **Blessed Hammer** (Hammerdin). Simplemente no es Shield Charge la que las tiene. Si algún día quieres una build de barrer rápido, **la tienes sin cambiar de personaje**.

⚠️ **Sobre "Wing Strikes es la mejor build de Paladín":** es **S** en farmeo rápido y **C/D** en endgame, empuje y jefes. Quien lo dice a secas está generalizando una lista de farmeo.

---

## 6. El dúo

Tú: Paladín con Vessel of Hatred **y** Lord of Hatred. Ella: nigromante **sin ninguna expansión**.

### 6.1 Lo bueno: sois compatibles justo donde importa

| Actividad | ¿Juntos? |
|---|:--:|
| Oleadas Infernales (zonas base) | ✅ |
| Mazmorras de Pesadilla | ✅ |
| **Rupturas de Pandemonio** (la mecánica de la temporada) | ✅ |
| El Foso, Hordas Infernales, Susurros | ✅ |
| Ciudad Subterránea de Kurast | ❌ (necesita Vessel of Hatred) |
| **Planes de Guerra** | ❌ (necesita Lord of Hatred; **el plan se inicia en Temis, Skovos**) |
| Cualquier cosa en Nahantu o Skovos | ❌ |

**Ella sí puede llegar a nivel 70** (*"The level cap increases to 70 for everyone, not just expansion owners"*), **sí tiene el rework completo del árbol de habilidades**, **sí puede hacer la mecánica estacional entera** (arranca en Kyovashad, ciudad del juego base) y **sí puede completar ~85 % del Rango de Temporada** (*"About 15% of the objectives require Lord of Hatred"*).

**Lo que no tiene:** Paladín y Brujo, Skovos/Temis, la continuación de la campaña, Echoing Hatred, Planes de Guerra, el sistema de **Talismán y Encantos**, el **Cubo Horádrico**, y las *"20+ opciones de habilidad transformadoras exclusivas de la expansión"*. Sin Vessel of Hatred, además: Nahantu, Ciudad Subterránea, **mercenarios** y **palabras rúnicas**.

**La buena noticia:** vuestro terreno común —**Oleadas Infernales + Mazmorras de Pesadilla + Rupturas**— es **exactamente el mejor bucle de experiencia de la temporada**. El dúo no os frena para subir a 70; os frena para el endgame de expansión.

**La mala:** tu mejor ruta individual (Planes de Guerra + Ciudad Subterránea) es contenido que ella **no puede tocar**. **Vas a tener que partir las sesiones**: en solitario para Planes de Guerra y Subterránea; en dúo para lo demás.

### 6.2 🔴 En dúo pierdes a Raheir. Y con él, un 25 %[x] de daño

La configuración de la build es **Raheir contratado (Hired) + Aldkin de refuerzo (Reinforcement)**:

| Nodo de Raheir | Efecto |
|---|---|
| **Bastion** | Toma posición 5 s **redirigiendo hacia sí el 90 % del daño** que recibirían los aliados cercanos, y **los vuelve Imparables 1 s** |
| **Inspiration** | Los enemigos afectados por Ground Slam reciben **+15 %[x]**; los aliados afectados por Bastion infligen **+25 %[x]** |
| **Raheir's Aegis** | **+15 % de resistencia a todos los elementos** |

**El mercenario Contratado pasa a reserva cuando te unes a un grupo; solo el Refuerzo se puede invocar.** Es lo que dice tu briefing y lo corroboran fuentes secundarias.

⚠️ **Honestidad sobre esta regla: NO está confirmada en ninguna página preferente fechada dentro de 3.1.x.** La única página de mercenarios de Maxroll es del **11/07/2025** (más de un año) y **no describe el comportamiento en grupo**. La refutación lo señaló expresamente. La regla es casi seguro cierta, pero **compruébala en pantalla**.

**Traducción para tus tardes con ella:**
- **En solitario:** Raheir + Aldkin. Build completa.
- **En dúo:** **Raheir desaparece.** Pierdes **Inspiration (+25 %[x] de daño)**, **Bastion (90 % de redirección + Imparable)** y **+15 % de resistencias**. Y al perder el Imparable de Bastion, **Tibault's Will se te enciende algo menos**.

👉 **Consecuencia práctica y muy importante: en dúo pegas y aguantas notablemente menos que en solitario con el mismo equipo. NO es que lo estés haciendo mal.** Si notas el bajón al jugar con ella, es esto.

### 6.3 La compensación: tú eres el ancla del grupo

Las tres auras dicen literalmente **"you and your allies"** en el texto del juego. Tu pareja recibe, sin comprar nada:

- **Defiance Aura:** +50 % de armadura, +50 % a todas las resistencias, **+15 % de vida máxima** (nodo *Maximum Life*), **+25 % de sanación recibida** (nodo *Bonus Healing*).
- **Fanaticism Aura:** velocidad de ataque, probabilidad de crítico, **daño de golpe crítico** (nodo *Rite of Vengeance*) y **+25 % de generación de recurso** (nodo *Resource Generation*).
- **Fortress:** acumulaciones de Resolve **cada 0,5 s** a ti y a tus aliados.

**En dúo tú pierdes daño individual, pero el conjunto gana bastante.** Y Maxroll considera al Paladín *"la mejor clase de apoyo del juego"*.

### 6.4 Cuatro detalles operativos del dúo que valen dinero

1. **Manteneos a menos de 90 metros.** El bonus de grupo es **+10 % de experiencia** y solo dentro de ese radio. **No se acumula** con más miembros.
2. **En dúo, el mundo abierto es más eficiente que las mazmorras.** *"La vida y el daño de los monstruos en el mundo abierto NO escalan con el número de jugadores; en mazmorras SÍ."* Meteros los dos en una mazmorra instanciada "para ir más rápido" la hace más dura sin darte más experiencia.
3. 🔴 **Abrid cada uno vuestro propio Alijo (Hoard) de jefe.** Tooltip literal del juego: *"Belial only drops his treasure for those who opened the Hoard that caught his attention."* Si Belial embosca y solo abriste tú, **ella no cobra**.
4. **No repartáis materiales a medias.** Ella **no tiene Cubo Horádrico ni sistema de Encantos**: los **Fragmentos de Pandemónium**, el **Polvo Primordial** y los **Set Charms** son material que **solo tú puedes usar**.

---

## 7. Lo que no se sabe

Todo esto queda **explícitamente sin resolver**. Nada de aquí se ha rellenado por inferencia.

### 7.1 Huecos que te afectan a la cara

1. **Dónde cae exactamente *Mantle of the Grey*.** Dos informes de este proyecto dan **jefes distintos** (Duriel vs Harbinger of Hatred), ambos apoyados en fuentes débiles: la página de únicos de Icy Veins **no muestra fecha** y la otra es secundaria. **Los dos son de escalón 2, así que farmear Llaves Mayores te cubre — pero el jefe concreto no está establecido.**
2. **Dónde cae *Herald of Zakarum*.** Confianza **baja**: solo extracto de buscador y una página sin fecha (Andariel / Harbinger).
3. **De dónde cae el ENCANTO *Griswold's Opus*.** La ruta Duriel/Harbinger que circula es la de la **espada** del mismo nombre. Para el encanto, **sin verificar**.
4. **Si las Cachés de Mítico del Rango de Temporada dan el objeto de la clase que las abre.** Maxroll dice "class-specific" sin explicar el mecanismo. **Es la duda más cara del documento.**
5. **Cuántas Llaves Superiores hace falta para el Corrupted Reaper.** Maxroll dice "two" en un sitio y "1x" en otro. La refutación sospecha que el "two" es un resto del mundo viejo de los dos Betrayer's Husks. **Cuéntalas en el juego.**
6. **El coste real de la ruta de Chispas Resplandecientes.** Las fuentes se contradicen entre **2 y 3 Chispas**, entre **Herrero y Joyero**, entre **3 y 18 runas**, y entre **5 000 000 y 50 000 000** de oro. **Lee la receta en pantalla.**
7. **Confirmación fechada de que el mercenario Contratado desaparece en grupo.** Solo fuentes secundarias; la página de Maxroll es de 11/07/2025.
8. **Si un Paladín YA CREADO recibe acceso a Planes de Guerra retroactivamente** cuando otro personaje completa la campaña de Lord of Hatred. La fuente dice *"any future characters"*. **No hay nada sobre personajes preexistentes.**
9. **Si se puede cambiar de Juramento, y a qué coste.** Ninguna fuente preferente y fechada lo dice. Hay un hilo de soporte oficial ("la Armería no guarda el Juramento") cuyo mero enunciado implica que **se cambia**, pero no lo confirma. **Míralo en la pantalla del Juramento.**
10. **Si la afinidad (Rapport) de mercenarios es de cuenta o por personaje.** Sin fuente fechada.

### 7.2 Números que simplemente no están publicados

11. **Cifras de DPS comparando builds.** No existen en ninguna fuente abierta.
12. **Números de Foso por build.** Ninguna de las ocho tier lists los publica. Solo letras.
13. **Objetivos numéricos de armadura, resistencias, vida o Dureza por tier de Tormento.** **Ninguna fuente preferente fechada en 3.1.x los publica.** Maxroll da la fórmula (`DR = Armadura / (Armadura·10/9 + 5678)` a nivel 70, tendiendo al 90 %) pero **explícitamente ningún objetivo**.
    🔴 **Y las cifras que devuelven los buscadores —"13 500 de armadura", "45 000 de vida", "cap de resistencias 70 %", "−25 % de resistencias por cada tier de Tormento"— NO las sostiene nada.** El campo `worldTiers` del cliente 3.1.0 contiene, para cada uno de los doce Tormentos, **exactamente dos atributos: multiplicador de oro y multiplicador de experiencia. Ninguna penalización defensiva.** Trátalas como muertas.
14. **Cifras objetivo de velocidad de ataque, crítico, vida o armadura para esta build.** El planificador **no las tiene**: su campo de estadísticas fijadas solo contiene `{Shield Charge: Damage, Fortress: Cooldown}`. **El único número duro de la build es Resolve = 30.**
15. **Cuántos Afijos Mayores caben por pieza.** La cifra que circula (3 / 4 / 1, ×1,5 al máximo) **solo la sostienen una fuente vetada y agregadores sin fecha**.
16. **El valor máximo de Fe.** No aparece como número plano en ninguna fuente ni en el fichero.
17. **Los valores de daño base (% de daño de arma) de cada habilidad.** El fichero los guarda como fórmulas sin resolver.
18. **Los nombres en español de las 24 habilidades.** Ninguna fuente los publica; el fichero solo trae inglés. **La pantalla del juego manda.**
19. **Tiempo real 1→70 en fuente preferente.** No existe. Todo lo publicado es de sitios de boosting y venta de oro.
20. **Obducita por run de Cámara Fuerte Horádrica.** Solo hay un dato (~350/min a tier 6 en Tormento XII); no hay tabla por tier.

### 7.3 Contradicciones abiertas entre fuentes fiables

21. **Escalado por rango de habilidad.** El fichero dice que el rango 15 multiplica **×1,40** la parte escalada (14 puntos para un +40 %). La página de árboles de Maxroll dice *"cada punto extra hace la habilidad un 10 % más potente"*. **Se contradicen frontalmente y nadie lo resuelve.**
22. **La runa Yom.** El fichero dice *"aturde y aumenta tu Daño de Golpe Crítico contra ellos"*; la página de runas de Maxroll dice *"aturde y **restaura 100 de Recurso**"*. **No dicen lo mismo.**
23. **Puntos de habilidad del Rango de Temporada:** Maxroll y el planificador dicen **14**; el anuncio oficial de la Temporada 14 dice **"up to 12"**. El total de 83 (69+14) sí está corroborado oficialmente.
24. **El Neathiron.** El tooltip del propio juego dice que el material *"desapareció misteriosamente"*, pero el mismo cliente sigue anunciando *"Neathiron cae más a menudo"* en Tormento IV, y Maxroll aún lo cobra para recolocar el capstone de una pieza de 900. **Si tienes Neathiron, refínalo a Obducita. Si un coste te lo pide, compruébalo en el yunque.**
25. **Si los encantos duplicados acumulan bonificación de conjunto.** El endgame lleva **tres Phoba**. El informe concluyó que corre la bonificación de 3 piezas; **la refutación lo degrada a hipótesis** porque las bonificaciones son escalonadas y acumulativas, y llevar 5 piezas también otorgaría el escalón de 3. **La página de talismán de Maxroll no lo aclara.**

### 7.4 Cosas que no se pudieron consultar

26. **Mobalytics está bloqueado a nivel de dominio** (HTTP 403 en todas las rutas probadas). Su tier list de Paladín y su guía de Shield Charge **no se han leído**.
27. **Reddit está bloqueado** para el rastreador de este proyecto. **No hay ningún contraste de comunidad en ninguno de los seis informes.**
28. **La guía de Shield Charge de Wowhead** devuelve solo navegación, y su cabecera marca **08/03/2026 — anterior al lanzamiento del Paladín**. Material de pre-lanzamiento. **No se ha usado nada de ella.**
29. **`pal-equipo` y `pal-leveling` no han pasado por refutación adversarial.** Sus datos sobre progresión de materiales, Maestría, temple, herencia de cuenta y ruta de subida **no han sido atacados por un segundo lector**. Es la parte menos garantizada de este documento.

---

## 8. Las siete cosas de esta semana, en una tabla

| # | Acción | Por qué |
|:--:|---|---|
| **0** | **No abras las Cachés de Mítico del Rango de Temporada con el nigromante** | Son 5 y podrían ser específicas de clase. Coste de esperar: cero |
| **1** | **Llega a Tormento I** (El Foso 10) | Sin Ancestrales no hay nada; sin Tormento I la receta de Mítico ni aparece |
| **2** | **Imprime los 10 aspectos** | La build no funciona sin ellos y son lo más barato |
| **3** | **Templa Resolve en casco, pecho y pantalones** | Escala el 4 %[x] por acumulación de Fortress |
| **4** | **Farmea el Corrupted Reaper** (Zarbinzet) | Mejor fuente del juego de Míticos **y** de Fragmentos |
| **5** | **Cubo: 4 Fragmentos + un único de PECHO** → repite | Mantle of the Grey es el mayor multiplicador. **Y ahora puedes equipar los tres crafteados** |
| **6** | **Maestría a 25 solo a partir de Tormento V** (excepto el arma) | Maxroll, textual. Antes es tirar Obducita en piezas que reemplazas |
| **7** | **Glifo Sentinel a tope** | Es el glifo de daño de la build |

**No hagas esto:** no cargues por el borde de los grupos · no cojas el glifo *Spirit* de Destreza · no sigas la guía de leveling de Shield Charge (es de Season 12) · no te creas ninguna página del Paladín anterior al 28/04/2026 · no te creas los titulares de "Paladín domina con builds S" (son del PTR) · y **no te creas la regla del "solo un Mítico crafteado": murió el 16/07/2026**.
