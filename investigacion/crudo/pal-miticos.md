# Míticos (Mythic Uniques) para Paladín — Season 14 "Death Awakening"

**Dominio:** Míticos: lista, efectos, procedencia, crafteo y orden de prioridad para un Paladín de *Shield Charge*.
**Parche vivo de referencia:** 3.1.3, build 73224, 12/08/2026.
**Fecha de la investigación:** 19/08/2026. Quedan ~4 semanas de temporada (fin ~15/09/2026).

---

## 0. Respuesta corta (si solo lees esto)

1. **El límite de "un solo Mítico crafteado equipado" YA NO EXISTE.** Blizzard lo eliminó en el hotfix
   3.1.1a del 16/07/2026. Puedes llevar los tres a la vez. *Casi toda la web sigue diciendo lo contrario,
   incluida la propia guía de Maxroll de tu build.* (§5)
2. **La receta del Cubo Horádrico cuesta 4 Fragmentos de Pandemónium (Pandemonium Fragments), no 5.**
   Bajó de 5 a 4 en el parche 3.1.1 del 14/07/2026 y no ha vuelto a cambiar. (§4.1)
3. **Los Míticos "clásicos" (Shako, Grandfather, Starless…) NO son tu prioridad.** La guía de la build no
   recomienda ninguno. Tus Míticos son Únicos de Paladín subidos a calidad Mítica. (§3)
4. **Orden concreto: 1º pecho (Mantle of the Grey) → 2º pantalones (Tibault's Will) → 3º escudo
   (Herald of Zakarum).** (§6)
5. **Antes de gastar nada: no abras las cachés de Mítico del Rango de Temporada con el nigromante.** (§4.4)

---

## 1. Aviso de método — qué es sólido y qué no

Esta sección existe porque en este proyecto ya se han publicado dos veces datos muertos. Léela.

| Fuente | Qué le pido | Fiabilidad |
|---|---|---|
| Notas de parche oficiales (news.blizzard.com, foros Blizzard) | Números de receta, límites, fechas | **Máxima.** Es la ley. |
| Maxroll / Icy Veins **con fecha dentro de 3.1.x** | Estructura, listas, contexto | Alta, *pero comprobando la fecha página por página* |
| Datamining `data.min.json` del planificador de Maxroll | Lista de objetos, textos de poder, fórmulas | Alta para *qué existe y qué hace*; ver lag abajo |
| Sitios de venta de oro / SEO (timesaver, nexttier, iggm, d4gold, mmogah…) | — | **No usadas para números.** Repiten datos de lanzamiento. |
| fextralife, primagames, beebom, etc. | — | Vetadas por encargo. No abiertas. |

**Tres avisos concretos, todos verificados:**

- ⚠️ **El fichero de datos va un parche por detrás.** `assets-ng.maxroll.gg/d4-tools/game/data.min.json`
  (HTTP 200, 11.606.292 bytes, descargado el 19/08/2026) se declara como **`"version":"3.1.0.72698"`**.
  El parche vivo es **3.1.3 / 73224**. Sirve para *qué objetos existen y qué hacen*; **no** para dar por
  buenos valores que 3.1.1/3.1.2/3.1.3 hayan tocado. **Esto es datamining**, no documentación oficial.
- ⚠️ **La guía de tu build en Maxroll tiene una línea caducada.** Actualizada el 25/07/2026, sigue
  afirmando: *"You can only equip one Mythic item that you have crafted through the Horadric Cube"*.
  Blizzard eliminó ese límite **nueve días antes**, el 16/07/2026. Es correcta en todo lo demás; en esto,
  no. Detalle y prueba en §5.
- ⚠️ **La guía "How to Farm Mythic Uniques (Season 14)" de Icy Veins está desactualizada pese al título.**
  Lista 12 Míticos, no menciona Paladín, no menciona Fragmentos de Pandemónium ni el Cubo, y da a
  Doombringer/The Grandfather clases que ya no corresponden. No la he usado para números.
- ⚠️ **Existe ya un PTR 3.2.0 (Season 15).** Nada de él aplica hoy. Lo que sale de ahí va marcado ⚠️PTR.

**Maxroll NO devolvió 403** en esta investigación (sí lo hizo **mobalytics.gg**, HTTP 403).
**reddit.com está bloqueado** para mi rastreador (error de dominio no accesible), así que no hay
contraste de comunidad en este informe. Va en "No encontrado".

---

## 2. EL MODELO CAMBIÓ: "Mythic 3.0" — léelo antes que cualquier lista

Este es el punto donde más gente se equivoca, y donde una lista de "los Míticos del juego" copiada de
temporadas anteriores te haría perder los fragmentos.

**En Season 14, Mítico dejó de ser una rareza (rarity) y pasó a ser una *calidad* de objeto (item quality).**

> "Mythic, instead of being an item Rarity, is now a modifiable Item Quality."
> — [Blizzard, The 3.1 PTR](https://news.blizzard.com/en-us/article/24259077/the-3-1-ptr-what-you-need-to-know) ⚠️ origen PTR, **confirmado en vivo** por [Maxroll, guía de temporada, act. 13/07/2026](https://maxroll.gg/d4/resources/season-guide)

Consecuencias prácticas:

| Antes (temporadas previas) | Ahora (S14) |
|---|---|
| Había ~12-13 objetos que *eran* Míticos | **Cualquier Único puede ser Mítico** |
| Cazabas *ese* objeto concreto | Cazas la *calidad* sobre el Único que te interesa |
| El Mítico tenía tiradas variables | **Todo Mítico es Ancestral, sube su Poder Único un +30% y clava el resto de afijos al máximo** |

El +30% y el "todos los afijos al máximo": [Blizzard 3.1 PTR](https://news.blizzard.com/en-us/article/24259077/the-3-1-ptr-what-you-need-to-know) ⚠️PTR, y [Maxroll guía de temporada 13/07/2026](https://maxroll.gg/d4/resources/season-guide) — *"unique powers increased by 30%… all non-unique affixes roll at maximum values"*.

**Por eso hay dos categorías distintas y el vocabulario importa:**

- **Míticos Icónicos (Iconic Mythics):** los objetos legendarios de siempre (Shako, Grandfather…). Siguen
  existiendo como objetos con nombre propio. Caen del suelo y de jefes.
- **Míticos crafteados:** *cualquier* Único llevado a calidad Mítica en el Cubo Horádrico o en el
  vendedor con Chispas. **Es la vía de tu build.**

**Prueba directa del mecanismo en los datos del juego** (datamining, fichero 3.1.0.72698). El texto de
*Mantle of the Grey* trae un condicional literal `{if:IsMythic}`, y el valor cambia de tirada aleatoria a
número fijo elevado:

```
Affix_Value_2 = S14_Mythic_UniquePotency>0
                ? 0.06*(1+S14_Mythic_UniquePotency)   <- versión Mítica: máximo * (1+potencia)
                : FloatRandomRangeWithInterval(10,0.04,0.06)   <- versión normal: 4%-6% aleatorio
```

Es decir: la versión Mítica **no tira dado**, coge el tope (0,06) y le aplica la potencia. Con el +30%
declarado por Blizzard eso da 0,078 (7,8%) por punto de Resolve. Sobre los 16 puntos que consume el
objeto: **~124,8% de daño aumentado frente a ~96% del mejor roll no-mítico.** El atributo
`S14_Mythic_UniquePotency` existe en la tabla de atributos con `defaultValue: 0` (se aplica en
tiempo de ejecución), así que **el 30% concreto lo pongo por la fuente de Blizzard, no por el fichero.**

---

## 3. Lista completa de Míticos Icónicos hoy, y cuáles sirven al Paladín

Extraída del fichero de datos del juego (`magicType: 4`), filtrando duplicados de Charm/Crucible.
**Esto es datamining sobre 3.1.0.72698.** Los textos de poder son los reales del juego; los valores
numéricos pueden haberse tocado en 3.1.1-3.1.3.

La columna "Paladín" sale del `classFilter` del propio objeto (índice 6 = Paladin, verificado contra
`d['classes']`: 0 Sorcerer, 1 Druid, 2 Barbarian, 3 Rogue, 4 Necromancer, 5 Spiritborn, **6 Paladin**, 7 Warlock).

| Mítico Icónico | Ranura | Paladín | Qué hace (texto del juego, resumido) |
|---|---|:--:|---|
| **Harlequin Crest** ("Shako") | Casco | **Sí** | **+6 rangos a todas las habilidades**; +10% reducción de enfriamiento, +2000 Vida, +18 recurso máx., +1500 Armadura |
| **Tyrael's Might** | Pecho | **Sí** | +20% Reducción de daño; a Vida llena tus habilidades lanzan una descarga divina (×3 daño de arma); +400 y +25% Resist. |
| **Shroud of False Death** | Pecho | **Sí** | Al recibir daño mortal: curas al máximo + barrera del 100% de Vida 3 s y empujas. Se agota hasta volver a la ciudad |
| **Ring of Starless Skies** | Anillo | **Sí** | Gastar recurso reduce coste y da **+10%x daño por acumulación, hasta +50%x** (3 s); +15% vel. ataque, +12% prob. crítico |
| **Melted Heart of Selig** | Amuleto | **Sí** | El daño va al recurso antes que a la Vida y se reduce drásticamente. Recurso ×2, **Vida máxima −75%** |
| **The Grandfather** | Espada 2M | **Sí** | **+120% Daño de Golpe Crítico**; +110 a todas las estadísticas, +Vida, +10 recurso |
| **Doombringer** | Espada 1M | **Sí** | Golpe de Suerte hasta 40%: daño de Sombra en área y −25% daño enemigo 5 s; +160 stats, +15% Vida máx. |
| **El'Druin, Sword of Justice** | Espada 1M | **Sí** | Matar un grupo de élites **reduce enfriamientos 10 s** (durante 12 s); +160 stats, +2600 Vida, +30% daño multiplicativo |
| **Andariel's Visage** | Casco | **Sí** | Golpe de Suerte hasta 20%: nova de veneno (40% del daño en 5 s); **+15% velocidad de ataque**, +666 Resist. |
| **Heir of Perdition** | Casco | **Sí** | Favor de la Madre: roba 15% prob. crítico a aliados cercanos y da **+15%x daño** permanente |
| **Ahavarion, Spear of Lycander** | Bastón | No | Efecto de santuario aleatorio al matar élite | 
| **Nesekem, the Herald** | Guja | No | Marca enemigos: vulnerables y crítico garantizado |
| **Shattered Vow** | Arma de asta | No | Ejecuta enemigos con más daño por tiempo que Vida restante |

**Total: 13 Míticos Icónicos. 10 los puede llevar un Paladín.** Los 3 excluidos son por restricción de
clase (Bastón/Guja/Asta no son armas de Paladín).

> **Nota sobre un decimocuarto:** el fichero contiene además **"The Cow King's Crown"** (Casco, todas las
> clases) con un texto de broma ("+1 Damage to Two-Legged Enemies", "Moobility damage while mooving",
> bonos por día de la semana). Es un objeto humorístico y **no lo cuento como objetivo de farmeo**. Si
> alguna web te dice que hay 14 Míticos, probablemente lo esté contando.

**Además, con calidad Mítica (`magicType: 4`) pero que no son equipo de combate:** *Resplendent Spark*
(reactivo de crafteo), *The Empyrean Eye* (gema), y cuatro Sellos Horádricos (*Mythic Unique Horadric
Seal*, *Seal of the Diamond Mind*, *Seal of the Golden Epiphany*, *Seal of the Severed Finger*).
⚠️ El hotfix 3.1.1a **quitó** la posibilidad de aplicar la calidad Mítica a Charms y Sellos: era un bug.

---

## 4. De dónde salen: las cuatro vías

### 4.1 Cubo Horádrico — la vía principal, y la contradicción 4 vs 5 RESUELTA

**Veredicto: 4 Fragmentos de Pandemónium. La cifra 5 está muerta desde el 14/07/2026.**

Cómo se resuelve, con la cronología:

| Fecha | Fuente | Dice | Estado |
|---|---|---|---|
| 24/06/2026 | [Maxroll, "Hunt the Death Cult"](https://maxroll.gg/d4/news/hunt-the-death-cult-in-season-of-death-awakening) | "5 Pandemonium Fragments" | Correcto **entonces** |
| 13/07/2026 | [Maxroll, guía de temporada](https://maxroll.gg/d4/resources/season-guide) | "5 Pandemonium Fragments per mythic conversion" | Correcto **hasta el día siguiente** |
| **14/07/2026** | **[Blizzard, notas de parche 3.1.1, build 72836](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes)** | *"Reduced the cost of the Upgrade to Mythic recipe on the Horadric Cube from 5 to 4 Pandemonium Fragments."* | **VIGENTE** |
| 28/07/2026 | [Blizzard 3.1.2, build 73020](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) | No toca el coste | — |
| 12/08/2026 | [Blizzard 3.1.3, build 73224](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) | No toca el coste | — |

La contradicción no es un error de nadie: es que **las dos páginas de Maxroll son de la víspera del parche.**
Comprobado expresamente que ninguna sección posterior (3.1.2, 3.1.3) vuelve a modificar el número.

**Receta vigente:**

| Concepto | Valor | Fuente |
|---|---|---|
| Ingrediente 1 | **1 Único de la ranura que quieras, con 850+ de Poder de Objeto** | [Maxroll 24/06/2026](https://maxroll.gg/d4/news/hunt-the-death-cult-in-season-of-death-awakening) |
| Ingrediente 2 | **4 Fragmentos de Pandemónium** | [Blizzard 3.1.1](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) |
| Nombre de la receta | **"Craft"** (antes "Upgrade") | [Blizzard 3.1.2](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) |
| Requisito de dificultad | Torment I o superior | [Maxroll guía de temporada](https://maxroll.gg/d4/resources/season-guide) |
| Nivel | 70 | [Maxroll guía de temporada](https://maxroll.gg/d4/resources/season-guide) |

**⚠️ EL DETALLE QUE MÁS DINERO CUESTA — el resultado es ALEATORIO dentro de la ranura.**
No conviertes *ese* Único en Mítico. Metes un Único de pecho y sale **un Mítico de pecho cualquiera**.

> "The upgrade yields a random item of the same slot, not the identical item."
> — [Maxroll, 24/06/2026](https://maxroll.gg/d4/news/hunt-the-death-cult-in-season-of-death-awakening)

Confirmado por dos vías independientes:
- Blizzard 3.1.1: *"The Upgrade to Mythic recipe in the Horadric Cube now always creates an item for the same gear slot."* (si fuera 1:1 esta nota no tendría sentido)
- Icy Veins, sobre S15: la crítica a S14 es *"the randomness of this recipe, in that the item received would be a random item of the same slot"* — [Icy Veins, cambios de S15](https://www.icy-veins.com/d4/news/mythic-unique-crafting-changes-coming-to-diablo-4-season-15/) ⚠️ese artículo describe PTR de S15

**Por eso "priorizar un Mítico" significa en realidad "elegir en qué RANURA gastas los fragmentos".**
Es la clave para leer bien el orden de §6.

Restricciones añadidas por parches: un Mítico **no** puede usarse como ingrediente
(3.1.3); Charms y Sellos **ya no** admiten calidad Mítica (3.1.1a).

**De dónde salen los Fragmentos de Pandemónium** (`S14_Seasonal_Currency` en el fichero de datos):

| Origen | Detalle | Fuente |
|---|---|---|
| Corrupted Reaper (jefe estacional) | **Hasta 2 por muerte, escalando con Tormento** | [Blizzard 3.1.1](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) |
| Recompensa repetible "Glints of Hope" (reputación) | **Garantiza 1 fragmento** | [Blizzard 3.1.1](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes) |
| Tablero de reputación de temporada | — | [Maxroll guía de temporada](https://maxroll.gg/d4/resources/season-guide) |
| Cachés Resplandecientes (Resplendent Caches) | — | [Maxroll guía de temporada](https://maxroll.gg/d4/resources/season-guide) |

### 4.2 Ruta del Joyero / Herrero con Chispas Resplandecientes y runas — CONTRADICTORIA, no la uses a ciegas

Aquí **no puedo darte un número único con confianza**, y prefiero decírtelo a inventarlo. Las fuentes
buenas se contradicen entre sí **e incluso Maxroll consigo mismo**, y discrepan hasta en qué vendedor es:

| Fuente (fecha) | Vendedor | Chispas | Runas | Oro | Resultado |
|---|---|---|---|---|---|
| [Maxroll, chuleta de crafteo (14/07/2026)](https://maxroll.gg/d4/resources/crafting-cheat-sheet) | **Herrero**, receta por ranura | **3** | 3 runas concretas | **5.000.000** | Mítico aleatorio de esa ranura |
| [Maxroll, chuleta de crafteo (14/07/2026)](https://maxroll.gg/d4/resources/crafting-cheat-sheet) | **Joyero**, totalmente aleatorio | **2** | — | **50.000.000** | Mítico aleatorio |
| [Maxroll, "Hunt the Death Cult" (24/06/2026)](https://maxroll.gg/d4/news/hunt-the-death-cult-in-season-of-death-awakening) | Joyero | **3** | **18** runas concretas | — | Mítico de la ranura |
| [Icy Veins, guía de farmeo](https://www.icy-veins.com/d4/guides/how-to-farm-uber-uniques/) | Joyero | **2** | 3× 6 runas legendarias | — | Mítico | 
| [Icy Veins, guía de farmeo](https://www.icy-veins.com/d4/guides/how-to-farm-uber-uniques/) | Herrero | **2** | — | — | Caché de Mítico |

Lo único en lo que **todas** coinciden: la ruta con Chispas **existe**, cuesta **entre 2 y 3 Chispas
Resplandecientes**, y en S14 **ya no permite elegir el Mítico exacto** — como mucho la ranura.

> "In Season 14, players can now only pick the desired item slot for their Mythic Unique, and hope that they get exactly what they want."

El fichero de datos respalda que el **Herrero** es el vendedor de la caché: existe el objeto
`Mythic Unique Cache` con clave interna **`BlackSmith_MythicCrafting`**.

**Mi recomendación operativa:** ábrelo en el juego y **lee la receta en pantalla antes de gastar**.
La pantalla del jugador gana a cualquier web. Va a "No encontrado" como número no confirmado.

⚠️ **Aviso extra:** circula un artículo de Icy Veins titulado *"Do Not Waste Resplendent Sparks on Diablo 4's
New Mythic System"* (publicado la primera semana de la temporada). **Su razonamiento ya no aplica**: se
apoyaba explícitamente en que *"Season 14 limits wearable crafted Mythics to one per character"*, límite
que Blizzard eliminó el 16/07/2026 (§5). No tomes esa decisión con ese artículo.

### 4.3 Caída natural: jefes de guarida (Lair Bosses)

**Requisito mínimo para cualquier Mítico: Tormento I (Torment I) o superior.**
— [Icy Veins, sistema de jefes de guarida](https://www.icy-veins.com/d4/guides/lair-boss-system-guide/) y [Maxroll, chuleta de botín de jefes, act. 16/08/2026](https://maxroll.gg/d4/resources/boss-loot-table-cheat-sheet)

| Nivel | Jefes | Material de invocación | De dónde sale el material |
|---|---|---|---|
| Iniciado (Initiate) | Varshan, Grigoire, Beast in the Ice, Lord Zir, Urivar | **1× Llave de Guarida** (Lair Key) | Planes de Guerra, Marea Infernal, jefes mundiales, eventos de Legión, caché del Árbol de los Susurros |
| Superior (Greater) | Duriel, Andariel, Harbinger of Hatred, Bloody Butcher | **1× Llave de Guarida Superior** (Greater Lair Key) | **Solo** de matar jefes de nivel Iniciado |
| Exaltado (Exalted) | Belial | **2× Betrayer's Husk** | Emboscada de Belial tras matar un jefe de guarida |
| Exaltado (Exalted) | Mephisto | **1× Crux of the False Prophet** | — |
| Estacional | **Corrupted Reaper** | **Superior Lair Key** para abrir su Hoard | Deathtoll Chambers |

**Cambio de modelo importante (S14):** ya **no** hay tabla de "este jefe suelta este Mítico".

> "Any Unique drop has a chance to be **Mythic** quality" — todos los jefes pueden soltar cualquier Mítico Icónico.
> — [Maxroll, chuleta de botín de jefes, act. 16/08/2026](https://maxroll.gg/d4/resources/boss-loot-table-cheat-sheet) *(la más reciente de todas las páginas usadas)*

Un bug relevante ya corregido: hasta 3.1.1, **los jefes de guarida no soltaban Únicos como Míticos**.
Blizzard lo arregló el 14/07/2026 (*"Fixed an issue preventing certain sources of Uniques from dropping as
Mythic, including Lair Bosses"*). Si leíste que "los jefes no dan Míticos", eso era el bug.

**El jefe estacional, Corrupted Reaper** — [Maxroll, guía del jefe, act. 10/07/2026](https://maxroll.gg/d4/bosses/corrupted-reaper-boss-guide):
- Ubicación: **Zarbinzet, Hawezar** (zona de Pandemónium / Pandemonium Threshold).
- Requiere **Tormento I o superior**.
- **Da las mejores probabilidades directas de Mítico Y de Fragmentos de Pandemónium de toda la temporada** ([Maxroll guía de temporada](https://maxroll.gg/d4/resources/season-guide)).
- 3.1.1a **subió sus tasas**: *"Increased the drop rates of Mythic and Iconic Unique Items from the Corrupted Reaper."*
- ⚠️ **Discrepancia sin resolver sobre las llaves:** la misma página de Maxroll dice en un sitio *"two Superior Boss Lair Keys"* y en otro *"1x Superior Lair Key to open the Hoard"*. **Cuéntalas en el juego.** Va a "No encontrado".
- Las Superior Lair Keys salen de **Deathtoll Chambers**, minimazmorras de una sala a las que se entra por portales de Realmwalker o mazmorras de pesadilla con afijo de Ruptura ([Maxroll guía de temporada](https://maxroll.gg/d4/resources/season-guide)).

### 4.4 Rango de Temporada (Season Rank) — Míticos GRATIS, y una trampa

Esta es la vía que más te conviene y la que casi nadie aprovecha bien.

> "Progress through Season Ranks to earn **class-specific Mythic Uniques** from Mythic Unique Caches."
> — [Maxroll, Rango de Temporada, act. 13/07/2026](https://maxroll.gg/d4/resources/season-journey)

| Rango | Recompensa | Fuente |
|---|---|---|
| Rango 3 | 1× Caché de Mítico (Mythic Unique Journey Cache) | [Maxroll, act. 13/07/2026](https://maxroll.gg/d4/resources/season-journey) |
| Rango 6 | 1× Chispa Resplandeciente | idem |
| Rango 7 | 1× Caché de Mítico | idem |
| Rango 8 | 1× Caché de Mítico + 1× Chispa Resplandeciente | idem |
| Rango 9 | **2× Cachés de Mítico** + 7× Chispas Resplandecientes | idem |
| **Total** | **5 Cachés de Mítico** | idem |

El objeto existe en el fichero de datos como `Mythic Unique Journey Cache` (clave `Mythic_Cache`,
tipo `JourneyCache`), lo que confirma el mecanismo por segunda vía.

🔴 **LA TRAMPA, y es la acción más urgente de todo este informe.**
El Rango de Temporada es **progreso de cuenta**, así que tu nigromante de 70 probablemente ya te ha
desbloqueado varias de estas cachés. Maxroll dice que los Míticos que dan son **específicos de clase**.
Si eso significa "de la clase que la abre" —que es lo que sostienen varias webs, aunque **ninguna de las
fiables lo dice con esas palabras**— abrirlas con el nigromante te tira 5 Míticos de Paladín a la basura.

**No las abras hasta comprobarlo en pantalla con el Paladín delante.** El coste de esperar es cero;
el de equivocarse, la temporada entera. La confirmación exacta va a "No encontrado".

---

## 5. El límite de "un solo Mítico crafteado equipado": ELIMINADO — verificado

**Estado: NO existe. Eliminado el 16/07/2026 en el hotfix 3.1.1a. Sigue eliminado en 3.1.3.**

Fuente primaria, foro oficial de Blizzard:

> **"Removed the 'one-crafted Mythic' equipment restriction on Mythic items."**
> — [Blizzard, parche 3.1.1a, 16/07/2026 (foro oficial)](https://us.forums.blizzard.com/en/d4/t/311a-patch-july-16-2026/263234)

Corroboración independiente:
- [Icy Veins, 16/07/2026](https://www.icy-veins.com/d4/news/diablo-4-season-14-hotfix-crafted-mythic-restriction-removed-and-mythic-drop-rate-increased/) — mismo texto literal.
- [Icy Veins, cambios de S15](https://www.icy-veins.com/d4/news/mythic-unique-crafting-changes-coming-to-diablo-4-season-15/) — *"The one-crafted Mythic equip limit was previously removed in Season 14, allowing players to equip multiple crafted Mythics."*

Comprobado además que **ni 3.1.2 (28/07) ni 3.1.3 (12/08) lo reintroducen**.

**Qué webs siguen diciendo lo contrario (y por qué):** la guía de tu build en Maxroll (act. 25/07/2026),
la guía de temporada de Maxroll (act. 13/07/2026, anterior al hotfix), el artículo de Chispas de Icy Veins
(principios de julio) y prácticamente todos los sitios SEO. **Ignóralo.**

⚠️ **Season 15 (PTR 3.2.0) — NO ES HOY:** está previsto que el límite de "1 objeto crafteado" **vuelva**,
pero **solo** para lo hecho en el Cubo Horádrico; lo del Herrero y el Joyero no llevará etiqueta de
crafteado. También llegaría una receta 1:1 que conserva afijos, temple y maestría del objeto original.
Fuente: [Icy Veins sobre S15](https://www.icy-veins.com/d4/news/mythic-unique-crafting-changes-coming-to-diablo-4-season-15/). **Nada de esto está vivo.**

👉 **Traducción práctica para ti:** durante estas 4 semanas puedes **craftear y equipar los tres Míticos
del orden de §6 simultáneamente**. Es una ventana que se cierra con la temporada.

---

## 6. ORDEN CONCRETO para Shield Charge Paladin

**Recuerda §4.1: el Cubo da un Mítico ALEATORIO de la ranura. "Ir a por Mantle of the Grey" = gastar
los 4 fragmentos metiendo un Único de PECHO de 850+.**

La guía de la build da este orden de crafteo — [Maxroll, Shield Charge Paladin, act. 25/07/2026](https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide):

| Orden | Objetivo | Ranura donde gastas | Qué hace (texto del juego, datamining 3.1.0) |
|:--:|---|---|---|
| **1º** | **Mantle of the Grey** | **Pecho** | Juggernaut Oath agranda tus habilidades Juggernaut un 25% pero consume hasta **16 de Resolve**, dando **~6%x (7,8%x si Mítico) de daño Juggernaut por punto consumido** |
| **2º** | **Tibault's Will** | **Pantalones** | **+15-20%x de daño** y +50 de regeneración de recurso mientras eres Imparable y 5 s después |
| **3º** | **Herald of Zakarum** | **Escudo** | **+40-50% de Fuerza, Resistencia, Armadura y probabilidad de Retribution**; Retribution +50% de tamaño |
| (solo variante *Push*) | **Blood-Mad Idol** | Amuleto | Siempre Berserking, pero recibes 200%x de daño como Quemadura; Berserking da **+80-100%x de daño** adicional |

En la variante *Push* el orden es: Mantle of the Grey → **Blood-Mad Idol** → Tibault's Will → Herald of Zakarum.

### Por qué Mantle of the Grey es el primero — argumento de datos, no de opinión

De **todos los Únicos del juego (1.075 entradas de calidad Única en el fichero), solo DOS** tienen en el fichero de datos la fórmula condicional explícita
`{if:IsMythic}` que sustituye la tirada aleatoria por el valor tope multiplicado por la potencia Mítica.
Uno es *Protean Heart* (amuleto de Spiritborn). **El otro es Mantle of the Grey.**

Traducido: en este objeto concreto, pasar a Mítico **no es un +30% genérico sobre un roll variable, sino
un salto de "4%-6% aleatorio" a "7,8% fijo" por punto de Resolve.** Sobre los 16 puntos que consume:

| Versión | Por punto | ×16 puntos consumidos |
|---|---|---|
| Único con roll malo | 4%x | ~64%x daño Juggernaut |
| Único con roll perfecto | 6%x | ~96%x daño Juggernaut |
| **Mítico** | **7,8%x** | **~124,8%x daño Juggernaut** |

*(El 7,8% sale de aplicar el +30% oficial de Blizzard a la fórmula datamineada. Marcado como cálculo, no
como cifra leída en pantalla.)*

Además encaja con el resto de tu build: la guía te hace llegar al **tope de 30 de Resolve** templando
"+4 Máximo de acumulaciones de Resolve" en casco, pecho y pantalones.

### Y los Míticos Icónicos, ¿dónde quedan?

**La guía de la build no recomienda NINGUNO** de los Icónicos (Harlequin Crest, Tyrael's Might, Ring of
Starless Skies, The Grandfather, Shroud of False Death, Melted Heart of Selig, Andariel's Visage, Heir of
Perdition, El'Druin) — verificado preguntando expresamente por cada uno sobre
[la página de Maxroll](https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide).

Motivo estructural: tu daño sale de **Thorns/Retribution y del Resolve**, no de multiplicadores genéricos
de crítico o de recurso. *The Grandfather* es espada a dos manos (te quita el escudo, que es tu build
entera). *Melted Heart* te quita el 75% de la Vida. *Starless Skies* premia gastar recurso.

**Pero no los deseches si caen gratis.** Si una caché del Rango de Temporada te suelta un **Harlequin
Crest** (+6 rangos a todas las habilidades) o un **Tyrael's Might** (+20% reducción de daño), son mejoras
sólidas y **no compiten con tus tres crafteos** (ranuras distintas: casco y pecho… ojo, Tyrael's Might sí
compite con Mantle of the Grey por el pecho — en ese caso, Mantle gana para esta build).

---

## 7. Accionable ya, en orden

1. **Antes que nada: NO abras cachés de Mítico del Rango de Temporada con el nigromante** hasta verificar
   en pantalla si el contenido depende de la clase que la abre (§4.4).
2. **Sube a Tormento I** en cuanto puedas: por debajo, **cero Míticos**, ni de jefes ni de crafteo.
3. **Reclama el Rango de Temporada con el Paladín.** Rangos 3, 7, 8 y 9 = **5 Cachés de Mítico gratis**.
   Es la vía sin RNG y ya tienes progreso de cuenta hecho.
4. **Farmea Corrupted Reaper** (Zarbinzet, Hawezar): mejor fuente única de Míticos **y** de Fragmentos.
   Llaves desde Deathtoll Chambers (Realmwalkers / mazmorras de pesadilla con afijo de Ruptura).
5. **Guarda Únicos de 850+ de PECHO, PANTALONES y ESCUDO.** Son la munición del Cubo. No los recicles.
6. **Junta 4 Fragmentos → Cubo → mete un Único de PECHO.** Repite hasta que salga Mantle of the Grey.
   Luego pantalones (Tibault's Will) y escudo (Herald of Zakarum).
7. **Equípate los tres a la vez.** El límite se eliminó el 16/07. Si tu guía dice otra cosa, está caducada.
8. **Antes de gastar Chispas Resplandecientes, lee la receta en pantalla** (§4.2: las fuentes se
   contradicen entre 2 y 3 Chispas y entre Herrero y Joyero).
9. **Ventana temporal:** en Season 15 vuelve el límite de 1 crafteado para el Cubo ⚠️PTR. Craftea ahora.

---

## Fuentes

Páginas efectivamente abiertas y leídas para este informe (19/08/2026):

**Oficiales (Blizzard)**
1. https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes — Notas de parche 3.1.3 (build 73224, 12/08/2026), 3.1.2 (73020, 28/07/2026), 3.1.1 (72836, 14/07/2026), 3.1.0 (72592, 30/06/2026). Fuente de "de 5 a 4 Fragmentos".
2. https://us.forums.blizzard.com/en/d4/t/311a-patch-july-16-2026/263234 — Hotfix 3.1.1a, 16/07/2026. Fuente primaria de la eliminación del límite de Mítico crafteado.
3. https://news.blizzard.com/en-us/article/24259077/the-3-1-ptr-what-you-need-to-know — ⚠️ PTR de 3.1: Mítico como calidad, +30% de Poder Único.

**Maxroll (sin 403 en esta sesión)**
4. https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide — act. 25/07/2026. Orden de crafteo de Míticos. ⚠️ contiene la línea caducada del límite de 1 crafteado.
5. https://maxroll.gg/d4/resources/season-guide — act. 13/07/2026. Mythic 3.0, Fragmentos, Corrupted Reaper, Deathtoll Chambers. ⚠️ da 5 fragmentos (víspera del parche).
6. https://maxroll.gg/d4/resources/crafting-cheat-sheet — act. 14/07/2026. Recetas con Chispas y oro.
7. https://maxroll.gg/d4/resources/boss-loot-table-cheat-sheet — act. 16/08/2026. La más reciente: cualquier Único puede salir Mítico, Tormento I mínimo.
8. https://maxroll.gg/d4/resources/season-journey — act. 13/07/2026. Cachés de Mítico por rango.
9. https://maxroll.gg/d4/bosses/corrupted-reaper-boss-guide — act. 10/07/2026. Ubicación, llaves, Tormento I.
10. https://maxroll.gg/d4/news/hunt-the-death-cult-in-season-of-death-awakening — 24/06/2026. Requisito 850+, resultado aleatorio por ranura, ruta del Joyero.
11. https://maxroll.gg/d4/news/lord-of-hatred-3-1-2-patch-notes — parche 3.1.2, 28/07/2026.
12. https://maxroll.gg/d4/wiki/uniques — ⚠️ act. 23/05/2026, **anterior a la temporada**. No usada para números.

**Icy Veins**
13. https://www.icy-veins.com/d4/news/diablo-4-season-14-hotfix-crafted-mythic-restriction-removed-and-mythic-drop-rate-increased/ — 16/07/2026. Corrobora el hotfix.
14. https://www.icy-veins.com/d4/news/diablo-4-season-14-patch-notes-increased-mythic-and-pandemonium-fragment-drop-rates/ — 14/07/2026.
15. https://www.icy-veins.com/d4/guides/lair-boss-system-guide/ — niveles de jefes y materiales de invocación.
16. https://www.icy-veins.com/d4/news/mythic-unique-crafting-changes-coming-to-diablo-4-season-15/ — ⚠️ describe PTR de S15; corrobora que el límite se quitó en S14.
17. https://www.icy-veins.com/d4/guides/how-to-farm-uber-uniques/ — ⚠️ **desactualizada pese al título "(Season 14)"**. Documentada como ejemplo de dato muerto, no usada para números.
18. https://www.icy-veins.com/d4/news/do-not-waste-resplendent-sparks-on-diablo-4s-new-mythic-system/ — ⚠️ principios de julio; su tesis depende del límite ya eliminado.
19. https://www.icy-veins.com/d4/news/diablo-4-season-14-lets-every-unique-become-mythic/ — ⚠️ basada en notas del PTR, previa al lanzamiento.

**Datamining (declarado como tal)**
20. https://assets-ng.maxroll.gg/d4-tools/game/data.min.json — fichero de datos del planificador de Maxroll. HTTP 200, 11.606.292 bytes. **Se declara `"version":"3.1.0.72698"`, un parche por detrás del vivo (3.1.3/73224).** Usado para: lista de Míticos (`magicType: 4`), textos de poder, `classFilter` de Paladín (índice 6), fórmula `S14_Mythic_UniquePotency` de Mantle of the Grey, y existencia de `Pandemonium Fragment` (`S14_Seasonal_Currency`), `Superior Lair Key`, `Mythic Unique Cache` (`BlackSmith_MythicCrafting`) y `Mythic Unique Journey Cache`.

**Intentos fallidos (declarados)**
21. https://mobalytics.gg/diablo-4/builds/paladin-shield-charge-endgame-build-guide — **HTTP 403**. No leída.
22. https://www.wowhead.com/diablo-4/guide/classes/paladin/shield-charge-build-overview — abierta pero **sin contenido de equipo recuperable**; además se fecha 2026/03/08, ⚠️ anterior al lanzamiento del Paladín (28/04/2026), probablemente material de PTR.
23. reddit.com/r/diablo4 — **dominio bloqueado** para el rastreador. Sin contraste de comunidad.

---

## No encontrado

Huecos declarados. **Nada de esto se ha rellenado por inferencia.**

1. **Coste exacto de la ruta de Chispas Resplandecientes.** Las fuentes fiables se contradicen entre
   **2 y 3 Chispas**, entre **Herrero y Joyero**, y entre **3 y 18 runas**; el oro aparece como
   5.000.000 o 50.000.000 según la receta. **Léelo en pantalla antes de gastar.** (§4.2)
2. **Qué runas concretas pide la receta del Joyero/Herrero.** Ninguna fuente abierta las nombra.
3. **Cuántas Superior Lair Keys hace falta para el Corrupted Reaper.** La propia página de Maxroll dice
   "two" y "1x" en párrafos distintos. Cuéntalas en el juego.
4. **Si las Cachés de Mítico del Rango de Temporada dan el objeto de la clase que las abre.** Maxroll dice
   "class-specific" pero no aclara el mecanismo. Es la duda más cara del informe: no las abras con el
   nigromante hasta comprobarlo. (§4.4)
5. **Probabilidades numéricas de caída de Mítico por jefe y por nivel de Tormento.** No publicadas por
   Blizzard. Las cifras tipo "~2%" que circulan vienen de páginas desactualizadas; no las reproduzco.
6. **Valores numéricos de los Míticos en el parche vivo 3.1.3.** Los de §3 salen del fichero 3.1.0.72698.
   Si 3.1.1/3.1.2/3.1.3 ajustaron alguno, aquí no se vería. (Sí consta que *Heir of Perdition* y
   *Shroud of False Death* recibieron cambios en 3.1, pero no he podido leer las cifras exactas
   posteriores en fuente fiable.)
7. **Ranking de daño (DPS) entre Míticos.** No existe fuente medida y fiable abierta en esta sesión.
   **No lo invento** — es exactamente lo que te dieron mal la última vez. El orden de §6 es el orden de
   *la guía de la build* más un argumento de datos para el primer puesto, no una simulación de daño.
8. **Contraste de comunidad (reddit).** Dominio bloqueado para el rastreador.
9. **Confirmación oficial de Blizzard del +30% en texto de parche vivo.** La cifra viene del artículo del
   ⚠️PTR de 3.1 y de Maxroll; no la he visto repetida en las notas de 3.1.0-3.1.3.
