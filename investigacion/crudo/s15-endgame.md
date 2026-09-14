# Endgame y clasificaciones en 3.2.1 (Temporada 15 — Hell's Legacy)

> **Ancla temporal:** redactado el 15 de septiembre de 2026, **antes** de que la Temporada 15 esté
> viva. El parche 3.2.1 y sus notas ya están publicados (12 sep 2026), pero **no existe ni una sola
> partida jugada de S15**: no hay clasificaciones pobladas, no hay tiempos reales, no hay builds
> probadas. Todo lo que circule hoy como "la mejor build de S15" es teoría de PTR.
> Parche anterior vivo: 3.1.4 (9 sep 2026). 3.2.0 nunca salió a producción: fue solo PTR
> (4–11 ago 2026) y su contenido se publica como **3.2.1**.

## Resumen

1. **La Falla no cambia de dificultad.** 3.2.1 no toca ni un número de escalado ni el tope: sigue en tier 150. Lo único que sube es la experiencia (tier 150: de 1800% a 2700% de bonus) y cuatro correcciones.
2. **Las clasificaciones no son de la Falla, son de la Torre del Artificiero** (10 minutos, jefe obligatorio). Y 3.2.1 **no contiene ni una línea** sobre Torre ni Leaderboards: S15 hereda el sistema de S14 tal cual.
3. **Se resetean cada semana**, con rondas que arrancan en jueves; títulos y halos duran toda la temporada y caen al empezar la siguiente. El modelo oficial de "rondas de dos semanas" es de la beta de S11 y está muerto.
4. **Hordas Infernales y Mazmorras de Pesadilla apenas se tocan** (una corrección cada una); el cambio real está en los **jefes de guarida**: los Míticos ahora salen del pool de cada jefe, y los Initiate igualan la tasa de los Greater.
5. **Nivel máximo 70, Paragón máximo 300, hasta 342 puntos de Paragón** (300 por niveles + hasta 42 del Rango de Temporada). Ninguno de los tres cambia en 3.2.1.

---

## Hallazgos

### La Falla (The Pit)

**F1 — Nivel máximo de Falla: 150.**
Las notas oficiales de 3.2.1 usan "Pit Tier 150" como el tramo más alto al describir la subida de XP,
y las dos guías preferentes lo repiten ("150 total difficulty levels" / "150 levels of difficulty").
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (publicado 12 sep 2026)
- https://maxroll.gg/d4/resources/pit-guide (actualizado 16 jul 2026, S14)
- https://www.icy-veins.com/d4/guides/the-pit-of-the-artificers-guide/ (titulada "Season 15", sin fecha visible)
- Evidencia: **corroborado**

**F2 — 3.2.1 NO cambia la dificultad, los tiers ni el escalado de la Falla.**
La sección "The Pit" de las notas oficiales contiene exactamente 6 líneas: 2 de experiencia y 4 de
corrección de bugs. Nada de balance de enemigos, nada de tiers nuevos.
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)
- Evidencia: **oficial** (por ausencia: el bloque completo está leído, no es un resumen)

**F3 — Bonus de experiencia de tiers altos subido: Falla 150 pasa de 1800% a 2700%.**
Texto literal: *"Increased Bonus Experience from higher Pit Tiers. Example: Pit Tier 150 increased
from 1800% to 2700%."*
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)
- Evidencia: **oficial**

**F4 — Los Orbes de Progreso dan el doble de XP con el nodo "Choron's Soul" activo.**
Es un nodo del árbol de War Plans de la Falla, no un cambio global.
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)
- Evidencia: **oficial**

**F5 — Cuatro correcciones en la Falla (3.2.1).**
Barrera Protectora que podía no aparecer tras matar al Guardián de la Falla; Guardianes que aparecían
mal cuando alguien del grupo cambiaba de piso; recompensas de mejora de glifo que **no se reducían al
fallar los objetivos de "Survival Mastery"**; y el mensaje de fin de run que citaba un objetivo de
maestría equivocado.
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)
- Evidencia: **oficial**

**F6 — ESCALADO POR NIVEL DE FALLA (el dato pedido).** Factores **multiplicativos por tier**, acumulados
sobre el tier anterior:

| Nivel de Falla | Daño que hace el enemigo, por tier | Vida del enemigo, por tier |
|---|---|---|
| 2 | +15% | +50% |
| 3 | +13% | +33% |
| 4–10 | +17,4% | +26,5% |
| 11–110 | +4,74% | +17% |
| 111+ | +2,37% | +32% |

Cita de la fuente sobre el marco: *"These values quickly ramp up due to each tier being multiplicative
to the last."* Y sobre su origen: *"this has been figured out"* — es decir, **derivado por la comunidad,
no publicado por Blizzard**.
- https://maxroll.gg/d4/resources/difficulty-overview (actualizado **26 jun 2026**, S14 — fuera del parche vivo)
- Evidencia: **unica** (una sola fuente preferente, no oficial, fecha anterior al parche). Ver contradicción C5.

**F7 — Multiplicadores de vida acumulados por dificultad, y daño extra que hace falta para subir de Tormento.**
Misma página, misma sección. "Incremento de vida" es acumulado respecto a Normal.

| Dificultad (Falla equivalente) | Vida aumentada | Daño extra necesario |
|---|---|---|
| Normal (Falla 1) | 0% | — |
| Difícil (Falla 3) | 100% | 100% |
| Experto (Falla 5) | 220% | 60% |
| Penitente (Falla 7) | 412% | 60% |
| Tormento 1 (Falla 10) | 719,20% | 60% |
| Tormento 2 (Falla 15) | 1.696,05% | 119% |
| Tormento 3 (Falla 20) | 3.837,75% | 119% |
| Tormento 4 (Falla 25) | 8.533,32% | 119% |
| Tormento 5 (Falla 30) | 18.828,11% | 119% |
| Tormento 6 (Falla 40) | 90.884,16% | 381% |
| Tormento 7 (Falla 50) | 437.245,26% | 381% |
| Tormento 8 (Falla 60) | 2.102.143,55% | 381% |
| Tormento 9 (Falla 70) | 10.105.024,22% | 381% |
| Tormento 10 (Falla 80) | 48.573.496,88% | 381% |
| Tormento 11 (Falla 90) | 233.484.850% | 381% |
| Tormento 12 (Falla 100) | 1.122.322.000% | 381% |

- https://maxroll.gg/d4/resources/difficulty-overview (26 jun 2026)
- Evidencia: **unica**

**F8 — VERIFICACIÓN DEL MARCO: las dos tablas de esa misma página no cuadran entre sí.**
Comprobación mía rehaciendo los acumulados de F7 con los factores de F6:
- Hasta Falla 7 cuadra al céntimo: 1,5 × 1,33 = ×2,0 (+100% en Falla 3) ✔; × 1,265² = ×3,19 (+220% en Falla 5) ✔; × 1,265² = ×5,11 (+412% en Falla 7) ✔.
- **En Falla 10 deja de cuadrar.** Con +26,5%/tier saldría 5,12 × 1,265³ = ×10,36 (+936%). La tabla dice **719,20% (×8,19)**, que es exactamente 5,12 × **1,17³** = ×8,19.
- De Falla 10 en adelante todo vuelve a cuadrar con +17%/tier: Falla 15 = 8,19 × 1,17⁵ = ×17,96 (+1696%) ✔; Falla 100 = ×11.223.220 (+1.122.322.000%) ✔.

**Conclusión:** el tramo declarado como "4–10 → +26,5% de vida" es en realidad **4–7**; desde el tier 8
ya se aplica el +17%. La cifra del titular (+26,5%) es la que está mal encuadrada, no los acumulados.
Además, la columna "daño extra necesario" **se deriva solo de la vida**, no del daño que hace el enemigo:
son dos ejes distintos y conviene no mezclarlos.
- Evidencia: **disputa** (inconsistencia interna de la propia fuente, detectada recalculando)

**F9 — Mapa Tormento ↔ Falla.** Hay 12 Tormentos: T1=Falla 10, T2=15, T3=20, T4=25, T5=30, T6=40,
T7=50, T8=60, T9=70, T10=80, T11=90, T12=100. Para desbloquear Tormento hay que llegar a nivel 70 y
progresar por la Falla.
- https://maxroll.gg/d4/resources/difficulty-overview (26 jun 2026)
- Evidencia: **unica**

**F10 — Estructura de un run de Falla.** Cinco pisos finitos conectados por portales, disposición y
monstruos aleatorios. Hay que llenar la barra matando enemigos (los élites dan mucha más progresión) y
luego matar al Guardián de la Falla antes de que se acabe el tiempo. Completar a tiempo desbloquea el
tier o tiers siguientes según el tiempo que sobre. **El jefe sale de la misma lista que usa la Torre.**
- https://maxroll.gg/d4/resources/pit-guide (16 jul 2026)
- Evidencia: **unica**. El temporizador está en disputa (ver C1).

**F11 — Intentos de mejora de glifo por run: hasta 9.**
4 de base + 1 si no mueres + hasta 4 de los nodos del árbol de War Plans de la Falla. La página de War
Plans lo confirma de forma independiente: *"Gain 4 extra Glyph upgrade chances in the Pit (for a total
of 9 chances per run)."*
- https://maxroll.gg/d4/resources/pit-guide (16 jul 2026)
- https://maxroll.gg/d4/resources/war-plans (actualizado 5 ago 2026)
- Evidencia: **corroborado** (dos páginas preferentes coinciden). Contradice a Icy Veins, ver C2.

**F12 — Probabilidad de mejora de glifo según diferencia (Falla − Glifo).**

| Diferencia | Resultado |
|---|---|
| 80 o más | 100%, +5 niveles |
| 60–79 | 100%, +4 |
| 40–59 | 100%, +3 |
| 20–39 | 100%, +2 |
| 10–19 | 100% |
| 8–9 | 90% |
| 6–7 | 80% |
| 0–5 | 70% |
| más de 50 por debajo | imposible mejorar |

- https://maxroll.gg/d4/resources/pit-guide (16 jul 2026)
- Evidencia: **unica**. Los tramos negativos intermedios quedan como hueco (ver Huecos).

**F13 — Glifos: tope 150. A nivel 50 pasan de Raro a Legendario por 15.000 fragmentos de gema**, ganando
radio (máximo 5) y un multiplicador legendario nuevo, que va de 5,5%[x] a nivel 51 hasta 15,4%[x] a nivel 150.
- https://maxroll.gg/d4/resources/pit-guide (16 jul 2026)
- https://maxroll.gg/d4/resources/paragon-boards (actualizado 9 jul 2026)
- Evidencia: **corroborado**

**F14 — Desbloqueo de la Falla.** En realm estacional, completando la mazmorra Capstone "Hellish Descent"
del Rango de Temporada II. En Eterno, a nivel 70. Se entra por el obelisco de Cerrigar o Temis.
- https://maxroll.gg/d4/resources/pit-guide (16 jul 2026)
- Evidencia: **unica**. Icy Veins dice otra cosa, ver C3.

### Clasificaciones / Leaderboards

**F15 — Las clasificaciones no son de la Falla: son de la Torre del Artificiero.**
La Falla baja (farmeo de glifos, sin ranking); la Torre sube y es el modo competitivo. Cita:
*"While the Pit descends you to the greatest depths to galvanize your strength, the Artificer's Tower
rises in challenge to match you against others on the Leaderboards."*
- https://maxroll.gg/d4/resources/tower-guide (actualizado 29 jul 2026)
- https://www.icy-veins.com/d4/guides/tower-leaderboards/ (titulada "Season 15", sin fecha visible)
- Evidencia: **corroborado**

**F16 — 3.2.1 no toca la Torre ni las clasificaciones: cero menciones.**
Revisado el cuerpo completo de las notas oficiales: la palabra "Tower" y la palabra "Leaderboard" no
aparecen ni una vez. S15 hereda el sistema de S14 sin cambios anunciados.
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)
- Evidencia: **oficial** (por ausencia verificada, no por resumen)

**F17 — Cómo funciona la Torre.** 10 minutos desde que sales del círculo inicial. Pisos aleatorios con
familias de monstruos distintas. Llenas la barra de progreso matando (el valor de cada monstruo escala
con la experiencia que daría) y recogiendo Orbes, que caen de élites, campeones y duendes del tesoro.
Al llenarla aparece un jefe aleatorio y hay que matarlo dentro del tiempo. Cuatro Pilones por run: los
tres primeros en orden aleatorio garantizando uno de cada tipo, el cuarto repite uno. Tipos:
**Canalización** (habilidades sin coste de recurso y enfriamientos muy reducidos), **Poder** (daño muy
aumentado) y **Velocidad** (Imparable, sin trabas y mucha velocidad de movimiento).
- https://maxroll.gg/d4/resources/tower-guide (29 jul 2026)
- https://www.icy-veins.com/d4/guides/tower-leaderboards/ (S15)
- Evidencia: **corroborado**

**F18 — Solo entras en la clasificación si matas al jefe y terminas dentro de los 10 minutos.**
El puesto se ordena por el tier más alto completado y, a igualdad, por el tiempo de clear.
- https://www.icy-veins.com/d4/guides/tower-leaderboards/ (S15)
- https://maxroll.gg/d4/resources/tower-guide (29 jul 2026)
- Evidencia: **corroborado**

**F19 — Categorías: 8 clasificaciones en solitario + 3 de grupo.**
Bárbaro, Druida, Nigromante, Pícaro, Hechicero, Espiritista, **Paladín** y **Brujo**, más grupo de 2, 3 y 4.
Filtros: plataforma (todas / solo PC), Normal / Hardcore, amigos y clan. Cada fila muestra puesto,
nombre, tier completado, tiempo y fecha. Se consultan en el Obelisco del Artificiero de Cerrigar o en
el menú de Colecciones.
- https://maxroll.gg/d4/resources/tower-guide (29 jul 2026) — es la lista de 8
- Evidencia: **unica** para la lista completa. Icy Veins lista solo 6, ver C8.

**F20 — RESETEO: semanal, y las rondas empiezan en JUEVES.**
Dos piezas que encajan: Maxroll dice *"These start on Thursdays, leaving time after a new season and
patch are launched for players to prepare to compete"*; y el post azul recogido por Icy Veins al salir
de beta dice *"Weekly rewards are granted to you the next time you log in after the previous weekly
reset has ended."* Cada semana se premia según el mejor rango logrado: haber jugado la Torre esa
semana, haber llegado a tier 100 o más, y top 1.000 / 500 / 100 / 10 / 1. El premio es un halo
cosmético, un título de prestigio y un alijo de equipo; a más rango, más objetos y más probabilidad de Únicos.
- https://maxroll.gg/d4/resources/tower-guide (29 jul 2026)
- https://www.icy-veins.com/d4/news/earn-new-rewards-for-participating-in-the-diablo-4-tower-leaderboards-in-season-14/ (S14)
- Evidencia: **corroborado**. Contradice al anuncio oficial de la beta, ver C6.

**F21 — Títulos y halos: duran toda la temporada, se resetean al empezar la siguiente.**
Top 1.000 recibe título: puesto 1 "Grandmaster of the Tower"; 2–10 "Champion of the Tower"; 11–100
"Elite of the Tower"; 101–500 "Knight of the Tower"; 501–1.000 "Veteran of the Tower". El puesto 1
recibe además un halo único. Al arrancar la temporada siguiente te dan un Emblema con el mejor rango
semanal que lograste en la anterior, al primer inicio de sesión.
- https://maxroll.gg/d4/resources/tower-guide (29 jul 2026)
- https://www.icy-veins.com/d4/news/earn-new-rewards-for-participating-in-the-diablo-4-tower-leaderboards-in-season-14/ (S14)
- Evidencia: **corroborado**

**F22 — Desbloqueo de la Torre y de sus tiers.** Se abre completando la mazmorra Capstone del Rango de
Temporada 2, y se entra por el mismo obelisco de Cerrigar que la Falla. Los tiers que ya tengas
desbloqueados en la Falla están disponibles en la Torre, **y la Torre también desbloquea tiers por su
cuenta**, así que puedes empujar Torre más alto que Falla.
- https://www.icy-veins.com/d4/guides/tower-leaderboards/ (S15)
- https://maxroll.gg/d4/resources/tower-guide (29 jul 2026)
- Evidencia: **corroborado**

**F23 — Si desactivas el juego multiplataforma, solo ves el ranking de tu plataforma.**
- https://www.icy-veins.com/d4/guides/tower-leaderboards/ (S15)
- Evidencia: **unica**

**F24 — Dos jefes están excluidos de la Torre por comportamiento inconsistente:** el Espectro Vampírico
(Vampire Wraith) y el Chamán Caído "Sower of Decay".
- https://www.icy-veins.com/d4/guides/tower-leaderboards/ (S15)
- Evidencia: **unica**

### Hordas Infernales

**F25 — Único cambio directo en 3.2.1: una corrección.**
*"Fixed an issue where Infernal Hordes could fail to grant Grim Favor."* Cero cambios de balance,
cero cambios de recompensa dentro de la actividad.
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)
- Evidencia: **oficial**

**F26 — Cambios indirectos que sí importan (3.2.1).**
Fabricar un Compás de Horda Infernal en el Ocultista baja de **666 a 500 Polvo de Sigilo**. Desguazar
un Compás sube de **25 a 100 Polvo de Sigilo**. Y se corrige que las emboscadas de Belial de
"Infernal Deception" no soltaran botín dentro de Hordas.
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)
- Evidencia: **oficial**

**F27 — Sistema vigente.** Compases de 6, 8 o 10 oleadas (los "Fleeting", pre-Tormento, solo 4).
Oleadas de 60 segundos. La moneda del run es el Éter Ardiente, que se pierde si no se gasta y se gana
y gasta de forma independiente por jugador en grupo. Al final se pelea contra 3 miembros del Consejo
Infame o, pagando **666 Éter**, contra Bartuc, Señor del Caos. Botines: Despojos de Material, de Oro,
**Despojos de Equipo Superior por 400 Éter** (garantiza al menos 1 Legendario Ancestral) y
**Tesoro de Equipo Superior por 1.000 Éter**, que solo aparece si has cogido el nodo "Infernal Hoard"
en tu War Plan.
- https://maxroll.gg/d4/resources/infernal-hordes (actualizado 16 jul 2026, S14)
- Evidencia: **unica** (y con un error ya detectado, ver C9)

**F28 — Esta temporada, la Esquirla del Terror de Diablo modifica Zona Infernal y Hordas Infernales.**
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)
- Evidencia: **oficial**

### Mazmorras de Pesadilla

**F29 — CAMBIO DE MARCO: las Mazmorras de Pesadilla ya no tienen niveles propios del 1 al 100.**
Escalan con la dificultad en la que juegas: *"Monsters, including bosses, scale based on the difficulty
you are playing on"*, y cada nivel de Tormento añade además penalizaciones a tu reducción de daño por
armadura y a tus resistencias. Cualquier guía que hable de "sigilo de nivel 100" está describiendo un
sistema muerto.
- https://maxroll.gg/d4/resources/nightmare-dungeons (actualizado 16 jul 2026, S14)
- Evidencia: **unica**

**F30 — Sigilos.** Se consiguen de Susurros, de las propias mazmorras, de eventos, de jefes del mundo en
Tormento, y se fabrican en el Ocultista por oro + **60 Polvo de Sigilo**. No se pueden rerollear: para
optimizar hay que fabricar nuevos desguazando los malos. En 3.2.1, desguazar un Sigilo de Pesadilla
**baja de 25 a 20** Polvo de Sigilo, y desguazar un Sigilo de Escalada **sube de 25 a 100**.
- https://maxroll.gg/d4/resources/nightmare-dungeons (16 jul 2026) — el coste de 60
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026) — los cambios de desguace
- Evidencia: **oficial** para los cambios, **unica** para el coste de fabricación

**F31 — Pesadillas Escaladas.** Se abren con un Sigilo de Escalada, que cae de las Cámaras Fuertes
Horádricas ya desde Tormento 1. Son **3 mazmorras encadenadas**: la primera con 1 afijo positivo y 1
negativo, y cada salto añade un par más, hasta 3 y 3 en la tercera. Al final espera **Astaroth**, con
esos mismos 3 positivos y 3 negativos (los positivos se sustituyen por otros de un pool propio), y su
sabueso, la Amalgama de Rabia. Requiere Tormento 1 o superior.
- https://maxroll.gg/d4/resources/nightmare-dungeons (16 jul 2026)
- https://maxroll.gg/d4/resources/bosses-overview (actualizado 16 jul 2026)
- Evidencia: **corroborado**

**F32 — Cámaras Fuertes Horádricas.** Eliges Pruebas en la Antecámara y luego tienes **100 segundos**
para acumular Sintonía. Hay **6 niveles de Sintonía**; llegar al 6 en Tormento alto da mucha Obducita,
fragmentos de gema, materiales, equipo legendario y buena probabilidad de Sigilos de Escalada. Es la
fuente principal de Obducita y la razón principal para farmearlas.
- https://maxroll.gg/d4/resources/nightmare-dungeons (16 jul 2026)
- Evidencia: **unica**

**F33 — Correcciones 3.2.1 relacionadas.** "Dungeon Delve" podía salir como afijo en Sigilos de Escalada
(corregido) y el modificador "Gauntlet Nightmare Dungeon" de War Plans no funcionaba en multijugador
(corregido).
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)
- Evidencia: **oficial**

**F34 — Esta temporada, la Esquirla del Odio de Mefisto modifica La Falla y las Mazmorras de Pesadilla.**
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)
- Evidencia: **oficial**

### Jefes de guarida e invocación

**F35 — Lo que cambia en 3.2.1 (todo oficial, misma URL, 12 sep 2026).**
- Los Míticos que sueltan los Jefes de Guarida Iniciáticos y Mayores, y los que se eligen en el Alijo de Belial, **solo saldrán del pool de Únicos de ese jefe**. Ojo al matiz que la propia nota añade: siguen soltando botín genérico aparte, así que queda una probabilidad pequeña de sacar Míticos fuera de ese pool.
- **Sube ligeramente** la tasa de Míticos de los Jefes de Guarida **Mayores**.
- **Sube** la tasa de Míticos de los **Iniciáticos hasta igualar la de los Mayores**.
- **Eco de Mefisto**: sube la calidad general del botín e incluye **un Mítico garantizado**.
- Corregido que solo un jugador recibiera crédito al matar a Belial en grupo, y que matarlo pudiera bloquear misiones si se abría el alijo muy rápido.
- Corregido que las **Guaridas Nemesis Definitivas** se pudieran resetear y farmear en bucle.
- Corregido que los jefes de **Marea Nemesis** soltaran materiales de jefe obsoletos.
- Evidencia: **oficial**

**F36 — Escalera de jefes vigente.**
*Iniciáticos* (1 Llave de Guarida, sueltan Llave de Guarida Mayor): Urivar, Grigoire, Bestia en el
Hielo, Eco de Varshan y Lord Zir.
*Mayores* (1 Llave de Guarida Mayor, comparten tabla de botín): Duriel, Heraldo del Odio, Eco de
Andariel y El Carnicero.
*Superiores* (1 Llave de Guarida Superior): **Belial, Señor de las Mentiras** y el **Segador Corrupto**.
Belial no tiene tabla propia: **tú eliges de qué jefe de la escalera cae el botín** al abrir su alijo, y
además garantiza un Único Ancestral y tiene alta probabilidad de soltar Compases de Horda Infernal.
El Segador Corrupto da los Fragmentos de Pandemónium para subir Únicos a Mítico.
La Llave Superior se consigue de la emboscada de Belial, que aparece con cierta probabilidad tras matar
a cualquier jefe de guarida.
*Pináculo*: Eco de Lilith (Ruina de la Iglesia, Nevesk) y Mefisto (Eco del Falso Profeta, Skovos).
- https://maxroll.gg/d4/resources/bosses-overview (16 jul 2026)
- Evidencia: **unica**

**F37 — Esta temporada, la Esquirla de la Destrucción de Baal modifica La Ciudad Subterránea y los Jefes de Guarida.**
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)
- Evidencia: **oficial**

### Nivel máximo y Paragón

**F38 — Nivel máximo de personaje: 70.**
Tres páginas preferentes lo dan por sentado desde ángulos distintos: *"Players must reach level 70 and
progress through the Pit to unlock the new Torment Difficulties"*; *"Leveling from Paragon 1 to 300
after reaching level 70"*; y la Falla se desbloquea en Eterno a nivel 70.
- https://maxroll.gg/d4/resources/difficulty-overview (26 jun 2026)
- https://maxroll.gg/d4/resources/paragon-boards (9 jul 2026)
- https://maxroll.gg/d4/resources/pit-guide (16 jul 2026)
- Evidencia: **corroborado**, pero **Blizzard no lo reafirma en 3.2.1**: el blog oficial de S15 no menciona el tope de nivel ni una vez.

**F39 — Paragón máximo: nivel 300. Puntos de Paragón totales: hasta 342.**
El desglose: 300 puntos por subir de Paragón 1 a 300, más **hasta 42 del Rango de Temporada**. Ese
"hasta 42" es dato **oficial** (aparece en la lista de recompensas de los Rangos de Temporada de S15);
el 300 viene de Maxroll.
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026) — *"Up to 42 Paragon points"*
- https://maxroll.gg/d4/resources/paragon-boards (9 jul 2026) — el 300 y el total de 342
- Evidencia: **corroborado** (oficial + preferente, encajan exactamente: 300 + 42 = 342)

**F40 — 3.2.1 no sube ni el nivel máximo ni el tope de Paragón.** No hay una sola línea al respecto en
las notas.
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)
- Evidencia: **oficial** (por ausencia verificada)

**F41 — Rango de Temporada de S15: 9 rangos y 125 objetivos.** Reparte hasta 14 Puntos de Habilidad,
hasta 42 puntos de Paragón, hasta 10 Chispas Resplandecientes (más las de los Cachés Míticos), 5 Cachés
de Único Mítico, 2 Emblemas, 2 Títulos, 4 Laureles, Llaves de Guarida y materiales.
**Aproximadamente el 15% de los objetivos requieren la expansión Lord of Hatred**, incluidos los
necesarios para completar el Rango VIII y llevarse todas las recompensas.
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)
- Evidencia: **oficial**

**F42 — Tableros de Paragón: 9 por clase, máximo 5 equipados** (el inicial más 4 adicionales).
- https://maxroll.gg/d4/resources/paragon-boards (9 jul 2026)
- Evidencia: **unica**

### Experiencia de endgame (contexto que cambia el ritmo de S15)

**F43 — Bonus de XP por Tormento subido (3.2.1):** Tormento X de 1200% a **1300%**, Tormento XI de
1300% a **1500%**, Tormento XII de 1400% a **1700%**.
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)
- Evidencia: **oficial**

**F44 — Susurros (3.2.1):** los Cachés de Experiencia pasan de 3–5 a **4–6 orbes**, con **2–4 orbes
adicionales en Tormento X o superior**. Los Cachés de Oro suben unas **3 veces**: en Tormento XII, de
unos 35 millones a unos **100 millones de oro**. Los Cachés de Gemas dan ahora 1 gema Real o Grandiosa
en lugar de una Impecable. Los Cachés de Llaves dan el doble de Tributos aleatorios y 5 veces más Polvo
de Sigilo, con probabilidad pequeña de Llave de Mefisto o Rastro de Ecos.
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)
- Evidencia: **oficial**

**F45 — War Plans (3.2.1):** la XP de los War Plans sube y **escala fuerte con el Tormento**. Los orbes
base por completar cualquier nodo en Tormento X o superior pasan de **2 a 4**, y los nodos de
recompensa de experiencia Mágicos, Raros, Legendarios y Míticos **duplican** sus orbes.
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)
- Evidencia: **oficial**

**F46 — Monstruos (3.2.1):** los élites en Tormento X o superior sueltan muchos más Fragmentos de Gema
y tienen mucha más probabilidad de soltar una Gema Real aleatoria. Y se corrige que los monstruos con
Vínculo Vital dieran experiencia de uno solo.
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)
- Evidencia: **oficial**

### War Plans (el esqueleto del endgame actual)

**F47 — Qué son.** Una playlist de hasta **5 actividades** elegidas entre Árbol de los Susurros,
Mazmorras de Pesadilla, Zonas Infernales, La Ciudad Subterránea, Jefes de Guarida, Hordas Infernales y
La Falla. Cada actividad da experiencia hacia **su propio árbol de habilidades**, que modifica cómo se
juega esa actividad. **La Torre no está en la lista.** Requisitos: el árbol de Jefes de Guarida exige
Tormento 1 o superior, los nodos de Jefe de Guarida Mayor exigen Tormento 6 o superior, y el árbol de
la Falla exige Rango de Temporada 2.
- https://maxroll.gg/d4/resources/war-plans (5 ago 2026)
- Evidencia: **unica**

**F48 — NOVEDAD de S15: los puntos de reputación de War Plans se comparten entre personajes** de la
misma partición de la cuenta (cada uno mantiene su propio reparto de puntos, como pasa con habilidades
o Paragón). El progreso de War Plans de los personajes de S14 se transfiere a Eterno al cambiar la
temporada el 15 de septiembre. En **Hardcore solo transfieren los personajes vivos**: si el tuyo murió,
necesitas otro Hardcore vivo en la misma partición —aunque sea uno de nivel 1 de almacenamiento— para
que los puntos lleguen a Eterno.
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)
- Evidencia: **oficial**

---

## Huecos

- **No hay datos de juego real de S15.** Al cerrar este informe la temporada no ha arrancado: no hay clasificaciones con gente dentro, ni tiempos de clear, ni tier máximo alcanzado por nadie. Lo que hay son notas de parche y teoría de PTR.
- **Fecha de apertura de la clasificación de la Torre en S15: no publicada.** La regla conocida es "empiezan en jueves", lo que apuntaría al jueves 17 de septiembre de 2026, pero eso es **inferencia mía, no un dato leído**. Ninguna fuente preferente da la fecha.
- **Blizzard no publica el escalado de la Falla.** El único desglose numérico (F6) es derivado por la comunidad, con fecha de 26 de junio de 2026 —fuera del parche vivo— y con una inconsistencia interna (C5). No he encontrado ninguna fuente oficial que dé porcentajes de vida o daño por tier.
- **El tramo 111–150 (+32% de vida por tier) no se puede cruzar contra nada.** La tabla de acumulados de la misma página se corta en Falla 100, así que ese tramo no tiene verificación cruzada de ningún tipo.
- **Qué son exactamente las "Masteries" de la Falla.** Las notas de 3.2.1 nombran "Survival Mastery" y hablan de un "objetivo de maestría" en el mensaje de fin de run. Ni la guía de la Falla de Maxroll ni la de Icy Veins documentan ese sistema: la palabra "mastery" no aparece en la de Maxroll. No sé cuántas maestrías hay, cuáles son, ni cuánto reducen exactamente las recompensas de glifo al fallarlas.
- **Escalado numérico de la Torre por tier.** Las dos fuentes dicen "funciona por tiers igual que la Falla", pero nadie publica los factores. Si son los mismos que los de la Falla, no está escrito en ninguna parte que haya visto.
- **Tramos negativos de la tabla de probabilidad de glifo.** La tabla de Maxroll lista porcentajes de 55%, 45%, 35%, 25% y 16% para diferencias negativas, pero la asociación entre cada porcentaje y su rango exacto no se pudo extraer con seguridad. Solo doy por bueno el extremo: por debajo de −50 no se puede mejorar.
- **Escalado numérico entre las 3 mazmorras de una Pesadilla Escalada.** La guía dice "más vida y más daño" sin una sola cifra.
- **Fecha de fin de la Temporada 15.** No aparece en ninguna de las fuentes consultadas.
- **Recompensas por tier de la Falla (obducita, materiales, cantidad concreta por nivel).** Se describen en prosa, sin tabla numérica actualizada al parche vivo.
- **El tope de Paragón 300 no está confirmado por ninguna página fechada dentro del parche vivo.** La única fuente es Maxroll con fecha de 9 de julio de 2026, y Blizzard no lo menciona en las notas de 3.2.1. El "hasta 42" del Rango de Temporada sí es oficial, pero solo encaja con 342 si el 300 es correcto.
- **Cuántos tiers desbloquea completar la Falla con tiempo de sobra.** Las dos fuentes preferentes se contradicen y una se contradice a sí misma (C4). No lo doy por sabido.
- **Si la clasificación sigue en "beta" en S15.** Ver C7: las fuentes se pisan y no hay declaración oficial en 3.2.1.

---

## Contradicciones

**C1 — Temporizador de la Falla: 15 minutos vs 10 minutos.**
- Maxroll: *"you need to slay enough monsters before the 15-minute timer runs out"* — https://maxroll.gg/d4/resources/pit-guide (16 jul 2026)
- Icy Veins: *"Upon slaying enough monsters within the 10-minutes timer, a portal to the boss' arena appears"* — https://www.icy-veins.com/d4/guides/the-pit-of-the-artificers-guide/ (titulada S15)
- **Sin resolver.** Sospecho contaminación desde la Torre, que sí son 10 minutos y es un texto más reciente, pero no tengo forma de comprobarlo sin abrir el juego. La pantalla del jugador manda.

**C2 — Intentos de mejora de glifo por run: 9 vs 4 vs 5.**
- Maxroll Falla + Maxroll War Plans: 4 de base + 1 sin morir + hasta 4 de War Plans = **9**.
- Icy Veins: *"three attempts to upgrade your Glyph's rank, with a bonus attempt if you didn't die"* = **4**, sin mencionar War Plans.
- Maxroll Tableros de Paragón: *"3 attempts... +1 extra if you did not die... (+1 extra from Seasonal Blessings)"* = **5**.
- **Resuelto a favor del 9**: las dos páginas que lo dan son las más recientes (16 jul y 5 ago 2026) y coinciden de forma independiente; la de Paragón es del 9 de julio, anterior a la actualización que añadió War Plans a estas guías, y la de Icy Veins no menciona War Plans en absoluto.

**C3 — Desbloqueo de la Falla.**
- Maxroll: capstone "Hellish Descent" del Rango de Temporada II, o nivel 70 en Eterno.
- Icy Veins: *"You will automatically unlock The Pit from Tier 1 to 10"*.
- **Sin resolver del todo.** Pueden ser compatibles (desbloqueas el modo por capstone y luego tienes los tiers 1–10 abiertos de salida), pero ninguna lo dice así.

**C4 — Tiers que desbloquea el tiempo sobrante: Icy Veins se contradice consigo misma en la misma página.**
- Versión A: *"If you finish a run with 4-6 minutes left, you skip two level and unlock an additional tier... if you defeat the boss with 6+ minutes left on the timer, two additional Tiers will unlock."*
- Versión B, tres líneas más abajo: *"Defeating the boss with 4-6 minutes left unlocks 3 additional tier. Defeating the boss with 6+ minutes left unlocks 5 additional tiers."*
- https://www.icy-veins.com/d4/guides/the-pit-of-the-artificers-guide/
- **Señal de página remendada**: texto viejo conviviendo con texto nuevo. Ninguna de las dos versiones es utilizable.

**C5 — El escalado de vida de la Falla: la propia fuente no cuadra consigo misma.**
- Tabla por tramos: tiers 4–10 → **+26,5% de vida por tier**.
- Tabla de acumulados de la misma página: Tormento 1 (Falla 10) → **+719,20%**.
- Con +26,5% saldría +936%. El +719,20% solo sale si los tiers 8, 9 y 10 van a **+17%**.
- https://maxroll.gg/d4/resources/difficulty-overview (26 jun 2026)
- **Lectura**: el tramo bueno es probablemente **4–7 a +26,5%** y **8 en adelante a +17%**. Todo lo demás de la tabla de acumulados cuadra exactamente, así que el error está en el titular del tramo, no en las cifras acumuladas. Es el ejemplo perfecto de por qué no basta con copiar una tabla bonita.

**C6 — Cadencia de reseteo de las clasificaciones: quincenal vs semanal.**
- Oficial, anuncio de la beta en S11 (2.5.2, enero 2026): *"Leaderboards will run in multiple two-week rounds throughout the season"*, con rondas de ejemplo del 12 al 26 de enero y del 26 de enero al 9 de febrero — https://news.blizzard.com/en-us/article/24247514/dominate-the-tower-and-leaderboards-beta
- Desde S14: **semanal**, con recompensas al primer login tras el reset semanal — https://www.icy-veins.com/d4/news/earn-new-rewards-for-participating-in-the-diablo-4-tower-leaderboards-in-season-14/
- **Resuelto a favor del semanal.** El propio anuncio de S11 avisaba: *"this timing cadence may be subject to change"*. Es un marco oficial pero caducado; citarlo hoy como vigente sería un error clásico de fuente antigua con sello de autoridad.

**C7 — ¿Sigue la clasificación en beta?**
- Icy Veins, guía titulada Season 15: *"the leaderboard is only in its Beta phase for now"*.
- Icy Veins, noticia de S14: *"The Tower & Leaderboards will finally be coming out of Beta in Season 14"*.
- Se contradicen entre sí, dentro del mismo sitio. 3.2.1 no dice nada al respecto. **Sin resolver**, aunque la noticia de S14 es más específica y más creíble que el párrafo arrastrado de la guía.

**C8 — Categorías de clasificación en solitario: 8 clases vs 6.**
- Maxroll (29 jul 2026) lista 8: Bárbaro, Druida, Nigromante, Pícaro, Hechicero, Espiritista, **Paladín** y **Brujo**.
- Icy Veins (S15) lista 6: le faltan Paladín y Brujo.
- **Resuelto a favor de Maxroll**: la propia cabecera de Icy Veins muestra las 8 clases del juego, incluidas Paladín y Brujo, así que su lista de 6 es un descuido, no una regla del juego.

**C9 — ¿Se puede fabricar el Compás de Horda Infernal?**
- Maxroll: *"Further Infernal Hordes Compass can not be crafted"* — https://maxroll.gg/d4/resources/infernal-hordes (16 jul 2026)
- Notas oficiales 3.2.1: *"Reduced the cost to craft an Infernal Horde Compass from 666 to 500 Sigil Powder"*, en la sección del Ocultista.
- **Resuelto a favor de lo oficial**: sí se fabrica. La guía de Maxroll está desactualizada en este punto.

**C10 — Qué Esquirla modifica qué actividad.**
Varios resúmenes automáticos de páginas secundarias atribuían las Hordas Infernales a la Esquirla de
Baal. El texto oficial dice otra cosa, y lo dejo fijado aquí porque es fácil equivocarse:
Diablo → **Zona Infernal + Hordas Infernales**; Baal → **La Ciudad Subterránea + Jefes de Guarida**;
Mefisto → **La Falla + Mazmorras de Pesadilla**; y las **tres** modifican el Árbol de los Susurros.
- https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy (12 sep 2026)

**C11 — Hora exacta de lanzamiento de S15.**
- Icy Veins: *"Season 15 will launch on Tuesday, September 15th, 10:00 AM PDT"* (= 17:00 UTC) — https://www.icy-veins.com/d4/guides/diablo-4-latest-season/
- El briefing de este proyecto la fija en **16:30 UTC**.
- El blog oficial **no da hora de arranque de temporada**: el único "11:00 a.m. PT" que aparece es la ventana de los Twitch Drops (15 al 29 de septiembre), no el lanzamiento.
- Lo dejo anotado sin resolver porque no afecta a ningún dato de endgame, pero la discrepancia existe.
