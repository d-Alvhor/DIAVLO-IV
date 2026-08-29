# Builds de Nigromante de Esbirros CON EXPANSIONES — Season 14 "Death Awakening"

**Fecha de la investigación:** 19-20 agosto 2026
**Parche vivo anclado:** 3.1.3 build #73224 (12 agosto 2026) — [notas oficiales](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes)
**Datamining usado:** `assets-ng.maxroll.gg/d4-tools/game/data.min.json`, versión declarada en el propio fichero: **3.1.0.72698**

> ⚠️ **Desfase declarado.** El fichero de datos del juego está en 3.1.0; el parche vivo es 3.1.3. He verificado línea a línea en las notas oficiales que **3.1.1, 3.1.2 y 3.1.3 no tocan nada de Nigromante ni de esbirros salvo un arreglo visual** (ver §1). Con eso, los datos de 3.1.0 son válidos para todo lo de este informe. Cualquier cosa que no haya visto escrita va en "No encontrado" al final.

---

## 0. Resumen ejecutivo — lo que importa

| Pregunta | Respuesta corta |
|---|---|
| ¿Existen "Naz Mages" y "Reaper Summoner"? | Sí, ambas en Icy Veins, actualizadas **3 julio 2026** |
| ¿Gargantua es real y es lo que le falta? | Sí. Es **una de las tres variantes de la habilidad Gólem**, y es la variante bloqueada tras Lord of Hatred |
| ¿Merece la pena cambiar a 27 días del fin? | **Sí, pero solo la mitad barata.** El 80% de la ganancia son puntos de habilidad (gratis, hoy). El otro 20% es equipo y charms que no le da tiempo |
| ¿Tier list? | **Las dos fuentes preferentes se contradicen.** Icy Veins: Naz Mages = S. Maxroll: Minion Necro = B. Detalle y explicación en §8 |
| Peligro para el dúo | **Los charms/talismanes requieren Lord of Hatred.** Si la pareja no lo ha comprado, no puede montar ninguna de estas dos builds tal cual |

---

## 1. Verificación del parche: ¿está viva la información de julio?

Las dos guías de Icy Veins se actualizaron el **3 de julio de 2026** (`dateModified` en el HTML: `2026-07-03T12:05:00+00:00` en Naz Mages, `2026-07-03T12:04:16+00:00` en Reaper Summoner). El parche vivo es del 12 de agosto. Hay seis semanas de hueco. Esto es lo que pasó en ese hueco:

| Parche | Build | Fecha | ¿Toca Nigromante / esbirros? |
|---|---|---|---|
| 3.1.3 | #73224 | 12 ago 2026 | Solo esto: *"Fixed an issue where Necromancer Shadow skills would obscure the Corrupted Reaper."* Visual. Nada más |
| 3.1.2 | #73020 | 28 jul 2026 | **Nada** de Nigromante. Sí: *"Fixed an issue where Mythic Unique items could not be recycled"* |
| 3.1.1 | #72836 | 14 jul 2026 | **Nada** de Nigromante. Sí: *"Reduced the cost of the Upgrade to Mythic recipe on the Horadric Cube from 5 to 4 Pandemonium Fragments"* |
| 3.1.0 | #72592 | 30 jun 2026 | **Sí, mucho.** Ver abajo |

Fuente de las cuatro filas: <https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes>

**Conclusión:** no hay cambios de equilibrio de clase desde el 30 de junio. Las guías de julio siguen siendo estructuralmente válidas. **Pero** el 3.1.0 (30 junio) es *anterior* a la actualización de las guías (3 julio) y aun así una de ellas publica un número muerto — ver §1.1.

### 1.1 🚩 Dato muerto cazado en Icy Veins

La página de Naz Mages describe hoy el anillo así:

> *"Signet of Pelghain — Your Freeze effects cause enemies to permanently take 20%[x] [15 – 20]% increased damage from you for each second they are Frozen."*
> — <https://www.icy-veins.com/d4/guides/mendeln-summoner-necromancer-build/>

Las notas oficiales del 3.1.0, **publicadas tres días antes de esa actualización**, dicen:

> *"Signet of Pelghain — Damage bonus reduced from 15-20% to 10-15% per second. Enemies are Frozen and now only applies to Cold Damage."*
> — <https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes>

**El valor real es 10-15% por segundo, no 15-20%.** La guía sí menciona el cambio en su sección "Season Updates" ("Signet of Pelghain limited to cold damage") pero **no corrigió el número en la tabla de equipo**. Es exactamente el patrón que ya le ha costado dos veces: el aviso al final no arregla la tabla del principio.

### 1.2 Otros números del 3.1.0 que mandan sobre las guías

Todos de <https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes>:

| Cosa | Cambio en 3.1.0 | Por qué le afecta |
|---|---|---|
| **Glifo Dominate** | *"Reduced from 23.6% per stack to 1.8% per stack at glyph level 150"* | Aniquilado. En los datos, Dominate = `OverpowerDamage_Willpower_Side`. Cualquier guía que aún lo recomiende está muerta |
| **Red Blessing** (charm) | *"Maximum Overpower bonus reduced from 4 to 2"* | Reduce a la mitad el motor de Overpower de las dos builds |
| **Nodo legendario Wither** | *"Now also triggers from Cold damage in addition to Shadow damage"* | 🆕 **Habilita Naz Mages (frío).** Antes era solo sombra |
| **Glifo Darkness** | *"Now grants bonus damage and triggers from Cold in addition to Shadow damage"* | Ídem |
| **Mace of King Leoric** | *"Golem damage bonus increased from 70-80% to 100-120%"* | Opción de arma para gólem puro |

---

## 2. 🚩 Verificación del MODELO — aquí es donde casi me equivoco

Esta sección es la más importante del informe. Me la pidió explícitamente y ha dado fruto: **estuve a punto de publicar una refutación falsa.**

### 2.1 La contradicción aparente

Las dos guías de Icy Veins dicen, en la misma página, dos cosas que parecen incompatibles:

- Introducción de Naz Mages: *"supported by **Golem Gargantua command aura**"*
- Introducción de Reaper Summoner: *"whilst **Gargantuan Golem provides an Attack Speed aura**!"*
- Sección "Class Mechanic – Book of the Dead" de **ambas**: *"**Golem : Iron [Sacrifice]** – You deal 15%[x] increased Critical Strike Damage, but your Golem does 50%[x] less damage."*

Sacrificar el gólem y a la vez depender del aura del gólem parecía un resto sin actualizar de una versión muerta del juego. Además, "Book of the Dead" **no aparece ni una sola vez** en el fichero de datos 3.1.0 (`grep -i "book of the dead" d4data.json` → 0 resultados), lo que reforzaba la hipótesis.

### 2.2 Lo que dicen los datos del juego — la contradicción NO existe

Al leer los pasivos reales en `d4data.json`:

```
Necromancer_Golem_Iron_Passive_Sacrifice → "Sacrifice"
  "You deal [0.15*...]% increased Critical Strike Damage, but your Golem does 50%[x] less damage."
```

**El sacrificio del gólem le quita daño, NO lo elimina.** El gólem sigue en el campo, así que el aura de Gargantua sigue funcionando. Las guías son coherentes. Retiro la sospecha.

**Y hay algo más que ninguna de las dos guías explica.** Todos los demás sacrificios (magos, guerreros) llevan esta coletilla:

```
Necromancer_SkeletonMage_Cold_Passive_Sacrifice:
  "...but the amount of Cold Mages you can Summon is reduced by 50%.
   Your Golem gains 60%[x] increased damage."

Necromancer_SkeletonWarrior_Reaper_Passive_Sacrifice:
  "You deal [0.15*...]%[x] increased damage, but the amount of Reapers you can
   Summon is reduced by 50%. Your Golem gains 60%[x] increased damage."
```

*(Fuente: datamining de `assets-ng.maxroll.gg/d4-tools/game/data.min.json` v3.1.0.72698, claves `Necromancer_SkeletonMage_*_Passive_Sacrifice` y `Necromancer_SkeletonWarrior_*_Passive_Sacrifice`.)*

**Cada sacrificio que NO sea el del gólem le da al gólem +60%[x] de daño.** Ese es el motor oculto de estas builds y la razón de la frase críptica de Icy Veins *"This build continues to use all minions, even sacrificed ones, for inter-Minion synergies"*. No lo he visto explicado en ninguna guía.

### 2.3 🚩 El modelo que casi todas las webs tienen mal

Una búsqueda web devuelve, con aire de autoridad, que las variantes del gólem son **Bone / Blood / Iron**. Eso es **mezclar dos ejes distintos**. Los datos son inequívocos: son dos sistemas independientes y simultáneos.

| Eje | Dónde vive | Opciones del Gólem | ¿Cuántas se eligen? |
|---|---|---|---|
| **Variante de habilidad** (Bonus Skill Variant) | Árbol de habilidades, tercera rama | **Gravebloom · Fel Gluttony · Gargantua** | Una |
| **Tipo de esbirro + mejoras** (lo que era Book of the Dead) | Pasivos por tipo | **Bone / Blood / Iron**, cada uno con Upgrade A, Upgrade B y Sacrifice | Un tipo + sus mejoras |

Por eso **"Gargantua" + "Iron [Sacrifice]" a la vez es perfectamente legal**: son ejes ortogonales. Cualquier fuente que le presente Bone/Blood/Iron como "las variantes de Gargantua" está fusionando dos sistemas.

---

## 3. 🆕 Qué desbloqueó EXACTAMENTE al comprar las expansiones

### 3.1 El reparto gratis / pago

Confirmado que el nivel 70 y el árbol nuevo son **gratis para todos**, y que lo de pago es otra cosa:

> *"Must have the Lord of Hatred expansion to open all three Bonus Skill Variants; otherwise, **2 out of 3 Bonus Skill Variants are accessible**"*
> — título de hilo en los foros oficiales, <https://us.forums.blizzard.com/en/d4/t/must-have-the-lord-of-hatred-expansion-to-open-all-three-bonus-skill-variants-otherwise-2-out-of-3-bonus-skill-variants-are-accessible/245511>

| Gratis con el parche 3.0 | Requiere comprar Lord of Hatred |
|---|---|
| Nivel máximo 70 | La **tercera** variante de cada habilidad |
| Árbol de habilidades rediseñado | **Talismanes y Charms** |
| Dos de las tres Bonus Skill Variants por habilidad | **War Plans** |
| | **Cubo Horádrico** |
| | Región de Skovos, Paladín y Brujo |

Fuente del reparto: <https://thephrasemaker.com/2026/04/28/diablo-4-lord-of-hatred-free-vs-paid/> y la página oficial <https://diablo4.blizzard.com/en-us/lord-of-hatred> (*"unlock bonus skill variants across each class... equip set bonuses with the new Talisman"*).

**Esto cuadra con su situación y la valida:** era nivel 70 sin expansiones (gratis), y tenía cinco variantes (las gratuitas), pero no Gargantua.

### 3.2 🆕 Las 23 variantes que se le acaban de abrir — lista completa

**Nota de método:** los datos no traen una bandera "expansión". Lo he deducido así: cada habilidad tiene tres variantes y cada una lleva un `border` distinto (solo hay 3 IDs de borde en todo el juego, ~194 usos cada uno = son las posiciones 1/2/3). **Las cinco variantes que usted ya tenía son las cinco del mismo borde (`678742091`), y Gargantua es del borde `858665677`.** Cinco de cinco. Con la regla "2 de 3 gratis", la conclusión es que el borde `858665677` es el bloqueado.

> **Esto es una inferencia mía a partir del datamining, no una frase que haya leído.** Es sólida (5/5) pero no es una cita. Verifíquelo en pantalla: entre en el árbol y mire si estas 23 aparecen ahora resaltadas como nuevas.

Las 23 de Nigromante (todas 🆕 para usted), texto literal del fichero de datos:

| Habilidad | Variante 🆕 | Efecto |
|---|---|---|
| **Gólem** | **Gargantua** | *"Golem now raises a larger Golem that gains an aura of command, increasing the Cast Speed and Movement Speed of your other Minions by [0.2*Table(34,sLevel)*100]%[x]"* |
| **Mago Esquelético** | Singularity | Consume toda la Esencia al lanzar; el mago hace +3%[x] daño y dura 0,1 s por punto de Esencia consumido |
| **Guerrero Esquelético** | Litany of Death | Si ya están todos invocados, invoca un **Sacerdote Esqueleto** que da a los esbirros +[0.15*Table(37,sLevel)]% de prob. de crítico y los cura al 100% de su vida en 8 s |
| **Ejército de los Muertos** | Dead Cold | Hace daño de **Frío** y **Congela** en vez de Aturdir |
| **Doncella de Hierro** | Blood Maiden | Es también habilidad de Sangre; recoge 4 Orbes de Sangre y los detona |
| **Tentáculos de Cadáver** | Jaws Of Death | Más daño y **sin retardo** antes de atraer |
| **Decrepify** | **Unholy Frenzy** | *"Instead of afflicting enemies Decrepify is now applied to your Minions, granting them [0.2*Table(34,sLevel)*100]%[x] increased Cast Speed and Movement Speed"* |
| Sever | Cold Pursuit | Daño de Frío, Enfría 15%, y busca otro enemigo |
| Blight | Volatile Blood | Pasa a Sangre y daño Físico; el área estalla al instante |
| Reap | Chilled To The Bone | Daño de Frío + 30%[+] Cast Speed |
| Hemorrhage | Soul Rip | Pasa a Oscuridad/Sombra; invoca un Esqueleto Volátil |
| Bone Splinters | Shadow Seekers | Pasa a Oscuridad; las esquirlas buscan enemigos |
| Bone Spear | Shadow Splitter | Pasa a Oscuridad; se bifurca en 2 lanzas hasta 2 veces |
| Decompose | Rip and Tear | Pasa a Hueso/Físico; golpea a todo lo que haya en medio |
| Blood Mist | Devouring Mist | Pasa a Oscuridad; aplica Maldición Vampírica |
| Bone Spirit | Astral Projection | Orbita a su alrededor en vez de buscar |
| Blood Surge | Pins and Needles | Expulsa 10 esquirlas perforantes en vez de la nova |
| Bone Prison | Life Imprisonment | Prisión alrededor suyo; +Esencia y +Cast Speed, drena 5% vida/s |
| Corpse Explosion | Shrapnel | Dispara 8 esquirlas perforantes |
| Bone Storm | Hungry Cyclone | Se lanza en el objetivo y busca; −[20*Table(37,sLevel)] s de reutilización |
| Blood Lance | Festering Wound | Pasa a Oscuridad; lanza permanente con daño Corruptor por segundo |
| Blood Wave | Hematolagnia | Pasa a Core, sin cooldown, cuesta 50 Esencia |
| Soulrift | Frozen Wasteland | Daño de Escarcha; los congelados se hacen añicos |

**🚩 Fíjese en Unholy Frenzy.** Lleva la **fórmula idéntica** a Gargantua (`0.2*Table(34,sLevel)*100`, Cast Speed + Movement Speed a los esbirros). Ninguna de las guías la menciona. **No sé si apila con Gargantua ni si rompe Blood Moon Breeches** (que necesita que Decrepify maldiga *enemigos*, y Unholy Frenzy lo redirige a los esbirros). Va a "No encontrado" — no lo infiera, pruébelo.

### 3.3 🆕 Valor real del aura de Gargantua

Fórmula del fichero: `0.2 * Table(34, sLevel) * 100`. Tabla 34 leída del propio fichero (`powerTables[34]` = `[1, 1, 1.1, 1.2, 1.3, 1.45, 1.55, 1.65, 1.75, 1.85, 2, 2.1, ...]`):

| Rango de habilidad | Aura (Cast Speed + Movement Speed a los otros esbirros) |
|---|---|
| 1 | **20%[x]** |
| 2 | 22%[x] |
| 3 | 24%[x] |
| 5 | 29%[x] |
| 10 | 40%[x] |
| 15 | 51%[x] |
| 20 | 62%[x] |

**🚩 Aviso de vocabulario:** el fichero dice **Cast Speed** (velocidad de lanzamiento), no Attack Speed. Icy Veins lo llama *"Attack Speed aura"* y Maxroll dice *"Golem Aura gives you as much as you need"* dentro de su FAQ de **cómo llegar a 100% de velocidad de ataque** (<https://maxroll.gg/d4/build-guides/minion-necromancer-guide>). Puede que en esbirros Cast Speed haga de velocidad de ataque, o puede que las guías estén usando el término suelto. **No lo he visto confirmado por escrito** → "No encontrado".

---

## 4. Su build actual vs. las dos estrella — el diff exacto

### 4.1 Los topes de esbirros, según los datos

Fórmulas literales del fichero (`pets[].max`):

- **Guerreros:** `Floor((4 + (Skirmisher UpgradeA ? 2 : 0) + (Master of Puppets ? 3 : 0) + afijos) × 0.5 por cada Sacrificio activo)`
- **Magos:** `Floor((3 + bonus + (Coven ? 2 : 0)) × 0.5 por cada Sacrificio activo)`
- **Gólems:** `Gravebloom ? 3 : 1`

Es decir: base 4 guerreros / 3 magos / 1 gólem. **Gravebloom = 3 gólems; Gargantua = 1 gólem (más grande, con aura).**

### 4.2 Tabla de cambios

| Elemento | Lo que lleva HOY | Naz Mages | Reaper Summoner | ¿Cuesta? |
|---|---|---|---|---|
| **Gólem (variante)** | Gravebloom (3 gólems) | **Gargantua** 🆕 | **Gargantua** 🆕 | Gratis (respec) |
| **Mago (variante)** | Coven (+2 magos) | **Coven** ✅ igual | **Coven** ✅ igual | — |
| **Guerrero (variante)** | Master of Puppets (+3) | **Service and Sacrifice** | Master of Puppets ✅ igual | Gratis |
| **AotD (variante)** | Unyielding Commander | **Unyielding Commander** ✅ | (en barra) ✅ | — |
| **Doncella (variante)** | Schadenfreude | no se usa | no se usa | Gratis |
| **Tipo de mago** | Sombras (mejora B) | **Frío [Upgrade #2]** | **Sombra [Upgrade #2]** ✅ igual | Gratis |
| **Tipo de guerrero** | Segadores (mejora B) | **Reaper [Sacrifice]** | **Reapers [Upgrade #2]** ✅ igual | Gratis |
| **Tipo de gólem** | Sangre (mejora A) | **Iron [Sacrifice]** | **Iron [Sacrifice]** | Gratis |
| **Barra** | Mago, Guerrero, Gólem, Tentáculos, Doncella, AotD | Mago, Sever, Guerrero, Hemorrhage, Gólem, AotD | Guerrero, Sever, Mago, Gólem, Blight, AotD | Gratis |
| **Únicos requeridos** | — | Hand of Naz, Blood Moon Breeches, Signet of Pelghain, Undercrown | Blood Moon Breeches, Deathgrip, Undercrown, Pact of Bone | **Farmeo** |
| **Charms** 🆕 | ninguno (bloqueado) | Black Shroud 5-set | Black Shroud 5-set | **Farmeo largo** |
| **Mercenario** 🆕 | — | Varyana + Raheir | Varyana + Raheir | Barato |

**Lectura:** Reaper Summoner reutiliza **casi todo** lo que ya tiene (Coven, Master of Puppets, magos de Sombra, guerreros Segadores). Naz Mages exige girar a **frío**, cambiar la variante de guerrero y farmear dos únicos que no tiene.

---

## 5. Las dos builds al detalle

### 5.1 Naz Mages — S-Tier según Icy Veins

Fuente única de toda esta sección: <https://www.icy-veins.com/d4/guides/mendeln-summoner-necromancer-build/> (actualizada 3 julio 2026). Autores: GhazzyTV y Garm Z.

**Barra:** Skeleton Mage · Sever · Skeleton Warrior · Hemorrhage · Golem · Army of the Dead
*"Decrepify and Iron Maiden are activated via Blood Moon Breeches and are not needed on the skill bar."*

**Árbol:** *"Use the Skill Tree above to complete an 83-point build. 69 skill points are gained by leveling, and 14 skill points are locked behind the Season Rank System or Renown"* — 69 puntos por niveles cuadra con el tope 70.

**Tipos de esbirro:**
- Guerreros: Reaper [Sacrifice] — *"You deal x15% increased damage, but the amount of Reapers you can Summon is reduced by 50%"*
- Magos: Cold [Upgrade #2] — *"Cold Mages occasionally cast a blizzard... Enemies damaged by Cold Mages are made Vulnerable for 4 seconds. Skeleton Mage is also a Darkness Skill"*
- Gólem: Iron [Sacrifice] — *"You deal 15%[x] increased Critical Strike Damage, but your Golem does 50%[x] less damage"*

**Equipo por hueco:**

| Hueco | Objeto | Texto (verbatim de la guía) |
|---|---|---|
| Casco | The Undercrown | *"maximum number of Skeleton Warriors and Skeleton Mages is increased by 4 and your Summon damage is increased by 25.0%[x] [15.0 – 25.0]%"* |
| Pecho | Aspect of Heavenly Strength | *"While wielding a Two Handed Weapon, gain [30 – 40%] Damage Reduction"* |
| Guantes | The Hand of Naz | *"Maximum number of Skeletons is increased by 1. Arch-Mages teleport to safety..."* |
| Pantalón | Blood Moon Breeches | *"Your Summons have #% chance to randomly inflict Decrepify or Iron Maiden"* |
| Botas | Exploiter's Aspect | *"You have 50% increased Crowd Control duration"* |
| Arma 2M | Bloodless Scream | *"deal x [200 – 250%] increased damage to Frozen enemies and bosses"* |
| Amuleto | Banished Lord's Talisman | *"After you spend 275 of your Primary Resource, gain 4 stacks of Overpower... 9%[x] [7 – 9]% increased damage per stack"* ⚠️ ver §1.2 (Red Blessing bajó de 4 a 2) |
| Anillo 1 | Pact of Bone | Attack Speed + Critical Strike Chance a los esbirros |
| Anillo 2 | Signet of Pelghain | 🚩 la guía dice 15–20%; **el valor real es 10–15%** (§1.1) |

**Gemas y runas:** Arma: Royal Sapphire. Joyería: Royal Diamond. Runewords: **Igni + Wat** (*"Invokes the Necromancer's Decrepify"*) y **Nagu + Que** (barrera).

**Paragón — orden de tableros y glifos:**
1. Starter → glifo **Mage**
2. Frailty → glifo **Warrior**
3. Cult Leader → glifo **Control**
4. Flesh Eater → glifo **Amplify**
5. Wither → glifo **Essence**

*"It is imperative to level up all Glyphs to level 25 first to increase their activation radius, and then to level 51 to unlock the secondary damage multiplier."*

**Charms:** *"Legendary Seal with +1 Charm Slot affix, to unlock 6 Charm slots asap. Full Black Shroud Charm Set of any quality. 5-set takes priority over any other Charms."* Chase: **Seal of the Diamond Mind** (permite un charm extra).

**Mercenario:** Varyana (Cleave, Hysteria, Bloodthirst, Intimidated). Refuerzo: Raheir con Provoke.

**Rotación:** Sever para generar cadáver → Gólem activo preventivo (Imparable) → Hemorrhage "Blood Runs Cold" para congelar → comandar Guerreros para enfocar magos sobre un enemigo congelado → repetir.
**Jefes:** *"After 2 staggers it's better to avoid generating more stagger... for 15 seconds until boss drops Crowd Control resistance."*

### 5.2 Reaper Summoner — A-Tier según Icy Veins

Fuente única: <https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/> (actualizada 3 julio 2026).

*"Skeletal Reapers are the main stacking force, Shadow Mages are in a support and secondary DPS role, whilst **Gargantuan Golem provides an Attack Speed aura**!"*

**Barra:** Skeleton Warrior · Sever · Skeleton Mage · Golem · Blight · Army of the Dead

**Tipos de esbirro:**
- Guerreros: **Reapers [Upgrade #2]** — la guía lo transcribe como *"-50%[x] increased damage and 15% chance to Stun for 1 second"*. El fichero de datos dice: *"Reapers deal 50%[x] increased damage and have a 15% chance to Stun enemies for 1 second"* → **es +50%, el guion de la web es un artefacto de maquetación**
- Magos: Shadow [Upgrade #2] — *"Shadow Mages' bolts grant you and the Shadow Mage a Barrier for #% of your Maximum Life for 4 seconds, up to 42%"*
- Gólem: Iron [Sacrifice]

**Diferencias de equipo respecto a Naz Mages:**

| Hueco | Reaper Summoner |
|---|---|
| Guantes | **Deathgrip** — *"maximum number of Skeleton Warriors is increased by 1. Skeleton Warriors cleave... Commanding them onto a target increases damage that target takes"* |
| Botas | **Aspect of Hewed Flesh** — *"Lucky Hit: Up to a 25% chance to form a Corpse... Corpse Skills deal 20.0%[x] [15.0 – 20.0]% increased damage"* |
| Anillo 1 | **Hellbent Commander Aspect** — *"You deal 60%[x] [40 – 60]% increased Summon damage"* |
| Anillo 2 | Pact of Bone |
| Gema arma | Royal Amethyst (sombra) en vez de Sapphire |

**Paragón:** Starter→Mage, Frailty→Warrior, Cult Leader→Essence, Flesh Eater→Amplify, Wither→**Deadraiser**.
(Diferencia con Naz Mages: **Deadraiser** en vez de Control. En los datos, `Deadraiser` = `Nodes_BonusToMinion` — coherente con una build de más esbirros.)

**Charms, mercenario y rotación:** idénticos a Naz Mages (Black Shroud, Varyana + Raheir).

---

## 6. 🚩 Un set de charms que NINGUNA de las guías evalúa

Los datos traen **cinco** sets de talismán de Nigromante. Las tres fuentes que he abierto (las dos de Icy Veins y la de Maxroll) recomiendan **Black Shroud** y no comentan las otras. Pero existe un set explícitamente de esbirros:

| Set (nombre literal en datos) | 2 piezas | 3 piezas | 5 piezas |
|---|---|---|---|
| **Peace of the Black Shroud** *(el que recomiendan las 3 guías)* | Habilidades de Oscuridad hacen 75% de su daño como daño Corruptor o de Escarcha en 30 s | 30% Reducción de Daño 5 s al infligir daño por tiempo | **175%[x] más daño de Sombra y Frío**; los Corrompidos/Escarchados por encima de su vida quedan Vulnerables, Debilitados, ralentizados 85%, +50%[x] daño recibido |
| **Rathma's Waking Touch** *(nadie lo comenta)* | **Sus esbirros hacen 60%[x] más daño** y reducen 1 s el cooldown de AotD cada vez que dañan | **35% del daño que usted recibe se redirige a sus esbirros** | **AotD hace 450%[x] más daño.** Mientras AotD esté activo, los esbirros son más grandes, tienen **+100%[x] Vida** y **+25%[+] Velocidad de Ataque** |

*(Fuente: datamining, `itemSets.Talisman_Necro_04` y `Talisman_Necro_05` con sus afijos resueltos.)*

**Por qué esto le interesa mucho:** usted lleva **Unyielding Commander** (*"While Army of the Dead is active, your Minions take 90% reduced damage and you deal 50%[x] increased Summon Damage"*). Con esa variante, el Ejército de los Muertos tiende a estar **activo permanentemente** — la propia guía de Naz Mages lo dice: *"the benefits from Unyielding Commander will be constantly active at all times"*. El bonus de 5 piezas de Rathma's está condicionado a *"While Army of the Dead is active"*.

**No estoy diciendo que Rathma's sea mejor.** Black Shroud da un 175%[x] plano que los esbirros de sombra/frío sí aprovechan, y las tres fuentes lo eligen por algo. Lo que digo es que **hay un set con etiqueta de esbirros que ninguna guía compara**, y usted está en posición de probarlo. Los números de arriba son literales; la comparación no la he visto hecha por nadie → va a "No encontrado".

---

## 7. Contradicciones entre las dos fuentes preferentes

No las voy a promediar. Se las enseño:

| Punto | Icy Veins (3 jul 2026) | Maxroll (22 jul 2026) |
|---|---|---|
| **Tier de esbirros** | Naz Mages **S**, Reaper Summoner **A** | Minion Necro **B** (endgame y push) |
| **Mercenario** | **Varyana** + Raheir | **Subo** + Aldkin |
| **Glifos (magos)** | Mage, Warrior, Control, Amplify, Essence | Mage, Essence, Deadraiser, Eliminator, Abyssal |
| **Estadísticas objetivo** | lista de prioridad, sin cifras duras | **100% Attack Speed, 100% Crit Chance, 30k vida**, 40+ Resolve (variante Warrior) |
| **Book of the Dead** | Sección explícita con tipos y sacrificios | **No la menciona en absoluto** |

Enlaces: <https://www.icy-veins.com/d4/guides/mendeln-summoner-necromancer-build/> · <https://maxroll.gg/d4/build-guides/minion-necromancer-guide>

**Cómo lo leo:** las tier lists de Maxroll están fechadas **29 junio 2026** (<https://maxroll.gg/d4/tierlists/necromancer-endgame-tier-list>), es decir **un día ANTES del parche 3.1.0** y tres semanas antes de que Maxroll reescribiera su propia guía de esbirros. Su changelog interno lo confirma: *"6/30 updated for s14 · 7/1 major overhaul with bloodless scream · 7/4 ... · 7/6 updated paragon"*. **La tier list B es anterior a su propia revisión.** No es que Maxroll piense que la build es B hoy; es que no ha vuelto a tocar la tier list.

Los objetivos duros de Maxroll (100/100/30k) son la parte más accionable de las dos guías y **no aparecen en Icy Veins**. Úselos como criterio de "¿voy bien?".

---

## 8. Tier list de Nigromante — Season 14 con expansiones

**Maxroll — Endgame** (última actualización **29 junio 2026**, *pre-3.1.0*) — <https://maxroll.gg/d4/tierlists/necromancer-endgame-tier-list>

| Tier | Builds |
|---|---|
| **A** | Blood Wave Necro · Bone Spirit Necro |
| **B** | **Minion Necro** · Golem Necro · Sever Necro · Blood Surge Necro |
| **C** | Blight Necro · AotD Necro · Bone Spear Necro · Blood Lance Necro |

**Maxroll — Push (Pit/Torre)** (misma fecha) — <https://maxroll.gg/d4/tierlists/necromancer-push-tier-list>

| Tier | Builds |
|---|---|
| **A** | Blood Wave Necro |
| **B** | Bone Spirit · **Minion Necro** · Golem Necro · Sever · Army of the Dead · Blood Surge · Blood Lance |
| **C** | Blight Necro · Bone Spear Necro |

**Icy Veins** (3 julio 2026, *post-3.1.0*) — etiqueta en la propia página de cada build:

| Tier | Build |
|---|---|
| **S** | **Naz Mages** |
| **A** | **Reaper Summoner** |

**Ninguna fuente pone Nigromante de esbirros en S en Maxroll, ni por debajo de A en Icy Veins.** No hay tier list de Nigromante posterior al 3.1.0 en Maxroll. La discrepancia es de fecha, no de opinión. **No la resuelva por autoridad: la S de Icy Veins es más reciente y post-parche; la B de Maxroll es pre-parche.**

---

## 9. ¿Cambiar o reforzar? — la respuesta

**Contexto temporal:** la temporada acaba, según estimación, el **15 de septiembre de 2026** (<https://blizzardwatch.com/2026/07/17/diablo-4-season-15-start-september-15/>). **Blizzard NO lo ha anunciado oficialmente**; hay estimaciones alternativas del 21 y del 28. Desde hoy: **~27 días**.

### La respuesta es: cambie la mitad barata HOY, y no persiga la cara

El cambio se divide en dos mitades con costes radicalmente distintos:

| Mitad | Qué es | Coste | ¿Da tiempo? |
|---|---|---|---|
| **Barata** | Variantes del árbol, tipos de esbirro, sacrificios, barra, runewords, mercenario, orden de glifos | **Gratis, reversible, 20 minutos** | Sí, hoy |
| **Cara** | 4-6 únicos concretos + Black Shroud 5 piezas + masterworking + míticos | Semanas de farmeo | **No en 27 días desde cero** |

La mitad barata contiene el aura de Gargantua (**20%[x] al rango 1, 40%[x] al rango 10**), el **+60%[x] al gólem por cada sacrificio** y los ajustes de glifos. Eso es una subida sustancial que no cuesta nada y que además le **deja el personaje configurado para la S15**.

La mitad cara no la persiga: los charms son el cuello de botella (5 piezas de un set concreto) y son lo primero que se reinicia en temporada nueva.

### Y hay un matiz que cambia la pregunta

Usted lleva **Coven + Master of Puppets + Gravebloom**: los tres son variantes de "más esbirros". Es un reparto de aprendiz, no de min-max. La guía de leveling de Mobalytics recomienda **cambiar Gravebloom por Gargantua ya en el nivel 36** (<https://mobalytics.gg/diablo-4/builds/minion-necromancer-leveling-build-guide>, vía resultado de búsqueda — **la página devuelve 403 y no he podido abrirla directamente**, ver "No encontrado"). Es decir: Gravebloom se considera opción de subida, no de endgame, incluso *sin* expansión.

**De las dos builds, vaya a Reaper Summoner, no a Naz Mages.** Razones:
1. Reutiliza **Coven, Master of Puppets, magos de Sombra y guerreros Segadores** — cuatro elecciones que ya tiene puestas.
2. Naz Mages exige girar a **frío** (magos Cold, Bloodless Scream, Royal Sapphire) y dos únicos que no tiene (Hand of Naz, Signet of Pelghain).
3. **Signet of Pelghain, pilar de Naz Mages, se llevó un recorte del 33%** en 3.1.0 (15-20% → 10-15%) que la guía aún no refleja en su tabla.

Naz Mages es el objetivo de **S15**, cuando empiece de cero y pueda farmear el frío desde el principio.

---

## 10. Plan por orden — qué hacer y en qué orden

### HOY, gratis, 20 minutos (antes de tocar nada más)
1. **Gravebloom → Gargantua.** Es el cambio de mayor retorno por euro cero. Suba el rango del Gólem: el aura escala fuerte (20% → 40% del rango 1 al 10).
2. **Tipo de gólem → Iron, y active su Sacrifice.** El gólem se queda en el campo (pierde 50% de daño propio, irrelevante: no es su fuente de daño) y usted gana 15%[x] de daño crítico.
3. **Active el Sacrifice de guerreros y/o magos.** Cada uno da **+60%[x] de daño al gólem** además de su propio bonus. Es el motor que las guías no explican.
4. **Barra:** meta **Sever** (genera cadáveres, movilidad) y **Blight**. Saque Tentáculos y Doncella de Hierro.
5. **Runewords:** **Nagu + Que** (Nagu es literalmente *"Maintain at least 1 active Summon for 5 seconds"* — hecho a medida para usted) e **Igni + Wat** (invoca Decrepify).
6. **Glifos: si tiene Dominate puesto, quítelo.** Pasó de 23,6% a **1,8%** por acumulación. Ponga **Mage** y **Warrior** primero.
7. **Mercenario:** Varyana con Cleave/Hysteria/Bloodthirst/Intimidated, refuerzo Raheir con Provoke. (Maxroll dice Subo+Aldkin; pruebe ambos, es gratis cambiarlos.)

### Esta semana
8. **Charms** 🆕 — es lo que más tarda. Objetivo: **Sello Legendario con "+1 Charm Slot"** y luego piezas de **Black Shroud** de cualquier calidad. Empiece hoy aunque no lo termine.
9. **Suba todos los glifos a 25** (radio), luego a **51** (segundo multiplicador). No los suba de uno en uno hasta 51.
10. **Objetivos duros de Maxroll:** 100% Velocidad de Ataque · 100% Prob. de Crítico · 30.000 de vida. Mida contra esto, no contra sensaciones.
11. **Únicos por prioridad:** The Undercrown (Duriel) → Deathgrip → Pact of Bone (Harbinger of Hatred) → Blood Moon Breeches (Astaroth).

### Antes del fin de temporada
12. **Míticos:** el coste bajó de 5 a **4 Fragmentos de Pandemónium** en 3.1.1. Solo puede llevar **1 mítico crafteado** a la vez (los que caen no cuentan). Prioridad de Maxroll para la variante Warrior: Pact of Bone → Undercrown → Deathgrip → Blood Moon Breeches.
13. **Pruebe Rathma's Waking Touch** contra Black Shroud si le caen piezas (§6). Nadie ha publicado la comparación.

---

## 11. El dúo — dos casos, y uno tiene un problema serio

⚠️ Como no se sabe si su pareja compró las expansiones, cubro los dos casos.

### Caso A — la pareja SÍ tiene Lord of Hatred
Sin fricción. Ambos acceden a Gargantua, charms y War Plans. Dos nigromantes de esbirros funcionan: el aura de Gargantua es *"of your other Minions"* (los suyos), así que **no se pisan ni se solapan**. Cada uno lleva su propio Gargantua.

### Caso B — la pareja NO tiene Lord of Hatred 🚩
**Aquí está el problema, y es más gordo que "le falta Gargantua":**

| Le falta | Consecuencia |
|---|---|
| La tercera variante de cada habilidad | Sin Gargantua. Se queda con Gravebloom o Fel Gluttony |
| **Talismanes y Charms** | **No puede montar Black Shroud ni ningún set.** Las dos builds estrella son charm-dependientes → **no puede seguir ninguna de las dos guías tal cual** |
| **Cubo Horádrico** | No puede craftear míticos ni imprimir el Tidal Aspect que Icy Veins marca como *"REQUIRES imprinted Tidal Aspect"* para activar Banished Lord's Talisman |
| **War Plans** | Le falta una vía de progresión de endgame |

**Qué hacer en el caso B:** que la pareja monte **Gravebloom (3 gólems) + Coven + Master of Puppets**, que es exactamente lo que usted lleva ahora y funciona sin expansión. **No le pase la guía de Naz Mages ni la de Reaper Summoner**: le pedirán charms que no puede equipar y se frustrará sin entender por qué.

Nivel 70 y árbol nuevo sí los tiene (son gratis), así que **no hay bloqueo de nivel ni de contenido base para jugar juntos**.

**No he encontrado escrito** si el juego cruzado PC ↔ PS5 tiene alguna restricción adicional cuando los miembros del grupo tienen distinta propiedad de expansión → "No encontrado".

---

## 12. Mirando a la S15

- **PTR 3.2.0** ya se corrió: *"from August 4, 10:00 a.m. PDT to August 11, 10 a.m. PDT"* (<https://news.blizzard.com/en-us/article/24292852/the-3-2-0-ptr-what-you-need-to-know>).
- Blizzard **no ha anunciado la fecha de la S15**. La estimación más citada es el 15 de septiembre.
- **No transcribo los cambios concretos del 3.2** porque el resumen automático que obtuve de esa página me devolvió un nombre de objeto inventado ("Command Abodian") y no pude verificar el resto contra el texto crudo. Va entero a "No encontrado" — ver la nota metodológica.
- Lo que sí es sólido para la S15: deje el personaje ya configurado con Gargantua y con las variantes de la expansión aprendidas. **Lo que no se reinicia es saber qué elegir.**

---

## 13. Nota metodológica — por qué algunos huecos están declarados

Durante esta investigación, el lector automático de páginas web me devolvió **información inventada** en al menos dos ocasiones verificadas:

1. Al pedirle las notas del parche 3.1.1, devolvió tres cambios de objeto que **no existen** en el texto real: *"The Gloom Ward: Now procs every 6th instance of damage, down from every 8th"*, *"Aspect of Serration: Critical Strike Chance increased from 5% to 10%"* y una línea sobre gólems y habilidades Macabras. Descargué el HTML crudo y ninguna aparece en 3.1.1.
2. Al pedirle el PTR 3.2.0, devolvió un objeto llamado *"Command Abodian"*, que no existe.

Por eso **todo número de este informe viene o del HTML crudo descargado con `curl` y limpiado, o del fichero de datos del juego**. Donde solo tenía un resumen automático sin verificar, el dato **no aparece**: aparece en "No encontrado".

---

## Fuentes

URLs efectivamente abiertas y leídas (HTML crudo o JSON, salvo donde se indica):

**Oficiales de Blizzard**
- <https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes> — notas 3.1.0 a 3.1.3, descargadas en crudo (131 KB) y leídas línea a línea
- <https://news.blizzard.com/en-us/article/24292852/the-3-2-0-ptr-what-you-need-to-know> — PTR 3.2.0 (solo fechas usadas; el resto descartado por no verificable)
- <https://diablo4.blizzard.com/en-us/lord-of-hatred> — página oficial de la expansión
- <https://us.forums.blizzard.com/en/d4/t/must-have-the-lord-of-hatred-expansion-to-open-all-three-bonus-skill-variants-otherwise-2-out-of-3-bonus-skill-variants-are-accessible/245511> — hilo del foro oficial sobre 2 de 3 variantes
- <https://news.blizzard.com/en-us/article/24271857/diablo-iv-patch-notes-3-0> — consultada; no contenía el rework de esbirros

**Datamining (declarado como tal)**
- <https://assets-ng.maxroll.gg/d4-tools/game/data.min.json> — 11,6 MB, versión **3.1.0.72698**. De aquí salen: textos literales de las 23 variantes, fórmulas de tope de esbirros, tabla 34 para el aura de Gargantua, textos de Sacrifice/Upgrade A/B por tipo, sets de talismán, runas Igni/Wat/Nagu/Que/Ceh, y el mapeo de glifos a afijos

**Icy Veins**
- <https://www.icy-veins.com/d4/guides/mendeln-summoner-necromancer-build/> — Naz Mages, HTML crudo, `dateModified` 2026-07-03
- <https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/> — Reaper Summoner, HTML crudo, `dateModified` 2026-07-03
- <https://www.icy-veins.com/d4/guides/necromancer-builds> — índice de builds (no contenía tier list)

**Maxroll**
- <https://maxroll.gg/d4/build-guides/minion-necromancer-guide> — guía de esbirros, HTML crudo, "Last Updated: July 22, 2026"
- <https://maxroll.gg/d4/tierlists/necromancer-endgame-tier-list> — HTML crudo, 29 junio 2026
- <https://maxroll.gg/d4/tierlists/necromancer-push-tier-list> — HTML crudo, 29 junio 2026

**Secundarias (usadas solo para el reparto gratis/pago y fechas)**
- <https://thephrasemaker.com/2026/04/28/diablo-4-lord-of-hatred-free-vs-paid/>
- <https://blizzardwatch.com/2026/07/17/diablo-4-season-15-start-september-15/>

**Intentadas y fallidas (HTTP 403 / 404)**
- mobalytics.gg (tier list y guía de leveling) — 403 tanto por `curl` como por el lector web
- wowhead.com/diablo-4 — 403
- d4builds.gg — 404 / aplicación JS sin HTML servible
- diablobytes.com — 403

---

## No encontrado

Huecos declarados. **No los he rellenado por inferencia.**

1. **Si Cast Speed = Attack Speed en esbirros.** El fichero de datos dice que Gargantua da *"Cast Speed and Movement Speed"*. Icy Veins lo llama "Attack Speed aura" y Maxroll lo usa en su FAQ de cómo llegar al 100% de velocidad de ataque. **No he visto escrito en ninguna parte que sean lo mismo para esbirros.** Compruébelo en la hoja de personaje.
2. **Si Unholy Frenzy apila con Gargantua.** Comparten fórmula idéntica (`0.2*Table(34,sLevel)*100`, Cast+Movement Speed a esbirros). Ninguna guía la menciona. Tampoco sé si rompe Blood Moon Breeches, que necesita que Decrepify maldiga enemigos.
3. **La comparación Rathma's Waking Touch vs Black Shroud.** Tengo los textos literales de ambos sets (§6); **no he encontrado a nadie que los compare** para una build de esbirros.
4. **Confirmación textual de que el borde `858665677` = variante de expansión.** Es una inferencia mía (5 de 5 de sus variantes actuales comparten otro borde, y Gargantua es de ese). Los datos no traen bandera de expansión. Verificable en pantalla en 10 segundos.
5. **Los cambios concretos del parche 3.2 / S15.** Descartados por completo: el resumen automático devolvió un objeto inexistente y no pude verificar el resto contra texto crudo.
6. **Fecha oficial de fin de la S14.** Blizzard no la ha anunciado. 15 de septiembre es estimación de terceros; hay estimaciones alternativas del 21 y del 28.
7. **La guía de leveling de Mobalytics (cambio a Gargantua en nivel 36).** El dato viene de un fragmento de resultado de búsqueda; **la página devuelve 403 y no he podido leerla directamente**. Trátelo como indicio, no como cita.
8. **Qué únicos concretos son exclusivos de cada expansión.** Los `flags` del fichero de datos no separan expansión de juego base (Blood Moon Breeches, que es de juego base, y The Undercrown comparten valores con objetos de distinto origen). No lo he podido determinar.
9. **Números por nivel de los glifos** Mage, Warrior, Control, Amplify, Essence, Deadraiser. Confirmo qué afijo escala cada uno (`SkeletonMageDamage`, `SkeletonWarriorDamage`, `Nodes_BonusToMinion`, `Nodes_BonusToMagic`) pero las descripciones vienen vacías en el fichero.
10. **Restricciones de juego cruzado PC ↔ PS5** cuando los miembros del grupo tienen distinta propiedad de expansión.
11. **Tier list de Nigromante posterior al 3.1.0 en Maxroll.** No existe; la suya es del 29 de junio, un día antes del parche.
12. **Reddit (r/diablo4, r/Diablo4Necromancer) y d4builds.gg / wowhead.** No aportaron nada verificable: los buscadores devolvieron resultados de temporadas antiguas y las páginas directas bloquearon el acceso (403).
