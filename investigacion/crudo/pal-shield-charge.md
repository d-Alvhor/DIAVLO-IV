# Paladín Carga con Escudo (Shield Charge Paladin) — Season 14 "Death Awakening"

**Investigado:** 24/08/2026 · **Parche vivo declarado:** 3.1.3 (build 73224, 12/08/2026)
**Dominio:** la build completa, con tres presupuestos y ruta de adquisición por objeto.

---

## 0. Antes de nada: de dónde sale cada número (léelo)

Esta guía tiene **tres calidades de dato** y están marcadas en todo el documento. No las mezcles.

| Marca | Qué significa | Fiabilidad |
|---|---|---|
| **[PLAN]** | Sale del **planificador real de Maxroll** de esta build, descargado en crudo (JSON, 167 KB). Es literalmente lo que el autor guardó. | Máxima para *qué* lleva la build |
| **[DATA]** | Sale del **fichero de datos del juego** que sirve Maxroll (`data.min.json`, 11.606.292 bytes descargados). Es **datamining**: tooltips y fórmulas reales del cliente. | Máxima para *qué hace* cada cosa |
| **[WEB]** | Página web fechada que abrí y leí. | Buena |
| **[EXT]** | **Extracto de buscador**, página no abierta o bloqueada. | Baja — verifícalo en pantalla |

### ⚠️ Desfase de versión que debes conocer

El fichero de datos del juego se identifica a sí mismo como **versión `3.1.0.72698`** — comprobado leyendo el campo `version` del JSON. **Tu parche vivo es 3.1.3 (build 73224).** Es decir: **el datamining va una revisión por detrás de tu cliente.**

Esto **no invalida la build**, y hay una razón concreta:

- Las notas oficiales de **3.1.3 (12/08/2026) no tocan ninguna clase ni ningún objeto**. Son arreglos de bugs (Corrupted Reaper, portal del Echo of Mephisto, objetivo de Rango de Temporada) — [icy-veins 3.1.3](https://www.icy-veins.com/d4/news/diablo-4-3-1-3-patch-notes-easier-season-objectives-and-echo-of-mephisto-portal-fix/) **[WEB]**, corroborado por [news.blizzard.com](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) **[WEB]**.
- Por tanto, **para efectos y números de esta build, 3.1.0 ≈ 3.1.3.** Lo que no puedo descartar es un cambio en **3.1.1 / 3.1.2**, que no he podido leer íntegros. Ver "No encontrado".

**Nada de este documento viene de PTR ni de beta.** La build es de parche vivo. Lo único con sabor a PTR que apareció en las búsquedas fue el hilo del foro "Patch 3.2 PTR" — **no lo he usado para nada**.

### La guía de origen es de antes de tu parche

La guía de Maxroll marca **`Last Updated: 25 de julio de 2026`** — extraído del HTML crudo de la página (`<time dateTime="2026-07-25">`). Tu parche 3.1.3 es del 12/08/2026. **La guía tiene 18 días menos de vida que tu parche**, pero como 3.1.3 no toca clases, sigue vigente.

---

## 1. Qué es esta build en una frase

Tu escudo **es** el arma. Cargas sin parar con **Carga con Escudo (Shield Charge)**; cada impacto **cuenta como un bloqueo**, y cada bloqueo dispara **Represalia (Retribution)**, una nova de daño de **Espinas (Thorns)** físico a tu alrededor. No hay rotación de DPS: hay conducción.

Texto literal del juego **[DATA]**:
> "Retribution Chance: cuando bloqueas, tienes una probabilidad de liberar una nova que inflige [X] de tu daño de Espinas."
> (`heroDetails[1][119].tooltip` en `data.min.json`)

Y la descripción del propio autor **[PLAN]** (campo `globalNotes.intro` del planificador):
> "Esta build usa Shield Charge para infligir daño de Espinas físico mediante impactos directos y Retribution pulsando a tu alrededor cada vez que bloqueas. […] Acumulas Resolve para reducir el daño recibido y aumentar el que haces mediante el Juramento Juggernaut, Mantle of the Grey y Sentinel."

**Fuerzas y debilidades**, literales del planificador **[PLAN]** (`strAndWeak`):
- Fuerzas: *"Zoomy zommy"* (va rapidísimo), *"golpea a los enemigos con un escudo"*.
- Debilidades: **alcance corto**, **exige buen posicionamiento**.

Para un principiante que quiere daño alto sin rotaciones imposibles, encaja: **una tecla principal, y la habilidad de verdad es colocarte**.

---

## 2. Barra de habilidades

Los seis huecos, con el identificador interno y el ID numérico **[PLAN]** (campo `metadata` + `skillBar`):

| Hueco | Habilidad (ES) | Nombre EN | ID interno | Papel |
|---|---|---|---|---|
| 1 | Choque | **Clash** | `Paladin_Punish` (2097465) | Genera Fe, da Marcha del Cruzado |
| 2 | **Carga con Escudo** | **Shield Charge** | `Paladin_ShieldCharge_Channel_Short` (2466077) | **Todo el daño** |
| 3 | Aura de Desafío | **Defiance Aura** | `Paladin_Defensive_Aura` (2187578) | Armadura, resistencias, Resolve, Imparable |
| 4 | Condena | **Condemn** | `Paladin_Condemn` (2226109) | Agrupa, Vulnerable, Debilitar |
| 5 | Aura de Fanatismo | **Fanaticism Aura** | `Paladin_Offensive_Aura` (2187741) | Vel. ataque, prob. crítico, Debilitar |
| 6 | Fortaleza | **Fortress** | `Paladin_Fortress` (2301078) | Inmunidad 3 s + bombazo de daño |

### Qué hace cada una, con el texto real del juego **[DATA]**

**Carga con Escudo** — `Paladin_ShieldCharge_Channel_Short`
> "Cargas con tu escudo y empujas a los enemigos hacia atrás, otorgando [0,6 × Tabla(37,sLevel) × 100]% de Armadura e infligiendo [daño] mientras canalizas."
> Coste: Fe variable, "más 1 adicional por segundo".

**Choque (Clash)** — `Paladin_Punish`
> "Golpeas a un enemigo con tu arma y escudo […]. Golpear enemigos con Clash te otorga **Marcha del Cruzado (Crusader's March)**, aumentando tu Probabilidad de Bloqueo en [0,3 × (1 + 25% si tienes el nodo) × 100]% durante [X] segundos."
> Genera Fe: **20** (30 con la mejora *Damage Bonus*).

⚠️ Ojo al detalle operativo, del propio autor **[PLAN]**: *"Asegúrate de mantener el buff activo usando esta habilidad **al menos una vez cada 6 segundos**."*

**Aura de Desafío (Defiance Aura)** — `Paladin_Defensive_Aura`
> "Pasiva: tu presencia os refuerza a ti y a tus aliados, otorgando [X]% de Armadura y [X]% de bonificación a Todas las Resistencias. **Activa: te vuelves Imparable durante 2 segundos.**"
> Buff en 3.1.0: *"Defiance Aura: Armadura y Resistencias adicionales aumentadas del 30% al 50%"* — [notas 3.1.0](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) **[WEB]**

**Aura de Fanatismo (Fanaticism Aura)** — `Paladin_Offensive_Aura`
> "Pasiva: gastar Fe emana poder, otorgándoos a ti y a tus aliados [X]% de Velocidad de Ataque y [X]% de Probabilidad de Golpe Crítico durante 3 segundos, hasta un máximo de **4 veces (5 con la mejora)**. Activa: Debilita a todos los enemigos cercanos durante 4 segundos."

**Condena (Condemn)** — `Paladin_Condemn`
> "Aprovechas la Luz y atraes a los enemigos tras [1,5] segundos, Aturdiéndolos brevemente e infligiendo [daño]. Mientras lanzas Condemn, te vuelves **Sin Obstáculos (Unhindered)**."

**Fortaleza (Fortress)** — `Paladin_Fortress`
> "Te plantas, volviéndote **Inmune** durante [3] segundos y creando un área defensiva a tu alrededor durante [8 + 2,5 × (rango−1)] segundos. Estar dentro de tu Fortress os otorga a ti y a tus aliados **Resolve cada 0,5 segundos**."
> Recarga base: **60 segundos**.

---

## 3. Árbol de habilidades, punto a punto

**83 puntos** en total **[PLAN]**. El planificador asume además **14 puntos de habilidad y 42 de Paragón procedentes de Renombre (Renown)** — campo `world: {renownSkills: 14, renownParagon: 42}`. **Esto lo heredas de la cuenta**: si ya tenías el Renombre hecho con el nigromante, tu paladín nuevo arranca con ellos.

> **El árbol es IDÉNTICO en arranque, intermedia y endgame.** Lo verifiqué comparando los tres perfiles nodo a nodo: cero diferencias. **Buena noticia para ti: pones el árbol una vez y no lo tocas más.** Solo la variante "Push" (empuje de Pozo alto) cambia.

### Rangos de habilidad

| Habilidad | Puntos | Nota |
|---|---|---|
| Carga con Escudo | **15/15** | máximo |
| Aura de Desafío | **15/15** | máximo |
| Aura de Fanatismo | **15/15** | máximo |
| Fortaleza | **15/15** | máximo |
| Choque (Clash) | **4/15** | solo 4 |
| Condena | **1/15** | solo 1 |

### Nodos de mejora, con su texto real **[DATA]**

**Carga con Escudo** (los tres, imprescindibles):
| Mejora | Efecto literal |
|---|---|
| **Hit Count As Blocking** | "Los impactos de Shield Charge cuentan como Bloqueos." ← **el corazón de la build** |
| **Relentless Charge** | "Shield Charge se convierte en habilidad **Core**. Ahora cuesta **20 de Fe** al lanzar y **1 de Fe adicional por segundo**." |
| **Damage Bonus** | "El daño de Shield Charge aumenta un **10%[x]** al golpear a un enemigo durante 6 s, hasta **30%[x]**." |

**Choque (Clash)**:
| Mejora | Efecto literal |
|---|---|
| **Punishment** | "Estás envalentonado durante Crusader's March: **+30% Probabilidad de Represalia** (×1,25 si tienes Hit Count As Blocking), **+Espinas**, …" |
| **Resolve** | "Golpear a un enemigo con Clash otorga **2 acumulaciones de Resolve**." |
| **Crusader's March Effectiveness** | "Aumenta el efecto de Crusader's March un **25%[x]**." |

**Aura de Desafío**:
| Mejora | Efecto literal |
|---|---|
| **Rite of Might** | "Aumenta tu daño un [X]%[x] durante 4 s **cada vez que ganas Resolve**." |
| **Maximum Life** | "La pasiva otorga además **+15% Vida Máxima** a ti y aliados." |
| **Bonus Healing** | "Otorga **+25% Sanación recibida** a ti y aliados." |

**Aura de Fanatismo**:
| Mejora | Efecto literal |
|---|---|
| **Rite of Vengeance** | "La pasiva aumenta el **Daño de Golpe Crítico** [X]%[x] para ti y tus aliados." |
| **Extra Passive Stack** | "La pasiva acumula **1 vez adicional**" (4 → 5) |
| **Resource Generation** | "Aumenta la Generación de Recurso un **25%** para ti y aliados." |

**Fortaleza**:
| Mejora | Efecto literal |
|---|---|
| **Resolve Damage Bonus** | "Dentro de tu Fortress ganas **4,0%[x] de daño por cada acumulación de Resolve**." ← con 30 de Resolve esto es enorme |
| **Rampart of Thorns** | "Los enemigos dentro de Fortress son Ralentizados un **50%** y reciben **500% de tu daño de Espinas por segundo**." |
| **Unstoppable** | "Dentro de tu Fortress eres **Imparable**." |

**Condena**:
| Mejora | Efecto literal |
|---|---|
| **Gather the Guilty** | "Condemn tiene **1 carga adicional** y aplica **Vulnerable** durante 4 s." |
| **Weaken** | "Condemn aplica **Debilitar** durante 4 s." |
| **Size Increase** | "El tamaño de Condemn aumenta un **50%**." |

### Variante "Push" (solo si empujas Pozo alto)
Suelta **las 6 mejoras de las dos Auras** y mete esos 6 puntos en **Choque 4/15 → 10/15**. Sigue siendo 83 puntos. **No lo hagas de entrada** — el autor no explica por qué, y para ti las auras valen más.

---

## 4. Juramento (Oath): **Juggernaut**

**Los cuatro perfiles usan Juggernaut** — ID `2261363`, confirmado por partida doble: campo `metadata.oath` y campo `oath` de cada perfil **[PLAN]**.

Texto real **[DATA]** (`Paladin_Oath_Juggernaut`):
> "Lanzar una habilidad **Juggernaut** consume **8 acumulaciones de Resolve**, otorgando a tus habilidades Juggernaut **+80%[x] de daño** y **+20% de tamaño** durante 5 segundos. Tu Resolve **Mínimo** aumenta en **1** y **ya no se consume al recibir golpes**."

Los otros tres Juramentos existen y **no son para esta build**: **Zealot** (`2273665`), **Judicator** (`2264962`), **Angel/Arbiter** (`2229208`).

---

## 5. Resolve: el número que gobierna la build

El autor es explícito **[PLAN]** (nota del widget de equipo, idéntica en los cuatro perfiles):

> "Alcanza el **tope de Resolve de 30** templando **'+4 Máximas Acumulaciones de Resolve'** en Casco, Pecho y Pantalones. **Este temple necesita crítico y crítico de Masterwork para llegar a +6.** Tu Resolve máximo base es **8** y necesitas **3× temples de +6**, el **Aspecto del Yunque de Glynn** y el set **Phoba of Righteous Will** para llegar a exactamente **30** de Resolve máximo."

La aritmética cuadra exactamente:

| Fuente | Resolve máximo |
|---|---|
| Base | **8** |
| 3 × temple "+6 Máx. Resolve" (casco, pecho, pantalones) | **+18** |
| Aspecto del Yunque de Glynn | **+2** |
| Set Cathan's Righteous Will (3 piezas) | **+2** |
| **TOTAL** | **30** |

Y por qué importa: **Fortress → Resolve Damage Bonus da 4,0%[x] por acumulación**. Con 30 → daño multiplicativo masivo mientras estás en la Fortaleza. Además el Juramento consume 8 por lanzamiento para el +80%[x].

**En el arranque no llegas a 30.** El perfil Starter lleva temples de **+3** (no +6, porque no está masterworkeado) y solo 2 piezas del set → ronda **19-21**. Es normal; sube con el masterworking.

---

## 6. Aspectos por hueco — los tres presupuestos

Todos los aspectos con su **texto literal del juego [DATA]** y el valor exacto que el planificador tiene puesto **[PLAN]**.

| Hueco | ARRANQUE | INTERMEDIA | ENDGAME |
|---|---|---|---|
| **Casco** | Yunque de Glynn (+4) | Yunque de Glynn (+4) | Yunque de Glynn (+4) |
| **Pecho** | **de lo Indomable** (45) | *(único: Mantle of the Grey)* | *(único: Mantle of the Grey)* |
| **Escudo** | **de Castigo** (75) | *(único: Herald of Zakarum)* | *(único: Herald of Zakarum)* |
| **Arma (Mayal)** | **Aplastante** (0,65) | Aplastante (0,65) | Aplastante (0,65) |
| **Guantes** | **de Canalización** (70) | de Canalización (70) | de Canalización (70) |
| **Pantalones** | **de Guardias Superpuestas** (0,4) | *(único: Tibault's Will)* | *(único: Tibault's Will)* |
| **Botas** | **Sticker-thought** (4.578) | Sticker-thought (6.100) | Sticker-thought (6.100) |
| **Anillo 1** | **del Pacto del Juggernaut** (1) | del Pacto del Juggernaut (1) | del Pacto del Juggernaut (1) |
| **Anillo 2** | **de Fuerza Redirigida** (0,6) | de Fuerza Redirigida (0,6) | de Fuerza Redirigida (0,6) |
| **Amuleto** | **de la Escritura de Lapa** (975) | de la Escritura de Lapa (1.188) | de la Escritura de Lapa (1.188) |

### Texto real de cada aspecto **[DATA]**

| Aspecto (EN) | Efecto literal |
|---|---|
| **Aspect of Glynn's Anvil** | "Tu Resolve máximo aumenta en **2** y ganas **[4]% de Reducción de Daño por Resolve**, hasta **[40]%**." |
| **Aspect of the Indomitable** | "Ganas Armadura y Reducción de Impedimentos igual al **[45]% de tu Probabilidad de Bloqueo**." |
| **Aspect of Chastisement** | "Tus habilidades **Juggernaut** infligen **[75]%[x]** más daño a **Jefes y enemigos con Control de Masas**." |
| **Crushing Aspect** | "Mientras estás **Fortificado**, infliges **[65]%[x]** más daño." |
| **Aspect of Channeling** | "Mientras **canalizas** una habilidad, todo el daño aumenta un **[70]%[x]**." ← Shield Charge canaliza |
| **Aspect of Layered Wards** | "Tu Reducción de Daño Bloqueado aumenta un **[40]%+**." |
| **Sticker-thought Aspect** | "Ganas **[X] Espinas** mientras Canalizas y durante **3 segundos** después." |
| **Aspect of the Juggernaut's Covenant** | "Consumir acumulaciones de Resolve con el Juramento Juggernaut otorga **[100]%[x] de daño adicional**." |
| **Aspect of Redirected Force** | "Ganas Daño de Golpe Crítico igual al **[60]%[x] de tu Probabilidad de Bloqueo**. **Bloquear duplica esta bonificación durante 10 segundos.**" |
| **Aspect of Lapa's Scripture** | "**Perder Resolve** te otorga **[X] Espinas** durante 10 s. Acumula hasta **20 veces**." |

**Nota de coherencia interna:** el motor de la build es Espinas + Bloqueo, y los diez aspectos apuntan a eso (Espinas, Bloqueo→Armadura, Bloqueo→Crítico, Canalización→daño, Resolve→daño). No hay ningún aspecto de relleno.

### Dónde se consiguen los aspectos
Los Aspectos Legendarios de Paladín **no están en el Códice de Poder por mazmorra**: son **caídas aleatorias en objetos legendarios**, que luego **extraes en el Herrero** para guardarlos en el **Códice de Poder** y después **imprimes en el Ocultista** — [EXT] (extracto de buscador sobre *Aspect of Glynn's Anvil*; no abrí la ficha).

**Atajo barato que sí merece la pena:** apostar en el **Purveyor of Curiosities** con **Óbolos**, eligiendo **la pieza cuyo tipo de aspecto quieres**. Los **pantalones cuestan 40 Óbolos y solo pueden llevar aspectos defensivos**, lo que estrecha muchísimo la lotería para *Yunque de Glynn*; y **botas** para *Sticker-thought* — **[EXT]**, ambos de extracto de buscador. ⚠️ **Verifica el coste en Óbolos en pantalla antes de vaciar el monedero.**

---

## 7. Objetos únicos y Míticos — **la pregunta que hiciste**

### Los tres únicos que definen la build

| Objeto | Hueco | Efecto literal **[DATA]** | Dónde cae |
|---|---|---|---|
| **Mantle of the Grey** | Pecho | "El Juramento Juggernaut hace tus habilidades Juggernaut **25% más grandes** pero **consume hasta 16 de Resolve**, otorgando **[6]%[x] de daño de habilidad Juggernaut por cada punto consumido**." | **Duriel** — [icy-veins](https://www.icy-veins.com/d4/news/diablo-4-paladin-unique-items-boss-drop-locations/) **[WEB]** |
| **Herald of Zakarum** | Escudo | "Ganas **[50]% más de Fuerza, Resistencia, Armadura y Probabilidad de Represalia**. Represalia gana **50%[+] de Tamaño**." + implícitos: **+40% Bloqueo**, **Indestructible** | **Andariel** y **Harbinger of Hatred** — [icy-veins](https://www.icy-veins.com/d4/news/diablo-4-paladin-unique-items-boss-drop-locations/) **[WEB]** |
| **Tibault's Will** | Pantalones | "Infliges **[20]%[x] más daño** y ganas **50 de Regeneración de Recurso Primario** mientras eres **Imparable** y durante 5 s después." | ⚠️ **Ya NO cae de un jefe concreto**: está en el **fondo general de únicos** desde S13; cualquier Lair Boss puede soltarlo. La vía fiable es el **Cubo Horadrico → "Upgrade to Unique" sobre pantalones**, que fuerza el hueco — **[EXT]** |

**Por qué Tibault's Will es tan bueno aquí y no es obvio:** tú eres **Imparable prácticamente todo el rato** — te lo dan *Fortress → Unstoppable*, la activa de *Defiance Aura* (2 s) y *Condemn* (Unhindered). Ese 20%[x] está casi siempre encendido.

**Y por qué el pecho es la pieza número uno:** *Mantle of the Grey* consume **hasta 16 de Resolve** y te paga **6%[x] por punto**. A 16 puntos consumidos son **~96%[x]**. Es, con diferencia, el mayor multiplicador de la build, y por eso encabeza la lista de crafteo mítico.

### El único-encanto (charm)

| **Griswold's Opus** | Encanto | "Infligir daño directo otorga **2%[x] de Daño de Golpe Crítico por cada enemigo golpeado** en 10 s, hasta **[150]%[x]**. Al máximo ganas: Golpe de Suerte: los Golpes Críticos tienen probabilidad de…" | **Duriel** y **Harbinger of Hatred** — [icy-veins](https://www.icy-veins.com/d4/news/diablo-4-paladin-unique-items-boss-drop-locations/) **[WEB]** |
|---|---|---|---|

Está en **arranque, intermedia y endgame** — es de los primeros objetivos, no un lujo.

### 🔴 MÍTICOS: el orden exacto y la regla que casi nadie cuenta

Orden literal del autor **[PLAN]** (nota `equipment`, idéntica en los cuatro perfiles):

> **"ORDEN DE CRAFTEO MÍTICO**
> **Solo puedes equipar UN objeto Mítico que hayas crafteado mediante el Cubo Horadrico, pero sí puedes equipar todos los Míticos conseguidos por otras vías.**
> 1. Mantle of the Grey
> 2. Tibault's Will
> 3. Herald of Zakarum"

**Esa regla es la respuesta a tu pregunta.** No craftees a lo loco: **el crafteo solo te da un Mítico equipable**. Los que **caigan** del suelo son ilimitados.

→ **Craftea el pecho (Mantle of the Grey) y solo el pecho.** Los otros dos, a esperar que caigan.

**La receta del Cubo [EXT]** (extractos de buscador, sitios comerciales — ⚠️ **verifica en el Cubo antes de gastar**):
- Requiere **1 Único de 850+ del hueco que quieres** + **4 Fragmentos de Pandemónium**.
- El coste **bajó de 5 a 4 fragmentos en el parche 3.1.1**.
- Devuelve **un Mítico aleatorio utilizable por tu clase, del mismo hueco**.

Ese "mismo hueco" **sí está confirmado en fuente oficial** — notas 3.1.0: *"La receta Upgrade to Mythic del Cubo Horadrico ahora siempre crea un objeto para el mismo hueco de equipo."* — [news.blizzard.com](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) **[WEB]**

**Fragmentos de Pandemónium**: de **Pandemonium Ruptures** (fuente principal), del jefe **Corrupted Reaper**, del tablero de reputación de temporada y de **Resplendent Caches** — **[EXT]**.

⚠️ **Aviso honesto:** la receta devuelve un mítico **aleatorio del hueco**, no *Mantle of the Grey* garantizado. El "orden de crafteo" es un orden de **prioridad de hueco**, no una compra dirigida.

### Mítico solo para la variante Push

**Blood-Mad Idol** (amuleto): *"Siempre estás en Frenesí (Berserking) pero recibes 200%[x] más daño como Quemadura durante 8 s. Mientras te Quemas, Frenesí otorga [195]%[x] más daño."* **[DATA]** — el autor lo marca *"solo para la variante Push"*. **No es para ti todavía.**

---

## 8. Runas y palabras rúnicas

Las runas van en **objetos con 2 engarces** y **solo puedes llevar 2 palabras rúnicas por personaje** — [maxroll runewords](https://maxroll.gg/d4/resources/runewords-overview) **[WEB]** (página fechada 16/07/2026).

Una palabra rúnica = **Runa de Ritual** (la condición) + **Runa de Invocación** (el efecto).

**Las runas exactas de esta build [PLAN]**, resueltas contra el fichero de datos **[DATA]** (los identificadores internos `Rune_Condition_*` / `Rune_Effect_*` corresponden a `ConditionRune` / `EffectRune` en `items`):

| Presupuesto | Pieza | Ritual | Invocación | Palabra |
|---|---|---|---|---|
| **Arranque** | Pecho | **Cir** | **Ceh** | CirCeh |
| **Arranque** | Pantalones | **Moni** | **Kry** | MoniKry |
| **Intermedia / Endgame / Push** | Pecho | **Moni** | **Yom** | **MoniYom** |
| **Intermedia / Endgame / Push** | Pantalones | **Igni** | **Kry** | **IgniKry** |

**Qué hace cada runa** — [maxroll runewords](https://maxroll.gg/d4/resources/runewords-overview) **[WEB]**, corroborado en [d4guides.gg](https://d4guides.gg/en/database/runes) **[WEB]**:

| Runa | Tipo | Ofrenda | Efecto |
|---|---|---|---|
| **Moni** | Ritual | 100 | "Lanza **2 habilidades de Movilidad o Macabras**." ← Shield Charge es movilidad: se alimenta sola |
| **Igni** | Ritual | 25 | "Almacena ofrenda cada 0,3 s. Lanza una habilidad no Básica para ganar la ofrenda almacenada." |
| **Cir** | Ritual | 300 | "Lanza 5 habilidades y quedas exhausto 3 segundos." |
| **Yom** | Invocación | **500** | "Invoca **Petrificar del Druida**, Aturdiendo enemigos y aumentando tu Daño de Golpe Crítico contra ellos." |
| **Kry** | Invocación | **300** | "Invoca **Vórtice del Espiritista**, infligiendo daño y **atrayendo enemigos**." |
| **Ceh** | Invocación | **100** | "Invoca un **Lobo Espiritual** que ataca durante 8 segundos." |

**Por qué esta combinación y no otra:** *Kry* (Vórtice) **agrupa** — y esta build vive de golpear a muchos a la vez con la carga. *Yom* (Petrificar) **aturde y sube crítico**. *Moni* se carga sola porque tu habilidad principal **es** una habilidad de movilidad. Es una máquina de automantenerse.

⚠️ El autor tiene puesta la opción `Power_Rune_Effect_Druid_Petrify: {active: true}` en el planificador **[PLAN]**, es decir, **los números mostrados asumen Yom activa**.

**Si te está matando algo**, el propio autor dice **[PLAN]** (FAQ): *"Sustituye la runa ofensiva por **Mot**, **Que** o **Lac**."*

---

## 9. Talismán, encantos (charms) y sello

### El sello
- **Arranque / Intermedia / Endgame:** **Legendary Horadric Seal** → **5 huecos de encanto**.
- **Push:** **Seal of the Diamond Mind** (Mítico) → **6 huecos**.

Rarezas y huecos — [maxroll talisman](https://maxroll.gg/d4/resources/talisman-charms-sets) **[WEB]** (fechada 28/06/2026):
| Rareza del sello | Huecos |
|---|---|
| Mágico | 3 |
| Raro | 4 |
| **Legendario** | **5** |
| Mítico Único | **6** |

El sello del planificador lleva además el afijo **"of Glory: +1 Hueco de Encanto"** **[PLAN]** — o sea que en la práctica llegan a 6.

### Los encantos, perfil por perfil **[PLAN]**

| | Arranque | Intermedia / **Endgame** | Push |
|---|---|---|---|
| 1 | Phoba *of Righteous Will* | Phoba *of Righteous Will* | Phoba *of Righteous Will* |
| 2 | **Fer *of Iron Conviction*** | Phoba *of Righteous Will* | **Berú *of Iron Conviction*** |
| 3 | Mlor *of Righteous Will* | Mlor *of Righteous Will* | Mlor *of Righteous Will* |
| 4 | Phoba *of Righteous Will* | Phoba *of Righteous Will* | Phoba *of Righteous Will* |
| 5 | **Berú *of Iron Conviction*** | Linta *of Righteous Will* | Linta *of Righteous Will* |
| 6 | **Griswold's Opus** | **Griswold's Opus** | **Fer *of Iron Conviction*** |

### ⚠️ El detalle que cambia la lectura: los duplicados NO cuentan

Fíjate en el endgame: lleva **Phoba tres veces**. Eso son **5 encantos del set pero solo 3 piezas distintas** (Phoba, Mlor, Linta).

**Los duplicados no acumulan bonificación de set** — **[EXT]** (extracto de buscador: *"las bonificaciones de set son equipables únicas; dos encantos con la misma bonificación (2) no se duplican"*).

**Y eso encaja perfectamente con la aritmética del propio autor:** él dice que el set aporta **+2 de Resolve máximo**, que es exactamente la bonificación de **3 piezas**, no la de 5. **→ El endgame corre la bonificación de 3 piezas de Cathan's Righteous Will.** Los Phoba repetidos están ahí por sus **afijos individuales**, no por el set.

### Bonificaciones de set, texto real **[DATA]**

**Cathan's Righteous Will** (`Talisman_Pala_01`):
| Piezas | Efecto |
|---|---|
| **2** | "Los enemigos se acobardan ante ti, quedando **Aterrados e Inmovilizados 0,5 s** la primera vez que te ven o cuando los Bloqueas." |
| **3** ← *la que corre esta build* | "Reflejas efectos de Aturdimiento y Empuje. Tu **Resolve Mínimo +2 y Máximo +2**, y ganas **10%[+] de Reducción de Daño por cada punto de Resolve Mínimo**." |
| **5** | "Cuando intentas aplicar Control de Masas a un enemigo digno que no puede recibirlo, te creces: **+500%[x] de daño durante 10 segundos**." |

**Cathan's Iron Conviction** (`Talisman_Pala_05`) — la del arranque y la del Push:
| Piezas | Efecto |
|---|---|
| **2** ← *la que corre* | "Ganas **55% de Potencia de Aura**." |
| **3** | "Ganas [X]% de Reducción de Daño. **Tus habilidades de Aura ganan todas sus Mejoras.** Las activas de Aura ya no cuestan Fe…" |
| **5** | "Ganas Aura de Convicción: los enemigos cercanos reciben **0,5%[x] más daño por cada rango de habilidad** que tengas en todas tus Auras." |

> 💡 **Pista fuerte para más adelante:** la de **3 piezas de Iron Conviction** regala **todas las mejoras de las Auras**. Eso libera **6 puntos del árbol** — y es exactamente lo que hace la variante Push (suelta las 6 mejoras de Aura y las mete en Choque). ⚠️ Esto lo deduzco yo de la coincidencia numérica; **el autor no lo explica**. Trátalo como hipótesis, no como hecho.

### Cómo se consiguen los encantos
- Los sets se completan con RNG normal de endgame **[EXT]**.
- **Truco del Cubo Horadrico:** la receta **3-a-1** combina 3 objetos del mismo tipo en uno nuevo, y existe una receta **"Reroll Set Charm"** que **convierte un encanto de set en otro del mismo set** — [maxroll talisman](https://maxroll.gg/d4/resources/talisman-charms-sets) **[WEB]**. **Si te llueven Phobas, conviértelos en Mlor y Linta.**
- Los **sellos Míticos Únicos** solo salen "en los niveles más altos de dificultad Tormento" — [maxroll talisman](https://maxroll.gg/d4/resources/talisman-charms-sets) **[WEB]**.

---

## 10. Mercenarios — y por qué **en dúo cambia todo**

**Configuración del planificador, idéntica en los cuatro perfiles [PLAN]:**

| Papel | Mercenario | Habilidades elegidas |
|---|---|---|
| **Contratado (Hired)** | **Raheir** (`MercenaryClass_ShieldBearer`) | Ground Slam, **Bastion**, **Inspiration**, **Raheir's Aegis** |
| **Refuerzo (Reinforcement)** | **Aldkin** (`MercenaryClass_CursedChild`) | Wither (`Mercenary_CursedChild_Wither`) |

Los cuatro nodos de Raheir, con texto real **[DATA]**:
| Nodo | Efecto |
|---|---|
| **Bastion** | "Raheir toma posición protectora 5 s, **redirigiendo hacia sí el 90% del daño** que recibirían los aliados cercanos." |
| **Inspiration** | "Los enemigos afectados por Ground Slam reciben **15%[x] más daño**. Los aliados afectados por Bastion infligen **25%[x] más daño**." |
| **Raheir's Aegis** | "Raheir te otorga **15% de Resistencia a Todos los Elementos**." |
| **Ground Slam** | "Daño físico masivo y **Ralentiza 30%** (60% en el centro)." |

Resumen del autor **[PLAN]**: *"Raheir te otorga Bastion e Inspiration para potenciar tu daño. Aldkin reduce el daño enemigo y ralentiza con Field of Languish."*

### 🔴 En dúo pierdes a Raheir. Y con él, un 25%[x] de daño.

Confirmado **[EXT]** (extracto de buscador, coincidente en varias fuentes):
> "Los Mercenarios **Contratados pasan a reserva cuando te unes a un grupo**, mientras que los **Refuerzos alistados sí pueden invocarse** aunque juegues con otros. Los Mercenarios primarios **no aparecen en grupo**."

**Traducción para tus tardes con tu pareja:**
- **En solitario:** Raheir contratado + Aldkin de refuerzo. Build completa.
- **En dúo:** **Raheir desaparece.** Solo te queda **Aldkin** (refuerzo). Pierdes **Inspiration (+25%[x] daño)**, **Bastion (90% de redirección de daño)** y **+15% de resistencias**.

**Consecuencia práctica, y es importante:** en dúo **pegas y aguantas notablemente menos** que en solitario con el mismo equipo. **No es que lo estés haciendo mal.** Si notas el bajón al jugar con ella, es esto.

**Compensación:** tus dos Auras (**Desafío** y **Fanatismo**) **benefician a los aliados** — el texto del juego dice literalmente *"a ti y a tus aliados"* en Armadura, Resistencias, Vida Máxima, Velocidad de Ataque, Prob. de Crítico, Daño de Crítico y Generación de Recurso. **Tu pareja nigromante recibe todo eso.** En dúo tú pierdes daño individual pero el conjunto gana bastante: eres el ancla del grupo.

---

## 11. Paragón: tableros y glifos

**5 tableros, en este orden exacto [PLAN]**, con el glifo asignado a cada uno:

| # | Tablero | Nodo Legendario | Glifo | Rotación / Posición |
|---|---|---|---|---|
| 0 | `Paragon_Paladin_00` — **Start** | (inicial) | **Revenge** (`Rare_033_Intelligence_Side`) | rot 0, (0,0) |
| 1 | `Paragon_Paladin_06` — **Relentless** | **Relentless** | **Outmatch** (`Rare_049_Strength_Main`) | rot 2, (0,−1) |
| 2 | `Paragon_Paladin_09` — **Beacon** | **Beacon** | **Honed** (`Rare_104_Dexterity_Side`) | rot 1, (1,−1) |
| 3 | `Paragon_Paladin_01` — **Castle** | **Castle** | **Spirit** (`Rare_050_Willpower_Side`) | rot 1, (−1,−1) |
| 4 | `Paragon_Paladin_02` — **Shield Bearer** | **Shield Bearer** | **Sentinel** (`Rare_103_Strength_Main`) | rot 0, (−1,0) |

### Orden de subida de glifos **[PLAN]** (literal: *"Glyph Leveling Priorities"*)
1. **Sentinel** · 2. **Spirit** · 3. **Honed** · 4. **Outmatch** · 5. **Revenge**

**Sentinel es el número uno** y encaja con la intro del autor (*"aumentas el daño mediante el Juramento Juggernaut, Mantle of the Grey y **Sentinel**"*). Sus afijos **[DATA]**: `DamageWithJuggernautSkills_Strength_Main` (**daño con habilidades Juggernaut**) + `MultDmgToClose_Legendary` (**daño a enemigos cercanos**). Para una build que carga contra los enemigos y usa habilidades Juggernaut, es exactamente el glifo correcto.

⚠️ **Cuidado con el nombre "Spirit":** hay **tres glifos distintos llamados Spirit** en los datos. El que usa esta build es **`Rare_050_Willpower_Side`** (afijos: `SpiritCritDamage_Willpower_Side` + `MultCritDmgPercent_Legendary`). **Si coges el de Destreza te equivocas.**

Igual con **Outmatch** (tres variantes) → usa **`Rare_049_Strength_Main`**, y **Revenge** (tres) → **`Rare_033_Intelligence_Side`**.

### Progresión en tres pasos **[PLAN]**
El planificador guarda tres estados con **glifos a nivel 1 → 50 → 100**, y el número de nodos activados sube con ellos:

| Tablero | Nodos a glifo 1 | a glifo 50 | a glifo 100 |
|---|---|---|---|
| Start | 27 | 31 | 39 |
| Relentless | 60 | 60 | 60 |
| Beacon | 37 | 52 | 60 |
| Castle | 46 | 54 | 54 |
| Shield Bearer | 28 | 53 | — |

**Lectura práctica:** completa **Relentless** primero (ya está lleno desde el principio), y deja **Beacon** y **Shield Bearer** para cuando los glifos suban.

**Nodos raros notables activados [DATA]:** Relentless, Defiance, Cull, Dervish, Endure (tablero 1) · Beacon, Champion, Sturdy, **Spiked Shield**, Fortitude (tablero 2) · Castle, Ironclad, Stalwart, Knight (tablero 3) · Shield Bearer, Knight, Constrict (tablero 4) · Brawn, Iron Strength, Raw Power, Tenacity (Start).

---

## 12. Estadísticas objetivo

### ⚠️ Aquí tengo que ser honesto contigo

**El planificador NO contiene cifras objetivo de velocidad de ataque, crítico, vida, armadura ni resistencias.** Lo comprobé: el campo `pinnedStats` solo tiene `{Shield Charge: ["Damage"], Fortress: ["Cooldown"]}`. **No hay una tabla de "apunta a X% de crítico".**

Lo que **sí** hay, y es literal:

| Estadística | Objetivo | Fuente |
|---|---|---|
| **Resolve máximo** | **exactamente 30** | **[PLAN]** nota de equipo |
| **Prob. de Bloqueo** | *"hasta 100%"* alcanzable | **[PLAN]** FAQ |
| **Prob. de Crítico** | Fanaticism Aura da **14% a 15 rangos** | **[PLAN]** FAQ |
| **Bloqueo por Aegis** | **42% a rango 15** | **[PLAN]** FAQ |
| **Defensas** | *"Céntrate en **Armadura** y **Vida Máxima**"* | **[PLAN]** nota de equipo |
| **Masterworking** | **25** (máximo) + Capstone | [icy-veins](https://www.icy-veins.com/d4/guides/masterworking-guide/) **[WEB]** |

**Prioridad de multiplicadores**, literal del autor **[PLAN]**:
> "El valor del multiplicador de **Daño de Golpe Crítico** sube cuanto más **Probabilidad de Golpe Crítico** consigas. **Si tienes muy poca Probabilidad de Golpe Crítico, los multiplicadores de Daño Físico, Daño a Vulnerables o Daño General valen más.**"

**Traducción para el arranque:** al principio, con poco crítico, **prioriza Daño Físico / a Vulnerables / General** sobre Daño de Crítico. Cuando el crítico suba, invierte el orden.

**Cómo tapar el crítico** **[PLAN]** (FAQ literal): Aura de Fanatismo → Afijos de encantos y sello → Temples de arma → **enfocar el Masterworking en Probabilidad de Golpe Crítico**.

**Cómo tapar el Bloqueo** **[PLAN]** (FAQ literal): Aegis → tablero **Castle** → tablero **Shield Bearer** → **Aspect of Interdiction** (*"puede dar hasta 100% con suficiente Resolve máximo"*) → **Bulwark's Aspect**.

⚠️ *Aegis*, *Aspect of Interdiction* y *Bulwark's Aspect* **no están en esta build**; el FAQ es común a varias guías de Paladín. Anótalos como alternativas, no como piezas de este montaje.

### Temples exactos del planificador **[PLAN]**

| Pieza | Temple | Arranque | Endgame |
|---|---|---|---|
| Casco | Máx. Acumulaciones de Resolve | **+3** | **+6** |
| Pecho | Máx. Acumulaciones de Resolve | **+3** | **+6** |
| Pantalones | Máx. Acumulaciones de Resolve | **+3** | **+6** |
| Escudo | Prob. de Golpe Crítico | **+5%** | **+10%** |
| Arma | Prob. de Golpe Crítico | **+5%** | **+10%** |
| Guantes | Daño Físico | **+40%** | **+50%** |
| Botas | Potencia de Aura (Defiance) | **+10%** | **+20%** |
| Anillos / Amuleto | Reducción de Recarga | **+6%** | **+7,5%** |

### Gemas **[PLAN]**
| Pieza | Arranque | Endgame |
|---|---|---|
| Casco | 2× **Rubí** (`Gem_Ruby_05`) | 2× Rubí (`_07`) |
| Escudo | Rubí | Rubí |
| Arma | **Calavera** (`Gem_Skull`) | Calavera |
| Anillo 1 | **Topacio** | Topacio |
| Anillo 2 | — | Rubí |
| Amuleto | **Diamante** | Diamante |

(Rubí = Vida, Calavera = Espinas/Robo, Topacio y Diamante = resistencias/utilidad. ⚠️ La correspondencia gema→estadística **no la verifiqué por escrito**; el planificador solo da el identificador.)

---

## 13. La rotación real

⚠️ **El campo `rotations` del planificador está VACÍO** (`[]` en los cuatro perfiles). **No existe una rotación oficial escrita.** Lo que sigue lo reconstruyo **solo** con reglas explícitas del autor y textos del juego — no invento prioridades.

**Reglas duras, todas citadas:**

1. **Choque (Clash) al menos una vez cada 6 segundos.** — literal **[PLAN]**: *"Asegúrate de mantener el buff activo usando esta habilidad al menos una vez cada 6 segundos."* Te da Marcha del Cruzado (+Bloqueo, +Prob. Represalia, +Espinas) y **2 de Resolve por golpe**, además de la Fe.
2. **Carga con Escudo en canalización continua.** Es tu botón de daño **y** de movimiento. Cuesta 20 de Fe + 1/segundo.
3. **Condena para agrupar.** — literal **[PLAN]**: *"ayuda a agrupar enemigos y aporta Unhindered, Vulnerable y Weaken."*
4. **Fortaleza contra jefes y apuros.** Inmune 3 s + **4%[x] de daño por Resolve** dentro. Recarga 60 s.
5. **Las dos Auras van siempre puestas** (son pasivas); sus **activas** son botones aparte: Desafío → **Imparable 2 s**; Fanatismo → **Debilitar en área**.

**Secuencia que se deduce de esas reglas, sin añadir nada:**

> **Al entrar a un paquete:** Condena (agrupa + Vulnerable + Debilitar) → Choque (buff + Fe) → **Carga con Escudo sin soltar**, atravesando el grupo por el centro.
> **Cada ~6 s:** un Choque para refrescar Marcha del Cruzado.
> **Contra jefe o élite peligrosa:** Fortaleza encima del objetivo, y cargar dentro del área.
> **Si te enganchan:** activa Aura de Desafío (Imparable).

**La única "habilidad mecánica" real de la build**, literal del autor **[PLAN]**:
> "**Maximiza la cantidad de enemigos que golpeas** con Shield Charge posicionándote adecuadamente para disparar **Hit Count As Blocking** tan a menudo como sea posible."

**Es decir: no cargues por el borde del grupo. Atraviésalo por el centro.** Más enemigos tocados = más "bloqueos" = más novas de Espinas. Eso es todo el pilotaje.

---

## 14. 🎯 LOS TRES PRESUPUESTOS, con el objeto que abre cada salto

### 🥉 ARRANQUE — nivel 70 recién llegado, **cero únicos de equipo**

**Qué llevas:** legendarios genéricos (Runic Skullcap, Runic Mail, Bone Shield, Spiked Flail, Runic Gloves, Runic Leggings, Runic Cleats, 2× Soulwatch Hoop, Ocelot's Eye) con los **10 aspectos** de la tabla del §6 imprimidos. Poder de objeto **850**, **masterworking 0** **[PLAN]**.

**El único "único" es un encanto:** **Griswold's Opus**.

**Resolve alcanzado:** ~19-21 (temples de +3, set a 2 piezas).

**Qué hacer, en orden:**
1. **Imprime los 10 aspectos.** Consíguelos gastando **Óbolos en el Purveyor of Curiosities** por tipo de pieza (pantalones → aspectos defensivos, 40 Óbolos **[EXT]**), extráelos en el **Herrero** y estámpalos en el **Ocultista**.
2. **Templa "+Máx. Acumulaciones de Resolve" en casco, pecho y pantalones.** Es lo que más daño te da por el 4%[x]/Resolve de Fortaleza.
3. **Consigue un Sello Legendario** (5 huecos) y mete lo que tengas del set.
4. **Farmea Griswold's Opus** — **Duriel** o **Harbinger of Hatred** **[WEB]**.

> ### 🔓 EL OBJETO QUE ABRE EL SALTO A INTERMEDIA
> ## **Mantle of the Grey** (pecho) — cae de **DURIEL**
> Es el mayor multiplicador de la build: **hasta ~96%[x]** (6%[x] × 16 de Resolve consumido).
> **Ruta:** Duriel es un jefe invocable. Farmea sus materiales de invocación y repítelo.
> **Ruta alternativa garantizada de hueco:** Cubo Horadrico → *Upgrade to Mythic* sobre un **pecho** único 850+ (4 Fragmentos de Pandemónium **[EXT]**) — pero devuelve un mítico **aleatorio del hueco**, no este en concreto.
> **Bonus:** Duriel suelta **también Griswold's Opus**. Un solo jefe, dos objetivos.

---

### 🥈 INTERMEDIA — con los aspectos y los únicos clave

**Cambios frente al arranque [PLAN]:**

| Hueco | Antes | Ahora | Ganas |
|---|---|---|---|
| **Pecho** | Aspecto de lo Indomable | **Mantle of the Grey** | hasta **~96%[x]** |
| **Escudo** | Aspecto de Castigo | **Herald of Zakarum** | **+50%** Fuerza/Resist./Armadura/Prob. Represalia, **+40% Bloqueo**, Indestructible |
| **Pantalones** | Aspecto de Guardias Superpuestas | **Tibault's Will** | **+20%[x]** casi permanente |
| Poder de objeto | 850 | **900** | |
| **Masterworking** | **0** | **25** | **+25% a todos los afijos** |
| Temples de Resolve | +3 | **+6** | |
| Gemas | `_05` | `_07` | |
| Palabras rúnicas | CirCeh / MoniKry | **MoniYom / IgniKry** | |
| Set de encantos | 2 pz RW + 2 pz IC | **3 pz Righteous Will** | +2/+2 Resolve, DR |

**Ahora sí llegas a Resolve 30.**

**Qué hacer, en orden:**
1. **Masterworking a 25 en todo.** Es el multiplicador más barato y seguro que tienes: **+25% a todos los afijos y estadísticas base**, más un **Capstone** que sube un afijo aleatorio **+50%** — [icy-veins](https://www.icy-veins.com/d4/guides/masterworking-guide/) **[WEB]**. **Enfoca los crits de Masterwork en Prob. de Golpe Crítico** **[PLAN]**.
2. **Re-templa Resolve a +6** (requiere crítico de temple **y** crítico de Masterwork **[PLAN]**).
3. **Andariel / Harbinger of Hatred** para el escudo.
4. **Cubo Horadrico sobre pantalones** para Tibault's Will.
5. **Convierte encantos duplicados** con la receta del Cubo hasta tener **Phoba + Mlor + Linta** distintos.
6. Sube **Yom** y **Kry** (500 y 300 de Ofrenda).

> ### 🔓 EL OBJETO QUE ABRE EL SALTO A ENDGAME
> ## **El Mítico crafteado — y solo UNO**
> Recuerda la regla literal **[PLAN]**: *"Solo puedes equipar UN objeto Mítico que hayas crafteado mediante el Cubo Horadrico, pero sí puedes equipar todos los Míticos conseguidos por otras vías."*
> **→ Gasta tu único crafteo en el PECHO (Mantle of the Grey).** Es el primero de la lista del autor y el mayor multiplicador.
> **Dónde se farmean los Fragmentos de Pandemónium** **[EXT]**: **Pandemonium Ruptures** (fuente principal), jefe **Corrupted Reaper**, tablero de reputación de temporada, **Resplendent Caches**.
> ⚠️ Coste (**4 fragmentos**, bajado de 5 en 3.1.1) viene de extracto de buscador. **Míralo en el Cubo antes de gastar.**

---

### 🥇 ENDGAME — equipo optimizado

**Diferencias respecto a intermedia [PLAN]:** son **sutiles**. Mismo árbol, mismos aspectos, mismos únicos, mismas runas, mismo Paragón. Lo que cambia:

- **Afijo extra "of Steel" en TODAS las piezas** (valor 0,125) — un afijo más por hueco.
- Valores de afijo más altos en todo (ej. *of the Powerful* 99 → **151,25**; *of Vigor* 1.225 → **1.812,5**; Espinas 915,79 → **1.907,90**).
- **Glifos a nivel 100** (frente a 1 y 50 en los pasos previos).
- Más nodos de Paragón activados (Start 27→39, Beacon 37→60, Shield Bearer 28→53).
- **5 encantos** del set (3 distintos) + Griswold's Opus.

**Es decir: el endgame no es otra build, es la misma afinada.** No hay un objeto milagroso al final — hay **glifos a 100 y afijos mayores (Greater Affixes)**.

**Qué hacer, en orden:**
1. **Glifos a 100.** Orden: **Sentinel → Spirit → Honed → Outmatch → Revenge** **[PLAN]**.
2. **Caza Afijos Mayores (Greater Affixes)** en las piezas clave.
3. Persigue **Herald of Zakarum** y **Tibault's Will** míticos **por caída** (no crafteados — la regla del único crafteo).
4. Completa el **Capstone** de Masterworking en cada pieza.

**Solo si empujas Pozo alto (variante Push):** Sello **Seal of the Diamond Mind** (6 huecos), amuleto **Blood-Mad Idol**, botas con **Exploiter's Aspect** (en vez de Sticker-thought), y el árbol reconfigurado (Choque 10/15, sin mejoras de Aura).

---

## 15. Resumen para tus próximas 4 semanas

Queda ~1 mes de temporada. Prioriza así:

| Prioridad | Acción | Por qué |
|---|---|---|
| **1** | Imprimir los **10 aspectos** | La build no funciona sin ellos; son lo más barato |
| **2** | Templar **Resolve** en casco/pecho/pantalones | Escala el 4%[x]/Resolve de Fortaleza |
| **3** | **Duriel** → Mantle of the Grey **+ Griswold's Opus** | Un jefe, los dos mayores multiplicadores |
| **4** | **Masterworking 25** en todo | +25% a todo, sin RNG de caída |
| **5** | **Andariel / Harbinger** → Herald of Zakarum | Bloqueo y Represalia |
| **6** | Glifo **Sentinel** a tope | El glifo de daño de la build |
| **7** | Cubo sobre **pantalones** → Tibault's Will | 20%[x] casi permanente |

**No hagas esto:** no gastes el crafteo mítico en nada que no sea el **pecho**; no cojas el glifo *Spirit* de Destreza; no cargues por el borde de los grupos.

---

## Fuentes

**Abiertas y leídas de verdad:**

1. https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide — guía de origen. **Fechada `2026-07-25`** (extraído del HTML: `<time dateTime="2026-07-25">`). Abierta dos veces vía WebFetch **y** descargada en crudo con `curl` (HTTP 200, 477.022 bytes). ⚠️ **NO devolvió 403 esta vez**, contra lo esperado. El detalle del build **no está en el HTML**: vive en el planificador incrustado.
2. https://maxroll.gg/d4/planner/19imlp0x — el planificador de esta build (enlace extraído del HTML de la guía).
3. https://planners.maxroll.gg/profiles/d4/19imlp0x — **JSON crudo del planificador** (HTTP 200, 167.015 bytes). Contiene los 4 perfiles, equipo, árbol, Paragón y las notas del autor. **Fuente primaria de todo lo marcado [PLAN].**
4. https://assets-ng.maxroll.gg/d4-tools/game/data.min.json — **fichero de datos del juego** (HTTP 200, **11.606.292 bytes**). **Datamining declarado.** Campo `version` = **`3.1.0.72698`**. Fuente de todo lo marcado [DATA].
5. https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes — notas oficiales. Sirvió **3.1.0 (30/06/2026)**, con los cambios de Paladín y la regla del Cubo Horadrico.
6. https://www.icy-veins.com/d4/news/diablo-4-3-1-3-patch-notes-easier-season-objectives-and-echo-of-mephisto-portal-fix/ — **3.1.3 (12/08/2026)**. Confirma: **cero cambios de clase y cero cambios de objeto**.
7. https://www.icy-veins.com/d4/news/diablo-4-paladin-unique-items-boss-drop-locations/ — jefes que sueltan cada único de Paladín. ⚠️ **La página no muestra fecha.**
8. https://maxroll.gg/d4/resources/runewords-overview — runas y palabras rúnicas. **Fechada 16/07/2026.**
9. https://d4guides.gg/en/database/runes — base de datos de runas (corrobora Yom/Kry/Ceh).
10. https://maxroll.gg/d4/resources/talisman-charms-sets — sistema de talismán, sellos y recetas del Cubo. **Fechada 28/06/2026.**
11. https://www.icy-veins.com/d4/guides/masterworking-guide/ — Masterworking máx. 25 + Capstone. ⚠️ **La página dice "Updated December 2025 (Season 14)", fecha internamente incoherente** (S14 empezó en junio de 2026). Uso solo el dato de rango máximo, que corrobora el `upgrade: 25` del planificador.

**Abiertas y fallidas (lo digo porque el hueco importa):**

12. https://www.wowhead.com/diablo-4/guide/classes/paladin/shield-charge-build-overview — **abierta, sin contenido útil**: solo cabecera y normas de comentarios. Marca `2026/03/08`, que es **anterior al lanzamiento del Paladín (parche 3.0, 28/04/2026)** → sería contenido de **pre-lanzamiento / PTR**. **No he usado nada de ella.**
13. https://mobalytics.gg/diablo-4/builds/paladin-shield-charge-endgame-build-guide — **HTTP 403 Forbidden**. No leída.

**Extractos de buscador (NO páginas abiertas) — todo lo marcado [EXT]:**
- Fuentes de caída de *Tibault's Will* en S14 (fondo general de únicos + método del Cubo).
- Coste de la receta *Upgrade to Mythic* (4 Fragmentos de Pandemónium) y fuentes de los fragmentos.
- Regla de que los encantos duplicados no acumulan bonificación de set.
- Adquisición de aspectos por apuesta de Óbolos en el Purveyor.
- Regla de mercenarios Contratado vs Refuerzo en grupo.
- Cifras de *Relentless Charge* citadas por terceros (157% daño, 10%/s Represalia hasta 50%) — **NO las he incorporado**: contradicen parcialmente el texto del cliente y venían de una wiki vetada.

**Vetadas y no usadas:** fextralife, primagames, beebom, gamespot, segmentnext, studioloot, gamerguides, pcgamesn, mythicdrop. Aparecieron en resultados de búsqueda; **no he tomado ni un número de ellas**.

---

## No encontrado

Lo que **no** pude verificar por escrito. Prefiero el hueco al número con buena pinta.

1. **Notas de los parches 3.1.1 y 3.1.2 completas.** El fichero de datos es 3.1.0 y las notas que abrí son 3.1.0 y 3.1.3. **Hay una ventana de dos revisiones (julio 2026) que no he leído.** Sé por extracto que **3.1.1 bajó el coste del Cubo de 5 a 4 fragmentos** y que hubo un **3.1.1a (16-17/07/2026)** que subió la tasa de Míticos, pero **no leí el texto íntegro**. ⚠️ **Si algo de esta guía falla, es el candidato número uno.**
2. **Cifras objetivo de velocidad de ataque, prob. de crítico, vida, armadura y resistencias.** **No existen en la guía ni en el planificador.** El único número duro es **Resolve = 30**. Los demás objetivos numéricos que circulan por ahí **no los he podido anclar**.
3. **El daño real de la build** (DPS, nivel de Pozo alcanzable, comparativa con otras builds). **No hay ni una cifra de rendimiento en ninguna fuente que abriera.** No te doy un ranking de daño porque no lo he visto escrito.
4. **Los valores numéricos concretos de muchos afijos y aspectos.** Los tooltips del cliente vienen con **fórmulas sin evaluar** (`[0.6*Table(37,sLevel)*100|%+|]`), no con números finales. Donde el planificador guardaba el valor calculado, lo he puesto; donde no, he dejado la fórmula.
5. **Nombres en español de casi todo.** El cliente que dataminé está **en inglés**. Las traducciones de habilidades, aspectos y objetos son **mías**; los nombres entre paréntesis en inglés son los fiables. ⚠️ **En tu cliente en español los nombres pueden diferir.**
6. **Por qué la variante Push suelta las mejoras de Aura.** Mi hipótesis (el 3-piezas de *Iron Conviction* las regala) **encaja numéricamente pero el autor no la confirma**. No la des por buena.
7. **Correspondencia gema → estadística.** El planificador solo da identificadores (`Gem_Ruby_07`); **no verifiqué por escrito** qué otorga cada gema en 3.1.x.
8. **Fecha de la página de únicos de Icy Veins** (§7). No la muestra. Los jefes que indica encajan con el resto, pero **sin fecha no puedo garantizar que sea de 3.1.x**.
9. **Cómo caen exactamente los encantos de set de Paladín.** La página de talismán de Maxroll **no cubre los sets de Paladín**. Solo tengo la receta genérica del Cubo.
10. **Si el "crítico de Masterwork" que lleva el temple de Resolve de +4 a +6 es un mecanismo real y cómo se llama.** El autor lo afirma **[PLAN]**, pero la guía de Masterworking que abrí **no usa esa terminología** (solo describe el Capstone a rango 25). ⚠️ **Contradicción sin resolver entre dos fuentes.**
11. **Confirmación en fuente primaria de la regla "solo un Mítico crafteado equipable".** Solo la tengo de la nota del autor **[PLAN]**. No la vi en notas oficiales. **Es una regla muy importante — confírmala en el Cubo antes de planificar.**
