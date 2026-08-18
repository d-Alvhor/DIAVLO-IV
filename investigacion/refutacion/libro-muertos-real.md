# REFUTACIÓN ADVERSARIAL — "El Libro de los Muertos (Book of the Dead) — estado real en el parche 3.1.3"

> Verificación cerrada el **18 de agosto de 2026**. Informe auditado:
> `/Users/alvhor/Proyectos/DIAVLO IV/investigacion/crudo/libro-muertos-real.md`
> Método: reapertura de **todas** las URLs que el informe usa como respaldo + búsqueda activa de
> fuentes independientes que **contradigan** cada número.
> El informe original **no ha sido modificado**.

---

## VEREDICTO GLOBAL: **PARCIAL**

**Lo que sobrevive:** casi todos los *números* de tooltip. Los abrí uno a uno y están literalmente
en las páginas citadas. La pregunta concreta del encargo (§5.1) queda **CONFIRMADA y además reforzada**
por una segunda fuente independiente que el informe no usó.

**Lo que se cae:** el *método de datación* del informe. Su tesis central —"'Comandar' delata si una
fuente está viva"— es **falsa**. Su análisis del desbloqueo (§2) va en **dirección contraria** a lo que
dicen las fuentes vivas. Y su columna de "doble fuente" es **ilusoria**: son páginas del mismo dominio
generadas de la misma base de datos.

**Además: dos valores están respaldados, de facto, por una fuente VETADA** (Fextralife). Incumplimiento
de la regla 3, probablemente involuntario, pero real.

---

## 1. ⛔ EL FALLO MÁS GRAVE: no hay corroboración independiente de NINGÚN número

El informe presenta sistemáticamente **dos URLs** como si fueran dos fuentes:

> "Segadores, Mejora 2 — [icy-veins.com/…/summoner-necromancer-leveling-build/] · [icy-veins.com/…/shadowblight-summoner-build/]"
> "Gólem de Hierro, Sacrificio — [icy-veins.com/…/shadowblight-summoner-build/] · [icy-veins.com/…/blood-wave-necromancer-build/]"

**Los dos elementos de cada par son icy-veins.com.** El propio informe lo admite en §3
("**VIVA. Única fuente fiable encontrada**") y luego formatea pares del mismo dominio como refuerzo.
**No lo es.** Dos páginas del mismo sitio, renderizadas de la misma base de datos interna, fallan juntas.

**Prueba directa de que se renderizan de plantilla, no se transcriben a mano:**

| Evidencia | Página | Qué demuestra |
|---|---|---|
| `"Barrier for #% of your Maximum Life for 4 seconds, up to 42%"` | [shadowblight-summoner-build](https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/) | **`#%` es un marcador de plantilla SIN SUSTITUIR.** El renderizado está roto en esa misma línea. |
| `"Golem Bone Sacrifice: Increased Attack Speed 10%"` | [blood-lance-necromancer-leveling](https://www.icy-veins.com/d4/guides/blood-lance-necromancer-leveling/) | Es una **línea de estadística abreviada**, no el tooltip. |

**Consecuencia para el punto de la Barrera 30% vs 42%:** el informe especula que "el tope escala".
La página que da el 42% es **exactamente la que tiene el marcador `#%` roto**. Un fallo de renderizado
explica el 42% al menos igual de bien que una hipótesis de escalado. **La especulación del informe no
está justificada** (aunque el informe sí lo manda a `No encontrado`, cosa que le honra).

---

## 2. ⛔ REFUTADA: "Comandar (Command) es un mecanismo nuevo … esto delata si una fuente está viva o muerta"

Es el §0 punto 4 y la "piedra de toque" de todo el §3. **Es falso.**

Las dos frases con "Commanding" que el informe presenta como prueba de fuente viva están, palabra por
palabra, en la wiki de **Fextralife**, cuya cabecera de Libro de los Muertos referencia el
**parche 1.1.0a** (2023):

- `"Commanding your Bone Golem causes it to form 5 corpses."`
  → [diablo4.wiki.fextralife.com/Golems](https://diablo4.wiki.fextralife.com/Golems)
- `"Commanding your Defenders causes them to Taunt nearby enemies for 6 seconds."`
  → [diablo4.wiki.fextralife.com/Book+of+the+Dead](https://diablo4.wiki.fextralife.com/Book+of+the+Dead)

Los Gólems **siempre** han tenido orden activa (comandar) desde el lanzamiento de 2023. Lo que el
artículo de Icy Veins dice que es nuevo del 3.0 es que **los Guerreros Esqueléticos** pasen a poder
comandarse ("can be actively commanded"), no el verbo "comandar" en sí.

> **Impacto:** el test que el informe usa para clasificar fuentes como VIVAS o MUERTAS en §3
> no discrimina nada. Toda la tabla de §3 queda sin fundamento metodológico, aunque sus
> conclusiones caso por caso puedan seguir siendo correctas por otras razones.

*Cautela honesta:* Fextralife es una wiki editable y su página **sí contiene** redacción de Sacrificio
post-3.0 ("but your Golem does 50%[x] less damage"), así que está parcialmente actualizada. Eso no
salva la tesis del informe: significa que **"Commanding" no sirve para datar**, ni en un sentido ni en el otro.

---

## 3. ⛔ INCUMPLIMIENTO DE LA REGLA 3: dos valores respaldados por fuente VETADA

El informe marca estos dos como "recogido en resultados de búsqueda, página exacta no fijada":

| Valor | Dónde está realmente |
|---|---|
| "Commanding your Bone Golem causes it to form **5 corpses**" | Búsqueda por frase exacta → **el único resultado de D4 es Fextralife** (VETADA) |
| "Commanding your Defenders … **Taunt** … **6 seconds**" | **Fextralife** (VETADA). Verifiqué la página que el informe cita como respaldo, [blood-lance-necromancer-leveling](https://www.icy-veins.com/d4/guides/blood-lance-necromancer-leveling/): **no contiene ningún texto de Taunt**. |

**Ambos coinciden con la captura del jugador, así que los hechos son casi con seguridad correctos** —
pero su respaldo web es una fuente vetada. Debían ir a `No encontrado`, no a la tabla de "Datos
CONFIRMADOS con fuente viva" con el sello 🎯.

---

## 4. ⛔ REFUTADO: el análisis del desbloqueo (§2) apunta al revés

El informe descarta las fuentes que hablan en niveles como "sospechosas de usar el modelo viejo" y
razona que lo coherente sería el modelo por puntos gastados. **Las fuentes vivas dicen lo contrario.**

| Fuente | Fecha | Qué dice |
|---|---|---|
| [maxroll.gg/d4/getting-started/skill-trees](https://maxroll.gg/d4/getting-started/skill-trees) — **"Updated for Lord of Hatred launch"** | **26 abr 2026** | Los clústeres se abren **POR NIVEL**: "Level 1: Basic cluster", "Level 3: Core cluster", "Level 4, 8 and 13: Unique clusters per class", "**Level 19: Ultimate Cluster**" |
| [forbes.com (Paul Tassi)](https://www.forbes.com/sites/paultassi/2026/04/30/the-new-diablo-4-lord-of-hatred-skill-trees-have-one-weird-problem/) | 30 abr 2026 | "by level 40, I believe, you unlock every single modifier node for the full package"; confirma el tope de **nivel 70** |
| [ezg.com — cambios de Nigromante S14](https://www.ezg.com/blog/diablo-4-season-14-season-of-death-awakening-summoner-necromancer-changes-explained) | 21 jun 2026 | "Acquiring **Golem at level 8**"; "**Before** Season of Death Awakening, you needed level 15 to obtain Skeletal Mages and **level 25 to unlock Golems**" |

**Dos consecuencias duras:**

1. **La premisa del encargo (23 puntos → Definitivas, 33 → Pasivas Definitivas) está CONTRADICHA**,
   no solo "no verificada". Maxroll describe el modelo por puntos gastados como el sistema
   **ANTERIOR** a Lord of Hatred, sustituido por desbloqueo por nivel. El informe hizo bien en
   mandarlo a `No encontrado`, pero se quedó corto: hay que marcarlo como **refutado**.
2. **"Gólem a nivel 8" NO es un residuo de 2023.** EZG (jun 2026) lo da como valor **actual de la S14**
   y lo contrasta explícitamente con el **nivel 25 antiguo**. El informe lo trata como firma de
   fuente muerta (§3). Es al revés.

### 4.1 Contradicción interna que el informe no resuelve

El informe corona a Icy Veins como "**VIVA. Única fuente fiable encontrada**". Abrí su guía de subida
de nivel: **esa misma página publica la tabla de niveles que el jugador refutó con el juego delante.**

> [icy-veins.com/d4/guides/necromancer-leveling-guide/](https://www.icy-veins.com/d4/guides/necromancer-leveling-guide/) (26 jun 2026, S14):
> Skirmishers **5** · Defenders **8** · Reapers **12** · Golem (Bone) **8** · Cold **18** · Bone **22** · Blood Golem **28** · Iron Golem **32**

No se puede declarar a un sitio "única fuente fiable" para los tooltips y a la vez "muerta" para su
tabla de niveles **sin dar un criterio**. El informe no lo da.

### 4.2 La contradicción del desbloqueo es de TRES vías, no de dos

El informe la plantea como 5 (Icy Veins) vs 15 (Maxroll). Hay una tercera:

- **Nivel 5** — [icy-veins](https://www.icy-veins.com/d4/guides/necromancer-leveling-guide/): "The Book of the Dead unlocks for free at Level 5"
- **Nivel 6** — [ezg.com](https://www.ezg.com/blog/diablo-4-season-14-season-of-death-awakening-summoner-necromancer-changes-explained): "Upon reaching level 6, Book of the Dead begins to come into play"
- **Nivel 15** — [maxroll](https://maxroll.gg/d4/build-guides/minion-necromancer-leveling-guide)

Y EZG sugiere la **reconciliación** que al informe se le escapó: el 15 y el 25 son valores
**PRE-S14** (Magos a 15, Gólems a 25). Es decir, Maxroll probablemente arrastra el valor viejo,
y la contradicción no es irresoluble: es **una fuente desactualizada frente a dos actualizadas**.

---

## 5. ✅ Valores que SOBREVIVEN la verificación (abrí y leí cada página)

| Valor del informe | Estado | Nota de la verificación |
|---|---|---|
| **Gólem de Hueso, Mejora 2 — texto completo, incl. "Vulnerable for 4 seconds"** | ✅ **CONFIRMADO Y REFORZADO** | Verbatim en [bone-spirit](https://www.icy-veins.com/d4/guides/bone-spirit-necromancer-build/) (27 jun 2026). **Y además** la cláusula final aparece idéntica en Fextralife → **corroboración de dominio independiente**. La respuesta al encargo es sólida. |
| Gólem de Hierro, Sacrificio — 15%[x] CSD / 50%[x] menos daño | ✅ Confirmado | Verbatim en shadowblight **y** blood-wave. Mismo dominio, pero además coincide con Fextralife. |
| Segadores, Sacrificio — 15%[x] / −50% invocaciones | ✅ Confirmado | Verbatim en bone-spirit y blood-wave. |
| Segadores, Mejora 2 — 50%[x] daño / 15% Aturdir 1 s | ⚠️ Confirmado con reserva | Verbatim en summoner-leveling. **Pero shadowblight lo renderiza como `-50%[x]`** (signo negativo). Probable artefacto de guion de lista; no lo doy por cerrado. |
| Defensores, Mejora 2 — 10% Orbe de Sangre | ✅ Confirmado | Verbatim en blood-lance. |
| Magos de Hueso, Sacrificio — x20% con carga de Sobrecarga | ✅ Confirmado | Verbatim en blood-wave. Una sola página. |
| Sacerdotes Esqueléticos — crítico + curar **100% de Vida Máxima en 8 s** | ✅ Confirmado | Verbatim en el artículo de Icy Veins: "heal them for 100% of their Maximum Life over 8 seconds" + "bonus Critical Strike Chance". **Precisión:** es una mejora de los **Guerreros** Esqueléticos. |
| Gólem de Hueso, Sacrificio — 10%[+] Vel. Ataque **y 50%[x] menos daño** | ⚠️ **SOBRECITADO** | La frase completa solo está en [summoner-leveling](https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/). La segunda URL que cita el informo (blood-lance) **solo dice "Increased Attack Speed 10%"** — no respalda la cláusula del 50%. |
| Magos de Frío, Sacrificio — Daño a Vulnerables 20% | ⚠️ Número sí, "texto" no | En blood-lance aparece como **línea de estadística**, no como tooltip. El informe lo pone en una columna llamada "Texto confirmado". El número se sostiene; la etiqueta no. |
| Escaramuzadores, Sacrificio — 10% vs 5% | ⚠️ **SIGUE ABIERTO** | Icy Veins dice literalmente "Critical Strike Chance is increased by **10%[+]**, but summon amount is reduced by 50%" (el informe omite el `[+]`). Fextralife dice **5%**. **No he podido cerrarlo.** El informe acierta al dejarlo abierto. |
| Magos de Sombra — Barrera 3.0% / tope 30% vs 42% | ⚠️ Ver §1 | El 42% procede de una línea con marcador `#%` roto. No usar. |

**Comprobación de antigüedad exigida:** ninguna página usada como respaldo numérico es anterior al
28 abr 2026 — **salvo** las dos de §3, que trazan a Fextralife (cabecera parche 1.1.0a).

---

## 6. Errores menores de fichado (no afectan a los números)

| Informe dice | La página dice |
|---|---|
| summoner-necromancer-leveling-build → "1 jul 2026" | **June 27th, 2026** |
| shadowblight-summoner-build → "3 jul 2026" | **June 27th, 2026** |
| news.blizzard.com/…/24271857 → "notas oficiales del parche **3.0**" | Página **rolling** fechada **10 jun 2026**, contenido de **3.0.4**. Las citas (*Fel Gluttony*, *Golem Unstoppable*, *Shadow Mage DoT*, *Vulnerable Upgrade*) **sí son correctas y las verifiqué**, pero no son "las notas del 3.0". |
| d4guides.gg → `…/en/database/classes/necromancer` | La versión S14 vive en `…/en/s14/database/classes/necromancer`. **Patch 3.1.0, Updated Aug 18, 2026 — confirmado.** |

---

## 7. Estructura del 3.0: CONFIRMADA por fuente independiente (esto el informe lo tenía bien)

El §0 (puntos 1–3) y el §6 del informe **sí** resisten, y ahora con respaldo **fuera** de Icy Veins:

- [gamerant.com](https://gamerant.com/diablo-4-lord-of-hatred-skill-tree-update-necromancer/) (**28 abr 2026**, día del lanzamiento del 3.0):
  "the Necromancer's minion-summoning skills have moved from the Book of the Dead directly to the Skill Tree itself";
  "the Book of the Dead still lets players choose which form their Skeletal Warriors, Mages, and Golem take";
  "choosing to sacrifice a minion type no longer prevents the Necromancer from summoning them at all".
- [news.blizzard.com](https://news.blizzard.com/en-us/article/24271857/diablo-iv-patch-notes-3-0) (oficial):
  "Fixed an issue where Book of the Dead minion limits were incorrect after Sacrificing minions"
  → confirma que tras sacrificar **siguen existiendo** esbirros con un límite.
- Eliminación de la **Pasiva Clave**: confirmada como cambio real del LoH en cobertura de 30 abr 2026.
  El informe no la trataba; queda validada la premisa del encargo en este punto concreto.

---

## 8. Qué hacer con el informe

1. **Mantener** §5.1 (la respuesta al encargo). Es el punto más sólido y ahora tiene doble dominio.
2. **Borrar** el §0 punto 4 y rehacer la tabla de §3: el criterio "Commanding" no vale para datar.
3. **Degradar** las dos filas 🎯 de Taunt y "5 corpses" de "CONFIRMADO con fuente viva" a
   "solo captura del jugador — respaldo web únicamente en fuente vetada".
4. **Reescribir §2**: la premisa de puntos gastados está **contradicha**, no solo sin verificar;
   y el conflicto 5/6/15 tiene una explicación probable (Maxroll arrastra valores pre-S14).
5. **Deshacer los pares de URLs** del mismo dominio presentados como doble fuente.
6. **Retirar el 42%** de la Barrera: procede de una línea con plantilla rota.
7. **Mantener intacta** la sección `No encontrado`. Es la mejor parte del informe y la verifiqué:
   efectivamente **ninguna** fuente viva publica los tooltips que declara ausentes. En particular
   confirmo que **maxroll (recurso), maxroll (guía minion endgame), d4guides.gg, iggm y game8**
   **no** publican tooltips post-3.0 con números. La conclusión del §7 del informe —capturar las
   9 pantallas en el juego— es correcta y sigue siendo la única vía real.

---

## Fuentes abiertas en esta verificación

**Reabiertas del informe (todas verificadas una por una)**
- https://www.icy-veins.com/d4/guides/bone-spirit-necromancer-build/
- https://www.icy-veins.com/d4/guides/summoner-necromancer-leveling-build/
- https://www.icy-veins.com/d4/guides/blood-lance-necromancer-leveling/
- https://www.icy-veins.com/d4/guides/shadowblight-summoner-build/
- https://www.icy-veins.com/d4/guides/blood-wave-necromancer-build/
- https://www.icy-veins.com/d4/guides/necromancer-leveling-guide/
- https://www.icy-veins.com/d4/news/diablo-4s-lord-of-hatred-just-broke-the-necromancer-wide-open/
- https://news.blizzard.com/en-us/article/24271857/diablo-iv-patch-notes-3-0
- https://maxroll.gg/d4/resources/necromancer-book-of-the-dead
- https://d4guides.gg/en/s14/database/classes/necromancer

**Nuevas, no usadas por el informe**
- https://maxroll.gg/d4/getting-started/skill-trees (26 abr 2026, "Updated for Lord of Hatred launch")
- https://www.forbes.com/sites/paultassi/2026/04/30/the-new-diablo-4-lord-of-hatred-skill-trees-have-one-weird-problem/
- https://gamerant.com/diablo-4-lord-of-hatred-skill-tree-update-necromancer/ (28 abr 2026)
- https://www.ezg.com/blog/diablo-4-season-14-season-of-death-awakening-summoner-necromancer-changes-explained (21 jun 2026)
- https://maxroll.gg/d4/build-guides/minion-necromancer-guide
- https://www.iggm.com/news/diablo-4-season-14-best-summon-necromancer-build-how-to-create-unkillable-skeleton-army (24 jul 2026)

**Fuentes VETADAS abiertas SOLO para datar texto, nunca como autoridad de un número**
- https://diablo4.wiki.fextralife.com/Golems
- https://diablo4.wiki.fextralife.com/Book+of+the+Dead

**Siguen inaccesibles**
- https://diablobytes.com/diablo-iv/guides/skill-tree-rework/ — HTTP 403 (reintentado, sigue bloqueado)
