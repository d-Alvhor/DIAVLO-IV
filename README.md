# DIAVLO IV

Guía de **Diablo IV** para **nigromante sin expansiones**, jugando en dúo (PC + consola),
escrita contra el parche vivo y con la fuente pegada a cada afirmación.

**→ [Leer la guía](https://d-alvhor.github.io/DIAVLO-IV/)**

## Por qué existe

Las guías públicas de Diablo IV tienen dos fallos que a un principiante le cuestan horas:

1. **No se fechan.** Mezclan parches y temporadas sin declararlo, y un novato no puede
   distinguir un consejo vivo de uno muerto hace tres temporadas.
2. **Asumen las expansiones en silencio.** Te mandan a por runas, mercenarios y zonas que
   no tienes, sin avisarte nunca.

Aquí cada sistema lleva **✅ juego base** o **🔒 requiere expansión**, y cada afirmación que
importa lleva su nivel de evidencia visible: *oficial · corroborado · fuente única · en
disputa · sin confirmar*.

Durante la construcción, varias wikis conocidas resultaron estar publicando textos del juego
reescritos meses antes. **Que cinco páginas coincidan no es corroboración si las cinco copian
de la misma versión muerta.**

## Cómo está montado

```
contenido/          fuente de verdad, en markdown
  nucleo/           sobrevive a la temporada (ajustes, mando, conceptos, cross-play)
  version/          atado al parche (dificultad, builds, itemización, paragón)
  temporada/        muere con la temporada
construir.mjs       markdown -> index.html. Node puro, CERO dependencias.
investigacion/      19 informes, sus refutaciones, y capturas de campo del jugador
.claude/skills/     el agente que reinvestiga y regenera
```

**El invariante que hace barato el relevo de temporada:** `nucleo/` no puede enlazar a
`temporada/`, y lo valida la build. Cuando cambie la temporada se archiva una capa en vez de
reescribir la guía.

## Construir

```
node construir.mjs
```

Produce `index.html`: un solo fichero autocontenido, sin CDN ni fuentes externas, que **abre
sin conexión**. Buscador con normalización de tildes y búsqueda bidireccional español↔inglés.

La build es **fail-closed**: rompe ante HTML crudo, protocolos no permitidos en enlaces,
sintaxis fuera del dialecto, frontmatter incompleto, `corroborado` con menos de dos fuentes,
porcentajes sin bloque de evidencia, o un paso obligatorio que exija expansión. Y es
**determinista**: mismo contenido, mismo fichero byte a byte.

## Licencia

MIT para el código. El contenido de la guía es un trabajo de la comunidad; Diablo IV es
propiedad de Blizzard Entertainment.
