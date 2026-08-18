# Sistema de dificultades de Diablo IV — Season 14 "Death Awakening" (parche 3.1.3)

> **Fecha de investigación:** 18 de agosto de 2026
> **Parche vigente:** 3.1.3, build 73224 (12 de agosto de 2026)
> **Temporada:** Season 14 — *Season of Death Awakening* (desde el 30 de junio de 2026)
> **Jugador objetivo:** Nigromante (Necromancer), principiante absoluto, **SOLO JUEGO BASE**, en dúo cross-play (PC + consola)
>
> 🔍 **DOCUMENTO VERIFICADO Y CORREGIDO** el 18/08/2026 por un segundo agente adversarial. La tesis central se confirma; **se corrigieron 11 errores**, cuatro de ellos graves. Las correcciones van marcadas en línea. **Leed la "Nota del verificador" al final antes de fiaros de cualquier número.**

---

## 0. TL;DR — lo que tenéis que saber antes de nada

1. ✅ **Todo el sistema de dificultades, incluidos los 12 niveles de Torment, funciona con el juego base.** No necesitáis ninguna expansión para llegar a Torment XII. Esto es la respuesta a la pregunta más importante del brief. (Hay una fuente que lo contradice; ver §9.)
2. ✅ **El nivel máximo de personaje es 70**, no 60. Subió de 60 a 70 en el parche 3.0 (Season 13) y ese aumento fue **gratuito para todos**.
3. ✅ La escalera completa es: **Normal → Hard → Expert → Penitent → Torment I…XII** (16 escalones).
4. ✅ **Ya NO existen penalizaciones de resistencia ni de armadura por nivel de Torment.** Se eliminaron en la revisión defensiva de la Season 11. Cualquier guía que os hable de "-25% resistencias en T1, -100% en T4" está obsoleta.
5. 🔒 Lo que sí os falta: Mercenarios (Mercenaries) y Palabras rúnicas (Runewords) de *Vessel of Hatred*; y Cubo Horadrim (Horadric Cube), Planes de Guerra (War Plans), Talismanes (Talismans) de *Lord of Hatred*. Esto **no os bloquea las dificultades**, y **tampoco os bloquea los Únicos Míticos** — caen como botín desde Torment 1 y existe una segunda ruta de crafteo sin Cubo (ver §8.3, corregido por el verificador). Os hace el ascenso más lento, no imposible.
6. La regla de oro práctica: **XP/hora = densidad × multiplicador de dificultad × velocidad de limpieza.** La dificultad más alta que podéis sobrevivir **casi nunca** es la dificultad más rentable.

---

## 1. La escalera completa de dificultades en S14

Diablo IV usa desde el parche 2.0 un sistema híbrido: cuatro dificultades "de campaña" seleccionables libremente, y luego una escalera de Torment desbloqueada por progresión real. En Season 13 (parche 3.0) los cuatro Torment originales se expandieron a **doce**.

### 1.1 Dificultades base (leveling)

| # | Dificultad (ES) | Nombre EN | Requisito de desbloqueo | Bonus XP | Bonus oro | Base? |
|---|---|---|---|---|---|---|
| 1 | Normal | Normal | Por defecto | — (base) | — | ✅ |
| 2 | Difícil | Hard | Por defecto | **+75%** | +25% / +75% ⚠️ | ✅ |
| 3 | Experto | Expert | Completar el **prólogo** | **+125%** | +50% / +125% ⚠️ | ✅ |
| 4 | Penitente | Penitent | Completar la **campaña base** (fuentes antiguas dicen "nivel 50") ⚠️ | **+175%** | +75% / +175% ⚠️ | ✅ |

⚠️ Los bonus de oro están en disputa entre fuentes. Ver §9, contradicción C.

Las cuatro se pueden seleccionar libremente una vez disponibles: podéis bajar y subir a voluntad desde el menú o desde la estatua del mundo.

### 1.2 Dificultades Torment (endgame)

Requieren **nivel 70** y se desbloquean **exclusivamente completando pisos de El Foso (The Pit)**. No se desbloquean terminando la campaña.

| Torment | Foso (Pit) requerido | Bonus XP | Bonus oro | Botín que se desbloquea |
|---|---|---|---|---|
| **T1** | Pit 10 | +300% | +100% | Calidad **Ancestral** (Ancestral) disponible; más Legendarios, Únicos y **Únicos Míticos** por tier ✅ |
| **T2** | Pit 15 | +400% | +120% ⚠️ | Manuales de Temple legendarios (Legendary Temper Manuals) y **Pergamino de Restauración** (Scroll of Restoration) ✅ |
| **T3** | Pit 20 | +500% | +140% ⚠️ | **Amuletos de conjunto** (Set Charms) más frecuentes ✅ |
| **T4** | Pit 25 | +600% | +160% ⚠️ | — |
| **T5** | Pit 30 | +700% | +180% ⚠️ | **Runas legendarias** (Legendary Runes) más frecuentes ✅ |
| **T6** | Pit 40 | +800% | +200% ⚠️ | — |
| **T7** | Pit 50 | +900% | +225% ⚠️ | ⚠️ *"Polvo Primordial Refinado" NO aparece en la tabla de Maxroll. Sin confirmar — probablemente inventado o mal atribuido.* |
| **T8** | Pit 60 | +1000% | +250% ⚠️ | **Amuletos únicos** (Unique Charms) más frecuentes ✅ — *el "XP aumentada en 3.1.x" era erróneo, ver §7* |
| **T9** | Pit 70 | +1100% | +275% ⚠️ | — |
| **T10** | Pit 80 | +1200% | +300% | **Sellos Horadrim Míticos** (Mythic Horadric Seals) más frecuentes ✅ — *lo de "fragmentos de gema" no está confirmado* |
| **T11** | Pit 90 | +1300% | +300% | — |
| **T12** | Pit 100 | +1400% | +300% | Techo actual de dificultad (Maxroll no lista desbloqueos nuevos en T12) |

**Patrón:** +100% de XP por escalón. El oro se estanca en +300% a partir de T10.

✅ **Verificado por el verificador (Maxroll *Difficulty Scaling*, act. 26 jun 2026, S14):** la columna de pisos del Foso es **exacta**, cita literal — *"Torment 1 (Pit 10), Torment 2 (Pit 15), Torment 3 (Pit 20), Torment 4 (Pit 25), Torment 5 (Pit 30), Torment 6 (Pit 40), Torment 7 (Pit 50), Torment 8 (Pit 60), Torment 9 (Pit 70), Torment 10 (Pit 80), Torment 11 (Pit 90), Torment 12 (Pit 100)"*. También confirmados: el rango de XP +300%→+1400%, el rango de oro +100%→+300%, el requisito de **nivel 70**, y los desbloqueos de botín marcados con ✅.
⚠️ **No confirmados:** los valores de oro **intermedios** (T2–T9). Maxroll solo me devolvió los extremos (+100% en T1, +300% en T12); la progresión +120/+140/+160/+180/+200/+225/+250/+275 es una interpolación plausible pero **no la he podido leer literalmente en ninguna fuente**.

**Nota sobre El Foso:** tiene **150 pisos** en total, o sea que Pit 100 (requisito de T12) no es el techo del Foso — todavía quedan 50 pisos de *pushing* por encima para leaderboards. ✅ El Foso es contenido de juego base.

**Cómo se desbloquea El Foso en temporada:** completando la mazmorra capstone **"Descenso Infernal" (Hellish Descent)** del **Rango II del Recorrido de Temporada (Season Rank II)**. En el reino Eterno, simplemente a nivel 70. Se accede desde el **Obelisco del Artífice (Artificer's Obelisk)**. ✅ Base.

---

## 2. Penalizaciones de resistencia, topes de armadura y resistencias

Esta es la sección donde más basura desactualizada vais a encontrar por internet. Atención.

### 2.1 Las penalizaciones por Torment YA NO EXISTEN ✅

En la **revisión defensiva de la Season 11** (la mayor de la historia del juego según Icy Veins), Blizzard **eliminó las penalizaciones de Armadura y Resistencias por nivel de Torment**. Cita textual de la cobertura: las penalizaciones se retiran "dando a los jugadores más libertad para empujar dificultades altas sin desventajas arbitrarias".

Por tanto, en S14 / parche 3.1.3:

- ❌ **NO** hay -25% resistencias en Torment I
- ❌ **NO** hay -50% en Torment II
- ❌ **NO** hay -75% en Torment III
- ❌ **NO** hay -100% en Torment IV

Si veis esos números en una guía, es de la era *Vessel of Hatred* (parche 2.x) y está muerta. **Subir de Torment ya no os quita defensas**; solo sube la potencia de los monstruos.

### 2.2 Cómo funcionan armadura y resistencias ahora

Desde la Season 11, **Armadura (Armor) y Resistencias (Resistances) son sistemas de *rating* con rendimientos decrecientes**, no porcentajes planos con tope duro.

La fórmula (fuente: guía de defensas de Maxroll, actualizada el 16 de agosto de 2026 — es decir, **anteayer**):

```
Reducción de daño % = Valor / (Valor × 10/9 + Constante)
```

| Estadística | Constante a nivel 70 | Asíntota |
|---|---|---|
| **Armadura** (Armor) | **5678** | → 90% de reducción de daño |
| **Resistencias** (Resistances) | **1136** | → 90% de reducción de daño |

**Implicaciones prácticas para vuestro nigromante:**

- **No hay un "tope" duro al que llegar y parar.** El término `10/9` crea un techo asintótico del **90% de reducción de daño**: os acercáis pero nunca lo alcanzáis. Cada punto extra vale menos que el anterior.
- La constante de Resistencias (1136) es **exactamente 1/5** de la de Armadura (5678). Cita literal de Maxroll: *"we need 1/5th the amount of Resistance to get the same DR%"*. ✅ **Verificado palabra por palabra.**
- ⚠️ **PERO — matiz crítico que la versión original de este informe se dejó (añadido por el verificador):** ese "5× más eficiente" es **por elemento**, y no significa que debáis priorizar Resistencias sobre Armadura. Maxroll confirma que **las Resistencias están divididas en 6 tipos de daño separados** (Frío/Cold, Fuego/Fire, Rayo/Lightning, Físico/Physical, Veneno/Poison, Sombra/Shadow), cada uno con su propio valor y su propia reducción, mientras que **la Armadura se aplica a los 6 tipos simultáneamente**. O sea: 1136 de Resistencia al Fuego solo os protege del fuego; 5678 de Armadura os protege de todo. Para cubrir los seis elementos hacen falta ~6 inversiones distintas, con lo que la ventaja del 5× se **diluye casi por completo** en la práctica. Maxroll **no recomienda priorizar una sobre otra**: dice textualmente que *"un buen reparto de Resistencias es una parte importante de aumentar vuestra supervivencia"* y aboga por invertir en **ambas capas defensivas de forma equilibrada**. Tratad el "5×" como *"no ignoréis los afijos de resistencia"*, **no** como *"pasad de la armadura"*.
- El viejo **tope del 70% de resistencias** es de la era *Season of Blood* (parche 1.2) y ya **no aplica**.
- La **Armadura ahora reduce TODO el daño**, físico y no físico. Antes solo físico.
- Existe una estadística nueva y dedicada de **Resistencia al Daño Físico** (Physical Damage Resistance).
- Habilidades y nodos de Paragón que antes daban Reducción de Daño ahora dan **bonus multiplicativos a Armadura o a Todas las Resistencias**.

### 2.3 Dureza (Toughness)

Estadística introducida en la Season 11, visible en la hoja de personaje bajo Poder de Ataque (Attack Power). Representa **el daño bruto total que podéis aguantar tras toda la mitigación**, promediado sobre los seis tipos de daño.

⚠️ **Aviso de min-maxer:** Maxroll advierte explícitamente que la Dureza promedio **es engañosa**. Un valor alto puede ocultar un agujero grave — por ejemplo armadura baja frente a enemigos de nivel alto, o una debilidad concreta a un tipo de daño. **Pasad el ratón por encima para ver el desglose por tipo de daño** y mirad el valor más bajo, no el promedio. Vuestro punto débil define en qué Torment reventáis.

**Objetivos orientativos de Dureza por Torment** (fuente secundaria, ver §9 contradicción E):

| Torment | Dureza aprox. |
|---|---|
| T6 | ~320.000 |
| T8 | ~800.000 |
| T10 | ~2.000.000 |
| T12 | ~5.000.000 |

### 2.4 Otros cambios defensivos relevantes (S11, vigentes en S14)

- **Fortificar (Fortify)** ya no es reducción de daño: es una **segunda barra de vida**. Se acumula hasta vuestra Vida Máxima y os cura un % de vida máxima por segundo consumiendo Fortify. Estáis "Fortificados" siempre, sin importar la cantidad.
- **Pociones:** capacidad base de 4. Curan el **35% de la vida total** al instante. Se regenera 1 poción cada 30 segundos. **Se eliminaron las mejoras de poción.**
- Subieron los valores de Vida al Golpear (Life on Hit), Regeneración de Vida y Vida al Matar (Life on Kill).

---

## 3. Escalado de monstruos por dificultad

**Los niveles de monstruo se eliminaron por completo** en el parche 2.0. Los monstruos **ya no tienen nivel**: escalan directamente con la dificultad seleccionada. Esto significa que:

- No hay zonas "de nivel bajo" ni "de nivel alto" en el mundo abierto. Toda Sanctuary es igual de dura dentro de una dificultad dada.
- Vuestro nivel de personaje **no** hace que los monstruos suban con vosotros dentro de la misma dificultad. Subir de nivel os hace genuinamente más fuertes hasta que vosotros decidís subir el escalón.
- El único mando que controla la dureza del mundo sois vosotros, en el menú de dificultad.

### 3.1 Escalado dentro de El Foso (relevante para desbloquear Torment)

El Foso sí escala piso a piso, y con tramos de pendiente distinta:

| Tramo de pisos | Daño infligido por piso | Puntos de vida por piso |
|---|---|---|
| Piso 2 | +15% | +50% |
| Piso 3 | +13% | +33% |
| Pisos 4–10 | +17,4% | +26,5% |
| Pisos 11–110 | **+4,74%** | **+17%** |
| Pisos 111+ | +2,37% | **+32%** |

**Lectura de min-maxer:** el tramo 4–10 es brutalmente empinado (+17,4% daño por piso) — es el muro que os vais a comer justo al desbloquear T1. A partir del piso 11 la pendiente de daño se aplana muchísimo (+4,74%), así que **si superáis Pit 10, los siguientes 20-30 pisos llegan mucho más rápido de lo que esperáis**. Y a partir de 111 el daño casi no sube pero la vida se dispara a +32%: ahí el juego pasa de ser un test de supervivencia a un test de DPS puro.

Cada intento de Foso tiene **cuenta atrás de 15 minutos** ✅ *(corregido por el verificador: la versión original de este informe decía 10 minutos; la guía del Foso de Maxroll, act. 16 jul 2026, dice literalmente "15-minute timer")*: hay que matar suficientes monstruos, invocar al jefe y matarlo dentro del tiempo. Terminar con tiempo sobrante **desbloquea pisos extra de golpe** (no solo el siguiente), lo cual acelera mucho la escalada de Torment.

---

## 4. LA RECOMENDACIÓN PRÁCTICA — a qué dificultad jugar en cada franja

### 4.1 El principio rector

Todas las fuentes convergen en la misma idea, y es contraintuitiva para un min-maxer novato:

> **XP/hora = densidad de monstruos × multiplicador de dificultad × velocidad de limpieza**

El multiplicador de dificultad es solo **uno de tres factores**. Maxroll lo dice sin rodeos en su guía de experiencia: *"Farmear experiencia no significa necesariamente jugar en la dificultad más alta."* Sus propias mediciones muestran que farmear en escalones inferiores puede ser **casi igual de eficiente** que en T12.

La regla operativa: **jugad la dificultad más alta en la que sigáis matando rápido.** No la más alta que podáis sobrevivir.

### 4.2 Tabla de recomendación por franja (Nigromante principiante, dúo, juego base)

| Franja | Dificultad recomendada | Razonamiento |
|---|---|---|
| **1–15** | **Difícil (Hard)** | Está desbloqueada por defecto y da +75% XP gratis. El nigromante de esbirros (Minion Necro) tiene ejército desde muy pronto y los esbirros tanquean por vosotros. Bajad a Normal solo si morís repetidamente. |
| **15–30** | **Experto (Expert)** | Desbloqueado tras el prólogo. +125% XP. Aquí el Minion Necro ya va sobrado: los esbirros absorben todo el daño. Es el escalón de mejor relación XP/riesgo para esta clase. |
| **30–50** | **Experto (Expert)**, subiendo a **Penitente** al acabar campaña | Mantened Experto mientras la limpieza sea fluida. En cuanto termine la campaña base, Penitente (+175% XP). |
| **50–60** | **Penitente (Penitent)** | +175% XP. Ojo: el nivel máximo ya **no** es 60, esta franja no tiene nada especial. Es tránsito. |
| **60–70** | **Penitente (Penitent)** | Seguid aquí. **No corráis a Torment I nada más tocar 70.** |
| **Paragon temprano (P1–P60 aprox.)** | **Penitente (Penitent)** → luego **T1** | ⚠️ **Este es el error clásico.** Saltar a T1 nada más llegar a 70 es una trampa: acumulad potencia antes. ⚠️ *Corrección del verificador: las cifras concretas de esta celda —"40–50 puntos de Paragón" para el primer nodo legendario, "60–100% de daño" por nodo, y el nodo "**Cold Leader**" con "+200% de daño"— **NO las he podido confirmar en ninguna fuente**. Trátalas como no verificadas; el nombre "Cold Leader" en particular es sospechoso de estar inventado o mal recordado.* Lo que **sí** dice Maxroll (*Endgame Progression*, act. 9 jul 2026) es: subid los **glifos (Glyphs) a nivel 25** primero y luego a **51** para desbloquear sus bonus legendarios, y farmead Paragón *"hasta aproximadamente el nivel de Paragón ~100"* en esta fase. Después: Pit 10 → **Torment I**. |
| **Paragon medio** | **T1 → T4, rápido** | Los primeros Torment "son fáciles de conquistar incluso con una build de leveling". Encadenad Pit 15/20/25. ⚠️ *Corregido: el umbral de "850 de poder de objeto" para reemplazar equipo **no existe como regla de progresión** — el 850 es el requisito del **Único que metéis al crafteo de Míticos**, y el informe original confundió las dos cosas. Lo que Maxroll dice de verdad para esta fase es usar los Manuales de Temple sobre equipo de **750 de poder de objeto**.* Meta intermedia: completar los **Amuletos de Conjunto (Set Charms)**, que caen a partir de T3 — Icy Veins lo señala como "un buen hito para progresar a una dificultad superior". |
| **Paragon tardío** | **T5 → T12**, con freno | A partir de T5 el gate real es el Foso (30/40/50/60/70/80/90/100), no vuestro nivel. Aquí ya toca min-max de verdad: Dureza, resistencias, nodos legendarios. |

### 4.3 Nota específica para dúo

- **Bonus de XP por grupo:** +5% por estar cerca de otro jugador, **+10% por estar en el mismo grupo**. Jugar en dúo es XP gratis: id siempre agrupados.
- **Hogueras (Campfires):** hasta **+15%** de XP, acumulable.
- **Escalado por tamaño de grupo:** ⚠️ Las mazmorras escalan vida y daño de los monstruos con el número de jugadores (hasta 4); el mundo abierto **no** escala. Con lo cual, en dúo, **el mundo abierto y las Helltides son desproporcionadamente fáciles y rentables** frente a las mazmorras. Farmead mundo abierto en dúo. (Ver §9, contradicción G — esta info puede ser anterior al parche 2.0.)
- Dos nigromantes de esbirros en dúo = pantalla llena de esbirros. Podéis permitiros **un escalón más de dificultad del que os tocaría en solitario** durante todo el leveling.

---

## 5. LA SEÑAL CONCRETA — "¿ya puedo subir de dificultad?"

Esto es lo que pedíais: criterios medibles, no sensaciones.

### 5.1 Señales de SUBIR ✅

| Señal | Umbral concreto |
|---|---|
| **Tiempo de run del Foso** | Limpiáis el Pit asociado a vuestro Torment actual **en 5 minutos o menos**. ✅ *(corregido: la cita literal de Maxroll es "the clears should last a maximum of 5 minutes to stay efficient". El "menos de 3 minutos" de la versión original NO aparece en Maxroll — procede de mtmmo.com, sitio de boosting.)* |
| **Tiempo de jefe de piso** | El jefe del Foso muere en **≤ 30 segundos**. ⚠️ *Umbral de fuente secundaria (mtmmo.com), no confirmado en Maxroll ni Icy Veins. Orientativo.* |
| **Regla maestra de Maxroll** | *"Solo cambiad a Torment superior cuando podáis hacer los pisos del Foso asociados a esa dificultad."* El Foso **es** el test de aptitud, por diseño. |
| **Salto de potencia** | Acabáis de desbloquear una habilidad clave, os ha caído un legendario/aspecto que cambia la build, o habéis subido un **glifo a nivel 25 / 51** (los umbrales que Maxroll sí documenta). *El "60–100% de daño por nodo legendario" no está verificado.* Subid inmediatamente. |
| **Hito de equipo** | Habéis completado un set de **Amuletos de Conjunto (Set Charms)** (caen desde T3). *El umbral de "850 de poder de objeto" era erróneo — ver §4.2.* |
| **Contenido estacional** | Ya no sufrís en Helltides ni en el contenido de temporada del escalón siguiente (criterio de Icy Veins). |

### 5.2 Señales de NO subir / BAJAR ❌

| Señal | Umbral concreto |
|---|---|
| **Run del Foso** | Las runs se alargan **más de 5 minutos** → NO subáis. *(umbral de Maxroll, corregido)* |
| **Jefe de piso** | El jefe tarda **bastante más de 30 segundos** → NO subáis. *(orientativo, fuente secundaria)* |
| **Muertes** | Morir repetidamente. Cada muerte es tiempo de viaje perdido; en un ARPG el coste real de morir es el *downtime*, no la penalización. |
| **"Slugfest"** | Icy Veins describe el síntoma del escalón demasiado alto como *"peleas de 5 minutos contra jefes"* sin mejora proporcional en la calidad del equipo. Si un jefe normal os lleva minutos, estáis quemando XP/hora. |
| **Sensación de goteo** | Maxroll: si el progreso se ralentiza de forma notable, **volver a una dificultad inferior es aceptable y correcto**. No hay orgullo en el escalón. |

### 5.3 El test de 60 segundos que podéis hacer hoy

1. Cronometrad una limpieza de una mazmorra/Helltide en vuestra dificultad actual.
2. Subid un escalón. Repetid.
3. Si el tiempo sube **menos de un 75%** (para Normal→Hard) o menos del % de XP que ganáis, **el escalón nuevo es rentable**. Si sube más, no lo es.

Esa es literalmente la matemática: el bonus de XP tiene que superar la pérdida de velocidad. Con +75% (Hard) o +125% (Expert), tenéis mucho margen. Con +100% marginal entre Torments consecutivos (p.ej. T7→T8 pasa de +900% a +1000%, que es solo un **+10% relativo**), el margen es **minúsculo**. Ojo con esto: **subir de T7 a T8 solo os da un 10% más de XP**, no un 100%. Los escalones altos de Torment se justifican por **botín** (runas, amuletos únicos, sellos míticos), **no** por XP.

---

## 6. Actividades de farmeo y su dificultad óptima (S14)

Según las mediciones de Maxroll (con una build tope, Dance of Knives Rogue, en Torment XII):

| Actividad | XP/minuto aprox. |
|---|---|
| Hordas Infernales (Infernal Hordes) | ~6.000.000 |
| Mazmorras de Pesadilla (Nightmare Dungeons) | ~4.300.000 |
| El Foso, piso 100 | ~3.300.000 |

⚠️ Contradicción: otra fuente sitúa la prioridad de farmeo de Paragón como **Mazmorras de Pesadilla > Ciudad Subterránea (Undercity) > Hordas Infernales**, diciendo que las Hordas "tardan más en terminarse" pese a haber sido buffeadas. Ver §9.

Para S14 concretamente: los **Hellwyrms / gusanos dentro de las Helltides** están señalados como uno de los métodos de XP de Paragón más rápidos, y como acelerador para los últimos 10–15 niveles del 1–70. ✅ Las Helltides son contenido de juego base.

Elemento adicional para vuestro dúo: los **datos de elite** — los enemigos de élite dan la mayor XP, recibiendo *"XP base del enemigo + 4704"* **antes** de aplicar el multiplicador de dificultad. Traducción min-max: **el multiplicador de dificultad se aplica encima del bono plano de élite**, así que cazar élites en dificultad alta es donde el multiplicador rinde más. Priorizad densidad de élites.

---

## 7. Season 14 y la dificultad

La mecánica estacional son las **Rupturas del Pandemónium (Pandemonium Ruptures)**: grietas que aparecen por Sanctuary, con más frecuencia en Helltides. Se mantienen abiertas matando enemigos y cerrando "Desgarros" (Tears), y dan reputación en forma de **Destellos de Esperanza (Glints of Hope)**.

Tres tipos:
- **Normales** — mundo abierto
- **Surgentes (Surging)** — dentro de Helltides
- **Colosales (Colossal)** — en los Campos de Profanación (Fields of Desecration)

Matar al jefe **Caminante del Reino (Realmwalker)** dentro de una ruptura abre la **Cámara del Doblar de Muerte (Deathtoll Chamber)**, una mini-mazmorra de una sala con recompensas mejoradas.

**Relevante para la dificultad:** 🔴 **CORREGIDO POR EL VERIFICADOR.** La versión original atribuía estos cambios al parche **3.1.3**. Es falso: al abrir la URL de Blizzard que el propio informe citaba (`news.blizzard.com/.../24287406`) resulta ser el parche **3.1.0, build 72592, del 30 de junio de 2026** — no el 3.1.3 build 73224 del 12 de agosto. Los cambios reales que dicen esas notas, y su parche correcto, son:

- *(parche **3.1.0**)* "The overall difficulty for Ruptures has been decreased in normal difficulty, so lower-level players can more confidently clear them." → os beneficia como principiantes. ✅
- *(parche **3.1.0**)* "The spawn rate for elite monsters in Ruptures has been increased." → os beneficia. ✅
- *(parche **3.1.0**)* "Increased experience rewards in Torment 8 and up" — 🔒 **pero OJO: esta línea está dentro de la sección de actividades de PLANES DE GUERRA (War Plan), que es contenido de *Lord of Hatred*.** No es un aumento global de XP en T8+. **A vosotros, con juego base, NO os aplica.** La versión original lo presentaba como una mejora general; era un error de lectura.

⚠️ **No he podido verificar el contenido del parche 3.1.3 (build 73224, 12 ago 2026) en ninguna fuente primaria**: el índice de noticias de Blizzard y los agregadores (Wowhead, Icy Veins) no me devolvieron el artículo. Todo lo que este informe atribuya específicamente a 3.1.3 debe considerarse **sin confirmar**.

**Modo Solo Self-Found (SSF):** nuevo, exclusivo de temporada. Impide agrupar y comerciar, con alijo y progresión separados y leaderboards dedicados. ⚠️ **Para vuestro caso concreto: SSF es incompatible con jugar en dúo.** Si vuestro objetivo es leaderboard *y* jugar juntos, tenéis que ir por la vía estándar, no SSF.

---

## 8. Juego base vs. expansiones — desglose exhaustivo

### ✅ Disponible con JUEGO BASE (gratis en el parche 3.0)

- **Nivel máximo 70** (subió de 60)
- **Los 12 niveles de Torment** ← el punto clave
- **Revisión completa de El Foso** (5 pisos, nuevos layouts, 150 tiers)
- **Filtro de botín (Loot Filter)** — ocultar/mostrar/colorear drops por reglas propias
- **Revisión de gemas** — bonus de daño multiplicativos ligados a elementos
- **Rework del árbol de habilidades** — reestructuración y asignación libre de puntos
- Rework de afijos de daño, cambios de objetos Únicos, rework de jefes de guarida (Lair Boss), superposición de mapa, *pathfinding*, rebalanceo de Aspectos
- **Clases:** Bárbaro, Druida, **Nigromante**, Pícaro, Hechicero
- **Zonas:** toda la Sanctuary original
- **Actividades:** Helltides, Mazmorras de Pesadilla, Jefes del Mundo, Susurros de los Muertos (Whispers of the Dead), El Foso, juego en grupo
- **Paragón** (200+ puntos)
- Participación completa en la temporada con las clases originales

### 🔒 Requiere *Vessel of Hatred*

- Clase **Spiritborn**
- **Mercenarios (Mercenaries)** ← os afecta, ver abajo
- **Palabras rúnicas (Runewords)** ← os afecta
- Zona Nahantu / Kurast

### 🔒 Requiere *Lord of Hatred*

- Clases **Warlock** y **Paladín (Paladin)**
- **Planes de Guerra (War Plans)** — sistema de actividades encadenables
- **Cubo Horadrim (Horadric Cube)** — añadir/quitar/rerollear afijos, craftear amuletos, crear runas, Transfiguración ← **os afecta mucho**
- **Talismanes (Talismans)** y sus bonus de conjunto
- Campaña de las Islas Skovos / ciudad de Temis
- Tercera variante de habilidad (los jugadores gratuitos tienen 2 variantes por habilidad; con expansión, 3)

### ⚠️ Impacto real de lo que os falta

1. 🔒 **Mercenarios:** las guías de progresión de S14 recomiendan explícitamente reclutar a **Raheir** (da resistencias y burbuja Bastion) y **Aldkin** (reduce el daño enemigo ~20%) como muleta de supervivencia al entrar en Torment 1. **Vosotros no los tendréis.** Compensadlo con más inversión en Resistencias (recordad: 5× más eficientes que Armadura punto por punto) y aprovechando que sois dos.
2. 🟡 **La guía de leveling de Nigromante de Esbirros de Maxroll (S Tier) menciona Mercenarios y Palabras Rúnicas — pero como MEJORAS OPCIONALES, no como requisitos.** ✅ *Matizado por el verificador tras abrir la guía (act. 30 jun 2026, S14):* la build **funciona sin ellos**; el texto recomienda a Raheir y a Aldkin *"una vez estén disponibles"* y dice que para las Runewords *"existen alternativas si no tenéis acceso a runas de nivel alto"*. La guía **sí asume acceso a *Vessel of Hatred*** y no ofrece una variante explícita de juego base, así que tendréis que traducir vosotros — pero la conclusión es más benigna de lo que decía la versión original: **seguid la guía y saltaos esas dos secciones, la build sigue en pie.** Habilidades clave confirmadas literalmente en la guía: **Skeleton Warrior, Skeleton Mage, Golem, Iron Maiden** y **Reap** (solo early game). Nota: la guía recomienda empezar en **"Normal o Difícil (Hard)"**, no solo en Hard.
3. 🟡 **Cubo Horadrim y Míticos — CORREGIDO POR EL VERIFICADOR. La versión original era demasiado alarmista.** El rework "Mythic Unique 3.0" de la S14 es real y está bien descrito (Mítico deja de ser una rareza y pasa a ser una **Calidad de objeto modificable**; cualquier Único puede volverse Mítico, siempre Ancestral, con el poder único +30% y el resto de afijos al máximo). Pero la afirmación *"el crafteo de Míticos os está vedado"* **es falsa**. La guía de temporada de Maxroll (act. 13 jul 2026) documenta **DOS rutas de crafteo, no una**:
   - **Ruta A — Cubo Horadrim (Horadric Cube):** 1 Único de 850+ del mismo slot + **5 Fragmentos del Pandemónium** (Pandemonium Fragments). 🔒 El Cubo requiere *Lord of Hatred* (confirmado por Nerdschalk, act. 27 abr 2026, que lo lista explícitamente como "No" para juego base).
   - **Ruta B — Joyero (Jeweler):** **18 Runas concretas + 3 Chispas Resplandecientes** (Resplendent Sparks). ⚠️ Esta ruta **no pasa por el Cubo**. Caveat honesto: las Runas son contenido de *Vessel of Hatred*, así que esta vía **también podría estaros cerrada** — no he podido confirmar si el Joyero exige Runas obtenibles solo con VoH. **Verificad in-game.**
   - **Ruta C — que caigan.** La tabla de botín de Maxroll dice que en **Torment 1 ya aumentan los "Legendary, Unique and Mythic Unique items per Torment tier"**. Es decir: **los Únicos Míticos CAEN como botín**, sin craftear y sin ninguna expansión. Ambas rutas de crafteo exigen nivel 70 y dificultad Torment o superior — requisitos que vosotros SÍ cumplís con juego base.

   **Conclusión corregida:** no tener el Cubo os **encarece y ralentiza** el acceso a Míticos (perdéis la ruta de crafteo dirigido), pero **no os los prohíbe**. No es "el mayor obstáculo para un objetivo de leaderboard": es una desventaja de eficiencia, no un muro.
4. ✅ **Pero las dificultades en sí, ninguna, os están bloqueadas.** Podéis llegar a T12.

---

## 9. Incertidumbres y contradicciones

Reporto todo lo que no he podido cerrar, sin promediar.

**A. ¿Torment V–XII requieren *Lord of Hatred*?** 🔴 **La contradicción más importante.**
- **Fextralife** (wiki) afirma literalmente que *"Torment V a Torment XII son exclusivos de la expansión Lord of Hatred"*.
- **Nerdschalk**, **Phrasemaker** (desglose free-vs-paid) y el consenso de búsqueda dicen lo contrario: los **12 niveles de Torment son gratuitos en el parche 3.0** para todos.
- **Mi lectura:** 3 fuentes contra 1, y la fuente discrepante es una wiki editada por comunidad con notoria deriva. **Me inclino fuertemente por "gratis, sin expansión"**, pero como es la pregunta que más os importa, **verificadlo in-game**: mirad si el selector de dificultad os muestra T5+ bloqueado por candado de expansión o solo por requisito de Foso.

🟢 **RESUELTO POR EL VERIFICADOR — a favor de "gratis, sin expansión". Dos pruebas nuevas:**
1. **Fextralife se contradice a sí misma en la misma página.** Al abrirla directamente, la frase *"Torment V through Torment XII are exclusive to the Lord of Hatred expansion"* convive con **su propia tabla de dificultades**, que lista **los 12 Torment desbloqueándose por pisos del Foso** (T1 = Pit 10 … T12 = Pit 100) **sin mencionar ninguna expansión**. Además la página se autodescribe como cobertura de *"Vessel of Hatred and Patch 2.0"*, es decir, **es una página de la era 2.x parcheada a mano**. Una fuente que se contradice internamente y se declara desactualizada no compite con Maxroll.
2. **Nerdschalk (act. 27 abr 2026) es explícito y literal:** sin *Lord of Hatred* tenéis *"up to tier 12 for scaling difficulty"* y *"max level 70"*. Su tabla free-vs-paid pone **nivel 70 y Torment 1–12 en la columna GRATIS**.
- **Veredicto: los 12 Torment y el nivel 70 son de juego base. La afirmación central del informe es CORRECTA.** Aun así, la verificación in-game sigue siendo gratis de hacer.

**B. Pisos del Foso requeridos por Torment.**
- **Maxroll (S14, act. 26 jun 2026):** T1=10, T2=15, T3=20, T4=25, T5=30, T6=40, T7=50, T8=60, T9=70, T10=80, T11=90, T12=100.
- **Icy Veins (página de world tiers):** T1=10, T2=25, T3=40, T4=55, y **solo cuatro Torment**.
- **Diagnóstico:** la página de Icy Veins es de la era *Vessel of Hatred* (parche 2.x) y **está sin actualizar**. Maxroll es coherente con Fextralife en el patrón (5 en 5 hasta T4, luego de 10 en 10). **Usad los números de Maxroll.**

**C. Bonus de oro de Hard / Expert / Penitent.**
- Una fuente: Hard +75%, Expert +125%, Penitent +175% (idénticos a la XP).
- Fextralife: Hard +25%, Expert +50%, Penitent +75%.
- **Sin resolver.** El oro es irrelevante para vuestro min-max de XP, así que no he invertido más en cerrarlo.

**D. Requisito de desbloqueo de Penitente.** 🟡 **Actualizado por el verificador — y la contradicción es peor de lo que decía el informe.**
- Unas fuentes: "al alcanzar **nivel 50**".
- **Fextralife (leído directamente):** Experto *"Requires completing the Campaign Prologue"* y Penitente *"Requires completing the base Campaign"*. Esto **coincide con lo que afirmaba el informe**.
- 🔴 **Pero Maxroll (*Difficulty Scaling*, act. 26 jun 2026) contradice a ambas:** al preguntarle explícitamente por los requisitos de desbloqueo, la página lista Normal, Hard, Expert y Penitent **sin ningún requisito**, presentándolas como disponibles desde la creación de personaje. Solo los Torment llevan requisito (nivel 70 + Foso).
- **Sin resolver, ahora a tres bandas.** Impacto práctico bajo: en cuanto abráis el menú de dificultad lo veréis. Si Maxroll tiene razón, podéis ir a **Penitente (+175% XP) desde el nivel 1**, lo cual cambiaría bastante la tabla de §4.2 — **comprobadlo en el primer minuto de juego, es gratis y es la optimización de XP más barata que tenéis.**

**D-bis. Nombre de la zona de *Lord of Hatred*.** ⚠️ *Añadido por el verificador.* El informe dice "Islas Skovos / ciudad de Temis". **Nerdschalk (act. 27 abr 2026) la llama "Sowos"** y añade un contenido llamado **"Echo of Hatred"** que el informe no menciona. **No he podido determinar cuál es el nombre correcto.** Irrelevante para vosotros (es contenido de pago), pero es señal de que la sección de expansiones del informe no está totalmente asentada.

**E. Objetivos de Dureza y Armadura por Torment.**
- Icy Veins da Dureza recomendada T1=2.000, T2=5.000, T3=15.000, T4=35.000 — números **de la era pre-Season 11**, cuando "Toughness" ni existía como stat. **Descartables.**
- Otra fuente da T6=320k, T8=800k, T10=2M, T12=5M. Órdenes de magnitud completamente distintos, consistentes con el rework. **Son los que he usado, pero son de fuente secundaria (sitio de boosting), no de Maxroll/Icy Veins. Tratadlos como orientativos.**
- La cifra de "~13.300–13.500 de Armadura para Torment 4" viene de un artículo sobre Spiritborn y **es sospechosa de ser pre-S11**. No la he podido confirmar para 3.1.3.
- **Maxroll evita deliberadamente dar objetivos numéricos de Dureza**, y remite a las guías de build individuales. Eso es probablemente lo más honesto.

**F. Tope de resistencias: 70% o asíntota del 90%.**
- El "tope 70%" aparece en fuentes de la era *Season of Blood* (parche 1.2).
- La fórmula actual de Maxroll (act. 16 ago 2026) implica **asíntota a 90% de reducción de daño, sin tope duro**.
- **Considero resuelto a favor de la fórmula de Maxroll** por ser la fuente más reciente y específica, pero el "70%" sigue circulando mucho.

**G. Escalado por tamaño de grupo.**
- La info que he encontrado (mazmorras escalan con nº de jugadores hasta 4; mundo abierto no) proviene de artículos que **parecen anteriores al parche 2.0**, cuando se eliminaron los niveles de monstruo.
- **No he podido confirmar que siga siendo así en 3.1.3.** Dado que ahora los monstruos escalan con dificultad y no con nivel, es plausible que el modelo haya cambiado. **Verificad empíricamente en dúo.**

**H. ¿El Cubo Horadrim es gratis o de pago?** 🟢 **PARCIALMENTE RESUELTO POR EL VERIFICADOR.**
- **El Cubo es de pago.** Nerdschalk (act. 27 abr 2026) lo lista sin ambigüedad como **"No"** disponible sin la expansión, con la nota *"20+ new crafting recipes"* bloqueadas tras *Lord of Hatred*. Confirmado.
- **Pero la consecuencia que el informe extraía de ahí era falsa.** Maxroll documenta una **segunda ruta de crafteo de Míticos vía el Joyero (Jeweler)** — 18 Runas + 3 Chispas Resplandecientes — que no usa el Cubo; y **los Únicos Míticos caen como botín ya desde Torment 1**. Ver §8.3 reescrito.
- **Sigue abierto:** si la ruta del Joyero exige Runas que solo se obtienen con *Vessel of Hatred*. **Verificad in-game.**

**I. Prioridad de actividades para XP.**
- Maxroll (medido): Hordas Infernales > Mazmorras de Pesadilla > Foso 100.
- Otra fuente: Mazmorras de Pesadilla > Undercity > Hordas Infernales ("las Hordas tardan más").
- **Probable causa de la discrepancia:** Maxroll mide XP/minuto *dentro* de la actividad; la otra fuente considera el tiempo total de setup/reinicio. **No es necesariamente una contradicción real, sino dos métricas distintas.** Nota: **Undercity (Ciudad Subterránea) es contenido 🔒 de *Vessel of Hatred***, así que esa vía os está cerrada de todas formas.

**J. Datos que NO he podido encontrar en absoluto:**
- Multiplicadores numéricos exactos de **vida y daño de los monstruos por escalón de dificultad** fuera del Foso (Normal→Hard→Expert→Penitent→T1…T12). Ninguna fuente publica esta tabla. Solo tenemos los bonus de XP/oro como proxy.
- Cifras de **densidad de monstruos** por dificultad.
- Si existe alguna penalización de **velocidad de movimiento, curación o regeneración** ligada al Torment en 3.1.3.

---

## 10. Plan de acción concreto para vuestro dúo

1. **Empezad en Difícil (Hard)** desde el minuto uno. Los dos. Es gratis, es +75% XP, y dos Nigromantes de esbirros lo trivializan.
2. **Subid a Experto (Expert)** en cuanto acabéis el prólogo. No lo penséis.
3. **Penitente al terminar la campaña.** Ahí os quedáis.
4. **Nivel 70 ≠ Torment.** Quedaos en Penitente farmeando Helltides (y los gusanos/Hellwyrms) acumulando Paragón y **subiendo glifos a nivel 25** antes de saltar. *(Corregido: el "40–50 puntos de Paragón / primer nodo legendario" no está verificado en ninguna fuente; el umbral de glifo 25→51 sí es de Maxroll.)* Esto es lo que separa a quien progresa de quien se atasca.
5. **Completad el Rango II del Recorrido de Temporada** ("Descenso Infernal") para abrir El Foso.
6. **Pit 10 → Torment I.** *(Corregido: olvidad la regla del "850 de poder de objeto" — no existe; ver §4.2.)*
7. **A partir de ahí, el Foso es vuestro termómetro.** Regla única: *si limpiáis el Foso de vuestro Torment en 5 minutos o menos, subid. Si no, no.* (El jefe en ≤30 s es un indicador extra, de fuente secundaria.)
8. **No descuidéis las Resistencias** — punto por punto son 5× más eficientes que la Armadura — **pero no las prioricéis por encima de la Armadura.** ⚠️ *(corregido por el verificador, ver §2.2bis)*: las Resistencias están **divididas en 6 elementos** (Frío, Fuego, Rayo, Físico, Veneno, Sombra) y cada una solo mitiga su propio tipo de daño, mientras que la **Armadura reduce los 6 a la vez**. Cubrir los 6 elementos cuesta ~6 inversiones separadas, así que la ventaja de "5×" se diluye casi por completo en la práctica. Maxroll recomienda literalmente **un buen reparto de ambas**, no priorizar una. Y mirad siempre el **desglose de Dureza por tipo de daño**, nunca el promedio: vuestro tipo de daño más débil es el que os mata.
9. **Compensad la falta de Mercenarios** con defensas propias y con el hecho de ser dos. Agrupaos siempre (+10% XP) y usad hogueras (+15%).
10. **Recordad:** de T7 a T8 solo ganáis un **+10% relativo de XP**. Los Torment altos se persiguen por **botín**, no por experiencia. No os matéis por subir escalones que no os rinden.

---

## Fuentes

Páginas realmente abiertas y leídas durante esta investigación:

- https://maxroll.gg/d4/resources/difficulty-overview — *Difficulty Scaling for Diablo 4* (act. 26 jun 2026, S14) — tabla Torment I–XII, escalado del Foso, botín por tier
- https://maxroll.gg/d4/resources/experience — *Experience in Diablo 4* (act. 21 jul 2026, S14) — nivel máx. 70, bonus XP, XP/min por actividad, bonus de grupo
- https://maxroll.gg/d4/getting-started/defenses-for-beginners — *In-depth Defense Guide* (act. **16 ago 2026**) — fórmulas de Armadura/Resistencia, constantes 5678 y 1136, asíntota 90%
- https://maxroll.gg/d4/meta/endgame-progression — *Endgame Progression* (act. 9 jul 2026, S14) — mapeo Pit→Torment, señal de "menos de 3–5 min"
- https://maxroll.gg/d4/resources/pit-guide — *The Artificer's Pit* (act. 16 jul 2026, S14) — desbloqueo vía Season Rank II, 150 pisos
- https://maxroll.gg/d4/resources/season-guide — *Season of Death Awakening* (act. 13 jul 2026) — Pandemonium Ruptures, Mythic Unique 3.0, SSF
- https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide — *Minion Necromancer Leveling* (act. 30 jun 2026, S14) — recomendación "Hard o superior", dependencia de VoH
- https://maxroll.gg/d4/tierlists/necromancer-leveling-builds-tier-list — *Necromancer Leveling Tier List* (act. 29 jun 2026) — Minion Necro en S Tier
- https://www.icy-veins.com/d4/guides/necromancer-leveling-guide/ — *Necromancer Leveling Guide* (act. 26 jun 2026, S14) — "empezad en Hard", síntoma del "slugfest de 5 minutos"
- https://www.icy-veins.com/d4/news/diablo-4s-biggest-defense-rework-ever-lands-in-season-11/ — rework defensivo S11: **eliminación de penalizaciones de Armadura/Resistencia por Torment**, Toughness, Fortify, pociones
- https://www.icy-veins.com/d4/news/best-ways-to-progress-through-the-endgame-in-diablo-4-season-14/ — progresión endgame S14, Set Charms como hito, nodos legendarios 60–100%
- https://www.icy-veins.com/d4/guides/world-tier-difficulty/ — *World Difficulty* — ⚠️ **página desactualizada** (solo T1–T4), usada para documentar la contradicción B
- https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes — notas oficiales, parche **3.1.3 build 73224 (12 ago 2026)** — XP aumentada en T8+, Polvo Primordial T7+, gemas T10+, ajuste de Rupturas en Normal
- https://diablo4.wiki.fextralife.com/Difficulty+Modes — tabla de dificultades con bonus de oro; ⚠️ fuente de la contradicción A (afirma que T5–T12 son exclusivos de expansión)
- https://nerdschalk.com/diablo-4-how-to-continue-playing-diablo-4-without-lord-of-hatred-torment-tiers-and-seasons-without-expansion/ — desglose base vs expansión: nivel 70 y Torment 12 accesibles sin expansión
- https://thephrasemaker.com/2026/04/28/diablo-4-lord-of-hatred-free-vs-paid/ — desglose free vs paid del parche 3.0 / Lord of Hatred
- https://d4builds.gg/leveling-guide/ — guía de leveling S14: "empezad en Normal, ajustad según clearspeed"; Pit 10 → T1
- https://www.mtmmo.com/news/2276--how-to-unlock-torment-1--reach-t12-fast-in-diablo-4-season-14 — (2 jul 2026) objetivos de Dureza T6/T8/T10/T12, benchmarks de tiempo, Mercenarios Raheir/Aldkin

**Fuentes que devolvieron HTTP 403 y no pude leer:** purediablo.com/diablo4/Difficulties, mobalytics.gg (parche 3.1.3 y guía Lord of Hatred), boostmatch.gg (guía Torment I–XII S13).

**Nota metodológica:** he priorizado Maxroll para datos numéricos por ser la fuente con fechas de actualización explícitas y verificables dentro de la Season 14 (la más reciente, del 16 de agosto de 2026, es de hace dos días). He marcado como sospechosa toda fuente sin fecha o cuyo contenido describe solo cuatro niveles de Torment, ya que eso la sitúa inequívocamente antes del parche 3.0 (abril de 2026).

---

## Nota del verificador

*(Añadida el 18 de agosto de 2026 por un segundo agente cuyo encargo era **intentar refutar** este informe, no confirmarlo.)*

### Limitación metodológica que debéis conocer

🔴 **La sesión de verificación agotó su presupuesto de búsquedas web antes de empezar (200/200 consumidas), así que NO pude hacer ni una sola búsqueda.** Toda la verificación se hizo abriendo **directamente** las URL que el propio informe citaba, más algunos intentos de localizar fuentes nuevas a ciegas. Consecuencia honesta: **soy bueno detectando que el informe leyó mal sus propias fuentes, y malo detectando fuentes que al informe se le escaparon.** Un sesgo de confirmación residual es inevitable. Tomadlo en cuenta.

**Páginas abiertas y leídas en esta verificación (11 distintas):** `maxroll.gg/d4/resources/difficulty-overview` (3 consultas), `maxroll.gg/d4/getting-started/defenses-for-beginners` (2), `maxroll.gg/d4/resources/experience`, `maxroll.gg/d4/resources/pit-guide`, `maxroll.gg/d4/resources/season-guide`, `maxroll.gg/d4/meta/endgame-progression`, `maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide`, `icy-veins.com/d4/news/diablo-4s-biggest-defense-rework-ever-lands-in-season-11/`, `diablo4.wiki.fextralife.com/Difficulty+Modes`, `nerdschalk.com/...without-lord-of-hatred...`, `news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes`.
**No accesibles:** `icy-veins.com/d4/diablo-4-patch-notes` (404), `maxroll.gg/d4/resources/patch-notes` (404), índices de `news.blizzard.com/en-us/diablo4` y `wowhead.com/diablo-4/news` (devolvieron solo cabecera).

---

### ✅ Lo que resistió el intento de refutación (verificado literalmente)

Esto lo di por bueno **tras leer la fuente original, no por confianza en el informe**:

1. **La tesis central es CORRECTA: los 12 niveles de Torment y el nivel máximo 70 son de JUEGO BASE.** Reforzada con dos pruebas nuevas que el informe no tenía — ver §9-A reescrito. Además descubrí que **Fextralife se contradice dentro de su propia página**, lo que la descarta como fuente discrepante seria.
2. **Requisitos de Foso por Torment (T1=10 … T12=100):** cita literal de Maxroll, **exactos, uno por uno**.
3. **Fórmula de defensas y constantes 5678 / 1136, asíntota 90%:** cita literal de Maxroll (act. 16 ago 2026). Incluida la frase del 1/5.
4. **Eliminación de las penalizaciones de Armadura/Resistencia por Torment en la S11:** cita literal de Icy Veins. El informe acertaba, y acertaba al llamar obsoletos los "-25% en T1".
5. **Tabla de escalado del Foso** (piso 2 +15%/+50%, piso 3 +13%/+33%, 4–10 +17,4%/+26,5%, 11–110 +4,74%/+17%, 111+ +2,37%/+32%): **exacta, celda por celda**.
6. **Bonus de XP** Hard +75% / Expert +125% / Penitent +175% / Torment +300%→+1400%; **grupo +5% cerca y +10% en party** (radio 90 m); **hoguera +15%**; **élite "+4704" plano**; XP/min por actividad y el detalle de que se midió con **Dance of Knives Rogue en Torment XII**. Todo literal.
7. **Botín por Torment:** T1 Ancestral, T2 Manuales de Temple legendarios + Pergamino de Restauración, T3 Set Charms, T5 Runas legendarias, T8 Amuletos únicos, T10 Sellos Horadrim Míticos. Literal.
8. **Foso:** desbloqueo por "Hellish Descent" del Rango II del Recorrido de Temporada (nivel 70 en Eterno), **150 tiers**, pisos extra por acabar rápido. Literal.
9. **S14:** Pandemonium Ruptures y sus tres variantes, **Corrupted Reaper** como lair boss (vía "Pandemonium Threshold" en Zarbinzet), y **SSF incompatible con dúo** (no permite party) — todo confirmado. El aviso sobre SSF es correcto y os importa.

---

### 🔴 Errores encontrados y corregidos en el cuerpo del documento

| # | Error | Corrección | Gravedad |
|---|---|---|---|
| 1 | **Cuenta atrás del Foso de "10 minutos"** | Son **15 minutos** (cita literal de Maxroll) | Media — afecta a cómo planificáis una run |
| 2 | **Atribuye cambios al parche 3.1.3 citando una URL que es del 3.1.0** (build 72592, 30 jun 2026) | Reatribuido al 3.1.0. **El contenido real del 3.1.3 queda SIN VERIFICAR** | Alta — mina la vigencia declarada del informe |
| 3 | **"XP aumentada en Torment 8+" presentada como mejora general** | Esa línea está en la sección de **Planes de Guerra (War Plans)** = 🔒 *Lord of Hatred*. **A vosotros NO os aplica** | Alta — es exactamente el tipo de error que el brief pedía cazar |
| 4 | **"El crafteo de Míticos os está vedado"** | **Falso.** Hay una 2ª ruta (Joyero: 18 Runas + 3 Chispas Resplandecientes) y además **los Míticos CAEN desde T1**. Sin Cubo vais más lentos, no bloqueados | Alta — era la conclusión más desmoralizante del informe y estaba mal |
| 5 | **"Invertid en Resistencias antes que en Armadura"** | El "5×" es **por elemento**: hay **6 resistencias separadas** y la Armadura cubre las 6 a la vez, así que la ventaja se diluye. Maxroll aboga por **reparto equilibrado**, no por priorizar | Alta — es un consejo de min-max activamente perjudicial |
| 6 | **Umbral de "menos de 3 minutos" atribuido a Maxroll** | Maxroll dice **"máximo 5 minutos"**. El "3 min" y el "jefe en ≤30 s" vienen de **mtmmo.com, un sitio de boosting**, no de Maxroll | Media — os haría quedaros estancados de más |
| 7 | **"Reemplazad todo lo que esté por debajo de 850 de poder de objeto"** | No existe tal regla. **850 es el requisito del Único que metéis al crafteo de Míticos.** Maxroll habla de **750** para Manuales de Temple | Media |
| 8 | **"40–50 puntos de Paragón para el primer nodo legendario", "60–100% de daño por nodo", nodo "Cold Leader" con "+200%"** | **Nada de esto lo he podido confirmar.** Marcado como no verificado; el nombre *Cold Leader* huele a inventado. Lo que Maxroll sí dice: **glifos a 25, luego a 51**, y farmear hasta **Paragón ~100** | Alta — el brief prohibía explícitamente inventar nombres y números |
| 9 | **"Polvo Primordial Refinado" en T7 y "fragmentos de gema" en T10** | No aparecen en la tabla de Maxroll. Marcados como sin confirmar | Baja |
| 10 | **Bonus de oro intermedios de Torment (+120/+140/…/+275)** | Maxroll solo publica los extremos (+100% → +300%). La progresión intermedia es **interpolación del informe**, no dato leído | Baja |
| 11 | **"La guía de Minion Necro integra Mercenarios y Runewords" (implicando que no podéis seguirla)** | La guía los trata como **opcionales**: la build funciona sin ellos y ella misma ofrece alternativas a las Runewords | Media — el informe era innecesariamente pesimista |

---

### 🟢 Contradicciones que he cerrado

- **A (¿T5–XII son de pago?) → RESUELTA a favor de "gratis".** Fextralife se contradice a sí misma y se declara cobertura de la era 2.0.
- **H (¿el Cubo Horadrim es gratis?) → PARCIALMENTE RESUELTA.** El Cubo **es de pago** (confirmado), **pero eso no os bloquea los Míticos** (ver error #4).

### 🟡 Contradicciones que siguen abiertas — y una nueva

- **C (bonus de oro de Hard/Expert/Penitent):** sigue abierta. Maxroll no publica esos valores; solo tengo el +25%/+50%/+75% de Fextralife.
- **D (desbloqueo de Penitente): AHORA ES PEOR.** Encontré una **tercera** postura: Maxroll presenta las cuatro dificultades base **sin requisito alguno**, disponibles desde la creación de personaje. Si eso es cierto, **podríais jugar en Penitente (+175% XP) desde el nivel 1** y la tabla de §4.2 se queda corta. **Es la comprobación más rentable que podéis hacer en vuestro primer minuto de juego.**
- **D-bis (NUEVA):** el nombre de la zona de *Lord of Hatred* baila — el informe dice "Skovos/Temis", Nerdschalk dice **"Sowos"** y menciona un "Echo of Hatred". Irrelevante para vosotros, pero indica que la sección de expansiones no está asentada.
- **E, G, I, J:** sin novedad, siguen como las dejó el informe. **No pude verificar el escalado por tamaño de grupo (G)**, que para un dúo es justamente lo más relevante que queda sin cerrar.

---

### ⚠️ Advertencia de vigencia que el informe no se hizo a sí mismo

El informe se presenta como "parche 3.1.3" en la cabecera, pero **la única nota de parche que llegó a abrir era del 3.1.0**, y ninguna de sus fuentes de Maxroll es posterior al 16 de agosto (defensas) — el resto son de junio y julio. **Casi todo el contenido está verificado para 3.1.0/3.1.x, no específicamente para 3.1.3.** Es muy probable que nada estructural haya cambiado en un parche de punto, pero **la etiqueta "3.1.3" del encabezado promete más precisión de la que el informe realmente tiene.**

### Veredicto

**PARCIAL.** La **tesis central —todo el sistema de dificultades, los 12 Torment y el nivel 70 funcionan con juego base— es correcta y ha salido reforzada** de la verificación. La mayoría de los números duros (Foso, defensas, XP, botín) son exactos y están citados con honestidad. Pero el informe contiene **once errores**, de los cuales **cuatro son graves para vuestro caso concreto**: un consejo defensivo perjudicial (Resistencias sobre Armadura), una conclusión falsa y desmoralizante (Míticos "vedados"), una mejora de XP que en realidad es contenido de pago, y varios números y un nombre de nodo que parecen inventados. Todos quedan corregidos arriba.
