# Paladín — parche 3.2.1 (Temporada 15, "Hell's Legacy")

**Anclaje:** 3.2.1 Build #73552, todas las plataformas — 15 de septiembre de 2026.
**Fuente primaria única:** las notas de 3.2.1 **no tienen artículo propio**; van embebidas en el blog de temporada
`news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy`,
bajo el ancla `#Patch`. Todo lo marcado `oficial` sale de ahí.

> **Aviso de estado (15/09/2026):** la temporada arranca HOY a las 16:30 UTC. **No existen leaderboards,
> ni builds probadas, ni un solo dato de juego real de S15.** Todo lo que no sea nota de parche es
> teoría. Cualquier página que hoy diga "la mejor build de la S15" está especulando.

## Resumen

1. **A tu build no la han tocado.** Ni Shield Charge, ni Defiance Aura, ni Condemn, ni la mecánica
   Retribution, ni Block Chance, ni Blocked Damage Reduction aparecen **una sola vez** en las notas
   de 3.2.1. Verificado por ausencia contra el texto oficial, no inferido.
2. **Sube lo genérico:** el escalar de estadística principal pasa de 1.25 a 1.625 (daño por cada 10 de
   Fuerza: 1.25% → 1.625%) y **Juramento de Juggernaut sube de 80% a 100%**. Son los dos buffs que sí te llegan.
3. **El parche es de Judgement/Judicator**, no de Espinas. El cambio grande ("Judgement escala con el
   rango de la habilidad que lo aplicó") no afecta a una build de espinas y bloqueo.
4. **Dos riesgos reales:** el fix de *"Maximum Resolve Stacks estaba sin tope al templar"* y el de
   *"Aspect of the Indomitable otorgaba bonificaciones no intencionadas"*. Ambos son nerfs encubiertos
   potenciales a un Juggernaut; ninguna fuente cuantifica el impacto. **Compruébalo en pantalla.**
5. **Solo hay UNA guía endgame de Paladín actualizada a S15 en fuentes preferentes** (Maxroll Shield
   Charge, 14/09/2026) y es justo una build de espinas y bloqueo. La de Shield of Retribution endgame
   sigue en S14 (27/07/2026): está **caducada** respecto a 3.2.1.

---

## Hallazgos

### A. Cambios globales de clase (3.2.1)

| Dato | Cifra | Fuente | Fecha | Evidencia |
|---|---|---|---|---|
| Escalar de estadística principal | 1.25 → **1.625** (daño por 10 de Fuerza: 1.25% → 1.625%) | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 15/09/2026 | oficial |
| Judgement escala con el **rango de la habilidad que lo aplicó** | (sin cifra publicada) | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 15/09/2026 | oficial |
| Afijos de **daño con el tiempo (DoT)** retirados del Paladín | ya no son usables ni aparecen en objetos | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 15/09/2026 | oficial |

Sobre el escalar: Blizzard lo redacta como "daño por cada 10 puntos de Fuerza". Eso es **+30% relativo
sobre el multiplicador de Fuerza**, no +30% de daño final; cuánto notas depende de qué fracción de tu
daño venía de Fuerza. En una build de espinas, donde el daño sale del valor de Thorns y no del arma,
ese reparto **no está documentado en ninguna fuente preferente**. Ver *Huecos*.

### B. Juramentos (Oaths) — 3.2.1

| Juramento | Cambio | Fuente | Fecha | Evidencia |
|---|---|---|---|---|
| **Juggernaut's Oath** (Juramento de juggernaut) | daño **80% → 100%** | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 15/09/2026 | oficial |
| **Disciple Oath** (Juramento de discípulo) | daño **80% → 100%** | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 15/09/2026 | oficial |
| **Zealot Oath** (Juramento de zelote) | daño por acumulación de **Fervor 25% → 35%** | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 15/09/2026 | oficial |
| **Judicator Oath** | **efecto nuevo:** "si Judgement solo golpea a 1 enemigo, inflige 100% más daño" | [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) | 15/09/2026 | oficial |

**Solo cambia la cifra de daño del Juggernaut's Oath.** Su funcionamiento (consumir Resolve, tamaño,
suelo mínimo de acumulaciones) **no se menciona**: sigue como estaba.

Cadena de valores para que veas la tendencia — el Juggernaut's Oath venía de **60% → 80% en 3.1.x**
([Blizzard, notas 3.1.0–3.1.3](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes), 12/08/2026, `oficial`)
y ahora **80% → 100%**. Dos parches seguidos subiéndolo.

### C. Habilidades — 3.2.1

| Habilidad | Cambio | Evidencia |
|---|---|---|
| **Blessed Shield — Shield of Retribution** | ahora **escala con rangos de habilidad el porcentaje de Espinas que inflige** | oficial |
| Blessed Shield — Shield of Justice | detona Judgement y rebota 5 veces más; al detonar Judgement, el siguiente lanzamiento +40%[x], máx. 5 acumulaciones, y +50%[x] daño de Judgement 5 s | oficial |
| Holy Bolt | mejora "Judgement" renombrada a "Damage Increase": ahora **20%[x] más daño** en vez de aplicar Judgement | oficial |
| Spear of the Heavens — Fist of the Heavens | los enemigos del impacto principal ya pueden recibir **un** proyectil adicional (solo uno) | oficial |
| Divine Lance | 90% → **110%**; Tip of the Spear 35% → **39%**; Zealous Joust 74% → **91%**; Divine Javelin inicial 99% → **121%**, estallido 495% → **605%** | oficial |
| Zeal | daño del golpe adicional 20% → **35%** | oficial |
| Shield Bash | Lay Siege 246% → **349%**; Smite inicial 287% → **451%**, secundario 102% → **307%** | oficial |

Todas: [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy), 15/09/2026.

**Shield of Retribution es el ÚNICO retoque a Espinas del Paladín en todo 3.2.1**, y es a la variante
de Blessed Shield, no a la estadística Thorns. Si no llevas Blessed Shield, no te toca.

### D. Lo que NO se menciona — verificado por ausencia

Esto lo pediste explícitamente y es, probablemente, lo más valioso del informe. Comprobado término a
término contra el texto oficial de 3.2.1 y contra la transcripción de Maxroll del mismo parche:

| Término buscado | ¿Aparece en 3.2.1? |
|---|---|
| **Punish / Punishment** | **No** |
| **Retribution** (la mecánica) | **No** |
| **Shield Charge** (Carga con escudo) | **No** |
| **Defiance Aura / Defiant Aura** (Aura desafiante) | **No** |
| **Condemn** | **No** |
| **Crusader's March** | **No** |
| **Block Chance** (prob. de bloqueo) | **No** |
| **Blocked Damage Reduction / Block Reduction** | **No** |
| **Thorns** en contexto Paladín | **Solo** vía Shield of Retribution (arriba). Las demás menciones de Thorns del parche son de **Spiritborn y Brujo**, no tuyas |
| **Resolve** | **Una sola vez**, y es un bug fix de templado (abajo) |
| **Herald of Zakarum** | **No** |
| **Mantle of the Grays / Grey** | **No** |
| **Penitent Greaves** | **No** |
| **Fists of Fate** | **No** |
| **Bloodthirsting Idol** | **No** |

Fuentes del cruce: [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy) (15/09/2026, `oficial`)
y [Maxroll — Hell's Legacy 3.2.1 Patch Notes](https://maxroll.gg/d4/news/diablo-4-3-2-1-patch-notes) (12/09/2026, `corroborado`).

**Traducción práctica:** tu barra de habilidades y tus tres piezas clave salen del parche **intactas**.
Lo que cambia bajo tus pies es el escalar de Fuerza, el Juggernaut's Oath y los dos fixes de la sección F.

### E. Objetos únicos y talismanes — 3.2.1

| Objeto | Cambio | Evidencia |
|---|---|---|
| **Tibault's Will** | **Regeneración de recursos 50% → 25%** (nerf) | oficial |
| **Crown of Lucion** | bug fix: "no se activaba de forma consistente cuando las habilidades se lanzaban con coste de recurso cero" | oficial |
| **X'Fal's Corroded Signet** | **ya no lo puede equipar el Paladín** | oficial |
| **Cathedral Song** | rediseñado: "consumir Judgement 100 veces invoca Spear of the Heavens sobre un enemigo aleatorio. Judgement en jefes cuenta como 10. Tu daño de Spear of the Heavens aumenta 80-100%" (antes: Golpe de suerte 8-10% al lanzar habilidades de Discípulo) | oficial |
| **Heaven's Radiant Fire** (talismán, 5 pz) | de "máx. 40 acumulaciones de Judgement Day" a "bonificación de daño de Judgement Day sube a **25%[x]** y máximo de acumulaciones a **20**. Juzgar a un jefe otorga **5** acumulaciones" | oficial |
| **Cathan's Righteous Will** (talismán, 5 pz) | duración **10 s → 15 s** | oficial |

Todas: [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy), 15/09/2026.

**Ninguno de tus seis objetos de la lista cambió.** Tibault's Will sí, y es el único de tu lista tocado:
si lo llevas por la regeneración, ese pilar se ha partido por la mitad. Crown of Lucion solo recibe un
arreglo de consistencia, no un cambio de efecto.

### F. Correcciones de errores que sí te pueden mover la aguja

| Fix | Lectura | Evidencia |
|---|---|---|
| "Maximum Resolve Stacks estaba **sin tope** al templar" (sección Templado) | **Riesgo de nerf directo.** Si tu templado de máximo de Resolve estaba por encima del tope legítimo, 3.2.1 te lo recorta. Un Juggernaut vive de ese máximo | oficial |
| "**Aspect of the Indomitable** otorgaba bonificaciones no intencionadas" | **Riesgo de nerf.** No dicen cuáles ni cuánto | oficial |
| "**Clash's Skirmish Variant** atacaba más despacio de lo previsto" | **Buff efectivo** si usas esa variante — Clash te da Crusader's March (prob. de Retribution, daño de Espinas y prob. de bloqueo) | oficial |
| "**Fanaticism Aura** hacía que el Santuario de artillería disparase de forma errónea" | Cosmético para ti | oficial |
| "**Iron Conviction** otorgaba variantes de aura no intencionadas" | Revisa si te beneficiabas de ello | oficial |
| "**Aegis** usaba un valor de duración de provocación incorrecto" | Menor | oficial |

Todas: [Blizzard 3.2.1](https://news.blizzard.com/en-us/article/24295394/celebrate-30-years-of-diablo-in-season-of-hell-s-legacy), 15/09/2026.

### G. Aspectos legendarios — 3.2.1

- **Aspect of Watkin's Law** — rediseñado y **encadenado al Judicator Oath**: "mientras uses el Juramento
  Judicator, las habilidades Judicator infligen 45-65% más daño a enemigos afectados por Judgement, y
  entonces consumen y reaplican Judgement. Consumir y reaplicar solo puede ocurrir una vez cada 3 s por
  enemigo." Antes funcionaba sin condición de juramento. `oficial`
- **Aspect of the Judicator** — bonificación de daño y tamaño de Judgement **40-60% → 60-80%**. `oficial`

### H. Builds de Paladín que proponen las fuentes preferentes para S15

**Lo primero: casi nadie ha actualizado.** Estado real a 15/09/2026:

| Guía | Fecha | ¿S15? | Evidencia |
|---|---|---|---|
| [Maxroll — **Shield Charge Paladin Endgame**](https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide) | 14/09/2026 (registro de cambios: "Updated for Season 15", 15/09/2026) | **Sí** | unica |
| [Maxroll — Shield of Retribution Paladin **Leveling**](https://maxroll.gg/d4/build-guides/shield-of-retribution-paladin-leveling-guide) | cabecera 14/09/2026 / S15, **pero su propio registro de cambios dice "actualizada para Season 14", 29/06/2026** | dudoso | disputa |
| [Maxroll — Shield of Retribution Paladin **Endgame**](https://maxroll.gg/d4/build-guides/shield-of-retribution-paladin-guide) | 27/07/2026 | **No, S14** | unica |
| Maxroll — Blessed Hammer / Divine Lance / Zeal **leveling** | 14/09/2026 | Sí | unica |
| Maxroll — Auradin, Zenith, Clash, Wing Strikes, Support, Zeal, Blessed Hammer, Divine Lance (endgame) | jul–ago 2026 | **No, S14** | unica |
| [Icy Veins — Blessed Shield Paladin](https://www.icy-veins.com/d4/guides/blessed-shield-paladin-build/) | 13/09/2026, dice S15 (el título de la página sigue diciendo "Season 14") | parcial | disputa |
| [Icy Veins — hub de builds de Paladín](https://www.icy-veins.com/d4/paladin/builds/) | sin marca de fecha ni de temporada | **No** | unica |
| [Maxroll — Paladin Class Overview](https://maxroll.gg/d4/resources/paladin-class-overview) | 14/07/2026, S14 | **No** | unica |

**La única propuesta endgame viva y pertinente para ti — Maxroll Shield Charge (14/09/2026):**
es una build de **Espinas físicas y bloqueo**, exactamente tu familia. Barra: **Shield Charge** (daño
principal), **Clash**, **Fortress**, **Condemn**, **Fanaticism Aura**, **Defiance Aura**. Juramento:
**Juggernaut**. Únicos: **Herald of Zakarum**, **Mantle of the Grey**, **Penitent Greaves** y
**Leoric's Crown** (*no* Crown of Lucion — esta guía no menciona Crown of Lucion en absoluto).

Citas verbatim que importan:
- Clash: *"Clash gives you the Crusader's March buff, which provides Retribution chance, Thorns damage and Block Chance."* Mantenerlo activo cada 6 s.
- Defiance Aura: *"recovers health, generates Resolve and can be activated to grant Unstoppable"*, y da mucho daño de Espinas vía **Rite of Thorns**.
- Aspect of Excellence: *"works alongside your Juggernaut Oath to give you increased Retribution chance and size."*
- Herald of Zakarum: solo lo describe como *"great for Retribution builds, as it significantly boosts its proc rate as well as the area of effect"*.

**Procedencia de la propuesta:** la guía **no dice** que esté basada en PTR, pero tampoco cita ni un solo
cambio de 3.2.1 en su texto. Su registro de cambios se limita a "Updated for Season 15". Dado que S15
no ha arrancado, **es una guía de S14 re-fechada con los ajustes de PTR/notas, no una build probada en S15**.
Trátala como hipótesis de arranque, no como resultado.

---

## Huecos

1. **Herald de Zakarum: no he encontrado su texto verbatim con cifras en ninguna fuente preferente con
   fecha dentro de 3.2.1.** Lo único con fecha viva es la descripción cualitativa de Maxroll ("sube
   mucho la tasa de proc y el área"). La investigación previa de este proyecto (`pal-equipo.md`) recoge
   "+40-50% de Fuerza, Resistencia, Armadura y probabilidad de Retribution; Retribution +50% de tamaño",
   pero **eso es un dato interno anterior, no reverificado hoy**. No lo publiques como cifra de 3.2.1.
2. **Penitent Greaves, Fists of Fate, Bloodthirsting Idol:** solo he podido confirmar que **no cambian
   en 3.2.1**. Sus textos y cifras actuales no los he verificado en fuente preferente con fecha.
3. **¿La nova de Retribution cuenta como habilidad de Juggernaut?** No lo he podido confirmar en
   **ninguna** fuente. Ver *Contradicciones 1* — es la pieza de tu modelo que más conviene comprobar.
4. **Magnitud del fix de "Maximum Resolve Stacks sin tope al templar":** nadie publica cuál es el tope
   legítimo ni cuánto recorta. **Solo se ve en tu pantalla**, comparando tu máximo de Resolve antes y
   después del parche.
5. **Qué otorgaba de más Aspect of the Indomitable:** no publicado.
6. **Cómo reparte el escalar de Fuerza (1.625) en una build de Espinas:** ninguna fuente preferente
   modela si Thorns escala con Fuerza ni en qué proporción. Sin eso, el "+30% al escalar" no se traduce
   a daño final.
7. **Parche 3.1.4 (≈9/09/2026): Blizzard nunca publicó notas.** Hay hilo en el foro oficial preguntando
   justo eso ("Update 3.1.4 without accompanying patch notes?"). Es un cambio de ~150 MB a ciegas: si algo
   de tu build se movió entre 3.1.3 y 3.2.1, pudo pasar ahí y **no hay forma documental de saberlo**.
8. **Delta PTR 3.2.0 → live 3.2.1:** Icy Veins publicó un artículo sobre "notas actualizadas" marcando en
   azul lo nuevo, pero **no separa limpiamente qué era PTR y qué llegó a 3.2.1**. Los valores que doy
   arriba son los del texto final de 3.2.1, no los del PTR.
9. **Block Chance y Blocked Damage Reduction:** confirmo que no se mencionan, pero **eso no prueba que
   sus topes internos no se hayan tocado en silencio.** Solo la pantalla lo confirma.
10. **Cero datos de juego real de S15.** Ni falla superada, ni clasificación, ni tiempos. La temporada
    empieza hoy a las 16:30 UTC.

---

## Contradicciones

**1. El mecanismo de tu propio escudo (la más importante).**
Tu modelo, tal y como está enunciado: *"el Heraldo de Zakarum (Castigo) hace que las espinas emitan un
pulso al bloquear, y ese pulso cuenta como habilidad de juggernaut"*. Lo que dicen las fuentes:

- **Retribution es una mecánica de clase, no un efecto del Heraldo.** Maxroll la define como *"Creates
  Thorns explosions around you, triggered by specific skills and passives"*
  ([Paladin Class Overview](https://maxroll.gg/d4/resources/paladin-class-overview), 14/07/2026). El
  Heraldo **solo** *"boosts its proc rate as well as the area of effect"*
  ([Shield Charge guide](https://maxroll.gg/d4/build-guides/shield-charge-paladin-guide), 14/09/2026).
  Es decir: el pulso existiría sin el Heraldo; el escudo lo hace más frecuente y más grande.
- **Contra el "cuenta como habilidad de juggernaut":** la guía S15 de Shield Charge dice literalmente
  *"Juggernaut Skills are not worth pursuing for this build, as they don't boost Thorns damage from
  Shield Charge"* — y aun así **sí** usa el **Juramento** Juggernaut. Distinción fina y decisiva:
  **el Juramento sí, las habilidades Juggernaut no.** Si tu escalado dependía de que el pulso contase
  como habilidad de Juggernaut, esa premisa **no está respaldada por ninguna fuente** y una fuente viva
  apunta en contra.
- **Versión conciliadora (no verificada):** lo que sí convierte una habilidad en Juggernaut es la mejora
  **Shield of Retribution** sobre Blessed Shield. Si tu build pasa por ahí, tu modelo podría ser correcto
  *para esa vía concreta* y no para la nova genérica de bloqueo. **Sin confirmar.**

*Consecuencia práctica:* el Juggernaut's Oath sube 80→100% y eso te llega **seguro** por el juramento.
Si además esperabas que multiplicase el pulso por contar como habilidad Juggernaut, **no lo des por hecho**.

**2. "Punición" / "Castigo" / "Punish": el nombre no cuadra.**
No existe "Punish" en las notas de 3.2.1 (verificado: no aparece). Tampoco figura como habilidad en la
lista de la guía S15 de Shield Charge, cuya barra es Shield Charge · Clash · Fortress · Condemn ·
Fanaticism Aura · Defiance Aura. Dos lecturas incompatibles:
- **(a)** "Punición" es **Condemn** — es la única casilla libre al mapear tu barra contra la de Maxroll.
- **(b)** "Punish/Punishment" es una **mejora de Clash**, según un resumen de búsqueda que **no he podido
  verificar en página con fecha**. Lo que sí está verificado es que Clash otorga **Crusader's March**.

Y "Castigo", en tu frase sobre el Heraldo, encaja con **Retribution** (que este proyecto ya tradujo como
**Represalia** en `pal-equipo.md`), no con una habilidad de la barra. **Conviene que confirmes los tres
nombres en tu cliente en español antes de que nada de esto entre en la guía.**

**3. Cambios de 3.1.x que circulan como si fueran de 3.2.1.**
Varios resúmenes de buscador mezclan parches. Estos valores son **3.1.x, NO 3.2.1**
([Blizzard, notas 3.1.0–3.1.3](https://news.blizzard.com/en-us/article/24287406/diablo-iv-patch-notes), 12/08/2026):
Shield Charge 90% → 180% y enfriamiento 10 → 8 s · Defiance Aura armadura y resistencias 30% → 50% ·
Stalwart (Paragón) reducción de daño bloqueado 5% → 15% · Aegis +30% armadura · Juggernaut/Judicator
60% → 80% · Disciple 50% → 80% · Zealot 21% → 25% por eco · Wing Strikes 160% → 200% ·
Seal of the Second Trumpet 80-100% → 100-150%.
También circula "Shield of Retribution: daño de Espinas reducido de 100% a 70%" atribuido vagamente:
**no está en 3.2.1**. Es anterior.

**4. Fechas que se contradicen dentro de la propia página.**
- Maxroll *Shield of Retribution Leveling*: cabecera 14/09/2026 + "Season 15", registro de cambios
  "updated for Season 14 — 29/06/2026".
- Icy Veins *Blessed Shield*: el título dice "(Season 14)", el cuerpo dice última actualización
  13/09/2026 y Season 15.
En ambos casos **el registro de cambios interno es más fiable que la cabecera**: las cabeceras se
re-sellan en bloque al abrir temporada. Regla de la casa: si la página no cita un cambio concreto de
3.2.1 en su texto, no está realmente actualizada a 3.2.1.
