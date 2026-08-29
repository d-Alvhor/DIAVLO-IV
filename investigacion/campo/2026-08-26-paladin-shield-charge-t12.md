# Hallazgo de campo — Paladín Shield Charge en Tormento 12

**Fecha:** 2026-08-26 · **Fuente:** el jugador, fichas de personaje capturadas en pantalla.
**Nivel de evidencia:** OFICIAL (lectura directa del juego). Supera a cualquier web.
**Personaje:** Paladín nivel 70, Shield Charge, Tormento 12, parche 3.1.3.

## Ficha completa

### Ofensiva
Daño base de arma **3.728** · Velocidad de arma **1,20** · Bonus vel. ataque **18,9%**
Prob. golpe crítico **44,4%** · Daño de golpe crítico **971,0%**
Daño por vulnerabilidad **133,8%** · Todo el daño **128,2%** · Daño físico **135,0%**
Daño contra élites **117,9%** · **Espinas 6.782** · Prob. de Castigo **65,0%**

### Defensiva
Vida máxima **11.260** · Vida por golpe **1.908** · Curación recibida **26,2%**
Armadura **46.683** → **81,1% de reducción de daño**
(20.526 por estadísticas del equipo · 19.137 por la Fuerza · 7.017 de otras fuentes)
**Dureza 334.925** · Reducción de todo el daño **43,1%**
Probabilidad de bloqueo **60,0%** (en ciudad) · Reducción de bloqueo **27,7%**
Resistencias: fuego 6.184 · rayos 5.246 · física 2.875 · veneno 2.806 · **frío 1.860 · sombra 1.860**

### Principales y utilidad
Fuerza **5.037** · Inteligencia 691 · Voluntad 748 · Destreza 571
Máximo de Fe 100 · Reducción coste de Fe 12,1% · Regeneración de fe 1,50
Velocidad de movimiento **137,5%** · Reducción de reutilización 21,2%

## Hallazgos que ninguna guía publica

### 1. "Resolución máxima" en la ficha muestra 15 en ciudad y 27 en combate
La ficha de personaje **en ciudad** marcaba **15**; peleando marcaba **27**. Los 27 cuadran con
la aritmética del equipo (8 base + 5+5+5 de temples + 2 de Yunque de Glynn + 2 de conjunto).
**Conclusión: el campo de la ficha en ciudad no refleja el máximo real.** No sirve para planificar.

### 2. El burst de la build se quita a sí mismo el bloqueo — y esto explica las muertes
Con **Aspecto de Interdicción a 2,6% de bloqueo por acumulación** y **40% base del escudo**:

| Resolución | Bloqueo del aspecto | + escudo | Estado |
|---:|---:|---:|---|
| 27 (llena) | 70,2% | 110% | **capado** |
| 11 (tras gastar 16 con Mantle of the Grey) | 28,6% | 68,6% | **NO capado** |

**Mantle of the Grey consume hasta 16 de Resolución** para dar su multiplicador. Cada burst
tira el bloqueo del 100% al ~69% justo cuando el jugador está metido en el paquete.

**El bloqueo se capa a partir de ~23 de Resolución.** Por eso la guía pide 30: no es el techo,
**es el colchón** para que gastar 16 no te deje por debajo del cap.

**Ninguna guía consultada explica esto.** Todas dicen "llega a 30" sin decir para qué.

### 3. Resistencias descompensadas 3:1
Frío y sombra a 1.860 frente a fuego 6.184. Punto ciego defensivo que no aparece en ninguna
lista de prioridades de afijos.

### 4. El crítico es la palanca de daño desaprovechada
Con **971% de daño crítico** y solo **44,4% de probabilidad**, más de la mitad de los golpes
no ven el multiplicador. Pasar de 44,4% a 60% de probabilidad es **+29% de daño medio**
(×5,3 → ×6,8). El Aura de Fanatismo a rango 15 da 14% de probabilidad **gratis**.

## Regla general que sale de aquí

**En builds que CONSUMEN un recurso para hacer daño y a la vez lo usan para defenderse,
el número que importa no es el máximo: es el resto después de gastar.** Documentar solo el
máximo —como hacen todas las guías— oculta el momento exacto en que el jugador muere.
