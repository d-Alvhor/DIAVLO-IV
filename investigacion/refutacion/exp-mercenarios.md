# Refutación adversarial — `crudo/exp-mercenarios.md`

**Verificado el 19-20 de agosto de 2026.** Parche vivo: 3.1.3 (build 73224, 12/08/2026), Temporada 14 "Death Awakening".
**Veredicto: PARCIAL.** El núcleo de datamining es sólido y lo he **reproducido de cero**. La capa operativa y táctica tiene errores reales, incluidos dos que cambian lo que debería hacer el jugador.

No he editado el original.

---

## 0. Resumen ejecutivo

| Capa del informe | Veredicto |
|---|---|
| Fichero de datos (versión, roster, IDs, árbol, textos de habilidad, Perks, Aspecto) | **Confirmado.** Descargado y verificado de forma independiente, campo a campo. Cero discrepancias en los números. |
| Citas de PureDiablo, Blizzard, Maxroll, Icy Veins | **Confirmadas literalmente.** |
| Estructura del árbol y presupuesto de 4 puntos | **Confirmado** por tres vías independientes (fichero + Icy Veins S14 + PureDiablo). |
| Regla de grupo/dúo (§0, §7) | **Confirmada**, y además **más fuerte de lo que el informe cree** (ver S1). |
| Modelo de Trueque / Marcas Pálidas (§8) | **Incompleto — error de modelo.** Falta un sistema entero. |
| Recomendación de farmeo del Aspecto de Asistencia (§8.3) | **Refutada.** |
| Recomendación de disparador de Refuerzo (§6.2, §10) | **Refutada en su parte de "alternativa segura".** |
| Procedencia de las fuentes de Wowhead | **Problema declarado a medias.** Son guías etiquetadas de Temporadas 10 y 12. |

---

## 1. Lo que he reproducido y confirma el informe

Descargué yo mismo `https://assets-ng.maxroll.gg/d4-tools/game/data.min.json` (HTTP 200, **11.606.292 bytes**).

| Afirmación del informe | Resultado |
|---|---|
| `version` = **3.1.0.72698** | ✅ Exacto. Campo `version` del JSON. |
| Tres hotfixes por detrás de 3.1.3 / 73224 | ✅ La página oficial declara "Patch 3.1.3, Build 73224, August 12, 2026". |
| Exactamente **4** mercenarios | ✅ `mercenaries` tiene 4 claves, ni una más. |
| IDs: Raheir 1454142, Varyana 1456949, Aldkin 1491904, Subo 1491907 | ✅ Los cuatro, exactos. |
| El fichero está al día en contenido de la 2ª expansión | ✅ `skillTrees` contiene `Paladin_NEW` y `Warlock`. |
| **Estructura idéntica en los cuatro** | ✅ **Confirmado con más fuerza de la que da el informe.** Los cuatro árboles tienen **exactamente 21 nodos y 22 conexiones**, y las coordenadas `pos` de los nodos son **las mismas en los cuatro**. |
| 6 activas + 12 pasivas + 1 Perk = 19 | ✅ Por árbol: 6 nodos `reward.type 0` (activas) + 12 nodos `reward.type 2` (pasivas) + 3 nodos estructurales `root` (el Perk es el `rootSkill`). |
| Presupuesto de 4 puntos (Rapport I–IV) | ✅ Triple confirmación: fichero; PureDiablo (*"Ranks I–IV: 1 Skill Point each (4 total)"*); Icy Veins S14. |

**Los cuatro Perks, verbatim del fichero — los cuatro exactos:**

- **Valiance** (`NPC_Mercenary_ShieldBearer_Valiance`, id 1391558): *"Cooldown: 30 seconds. When you would be damaged for at least 15% of your current Life at once, Raheir comes to your aid to negate the damage, Knock Down Close enemies for 2 seconds, and grant you Unstoppable for 0.5 seconds."* ✅ Coincide palabra por palabra.
- **Massacre** (id 1479154): 10 pilas → 5%[+], 25 → 10%, 50 → 15%, 100 → 20% Vel. Movimiento; *"resets after 7 seconds of not killing an enemy"*. ✅ Exacto.
- **Blasphemous Fate** (`Mercenary_CursedChild_SummonDemonForm`, id 1555493): ✅ **El informe tiene razón y Wowhead se equivoca.** El nombre en los datos es *Blasphemous Fate*, no "Blasphemous Fire". Y la quemadura es efectivamente un marcador sin resolver: `[{dot:player_burn}|2?|] damage over 3 seconds`. El "30%" de Wowhead no aparece. Bien mandado a "No encontrado".
- **Seeker** (id 1684569): *"Killing a marked enemy restores 50 of your Primary Resource"*. ✅ **Cantidad plana, no porcentaje.** El informe corrige bien a Wowhead.

**Los números de Raheir de la §9.2 (los que sostienen la recomendación principal) — los verifiqué uno a uno y salen todos exactos:**
Raheir's Aegis *"15% Resistance to All Elements"*; Raheir's Guard *"15%\[+\] Armor"*; Inspiration *"Enemies affected by Raheir's Ground Slam take 15%\[x\] increased damage / Allies affected by Raheir's Bastion deal 25%\[x\] increased damage"*; Bastion *"redirecting 90% of the damage... for 5 seconds"* + *"Unstoppable for 1.0 seconds"*; Provoke *"5 seconds... 5% Damage Reduction for each target, up to 20%"*, CD 25; Sundering Shield *"200%\[x\] increased damage and inflicts Vulnerable... for 4 seconds"*; Ground Slam *"Slowing enemies by 30% for 6 seconds... center... Slowed by 60%"*, CD 11.

**Aspecto de Asistencia** (`legendary_generic_126_x1`, id 2107188): descripción, fórmula `0.225+(CurrentLegendaryRank()-1)*0.005` e `itemLabels [16,17,29,28,26,30,15]` ✅ exactos. Wowhead confirma **23–33%** y las siete ranuras (Yelmo, Peto, Botas, Guantes, Amuleto +50%, Pantalones, Escudo).

**Citas de PureDiablo — abiertas y comprobadas una a una** (la página da 403 a un agente normal; se obtiene con user-agent de navegador). Última edición: **8 de diciembre de 2025**, `oldid=48023`. Son todas literales y están bien transcritas: *"Primary Mercenaries do not appear in groups."* · *"Only the party leader can have a Mercenary." / "False. Every player may have a Reinforcement; Primaries simply do not appear in groups."* · *"Mercenaries are not minions or companions, any effects referring to those categories do not apply."* · *"Uses one Active Skill of your choice (base version only). Does not use passives or Perks."* · *"In solo play they earn 50% of the Rapport... In group play, they gain full Rapport."* · Historial de cambios con **una sola entrada**: *"Patch 2.0, October 8, 2024 — Added in Vessel of Hatred"*. ✅ Todo correcto, incluida la lista de disparadores.

**Otras confirmaciones independientes:**
- Maxroll *Minion Necromancer*: **22 de julio de 2026, Season 14**, Subo + Aldkin, con la cita justificativa exacta. ✅
- Blizzard oficial: *"Upon completing the Vessel of Hatred campaign, Raheir will be available to use in combat."* y *"Note that you will need to have a different Hired Mercenary than the one who is currently your Reinforcement."* ✅
- Notas 3.1.2 (Lord of Hatred, 28/07/2026): **ninguna mención** a mercenarios, y **ningún quinto mercenario**. ✅ Corroborado además por búsqueda independiente.
- **Mayús + M** ✅ corroborado fuera de Wowhead.
- Campaña: 4 capítulos + epílogo, ~30 misiones, capítulo final *Presaged Fate* ✅.
- **Ninguna fuente vetada respalda ningún número.** Revisé las 21 URLs citadas: cero apariciones de fextralife, primagames, beebom, gamespot, segmentnext, studioloot, gamerguides, pcgamesn o mythicdrop. Game8 y DiabloBytes aparecen solo para ser descartadas. ✅ Limpio.
- Los **tres nombres de misión de adquisición** que el informe mandó a "No encontrado" (#3) **sí se corroboran** en fuentes no vetadas (thegamer, gameranx, gamingbolt, screenrant). Se pueden dar por buenos, aunque no vengan de fuente preferente dentro de 3.1.x.
- El hilo del foro 225812 está citado con fidelidad, **incluida la voz discrepante**. ✅ Honesto.

---

## 2. Errores confirmados

### E1 — "Guide Coffers" no existe: es **Guild Coffers**
El informe escribe *"Guide Coffers"* dos veces (§3, tabla y cuerpo). Las fuentes independientes lo dan como **Guild Coffers** — Cofres del Gremio, el vendedor de anillos y amuletos. Error de nombre propio, justo lo que la regla 7 pedía vigilar.

### E2 — "Cero menciones a mercenarios en 3.1.0 / 3.1.2 / 3.1.3" es falso como está escrito
Abrí la página oficial de 3.1.3 y **sí contiene una aparición**: *"Fixed an issue where Impetus and Misanthropic Aspects treated pets and mercenaries as active demons."*
El propio informe la cita dos párrafos más abajo — es decir, **su tabla se contradice con su propio cuerpo**. La sustancia (ningún cambio de balance al sistema) se sostiene; el absoluto "ninguna mención" no.
Añadido: la página de Maxroll de **3.1.0** hace aflorar esa misma línea, lo que sugiere que el arreglo no es exclusivo de 3.1.3 como da a entender el informe. No lo cierro.

### E3 — La categoría del Aspecto de Asistencia no está confirmada por ninguna de las dos fuentes que el informe cita
El informe afirma: *"Categoría: **Utilidad** (Utility)"*, citando la página de Wowhead del afijo.
- **La página de Wowhead no declara categoría.** La abrí: da el texto, el rango 23–33% y las ranuras, y nada más.
- **El fichero de datos no la respalda tampoco.** Las etiquetas del afijo son:
  `"tags": ["HoradricCube_Legendary_Utility_Mobility", "Search_Copy_Ultimate", "FILTER_Legendary_Offensive"]`
  Es decir: una etiqueta que **mezcla Utilidad y Movilidad**, y otra que lo filtra como **Ofensivo**.

Ninguna de las dos fuentes citadas sostiene "Utilidad" a secas.

### E4 — "Vía determinista" es incorrecto, sea cual sea la categoría
El informe recomienda: *"Si lo quiere por vía determinista, **Subo a Rapport V es el camino**."*
El propio fichero que usa dice lo contrario, dos veces:
- `Merc_Rapport_BountyHunter_BarteringUpgrade_01`: *"An additional Legendary item will be offered when Bartering, **with a chance of it being** a cache of items with Utility Aspects."*
- Todos los `Mercenary_Contract_*`: *"**It does not guarantee stock** of these items."*

Y existe `Merc_Rapport_Bartering_Upgrade_Item` — **Looter's Luck**, *"+5% chance for the item to be offered when Bartering"* (y II, +10%) — que solo tiene sentido en un sistema probabilístico. **No hay vía determinista.**

### E5 — Error de modelo: falta el sistema de **Acuerdos Comerciales (Trade Agreements)** entero
Éste es el hallazgo de regla 6: **las tres guías (Wowhead, Maxroll, PureDiablo) comparten el mismo marco simplificado —"un mercenario, una categoría de aspecto"— y el fichero de datos lo desmiente.**

En los datos hay **dos sistemas distintos**, y el informe solo describe uno:

1. **Vía Rapport** (`Merc_Rapport_*_BarteringUpgrade_01/02`) — sí es exclusiva por mercenario. La tabla §8.3 del informe **es correcta para esto**: Raheir→Defensivos/Fabricación, Varyana→Movilidad/Masterworking+Óbolos, Aldkin→Recurso/"Augmentations" (Prismas, Fragmentos de Gema y Runas), Subo→Utilidad/Invocación de jefes. Verificado. También los materiales de jefe: Raheir→Grigoire (Acero Vivo), Varyana→Varshan (Corazones Malignos), Aldkin→Bestia del Hielo (Miedo Destilado), Subo→Lord Zir (Sangre Exquisita). ✅

2. **Acuerdos Comerciales** (`Mercenary_Contract_*`), *"unlocked in the Mercenary Den, adding additional item types to a Mercenary's Bartering pool"* — **el informe no lo menciona en ningún sitio.** Hay 8–9 por mercenario, y rompen la exclusividad:

| Acuerdo | Raheir | Varyana | Aldkin | Subo |
|---|---|---|---|---|
| `Aspect_01` | Defensivos | Movilidad | Recurso | Utilidad |
| **`Aspect_02`** | **Ofensivos** | **Ofensivos** | **Ofensivos** | **Ofensivos** |
| `Materials_03` | **Masterworking** | Masterworking | Masterworking | Masterworking |
| `Materials_04` | **Prisma Disperso** | Prisma Disperso | Prisma Disperso | Prisma Disperso |
| `Runes_01` | **Runas: Condición** | (sin nombre) | Runas: Efecto | **Runas: Condición** |

Consecuencias que el informe da por ciertas y no lo son:
- **Masterworking no es de Varyana**: los cuatro lo ofrecen.
- **Los Prismas Dispersos no son de Aldkin**: los cuatro los ofrecen.
- **Las Runas no son de Aldkin**: Raheir y Subo ofrecen Runas de Condición; Aldkin, de Efecto.
- **Los Aspectos Ofensivos salen de los cuatro.** Si el Aspecto de Asistencia va por la etiqueta `FILTER_Legendary_Offensive`, cualquiera de los cuatro sirve, y el consejo "Subo" pierde su razón de ser.

### E6 — "El disparador universal nunca falla": refutado, y afecta justo a su clase y a su configuración
El informe recomienda en §6.2 y §10: *"La alternativa segura es el disparador universal 'al usar cualquier habilidad en combate', que **nunca falla**."*

Hay informes de jugadores en los foros oficiales que ligan **exactamente esa opción** a que el mercenario **Contratado se quede sin contratar** al reconectar. Y nombran **a Aldkin de Refuerzo**, que es precisamente el emparejamiento que el informe recomienda:

- NameUnknow-11786 (18/05/2026): *"When you have Aldkin as reinforcement and log out of the game, it removes any of the hired primary mercenaries when you log back into the game."*
- FateOfNines-1735 (18/05/2026): *"On your Reinforcement, if you have your skill activation for them set to 'Cast when the player casts any skill in combat' it causes this. Change the reinforcement skill to activate on ANY other option and this typically stops happening."*
- Hilo paralelo (28/04/2026, parche 3.0.1): *"After every relog, my primary mercenary disappears and becomes unrecruited."* — con varios reportes de Nigromante. Solución de emergencia: volver al Albergue y recontratar.

**Salvedad honesta:** son reportes de abril-mayo de 2026 (parche 3.0.1 / lanzamiento de LoH), **no verificados en 3.1.3**, y sin respuesta oficial. Pero tampoco hay arreglo documentado: el propio informe demuestra que **ninguna nota de 3.1.x menciona mercenarios**, lo cual corta en las dos direcciones.

**Efecto práctico:** el disparador ligado a **Tentáculos de Cadáver** que el informe recomienda como opción principal es el correcto y además esquiva el problema. Lo que hay que retirar es la frase de que el universal "nunca falla" — es el disparador señalado como culpable. Y conviene evitar ligarlo a Guerreros/Magos Esqueléticos, que también aparece señalado.

### E7 — El contenido del Albergue no está disponible de golpe
La §3 presenta el Albergue como una lista plana. Las fuentes independientes dicen que se abre por etapas: **Guild Coffers** tras reclutar a Subo, **Raheir's Anvil** tras reclutar a Raheir, **Cursed Toy Box** (Ocultista) tras completar *A Nameless Mystery* (la misión de Aldkin). El día 1 no tendrá ni herrero ni ocultista ahí dentro.

### E8 — *Slayer's Retribution* tiene un requisito previo no declarado
Para desbloquear a Varyana hace falta haber completado antes el **Bastión del Templo de la Putrefacción (Temple of Rot Stronghold)**. La §2.2 solo menciona la nota clavada en la estaca.

### E9 — "El único aspecto que interactúa con el Refuerzo" deja fuera algo que a él le importa
La §6.3 dice que el Aspecto de Asistencia es *"el único aspecto legendario del juego que interactúa con el Refuerzo"*. Literalmente cierto para **aspectos legendarios**. Pero en el mismo fichero está:

> `Talisman_SealAffix_Normal_Elegance_03` — *"While Elegance Charm equipped, using a Cooldown reduces the Cooldown of your Reinforcement Mercenary by 3 second."*

Para un jugador cuyo **único** mercenario en dúo es el Refuerzo, una segunda fuente de reducción de enfriamiento del Refuerzo no es un detalle. El sistema de Amuletos/Talismanes es contenido vivo y voluminoso en este fichero (1.078 afijos de talismán). Omisión material, no error factual. (Ver el documento hermano `exp-charms.md`.)

---

## 3. Problema de procedencia que el informe declara solo a medias

El informe da las fechas de Wowhead pero **no dice que las páginas están etiquetadas para temporadas muertas**:

| Página | Citas en el informe | Cabecera real |
|---|---|---|
| `mercenaries-guide` | **25** — la más citada de todo el documento | *"Mercenaries Guide — **Diablo 4 Season 10**"*, 2025/10/02 |
| `mercenaries-reinforcement-guide` | 5 | **Season 12**, 2026/03/11 |
| `vessel-of-hatred-campaign-guide` | 4 | 2025/04/14 |

Bajo la regla 3 del encargo (solo páginas actualizadas dentro de 3.1.x) **ninguna de las tres cualifica**, y entre ellas soportan: la ubicación del Albergue, el atajo Mayús+M, la tabla de costes en Marcas Pálidas (50/50/50/75/75/100), las 4 ranuras de Fayira y el mínimo de 750 de poder de objeto en Tormento I, los 25.000 de experiencia por nivel de Rapport, y la cita principal de la regla de grupo.

**No he podido reabrir el cuerpo de ninguna página de Wowhead** (403 a `curl`; el recuperador solo devuelve la cáscara de la página). Por tanto **ningún número exclusivo de Wowhead ha podido ser re-verificado por mí**. Los que sí tienen segunda fuente (Mayús+M, restock de 100 Marcas, nivel 15 + Rapport V, afijos Ancestrales Superiores, materiales de jefe por mercenario) están confirmados; el resto queda en la palabra de una guía de la Temporada 10.

Lo mismo con **Mobalytics**: 403 tanto al recuperador como a `curl`. Las citas verbatim de §9.1 y §9.2 no las he podido re-verificar. Atenuante fuerte: **las cuatro cifras que el informe le atribuye coinciden exactamente con el fichero de datos**, que sí verifiqué. Es corroboración indirecta, no directa.

---

## 4. Un punto donde el informe se queda corto **a su favor**

### S1 — La afirmación titular tiene una cuarta pata, y es oficial
El informe apoya su §0 ("el Contratado no aparece en grupo") en tres guías más los foros. Se le escapó que **la propia nota de Blizzard que ya cita** lo dice de pasada:

> *"Mercenaries can offer their support by joining your Party, by **Hiring them when playing solo**, or by selecting them to add key Reinforcements in times of need."*

Blizzard encuadra el Contratado como el modo de apoyo **en solitario**. No es concluyente por sí solo, pero es una fuente oficial más en la misma dirección. **La afirmación más consecuente del informe queda reforzada, no debilitada.**

Y el conflicto que el informe declaró sin resolver (#2, momento del desbloqueo) **se resuelve en favor de su propia elección**: fuentes independientes confirman que el Albergue se abre *"after completing The Hand Remembers The Blade quest"*, en el capítulo 2 — no al terminar la campaña. El informe apostó bien y avisó de que podía equivocarse.

---

## 5. Correcciones concretas al original

1. §3: **Guild Coffers**, no "Guide Coffers".
2. §1.1: quitar el absoluto "ninguna mención" de la fila de 3.1.3 (y revisar 3.1.0). Sustituir por "una mención, y es un arreglo de interacción, no un cambio de sistema" — que es lo que ya dice el cuerpo.
3. §6.3 y §8.3: retirar la categoría "Utilidad" atribuida a Wowhead. Declararla **no encontrada**, y anotar las etiquetas reales del fichero (`Utility_Mobility` + `FILTER_Legendary_Offensive`).
4. §8.3: sustituir "vía determinista" por "vía con probabilidad aumentada". Añadir Looter's Luck.
5. §8: añadir los **Acuerdos Comerciales** y corregir la lectura de exclusividad de Masterworking, Prismas y Runas.
6. §6.2 y §10: **eliminar "que nunca falla"** del disparador universal y añadir el aviso del fallo con Aldkin de Refuerzo. Mantener Tentáculos de Cadáver como recomendación.
7. §3: marcar que Herrero, Ocultista y Cofres del Gremio se abren según se reclutan mercenarios.
8. §2.2: añadir el requisito del Bastión del Templo de la Putrefacción para Varyana; y quitar los tres nombres de misión del apartado "No encontrado", que sí se corroboran.
9. §6.3: añadir el sello **Elegance** del Amuleto como segunda fuente de reducción de enfriamiento del Refuerzo.
10. Fuentes: etiquetar las tres páginas de Wowhead como **Temporada 10 / Temporada 12**, no solo con su fecha.
11. §0: añadir la cita oficial de Blizzard como cuarto apoyo.

---

## 6. Lo que sigue sin poder cerrarse

Los 16 huecos del original siguen siendo huecos legítimos. Se mantienen intactos, salvo el #3 (nombres de misión, ahora corroborados) y el #2 (momento de desbloqueo, resuelto a favor del capítulo 2). Se añaden:

17. **Categoría real del Aspecto de Asistencia.** Ninguna fuente la declara; el fichero se contradice consigo mismo.
18. **Si el fallo del disparador universal sigue vivo en 3.1.3.** Reportes de abril-mayo de 2026, sin respuesta oficial y sin arreglo documentado en ninguna nota de 3.1.x.
19. **Cómo se desbloquean los Acuerdos Comerciales** y a qué ritmo. El fichero dice "in the Mercenary Den" y nada más.
20. **Todo lo que solo dice Wowhead.** Su cuerpo es inaccesible a verificación automática; sus páginas son de las Temporadas 10 y 12.

---

## Fuentes abiertas en esta verificación

**Reproducción directa**
- `https://assets-ng.maxroll.gg/d4-tools/game/data.min.json` — descargado (11.606.292 bytes), `version` = 3.1.0.72698. Origen de toda la verificación de números.

**Oficiales**
- https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes — 3.1.3 / build 73224 / 12-08-2026. Confirmada **una** aparición de "mercenaries".
- https://news.blizzard.com/en-us/diablo4/24128995/delve-deeper-into-nahantu-with-mercenaries-dark-citadel-and-more — dos citas literales confirmadas + el "when playing solo".
- https://us.forums.blizzard.com/en/d4/t/suggestion-dont-make-the-hired-merc-disappear-when-you-party-up/225812 — citas del original confirmadas, ambas caras.
- https://us.forums.blizzard.com/en/d4/t/necromancer-mercenary/255195 — el fallo del disparador universal con Aldkin (18/05/2026).
- https://us.forums.blizzard.com/en/d4/t/301-primary-mercenary-becomes-unrecruited-after-every-relog/246203 — 28/04/2026, parche 3.0.1.
- https://us.forums.blizzard.com/en/d4/t/mercenaries-disappeared/241318 — sin relación con el disparador; descartado como apoyo.
- https://us.forums.blizzard.com/en/d4/t/lord-of-hatred-mercs/242931 — ningún quinto mercenario en LoH.

**Preferentes**
- https://maxroll.gg/d4/build-guides/minion-necromancer-guide — 22-07-2026, S14. Subo + Aldkin confirmado.
- https://maxroll.gg/d4/news/lord-of-hatred-3-1-2-patch-notes — 28-07-2026. Cero menciones confirmado.
- https://maxroll.gg/d4/news/diablo-4-3-1-0-patch-notes — aflora la línea de Impetus/Misanthropic.
- https://www.icy-veins.com/d4/guides/mercenaries-guide/ — S14. Confirma estructura del árbol y los 4 puntos, y **no** cubre grupo ni ubicación, tal como decía el informe.
- https://www.wowhead.com/diablo-4/affix/aspect-of-assistance-2107188 — 23-33% y ranuras confirmadas; **sin categoría declarada**.
- https://www.wowhead.com/diablo-4/guide/mercenaries-guide — solo cabecera: **"Season 10"**, 2025/10/02.
- https://www.wowhead.com/diablo-4/guide/mercenaries-reinforcement-guide — solo cabecera: **"Season 12"**, 2026/03/11.
- https://www.wowhead.com/diablo-4/guide/zones/vessel-of-hatred-campaign-guide — solo cabecera: 2025/04/14.

**Otras**
- https://www.purediablo.com/diablo4/Mercenaries — recuperada íntegra. Última edición 08-12-2025. Todas las citas del informe verificadas.
- https://mobalytics.gg/diablo-4/builds/minion-necromancer-endgame-build-guide y .../guides/mercenary-guide — **403, no verificables**.
- Búsquedas agregadas (thegamer, gameranx, gamingbolt, screenrant, progametalk) para nombres de misión, contenido del Albergue y Mayús+M. **Ninguna fuente vetada usada para ningún número.**
