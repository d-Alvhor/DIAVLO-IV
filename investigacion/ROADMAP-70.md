# ROADMAP 70 — Nigromante de esbirros con las dos expansiones

**Fecha de síntesis:** 20 de agosto de 2026 · **Parche vivo:** 3.1.3 (build 73224, 12/08/2026)
**Temporada:** 14 "Death Awakening" (desde 30/06/2026) · **Fin estimado:** ~15/09/2026 → **quedan ~4 semanas**

> El 15/09 lo leen los rastreadores del **temporizador in-game**, no de un anuncio de Blizzard. Hay estimaciones alternativas del 21 y del 28 de septiembre. **Planifica con 27 días y no te sorprendas si son 33.**

**Fuente:** síntesis de los 7 informes de campo (`crudo/exp-*.md`) y de sus 5 refutaciones adversariales (`refutacion/exp-*.md`). Donde el informe y su refutación chocan, **manda la refutación** y lo digo. Donde dos informes chocan entre sí, lo digo también.

---

## 0. Antes de nada: cinco correcciones de marco

No son detalles. Cada una cambia una decisión que ibas a tomar.

| # | Lo que probablemente creías | Lo que es |
|---|---|---|
| 1 | "Tormento IV es el techo" | **Hay 12 Tormentos.** T4 es el escalón 4 de 12 y solo pide **Foso 25**. El techo real es T12 = Foso 100, y el Foso llega a 150. — [Blizzard: *"Torment levels expand from 4 to 12"*](https://news.blizzard.com/en-us/article/24267729/prepare-for-the-reckoning-lord-of-hatred-draws-near). Verificado entrada por entrada contra el fichero de datos del juego. **Confianza: alta.** |
| 2 | "Solo puedo llevar 1 Mítico crafteado" | **Ese límite ya no existe.** Se eliminó el 16/07/2026 (PC) en el hotfix 3.1.1a: *"Removed the 'one-crafted Mythic' equipment restriction on Mythic items"* — [post oficial de Blizzard](https://us.forums.blizzard.com/en/d4/t/311a-patch-july-16-2026/263234). **Confianza: alta (fuente oficial).** ⚠️ **Dos de mis propios informes (`exp-roadmap-70`, `exp-builds-nigro`) siguen repitiendo el límite** porque copiaron a Maxroll (13/07) e Icy Veins (27/06), ambas anteriores al hotfix. **El informe del Cubo tiene razón y los otros dos están muertos en ese punto.** |
| 3 | "El nivel 70 y los Tormentos son de la expansión" | **Son gratis para todos.** Blizzard los pone en la columna *"Available across full game regardless of expansion ownership"*, junto al filtro de botín, el mapa superpuesto y el rediseño de los árboles de habilidad. **Tu pareja ya los tiene aunque no compre nada.** — [misma URL](https://news.blizzard.com/en-us/article/24267729/prepare-for-the-reckoning-lord-of-hatred-draws-near). **Confianza: alta.** |
| 4 | "Recorrer los Tenets of Akarat / Chronicles of Creation da puntos" | **En reino de temporada, no.** El Renombre se retiró del reino estacional en el parche 2.5.0 y lo sustituye el **Rango de Temporada** — [Maxroll](https://maxroll.gg/d4/resources/renown-system) (09/12/2025) · [Icy Veins](https://www.icy-veins.com/d4/guides/season-rank/). Los 30 Tenets y los 30 Chronicles te dan XP del momento, logros y monturas. **Cero puntos de habilidad, cero Paragón.** **Confianza: alta.** Esto te habría costado un fin de semana. |
| 5 | "Lord of Hatred y Vessel of Hatred son dos compras" | **LoH incluye VoH.** Literal: *"Diablo IV: Lord of Hatred includes our first expansion, Vessel of Hatred"* — [Blizzard](https://news.blizzard.com/en-us/article/24247511/stand-against-mephisto-pre-purchase-lord-of-hatred). **Si compraste las dos por separado, revisa la tienda de tu cuenta hoy.** Y: te has desbloqueado **tres** clases nuevas, no dos — Paladín, Brujo y **Spiritborn** (que viene con VoH). |

---

## Las primeras 2 horas

Orden estricto. Los pasos 1–6 son gratis, reversibles y desbloquean lo que más rinde. Sé honesto contigo mismo: **los pasos 7 y 8 probablemente se te vayan de las dos horas**, y no pasa nada.

### 1. Sal del juego y vuelve a entrar

Los desbloqueos de compra entran *"after next login"* — [página oficial de LoH](https://diablo4.blizzard.com/en-us/lord-of-hatred), nota al pie. Sin esto no verás nada.

### 2. Revisa la cuenta (2 minutos, puede valerte dinero)

- ¿Pagaste **VoH y LoH por separado**? LoH la incluía. Si es así, es un caso de soporte.
- Comprueba que tienes: **Paladín, Brujo, Spiritborn**, **+1 pestaña de alijo**, **+2 huecos de personaje**.

### 3. Respec del árbol: **Gravebloom → Gargantua**

Es el cambio de mayor retorno por coste cero de todo el documento. Gargantua era **la variante bloqueada** del Gólem (de las tres variantes de cada habilidad, sin LoH tenías dos — [foro oficial](https://us.forums.blizzard.com/en/d4/t/must-have-the-lord-of-hatred-expansion-to-open-all-three-bonus-skill-variants-otherwise-2-out-of-3-bonus-skill-variants-are-accessible/245511)).

Texto literal del fichero de datos: *"Golem now raises a larger Golem that gains an aura of command, increasing the **Cast Speed and Movement Speed** of your other Minions by [0.2*Table(34,sLevel)*100]%[x]"*.

| Rango del Gólem | Aura a los otros esbirros | Confianza |
|---|---|---|
| 1 | **20%[x]** | Alta — fórmula y `powerTables[34]` recalculados por dos pasadas independientes |
| 3 | 24%[x] | Alta |
| 10 | **40%[x]** | Alta |
| 15 | 51%[x] | Alta |
| 20 | 62%[x] | Alta |

**Sube el rango del Gólem.** El aura escala fuerte y es la parte gratis del cambio.

⚠️ **Gravebloom te da 3 gólems; Gargantua te da 1 gólem grande.** Pierdes dos cuerpos y ganas un aura multiplicativa sobre toda la horda. Ninguna guía de endgame usa Gravebloom — es opción de subida.

### 4. Mira la hoja de personaje con y sin Gargantua

**Este es el hueco número uno de toda la investigación y lo cierras tú en 30 segundos.** El fichero del juego dice **Cast Speed** (velocidad de lanzamiento). Icy Veins lo llama *"Attack Speed aura"* y Maxroll lo mete en su FAQ de **cómo llegar al 100% de velocidad de ataque** (*"Golem Aura gives you as much as you need"* — [Maxroll, 22/07/2026](https://maxroll.gg/d4/build-guides/minion-necromancer-guide)). **Nadie lo ha escrito.** Si tu Velocidad de Ataque se mueve al invocar el Gargantua, la duda se acaba.

### 5. Quita el glifo **Dominate** si lo llevas

*"Dominate Glyph: Reduced from 23.6% per stack to 1.8% per stack at glyph level 150"*. **Está en el parche 3.1.0 (30/06/2026)**, no en el 3.1.3 — mi informe original lo atribuyó mal y la refutación lo recalculó a mano desde el fichero (`base=1, perLevel=0.005625` → 1,838% a nivel 150). **Confianza: alta, verificado dos veces.**

Pon **Mage** y **Warrior** primero.

> **Matiz honesto:** la guía de esbirros de Maxroll está fechada el **22/07/2026** — es decir, **tres semanas POSTERIOR al nerfeo** — y **sigue recomendando Dominate** como primer glifo en su variante híbrida. No es que no se hayan enterado. Puede que el tablero Dominate valga por sus nodos aunque el glifo esté muerto. **Mi consejo sigue siendo quitarlo, pero el argumento "esa guía está caducada" es falso.**

### 6. Abre la pestaña de Rango de Temporada y busca el **Rango 2**

**En reino de temporada, El Foso NO se abre por nivel.** Se abre completando **Hellish Descent** (mazmorra de capitel, nivel 60, dificultad Penitente), que es el requisito del Rango de Temporada 2 — [Maxroll — Pit Guide](https://maxroll.gg/d4/resources/pit-guide) (16/07/2026) · [Maxroll — Season Rank](https://maxroll.gg/d4/resources/season-journey) (13/07/2026). **Confianza: alta.**

Si no lo tienes hecho, es lo único que hay que hacer antes de cualquier otra cosa. **Sin Foso no hay glifos, ni Tormentos, ni nada.**

### 7. Foso hasta el nivel 10 → **Tormento I**

Texto literal del juego: `"Unlock Artificer's Tier and Conquer Tier 10 on this character"`. Tormento I da **+300% XP y +100% oro** frente a Penitente, y sobre todo **abre los objetos Ancestrales** y desbloquea la mayoría de los Tributos de la Subciudad (*"Only usable in Torment Difficulties"*). **Es el cuello de botella número uno del día.**

### 8. Arranca la campaña de **Vessel of Hatred**. Línea recta, cinemáticas saltadas

**No puedes saltarte ninguna de las dos campañas.** El "Saltar campaña" solo aparece **al crear personaje** y solo si esa campaña ya está completada **una vez en la cuenta** — y tú no la has completado nunca. Crear un Nigromante nuevo tampoco sirve: tampoco podría saltarla, y empezarías a nivel 1.

- Condición documentada (**confianza alta**): *"To skip the story in future seasons, you must complete the Lord of Hatred campaign at least once"* — [Icy Veins, 24/04/2026](https://www.icy-veins.com/d4/guides/lord-of-hatred-overview/).
- Condición "solo en creación de personaje" (**confianza media**): solo la sostienen tres hilos de foro sin respuesta oficial. **Mira la pantalla de selección de personaje antes de dar por perdida la tarde.**

**A nivel 70 la campaña no te da progresión de nivel útil, solo llaves.** Puedes correrla en modo bulldozer.

**Por qué VoH antes que LoH:** un jugador reportó quedarse **sin punto de inicio para VoH** tras hacer LoH primero ([foro US, 13/05/2026](https://us.forums.blizzard.com/en/d4/t/start-vessel-of-hatred-after-lord-of-hatred/253311), sin respuesta azul). No está probado que esté roto, pero es un riesgo asimétrico: hacer VoH primero no te cuesta nada y es el orden narrativo. **Confianza: media.**

---

## ¿Cambio de build?

### Respuesta corta

**No cambies de build. Haz el ajuste barato hoy y no persigas el caro.** Y no existe "la build de Gargantua": **Gargantua es una variante de habilidad, no una build.** Cualquier build de esbirros de endgame la lleva.

### El cambio se parte en dos mitades con costes incomparables

| Mitad | Qué incluye | Coste | ¿Da tiempo en 27 días? |
|---|---|---|---|
| **Barata** | Variantes del árbol (Gargantua), tipos del Libro de los Muertos, sacrificios, barra de habilidades, palabras rúnicas, mercenario, orden de glifos | **Gratis, reversible, ~20 minutos** | **Sí, hoy** |
| **Cara** | 4–6 Únicos concretos + set de 5 Charms + Masterworking a 25 + Míticos | **Semanas de farmeo** | **No desde cero** |

La mitad barata contiene el aura de Gargantua (**20%[x] → 40%[x]**), los ajustes de glifos y las runas. Y además **te deja el personaje configurado para la S15**: lo que no se reinicia al empezar temporada es saber qué elegir.

### Un motor que creías tener y no tienes

Mi informe de builds anunció como hallazgo propio que *"cada sacrificio que no sea el del gólem le da al gólem +60%[x] de daño"*. **La refutación lo tumbó, y con razón.** El texto completo del fichero es:

```
"...but the amount of Cold Mages you can Summon is reduced by 50%.
{if:ParagonNodeIsPurchased(681465)}  Your Golem gains 60%[x] increased damage. {/if}"
```

El nodo **681465** es **Hulking Monstrosity**, un nodo legendario que vive en un tablero de Paragón que se llama igual. **Sin ese tablero enganchado, sacrificar magos o guerreros no le da absolutamente nada al gólem.** Verificado también en [PureDiablo](https://www.purediablo.com/diablo4/Hulking_Monstrosity_Node). **Confianza: alta.**

Consecuencia: **el sacrificio sigue valiendo por su bonus propio** (Iron [Sacrifice] = +15%[x] daño crítico para ti; Reaper [Sacrifice] = +15%[x] daño), **pero no por el gólem** salvo que cojas ese tablero.

### Corrección de vocabulario que te va a ahorrar buscar en pantalla algo que no existe

Mi informe presentó una tabla de "órdenes de tablero de Paragón" con los nombres **Warrior, Mage, Essence, Eliminator, Abyssal, Deadraiser, Dominate**. **Esos son GLIFOS, no tableros.** Lo que Maxroll publica bajo ese epígrafe es literalmente *"Paragon Board **Glyph** Priorities"*.

**Los 10 tableros reales del Nigromante**, leídos del fichero:

> **Start · Cult Leader · Hulking Monstrosity · Flesh-eater · Scent of Death · Bone Graft · Blood Begets Blood · Bloodbath · Wither · Frailty**

Eliges **5** (incluido el inicial), con **1 ranura de glifo por tablero**. La lista de Icy Veins sí empareja bien tablero con glifo:

1. Starter → glifo **Mage**
2. **Frailty** → glifo **Warrior**
3. **Cult Leader** → glifo **Control** (Naz Mages) o **Essence** (Reaper Summoner)
4. **Flesh Eater** → glifo **Amplify**
5. **Wither** → glifo **Essence** (Naz) o **Deadraiser** (Reaper)

### Las tres candidatas reales, con su coste de entrada

| Build | Tier | Qué reutiliza de lo tuyo | Qué te falta | Fecha de la guía |
|---|---|---|---|---|
| **Reaper Summoner** | **A** (Icy Veins) | **Coven ✅, Master of Puppets ✅, Magos de Sombra ✅, Guerreros Segadores ✅** — cuatro de tus elecciones actuales | Gargantua, Gólem Iron [Sacrifice], barra nueva, y los Únicos: Deathgrip, Pact of Bone, The Undercrown, Blood Moon Breeches | [03/07/2026](https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/) |
| **Naz Mages** | **S** (Icy Veins) | Coven ✅, Unyielding Commander ✅ | **Giro completo a frío** (Magos Cold), variante de guerrero distinta, y **dos Únicos que no tienes**: The Hand of Naz, Signet of Pelghain | [03/07/2026](https://www.icy-veins.com/d4/guides/mendeln-summoner-necromancer-build/) |
| **Shadow Golems Summoner** | **A** (Icy Veins) | Tu perfil de gólem (venías de 3 gólems + Gólem de Sangre) | Reaper [Sacrifice], Bone [Sacrifice], Gólem Iron **[Upgrade #1]**, **Mace of King Leoric**, y el tablero **Hulking Monstrosity** | [02/07/2026](https://www.icy-veins.com/d4/guides/golem-summoner-necromancer-build/) |

### El criterio decidible

Si la respuesta honesta fuera "depende", esto es de qué depende y cómo se decide sin discutir:

> **Por defecto vas a Reaper Summoner.** Reutiliza cuatro de tus cinco elecciones actuales y no exige girar de elemento. Es la ruta de menor fricción y la única que puedes montar hoy sin farmear nada.
>
> **Cambias a Naz Mages solo si te caen Bloodless Scream Y The Hand of Naz antes del 1 de septiembre.** Si a esa fecha te falta uno de los dos, no lo intentes: te quedan tres semanas y estarías a medio camino de dos builds.
>
> **Cambias a Shadow Golems solo si te cae Mace of King Leoric** (lo suelta **The Butcher**, guarida The Broiler, escalón 2 de jefes). Su daño de gólem subió de **70-80% a 100-120%** en el 3.1.0. Es la **única** de las tres que engancha Hulking Monstrosity, y por tanto la única donde el +60%[x] al gólem por sacrificio funciona de verdad.

**Un aviso sobre Naz Mages que su propia guía no ha corregido:** **Signet of Pelghain**, uno de sus dos anillos, se llevó un recorte del 33% en el 3.1.0 — *"Damage bonus reduced from 15-20% to 10-15% per second"* ([notas oficiales](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes)). Icy Veins **sigue publicando 15-20% en su tabla de equipo**, y actualizó la página tres días después del parche. Es exactamente el patrón que ya te ha mordido: el aviso al final no arregla la tabla del principio.

**Y otro sobre Reaper Summoner:** **Hellbent Commander Aspect**, su anillo 1, bajó de *"50-70% a 40-60%"* en el 3.1.0. El valor que la guía publica ya es el post-recorte, así que la guía está bien; el aviso es para que no te sorprendas.

### Ni Maxroll ni Icy Veins tienen razón por autoridad

| Punto | Icy Veins (03/07/2026) | Maxroll (22/07/2026) |
|---|---|---|
| Tier | Naz Mages **S**, Reaper **A**, Shadow Golems **A** | Minion Necro **B** |
| Mercenario | **Varyana** + Raheir | **Subo** + Aldkin |
| Objetivos numéricos | ninguno | **100% Vel. Ataque · 100% Prob. Crítico · 30k Vida · 40+ Resolve** |
| Libro de los Muertos | sección explícita | **no lo menciona** |

**La tier list B de Maxroll está fechada el 29/06/2026 — un día ANTES del parche 3.1.0** y tres semanas antes de que Maxroll reescribiera su propia guía de esbirros. **No es que Maxroll piense que la build es B hoy: es que no ha vuelto a tocar la tier list.** No hay tier list de Nigromante posterior al 3.1.0 en Maxroll.

**Cómo usarlas:** los **objetivos duros de Maxroll** (100/100/30k/40+) son lo más accionable que existe — úsalos como termómetro de "¿voy bien?". El **emparejamiento tablero↔glifo de Icy Veins** es el correcto — úsalo para el Paragón.

### Lo que NO tiene sentido perseguir en 27 días

- **Seal of the Diamond Mind** (cae en Tormento 10+). Es el techo del sistema de Talismán, no tu objetivo de este mes.
- **Dos sets de 5 Charms a la vez.**
- **Masterworking 25 + capstone en todas las piezas.**
- Los **Charms son lo primero que se reinicia** en temporada nueva. Perseguir el 5-set completo a última hora es tirar tiempo.

---

## Roadmap 70 → Tormento IV

**Toda la escalera está verificada entrada por entrada contra el fichero de datos del juego y corroborada por [Maxroll — Difficulty Scaling](https://maxroll.gg/d4/resources/difficulty-overview). Confianza: alta.**

### Bloque A — Abrir la puerta

| # | Paso | Requisito exacto | Qué desbloquea |
|---|---|---|---|
| **1** | **Rango de Temporada 2** | Completar **Hellish Descent** (nivel 60, Penitente) | **El Foso y la Torre.** Sin esto no hay nada más |
| **2** | **Foso 10** | — | **Tormento I** (`"Unlock Artificer's Tier and Conquer Tier 10 on this character"`) |
| **3** | **Cambia a Tormento I ya** | — | **+300% XP, +100% oro.** Aparecen los **objetos Ancestrales**. Se abren la mayoría de Tributos de la Subciudad, la Ciudadela Oscura y el árbol de Jefes de Guarida de los Planes de Guerra |

### Bloque B — La campaña (el peaje inevitable)

| # | Paso | Qué desbloquea | Confianza |
|---|---|---|---|
| **4** | **Campaña de VoH, capítulo 2**, misión *The Hand that Remembers the Blade* | 🆕 **Mercenarios** (Raheir) | Media-alta. Blizzard dice *"upon completing the VoH campaign"*, Wowhead dice capítulo 2, y fuentes independientes confirman el capítulo 2. **Si no aparece, sigue jugando** |
| **5** | **Misión prioritaria de Kurast dentro de VoH** | 🆕 **Subciudad de Kurast** (Brasero de Espíritus, permanente) | Media. **Conflicto abierto:** Maxroll dice que hace falta la campaña; Icy Veins dice solo nivel 20 + invocar la Llama Espiritual. **Compruébalo en 5 minutos entrando a Nahantu** |
| **6** | **Terminar VoH** (*Presaged Fate*) | 🆕 **Palabras Rúnicas** + los alts se saltan VoH para siempre | Alta |
| **7** | **El Cubil (The Den)**: tres misiones de adquisición | 🆕 Varyana, Aldkin, Subo | Media. ⚠️ **Varyana exige antes el Bastión del Templo de la Putrefacción** |
| **8** | **Campaña de LoH hasta el barco a Temis** — misión *Last of the Horadrim* | 🆕 **Talismán, Sellos y Charms**, **a nivel de cuenta** | Alta. *"unlocked early on during the Lord of Hatred Campaign before boarding the ship towards Temis. This unlocks it for your other characters as well"* — [Maxroll, 28/06/2026](https://maxroll.gg/d4/resources/talisman-charms-sets) |
| **9** | **Terminar LoH** | 🆕 **Cubo Horádrico** + 🆕 **Planes de Guerra** (Tyrael, en Temis) | Alta |

> **Si tienes que parar a mitad:** el mejor corte es **terminar VoH** (mercenarios + runas + Subciudad de golpe). El segundo mejor es **llegar al barco de Temis** (Talismán). Los Planes de Guerra y el Cubo exigen terminar LoH entera.

### Bloque C — Los Planes de Guerra, que es la palanca de verdad

| # | Paso | Por qué antes que farmear |
|---|---|---|
| **10** | **Árbol de El Foso**, nodos **Choron's Blessing** y **Choron's Haste** | Base **4** oportunidades de mejora de glifo por carrera + **1** por no morir + *"Up to 4 extra from nodes in the Pit Skill Tree from War Plans"* = **hasta 9 por carrera**. Esta es la razón número uno para tocar los Planes de Guerra hoy |
| **11** | **Árbol de Marea Infernal**: **Hellmouth** → **Writhe and Rot** | *"Whatever Pit Level you can complete efficiently (sub 3 min), **Helltide with the Writhe and Rot War Plan upgrade**"* es lo que Maxroll señala como la mejor XP de Paragón — [Maxroll — Endgame Progression](https://maxroll.gg/d4/meta/endgame-progression) (09/07/2026) |
| **12** | **Árbol de la Subciudad**, rama derecha: **Jade Epiphany → Finely Tuned → Pathfinder → Initiative** | XP + velocidad de ciclo. ⚠️ **Coste oculto: cada uno de esos cuatro nodos añade +1 de Poder de Monstruo** a toda la Subciudad. La rama entera son **+4 acumulados** y los pagas tú |
| **13** | **Carga los planes de Mazmorras de Pesadilla de Escalada y Marea Infernal**, no de actividades normales | XP de actividad en Tormento: estándar **50–150**, Hordas **100–300**, Marea Infernal Mayor **150–450**, **Escalada 170–510**. Son **3,4×** — [Maxroll — War Plans](https://maxroll.gg/d4/resources/war-plans) (05/08/2026) |

⚠️ **El tablero de Planes de Guerra es por personaje y la experiencia de actividad NO se comparte** — *"you must level one from scratch for every character you create"* (misma URL). En la S15 desbloquearás el sistema desde el minuto uno, pero **el árbol lo subes otra vez desde cero**.

### Bloque D — La escalera de Tormentos

Cada escalón solo pide un nivel de Foso. **No hay ningún requisito de estadística ni de nivel.** El gate real es terminar ese Foso en los **15 minutos** sin morir demasiado.

| Tormento | Foso | XP / Oro | Qué desbloquea o mejora |
|---|---|---|---|
| **I** | **10** | +300% / +100% | **Objetos Ancestrales.** Empieza el endgame |
| **II** | **15** | +400% / +120% | **Manuales de Temple Legendarios** y **Pergaminos de Restauración** |
| **III** | **20** | +500% / +140% | **Amuletos de conjunto (Set Charms)** caen más a menudo |
| **IV** | **25** | +600% / +160% | **Neathiron** |
| **V** | **30** | +700% / +180% | **Runas Legendarias.** ⭐ **Aquí empieza el Masterworking** |
| **VI** | **40** | +800% / +200% | **Llaves de Guarida Superiores** → la escalera de jefes |
| **VII** | **50** | +900% / +225% | **Polvo Primordial Volátil** |
| **VIII** | **60** | +1000% / +250% | **Amuletos Únicos.** El 3.1.0 subió la XP de T8 en adelante |
| **IX** | **70** | +1100% / +275% | **Prismas de Sintonización Kulleanos** |
| **X** | **80** | +1200% / +300% | **Sellos Horádricos Míticos** |
| **XI** | **90** | +1300% / +300% | *"For paragons and fools"* (campo `recommended` del propio juego) |
| **XII** | **100** | +1400% / +300% | *"For paragons and fools"* |

> ⚠️ Los porcentajes de XP salen del fichero de datos, cuya versión interna es **3.1.0**. El 3.1.0 subió la XP de Tormento VIII+. **Los valores de T8 a T12 podrían estar ya desactualizados. Declarado.**

**Regla transversal de ritmo, textual:** *"It is often more efficient to farm in a lower Torment difficulty… rather than push into higher tiers"* — [Maxroll](https://maxroll.gg/d4/meta/endgame-progression). **Súbete de Tormento cuando el escalón nuevo te dé algo que quieras** (Ancestrales en I, manuales en II, Set Charms en III, Neathiron en IV, llaves en VI), no por deporte.

### El Rango de Temporada es tu roadmap paralelo, y paga

| Rango | Requisito | Recompensa |
|---|---|---|
| **3** | *Enclave of Darkness* (**Foso 12**, Tormento I) | **+6 Paragón**, 1 alijo Mítico |
| **4** | *Den of the Apostate* (**Foso 18**, Tormento II) | **+12 Paragón** |
| **5** | Cualquier **Jefe de Guarida en Tormento IV+** | **+10 Paragón**, 1 alijo Mítico |
| **6** | **Corrupted Reaper** en el Pandemonium Threshold, **Tormento VI+** | **+8 Paragón**, **1 Chispa** |
| **7** | **Echo of Lilith** en **Tormento VIII+** | Crux of the False Prophet, 1 alijo Mítico |
| **8** | **Echo of Mephisto** en **Tormento X+** | 1 alijo Mítico, **1 Chispa** |
| **9** | 10 objetivos del Rango 9 | 2 alijos Míticos, **7 Chispas** |

**Total oficial de Blizzard:** *"Up to 12 Skill Points"*, *"Up to 42 Paragon points"*, *"Up to 7 Resplendent Sparks"*, *"5 Mythic Unique Caches"*, *"nine ranks and over 120 objectives"* — [blog oficial de S14](https://www.wowhead.com/diablo-4/blue-tracker/news/eu/hunt-the-death-cult-in-season-of-death-awakening-diablo-iv-blizzard-news-24268702). **Maxroll da 14 puntos de habilidad, 9 Chispas y un número de alijos que no cuadra ni consigo mismo. Coinciden solo en los 42 de Paragón.**

### Paragón y glifos: los números que sí están cerrados

| Dato | Valor | Confianza |
|---|---|---|
| Niveles de Paragón | **1 a 300**, empieza al llegar a 70 | Alta |
| Puntos totales | **342** (300 + 42 del Rango de Temporada) | Alta |
| Tableros equipables | **5** contando el inicial · **4 puertas** por tablero · **1 ranura de glifo** por tablero | Alta |
| Nivel máximo de glifo | **150** · se suben **solo en El Foso** | Alta |
| Paso a calidad Legendaria | **15.000 fragmentos de gema** al llegar a nivel 50 | Alta |
| Bono legendario de daño (glifos de esbirros) | **5,5%[×] en nivel 51 → 15,4%[×] en nivel 150** | Alta — dos pasadas independientes lo recalcularon desde `base=0.005, perLevel=0.001` y reproduce los dos puntos que publica Maxroll |
| Glifo **Essence** | **8,575% en nivel 51 → 19,96% en nivel 150** | Media — derivación desde el fichero (`base=0.02825, perLevel=0.00115`), **nadie lo publica para cotejar** |
| Tiempo límite del Foso | **15 minutos** · el Foso llega a **150** niveles · ya no cuesta material entrar | Alta |

**⚠️ Conflicto sin cerrar: ¿el radio del glifo sube en 15 o en 25?** Maxroll dice **25** (tres páginas, todas de julio de 2026); Icy Veins dice **15**, y su página no muestra día de actualización. **El dato no está en el fichero del juego** — no hay campo de radio en `paragonGlyphs`. Tres a uno a favor del 25, pero no lo doy por cerrado. **Míralo en el tooltip del glifo. Tu pantalla gana.**

**Regla operativa que funciona sea cual sea la respuesta:** corre Fosos **≥10 niveles por encima del nivel de tu glifo** y **sin morir**. Sube **todos** los glifos relevantes al primer breakpoint de radio antes de subir ninguno a 51.

### El orden de gasto, textual de Maxroll

| Fase | Masterworking | Glifos | Míticos |
|---|---|---|---|
| **Tormento 1, Foso 10-14** | **"don't bother with Masterworking yet"** | *"Level relevant Glyphs to level 25 for the extra range"* | — |
| **Tormento 5, Foso 40** | *"Masterwork the rest of your items to 25 Quality and start funneling Masterworking Capstone Bonuses"* | *"Get your main Glyph(s) to 51 for the Legendary Bonus"* | — |
| **Tormento 10, Foso 80+** | Capstones en los afijos relevantes | *"Keep farming the Pit to upgrade your glyphs beyond level 51"* | *"Farm Resplendent Spark / Mythic Uniques in Boss Lairs"* |

> **No gastes Obducita hasta Tormento V.** En Tormento I el equipo que llevas se va a reemplazar entero. **Maxroll lo dice con esas palabras.** — [Maxroll — Endgame Progression](https://maxroll.gg/d4/meta/endgame-progression) (09/07/2026)

**Masterworking, números vivos:** rango máximo **25**, **+1% por rango** a daño base, armadura, resistencia y **todos los afijos**, **capstone en el 25** (*"+50% bonus to a random affix"*), coste por rango `floor(3.75 × CurrentQuality + 10)` → de **10** a **100**, total **492–1.366** de Obducita. **Confianza: alta**, aunque la página que los publica es del **23/05/2026, anterior al parche 3.1.0**.

⚠️ **Rerodar el capstone: conflicto de tres cifras.** Maxroll dice **10.000.000 de oro**; Icy Veins dice **1.000 Obducita + 1 Neathiron + 1.000.000 de oro**. **Nadie coincide. Míralo en la interfaz del Herrero.**

**Mejores fuentes de Obducita** ([Maxroll — Optimal Farming, 03/07/2026](https://maxroll.gg/d4/meta/optimal-farming-guide)): **~350/minuto** desde un **Strongroom** en Tormento 12 · **~330/minuto** en la **Subciudad de Kurast** con Greater Tribute en Tormento 12.

### El olvido de "9.230 de armadura" y los "35.000 de Dureza"

**No existe ninguna tabla de armadura/resistencia/dureza por Tormento en S14, ni de Blizzard ni de Maxroll.** Se buscó expresamente en cuatro páginas. **La pregunta ya no tiene respuesta, no es que falte el dato.**

Lo vigente ([Maxroll — In-depth Defense Guide, **16/08/2026**](https://maxroll.gg/d4/getting-started/defenses-for-beginners), la página más fresca de todo el dossier):

- **Ya no hay topes por dificultad.** Es un sistema de *rating* con rendimientos decrecientes desde la Temporada 11.
- `DR% from Armor = Armor / (Armor*10/9 + Constant)` · **Constante de Armadura a nivel 70: 5.678** · **Constante de Resistencias: 1.136** · techo asintótico del **90%**.
- Sobre la **Dureza**: la propia guía la declara *"not real"* como métrica única. Sirve para comparar builds, no como objetivo.

**Perseguir "9.230 de armadura" ya no significa nada.** Era el tope duro de un sistema que ya no existe. Los "2000/5000/15000/35000 de Dureza" que circulan salen de una página de Icy Veins que **sigue creyendo que solo hay 4 Tormentos**.

**Tus únicos objetivos numéricos vigentes** ([Maxroll — Minion Necromancer, 22/07/2026](https://maxroll.gg/d4/build-guides/minion-necromancer-guide)):

> **100% Velocidad de Ataque** (*"number one priority"*) · **100% Prob. de Crítico** · **30.000 de Vida** · **40+ acumulaciones de Resolución** (solo en la variante híbrida)

---

## Los sistemas nuevos, en orden de rentabilidad

**Dos ordenaciones distintas, porque no coinciden.** La primera es "qué te rinde más por hora invertida". La segunda es el orden en que puedes tocarlos, que te lo imponen las campañas.

### Por rentabilidad pura

| # | Sistema | Rentabilidad | Por qué |
|---|---|---|---|
| **1** | 🆕 **Planes de Guerra** | **MÁXIMA** | Es el único sistema que **modifica a todos los demás**. Sin él, la Subciudad y las Mareas Infernales rinden en modo base. Y contiene el multiplicador más grande de tu progresión: **hasta +4 oportunidades de mejora de glifo por carrera del Foso** (de 5 a 9, un +80%). Maxroll lo llama *"incredibly important for character progression"* |
| **2** | 🆕 **Subciudad de Kurast** | **MUY ALTA** | **Es la única actividad del juego donde eliges el botín antes de entrar.** Carreras de 60–120 segundos, el ciclo más rápido que existe. **Tribute of Heritage** = Únicos **de tu clase**; **Tribute of Titans** = llaves de jefes de guarida; **Tribute of Growth** = XP; **Tribute of Harmony** = Runas. Es un grifo dirigible, no una tragaperras |
| **3** | 🆕 **Talismán / Charms** | **ALTA, pero lenta** | El **5-set de Black Shroud** es el mayor salto de poder que nombran las guías. **Pero** completar un 5-set es el chase más largo del juego, y los Charms **son lo primero que se reinicia en temporada nueva**. Objetivo realista: **Sello Legendario con el afijo "+1 Charm Slot" → 6 ranuras**. Maxroll: *"Legendary Seals are your bread-and-butter for most of the endgame"* |
| **4** | 🆕 **Mercenarios** | **MEDIA — y la mitad de su valor se te cae en dúo** | Barato, rápido, y el **Rapport es de cuenta por tipo de reino** (te sirve para la S15). **Pero el Contratado no aparece cuando juegas en grupo** (ver §El dúo). En solitario es una subida sólida; en dúo solo tienes el Refuerzo |
| **5** | 🆕 **Palabras Rúnicas** | **MEDIA — barata y con un truco** | Solo **2 palabras rúnicas por personaje** (4 runas), así que el techo es bajo. Pero es gratis de montar y **`Igni + Wat` te libera un hueco de barra**: aplica Decrepitud automáticamente y **la Doncella de Hierro deja de necesitar estar en la barra**. Además, la Subciudad con **Tribute of Harmony** es el grifo, así que va gratis con el sistema #2 |
| **6** | 🆕 **Cubo Horádrico** | **MEDIA-BAJA hoy, ALTA en tres semanas** | Es el taller de min-max (reroll de afijos, Afijos Mayores, transfiguración) y la fábrica de Míticos. **Pero no rinde hasta que tengas Fragmentos de Pandemónium y Únicos de 850+.** Su valor sube en línea recta con tu Tormento |
| **7** | 🆕 **Ciudadela Oscura** | **BAJA — una pasada semanal, nunca más** | **No es un motor de farmeo.** La única razón real para entrar es el **Prisma Disperso** (abre engarces en equipo Ancestral), que el fichero lista como *"frequently found"* en solo dos sitios: **Jefes de Mundo y Ciudadela Oscura**. Mínimo 2 jugadores y **la dificultad no escala con el número de jugadores** |
| **—** | **Renombre / Tenets / Chronicles** | **CERO** | Ver corrección #4 de la §0. En temporada no dan puntos |

### Por orden en que puedes tocarlos (las puertas te lo imponen)

```
Campaña VoH cap. 2 ──► MERCENARIOS
Campaña VoH (misión prioritaria) ──► SUBCIUDAD DE KURAST
Campaña VoH completa ──► PALABRAS RÚNICAS
LoH, antes del barco a Temis ──► TALISMÁN / CHARMS   ← muy pronto, no lo pases de largo
LoH completa ──► CUBO HORÁDRICO + PLANES DE GUERRA
Foso 10 → Tormento I ──► CIUDADELA OSCURA + árbol de Jefes de Guarida
```

**El conflicto entre las dos ordenaciones se resuelve solo:** lo más rentable (Planes de Guerra) está detrás de la puerta más cara (terminar LoH). **Por eso el paso 8 de las primeras dos horas es "empieza la campaña", no "empieza a farmear".**

### Detalle de lo que más te rinde

#### Planes de Guerra — los nodos que importan

**El Foso** (inversión directa en glifos):
- **Choron's Blessing** — *"Gain +1 Glyph Upgrade Chance for completing The Pit."*
- **Choron's Haste** — *"+1 Glyph Upgrade Chance for every 5 minutes left on the Timer"*
- **Heart of Stone** — *"+1 Glyph Upgrade Chance"* al depositarlo
- ⚠️ **Pit Butcher** — *"you **fail the run** if he kills any player"*. **En dúo esto es el doble de peligroso.** No lo cojas mientras juguéis juntos

**Marea Infernal** (XP de Paragón):
- **Hellmouth** → **Writhe and Rot**: *"Hellwyrms will always spew **Maggots** that gain +1 Monster Power. Sometimes, a **Pang of Duriel** will also crawl forth. **Lair Keys** often burst out of Pangs of Duriel."* XP **y** llaves a la vez
- ⚠️ **Evita meter Hordas Infernales en el plan**: *"they take much longer to complete compared to other activities"* — [Icy Veins](https://www.icy-veins.com/d4/news/fastest-diablo-4-season-14-leveling-route/)
- Cambio de S14: el progreso de Marea Infernal se cuenta ahora **por cenizas recogidas**, no por cofres: **75** en Normal→Penitente, **300** en Tormento 1+

**Jefes de Guarida** (Míticos y llaves):
- **Lair of Plenty** — *"+1 Hoard Chest when you slay a Lair Boss"*
- **Lair of Runes** — *"higher chance of dropping specific Runes"*. **Es la única mecánica documentada que dice runas *específicas***
- **Duriel's Invasion / Children of Zir / Blood of Bartuc / …** — meten a un jefe dentro de otra actividad **sin gastar llave**
- **Ultimate Nemesis** — acepta **3 Superior Lair Keys** → *"10 Hoard Chests worth of Items"*

**Susurros** — se **solapan** con cualquier otra actividad (*"Whispers can double up with any activity selected"*), así que sus nodos son lo más barato del sistema: **Wisdom of Whispers** (+50% orbes de XP) y **Resplendent Favor** (probabilidad de **Chispa Resplandeciente** en cada alijo).

**Marcas de El'Druin:** sincronizar el tablero con todo el grupo cuesta **2 Marcas**, requiere que **todos estén en Temis** y **aceptación unánime**. Confianza alta. El coste de rehacerlo en solitario (¿1?) y el tope de acumulación (¿3?) **solo salen en fuentes no preferentes**.

#### Subciudad — los tres tributos que te importan

| Tributo | Qué da (texto literal del fichero) | ¿Fuera de Tormento? |
|---|---|---|
| **Tribute of Heritage** | *"Uniques **specific to your class**"* con Sintonía Rango 1 | ✅ Todas las dificultades |
| **Tribute of Growth** | *"Earn **Experience**"* | ✅ Todas |
| **Tribute of Titans** | *"Earn **Lair Boss Hoard Keys**"* | ❌ Solo Tormento |
| **Tribute of Harmony** / **Greater** | Runas / **Runas Legendarias** | ❌ Solo Tormento |
| **Tribute of Refinement** / **Greater** | **Obducita** / **Neathiron + Obducita + Pergaminos** | ❌ Solo Tormento |

**El modelo real son DOS relojes distintos:** el **Tiempo** (120 s sin tributo, **75 s** con tributo Raro, **60 s** con Legendario — sí, **mejor tributo = menos tiempo**) y la **Sintonía** (*"dictates how many rewards you receive"*). El botín solo se entrega al final, tras el Jefe de Distrito.

⚠️ **Nombres de tributo que YA NO EXISTEN** (si los ves, esa guía es de 2024): *Tribute of Mystique*, *Tribute of Equipment*, *Tribute of Gold*. Y **si una guía te habla de "Fuego Sagrado" o "Aether" en la Subciudad, está mirando otra versión**: el Aether vive en las **Hordas Infernales**.

#### Cubo Horádrico — la ventana que se cierra el 15 de septiembre

**La receta ya no se llama "Upgrade": se llama "Craft Mythic"** (renombrada en el 3.1.2). Coste vivo: **1 Único de 850+ de poder de objeto + 4 Fragmentos de Pandemónium**. **Confianza: alta (nota oficial 3.1.1, 14/07/2026).** ⚠️ Maxroll publica **5** en una página del 16/07 — quedó obsoleta dos días antes de publicarse.

**Lo que hay que entender, porque es lo caro:**

> *"This completely randomizes the item gained, meaning it **does not retain Greater Affixes, Affixes, nor is it guaranteed to be the same item**."* — [Maxroll](https://maxroll.gg/d4/resources/horadric-cube)

**Es una tragaperras por ranura.** El objeto de entrada solo decide la **ranura**, nada más. **Corolario: mete siempre el Único más basura que tengas de 850+ en esa ranura.** Meter uno con Afijos Mayores buenos es quemarlo para nada.

**El bucle que se te abre hoy:** Cubo (4 fragmentos) → Mítico al azar → si no sirve, **desguazarlo en el Herrero** → **1 Chispa Resplandeciente** → **2 Chispas = 1 Mítico ELEGIDO** en el Joyero. El 3.1.2 arregló que los Míticos no se pudieran reciclar, así que el bucle está operativo.

**Aritmética sólida:** hasta **2 Fragmentos por Corrupted Reaper** escalando con el Tormento → **~2 kills = 1 Mítico crafteado**.

🔮 **Aviso oficial para la S15, del mismo hotfix 3.1.1a:** Blizzard quitará el crafteo de Mítico por re-roll del Cubo y lo sustituirá por **una mejora directa que conserva el Único original**. Y los **Fragmentos de Pandemónium son moneda de temporada** (`S14_Seasonal_Currency`): **no viajan a la S15**. **Gástalos todos antes del final.**

**Los 8 polvos primordiales** (para cuando llegues al min-max fino): **Attuned** = rerolear el valor del poder de un Único · **Resonant** = *"upgrade a random affix into a Greater Affix"* · **Refined** = cambiar o quitar afijos (su tasa de caída *"has been increased significantly in Torment VII and above"* desde el 3.1.0).

⚠️ **No metas un Mítico bueno en Transfigure.** El **Entropic Tuning Prism** dice literalmente *"Has a 100% chance of making an item Unmodifiable"*. Un Mítico marcado así no se puede seguir puliendo.

#### Charms — el debate que nadie ha resuelto y que vas a resolver tú

Las guías recomiendan **Peace of the Black Shroud** de forma unánime. **Su razonamiento publicado es falso.** Maxroll dice *"all the skills are also Darkness skills"*, y las etiquetas del fichero lo desmienten:

| Habilidad tuya | Etiquetas reales | ¿Darkness? |
|---|---|---|
| Skeleton Warrior | `Summon, Corpse, Physical, Minion` | ❌ No |
| Skeleton Mage | `Summon, Minion, Core, Damage` | ❌ No |
| Golem | `Unstoppable, Summon, Macabre, Cooldown, Minion` | ❌ No |
| Army of the Dead | `Summon, Crowd Control` | ❌ No |
| Corpse Tendrils | `Profane` | ❌ No |
| Iron Maiden | `Profane, Physical, Essence` | ❌ No |

**Ninguna habilidad de esbirros lleva la etiqueta `Darkness`.** El (5) piezas de Black Shroud funciona **por tipo de daño**, no por etiqueta: *"You deal 175%[x] increased **Shadow and Cold** damage"*. Con tus **Magos de Sombra** sí entra. Con tu **Gólem de Sangre** probablemente no. Con Tentáculos y Doncella, no.

**Y existe un set con etiqueta de esbirros que ninguna guía compara:**

**Rathma's Waking Touch** (`Talisman_Necro_05`), texto literal del fichero, corroborado independientemente por game8:
- **(2)** Tus **Esbirros infligen 60%[x] más daño** y reducen el enfriamiento de **Ejército de los Muertos en 1 s** cada vez que dañan
- **(3)** El **35% del daño que recibes se redirige a tus Esbirros**
- **(5)** **Ejército de los Muertos inflige 450%[x] más daño.** Mientras esté activo, los esbirros tienen **+100%[x] Vida** y **+25%[+] Velocidad de Ataque**

**Por qué te interesa especialmente:** llevas **Unyielding Commander**, y la propia guía de Naz Mages dice que con esa variante *"the benefits from Unyielding Commander will be **constantly active at all times**"*. El (5) de Rathma's está condicionado precisamente a *"While Army of the Dead is active"*.

**No estoy diciendo que Rathma's gane.** Digo que **nadie ha publicado la comparación** — ni Maxroll, ni Icy Veins, ni game8. **Recoge los dos.** Los Set Charms se rerolean **dentro del mismo set** en el Cubo, así que los duplicados se convierten en las piezas que te faltan.

**La prueba que lo zanja**, cuando tengas 4-5 piezas de uno: maniquí de entrenamiento, 5 de Rathma's con y sin AotD activo, luego 5 de Black Shroud, comparar. **Es la única forma honesta.**

**🚨 Y una trampa grande:** *"Unique Charms provide the power of their respective Unique item"* es lo que dicen todas las fuentes. **Es falso.** El fichero guarda **dos afijos distintos** por cada único, y no coinciden:

| Único | Versión OBJETO | Versión CHARM |
|---|---|---|
| **Will of Rathma** | Afligidos reciben **40%** más daño | Afligidos reciben **20%** más daño |
| **Pact of Bone** | Esbirros ganan 30-35%[+] Vel.Ataque y Crítico; al morir uno, los demás infligen 30-35%[x] más | Esbirros **infligen 15-25%[+]** más daño; al morir uno, los demás ganan 20-35%[+] Vel.Ataque y Crítico |
| **Red Blessing** | **2** de Sobrepoder máx. | **4** de Sobrepoder máx. ⚠️ conflicto sin resolver |

**No puedes deducir lo que hace un Charm Único mirando el objeto.** Y **Red Blessing** —que Icy Veins pone el primero de su lista ofensiva— tiene el objeto nerfeado de 4 a 2 en el 3.1.0 y el charm todavía en 4. **No sé si es tuneo aparte o un afijo sin parchear. Míralo en el tooltip.** Además, con el nerfeo de Dominate, **Red Blessing es el charm con más probabilidad de estar sobrevalorado en las guías. No lo persigas primero.**

🔍 **Al buscar en el juego:** el sistema escribe *"Rathma's **Walking** Touch"* en los afijos de Sello, pero el set se llama *"Rathma's **Waking** Touch"*. **Es una errata en las cadenas del juego y las dos grafías conviven.** Prueba las dos.

#### Mercenarios — quién y con qué

**Contratado (en solitario):** **Raheir**, montaje que se reconstruye nodo a nodo y cuadra en los 4 puntos exactos:
1. **Ground Slam** (Core rama B) — ralentiza 30/60%, **no dispersa** (Shield Charge sí; por eso no cojas esa rama)
2. **Raheir's Aegis** — **+15% Resistencia a Todos los Elementos**
3. **Bastion** — redirige **90%** del daño de aliados cercanos 5 s
4. **Inspiration** — enemigos con Ground Slam **reciben 15%[x] más daño**; aliados con Bastion **infligen 25%[x] más**

Perk gratis: **Valiance** (anula un golpe de ≥15% de tu vida, CD 30 s).

**La distinción que decide todo y que ninguna guía hace explícita:**

| Familia | Ejemplo | ¿Beneficia a tus esbirros? |
|---|---|---|
| **Debuff sobre el enemigo** (*"los enemigos reciben X% más daño"*, Vulnerable) | Inspiration (1ª mitad), Loaded Munitions, Recklessness | **Sí, sin ambigüedad.** El enemigo recibe más daño de cualquier fuente |
| **Buff sobre "ti"** (*"**tú** infliges X% más daño"*, +Vel. Ataque) | Mocking Lure, Rampage, Hysteria, Bloodlust | **No se sabe.** Depende de si los esbirros heredan tus multiplicadores, y **nadie lo ha escrito** |

**Por eso Raheir con Inspiration/Ground Slam es la apuesta segura**: su valor está en el lado del debuff, no en el del buff. **Y no recomiendo Varyana pese a Icy Veins**: su valor es Velocidad de Ataque **para ti**, y tú no eres quien pega.

**Dato duro que corta por lo sano:** *"Mercenaries are **not minions or companions**, any effects referring to those categories do not apply"* — [PureDiablo](https://www.purediablo.com/diablo4/Mercenaries). **Tu Unyielding Commander y tus rangos a Guerrero/Mago no tocan al mercenario.**

**Orden de subida de Rapport:** **Aldkin a IV** (para desbloquear *Field of Languish*, que es Icónica) → **Raheir a IV** → **Subo a V** → **Varyana**.

⚠️ **Corrección al modelo de Trueque:** las tres guías comparten un marco simplificado —"un mercenario, una categoría de aspecto"— que **el fichero desmiente**. Existen los **Acuerdos Comerciales** (`Mercenary_Contract_*`), que rompen la exclusividad: **los cuatro mercenarios ofrecen Masterworking, Prismas Dispersos y Aspectos Ofensivos**. Y *"It **does not guarantee stock** of these items"* — **no hay vía determinista para ningún aspecto**.

#### Runas — el techo es bajo pero es gratis

**Huecos: Casco 2, Pecho 2, Piernas 2, Arma a Dos Manos 2.** Anillos y amuleto: 1 (solo gemas). **Máximo 2 palabras rúnicas por personaje = 4 runas.** **Confianza: alta, tres fuentes incluida la oficial.**

**Ponlas en ARMADURA, no en el arma.** *"Weapon Gems offer powerful multiplicative damage bonuses"* — el mandoble lleva 2× Amatista Horádrica Impecable en las seis variantes del planificador de esbirros de Maxroll.

**Lo que monta el planificador de Maxroll (22/07/2026), variantes Warrior y Mages — las tuyas:**
> **Nagu + Que** (Casco, sobre *The Undercrown*) · **Igni + Ceh** (Pecho)

`Nagu` genera Ofrenda **solo por tener esbirros vivos** — es la runa de Ritual hecha a tu medida. `Ceh` invoca un Lobo Espiritual que *"now benefits from Summon and Companion bonuses"*, o sea que **escala con tus bonus de esbirros**.

**El desacuerdo entre casas, declarado:** **el planificador de Maxroll no lleva ni un Teb ni un Wat en ninguna de sus 6 variantes** (verificado a mano sobre el JSON, 214 ítems). **Las tres guías de esbirros de Icy Veins montan `Igni + Wat`** como pieza de endgame. **Mi informe de runas dijo que "ninguna guía de esbirros los usa" y eso es falso: tres las usan.**

**Y la recomendación estaba invertida.** Yo dije *"Igni + Wat solo si abandonas la Doncella de Hierro de la barra"*. Las guías dicen lo contrario:
> *"Iron Maiden and Decrepify are activated via Blood Moon Breeches and via Wat Runeword **so they are not needed on the skill bar**."* — [Reaper Summoner](https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/)

**`Igni + Wat` es lo que te LIBERA el hueco de barra que hoy ocupa la Doncella de Hierro.** No es un peaje: es la ganancia.

**Y el argumento con que descarté Wat también era falso.** Dije que Blood Moon Breeches ya reparte las maldiciones. El afijo real dice: *"Your Summons have a **[7-10%] chance** to **randomly** inflict Decrepify **or** Iron Maiden"*. **7-10% y encima elige al azar entre las dos. Es una lotería, no un sistema de reparto.** Y la propia Maxroll escribe: *"the combo of Teb/Wat runes make for **better Curse uptime and more consistent automation**"*.

**🚨 La runa temática de esbirros ya no existe.** `Ur` (*"tu esbirro mata a un enemigo o muere"*) **fue eliminada del juego**. Confirmado en fuente oficial: *"Fixed an issue where **the removed Ur rune** was still required to craft Yul runes"*. Sigue apareciendo en el fichero de datos, en diablo4.life, en d4planner.io y en la hoja de crafteo de Maxroll. **Todas esas listas están muertas en ese punto.**

**Dos trucos que valen dinero:**
- **Amalgama toda la basura:** 5 Mágicas cualesquiera → 1 Rara; 5 Raras → 1 Legendaria (Cubo Horádrico)
- **No tires ningún Teb.** Aunque no lo uses, **1× Teb es la semilla para craftear `Igni`**, que sí es endgame de esbirros. Igual `Gar` → `Vex`

---

## El dúo

**Regla que te cambia el plan del día:**

> **El mercenario Contratado NO aparece cuando juegas en grupo.** En dúo solo funciona el **Refuerzo**, y el Refuerzo **no usa pasivas ni el Perk**: solo una habilidad activa en versión base, disparada por una condición.

**Confianza: alta.** Cuatro fuentes independientes, incluida la oficial:
- *"**Primary Mercenaries only show up when you are playing solo.**"* — [Wowhead](https://www.wowhead.com/diablo-4/guide/mercenaries-guide)
- *"When playing in a group with other players, **only your Reinforcement Mercenary will remain active**."* — [Wowhead, Reinforcement](https://www.wowhead.com/diablo-4/guide/mercenaries-reinforcement-guide)
- *"Primary Mercenaries do not appear in groups… **There is no party-leader restriction on Reinforcements**."* — [PureDiablo](https://www.purediablo.com/diablo4/Mercenaries)
- Blizzard, de pasada: *"Mercenaries can offer their support… **by Hiring them when playing solo**"*

**Y el mito desmentido explícitamente:** *"'Only the party leader can have a Mercenary.' **False.**"*

**Consecuencia operativa: no cuentes con el 15% de Resistencia a Todo de Raheir para llegar al tope de resistencias si juegas en dúo.** Míralo en la hoja de personaje con grupo y sin grupo.

### Tu configuración de Refuerzo

| Opción | Habilidad | Por qué | CD |
|---|---|---|---|
| **1ª — recomendada** | **Aldkin → Field of Languish** | Consenso de Maxroll y Mobalytics, y **funciona de Refuerzo porque los números están en la habilidad, no en una pasiva**: **Ralentiza 40%** (los enemigos se quedan en la alfombra de esbirros) y **reduce el daño enemigo un 20%** (os protege a los dos) | 20 s |
| **2ª — agrupar** | **Varyana → Ancient Harpoons** | **Atrae y Aturde 4 s.** Agrupar es exactamente lo que le falta a una horda de esbirros | 17 s |
| **3ª — defensa de dúo** | **Raheir → Bastion** | Redirige **90%** del daño de los **aliados cercanos** 5 s. En dúo puede tapar también a tu pareja | 30 s |
| **Descartada** | **Subo, cualquiera** | Todo su valor (el Vulnerable) vive en la pasiva **Loaded Munitions**, y **las pasivas no funcionan de Refuerzo** | — |

**Disparador (Opportunity):** ligarlo a **Tentáculos de Cadáver**. Los enemigos quedan apiñados justo donde caerá el *Field of Languish*, y el enfriamiento encaja con los 20 s de Aldkin.

⚠️ **NO uses el disparador universal *"al usar cualquier habilidad en combate"*.** Mi informe lo llamó *"la alternativa segura, que nunca falla"* y **la refutación demostró que es al revés**: hay reportes en el foro oficial que ligan **exactamente esa opción, exactamente con Aldkin de Refuerzo**, a que el **Contratado se quede sin contratar al reconectar**:
> *"On your Reinforcement, if you have your skill activation set to 'Cast when the player casts any skill in combat' **it causes this**. Change the reinforcement skill to activate on ANY other option and this typically stops happening."* — [foro oficial, 18/05/2026](https://us.forums.blizzard.com/en/d4/t/necromancer-mercenary/255195)
>
> **Confianza: media** (reportes de abril-mayo de 2026, parche 3.0.1, sin respuesta oficial y sin arreglo documentado en ninguna nota de 3.1.x — lo cual corta en las dos direcciones).

**Dos palancas que doblan el valor del Refuerzo, y en dúo el Refuerzo es lo único que tienes:**
- 🆕 **Aspecto de Asistencia** (`legendary_generic_126_x1`): *"Your Reinforcement Cooldown is reduced by **23-33%**[x]. After casting your **Ultimate** Skill, your Reinforcement Mercenary is called."* **Tú llevas Ejército de los Muertos**, que es una Definitiva. Es un segundo disparador gratis. Ranuras permitidas: Yelmo, Peto, Botas, Guantes, Amuleto, Pantalones, Escudo. ⚠️ **Game8 publica "7,7%" para este aspecto: es un número muerto.**
- **Sello Elegance del Talismán**: *"While Elegance Charm equipped, using a Cooldown reduces the Cooldown of your Reinforcement Mercenary by 3 seconds."* (datamining, sin confirmación editorial)

**Truco gratis:** el Refuerzo **gana Rapport aunque no lo invoques nunca**. En dúo, ten siempre alistado al mercenario que te falte por subir.

### Si tu pareja NO ha comprado las expansiones

**Lo que SÍ podéis hacer juntos** — y es más de lo que parece:

- **Nivel 70** (gratis para todos) · **Tormento I a XII** completos · **Paragón** · árbol de habilidades rediseñado · filtro de botín · mapa superpuesto
- **El Foso**, **Mazmorras de Pesadilla**, **Mareas Infernales**, **Hordas Infernales**, **Árbol de los Susurros**, **Jefes de Guarida del juego base**
- **La mecánica completa de la Temporada 14**: las **Rupturas de Pandemónium** *"can appear throughout Sanctuary but are more frequent in Helltide Zones"*; las Colossal solo en **Fields of Desecration**, al sureste de Zarbinzet. **Ninguna de esas ubicaciones es de expansión**
- La mayor parte del **Rango de Temporada** (solo *"about 15% of the objectives require Lord of Hatred"*)
- **Grupo máximo 4**, **botín personal por Smart Loot** — jugar juntos **no os divide el botín**

**Lo que NO puede hacer:**

| Bloqueado | Consecuencia real para el dúo |
|---|---|
| 🆕 **Planes de Guerra** | **La asimetría más grande de todas.** Tú tendrás **hasta 9 oportunidades de mejora de glifo por carrera del Foso** y tu pareja **5**. Y tú tendrás la XP de Writhe and Rot y ella/él no |
| 🆕 **Talismán y Charms** | **El segundo más grave.** Sin Talismán no hay sets. No puede montar ninguna de las builds estrella tal cual |
| 🆕 **Cubo Horádrico** | No puede craftear Míticos por esa vía. Su única ruta es el **Herrero: 2 Chispas + 50.000.000 de oro**, que es *mucho* más lenta |
| 🆕 **Palabras Rúnicas** | Sus piezas solo aceptan gemas |
| 🆕 **Mercenarios, Subciudad, Ciudadela Oscura, Nahantu** | Contenido de VoH |
| 🆕 **Skovos, Temis, Echoing Hatred, Belial, Astaroth, Paladín, Brujo, Spiritborn** | Contenido de LoH / VoH |

**Qué hacer en ese caso, en concreto:**

1. **Que monte lo que tú llevas hoy**: **Gravebloom (3 gólems) + Coven + Master of Puppets**, con Magos de Sombra y Guerreros Segadores. Funciona sin expansión y es exactamente el punto del que tú vienes.
2. **NO le pases la guía de Naz Mages ni la de Reaper Summoner.** Le pedirán Charms que no puede equipar y se frustrará sin entender por qué.
3. **Si compra, que compre solo Lord of Hatred**: VoH viene dentro.
4. **Decidid esta semana, no la que viene.** Quedan 27 días y hay que hacer **dos campañas** antes de tocar nada.
5. **La Ciudadela Oscura queda fuera para los dos**: requiere VoH y mínimo 2 jugadores.

### Si tu pareja SÍ tiene las expansiones

- **Los dos sois Nigromantes: cada Set Charm duplicado que le caiga a uno es una pieza que le falta al otro.** Combinado con el reroll del Cubo, **cerráis sets al doble de velocidad**. Es la mejor situación posible.
- **Charms y Sellos no míticos son intercambiables** (el 3.0 arregló que no lo fueran). De los míticos, **no se sabe**.
- **Las runas son intercambiables** entre jugadores.
- **Sincronizad el tablero de Planes de Guerra en Temis**: 2 Marcas de El'Druin, aceptación unánime.
- **Ciudadela Oscura**: es la **única** forma de hacerla (mínimo 2). Pero está diseñada para 4 y **la dificultad no escala**. Con dos nigromantes y uno principiante, esperad muro.
- ⚠️ **No uséis Tributos "Resolute"** en la Subciudad estando en grupo: *"**Resolute Tributes reward only the Player who offers the Tribute**"* (texto literal del ítem).
- ⚠️ **Si alguno crea un personaje Solo Self-Found (modo nuevo de S14), no podéis jugar juntos con él**: *"SSF characters **cannot join parties or trade** with other players"* — Blizzard, blog de S14.

**Lo que no sé y os afecta:** si la sincronización de Planes de Guerra funciona cuando un miembro no tiene LoH; si la Ciudadela Oscura exige que **todos** tengan VoH; y si acompañar a alguien en su campaña **acredita la tuya** (es decir, si tenéis que hacer las campañas una vez o dos). **Ninguna fuente lo aborda.** Y hay un bug reportado de agrupación **incluso teniendo ambos la expansión** ([foro US, 09/05/2026](https://us.forums.blizzard.com/en/d4/t/cant-play-with-friend-in-new-expansion-lord-of-hatred/251798), sin respuesta azul).

---

## Lo que queda de temporada

**Aviso previo, y va en serio: ninguna fuente preferente publica estimaciones de tiempo.** Se buscó expresamente. Todo lo que circula viene de **webs de venta de servicios de boosting** (timesaver, mmoexp, mmogah), que tienen incentivo comercial para exagerar. *"Torment 4 en 1h15"*, *"Torment 7 en 7 horas"*, *"Tormento 12 el segundo día"*: **ignóralas todas.** El único cronómetro fiable que tienes es el de **15 minutos del Foso**.

Con esa reserva puesta, y sabiendo que **las dos campañas se comen un trozo grande de la primera semana**:

### Realista en 4 semanas

| Objetivo | Por qué es realista |
|---|---|
| **Las dos campañas terminadas** | A nivel 70, línea recta y sin cinemáticas, no ganas nivel: solo desbloqueos. Es trámite, no proyecto |
| **Los tres árboles de Planes de Guerra que importan** (Foso, Marea Infernal, Subciudad) | 7 niveles por árbol, 1 punto por nivel. Cargando Escalada y Marea Infernal en los planes vas 3,4× más rápido |
| **Tormento VI–VIII** | T6 = Foso 40 (llaves de guarida), T8 = Foso 60. Es donde el botín empieza a merecer la pena de verdad. **No tengo base para prometer más** |
| **Rango de Temporada 5–6** | Rango 5 = cualquier Jefe de Guarida en T4+ (**+10 Paragón**). Rango 6 = Corrupted Reaper en T6+ (**+8 Paragón + 1 Chispa**) |
| **Glifos principales a 51** | Con 9 oportunidades por carrera del Foso en vez de 5, el ritmo cambia mucho |
| **Sello Legendario con "+1 Charm Slot" → 6 ranuras** | *"Legendary Seals are your bread-and-butter for most of the endgame"* — Maxroll |
| **Un 5-set de Charms** (Black Shroud o Rathma's) | Gracias al **reroll de Set Charm en el Cubo**: los duplicados se convierten en las piezas que faltan. Es el mecanismo que lo hace posible |
| **2–4 Míticos crafteados** | ~2 kills de Corrupted Reaper = 4 Fragmentos = 1 craft. **Y el límite de "un solo crafteado equipado" ya no existe** |
| **Masterworking a 25 en las piezas clave** | Solo a partir de Tormento V. Prioriza **armas** (su daño base sube con cada rango de calidad) |
| **Tu Nigromante configurado para la S15** | Gargantua aprendido, tableros correctos, saber qué charm y qué runa. **Lo que no se reinicia es saber qué elegir** |

### NO realista en 4 semanas

| Objetivo | Por qué no |
|---|---|
| **Tormento X–XII** | T10 = Foso 80, T12 = Foso 100. Con Paragón desde 0 y equipo por hacer, no |
| **Paragón 300** | 342 puntos totales es el techo teórico de una temporada entera bien jugada |
| **Seal of the Diamond Mind** | Cae en **Tormento 10+**. Es el techo del sistema |
| **Dos sets de 5 Charms simultáneos** | Necesita Diamond Mind (que necesita T10+) |
| **Echo of Mephisto (Rango 8)** | Exige **Tormento X+** |
| **Foso 150** | Ni de lejos |
| **Cambiar a Naz Mages desde cero** | Giro a frío + 2 Únicos que no tienes + un anillo pilar recortado un 33%. **Es tu objetivo de S15, no de agosto** |
| **Perseguir el 5-set en la última semana** | Los Charms **son lo primero que se reinicia** en temporada nueva |

### La regla de oro para estas 4 semanas

**Gasta el tiempo en lo que se acumula, no en lo que se reinicia.** Lo que se acumula: Paragón, glifos, Rapport de mercenario (es **de cuenta por tipo de reino**), y sobre todo **saber qué elegir**. Lo que se reinicia: charms, equipo, fragmentos de temporada.

**Y una excepción a esa regla:** los **Fragmentos de Pandemónium son moneda de temporada y no viajan a la S15**. **Gástalos todos, hasta el último, antes del final.** Además, Blizzard ya ha anunciado que en la S15 **quitará el crafteo de Mítico por re-roll del Cubo**. Esa lotería barata por ranura es **una ventana que se cierra**.

### Lo que se sabe de la S15

| Cambio en el PTR 3.2.0 (corrió del 04 al 11/08/2026) | Impacto |
|---|---|
| **Escalar de estadística principal del Nigromante: de 1.25 a 1.625** | El fichero confirma que el valor **vivo hoy** es `damageScalar: 1.25`. Es un **+30%** a la conversión de Inteligencia en daño. **Buena señal para la clase** |
| **Glifo nuevo: Superiority** — *"+30% bonus to all magic Nodes within range"* | Mismo arquetipo que Deadraiser/Amplify |
| **Mazmorras de Desafío** — elegir dificultad *"up to three Torment tiers above"* la actual | — |
| El crafteo de Mítico del Cubo se sustituye por **una mejora directa que conserva el Único original** | Anunciado en la nota del desarrollador del hotfix 3.1.1a |
| **El PTR NO anuncia subida de nivel máximo** | La herramienta ofrece "Set Level to 70" y "Set Paragon to 200", lo que **sugiere** que 70 sigue siendo el techo. **Es lectura de una herramienta de test, no un anuncio. No confirmado** |

---

## Lo que no se sabe

Explícito y completo. **Nada de esto se ha rellenado por inferencia.** Un hueco declarado vale más que un número con buena pinta.

### Lo que puedes cerrar tú en 30 segundos mirando la pantalla

1. **¿El aura de Gargantua se ve como Velocidad de Ataque en tu hoja de personaje, o solo como Cast Speed?** El fichero dice *Cast Speed*; Icy Veins lo llama *"Attack Speed aura"*; Maxroll lo mete en su FAQ de cómo llegar al 100% de velocidad de ataque. **Nadie lo ha escrito.** Es el hueco con más consecuencias de todo el dossier.
2. **¿El radio del glifo sube en el nivel 15 o en el 25?** Tres fuentes de julio dicen 25, una sin fecha dice 15, y **el dato no existe en el fichero del juego**. Mira el tooltip.
3. **¿El segundo aumento de radio es en 50 o en 51?** Maxroll se contradice consigo misma en la misma página.
4. **¿Red Blessing como Charm tiene 2 o 4 de Sobrepoder máximo?** El objeto dice 2 (coherente con el nerfeo oficial), el charm dice 4. Mira el tooltip.
5. **¿La receta del Cubo pide 4 o 5 Fragmentos de Pandemónium?** Está escrito que 4 (oficial, 3.1.1). Si ves 5 en pantalla, manda tu pantalla.
6. **¿Cuál es el rango máximo de Sintonía en la Subciudad?** Maxroll dice que la barra es *"four-staged"* pero el nodo *Initiative* habla de *"as if your Attunement was 2 higher (max 6)"*. Mira tu barra.
7. **¿Desaparece de verdad tu mercenario Contratado al agruparte, y baja tu resistencia un 15%?** Cuatro fuentes dicen que sí, un jugador del foro lo discute. Mira la hoja de personaje con grupo y sin grupo.
8. **¿La Subciudad de Kurast exige la campaña de VoH, o solo nivel 20 + invocar la Llama Espiritual?** Maxroll y Icy Veins se contradicen. Entra a Nahantu y mira si el Brasero está activo.
9. **¿El botón de "Saltar campaña" aparece de verdad solo al crear personaje?** Solo lo sostienen tres hilos de foro sin respuesta oficial. **Mira la pantalla de selección antes de dar por perdida la tarde.**
10. **¿Cuánto cuesta de verdad rerodar el capstone de Masterworking?** Tres cifras en tres sitios. Está en la interfaz del Herrero.
11. **¿Cuánto cuesta el Mítico elegido en el Joyero?** Tres versiones contradictorias, ninguna oficial. Está en la interfaz del Joyero.

### Preguntas de min-max que nadie ha respondido por escrito

12. **¿Cuál gana en DPS real: Rathma's Waking Touch o Peace of the Black Shroud, para esta build?** **No existe ninguna comparación numérica publicada.** Ni Maxroll, ni Icy Veins, ni game8, ni foros. Es la decisión más grande del sistema de Charms y la tienes que tomar tú con el maniquí.
13. **¿Los esbirros del Nigromante heredan los multiplicadores del jugador?** Es decir: cuando un mercenario o un charm dice *"**tú** infliges X% más daño"*, ¿lo cobran tus magos y guerreros? **Ninguna de las tres guías de S14 lo aborda.** Esta es la incógnita que más valor tiene sin resolver: decide qué mercenario, qué glifos y qué afijos merecen la pena.
14. **¿De qué tipo de daño son los Guerreros Segadores y el Ejército de los Muertos?** Sin eso no se puede decir si cobran el **175%[x] de Sombra y Frío** del 5-set de Black Shroud.
15. **¿La variante Unholy Frenzy de Decrepify apila con Gargantua?** Llevan **la fórmula idéntica** (`0.2*Table(34,sLevel)*100`, Cast Speed + Movement Speed a los esbirros). **Ninguna guía la menciona.** Lo único escrito es que en el 3.1.0 se arregló un bug por el que *"taking the Unholy Frenzy Variant of Decrepify would cause Iron Maiden to fail to apply to enemies"*.
16. **¿Puede el Joyero craftear Míticos NO icónicos** (Únicos de clase como Pact of Bone o The Undercrown con calidad Mítica) **o solo la lista de 14 icónicos?** **Es la pregunta que decide toda tu estrategia de min-max** y no hay respuesta escrita.
17. **¿Qué probabilidad tiene cada Mítico dentro de una ranura al usar Craft Mythic?** Nadie publica la tabla.
18. **¿Cuánto daño hace exactamente la Doncella de Hierro de `Teb` y cuánto Debilita la Decrepitud de `Wat`?** Ninguna fuente publica los números y el fichero solo trae el texto, no las tablas de potencia.
19. **¿Cuánta Ofrenda genera `Nagu` en total con 5 invocaciones** — ¿100 por cada una, o 100 repartidos?
20. **¿Cuánta Obducita da cada actividad y por escalón de Tormento?** La guía lista las fuentes por eficiencia pero *"specific drop quantities per activity are not provided"*.
21. **¿Cuánta Experiencia de Actividad hace falta para cada nivel de árbol de Planes de Guerra (1→7)?** Maxroll publica la XP *ganada*, no el umbral.
22. **¿Cuál es la tabla completa de probabilidad de mejora de glifo por diferencia de nivel?** Solo se han visto los extremos: 100% con +5 de bono a partir de 80 niveles de diferencia, 0% si el Foso está 51+ niveles por debajo.
23. **¿Intentos base de mejora de glifo por carrera: 3 o 4?** Maxroll dice 4, Icy Veins dice 3.

### Sobre el dúo

24. **No existe ninguna página oficial de Blizzard con una matriz de qué se puede hacer en cooperativo sin expansión.** Todo lo de esa sección se apoya en la tabla de contenido de pago de Blizzard más foros oficiales sin respuesta azul. **Es la mayor laguna de todo el dossier.**
25. **¿Funciona la sincronización de Planes de Guerra si un miembro no tiene LoH?**
26. **¿Exige la Ciudadela Oscura que TODOS los miembros tengan VoH?**
27. **¿Acompañar a otro jugador en su campaña acredita la tuya?** Decide si hacéis las campañas una vez o dos.
28. **¿Hay alguna restricción de crossplay PC ↔ PS5 por propiedad desigual de expansión?** Ninguna fuente lo trata.
29. **¿Son intercambiables los Charms y Sellos Míticos?** Solo consta que los **no** míticos sí.

### Conflictos entre fuentes preferentes, sin árbitro

30. **Chispas Resplandecientes del Rango de Temporada: ¿7 (Blizzard) o 9 (Maxroll)?**
31. **Puntos de habilidad del Rango de Temporada: ¿12 (Blizzard) o 14 (Maxroll)?**
32. **Alijos Míticos del Rango de Temporada: ¿5 (Blizzard), 3 o 2 (Maxroll, que se contradice consigo misma)?**
33. **¿Los mercenarios resucitan solos o hay que reanimarlos?** Wowhead dice que solos, Maxroll dice que hincan rodilla.
34. **¿Cuántas runas hay vivas?** Maxroll dice 32, Icy Veins implica 34, el fichero tiene 52 (con entradas muertas confirmadas). **Nadie publica la lista de runas eliminadas** — solo `Ur` está confirmada por nombre.
35. **¿Qué da el Tribute of Radiance?** Maxroll dice "Aspectos"; el fichero dice "Ancestral Legendaries".
36. **¿Cuál es la categoría del Aspecto de Asistencia?** Wowhead no la declara y el fichero se contradice: las etiquetas son `HoradricCube_Legendary_Utility_Mobility` **y** `FILTER_Legendary_Offensive`.

### Sobre el método (léelo, porque calibra todo lo de arriba)

37. **El fichero de datos del juego que sirve el planificador de Maxroll declara `version: 3.1.0.72698`.** El parche vivo es **3.1.3 build 73224**. Está por detrás. **Pero:** la refutación demostró que el fichero (build 72698) es **posterior** al parche 3.1.0 (build 72592) y **contiene el valor post-nerfeo de Dominate** (1,838% recalculado a mano). Así que el fichero refleja al menos el 3.1.0. **Lo que 3.1.1, 3.1.2 y 3.1.3 hayan tocado puede no estar.**
38. **Es datamining, y la cadena de custodia es la misma organización.** El fichero se sirve desde `assets-ng.maxroll.gg`. Llamar a "el fichero" y a "la guía de Maxroll" **dos vías independientes infla la garantía**: son datos crudos del cliente frente a prosa humana, lo cual vale, pero no son independientes.
39. **Cuatro fuentes que el dossier trata como "vigentes de S14" son ANTERIORES al parche 3.1.0 (30/06/2026)**: `difficulty-overview` (26/06) — que sostiene toda la escalera de Tormentos; `masterworking-guide` (23/05) — que sostiene *todos* los números de Masterworking; `item-crafting` (29/06); e Icy Veins Naz Mages (27/06). **Los valores se han verificado por otras vías y aguantan, pero la freshness declarada es optimista.**
40. **Fuentes contaminadas identificadas y bloqueadas** (publican el marco muerto de nivel 60 / 4 Tormentos): **Icy Veins "World Difficulty"** (sin fecha) · **Wowhead "Difficulty & Torment Levels"** (dice Foso 20/35/50/65) · **Maxroll "Shadow Minion Necromancer"** (autodeclarada S4, agosto 2024) · **Maxroll "Paragon Board Selection and Pathing"** (S5) · **Maxroll "Mercenaries Overview"** (11/07/2025) · **Maxroll "Dark Citadel"** (24/04/2025) · **Icy Veins "Dark Citadel"** (dice nivel 60) · **DiabloBytes** (afirma que los mercenarios equipan objetos, que es falso) · **Game8** (Aspecto de Asistencia al 7,7%).
41. **Fuentes que nunca respondieron:** `mobalytics.gg` devuelve **HTTP 403** consistentemente (contenido solo por extractos de buscador); `wowhead.com/diablo-4` sirve solo la cabecera, no el cuerpo; `reddit.com` bloquea al agente — **cuatro pasadas consecutivas fallidas, conviene dejar de intentarlo**. `d4builds.gg` **sí responde HTTP 200** (mi informe declaró 404 y era falso) pero sirve una aplicación JS sin HTML legible.
42. **Las páginas de Wowhead más citadas de todo el dossier están etiquetadas "Season 10" y "Season 12".** Bajo la regla de "solo páginas dentro de 3.1.x", **no cualifican** — y entre ellas soportan la ubicación del Albergue, el atajo Mayús+M, la tabla de Marcas Pálidas y la cita principal de la regla de grupo. Los datos con segunda fuente están confirmados; el resto queda en la palabra de una guía de la Temporada 10.

---

## Anexo: el chequeo de 5 minutos que vale por media investigación

Cuando entres, en este orden:

1. Tienda de la cuenta → ¿pagaste VoH dos veces?
2. Selección de personaje → ¿hay botón de "Saltar campaña"? (probablemente no, pero mira)
3. Árbol de habilidades → Gravebloom fuera, Gargantua dentro, subir rango del Gólem
4. Hoja de personaje → ¿se mueve la Velocidad de Ataque con el Gargantua invocado?
5. Tooltip de un glifo → ¿el radio sube en 15 o en 25?
6. Pestaña de Rango de Temporada → ¿tienes el Rango 2 hecho?
7. Pestaña Engarzables → ¿qué runas tienes ya sin saberlo?
8. Casco → ¿tiene 2 huecos? (si sí, el sistema de runas está activo)
9. Nahantu → ¿está activo el Brasero de Espíritus antes de tocar la campaña?
10. Agrúpate con tu pareja y mira la resistencia con y sin grupo

**Diez respuestas que ninguna web publica y que tú tienes en pantalla. Tu pantalla gana.**
