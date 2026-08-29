# PROGRESIÓN DE EQUIPO — PALADÍN, NIVEL 70 → TORMENTO ALTO

> **Dominio:** orden de gasto de materiales, Afijos Mayores, Temple, Maestría, objetivos defensivos por tier de Tormento, escalera de jefes invocables y tabla actividad→material.
> **Personaje:** Paladín (clase nueva, parche 3.0, 28/04/2026) con build **Shield Charge (Carga con Escudo)**. Principiante. Dúo la mitad del tiempo.
> **Fecha del informe:** 19/08/2026 · **Parche vivo anclado:** 3.1.3, build 73224 (12/08/2026).
> **Tiempo real disponible:** ~4 semanas hasta el fin previsto de la S14.

---

## 0. Advertencia de método (léela antes que la tabla)

Este informe distingue tres calidades de dato y **las marca en la misma línea**, no en un aviso al final:

| Marca | Qué significa |
|---|---|
| **[JUEGO]** | Sale del fichero de datos del juego que sirve el planificador de Maxroll (`assets-ng.maxroll.gg/d4-tools/game/data.min.json`, 11.606.292 bytes, HTTP 200, campo `"version":"3.1.0.72698"`). Es **datamining**: son las cadenas y fórmulas reales del cliente. **Es 3.1.0, no 3.1.3** — tres hotfixes por detrás del parche vivo. |
| **[FECHADO]** | Página abierta de verdad, con fecha visible dentro de 3.1.x. |
| ⚠️ **[CADUCO]** o ⚠️ **[SECUNDARIO]** | Página abierta pero fechada antes de 3.0/3.1, o fuente no preferente. **No la uses para tomar decisiones caras.** |

**Tres cosas que este informe corrige de lo que circula por ahí** (detalladas en §10):
1. La Maestría **ya no tiene golpes en 4/8/12**. Tiene **un solo capstone en calidad 25**. Todo texto que hable de "tres crits" es de 2024-2025.
2. El **Neathiron ya no se obtiene** — el propio tooltip del juego dice que "desapareció misteriosamente". Cualquier coste que lo pida es sospechoso.
3. El famoso **"-25 % de resistencias por cada tier de Tormento"** **no aparece** en los datos del juego 3.1.0. Los tiers de Tormento en 3.1.0 solo modifican XP, oro y tasas de drop. Ver §5.

**Lo que NO pude abrir:** `mobalytics.gg` devolvió **HTTP 403** a la guía de Shield Charge Paladin (era fuente preferente del encargo). `maxroll.gg/d4/resources/horadric-cube-guide` devolvió **404** (la URL buena es sin `-guide`). Reddit está bloqueado a este agente por política del rastreador. **Maxroll sí respondió** en esta sesión (16 páginas abiertas), pero **las tablas de equipo pieza a pieza de sus guías de build viven dentro del planificador interactivo, no en el HTML**, así que la lista slot-por-slot de Shield Charge **no la tengo** y está declarada en «No encontrado».

---

## 1. Veredicto operativo — el orden de gasto en una pantalla

Esto es lo único que hay que memorizar. El resto del informe lo justifica.

| Fase | Dónde estás | Qué SÍ gastas | Qué NO tocas | Por qué |
|---|---|---|---|---|
| **A** | Nivel 70, aún en Penitente | Nada caro. Aspectos del Códice, joyas normales | Obducita, Almas Olvidadas, Chispas, Polvo Primordial | Todavía no caen Ancestrales. Todo lo que crafteas ahora se tira. |
| **B** | Tormento I (Pit 10) | **Temple, y solo temple** | **Obducita** | Maxroll, textual: *"Temper these items instantly, but don't bother with Masterworking yet"* — [FECHADO 09/07/2026] |
| **C** | Tormento II–IV | Temple + reemplazo de piezas. Guarda Obducita | Obducita | En T II se abren los manuales de temple legendarios; en T IV el Neathiron |
| **D** | **Tormento V (Pit 30)** | **AQUÍ empieza la Maestría en serio.** Maxroll: *"Masterwork the rest of your items to 25 Quality and start funneling Masterworking Capstone Bonuses to useful affixes"* — [FECHADO 09/07/2026] | — | **La regla del encargo está CONFIRMADA**, con un matiz importante: ver §2 |
| **E** | Tormento VI–VIII | Míticos: Fragmentos de Pandemónium al Cubo | — | Con el equipo ya estable, el Mítico deja de ser lotería y pasa a ser inversión |
| **F** | Tormento IX–XII | Transfiguración (Polvo Volátil) — **paso irreversible, siempre el último** | — | Transfigurar deja el objeto inmodificable |

**Regla de una línea:** *temple desde el primer minuto de Tormento I; Obducita a partir de Tormento V; Chispas y Fragmentos cuando el equipo ya no se te cae de las manos; Polvo Volátil el último de todos.*

---

## 2. La regla de la Obducita: confirmada, pero no como te la contaron

**El encargo preguntaba si existe una regla documentada de Maxroll de no gastar Obducita hasta Tormento V. Existe.** La guía *Endgame Progression* de Maxroll [FECHADO 09/07/2026] está estructurada por tramos de Tormento y dice, en el tramo de Tormento 1:

> *"Temper these items instantly, but don't bother with Masterworking yet."*
> (*"Templa estos objetos al instante, pero no te molestes todavía con la Maestría"*) — https://maxroll.gg/d4/meta/endgame-progression

y en el tramo de **Tormento 5**:

> *"Masterwork the rest of your items to 25 Quality and start funneling Masterworking Capstone Bonuses to useful affixes."*
> (*"Sube el resto de tus objetos a Calidad 25 y empieza a canalizar los Bonus de Capstone hacia afijos útiles"*) — https://maxroll.gg/d4/meta/endgame-progression

**Los tres matices que cambian cómo se aplica:**

1. **No es "cero Obducita hasta T V". Es "cero Obducita en piezas que vas a tirar".** La misma web, en su guía de progresión, señala aparte que **el arma es la excepción**: *"prioritize weapons first"* / *"Prioritize high-value items like weapons"* — https://maxroll.gg/d4/meta/endgame-progression. Un arma ancestral con buen daño base te dura desde T I hasta el final; una pechera de 850 no.
2. **Hay una contradicción interna en Maxroll y conviene saberla.** La página *Endgame Progression* [09/07/2026] dice "no masterworkees todavía" en T I; pero la misma página, en su resumen de crafteo, dice *"Start quality improvements toward 25 once you have ancestral gear in Torment 1"*. **Las dos frases están en la misma página.** La lectura coherente —y la que coincide con el tramo de T V— es: *empieza por el arma en cuanto tengas un arma ancestral que te vaya a durar; el resto del equipo, en T V.* Esto es **interpretación mía**, no cita.
3. **El motivo económico es medible.** Subir una pieza de 900 de poder a Calidad 25 cuesta entre **492 y 1.366 Obducita** más entre **115 y 275 Almas Olvidadas** y entre **7,25 y 11,25 millones de oro** [FECHADO 29/06/2026 — https://maxroll.gg/d4/resources/item-crafting]. Reventar eso en una pieza que reemplazas en T III es tirar entre media hora y dos horas de farmeo.

---

## 3. La escalera de Tormento, con lo que abre cada tier

**Esta es la tabla más útil del informe para decidir el orden de gasto**, porque cada tier de Tormento **abre un grifo de material distinto**. Sale entera del fichero de datos del juego, campo `worldTiers`. **[JUEGO — v3.1.0.72698]** · https://assets-ng.maxroll.gg/d4-tools/game/data.min.json

| Tier | Desbloqueo (textual del juego) | XP | Oro | **Grifo que abre (textual del juego)** |
|---|---|---|---|---|
| **Tormento I** | *"Unlock Artificer's Tier and Conquer Tier 10"* | +300 % | +100 % | **Aparecen los objetos de calidad Ancestral.** Más Legendarios, Únicos y Míticos por tier |
| **Tormento II** | Pit 15 | +400 % | +120 % | **Manuales de Temple Legendarios** y **Pergaminos de Restauración** caen más a menudo. Más probabilidad de Ancestral por tier |
| **Tormento III** | Pit 20 | +500 % | +140 % | **Set Charms** caen más a menudo |
| **Tormento IV** | Pit 25 | +600 % | +160 % | **Neathiron** cae más a menudo ⚠️ (ver §10.2 — este material está deprecado) |
| **Tormento V** | Pit 30 | +700 % | +180 % | **Runas Legendarias** caen más a menudo |
| **Tormento VI** | Pit 40 | +800 % | +200 % | **Llaves de Guarida Mayores** caen más a menudo |
| **Tormento VII** | Pit 50 | +900 % | +225 % | **Polvo Primordial Volátil** cae más a menudo (= Transfiguración) |
| **Tormento VIII** | Pit 60 | +1000 % | +250 % | **Amuletos (Charms) Únicos** caen más a menudo |
| **Tormento IX** | Pit 70 | +1100 % | +275 % | **Prismas de Sintonía Kullean** caen más a menudo |
| **Tormento X** | Pit 80 | +1200 % | +300 % | **Sellos Horádricos Míticos** caen más a menudo |
| **Tormento XI** | Pit 90 | +1300 % | +300 % | *(el juego describe este tier como "For paragons and fools")* |
| **Tormento XII** | Pit 100 | +1400 % | +300 % | *("For paragons and fools")* |

**Cómo se lee esta tabla para un principiante con 4 semanas:**
- **T I** es la puerta real del juego: sin Ancestrales no hay Afijos Mayores y no hay nada que masterworkear.
- **T II** es más importante de lo que parece: es donde empiezan a caer los **manuales de temple legendarios**, que son los que traen las recetas buenas de Paladín (§6). Sin T II estás templando con manuales de rareza baja.
- **T V** es tu objetivo real de temporada. Es donde Maxroll te deja gastar Obducita y donde caen runas legendarias.
- **T VII** es donde el Polvo Volátil deja de ser una anécdota. Antes de T VII, no planifiques transfiguraciones.
- **T X–XII** están fuera del alcance realista de un personaje nuevo en 4 semanas. No organices tu farmeo alrededor de ellos.

**Lo que esta tabla NO dice** — y es un hueco significativo: **no hay ninguna penalización de armadura ni de resistencias por subir de Tormento** en los datos 3.1.0. El campo `attributes` de cada tier solo contiene dos entradas (`id 1231` = oro, `id 73` = experiencia). Ver §5.

---

## 4. Temple (Tempering) — recetas reales del Paladín

### 4.1 Reglas del sistema

| Dato | Valor | Fuente |
|---|---|---|
| Cargas de temple por objeto | **3** de base, **hasta 7** si el objeto tiene cuatro Afijos Mayores | ⚠️ [CADUCO 23/05/2026] https://maxroll.gg/d4/resources/tempering-guide |
| Coste, legendario 850 | 25 material básico + 10 Cristales Velados | [FECHADO 29/06/2026] https://maxroll.gg/d4/resources/item-crafting |
| Coste, ancestral 900 | **25 Almas Olvidadas por intento** | [FECHADO 29/06/2026] ídem |
| Recuperar una carga | **Pergamino de Restauración** — *"Use to restore 1 Tempering Charge on an item"* | **[JUEGO]** |
| De dónde salen los pergaminos | Ciudadela Oscura, Hordas Infernales, jefes de mundo | ⚠️ [CADUCO 23/05/2026] tempering-guide |
| Cuándo caen más manuales legendarios | **Tormento II en adelante** | **[JUEGO]** `worldTiers` |

**Consecuencia económica que casi nadie calcula:** cada tirada de temple en una pieza ancestral cuesta **25 Almas Olvidadas**. Tres cargas = **75 Almas Olvidadas por pieza**, y si fallas las tres, la pieza queda inservible (*bricked*) salvo que gastes un Pergamino. Con 10 piezas eso son **750 Almas Olvidadas** solo en temple, antes de tocar la Maestría. **Las Almas Olvidadas son tu cuello de botella real en T I–IV, no la Obducita.**

### 4.2 Categorías de manual y en qué ranuras entran

⚠️ [CADUCO 23/05/2026] — https://maxroll.gg/d4/resources/tempering-guide. Cruzado con el campo `temperingGroups` **[JUEGO]**, que coincide.

| Categoría | Ranuras admitidas |
|---|---|
| Weapons (Armas) | Armas y mano secundaria |
| Offensive (Ofensivo) | Amuletos, armas, mano secundaria, anillos, guantes |
| Defensive (Defensivo) | Amuletos, yelmos, pechera, pantalones, escudos |
| Utility (Utilidad) | Amuletos, botas, guantes, yelmos, pechera, pantalones, escudos |
| Mobility (Movilidad) | Amuletos y botas |
| Resource (Recurso) | Anillos y amuletos |

### 4.3 Las nueve recetas que le importan a un Shield Charge Paladin

**Esto es datamining puro y es lo más sólido del informe: son los identificadores internos reales del cliente 3.1.0.** Ningún guía las publica con este nivel de detalle. **[JUEGO — v3.1.0.72698]**

| Manual | Categoría | Opciones que puede darte (tier 3 = manual legendario) |
|---|---|---|
| **Juggernaut Augments** | Weapons | Daño de Clash · Daño de **Shield Bash** · **Daño de Shield Charge** · **Daño de Retribution** |
| **Juggernaut Innovation** | Utility | **Tamaño de Shield Bash** · **Tamaño de Retribution** · Duración de Aegis |
| **Juggernaut Efficiency** | Resource | Recurso tras Clash · Reducción de reutilización de Valor · Reducción de reutilización de Fortress |
| **Paladin Resolve** | Defensive | **Tasa de generación de Resolve** · **Máximo de acumulaciones de Resolve** |
| **Paladin Perseverance** | Defensive | **Probabilidad de bloqueo** · Armadura mientras Arbiter |
| **Paladin Guard** | Defensive | Reducción de reutilización de Aegis · **Probabilidad de bloqueo** |
| **Paladin Recovery** | Defensive | Generación de vida Fortificada · Reducción de reutilización de Consecration |
| **Paladin Motion** | Mobility | Reducción de reutilización de Falling Star · **Reducción de reutilización de Shield Charge** |
| **Guardian Finesse** | Offensive | Daño Disciple · Daño Zealot · Daño mientras Arbiter · Daño de tipo Judgement |

**Los tres manuales que definen la build:** `Juggernaut Augments` (daño de Shield Charge y de Retribution), `Paladin Resolve` (el máximo de acumulaciones, que es la mecánica de la build) y `Paladin Perseverance`/`Paladin Guard` (probabilidad de bloqueo, porque **la build convierte cada bloqueo en una explosión de Espinas** vía Retribution).

⚠️ **Ojo con `Paladin Perseverance` y `Paladin Guard`: los dos pueden dar "Probabilidad de bloqueo".** Si necesitas bloqueo, `Paladin Guard` te da 1 de 2 opciones útiles y `Paladin Perseverance` también 1 de 2 — pero `Perseverance` es el único con `classFilter` marcado a `true` para Paladín en los datos, mientras que `Resolve`, `Guard`, `Recovery` y `Motion` lo tienen todo a `false`. **No sé interpretar esa discrepancia y no la infiero** — está en «No encontrado».

### 4.4 Valores reales de los temples (fórmulas del cliente)

**[JUEGO — v3.1.0.72698]**, campo `attributeFormulas`. Estos son los rangos exactos, no aproximaciones de guía:

| Temple | Fórmula interna | Rango real |
|---|---|---|
| Daño de Shield Charge / Retribution (tier 3) | `TemperedAffix_35%` = `(24,5 + 0,5·RandomInt(1,21))/100` | **+25 % a +35 %** |
| Vida plana (tier 3) | `RandomInt(1000,1500)` | **+1.000 a +1.500 de Vida** |
| Armadura plana (tier 3) | `RandomInt(1250,2000)` | **+1.250 a +2.000 de Armadura** |
| Resistencia a todos los elementos (tier 3) | `RandomInt(60,70)` | **+60 a +70** (unidad interna, no %) |
| Resistencia a un elemento (tier 3) | `RandomInt(440,490)` | **+440 a +490** (unidad interna, no %) |
| Vida plana (tier 2 / manual raro) | `RandomInt(400,500)` | +400 a +500 |
| Armadura plana (tier 2) | `RandomInt(600,900)` | +600 a +900 |

**Esto confirma un punto de modelo, no de cifra, y es importante:** en 3.1.0 **la resistencia es una puntuación plana, no un porcentaje**. Un temple da "+440 a +490 de resistencia", no "+8 %". Toda guía que hable de "llegar al 70 % de resistencias" está describiendo un modelo que el cliente 3.1.0 **ya no usa así**. Ver §5.

---

## 5. Objetivos defensivos: Dureza (Toughness), armadura y resistencias

### 5.1 Qué es la Dureza, con la definición del juego

**[JUEGO]** — tooltip literal de la ficha de personaje:

> *"**Toughness** is an approximation of your survivability for each damage type based on your Life, Armor, Resistances, and other Damage Reduction sources."*
> (*"La **Dureza** es una aproximación de tu supervivencia para cada tipo de daño, basada en tu Vida, Armadura, Resistencias y otras fuentes de Reducción de Daño."*)

Y el tooltip de Armadura, también literal **[JUEGO]**:

> *"Reduces incoming Damage by {s2}. (…) The Damage Reduction from Physical Resistance is capped at {s6}."*

**Dos lecturas duras de ahí:**
1. La Dureza **no es una estadística que se sube**: es un número resumen. No la persigas directamente; sube Vida, Armadura y Resistencias y la Dureza sube sola.
2. **La armadura, en 3.1.x, es literalmente Resistencia Física.** El cap existe pero es una variable de tiempo de ejecución (`{s6}`), **no un número fijo en los datos**. Cualquiera que te dé "el cap de armadura es X" está inventando o citando una versión vieja.

### 5.2 Las fórmulas reales

[FECHADO 16/08/2026] — https://maxroll.gg/d4/getting-started/defenses-for-beginners (es la fuente **más reciente** de todo este informe, tres días antes de la fecha del encargo):

- `DR % por Armadura = Armadura / (Armadura·10/9 + 5678)` — constante **5.678 a nivel 70**
- `DR % por Resistencia = Resistencia / (Resistencia·10/9 + 1136)` — constante **1.136 a nivel 70**
- Ambas *"approach 90 %"* — **tienden a 90 %, sin llegar**

### 5.3 Tabla de objetivos — CALCULADA, no publicada

⚠️ **Esta tabla la he calculado yo despejando la fórmula de Maxroll. NO es una cifra que publique nadie.** La fórmula sí es citada y fechada; los números de abajo son aritmética sobre ella. Los doy porque **no encontré objetivos publicados por tier de Tormento en ninguna fuente preferente** (ver «No encontrado»).

Despeje: `Valor = DR · C / (1 − 10·DR/9)`

| Reducción de daño que quieres | **Armadura** necesaria (C = 5.678) | **Resistencia** necesaria (C = 1.136) |
|---|---|---|
| 40 % | ~4.090 | ~820 |
| 50 % | ~6.390 | ~1.280 |
| 60 % | ~10.220 | ~2.045 |
| 70 % | ~17.890 | ~3.580 |
| 80 % | ~40.880 | ~7.160 |

**Cómo usarlo de verdad:** un solo temple de armadura tier 3 da **+1.250 a +2.000** (§4.4). Es decir, **tres temples de armadura bien puestos te mueven del 40 % al 50 % de reducción física**. Un temple de resistencia a un elemento da **+440 a +490**: en resistencias, **un solo temple mueve la aguja mucho más** porque la constante es cinco veces menor. Para un Paladín de Shield Charge, que ya nada en armadura por la propia habilidad —el tooltip de `Paladin_ShieldCharge_Channel_Short` **[JUEGO]** dice que otorga armadura mientras canalizas—, **el temple de resistencias rinde más por hueco que el de armadura**.

### 5.4 El dato muerto que hay que tirar

⚠️ **"Cada tier de Tormento te resta un 25 % de resistencias y 250 de armadura", "el cap de resistencias es 70 % ampliable a 85 % con Tyrael's Might", "necesitas 13.500 de armadura y 45.000 de vida".** Estas tres frases circulan por todas partes. **Las he buscado y NO las sostiene ninguna fuente preferente fechada dentro de 3.1.x.** Peor: el campo `worldTiers` del cliente 3.1.0 **[JUEGO]** contiene, para cada uno de los doce Tormentos, **exactamente dos atributos**: multiplicador de oro (`id 1231`) y multiplicador de experiencia (`id 73`). **Ninguna penalización defensiva.** Los buscadores devuelven esas cifras desde páginas de la era *Vessel of Hatred* (Season 6, 2024-2025) sin fecha visible. **Trátalas como muertas hasta que las veas en tu pantalla.**

---

## 6. Afijos Mayores (Greater Affixes)

### 6.1 Lo que está confirmado

| Dato | Fuente |
|---|---|
| Los Ancestrales de **900 de poder** son los que traen *"a chance of Greater Affixes"*; cerca de nivel 70 los monstruos *"always drop item power 850 loot"* | [FECHADO 25/07/2026] https://maxroll.gg/d4/resources/equipment |
| El poder del objeto determina el **rango** de los afijos, no solo su cantidad | [FECHADO 25/07/2026] ídem |
| Desde 3.1.0, **todos los Únicos traen 2 afijos garantizados al caer** | [FECHADO 30/06/2026] https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes |
| Desde 3.1.0, los afijos añadidos por Encantamiento, Transfiguración y Temple **salen siempre al valor máximo cuando se añaden a un Mítico** | [FECHADO 30/06/2026] ídem |
| Existe un material, **Polvo Primordial Resonante**, cuya única función es *"upgrade a random affix into a Greater Affix"* en el Cubo Horádrico | **[JUEGO]** tooltip literal |
| La **Transfiguración** tiene ~15 % de probabilidad de resultado *"Upgrade to Greater Affix"*; la receta **3-a-1** y el **Reroll Set Charm** (~4 % por afijo) también pueden producirlos | [FECHADO 16/07/2026] https://maxroll.gg/d4/resources/horadric-cube |
| El **Prisma Entrópico** garantiza un resultado útil de Transfiguración **a cambio de eliminar la posibilidad de Afijo Mayor** | [FECHADO 16/07/2026] ídem |

### 6.2 Cuántos buscar por pieza — **respuesta honesta: no lo sé con fuente fechada**

La cifra que circula ("un legendario ancestral hasta 3, un Único hasta 4, un Mítico exactamente 1, ×1,5 al valor máximo") aparece en los extractos de buscador, **pero las páginas que la sostienen son fextralife (vetada por el encargo) y agregadores sin fecha**. La página de Maxroll que debería tenerlo (`item-crafting`, `equipment`) **no la publica en su HTML**. **No la doy por buena.** Está en «No encontrado».

**Lo que sí puedo darte como criterio operativo sin inventar cifras:**
- Un Afijo Mayor **solo aparece al caer el objeto**. No se fabrica con temple ni con encantamiento. La única vía de fabricación documentada es el **Polvo Primordial Resonante** en el Cubo **[JUEGO]** y la Transfiguración a ~15 % [FECHADO 16/07/2026].
- Por tanto, **en T I–IV no filtres por Afijos Mayores**: filtra por *pieza ancestral con el afijo correcto*. Perseguir Afijos Mayores con 4 semanas y un personaje nuevo es perseguir lotería.
- **A partir de T V**, cuando ya masterworkeas, un Afijo Mayor en el afijo que te importa **sí justifica reemplazar una pieza masterworkeada**, porque el Afijo Mayor y el capstone de Maestría **se suman** [⚠️ CADUCO 23/05/2026, masterworking-guide: *"stacks with Greater Affix bonuses"*].

---

## 7. Maestría (Masterworking): rangos, costes y el capstone

### 7.1 El sistema en 3.1.x

| Dato | Valor | Fuente |
|---|---|---|
| Rango de calidad | **0 a 25** | ⚠️ [CADUCO 23/05/2026, decl. parche 2.5.0] https://maxroll.gg/d4/resources/masterworking-guide · corroborado [⚠️ SECUNDARIO 30/07/2026, decl. 3.1.0–3.1.2] https://timesaver.gg/blog/diablo-4-masterworking-guide-season-14 |
| Efecto por rango | **+1 %** acumulativo al daño base, armadura, resistencia y **valor de los afijos**. Máximo **+25 %** en rango 25 | ⚠️ [CADUCO] masterworking-guide |
| **Capstone** | **Uno solo, en calidad 25**: **+50 % a un afijo aleatorio** | ⚠️ [CADUCO] masterworking-guide; corroborado [⚠️ SECUNDARIO] timesaver |
| **Golpes en 4/8/12** | **NO EXISTEN en 3.1.x.** Textual de la fuente secundaria: *"There are no intermediate critical ranks at specific thresholds (4, 8, 12)"* | [⚠️ SECUNDARIO 30/07/2026] timesaver |
| Rangos por intento | Cada mejora puede dar **hasta 5 rangos de golpe** — de ahí la horquilla mejor/peor caso | [⚠️ SECUNDARIO 30/07/2026] timesaver |

**Este es el punto donde más gente va con datos muertos.** El sistema de tres "crits" en los rangos 4, 8 y 12 fue el de 2024–2025. En 3.1.x **hay un único premio, al final, y es aleatorio entre tus afijos**.

### 7.2 Costes exactos

**Fórmula de Obducita por rango** [⚠️ CADUCO 23/05/2026 masterworking-guide, republicada en [⚠️ SECUNDARIO 30/07/2026] timesaver como *"community-derived from in-game data, verified by Maxroll.gg"*]:

```
Obducita = floor( 3,75 × CalidadActual + 10 )
```

Es decir: **10 de Obducita** en calidad 0 → **100 de Obducita** en calidad 24. **Las armas a dos manos cuestan el doble en todos los rangos.**

**Coste total de una pieza, de 0 a 25 + capstone** [FECHADO 29/06/2026] https://maxroll.gg/d4/resources/item-crafting:

| Objeto | Caso | Obducita | Segundo material | Oro |
|---|---|---|---|---|
| 850 de poder | Peor | **1.366** | 150 Sigilos Abstrusos | **11.250.000** |
| 850 de poder | Mejor | **492** | 70 Sigilos Abstrusos | **7.250.000** |
| **900 ancestral** | Peor | **1.366** | **275 Almas Olvidadas** | **11.250.000** |
| **900 ancestral** | Mejor | **492** | **115 Almas Olvidadas** | **7.250.000** |

**Recolocar el capstone (rerroll)** [FECHADO 29/06/2026, ídem]:

| Objeto | Coste |
|---|---|
| 850 de poder | **100 Obducita + 10.000.000 de oro** |
| 900 ancestral | **200 Obducita + 1 Neathiron + 10.000.000 de oro** ⚠️ **ver §10.2 — el Neathiron está deprecado en 3.1.0** |
| Armas a dos manos | **El doble** |

**Lo que esto significa para tus 4 semanas:** equipar 10 piezas ancestrales a Calidad 25 cuesta, en el mejor de los casos, **~4.920 de Obducita, ~1.150 Almas Olvidadas y ~72,5 millones de oro**; en el peor, **~13.660 de Obducita, ~2.750 Almas Olvidadas y ~112,5 millones**. **No vas a hacer eso en cuatro semanas siendo principiante.** Elige **cuatro piezas** —arma, escudo, y las dos que lleven el afijo que la build necesita al máximo— y deja el resto en calidad baja.

### 7.3 El "Masterwork crit" y el número +6 de Resolve

La guía de Maxroll de Shield Charge dice, **textualmente** [FECHADO 25/07/2026] https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide:

> *"Reach the Resolve cap of 30 by tempering '+4 Maximum Resolve Stacks' on Helm, Chest and Pants. This temper needs to crit and be Masterwork crit to go to +6. Your basline maximum Resolve is 8 and you need 3x +6 Maximum Resolve Tempers, Aspect of Glynn's Anvil and the Phoba of Righteous Will set to reach exactly 30 Maximum Resolve."*

**Comprobación aritmética (derivación mía, no cita):** el capstone de Maestría es **+50 % a un afijo aleatorio** (§7.1). `+4 × 1,5 = +6`. **Encaja exacto.** Es decir, lo que la comunidad llama *"Masterwork crit"* es **el capstone de calidad 25 cayendo sobre ese afijo concreto**. Y el desglose de Maxroll cuadra: `8 base + 6 + 6 + 6 = 26`, más lo que aporten `Aspect of Glynn's Anvil` y el set `Phoba of Righteous Will` hasta **30**.

**Consecuencia práctica, y es la más importante del informe para tu build:**
> Yelmo, pechera y pantalones **tienen que llegar a Calidad 25 y el capstone tiene que caer en el temple de Resolve**. Si cae en otro afijo, **pagas 100–200 de Obducita + 10 millones de oro por cada intento de recolocarlo**, por pieza. Son **tres piezas**. Presupuesta eso como el gasto de Obducita más grande de tu temporada y **no masterworkees nada más hasta tenerlo**.

Y el corolario incómodo: **el cap de Resolve 30 es un objetivo de final de temporada, no de la semana 2.** Con 4 semanas, apunta a **dos de las tres piezas** y asume que juegas por debajo del cap.

---

## 8. Míticos y Chispas Resplandecientes: las tres economías

En S14 hay **tres vías distintas** para conseguir un Mítico, y **cuestan monedas diferentes**. Confundirlas es el error caro.

### 8.1 Las tres vías

| Vía | Coste | Qué obtienes | Fuente |
|---|---|---|---|
| **Cubo Horádrico — "Upgrade to Mythic"** | **1 Único de 850+ de poder + 4 Fragmentos de Pandemónium** | Un Mítico **de la misma ranura** que el Único que metiste, aleatorio | Coste 4: [FECHADO 14/07/2026] https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes — *"Reduced the cost of the Upgrade to Mythic recipe on the Horadric Cube from 5 to 4 Pandemonium Fragments"* |
| **Herrero — Caché de Mítico Icónico** | **2 Chispas Resplandecientes + 50.000.000 de oro** | Un **Mítico Icónico** aleatorio (Shako, Grandfather, Starless Skies…) | [⚠️ SECUNDARIO 26/07/2026] https://conquestcapped.com/guides/diablo-4/mythic-unique-crafting/ |
| **Joyero — Rune Crafting** | **3 Chispas Resplandecientes + 5.000.000 de oro + 3 runas nombradas (×3 de cada)** | Un Mítico **de la ranura que elijas** | [⚠️ SECUNDARIO 26/07/2026] ídem. El uso del Joyero con Chispas está confirmado por el tooltip del juego **[JUEGO]**; **las cantidades no** |

⚠️ **Contradicción detectada y sin resolver:** la página del Cubo de Maxroll [FECHADO 16/07/2026] sigue publicando *"1x Unique Item, 5x Pandemonium Fragment"*. Las notas de Blizzard del **14/07/2026** ya lo habían bajado a **4**. **Maxroll está dos días y un hotfix por detrás en esa cifra.** Fíate de Blizzard: **son 4**.

### 8.2 La regla que cambia toda la planificación

Cita **textual** de la guía de Shield Charge de Maxroll [FECHADO 25/07/2026]:

> *"You can only equip one Mythic item that you have crafted through the Horadric Cube, but you are able to equip all Mythics that are acquired elsewhere."*
> (*"Solo puedes equipar **un** objeto Mítico que hayas crafteado en el Cubo Horádrico, pero puedes equipar **todos** los Míticos que consigas por otras vías."*)

**Traducción operativa:** los Míticos que te **caigan** son gratis y sin límite. **El crafteado del Cubo es UNO y solo uno.** Por tanto, gastar 4 Fragmentos de Pandemónium en un segundo Mítico crafteado es tirar el material salvo que vayas a desequipar el primero.

### 8.3 El orden de crafteo de Maxroll para Shield Charge

Cita **textual** [FECHADO 25/07/2026]:

- **Variante Endgame:** *"1. Mantle of the Grey 2. Tibault's Will 3. Herald of Zakarum"*
- **Variante Push:** *"1. Mantle of the Grey 2. Blood-Mad Idol (only for Push variant) 3. Tibault's Will 4. Herald of Zakarum"*

⚠️ **Aquí hay un problema de interpretación que declaro abierto en vez de resolverlo.** El datamining **[JUEGO]** confirma que los tres son **Únicos normales (`magicType: 2`), NO Míticos**:

| Objeto | Clave interna | `magicType` | Ranura | Clase |
|---|---|---|---|---|
| Mantle of the Grey | `Chest_Unique_Paladin_001` | **2 (Único)** | Pechera | Solo Paladín |
| Tibault's Will | `Pants_Unique_Generic_102` | **2 (Único)** | Pantalones | Todas |
| Herald of Zakarum | `1HShield_Unique_Paladin_004` | **2 (Único)** | Escudo | Solo Paladín |
| Blood-Mad Idol | `Amulet_Unique_Generic_102` | **2 (Único)** | Amuleto | Todas |

Y la receta del Cubo *"now always creates an item for the same gear slot"* [FECHADO 30/06/2026, Blizzard] con los afijos **completamente aleatorizados** [FECHADO 16/07/2026, Maxroll]. **La lectura que más encaja** es que la lista de Maxroll indica **en qué ranura gastar los Fragmentos**, nombrada por el Único que esperas obtener en versión Mítica — es decir: *mete un Único de pechera al Cubo y reza por que salga Mantle of the Grey mítico*. Una fuente secundaria [⚠️ SECUNDARIO, mmogah/nexttier vía extractos de buscador] describe exactamente ese modelo: *"You will receive a random Mythic Unique from the same equipment slot as the Unique item you used"*, distinguiendo el "pool nuevo" (Únicos ascendidos) del pool de "Míticos Icónicos" clásicos del Herrero. **No lo confirmo con fuente preferente. Va a «No encontrado».**

### 8.4 Míticos que el Paladín puede llevar — lista completa del cliente

**[JUEGO — v3.1.0.72698]**, filtrando `magicType: 4` (Mítico) por el índice de clase del Paladín (posición 6 del `classFilter`):

| Mítico | Ranura | ¿Paladín? |
|---|---|---|
| Harlequin Crest | Yelmo | **Sí** |
| Andariel's Visage | Yelmo | **Sí** |
| Heir of Perdition | Yelmo | **Sí** |
| The Cow King's Crown | Yelmo | **Sí** |
| Tyrael's Might | Pechera | **Sí** |
| Shroud of False Death | Pechera | **Sí** |
| Melted Heart of Selig | Amuleto | **Sí** |
| Ring of Starless Skies | Anillo | **Sí** |
| Doombringer | Espada 1M | **Sí** |
| **El'Druin, Sword of Justice** | Espada 1M | **Sí** |
| The Grandfather | Espada 2M | **Sí** |
| **The Empyrean Eye** | **Gema mítica** | **Sí** |
| Ahavarion, Spear of Lycander | Bastón | **No** |
| Nesekem, the Herald | Glaive | **No** |
| Shattered Vow | Alabarda | **No** |

**Notas que importan:**
- **El'Druin, Sword of Justice** es la espada del propio Tyrael y **fue añadida a la Caché de Mítico del Herrero en el parche 3.1.1** [FECHADO 14/07/2026] https://www.icy-veins.com/d4/news/diablo-4-season-14-patch-notes-increased-mythic-and-pandemonium-fragment-drop-rates/. Es Mítico de espada a una mano y **el Paladín puede llevarla**. Para una build de escudo, es el candidato natural de arma.
- **The Empyrean Eye** es un **Mítico de tipo Gema** (`Gem_Mythic_01`). Es el único Mítico que no ocupa ranura de equipo. **No lo he visto mencionado en ninguna guía de Paladín.**
- **The Grandfather** es de dos manos: **incompatible con Shield Charge**, que necesita escudo. Descártalo pese a su fama.
- Para un **Shield Charge** que vive del bloqueo y las Espinas, los Míticos defensivos —**Tyrael's Might, Shroud of False Death, Melted Heart of Selig**— encajan mejor con la mecánica que los ofensivos puros. **Esto es criterio mío, no está en ninguna fuente.**

### 8.5 De dónde salen las Chispas y los Fragmentos

| Material | Cómo se obtiene | Fuente |
|---|---|---|
| **Chispa Resplandeciente** | *"Collected from Salvaging a Mythic Unique at the Blacksmith"* — es decir: **desguazando un Mítico** | **[JUEGO]** tooltip literal |
| Chispa Resplandeciente | ⚠️ Receta estacional del Cubo: **7 Fragmentos de Pandemónium → 1 Chispa** | [⚠️ SECUNDARIO, extracto de buscador nexttier.pro] — **no confirmado en fuente preferente** |
| **Fragmento de Pandemónium** | **Corrupted Reaper: hasta 2 por muerte, escalando con el Tormento** | [FECHADO 14/07/2026] Blizzard, parche 3.1.1 |
| Fragmento de Pandemónium | **La recompensa repetible "Glints of Hope" del tablero de reputación garantiza 1** | [FECHADO 14/07/2026] Blizzard, 3.1.1 |
| Fragmento de Pandemónium | Sellar Ruptures, Cachés Resplandecientes | [⚠️ SECUNDARIO 26/07/2026] conquestcapped |

**Cuenta de la vieja para tus 4 semanas:** un Mítico crafteado en el Cubo = **4 Fragmentos**. El Corrupted Reaper da **hasta 2** por muerte. Es decir, **entre 2 y 4 runs del Reaper por Mítico crafteado**, y solo puedes **equipar uno**. **Tu objetivo realista de temporada es UN Mítico crafteado**, en la ranura donde más te falte.

---

## 9. La escalera de jefes invocables

### 9.1 Los tres escalones y sus llaves

**Mecánica clave que casi todo el mundo entiende al revés y que el cliente confirma:** la llave **no invoca al jefe**. La llave **abre el Alijo (Hoard)** que aparece **después** de matarlo. Tooltip literal **[JUEGO]**: *"Used to open a Lair Boss Hoard."* Puedes matar al jefe sin llave; simplemente no cobras.

**Tabla completa, con las cadenas de conversión reales del cliente [JUEGO — v3.1.0.72698]** cruzadas con ubicaciones y botín de Paladín de [⚠️ SECUNDARIO 18/07/2026] https://conquestcapped.com/guides/diablo-4/diablo-4-bosses-guide/:

#### Escalón 1 — Llave de Guarida (Lair Key)

| Jefe | Ubicación | Material que sueltan los mobs → conversión en el Alquimista | Únicos de Paladín |
|---|---|---|---|
| **Echo of Varshan** | Malignant Burrow, Hawezar | *Trembling Hand* / *Gurgling Head* / *Blackened Femur* → **Malignant Heart** → **Lair Key** | Seal of the Second Trumpet, Wreath of Auric Laurel |
| **Grigoire** | Hall of the Penitent, Dry Steppes | **Living Steel** → Lair Key | Bastion of Sir Matthias, Sunbrand |
| **Beast in the Ice** | Glacial Fissure, cerca de Kyovashad | **Distilled Fear** → Lair Key | Light's Rebuke, Sanctis of Kethamar |
| **Lord Zir** | Ancient's Seat, Darkened Way | **Exquisite Blood** → Lair Key | Judgment of Auriel, Judicant's Glaivehelm |
| **Urivar** | Fields of Judgement, Nahantu | **Judicator's Mask** → Lair Key | Cathedral's Song, Herald's Morningstar |

#### Escalón 2 — Llave de Guarida Mayor (Greater Lair Key)

| Jefe | Ubicación | Cadena de materiales | Únicos de Paladín |
|---|---|---|---|
| **Duriel** | Gaping Crevasse, Kehjistan | *Mucus-Slick Egg* → **Shard of Agony** → **Greater Lair Key** | Supplication, **Ward of the White Dove** |
| **Echo of Andariel** | Hanged Man's Hall, Kehjistan | *Sandscorched Shackles* → **Pincushioned Doll** → Greater Lair Key | Argent Veil, Dawnfire |
| **Harbinger of Hatred** | Sur de Kurast Docks, Nahantu | **Abhorrent Heart** → Greater Lair Key | Gate of the Red Dawn, **Mantle of the Grey** |
| **The Butcher** | The Broiler, Gea Kul | **Pound of Flesh** | March of the Stalwart Soul, Red Sermon |
| *(vía alternativa)* | The Pit | **Stygian Stone** → Greater Lair Key | — |

#### Escalón 3 — Llave de Guarida Superior (Superior Lair Key)

| Jefe | Ubicación | Cadena de materiales | Notas |
|---|---|---|---|
| **Belial, Lord of Lies** | Palace of the Deceiver, Kehjistan | **Betrayer's Husk** → *"Bring it to an Alchemist to convert it into a Superior Lair Key"* **[JUEGO]** | Botín elegible de cualquier tabla; probabilidad de Mítico elevada |
| **Corrupted Reaper** *(estacional)* | Pandemonium Threshold, Zarbinzet | Superior Lair Key | **Mejores probabilidades de Mítico del juego**; hasta 2 Fragmentos de Pandemónium |

#### Fuera de escalón — Mephisto

Tooltip literal **[JUEGO]** de `Crux of the False Prophet`: *"Used to open Mephisto's Hoard. **Rarely found in Torment X or higher** from Greater Lair Bosses. Very Rarely found from Key Spoils in War Plans."*
**Traducción:** el Eco de Mephisto está **detrás de Tormento X**. Para tu personaje, en 4 semanas, **no existe**. (El parche 3.1.3 arregló que los miembros del grupo que se unen a un Eco de Mephisto en curso puedan usar el portal a la tercera fase — [FECHADO 12/08/2026] Blizzard. Relevante para el dúo, si algún día llegáis.)

### 9.2 De dónde salen las llaves sin matar jefes

Tooltips literales **[JUEGO]**:
- **Lair Key / Greater Lair Key:** *"Found in Torment difficulties from: Key Spoils in War Plans · Tortured Gifts in Helltide…"* — **las llaves normales caen en Helltide y en War Plans, en dificultad Tormento**.
- **Greater Lair Key:** también del **Glacial Fissure**.
- **Superior Lair Key:** *"Acquired from Belial, Lord of Lies, who sometimes ambushes after opening a Lair Boss's Hoard. **Belial will only drop his treasure for those who opened the Hoard that caught his attention.**"*

⚠️ **Esa última frase es crítica para el dúo:** si Belial embosca, **solo cobra quien abrió el Alijo que lo atrajo**. **Id los dos con llaves y abrid los dos vuestro propio Alijo**, o uno de los dos se queda sin nada.

- **Cachés del Rango de Temporada:** existen `Lair Key Ring`, `Greater Lair Key Ring` y **`Superior Lair Key Ring`** — *"Grants several Superior Lair Keys"* **[JUEGO]**. **El Season Journey te regala llaves superiores.** Hazlo.
- **Cámara Deathtoll:** *"Deathtoll Chambers will always reward at least one Superior Lair Key in high Torment levels"* — [FECHADO 14/07/2026] Blizzard, parche 3.1.1. **Es la vía fiable y no aleatoria.**

⚠️ **Contradicción sin resolver sobre el coste de un Alijo Exaltado:** conquestcapped [18/07/2026] dice **2 Llaves Superiores** por Alijo Exaltado (Belial / Corrupted Reaper); otras fuentes secundarias dicen **1**. **No lo he podido confirmar en fuente preferente. Presupuesta 2 y llévate de sobra.**

### 9.3 Dónde caen los tres Únicos que la build necesita

| Único | Jefe | Confianza |
|---|---|---|
| **Ward of the White Dove** (escudo) | **Duriel** | **Alta** — dos fuentes independientes convergen [⚠️ SECUNDARIO 18/07/2026 conquestcapped + extracto de buscador] |
| **Mantle of the Grey** (pechera) | **Harbinger of Hatred** | **Media** — [⚠️ SECUNDARIO 18/07/2026 conquestcapped]. Un extracto de buscador decía "Arcadia", que es **otro Único de Paladín** (pantalones, `Pants_Unique_Paladin_002` **[JUEGO]**) y por tanto un error de la fuente. Me quedo con Harbinger |
| **Herald of Zakarum** (escudo) | Andariel, Duriel o Harbinger of Hatred | **Baja** — solo extracto de buscador; **no aparece en la tabla de conquestcapped que abrí**. Verifícalo en tu pantalla |

**Lectura práctica:** **los tres Únicos que la build quiere están en el escalón 2 (Llave de Guarida Mayor)**, y las Llaves Mayores *"caen más a menudo"* a partir de **Tormento VI** **[JUEGO]**. Eso te da un objetivo intermedio muy claro entre T V (Obducita) y T VII (Polvo Volátil).

---

## 10. Datos muertos y contradicciones detectadas

### 10.1 La Maestría ya no tiene golpes en 4/8/12
Cualquier guía que hable de tres "Masterwork crits" describe el sistema de 2024–2025. En 3.1.x: **25 rangos, +1 % cada uno, un solo capstone en el 25 con +50 % a un afijo aleatorio**. [⚠️ SECUNDARIO 30/07/2026, decl. 3.1.0–3.1.2] https://timesaver.gg/blog/diablo-4-masterworking-guide-season-14

### 10.2 El Neathiron está deprecado — y Maxroll aún lo cobra
Tooltip **literal del cliente 3.1.0** **[JUEGO]**:
> *"Neathiron: Material that used to be earned from deep inside The Pit, but has **mysteriously vanished**. Can be Refined into the Obducite at the Alchemist."*

Sin embargo, `worldTiers` sigue anunciando *"Neathiron now drops more frequently"* en **Tormento IV** **[JUEGO]** — **el propio cliente se contradice consigo mismo**. Y la página de crafteo de Maxroll [FECHADO 29/06/2026] sigue pidiendo **1 Neathiron** para recolocar el capstone de un objeto de 900. **Si tienes Neathiron guardado, refínalo a Obducita. Si un coste te pide Neathiron, compruébalo en el yunque antes de contar con él.**

### 10.3 El coste del Mítico: Blizzard dice 4, Maxroll dice 5
Blizzard, 3.1.1, **14/07/2026**: *"Reduced the cost of the Upgrade to Mythic recipe on the Horadric Cube from 5 to 4 Pandemonium Fragments."*
Maxroll, página del Cubo, **16/07/2026**: *"5x Pandemonium Fragment."*
**Gana Blizzard. Son 4.**

### 10.4 Las páginas nucleares de crafteo de Maxroll están sin actualizar desde antes del Paladín
- `masterworking-guide`: última actualización **23/05/2026**, declara **parche 2.5.0 (Season 11)**.
- `tempering-guide`: última actualización **23/05/2026**.
- `general-farming-guide`: la fetch devolvió *"Last Updated: 25/07/2026 (archived)"* pero con **referencia a Season 8 (19/04/2025)** en el cuerpo. **Página zombi.**

El Paladín salió el **28/04/2026**. **Ninguna de esas tres páginas ha sido revisada con la clase nueva encima.** Por eso el §4.3 de este informe viene del datamining y no de ellas.

### 10.5 Las penalizaciones defensivas por tier de Tormento no existen en los datos 3.1.0
Ver §5.4. **Es la afirmación más repetida de internet sobre progresión de Tormento y no la sostiene el cliente.**

---

## 11. Tabla maestra: "qué farmeo según lo que necesito"

Fuente por defecto: tooltips del cliente **[JUEGO — v3.1.0.72698]**. Se indica cuando viene de otro sitio.

| Necesito… | Actividad principal | Detalle / cifra |
|---|---|---|
| **Obducita** | Mazmorras de Pesadilla · Hordas Infernales · Ciudad Baja de Kurast | Tooltip: *"Collected at level 60 from: Nightmare Dungeons, Infernal Hordes, Undercity of Kurast"*. Maxroll añade el **Tributo de Refinamiento** en la Ciudad Baja y **Bartering con mercenarios** [FECHADO 09/07/2026] |
| **Obducita (máximo rendimiento)** | **Cámara Fuerte Horádrica** dentro de Mazmorra de Pesadilla | ***"~350 por minuto con recompensas de tier 6 en Tormento 12"*** — [FECHADO 03/07/2026] https://maxroll.gg/d4/meta/optimal-farming-guide |
| **Obducita (multiplicador)** | **Elixir de Obducita** | *"Grants 15 % more Obducite from Nightmare Dungeons. Duration: 30 minutes"* |
| **Obducita (cachés)** | Refinado en el Alquimista | Small I **15** · Small II **45** · Medium I **75** · Medium II **225** · Large I **300** · **Large II 900** |
| **Almas Olvidadas** | **Desguazar legendarios en el Herrero** · Botín de salvamento en **War Plans** · Cachés del **Árbol de los Susurros** | Maxroll señala la **Caché de Material Mayor del Árbol de los Susurros** como fuente principal [FECHADO 03/07/2026]. **3.1.1 arregló que no cayeran de las Cachés de Susurro en Tormento** [FECHADO 14/07/2026, Blizzard] |
| **Sigilos Abstrusos** (Maestría de joyería) | **Desguazar joyería** legendaria/única/mítica · Cachés de recompensa | Trato comercial del mercenario **Subo** los ofrece en Bartering |
| **Cristales Velados** | Desguazar objetos raros, legendarios y únicos | — |
| **Coiling Ward** (armadura legendaria) | Desguazar armadura legendaria/única/mítica | Trato comercial de **Raheir** |
| **Fragmentos Balefu­l** (imprimir aspectos) | Desguazar equipo | Trato comercial de **Varyana** |
| **Prismas Dispersos** (engarces en ancestrales) | **Jefes de mundo** · Ciudadela Oscura · Duendes del tesoro | *"Frequently found in Torment difficulties"* |
| **Polvo Primordial** (todos los tipos) | **Cube Spoils en War Plans** · Cachés del **Árbol de los Susurros** · **Monstruos de élite** · **Ciudad Baja de Kurast** | Los ocho tipos comparten fuente. Maxroll añade **Mazmorras de Pesadilla con Nemesis + Fearless Conviction** por densidad de élites [FECHADO 03/07/2026] |
| **Polvo Primordial Volátil** (Transfiguración) | Igual, pero **cae más a partir de Tormento VII** | `worldTiers` |
| **Polvo Primordial Resonante** (→ Afijo Mayor) | Igual. *"An exceptionally rare material"* | Es la **única fabricación directa de Afijo Mayor** documentada |
| **Llaves de Guarida / Mayores** | **Helltide (Tortured Gifts)** · **Key Spoils en War Plans** · Glacial Fissure | Maxroll: *"Helltides with Writhe and Rot War Plans"* es lo más eficiente [FECHADO 03/07/2026] |
| **Llaves de Guarida Superiores** | **Cámara Deathtoll** (garantiza ≥1 en Tormento alto) · **Emboscada de Belial** · **Cachés del Rango de Temporada** | [FECHADO 14/07/2026, Blizzard 3.1.1] + tooltips |
| **Fragmentos de Pandemónium** | **Corrupted Reaper** (hasta 2, escala con Tormento) · **"Glints of Hope"** del tablero de reputación (garantiza 1) | [FECHADO 14/07/2026, Blizzard 3.1.1] |
| **Chispas Resplandecientes** | **Desguazar un Mítico en el Herrero** | Tooltip literal |
| **Manuales de Temple Legendarios** | Cualquier contenido, pero **más a menudo desde Tormento II** | `worldTiers` |
| **Pergaminos de Restauración** | **Más a menudo desde Tormento II** · Ciudadela Oscura · Hordas Infernales | `worldTiers` + ⚠️ [CADUCO 23/05/2026] |
| **Runas Legendarias** | **Más a menudo desde Tormento V** | `worldTiers` |
| **Set Charms** | **Más a menudo desde Tormento III** | `worldTiers` |
| **Amuletos (Charms) Únicos** | **Más a menudo desde Tormento VIII** | `worldTiers` |
| **Fragmentos de Gema** | **Escalating Nightmares con Gem Reserve** | *"Most optimal place"* [FECHADO 03/07/2026] |
| **Oro** | Árbol de los Susurros · **vender Sellos Horádricos Legendarios** · Escalating Nightmares | [FECHADO 09/07/2026] endgame-progression |
| **XP de Glifos** | El Pit más alto que completes | [FECHADO 09/07/2026] |
| **XP de Paragón** | Pit que limpies **en menos de 3 minutos** · Helltide con mejora Writhe and Rot | [FECHADO 09/07/2026] |

---

## 12. Ruta concreta para tus 4 semanas

Ordenada, con la puerta de cada paso.

**Semana 1 — llegar a Tormento I y NO gastar nada**
1. Nivel 70. En Penitente, sin tocar materiales caros.
2. **Pit 10 → Tormento I.** Es la puerta: sin Ancestrales no hay nada que optimizar.
3. En cuanto entres en T I: **templa todo lo ancestral al instante**. Cero Obducita.
4. Objetivo de piezas: cualquier ancestral con el afijo correcto. **No filtres por Afijos Mayores todavía.**

**Semana 2 — Tormento II–IV, acumular**
5. **Pit 15 → T II.** Aquí empiezan a caer los **manuales de temple legendarios**. Farmea hasta tener `Juggernaut Augments` y `Paladin Resolve` en legendario, que son los dos que definen la build.
6. **El arma es la excepción:** si te cae un arma ancestral con buen daño base, **esa sí la puedes empezar a masterworkear**.
7. Acumula **Almas Olvidadas** como si fueran oro. Son tu cuello de botella (§4.1), no la Obducita.
8. **Pit 25 → T IV.** Si tienes Neathiron, **refínalo a Obducita en el Alquimista** (§10.2).

**Semana 3 — Tormento V, abrir el grifo de la Obducita**
9. **Pit 30 → Tormento V. Este es el hito de la temporada.**
10. Ahora sí: **Maestría a Calidad 25**, empezando por **yelmo, pechera y pantalones** — son las tres piezas que necesitan el capstone en el temple de Resolve (§7.3).
11. Cámaras Fuertes Horádricas en Mazmorras de Pesadilla para Obducita. Usa el **Elixir de Obducita** (+15 %).
12. Aparecen las **runas legendarias**: empieza a mirar runewords.

**Semana 4 — Tormento VI y el Mítico**
13. **Pit 40 → T VI**, donde caen más **Llaves de Guarida Mayores** — que son las de **Duriel, Andariel y Harbinger of Hatred**, los tres jefes que sueltan `Ward of the White Dove`, `Mantle of the Grey` y (probablemente) `Herald of Zakarum`.
14. Cámaras Deathtoll para **Llaves Superiores** → **Corrupted Reaper** → **Fragmentos de Pandemónium**.
15. Con **4 Fragmentos**: **un** Mítico en el Cubo, en la ranura que tengas peor. **Solo uno se puede equipar** (§8.2).
16. **No transfigures nada.** El Polvo Volátil no fluye hasta T VII y la Transfiguración es irreversible.

**En dúo, lo específico:**
- **Abrid cada uno vuestro propio Alijo.** Si Belial embosca, *"only drop his treasure for those who opened the Hoard"* **[JUEGO]**.
- Tu pareja va de nigromante **sin expansiones**: no tiene Cubo Horádrico ni Amuletos/Charms. **Todo lo que sea Fragmento de Pandemónium, Polvo Primordial y Set Charm es material que solo tú puedes usar.** No lo repartáis a medias.
- El parche **3.1.3** arregló el portal de la tercera fase del Eco de Mephisto para quien se une a la pelea en curso [FECHADO 12/08/2026] — irrelevante ahora (Mephisto es T X+), útil de saber.

---

## Fuentes

**Abiertas y leídas de verdad en esta sesión.**

**Fichero de datos del juego (datamining, declarado como tal):**
- https://assets-ng.maxroll.gg/d4-tools/game/data.min.json — HTTP 200, 11.606.292 bytes, `"version":"3.1.0.72698"`. Campos usados: `worldTiers`, `temperingRecipes`, `temperingGroups`, `affixes`, `attributeFormulas`, `attributeDescriptions`, `items`, `heroDetails`, `skills`, `classes`. **Es 3.1.0, tres hotfixes por detrás del parche vivo 3.1.3.**

**Blizzard (preferente):**
- https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes — notas de 3.1.0 (30/06/2026), 3.1.1 (14/07/2026), 3.1.2 (28/07/2026) y 3.1.3 (12/08/2026)

**Maxroll (preferente) — respondió, sin 403 en esta sesión:**
- https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide — act. **25/07/2026** (3 consultas distintas)
- https://maxroll.gg/d4/meta/endgame-progression — act. **09/07/2026** (3 consultas distintas)
- https://maxroll.gg/d4/resources/item-crafting — act. **29/06/2026**
- https://maxroll.gg/d4/resources/horadric-cube — act. **16/07/2026**
- https://maxroll.gg/d4/resources/equipment — act. **25/07/2026**
- https://maxroll.gg/d4/getting-started/defenses-for-beginners — act. **16/08/2026**
- https://maxroll.gg/d4/meta/optimal-farming-guide — act. **03/07/2026**
- https://maxroll.gg/d4/resources/masterworking-guide — ⚠️ act. **23/05/2026**, declara parche **2.5.0**
- https://maxroll.gg/d4/resources/tempering-guide — ⚠️ act. **23/05/2026**
- https://maxroll.gg/d4/resources/general-farming-guide — ⚠️ zombi (referencia a Season 8)

**Icy Veins (preferente):**
- https://www.icy-veins.com/d4/news/diablo-4-season-14-patch-notes-increased-mythic-and-pandemonium-fragment-drop-rates/ — parche **3.1.1**, build 72805, **14/07/2026**
- https://www.icy-veins.com/d4/guides/blessed-shield-paladin-build/ — act. **24/06/2026**. ⚠️ **Es de Blessed Shield, NO de Shield Charge**: sus tablas de equipo **no son trasladables** a esta build y no las he usado como tales
- https://www.icy-veins.com/d4/guides/horadric-strongrooms/ — sin fecha visible; sin cifras de Obducita

**Otras (declaradas como secundarias):**
- https://d4guides.gg/en/s14/bosses — escalones de llaves
- https://conquestcapped.com/guides/diablo-4/diablo-4-bosses-guide/ — act. **18/07/2026** — ubicaciones y Únicos de Paladín por jefe
- https://conquestcapped.com/guides/diablo-4/mythic-unique-crafting/ — act. **26/07/2026** — costes de Herrero y Joyero
- https://timesaver.gg/blog/diablo-4-masterworking-guide-season-14 — pub. **30/07/2026**, declara cubrir **3.1.0–3.1.2**

**Intentadas y fallidas (declaradas):**
- https://mobalytics.gg/diablo-4/builds/paladin-shield-charge-endgame-build-guide — **HTTP 403**
- https://maxroll.gg/d4/resources/horadric-cube-guide — **HTTP 404** (URL correcta sin `-guide`)
- https://www.wowhead.com/diablo-4/guide/gear/defenses-armor-elemental-resistance-damage-reduction — cargó solo cabecera y comentarios; **sin cuerpo del artículo**. Marcaba "Updated: 2026/04/27" y "Season 13"
- reddit.com — bloqueado al rastreador por política

---

## No encontrado

**Lo que el encargo pedía y no puedo entregar con fuente. Prefiero el hueco al número con buena pinta.**

1. **La tabla de equipo de Shield Charge Paladin, pieza a pieza.** Maxroll la sirve dentro del planificador interactivo, no en el HTML de la guía. La fetch devolvió textualmente que *"the actual slot-by-slot breakdown … is not present in the text provided"*. Mobalytics, que la tiene, dio **403**. **Los únicos nombres de objeto que la guía de Maxroll expone en texto son:** `Mantle of the Grey`, `Tibault's Will`, `Herald of Zakarum`, `Blood-Mad Idol`, `Aspect of Glynn's Anvil` y el set `Phoba of Righteous Will`. **Nada más. No he inventado el resto.**

2. **Cuántos Afijos Mayores caben por pieza y por tipo de objeto.** La cifra "3 en legendario ancestral / 4 en Único / 1 en Mítico / ×1,5 al valor máximo" **solo la sostienen fextralife (vetada) y agregadores sin fecha**. Ni `item-crafting` ni `equipment` de Maxroll la publican en su HTML. **No la doy por buena.**

3. **Objetivos numéricos de Armadura / Resistencias / Vida / Dureza por tier de Tormento.** **Ninguna fuente preferente y fechada dentro de 3.1.x los publica.** Maxroll da la fórmula pero **explícitamente ningún objetivo** (*"The document contains no specific Life, Armor, or Resistance targets by Torment tier"*). Las cifras que devuelven los buscadores (13.500 de armadura, 45.000 de vida, cap del 70 %, −25 % de resistencias por tier) vienen de páginas sin fecha de la era *Vessel of Hatred* y **se contradicen entre sí**. La tabla del §5.3 **la he calculado yo** y está marcada como tal.

4. **Si la lista "1. Mantle of the Grey 2. Tibault's Will 3. Herald of Zakarum" son objetivos de crafteo Mítico o indicaciones de ranura.** El datamining demuestra que los tres son **Únicos (`magicType: 2`), no Míticos**, y que la receta del Cubo produce un resultado **aleatorio de la misma ranura**. La lectura "es la ranura donde gastar los Fragmentos" **encaja pero es derivación mía**. **Verifícalo en el Cubo antes de gastar 4 Fragmentos.**

5. **El coste en Llaves Superiores de un Alijo Exaltado.** Una fuente secundaria dice **2**, otras dicen **1**. Sin confirmación preferente.

6. **La receta estacional "7 Fragmentos de Pandemónium → 1 Chispa Resplandeciente".** Solo en extracto de buscador de fuente secundaria. **Sin confirmar.**

7. **Las cantidades exactas del Joyero** (3 Chispas + 5.000.000 de oro + 3 runas nombradas ×3). El tooltip del juego confirma **que el Joyero craftea Míticos con Chispas**; **las cantidades son de fuente secundaria**.

8. **Obducita por run de Cámara Fuerte Horádrica por tier de Atonamiento.** Maxroll da **~350/min a tier 6 en Tormento XII**, pero **no publica la tabla por tier de Atonamiento**, y la página de Icy Veins sobre Cámaras Fuertes **no trae cifras**. Los "800–1.000 en Tormento IV" y "1.000–2.000 por run" que devuelven los buscadores son de agregadores sin fecha. **No los uses para planificar.**

9. **La discrepancia de `classFilter` en las recetas de temple del Paladín.** En los datos 3.1.0, `Paladin Perseverance` tiene el filtro de clase de Paladín en `true`; `Paladin Resolve`, `Paladin Guard`, `Paladin Recovery` y `Paladin Motion` lo tienen **todo en `false`**, igual que `Barbarian Control`. No sé si es un campo sin usar, un artefacto del volcado o algo real. **No lo interpreto.**

10. **Qué hereda exactamente la cuenta al empezar el Paladín** (alijo, oro, materiales, Renombre, altares, progreso de campaña, Rango de Temporada). **Fuera de mi dominio y sin fuente abierta en esta sesión.** Lo cubre otro informe del proyecto.

11. **Si hubo un nerf a la tasa de Obducita en la S14.** Un titular de agregador lo afirma ("after drop rate nerf"). **Las notas de 3.1.0 a 3.1.3 de Blizzard que abrí no contienen ningún cambio de Obducita ni de Maestría.** Sin confirmar.

12. **Efecto y valores concretos de `The Empyrean Eye`** (la gema Mítica) y de `El'Druin, Sword of Justice`. Aparecen en el cliente y en las notas de 3.1.1 respectivamente, pero **no encontré descripción de sus poderes en fuente fechada**.
