# Mercenarios (Mercenaries) — Vessel of Hatred · Dominio completo

**Investigado el 19-20 de agosto de 2026.** Parche vivo declarado: **3.1.3 (build 73224, 12/08/2026)**. Temporada 14 "Death Awakening" (desde 30/06/2026).

🆕 **TODO este documento describe contenido que el jugador acaba de desbloquear hoy al comprar Vessel of Hatred.** El sistema de Mercenarios es exclusivo de VoH: sin la expansión no existe ni el sistema ni el acceso al Albergue. Se marca 🆕 igualmente en los puntos donde la distinción base/expansión es operativa.

---

## 0. Titular: la regla que le cambia el plan

> **El mercenario Contratado (Primary / Hired) NO aparece cuando juegas en grupo.** En dúo con su pareja solo funciona el **Refuerzo (Reinforcement)**, y el Refuerzo *no usa pasivas ni el Perk*: solo una habilidad activa en versión base, disparada por una condición.

Esto está confirmado por tres fuentes independientes y desmentido explícitamente el mito contrario ("solo el líder de grupo tiene mercenario"). Detalle y evidencia en la §7. Consecuencia práctica: **la pregunta "¿qué mercenario principal?" solo tiene efecto cuando juega solo.** En dúo lo único que decide es qué habilidad de Refuerzo y con qué disparador.

---

## 1. Estado del parche y fiabilidad de cada fuente (verificación del modelo)

### 1.1 ¿Han tocado los mercenarios en el parche 3.1.x?

| Parche | Fecha | ¿Menciona Mercenary / Reinforcement / Rapport / Pale Mark / Den? | Fuente |
|---|---|---|---|
| 3.1.0 (lanzamiento S14) | 30/06/2026 | **No, ninguna mención** | [maxroll 3.1.0](https://maxroll.gg/d4/news/diablo-4-3-1-0-patch-notes) |
| 3.1.2 (Lord of Hatred) | 28/07/2026 | **No, ninguna mención** | [maxroll 3.1.2](https://maxroll.gg/d4/news/lord-of-hatred-3-1-2-patch-notes) |
| 3.1.3 (build 73224) | 12/08/2026 | **No, ninguna mención** | [notas oficiales Blizzard](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) |
| S14 cambios no documentados | 02/07/2026 | **No, ninguna mención** | [maxroll undocumented](https://maxroll.gg/d4/news/diablo-4-season-14-undocumented-changes) |

La wiki de PureDiablo mantiene un historial de cambios del sistema con una única entrada: **"Patch 2.0, October 8, 2024 — Added in Vessel of Hatred"** ([purediablo](https://www.purediablo.com/diablo4/Mercenaries)). Es decir: **el sistema de mercenarios no ha recibido cambios de balance documentados desde su lanzamiento**. Eso hace que guías antiguas sigan siendo válidas *en el modelo* — pero no en los números concretos, que sí se han movido en silencio (ver 1.3).

Lo único adyacente en 3.1.3: *"Fixed an issue where Impetus and Misanthropic Aspects treated pets and mercenaries as active demons"* — es un arreglo de interacción, no un cambio del sistema ([notas oficiales](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes)).

### 1.2 Fichero de datos del juego (datamining) — con su desfase declarado

He descargado el fichero que sirve el planificador de Maxroll: `https://assets-ng.maxroll.gg/d4-tools/game/data.min.json` (11,6 MB).

- **Campo `version` del fichero: `3.1.0.72698`.**
- **El parche vivo es 3.1.3 / build 73224.** El fichero va **tres hotfixes por detrás**.
- Esto es **datamining**, no documentación oficial. Los textos que saco de ahí son las cadenas internas del juego, lo cual es más fiable que una wiki, pero pueden haberse ajustado entre 72698 y 73224 sin que yo pueda verlo.

Dado que ni 3.1.1, ni 3.1.2 ni 3.1.3 mencionan mercenarios, **el riesgo de desfase en estos valores concretos es bajo, pero no es cero y no lo puedo cerrar**.

Contenido de mercenarios en el fichero: exactamente **4 mercenarios**, claves internas `MercenaryClass_ShieldBearer` (Raheir, id 1454142), `MercenaryClass_BerserkerCrone` (Varyana, id 1456949), `MercenaryClass_CursedChild` (Aldkin, id 1491904), `MercenaryClass_BountyHunter` (Subo, id 1491907). **No hay un quinto mercenario en los datos.** (El mismo fichero sí muestra las clases `Paladin_NEW` y `Warlock` de Lord of Hatred, así que el fichero está al día en contenido de la segunda expansión — refuerza que el roster de mercenarios sigue siendo de cuatro.)

### 1.3 Fuentes que he tenido que descartar o corregir

Esto es importante porque el jugador ya se ha comido dos veces datos muertos.

| Fuente | Problema detectado | Veredicto |
|---|---|---|
| **DiabloBytes** ([enlace](https://diablobytes.com/diablo-iv/guides/mercenaries-guide/)) | La cabecera dice "SEASON 14 · PATCH 3.1.3" pero la firma dice **"Updated May 2026"** — imposible, la S14 empezó el 30/06/2026. Además afirma: *"Their damage output scales primarily off their own equipped gear (which you control via the merc inventory)"* — **falso**: los mercenarios **no pueden equipar objetos**. Y sitúa Nahantu "(Hawezar region)", que tampoco es. | **Descartada.** No he usado ninguna de sus recomendaciones. |
| **Maxroll — Mercenaries Overview** ([enlace](https://maxroll.gg/d4/resources/mercenaries-overview)) | "Last Updated: **July 11, 2025**". Contiene la frase *"you can only hire one Mercenary to join you at a time, solo or in a party (via the Party Leader)"*. Eso es un resto de la **información de Gamescom de agosto de 2024**, previa al lanzamiento (ver el hilo [eu.forums 17859](https://eu.forums.blizzard.com/en/d4/t/voh-mercenaries-only-party-leader/17859), del 21/08/2024, que cita exactamente esa promesa). **El juego lanzado no funciona así.** | **Usada solo para lo que corrobora otra fuente.** La regla del "líder de grupo" está desmentida. |
| **Game8 — Aspect of Assistance** | Publica el valor **"7,7%"** de reducción de enfriamiento del Refuerzo. El fichero de datos 3.1.0 y la base de datos de Wowhead dan **23–33%**. Número muerto. | **Descartada para ese valor.** |
| **Wowhead — Mercenaries Guide** ([enlace](https://www.wowhead.com/diablo-4/guide/mercenaries-guide)) | "Updated: 2025/10/02". Es la guía **más completa que existe** y su modelo se sostiene, pero tiene errores de detalle: llama al perk de Aldkin *"Blasphemous Fire"* (en los datos es **Blasphemous Fate**), escribe *"Fayina"* y *"Fayira"* en la misma página, y dice que el Seeker de Subo restaura *"50% of your Maximum Resource"* cuando los datos dicen **"50 of your Primary Resource"** (cantidad plana, no porcentaje). | **Usada, con los números corregidos contra el fichero de datos.** |
| **Icy Veins — Mercenaries** ([enlace](https://www.icy-veins.com/d4/guides/mercenaries-guide/)) | `dateModified` en el HTML: **2026-06-30**, y el texto dice "Updated for Season 14". Buena, pero superficial: no cubre grupo/dúo ni la ubicación del Albergue. | **Usada como corroboración de estructura.** |
| **PureDiablo — Mercenaries** ([enlace](https://www.purediablo.com/diablo4/Mercenaries)) | Última edición **8 de diciembre de 2025**. Es la única que trata el comportamiento en grupo de forma explícita y con sección de "Common Misconceptions". | **Usada como fuente principal para grupo/dúo.** |

---

## 2. 🆕 Cómo se desbloquean exactamente

### 2.1 ¿Hay que hacer la campaña de VoH? ¿Cuánta?

**Sí, hay que empezarla. No, no hace falta terminarla para tener mercenarios.**

La campaña de Vessel of Hatred es el **Acto VII**, con **4 capítulos y 30 misiones principales** más una línea post-campaña ([Wowhead — VoH Campaign Questline Guide](https://www.wowhead.com/diablo-4/guide/zones/vessel-of-hatred-campaign-guide), actualizada 2025/04/14).

| Capítulo | Misiones | Hito |
|---|---|---|
| Ch 1. *The Art of Salvaging What Remains* | 5 | Contiene *A Magpie in Flight*, donde conoces a Raheir en **Gea Kul** |
| Ch 2. *The Wound Heals, the Pain Lingers* | 10 | **`The Hand that Remembers the Blade` → abre Mercenarios** |
| Ch 3. *A Stairway Carved from Corpses* | 8 | — |
| Ch 4. *False Prophets, Fallen Saints* | 7 | Misión final → permite que los alts salten la campaña de VoH |

Orden exacto del arranque (Ch 1): *Rekindled Faith* → *A Fist of Fire* → *Pursuit of Justice* → **A Magpie in Flight** → *Enmity Rising*. En *A Magpie in Flight* los objetivos son: hablar con Raheir en Gea Kul, buscarlo, entrar en su taller, hablar con él, encontrar el origen del disturbio y derrotar a los Huecos en la puerta este ([mismo enlace](https://www.wowhead.com/diablo-4/guide/zones/vessel-of-hatred-campaign-guide)).

**Conclusión operativa: el desbloqueo cae en el capítulo 2, es decir dentro de las primeras ~6-8 misiones de 30.** No es "termina la expansión": es una tarde corta.

> ⚠️ Conflicto de fuentes declarado: la nota oficial de Blizzard dice *"Upon completing the Vessel of Hatred campaign, Raheir will be available to use in combat"* ([news.blizzard.com](https://news.blizzard.com/en-us/diablo4/24128995/delve-deeper-into-nahantu-with-mercenaries-dark-citadel-and-more)) y d4guides.gg repite *"Mercenaries become available after completing the Vessel of Hatred campaign"*. Eso **contradice** el desglose por capítulos de Wowhead y el hecho de que la misión de Raheir sea la cuarta del capítulo 1. Me quedo con el desglose por capítulos porque es el único que nombra la misión concreta que abre el sistema; pero si en la pantalla el mercenario no aparece hasta el final, la fuente oficial tenía razón y la mía no. **Que lo compruebe en pantalla.**

### 2.2 Misiones de adquisición de los otros tres

Raheir se obtiene por campaña. Los otros tres se desbloquean interactuando con objetos marcados dentro del Albergue, cada uno arranca una *Acquisition Quest*:

| Mercenario | Misión | Objeto que la inicia (en el Albergue) |
|---|---|---|
| Varyana | *Slayer's Retribution* | Nota brutal clavada en una estaca ensangrentada |
| Aldkin | *A Nameless Mystery* | Archivo de Kuo Chosah |
| Subo | *A Feather on the Scale* | Carta embarrada bajo un yelmo de mercenario |

Fuente: resultados de búsqueda agregados (gamingbolt / screenrant / gameranx). **Los nombres de estas tres misiones no los he podido verificar en una fuente preferente con fecha dentro de 3.1.x** — van también en §"No encontrado".

### 2.3 Persistencia y saltos

- *"Once one character finishes the final VoH chapter (Presaged Fate), all alts may hire Mercenaries from level 1."* ([purediablo](https://www.purediablo.com/diablo4/Mercenaries)). Wowhead lo confirma con el mismo nombre de capítulo final, *Presaged Fate* ([wowhead merc guide](https://www.wowhead.com/diablo-4/guide/mercenaries-guide)) — aunque su propia guía de campaña lo escribe *"Presaging Faith"* ([wowhead campaña](https://www.wowhead.com/diablo-4/guide/zones/vessel-of-hatred-campaign-guide)). Dos grafías en el mismo sitio; el hito es el mismo.
- **Mercenarios y Rapport son de cuenta, por tipo de reino** (Estacional, Eterno, Estacional Hardcore, Eterno Hardcore) — no por personaje ([wowhead](https://www.wowhead.com/diablo-4/guide/mercenaries-guide), [purediablo](https://www.purediablo.com/diablo4/Mercenaries)). Lo que suba esta temporada le sirve a cualquier personaje estacional que haga después.
- **Contratar no cuesta oro** ([maxroll](https://maxroll.gg/d4/resources/mercenaries-overview), [purediablo](https://www.purediablo.com/diablo4/Mercenaries)).

---

## 3. 🆕 El Albergue (The Den) — dónde está y qué hay dentro

**Ubicación:** *"The Den, which is located in the Flayer Jungle in the upper northwest corner of Lingering Hatred in Nahantu."* El icono verde en forma de diamante **al noreste del Bazar de Kurast** lleva allí, y al pulsarlo se activa el punto de viaje interior ([wowhead merc guide](https://www.wowhead.com/diablo-4/guide/mercenaries-guide)).

Nahantu es región exclusiva de VoH — de ahí que el sistema entero requiera la expansión ([purediablo](https://www.purediablo.com/diablo4/Mercenaries)).

**Qué hay dentro** ([wowhead merc guide](https://www.wowhead.com/diablo-4/guide/mercenaries-guide)):

| Elemento | Función |
|---|---|
| Los cuatro mercenarios | Contratar (Hire = Contratado) o Alistar (Enlist = Refuerzo). Se cambian pulsando sobre ellos |
| **Fayira** | Vendedora de Trueque (Bartering) con Marcas Pálidas (Pale Marks) |
| Tu alijo (stash) | — |
| **Guide Coffers** | Vendedor de anillos y amuletos |
| **Cursed Toy Box** | Ocultista |
| **Raheir's Anvil** | Herrero |

**Panel de mercenario:** desde el panel de personaje, pestaña de mercenario arriba a la derecha, o atajo **Mayús + M**. Ahí se eligen habilidades y se ven las recompensas de Rapport. **La asignación Contratado/Refuerzo se cambia en el Albergue, no en el panel** ([wowhead merc guide](https://www.wowhead.com/diablo-4/guide/mercenaries-guide)). PureDiablo lo confirma: *"You can't dismiss them in the field"*, y no hace falta despedir antes de contratar a otro: contratar reemplaza automáticamente ([purediablo](https://www.purediablo.com/diablo4/Mercenaries)).

---

## 4. Reglas generales del sistema (verificadas)

| Regla | Fuente |
|---|---|
| **Los mercenarios no pueden equipar objetos.** No hay inventario de mercenario | [wowhead](https://www.wowhead.com/diablo-4/guide/mercenaries-guide) ("VoH Mercenaries cannot be equipped with gear"), [purediablo](https://www.purediablo.com/diablo4/Mercenaries) ("Mercenaries cannot equip gear"). Corroborado negativamente: en el fichero 3.1.0 las entradas `mercenaries` solo tienen `id`, `name`, `skills`, `tree` — no hay campo de equipo |
| **Los mercenarios NO son esbirros ni compañeros.** *"Mercenaries are not minions or companions, any effects referring to those categories do not apply"* | [purediablo](https://www.purediablo.com/diablo4/Mercenaries) |
| Si "mueren" hincan rodilla y dejan de usar habilidades; puedes revivirlos como a un jugador | [maxroll](https://maxroll.gg/d4/resources/mercenaries-overview) |
| Wowhead dice en cambio que *"Mercenaries that die respawn on their own. There's no need to resurrect them."* | [wowhead](https://www.wowhead.com/diablo-4/guide/mercenaries-guide) — **contradicción entre fuentes, sin resolver** |
| No puedes poner al mismo mercenario como Contratado y Refuerzo | [wowhead reinforcement](https://www.wowhead.com/diablo-4/guide/mercenaries-reinforcement-guide), [Blizzard](https://news.blizzard.com/en-us/diablo4/24128995/delve-deeper-into-nahantu-with-mercenaries-dark-citadel-and-more) |
| Puedes llevar uno, los dos, o ninguno | [wowhead](https://www.wowhead.com/diablo-4/guide/mercenaries-guide) |
| **Los mercenarios son invisibles para los demás jugadores.** *"Mercenaries are invisible to other players."* | [purediablo](https://www.purediablo.com/diablo4/Mercenaries) |

### Estructura del árbol — idéntica en los cuatro

Verificada cruzando el fichero de datos 3.1.0 con la descripción de Wowhead; **coinciden nodo a nodo**.

Cada mercenario tiene **dos ramas** que arrancan de una **Habilidad Fundamental (Core)** distinta. La Core determina **el arma y el ataque básico** del mercenario. Dentro de cada rama:

```
Rama A                                   Rama B
├─ Habilidad Core A                      ├─ Habilidad Core B
├─ Pasiva Core: A1 ó A2                  ├─ Pasiva Core: B1 ó B2
└─ eliges UNA Icónica de dos:            └─ eliges UNA Icónica de dos:
   ├─ Icónica A-1 → Pasiva A3 ó A4          ├─ Icónica B-1 → Pasiva B3 ó B4
   └─ Icónica A-2 → Pasiva A5 ó A6          └─ Icónica B-2 → Pasiva B5 ó B6
```

Totales por mercenario en los datos 3.1.0: **2 Core + 4 Icónicas = 6 activas, 12 pasivas, 1 Perk**.

**Presupuesto de puntos: 4.** Rapport I–IV dan 1 punto de habilidad cada uno, 4 en total ([purediablo](https://www.purediablo.com/diablo4/Mercenaries): *"Ranks I–IV: 1 Skill Point each (4 total)"*; [wowhead](https://www.wowhead.com/diablo-4/guide/mercenaries-guide)). Encajan exactamente con las 4 elecciones: 1 Core + 1 pasiva Core + 1 Icónica + 1 pasiva Icónica. **El Perk es automático y gratis, y solo aplica al Contratado.**

> ⚠️ Discrepancia declarada: d4guides.gg anuncia **"28 Skills"** por mercenario ([d4guides](https://d4guides.gg/en/database/mercenaries)). En el fichero de datos salen 19 entradas por mercenario (6+12+1). No sé de dónde sale el 28 y no lo he podido reconstruir. No lo uso.

---

## 5. 🆕 Los cuatro mercenarios, uno a uno

Todos los textos de habilidad y todos los enfriamientos de estas tablas salen del fichero `data.min.json` versión **3.1.0.72698** (datamining) salvo donde se indique otra fuente. Los enfriamientos son el campo `cooldown` de cada habilidad.

### 5.1 Raheir, el Portaescudos (Shieldbearer) — Tanque / soporte defensivo

**Perk (solo como Contratado) — Valiance (Valor):** *"When you would be damaged for at least **15%** of your current Life at once, Raheir comes to your aid to negate the damage, Knock Down Close enemies for **2** seconds, and grant you Unstoppable for **0,5** segundos. Cooldown: **30** segundos."*

| Rama | Habilidad Core (arma / básico) | Efecto y números |
|---|---|---|
| A | **Shield Charge** (Carga de Escudo) — CD **11 s**. Arma: **Escudo Torre**. Básico: *Shield Bash* | Embiste, daño físico, **Provoca (Taunt) 4 s**. El básico te **Fortifica un 0,2% de tu Vida Máxima** por golpe |
| B | **Ground Slam** (Golpe de Suelo) — CD **11 s**. Arma: **Escudo Redondo**. Básico: *Shield Strike* | Ralentiza **30% / 6 s** (**60%** en el centro). Cada **20** golpes del básico te **cura un 8% de tu Vida Máxima** |

| Icónicas | CD | Efecto |
|---|---|---|
| **Provoke** (rama A) | 25 s | Provoca a los enemigos a tu alrededor **5 s**. Ganas **5% de Reducción de Daño por objetivo, hasta 20%** |
| **Crater** (rama A) | 22 s | Golpea el suelo **3 veces**, atrae enemigos; la última ráfaga **Aturde 2 s** |
| **Bastion** (rama B) | 30 s | Se planta **5 s** y **redirige hacia sí el 90% del daño** que recibirían los aliados cercanos durante **5 s**. Al lanzarla, **Imparable 1,0 s** a los aliados cercanos |
| **Shield Throw** (rama B) | 22 s | Lanza el escudo, **Provoca 5 s**, rebota hasta **9 veces** sin repetir objetivo. Escalar de daño más alto de su kit (`payload scalar` 4,5) |

| Pasiva | Rama / puerta | Texto exacto |
|---|---|---|
| **Raheir's Guard** (A1) | Core A | Te da **15%[+] Armadura** |
| **Vanguard** (A2) | Core A | Ralentiza a los enemigos que le rodean un **40%** |
| **Mocking Lure** (A3) | tras Provoke | **Tú** infliges **15%[x]** más daño a enemigos Provocados por Raheir |
| **Iron Wolf's Ward** (A4) | tras Provoke | Al dispararse Valiance: Empuja a los cercanos y Provoca a los lejanos **4 s**. **CD de Valiance −35%** |
| **Sundering Shield** (A5) | tras Crater | La última ráfaga de Crater hace **200%[x]** más daño y aplica **Vulnerable 4 s** |
| **Iron Wolf's Call** (A6) | tras Crater | Al dispararse Valiance: tus **4** próximas Habilidades Fundamentales en **10 s** hacen **25%[x]** más daño y no cuestan recurso. **CD de Valiance −25%** |
| **Raheir's Aegis** (B1) | Core B | Te da **15% de Resistencia a Todos los Elementos** |
| **Draw Fire** (B2) | Core B | Al usar Poción de Curación, Raheir Provoca **4 s**. Máx. **1 vez cada 20 s** |
| **Inspiration** (B3) | tras Bastion | Los enemigos afectados por Ground Slam **reciben 15%[x] más daño**. Los aliados afectados por Bastion **infligen 25%[x] más daño** |
| **Iron Wolf's Virtue** (B4) | tras Bastion | Al dispararse Valiance: te **cura un 25% de tu Vida Máxima**. **CD de Valiance −35%** |
| **Consecrated Shield** (B5) | tras Shield Throw | Shield Throw **Consagra 6 s**; dañar directamente a un consagrado te **cura un 6% de Vida Máxima**, una vez por objetivo |
| **Iron Wolf's Arrival** (B6) | tras Shield Throw | Al dispararse Valiance también lanza **Ground Slam y Shield Throw**. **CD de Valiance −35%** |

### 5.2 Varyana, la Bruja Berserker (Berserker Crone) — DPS cuerpo a cuerpo

**Perk — Massacre (Masacre):** tú y Varyana acumuláis pilas al matar. **10 pilas → +5% Vel. Movimiento · 25 → +10% · 50 → +15% · 100 → +20%**. Se reinicia tras **7 s** sin matar.

| Rama | Core (arma / básico) | Números |
|---|---|---|
| A | **Cleave** — CD **11 s**. Arma: **Hachas dobles**. Básico: *Double Strike* | Daño físico + Sangrado. El básico tiene **45%** de probabilidad de aplicar Sangrado **3 s** |
| B | **Shockwave** — CD **11 s**. Arma: **Maza a dos manos**. Básico: *Heavy Strike* | **Derriba 1,5 s**. El básico tiene **+20%[+] de Prob. de Crítico** |

| Icónicas | CD | Efecto |
|---|---|---|
| **Bloodthirst** (A) | 22 s | Varyana gana **30%[+] Vel. Ataque, 200%[+] Vel. Movimiento e Imparable 7 s**. **A ti te da 10%[+] Vel. Ataque** la misma duración |
| **Whirlwind** (A) | 11 s | Gira en línea, daño repetido + Sangrado **5 s** |
| **Earth Breaker** (B) | 17 s | Temblor que hace daño durante **3 s** y **Derriba repetidamente** |
| **Ancient Harpoons** (B) | 17 s | **Tres arpones** que perforan; luego **atrae y Aturde 4 s** |

| Pasiva | Puerta | Texto |
|---|---|---|
| **Hysteria** (A1) | Core A | **+1,0%[+] Vel. Ataque 5 s** cada vez que Varyana daña, hasta **10,0%[+]** |
| **Recklessness** (A2) | Core A | Cleave aplica **Vulnerable 3 s** |
| **Intimidated** (A3) | tras Bloodthirst | Mientras tenga Bloodthirst, los enemigos a su alrededor **hacen 15% menos daño** |
| **Bloodlust** (A4) | tras Bloodthirst | Bloodthirst te da **+5%[+] Vel. Ataque** adicional |
| **Taste of Flesh** (A5) | tras Whirlwind | Al dañar directamente a un enemigo con Sangrado suyo, **te curas un 1% de Vida Máxima** |
| **No Escape** (A6) | tras Whirlwind | Whirlwind **atrae cada 1,5 s** y gana **60% de tamaño** |
| **Crushing Force** (B1) | Core B | **30%** de probabilidad de **Derribar 1,5 s** al dañar |
| **Reprisal** (B2) | Core B | Si te controlan, salta al culpable: daño y **Derribo 2,28 s**. Máx. **1 vez cada 12 s** |
| **Rampage** (B3) | tras Earth Breaker | **Tú** haces **15%[x]** más daño a enemigos bajo cualquier control de Varyana |
| **Dismembering** (B4) | tras Earth Breaker | Enemigos dañados por Earth Breaker: tu siguiente golpe en **3 s** hace **20%[x]** más daño. Una vez cada **5 s** por objetivo |
| **Iron Grip** (B5) | tras Harpoons | Los arpones viajan **33%** más lejos y bajan la **Resistencia a Impedimentos un 50% / 5 s** |
| **Annihilator** (B6) | tras Harpoons | Los arpones además **Ralentizan 40% / 5 s**; durante ese tiempo ganas **30%[x] de Prob. de Golpe de Suerte** contra ellos |

### 5.3 Aldkin, el Niño Maldito (Cursed Child) — Lanzador Sombra / Fuego

**Perk — Blasphemous Fate (Destino Blasfemo):** *"Aldkin occasionally loses control of his curse, transforming into a ferocious demon for **22 seconds**. This grants Aldkin powerful new abilities, but the unleashed evil curses you for its duration."*
- **Curse of Darkness:** los enemigos cercanos se vuelven **Vulnerables**.
- **Curse of Flames:** tu daño directo **Quema** a los enemigos **3 s**.
- La maldición y la forma demoníaca **las decide su habilidad Core**.

> ⚠️ Wowhead lo llama **"Blasphemous Fire"** y cifra la quemadura en **"30% damage over 3 seconds"**. En el fichero de datos el nombre es **Blasphemous Fate** y el valor de la quemadura es un marcador (`{dot:player_burn}`) que no resuelvo. **El 30% no lo he podido verificar** → va a "No encontrado".
>
> ⚠️ La versión Maxroll del perk habla de *"8% Maximum Resource per second"* drenado ([maxroll](https://maxroll.gg/d4/resources/mercenaries-overview)). **Ese texto no aparece en el fichero 3.1.0.** Puede ser una versión muerta del perk. No lo uso.

| Rama | Core | Números |
|---|---|---|
| A | **Haunt** — CD **14 s**. Fate: **Forsaken**. Básico: *Shadow Strike* | Emite **3** almas que Encantan y hacen daño de Sombra en el tiempo. Si el objetivo muere Encantado, **el alma salta a otro** |
| B | **Flame Surge** — CD **11 s**. Fate: **Aflame**. Básico: *Fire Shot* | Canaliza un cono de llamas **4 s** |

| Icónicas | CD | Efecto |
|---|---|---|
| **Field of Languish** (A) | 20 s | Deseca un área **6 s**: **Ralentiza 40%** y **reduce el daño que infligen los enemigos un 20%** |
| **Chain of Souls** (A) | 21 s | Encadena hasta **10** enemigos, daño de Sombra **2,5 s**; al expirar, daño y **Aturde 2,5 s** |
| **Storm of Fire** (B) | 20 s | Tormenta de fuego que permanece **10 s**; Quema cada segundo. **30%** de probabilidad de **Aturdir** a los alcanzados |
| **Wave of Flame** (B) | 25 s | Masa de llamas: daño repetido, **Empuja** y **destruye proyectiles pequeños** |

| Pasiva | Puerta | Texto |
|---|---|---|
| **Terrify** (A1) | Core A | Los golpes de Haunt tienen **30%** de aplicar **Vulnerable 4 s** |
| **Exhaustion** (A2) | Core A | Su daño de Sombra tiene **10%** de **Aturdir levemente (Daze) 2 s** |
| **Paranoia** (A3) | tras Field of Languish | Los enemigos "Languishing" reciben **15%[x]** más daño **de ti**. Golpe de Suerte: hasta **20%** de Daze **1,0 s** |
| **Condemned** (A4) | tras Field of Languish | **Matas al instante** a enemigos "Languishing" con menos del **40%** de Vida. **No funciona con Élites** |
| **Shared Pain** (A5) | tras Chain of Souls | El CD de Chain of Souls baja **1,5 s** cuando muere un encadenado |
| **Amplified Suffering** (A6) | tras Chain of Souls | Dañar a un encadenado **detona la cadena antes**, con daño de Sombra alrededor |
| **Covered in Ash** (B1) | Core B | Flame Surge **Ralentiza 20%** y añade Quemadura **3 s** |
| **Raging Violence** (B2) | Core B | **Los aliados ganan 15%[+] de Prob. de Crítico** contra enemigos afectados por Flame Surge |
| **Eradication** (B3) | tras Storm of Fire | Enemigos muertos dentro de la tormenta **explotan** |
| **Ember's Gift** (B4) | tras Storm of Fire | **Recuperas 33 de recurso por segundo** mientras estés dentro de la tormenta |
| **Raging Havoc** (B5) | tras Wave of Flame | Enemigos dañados por Wave of Flame reciben **15%[x] más Daño en el Tiempo 4 s** |
| **Burning Chaos** (B6) | tras Wave of Flame | **El CD de Wave of Flame se reinicia al lanzar tu Habilidad Definitiva** |

### 5.4 Subo, el Arquero Borracho (Drunken Archer / Bounty Hunter) — Utilidad a distancia

**Perk — Seeker (Rastreador):**
- **Pasivo:** *"Subo reveals all enemies and materials in the area."* (el "maphack")
- **Activo:** marca a un enemigo **10 s**. Matarlo **restaura 50 de tu Recurso Primario** y **reduce el CD de Seeker en 10 s**. **CD: 20 s.**

> ⚠️ Wowhead escribe *"restores **50%** of your Maximum Resource"*. El fichero 3.1.0 dice *"restores **50** of your Primary Resource"* — **cantidad plana, no porcentaje**. Uso el fichero.

| Rama | Core (arma / básico) | Números |
|---|---|---|
| A | **Wire Trap** — CD **10 s**. Arma: **Arco**. Básico: *Heavy Shot* | Trampa que se arma en **0,8 s**; explota y **Aturde 2,0 s**. El básico tiene **30%** de **Aturdir 1,0 s** |
| B | **Molotov** — CD **11 s**. Arma: **Ballesta**. Básico: *Salvo* | Incendiaria: Aturde y luego arde **5 s**. El básico lanza **5 dardos**; el último **Ralentiza 50% / 2 s** |

| Icónicas | CD | Efecto |
|---|---|---|
| **Cover Fire** (A) | 20 s | Descarga de flechas **sobre tu posición**; **Ralentiza 50%** |
| **Trip Mines** (A) | 18 s | **3** trampas explosivas (se arman en **1,0 s**); **Derriban 1,5 s** |
| **Snipe** (B) | 20 s | Perno perforante cargado; **Empuja** |
| **Explosive Charge** (B) | 22 s | **4** cargas adheridas; explotan a los **6,5 s** o al morir el objetivo |

| Pasiva | Puerta | Texto |
|---|---|---|
| **Piercing Arrows** (A1) | Core A | Heavy Shot **perfora** |
| **Ready At Hand** (A2) | Core A | Daño directo a un Élite te da **20%[+] Vel. Movimiento 2 s** |
| **Pin Cushion** (A3) | tras Cover Fire | Cover Fire además **Inmoviliza** |
| **Opening Fire** (A4) | tras Cover Fire | **Tú** haces **25%[x]** más Daño Crítico a los alcanzados por Cover Fire durante **4 s** |
| **Loaded Munitions** (A5) | tras Trip Mines | Wire Trap y Trip Mines aplican **Vulnerable 5 s** |
| **Mastermind** (A6) | tras Trip Mines | Wire Trap y Trip Mines **+60% de tamaño**. Tú y Subo ganáis **+25%[+] Duración de Control** |
| **Scorched Earth** (B1) | Core B | La explosión inicial de Molotov hace que reciban **30%[x] más Daño en el Tiempo tuyo** durante **3 s** |
| **Share a Drink** (B2) | Core B | Al explotar un Molotov, **50%** de soltarte una **Poción de Curación** |
| **Incendiary Bolt** (B3) | tras Snipe | Si Snipe acierta al objetivo original, **explota un Molotov** sobre él |
| **Ambusher** (B4) | tras Snipe | **+20%[x] Prob. de Golpe de Suerte** contra enemigos dañados por Salvo en los últimos **3 s** |
| **Bargaining Chips** (B5) | tras Explosive Charge | Los objetivos con cargas reciben **+5%[x] de daño por cada carga adherida** |
| **Thrillseeker** (B6) | tras Explosive Charge | Tus enfriamientos activos bajan **0,5 s** por cada carga que explota. Las cargas detonan en **1,5 s** en vez de 6,5 |

---

## 6. 🆕 El sistema de Refuerzo (Reinforcement) y cómo se combinan dos

### 6.1 Qué es y qué NO es

| Contratado (Hired / Primary) | Refuerzo (Reinforcement) |
|---|---|
| Te acompaña permanentemente | Aparece **brevemente** y se va |
| **Solo en juego en solitario** | **En solitario Y en grupo** |
| Usa 1 Core + 1 Icónica + 2 pasivas + **el Perk** | Usa **1 sola habilidad activa, en versión base** |
| — | **NO usa pasivas. NO usa el Perk** |
| Gana Rapport completo en solitario | Gana **50% en solitario** (mientras haya Contratado) |

Fuentes: [purediablo](https://www.purediablo.com/diablo4/Mercenaries) (*"Uses one Active Skill of your choice (base version only). Does not use passives or Perks."*), [maxroll](https://maxroll.gg/d4/resources/mercenaries-overview) (*"These Mercenaries will only use the base version of their skills and will not be affected by their passives."*), [wowhead](https://www.wowhead.com/diablo-4/guide/mercenaries-guide) (*"Perks only apply to a Primary Mercenary, not to a Reinforcement."*).

> **Esto tiene una consecuencia grande y poco intuitiva:** todo el valor de un mercenario que viva en sus *pasivas* desaparece cuando lo pones de Refuerzo. Ejemplo: el Vulnerable de Subo viene de **Loaded Munitions**, que es una pasiva → **Subo de Refuerzo NO aplica Vulnerable**. En cambio, la reducción del 20% de daño enemigo de Aldkin está escrita **dentro de la propia habilidad** *Field of Languish* → **sí funciona de Refuerzo**. Es la razón mecánica de por qué las guías eligen a Aldkin de Refuerzo.

### 6.2 Cómo se enlaza: las "Oportunidades" (Opportunities)

Se configura en el **panel de mercenario (Mayús + M), pestaña Reinforcement**. Eliges **una habilidad** del mercenario alistado y **una condición** que la dispare. La lógica es "algo entra, algo sale" ([wowhead reinforcement](https://www.wowhead.com/diablo-4/guide/mercenaries-reinforcement-guide)).

**Lista de disparadores** ([purediablo](https://www.purediablo.com/diablo4/Mercenaries)):

| Tipo | Disparador |
|---|---|
| Específico | **Cuando usas una habilidad concreta que tú elijas** |
| Universal | Cuando usas **cualquier** habilidad en combate |
| Universal | Cuando quedas **Herido (Injured, <35% de Vida)** |
| Universal | Cuando te alcanza un **efecto de control (Control-Impairing Effect)** |

Reglas de enfriamiento ([wowhead reinforcement](https://www.wowhead.com/diablo-4/guide/mercenaries-reinforcement-guide)):
- El Refuerzo aparece **si la Oportunidad se cumple Y su habilidad no está en enfriamiento**.
- Si la Oportunidad salta con la habilidad en enfriamiento, **se pierde**: hay que volver a dispararla después.
- **Más Rapport = más habilidades disponibles** para asignar como Refuerzo.
- Cada Refuerzo tiene **su propio enfriamiento** ([purediablo](https://www.purediablo.com/diablo4/Mercenaries)).
- **Solo tú ves aparecer tu Refuerzo** ([purediablo](https://www.purediablo.com/diablo4/Mercenaries)).

**Dónde aparece el Refuerzo (datamining, etiqueta interna).** El fichero 3.1.0 marca cada habilidad con etiquetas `Skill_Mercenary_Reinforcement_Farspawn` (aparece lejos, en el enemigo) o `Skill_Mercenary_Reinforcement_TargetPlayer` (aparece sobre ti):

| Mercenario | Habilidades marcadas `Farspawn` | Marcadas `TargetPlayer` |
|---|---|---|
| Raheir | Shield Charge | **Bastion** |
| Varyana | Ancient Harpoons | **Bloodthirst** |
| Aldkin | — | — |
| Subo | Wire Trap, Molotov, Trip Mines, Snipe, Explosive Charge | Cover Fire (también Farspawn) |

*Interpretación mía de la etiqueta, no confirmada por ninguna guía.* La lista de qué habilidad lleva qué etiqueta sí es dato duro del fichero.

### 6.3 El Aspecto de Asistencia (Aspect of Assistance) 🆕

Es el único aspecto legendario del juego que interactúa con el Refuerzo, y **es exclusivo de VoH**, así que también acaba de desbloquearse.

| Dato | Valor | Fuente |
|---|---|---|
| Texto | *"Your Reinforcement Cooldown is reduced by X%[x]. After casting your **Ultimate** Skill, your Reinforcement Mercenary is called. This cannot occur more than once each **30** seconds."* | fichero 3.1.0, clave `legendary_generic_126_x1`; [wowhead affix](https://www.wowhead.com/diablo-4/affix/aspect-of-assistance-2107188) |
| Valor | **23–33%** (Wowhead). Fórmula interna del fichero: `0.225 + (rango legendario − 1) × 0.005` → **22,5% en rango 1** | [wowhead affix](https://www.wowhead.com/diablo-4/affix/aspect-of-assistance-2107188) + fichero 3.1.0 |
| Categoría | **Utilidad** (Utility). Está en el **Codex of Power** | [wowhead affix](https://www.wowhead.com/diablo-4/affix/aspect-of-assistance-2107188) |
| Ranuras permitidas | **Yelmo, Peto, Botas, Guantes, Amuleto (poder +50%), Pantalones, Escudo** | [wowhead affix](https://www.wowhead.com/diablo-4/affix/aspect-of-assistance-2107188); coincide con `itemLabels: [16,17,29,28,26,30,15]` del fichero |
| Añadido en | parche **2.0.1.58184** | [wowhead affix](https://www.wowhead.com/diablo-4/affix/aspect-of-assistance-2107188) |
| ID interno | `2107188` / `legendary_generic_126_x1` | ambos |

⚠️ **Game8 publica "7,7%" para este aspecto. Es un número muerto.** El valor vivo es 23–33%.

**Por qué le importa a él en particular:** tiene **Ejército de los Muertos** (Army of the Dead) en la barra, que es una Definitiva. Este aspecto convierte su Definitiva en un botón que **también invoca al Refuerzo**, además de recortarle el enfriamiento casi un tercio. Y como el Refuerzo es lo *único* que le funciona en dúo, este aspecto vale el doble para él que para un jugador en solitario.

### 6.4 Un dato del fichero que NO doy por vivo

En el fichero 3.1.0, sección `stones`, existe **"Beastmaster's Training"** (`S08_CollectibleBossPower_022_Apparition_Beastmaster`):

> *"Whenever you cast a **Summon** Skill or **call a Mercenary for Reinforcement**, one of your Summons or Mercenaries Stuns surrounding enemies for [~2 s] and gains **75,0%** Damage Reduction."*
> Modificador: *"Your Summons deal **5%[x]** more damage, increased by **0,25%[x]** for each 1% Bonus Critical Strike Damage from items and Paragon, up to [17%+...]"*

Sería **perfecto** para un nigromante de esbirros con Refuerzo. Pero su categoría interna es **`S8_Boss`** — es un Poder de Jefe de la **Temporada 8**. **No he encontrado ninguna fuente que confirme que ese sistema esté activo en la Temporada 14.** Lo dejo aquí anotado y lo mando a "No encontrado". **No actúe sobre esto sin verlo en pantalla.**

---

## 7. 🆕 DÚO: qué pasa exactamente cuando juega con su pareja

### 7.1 La regla

| Situación | Contratado | Refuerzo |
|---|---|---|
| **En solitario** | ✅ Activo, con Perk y pasivas | ✅ Activo |
| **En grupo (dúo incluido)** | ❌ **No aparece** | ✅ **Activo, para cada jugador por separado** |

**Evidencia (tres fuentes, dos independientes entre sí):**

1. [Wowhead — Mercenaries Guide](https://www.wowhead.com/diablo-4/guide/mercenaries-guide) (2025/10/02): *"**Primary Mercenaries only show up when you are playing solo.**"* y *"When you're grouped with other players, your Reinforcement Mercenary will earn experience, but your Primary will not since that Mercenary is not accompanying you."*
2. [Wowhead — Reinforcement Guide](https://www.wowhead.com/diablo-4/guide/mercenaries-reinforcement-guide) (2026/03/11): *"**When playing in a group with other players, only your Reinforcement Mercenary will remain active.**"*
3. [PureDiablo](https://www.purediablo.com/diablo4/Mercenaries) (editada 08/12/2025), sección *Group Play Rules*: *"Primary Mercenaries do not appear in groups. Reinforcement Mercenaries continue to function for every player. Reinforcement triggers are personal and visible only to the owner. **There is no party-leader restriction on Reinforcements.**"*

**Y el desmentido explícito del mito**, en su sección *Common Misconceptions*:
> *"'Only the party leader can have a Mercenary.' **False.** Every player may have a Reinforcement; Primaries simply do not appear in groups."*

**Evidencia de jugadores en el juego vivo:** hilo [us.forums.blizzard 225812](https://us.forums.blizzard.com/en/d4/t/suggestion-dont-make-the-hired-merc-disappear-when-you-party-up/225812) (29/06/2025–02/07/2025): *"Kind of annoying losing Sobu's find skill or Rahir's resist all buffs when you're in a party"* y *"Most guides warn that if you rely on Rahier to get the resist cap, if you party up, to find alternate resist all sources."*

> ⚠️ **Un jugador de ese mismo hilo lo discute** (*"I believe that you still get the skill tree benefits or at least some of them; I know Rahier's armor and res buffs remain even in parties"*). No hay resolución oficial. Las tres guías coinciden en contra de él, así que **el aviso operativo se mantiene**: no cuente con el 15% de Resistencia a Todo de Raheir para llegar al tope de resistencias si juega en dúo. **Que lo mire en la hoja de personaje con y sin grupo.**

### 7.2 Rapport en dúo

| Situación | Contratado | Refuerzo |
|---|---|---|
| Solitario | 100% | **50%** ([maxroll](https://maxroll.gg/d4/resources/mercenaries-overview), [purediablo](https://www.purediablo.com/diablo4/Mercenaries)) |
| En grupo | 0% (no acompaña) | **100%** — *solo lo dice PureDiablo* |

PureDiablo: *"In group play, Reinforcement Mercenaries earn full Rapport"* y *"Reinforcement Mercenaries always gain Rapport while they are Hired in the Reinforcement slot, **even if they never appear in combat**. Summoning a Reinforcement is not required for Rapport progression."* ([purediablo](https://www.purediablo.com/diablo4/Mercenaries)).

Wowhead solo dice que el Refuerzo "gana experiencia" en grupo, sin cifra. **El 100% es una fuente única. Lo señalo como tal.**

**Lo aprovechable de todos modos:** su Refuerzo sube Rapport **aunque no lo invoque nunca**. Así que en dúo puede llevar de Refuerzo al mercenario que le falte por subir, sin coste ninguno.

### 7.3 La pareja y las expansiones — los dos casos

⚠️ **Nahantu es región exclusiva de Vessel of Hatred** ([purediablo](https://www.purediablo.com/diablo4/Mercenaries): *"their recruitment hub, The Den, is located in Nahantu, the new region added and exclusive to VoH"*).

| Caso | Consecuencia |
|---|---|
| **La pareja TIENE VoH** | Puede acompañarle a Nahantu y al Albergue. Cada uno lleva su propio Refuerzo, sin restricción de líder. Ninguno de los dos verá el mercenario Contratado del otro (ni el suyo). |
| **La pareja NO tiene VoH** | **No puede entrar en Nahantu con él.** No tiene el sistema de mercenarios en absoluto. Él tendrá que hacer la campaña de VoH y las misiones del Albergue **en solitario** (lo cual, dicho sea de paso, es cuando su mercenario Contratado sí funciona). Después pueden volver a jugar juntos en el contenido base — pero él seguirá sin Contratado mientras estén en grupo. |

Base de la afirmación sobre acceso: *"The new region of Nahantu is part of the expansion, so a player without Vessel of Hatred won't be able to access this area with you"* (agregado de resultados de búsqueda sobre la página oficial [diablo4.blizzard.com/vessel-of-hatred](https://diablo4.blizzard.com/en-us/vessel-of-hatred)). **No he abierto una nota oficial de Blizzard que lo diga con esas palabras** → lo marco como no cerrado del todo en "No encontrado".

---

## 8. Rapport, Marcas Pálidas (Pale Marks) y Fayira

### 8.1 Cómo se sube el Rapport

- **Se gana como experiencia**, luchando con el mercenario ([wowhead](https://www.wowhead.com/diablo-4/guide/mercenaries-guide)).
- **Los objetos y elixires de bonificación de experiencia también aplican al Rapport** ([wowhead](https://www.wowhead.com/diablo-4/guide/mercenaries-guide)) — dato concreto y accionable.
- **Eventos de mundo con mercenarios** por todo Santuario dan Rapport extra y **Marcas Pálidas** ([maxroll](https://maxroll.gg/d4/resources/mercenaries-overview), [wowhead](https://www.wowhead.com/diablo-4/guide/mercenaries-guide)).
- **10 niveles** de Rapport; a partir de X se repite indefinidamente. **Cada nivel después de X cuesta 25.000 de experiencia de mercenario** ([wowhead](https://www.wowhead.com/diablo-4/guide/mercenaries-guide)).
- **Rapport y Marcas Pálidas son de cuenta, por tipo de reino.** **Las recompensas de objeto solo se pueden reclamar una vez** ([wowhead](https://www.wowhead.com/diablo-4/guide/mercenaries-guide)).

### 8.2 Tabla de recompensas por nivel de Rapport

Fuente: [Wowhead — Mercenaries Guide](https://www.wowhead.com/diablo-4/guide/mercenaries-guide). Corroborada en estructura (no en cifras de Marcas) por [maxroll](https://maxroll.gg/d4/resources/mercenaries-overview) y [purediablo](https://www.purediablo.com/diablo4/Mercenaries).

| Nivel | Marcas Pálidas | Recompensa |
|---|---|---|
| **I – IV** | — | **1 punto de habilidad** de ese mercenario por nivel (**4 en total**) |
| **V** | **50** | Abre el **Trueque** (la primera vez, con el primer mercenario). Habilita comprar una **Caja de Aspectos** (5 legendarios con Aspecto de ese tipo) |
| **VI** | **50** | Caja de legendarios + oro |
| **VII** | **50** | Caja de **Masterworking** + legendarios |
| **VIII** | **75** | **Añade otra ranura de legendario** a Fayira + habilita una **Caja de Materiales** |
| **IX** | **75** | Caja de **materiales de invocación** + oro + legendarios |
| **X** | **100** | **Gran Caja**: oro, Fragmentos de Gema, Prismas Dispersos y legendarios |
| **XI+** | **100 por nivel** | Repetible sin fin |

**Total: 400 Marcas Pálidas por llevar un mercenario a Rapport X → 1.600 por los cuatro** ([wowhead](https://www.wowhead.com/diablo-4/guide/mercenaries-guide)).

### 8.3 Qué desbloquea cada mercenario (y por qué importa para él)

| Mercenario | Tipo de legendario que regala | Aspectos en Trueque | Caja de materiales (Rapport VIII) |
|---|---|---|---|
| **Raheir** | **Armadura** | **Defensivos** | Materiales de fabricación |
| **Aldkin** | **Anillos** | **De Recurso** | Prismas Dispersos, Gemas y **Runas** |
| **Subo** | **Amuletos** | **De Utilidad** | **Materiales de invocación de jefes** |
| **Varyana** | **Armas** | **De Movilidad** | Materiales de **Masterworking** y **Óbolos** |

Fuentes: [wowhead](https://www.wowhead.com/diablo-4/guide/mercenaries-guide) y [maxroll](https://maxroll.gg/d4/resources/mercenaries-overview) — **coinciden**. (Wowhead detalla además los materiales de invocación por mercenario: Aldkin→Distilled Fear, Raheir→Living Steel, Subo→Exquisite Blood, Varyana→Malignant Hearts.)

> **Nota táctica:** el **Aspecto de Asistencia es de categoría Utilidad** → cae en la **Caja de Aspectos de Utilidad de Subo**. Si lo quiere por vía determinista, Subo a Rapport V es el camino. También se puede desguazar de cualquier legendario que lo lleve, y **las botas solo pueden llevar Aspectos de Movilidad o Utilidad**, lo que las hace la compra barata en el Vendedor de Curiosidades para farmearlo.

### 8.4 Fayira y el Trueque

- **Fayira** está en el centro del Albergue. Empieza con **4 ranuras** de legendarios, de nivel apropiado al personaje y dificultad. **En Tormento I, el mínimo es 750** de poder de objeto ([wowhead](https://www.wowhead.com/diablo-4/guide/mercenaries-guide)).
- **El Trueque se abre a nivel de personaje 15 y Rapport V con cualquier mercenario** ([purediablo](https://www.purediablo.com/diablo4/Mercenaries)). Wowhead lo dice igual: *"Barter is not available at Level 1, even if fully opened on a previous character."*
- **Restock: gratis las primeras veces, luego 100 Marcas Pálidas por reinicio** ([wowhead](https://www.wowhead.com/diablo-4/guide/mercenaries-guide), [maxroll](https://maxroll.gg/d4/resources/mercenaries-overview), [purediablo](https://www.purediablo.com/diablo4/Mercenaries) — las tres coinciden en el 100).
- **Puede salir equipo Ancestral con Afijos Superiores (Greater Affixes)** ([wowhead](https://www.wowhead.com/diablo-4/guide/mercenaries-guide), [maxroll](https://maxroll.gg/d4/resources/mercenaries-overview)).
- Las cajas de materiales pueden dar **varias Runas**: *"one of the best guaranteed sources for Runes outside of farming Kurast Undercity with Tributes of Harmony"* ([wowhead](https://www.wowhead.com/diablo-4/guide/mercenaries-guide)).

---

## 9. LO IMPORTANTE: qué mercenario y qué refuerzo para NIGROMANTE DE ESBIRROS en S14

### 9.1 Qué dicen las guías vivas de S14 (las tres, con fecha)

| Guía | Fecha / temporada | Contratado | Refuerzo | Razón textual |
|---|---|---|---|---|
| [Maxroll — Minion Necromancer Endgame](https://maxroll.gg/d4/build-guides/minion-necromancer-guide) | 22/07/2026, S14 | **Subo** | **Aldkin** | *"Subo provides his map hack and a small amount of damage increase while Aldkin provides a boost to your damage reduction."* |
| [Mobalytics — Minion Necromancer Endgame](https://mobalytics.gg/diablo-4/builds/minion-necromancer-endgame-build-guide) (Raxxanterax) | publicada 03/08/2026, changelog "6/29/26 – Updated for Season 14" | **Raheir** | **Aldkin** | *"Raheir dives in to save you from a huge hit, provides 15% All Resist, makes enemies take 15% more Damage and makes you deal 25% more Damage."* · *"Aldkin provides you with 20% damage reduction when standing in his Field of languish. You need to level him up a bit to unlock this skill. Start off with Haunt until it's available."* |
| [Icy Veins — Naz Mages (Mendeln Summoner)](https://www.icy-veins.com/d4/guides/mendeln-summoner-necromancer-build/) | 27/06/2026, S14 | **Varyana** (Cleave, Hysteria, Bloodthirst, Intimidated) | **Raheir** con **Provoke** al usar una habilidad | *"stick with Raheir, utilizing Provoke when you use a Skill"* |

**Lectura honesta: no hay consenso sobre el Contratado.** Sí lo hay a medias sobre el Refuerzo: **Aldkin en 2 de 3**.

### 9.2 El razonamiento de Mobalytics, traducido a nodos exactos

Es la única recomendación de las tres que puedo reconstruir **nodo a nodo** contra el fichero de datos, y encaja perfectamente en los 4 puntos:

| Punto | Nodo | Efecto verificado |
|---|---|---|
| 1 | **Ground Slam** (Core rama B) | Arma escudo redondo; ralentiza 30/60%; el básico cura 8% de Vida Máxima cada 20 golpes |
| 2 | **Raheir's Aegis** (pasiva Core B1) | **+15% Resistencia a Todos los Elementos** |
| 3 | **Bastion** (Icónica rama B) | Redirige **90%** del daño de los aliados cercanos durante **5 s** + Imparable 1 s |
| 4 | **Inspiration** (pasiva Icónica B3) | Enemigos con Ground Slam **reciben 15%[x] más daño** · Aliados con Bastion **infligen 25%[x] más daño** |

Perk gratis: **Valiance** (anula un golpe de ≥15% de vida, CD 30 s).

Las cuatro cifras que cita Mobalytics (15% res, 15% más daño recibido, 25% más daño infligido, y el "dives in to save you") **coinciden exactamente** con los textos del fichero 3.1.0. Es la recomendación mejor auditada de las tres.

### 9.3 Mi lectura para SU build concreta (Coven + Master of Puppets + Gravebloom, Magos de Sombra + Guerreros Segadores + Gólem de Sangre)

**El eje del análisis es una distinción que casi ninguna guía hace explícita:** los efectos de mercenario se dividen en dos familias, y para un nigromante de esbirros no valen lo mismo.

| Familia | Ejemplo | ¿Beneficia al daño de sus esbirros? |
|---|---|---|
| **Debuff sobre el enemigo** ("los enemigos reciben X% más daño", "Vulnerable") | Inspiration (1ª mitad), Loaded Munitions, Recklessness, Terrify, Sundering Shield | **Sí, sin ambigüedad.** El enemigo recibe más daño de *cualquier* fuente, incluidos sus magos, guerreros y gólems |
| **Buff sobre "ti"** ("**tú** infliges X% más daño", "+Vel. Ataque") | Mocking Lure, Rampage, Paranoia, Opening Fire, Hysteria, Bloodlust | **No lo sé.** Depende de si los esbirros heredan los multiplicadores del jugador, y **no he encontrado ninguna fuente que lo diga por escrito** |

Además, dato duro que corta por lo sano: **"Mercenaries are not minions or companions, any effects referring to those categories do not apply"** ([purediablo](https://www.purediablo.com/diablo4/Mercenaries)). Es decir: sus **Unyielding Commander**, sus rangos a Guerrero/Mago Esquelético y todo lo que diga "esbirros" **NO tocan al mercenario**. El mercenario es una entidad aparte.

**Con eso, mi recomendación:**

#### A) Cuando juegue SOLO → **Raheir Contratado**, montaje de Mobalytics

Porque:
1. **Inspiration es debuff de enemigo en su primera mitad** (+15%[x] daño recibido con Ground Slam) → sube el daño de sus esbirros **sin depender de la incógnita**.
2. **Ground Slam ralentiza 30-60%** y **no dispersa**. Su build vive de que los enemigos se queden quietos delante de la horda. Maxroll marca explícitamente "Scatters Monsters" como contra de Raheir — ese contra es de la rama **Shield Charge**, no de Ground Slam. Escogiendo Ground Slam se evita.
3. **Taunt.** Un nigromante de esbirros quiere que los enemigos peguen a otra cosa. Raheir es el único que reparte Provocación en cantidad.
4. **Valiance** cubre el único modo real de morir en esta build: el pico de daño súbito.
5. El **+15% Resistencia a Todo** le resuelve la resistencia al tope sin gastar afijos.

**Alternativa defendible: Subo** (lo que dice Maxroll), con **Wire Trap + Trip Mines + Loaded Munitions (Vulnerable 5 s) + Mastermind**. El Vulnerable **es debuff de enemigo**, así que también le sirve a los esbirros, y el maphack de Seeker acelera muchísimo el farmeo. Si su cuello de botella hoy es *velocidad de farmeo*, Subo. Si es *no morir y empujar Pit*, Raheir.

**No recomiendo Varyana de Contratado para esta build**, pese a Icy Veins: su valor está en Velocidad de Ataque **para usted**, y usted no es quien pega. La guía de Icy Veins que la recomienda es para *Naz Mages / Mendeln*, un build distinto donde el jugador sí actúa más.

#### B) Cuando juegue EN DÚO → lo único que existe es el Refuerzo

Recuerde: **sin pasivas y sin Perk**. Solo una habilidad base con disparador. Candidatas, ordenadas por lo que aporta a una horda de esbirros:

| Opción | Habilidad | Por qué | CD |
|---|---|---|---|
| **1ª — recomendada** | **Aldkin → Field of Languish** | Es el consenso de Maxroll y Mobalytics, y funciona de Refuerzo **porque los números están en la habilidad, no en una pasiva**: **Ralentiza 40%** (los enemigos se quedan en la alfombra de esbirros) y **reduce el daño enemigo un 20%** (protege a los dos, a él y a su pareja) | 20 s |
| **2ª — agrupar** | **Varyana → Ancient Harpoons** | **Atrae y Aturde 4 s**. Agrupar es exactamente lo que le falta a una horda de esbirros. Etiqueta `Farspawn`: aparece en el enemigo | 17 s |
| **3ª — defensa de dúo** | **Raheir → Bastion** | Redirige **90%** del daño de los **aliados cercanos** 5 s + Imparable. Etiqueta `TargetPlayer`: aparece sobre usted. En dúo puede tapar también a su pareja | 30 s |
| **4ª — la de Icy Veins** | **Raheir → Provoke** | Provoca 5 s y le da hasta **20% de Reducción de Daño**. Más simple y más frecuente que Bastion | 25 s |
| **Descartada** | **Subo** cualquiera | Todo su valor (Vulnerable) vive en la pasiva **Loaded Munitions**, y **las pasivas no funcionan de Refuerzo**. De Refuerzo, Subo hace poco más que ruido | — |

**Disparador (Opportunity) que le recomiendo:** ligarlo a **Tentáculos de Cadáver (Corpse Tendrils)**. Es su habilidad de agrupar: los enemigos quedan apiñados justo donde caerá el *Field of Languish*, y el enfriamiento de Tendrils encaja bien con los 20 s de la habilidad de Aldkin. La alternativa segura es el disparador universal *"al usar cualquier habilidad en combate"*, que nunca falla pero desperdicia lanzamientos.

**Y encima:** si consigue el **Aspecto de Asistencia**, gana un segundo disparador gratis ligado a **Ejército de los Muertos** (su Definitiva), con **−23-33% al enfriamiento del Refuerzo**. Con ambos, el Refuerzo pasa de anécdota a estar casi siempre disponible — que es justo lo que necesita, porque en dúo es su único mercenario.

#### C) Orden de subida de Rapport para él

1. **Aldkin primero a Rapport IV.** Necesita los puntos para desbloquear *Field of Languish*, que es Icónica (Mobalytics lo avisa: *"You need to level him up a bit to unlock this skill. Start off with Haunt until it's available."*). Y de paso Aldkin regala **anillos** y **Runas/Prismas** en el Trueque.
2. **Raheir a IV** (para el montaje en solitario) — regala **armadura** y materiales de fabricación.
3. **Subo a V** — abre la **Caja de Aspectos de Utilidad**, que es donde vive el **Aspecto de Asistencia**; y regala **amuletos** y **materiales de invocación de jefes**.
4. **Varyana** al final — **armas** y materiales de **Masterworking + Óbolos**.

Truco de dúo: como el Refuerzo gana Rapport **aunque nunca aparezca**, puede tener siempre alistado al que le falte por subir mientras juega con su pareja.

---

## 10. Plan de hoy (resumen operativo)

1. Selección de personaje → **empezar la campaña de Vessel of Hatred** (Acto VII). Cuatro misiones hasta conocer a Raheir en Gea Kul (*A Magpie in Flight*); el sistema se abre en el **capítulo 2**, misión *The Hand that Remembers the Blade*.
2. En el Albergue (Selva de los Desolladores, esquina noroeste de *Lingering Hatred*, en Nahantu; icono verde al **noreste del Bazar de Kurast**), hacer las **tres misiones de adquisición** con los objetos marcados.
3. Terminar la campaña de VoH (*Presaged Fate*) para que sus futuros personajes se la salten y tengan mercenarios desde nivel 1.
4. Configurar: **Raheir Contratado** (Ground Slam / Raheir's Aegis / Bastion / Inspiration) + **Aldkin Refuerzo** (*Field of Languish*, disparador **Tentáculos de Cadáver**).
5. Farmear el **Aspecto de Asistencia** (botas por Óbolos, o Caja de Utilidad de Subo a Rapport V).
6. Comprobar en pantalla las dos cosas que las fuentes no cierran: si el mercenario Contratado desaparece al agruparse con su pareja, y si la resistencia baja 15% al hacerlo.

---

## Fuentes

URLs realmente abiertas durante esta investigación.

**Oficiales (Blizzard)**
- https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes — Notas del parche **3.1.3, build #73224, 12/08/2026**. Verificado: cero menciones a mercenarios.
- https://news.blizzard.com/en-us/diablo4/24128995/delve-deeper-into-nahantu-with-mercenaries-dark-citadel-and-more — Anuncio oficial del sistema de Mercenarios (VoH).
- https://us.forums.blizzard.com/en/d4/t/suggestion-dont-make-the-hired-merc-disappear-when-you-party-up/225812 — Hilo de jugadores, jun-jul 2025, sobre la pérdida del Contratado al agruparse.
- https://eu.forums.blizzard.com/en/d4/t/voh-mercenaries-only-party-leader/17859 — Hilo del 21/08/2024 que documenta el origen (Gamescom) del mito del "líder de grupo".

**Datamining**
- https://assets-ng.maxroll.gg/d4-tools/game/data.min.json — Fichero de datos del juego que sirve el planificador de Maxroll. **`version` = 3.1.0.72698**, es decir tres hotfixes por detrás del parche vivo 3.1.3/73224. Origen de todos los textos de habilidad, pasivas, enfriamientos, etiquetas de Refuerzo y de la fórmula del Aspecto de Asistencia.

**Maxroll**
- https://maxroll.gg/d4/resources/mercenaries-overview — *Last Updated: July 11, 2025*. Usada con reservas (contiene la afirmación pre-lanzamiento del "líder de grupo").
- https://maxroll.gg/d4/build-guides/minion-necromancer-guide — **22/07/2026, S14**. Recomendación Subo + Aldkin.
- https://maxroll.gg/d4/news/diablo-4-3-1-0-patch-notes — Notas 3.1.0. Cero menciones a mercenarios.
- https://maxroll.gg/d4/news/lord-of-hatred-3-1-2-patch-notes — **28/07/2026**, notas 3.1.2 (Lord of Hatred). Cero menciones a mercenarios.
- https://maxroll.gg/d4/news/diablo-4-season-14-undocumented-changes — **02/07/2026**. Cero menciones a mercenarios.

**Icy Veins**
- https://www.icy-veins.com/d4/guides/mercenaries-guide/ — `dateModified` **2026-06-30**, "Updated for Season 14".
- https://www.icy-veins.com/d4/guides/mendeln-summoner-necromancer-build/ — **27/06/2026, S14**. Recomendación Varyana + Raheir (Provoke).

**Wowhead**
- https://www.wowhead.com/diablo-4/guide/mercenaries-guide — **Updated 2025/10/02**. La guía más completa del sistema.
- https://www.wowhead.com/diablo-4/guide/mercenaries-reinforcement-guide — **Updated 2026/03/11**. Regla de grupo y mecánica de Oportunidades.
- https://www.wowhead.com/diablo-4/guide/zones/vessel-of-hatred-campaign-guide — **Updated 2025/04/14**. Estructura de la campaña de VoH y el hito exacto que abre Mercenarios.
- https://www.wowhead.com/diablo-4/affix/aspect-of-assistance-2107188 — Base de datos del Aspecto de Asistencia (23-33%, ranuras permitidas).

**Otras (abiertas y evaluadas)**
- https://www.purediablo.com/diablo4/Mercenaries — Última edición **08/12/2025**. Fuente principal para el comportamiento en grupo y los disparadores.
- https://mobalytics.gg/diablo-4/builds/minion-necromancer-endgame-build-guide — **03/08/2026**, changelog "6/29/26 – Updated for Season 14". Recomendación Raheir + Aldkin, reconstruible nodo a nodo.
- https://d4guides.gg/en/database/mercenaries — declarado "Season 14, Patch 3.1.0, 22/07/2026". Usada solo para confirmar que el roster son 4.
- https://diablobytes.com/diablo-iv/guides/mercenaries-guide/ — **DESCARTADA.** Fecha contradictoria y modelo muerto (afirma que los mercenarios equipan objetos).

---

## No encontrado

Huecos declarados. Nada de esto se ha reconstruido ni inferido.

1. **Confirmación en el parche vivo (3.1.3 / 73224) de los valores de habilidad.** El fichero de datos disponible es 3.1.0.72698. Ninguna nota de 3.1.1/3.1.2/3.1.3 menciona mercenarios, pero **no puedo cerrar que no haya habido ajustes silenciosos**.
2. **El momento exacto del desbloqueo.** Wowhead dice capítulo 2 (*The Hand that Remembers the Blade*); Blizzard y d4guides.gg dicen "al completar la campaña de VoH". **Contradicción sin resolver.**
3. **Los nombres de las tres misiones de adquisición** (*Slayer's Retribution*, *A Nameless Mystery*, *A Feather on the Scale*) **no los he verificado en una fuente preferente con fecha dentro de 3.1.x**. Vienen de agregación de resultados de búsqueda.
4. **Requisito de nivel para empezar la campaña de VoH.** No lo he encontrado escrito en ninguna fuente que haya abierto.
5. **Cuánto dura en tiempo real llegar al Albergue.** Wowhead da el número de misiones (30 en total, hito en cap. 2), pero **ninguna fuente da horas**.
6. **Si los esbirros del Nigromante cuentan como "aliados" para *Inspiration*** (*"Allies affected by Raheir's Bastion deal 25%[x] increased damage"*) y como destinatarios de los efectos que dicen *"you deal X% increased damage"*. **Esta es la incógnita que más valor tiene sin resolver** y ninguna de las tres guías de S14 la aborda. Solo se puede zanjar mirando el número en pantalla.
7. **El valor de la quemadura de *Curse of Flames*** (perk de Aldkin). Wowhead dice 30% en 3 segundos; en el fichero 3.1.0 es un marcador sin resolver. Nombre correcto del perk: **Blasphemous Fate**, no "Blasphemous Fire".
8. **El drenaje del "8% de Recurso Máximo por segundo"** que Maxroll atribuye a *Blasphemous Fate*. **No aparece en el fichero 3.1.0.** Posible versión muerta del perk.
9. **Si los mercenarios resucitan solos o hay que reanimarlos.** Wowhead dice que reaparecen solos; Maxroll dice que hincan rodilla y hay que revivirlos. **Contradicción sin resolver.**
10. **El "100% de Rapport para el Refuerzo en grupo".** Solo lo afirma PureDiablo. Wowhead confirma que el Refuerzo gana experiencia en grupo pero no da cifra.
11. **De dónde sale la cifra de "28 Skills" por mercenario** de d4guides.gg. En el fichero de datos son 19 entradas (6 activas + 12 pasivas + 1 perk).
12. **Si "Beastmaster's Training"** (invocaciones + Refuerzo aturden y ganan 75% de Reducción de Daño; invocaciones +5%[x] escalando con Daño Crítico) **sigue activo en la Temporada 14.** Está en el fichero 3.1.0 pero con categoría interna **`S8_Boss`** — Poderes de Jefe de la Temporada 8. **No usar sin verlo en pantalla.**
13. **Confirmación oficial de Blizzard, con esas palabras, de que un jugador sin Vessel of Hatred no puede entrar en Nahantu acompañando a uno que sí la tenga.** Lo afirman PureDiablo (Nahantu es exclusiva de VoH) y agregados de búsqueda, pero **no he abierto una nota oficial que lo diga literalmente**.
14. **Lista exhaustiva de qué habilidades concretas están disponibles como Refuerzo en cada nivel de Rapport.** Wowhead dice que "más Rapport = más habilidades disponibles" pero **ninguna fuente publica la tabla**.
15. **Confirmación de la interpretación de las etiquetas `Farspawn` / `TargetPlayer`** del fichero de datos. La asignación por habilidad es dato duro; que signifiquen "aparece en el enemigo" y "aparece sobre ti" es lectura mía.
16. **Si los buffs pasivos del Contratado (p. ej. el 15% de Resistencia a Todo de Raheir) persisten al agruparse.** Tres guías dicen que el Contratado desaparece; un jugador en el foro lo discute. **Sin resolución oficial.**
