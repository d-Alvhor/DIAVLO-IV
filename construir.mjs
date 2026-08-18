#!/usr/bin/env node
// Generador de la guía. Node puro, CERO dependencias.
// contenido/**/*.md  ->  index.html (un solo fichero, autocontenido, offline)
//
// Reglas duras:
//  - Dialecto markdown CERRADO. Sintaxis desconocida => la build rompe.
//  - HTML crudo => la build rompe SIEMPRE. No se sanea: se rechaza.
//  - Enlaces: solo https:, http:, anclas # y rutas relativas. Cualquier otro => rompe.
//  - Determinista: mismo contenido => mismo index.html byte a byte.

import { readFileSync, writeFileSync, readdirSync, statSync, existsSync } from 'node:fs'
import { join, relative, dirname, sep } from 'node:path'
import { fileURLToPath } from 'node:url'

const RAIZ = dirname(fileURLToPath(import.meta.url))
const DIR = join(RAIZ, 'contenido')
const SALIDA = join(RAIZ, 'index.html')

const CAMPOS = ['titulo', 'capa', 'parche', 'temporada', 'estado', 'entitlement', 'verificado', 'revisar_despues']
const CAPAS = ['nucleo', 'version', 'temporada', 'archivo']
const ESTADOS = ['vivo', 'ptr', 'caducado', 'archivado']
const ENTS = ['base', 'voh', 'loh']
const NIVELES = ['oficial', 'corroborado', 'unica', 'disputa', 'sinconfirmar']
const PROTOCOLOS = /^(https?:\/\/|#|\.{0,2}\/)/

const errores = []
const fallo = (f, l, m) => errores.push(`${f}:${l} - ${m}`)

const esc = (s) => String(s)
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
  .replace(/"/g, '&quot;').replace(/'/g, '&#39;')

const sinTildes = (s) => s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase()
const slug = (s) => sinTildes(s).replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 60)

function ficheros(dir, acc = []) {
  if (!existsSync(dir)) return acc
  for (const n of readdirSync(dir).sort()) {
    const p = join(dir, n)
    if (statSync(p).isDirectory()) ficheros(p, acc)
    else if (n.endsWith('.md')) acc.push(p)
  }
  return acc
}

function frontmatter(txt, rel) {
  if (!txt.startsWith('---\n')) { fallo(rel, 1, 'falta el frontmatter'); return null }
  const fin = txt.indexOf('\n---\n', 4)
  if (fin === -1) { fallo(rel, 1, 'frontmatter sin cerrar'); return null }
  const meta = {}
  txt.slice(4, fin).split('\n').forEach((linea, i) => {
    if (!linea.trim() || linea.trim().startsWith('#')) return
    const c = linea.indexOf(':')
    if (c === -1) return fallo(rel, i + 2, `linea de frontmatter invalida: ${linea}`)
    meta[linea.slice(0, c).trim()] = linea.slice(c + 1).trim().replace(/\s+#.*$/, '').replace(/^["']|["']$/g, '')
  })
  for (const c of CAMPOS) if (!(c in meta)) fallo(rel, 1, `falta el campo "${c}" en el frontmatter`)
  if (meta.capa && !CAPAS.includes(meta.capa)) fallo(rel, 1, `capa invalida: ${meta.capa}`)
  if (meta.estado && !ESTADOS.includes(meta.estado)) fallo(rel, 1, `estado invalido: ${meta.estado}`)
  if (meta.entitlement && !ENTS.includes(meta.entitlement)) fallo(rel, 1, `entitlement invalido: ${meta.entitlement}`)
  if (meta.temporada && meta.temporada !== 'todas' && !/^\d+$/.test(meta.temporada)) fallo(rel, 1, `temporada invalida: ${meta.temporada}`)
  return { meta, cuerpo: txt.slice(fin + 5) }
}

const MARCA = '\u0001'

function inline(txt, rel, ln) {
  if (/<[a-zA-Z/!]/.test(txt)) { fallo(rel, ln, 'HTML crudo prohibido'); return '' }
  const codigos = []
  let t = txt.replace(/`([^`]+)`/g, (_, c) => `${MARCA}${codigos.push(c) - 1}${MARCA}`)
  t = esc(t)
  t = t.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, (_, texto, url) => {
    const limpia = url.replace(/&amp;/g, '&')
    if (!PROTOCOLOS.test(limpia)) { fallo(rel, ln, `protocolo no permitido en enlace: ${limpia}`); return texto }
    const ext = /^https?:/.test(limpia)
    return `<a href="${esc(limpia)}"${ext ? ' target="_blank" rel="noopener noreferrer"' : ''}>${texto}</a>`
  })
  t = t.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>').replace(/(^|[^*])\*([^*]+)\*/g, '$1<em>$2</em>')
  return t.replace(new RegExp(MARCA + '(\\d+)' + MARCA, 'g'), (_, i) => `<code>${esc(codigos[+i])}</code>`)
}

function atributos(cab) {
  const a = {}
  for (const m of cab.matchAll(/(\w+)=("([^"]*)"|\S+)/g)) a[m[1]] = m[3] ?? m[2]
  return a
}

const ETIQ = {
  oficial: ['Oficial', 'Notas de parche, blog de Blizzard o captura del juego'],
  corroborado: ['Corroborado', 'Dos o mas fuentes independientes fechadas en el parche vivo'],
  unica: ['Fuente unica', 'Solo una fuente lo dice'],
  disputa: ['En disputa', 'Las fuentes se contradicen'],
  sinconfirmar: ['Sin confirmar', 'No se pudo fechar ni contrastar. No es un hecho.'],
}
const ENT_ETIQ = { base: ['\u2705', 'Juego base'], voh: ['\uD83D\uDD12', 'Vessel of Hatred'], loh: ['\uD83D\uDD12', 'Lord of Hatred'] }

function render(cuerpo, rel, meta) {
  const lineas = cuerpo.split('\n')
  const out = []; const indice = []; const busca = []
  let i = 0, cifrasFuera = 0
  const plano = (s) => s.replace(/[*`[\]]/g, '').replace(/\(([^)]*)\)/g, ' ')

  while (i < lineas.length) {
    const l = lineas[i]; const ln = i + 1
    if (!l.trim()) { i++; continue }

    if (l.startsWith(':::')) {
      const cab = l.slice(3).trim()
      const tipo = cab.split(/\s/)[0]
      const at = atributos(cab)
      const buf = []
      i++
      while (i < lineas.length && lineas[i].trim() !== ':::') buf.push(lineas[i++])
      if (i >= lineas.length) { fallo(rel, ln, `bloque ::: ${tipo} sin cerrar`); break }
      i++
      const dentro = buf.map((x) => inline(x, rel, ln)).filter(Boolean).join('<br>')
      busca.push(plano(buf.join(' ')))

      if (tipo === 'evidencia') {
        const nivel = at.nivel || 'sinconfirmar'
        if (!NIVELES.includes(nivel)) fallo(rel, ln, `nivel de evidencia invalido: ${nivel}`)
        const fs = (at.fuentes || '').split(',').map((x) => x.trim()).filter(Boolean)
        if (!fs.length && nivel !== 'sinconfirmar') fallo(rel, ln, `bloque evidencia nivel=${nivel} sin fuentes=`)
        if (nivel === 'corroborado' && fs.length < 2) fallo(rel, ln, 'nivel=corroborado exige 2 o mas fuentes')
        const [et, tit] = ETIQ[nivel] || ETIQ.sinconfirmar
        out.push(`<div class="ev ev-${esc(nivel)}"><div class="ev-h"><span class="ev-b" title="${esc(tit)}">${esc(et)}</span>` +
          (fs.length ? `<span class="ev-f">${fs.map(esc).join(' \u00b7 ')}</span>` : '') +
          `</div><div class="ev-c">${dentro}</div></div>`)
      } else if (tipo === 'build') {
        const ent = at.entitlement || 'base'
        if (!ENTS.includes(ent)) fallo(rel, ln, `entitlement invalido en build: ${ent}`)
        if (!at.nombre) fallo(rel, ln, 'bloque build sin nombre=')
        if (!at.estado) fallo(rel, ln, 'bloque build sin estado=')
        const [ic, tt] = ENT_ETIQ[ent]
        out.push(`<div class="bd"><div class="bd-h"><span class="bd-n">${esc(at.nombre || '')}</span>` +
          `<span class="bd-e">${esc(at.estado || '')}</span><span class="ent">${ic} ${esc(tt)}</span></div>` +
          `<div class="bd-c">${dentro}</div></div>`)
      } else if (tipo === 'paso') {
        const ent = at.entitlement || 'base'
        if (!ENTS.includes(ent)) fallo(rel, ln, `entitlement invalido en paso: ${ent}`)
        const obl = at.obligatorio === 'si'
        if (obl && ent !== 'base') fallo(rel, ln, `paso obligatorio con entitlement=${ent}: rompe la ruta de juego base`)
        const [ic, tt] = ENT_ETIQ[ent]
        out.push(`<div class="ps${obl ? '' : ' ps-opt'}"><div class="ps-n">${esc(at.n || '\u00b7')}</div>` +
          `<div class="ps-c">${dentro}${obl ? '' : ' <span class="ps-o">opcional</span>'}` +
          (ent === 'base' ? '' : ` <span class="ent">${ic} ${esc(tt)}</span>`) + '</div></div>')
      } else if (tipo === 'aviso') {
        const t = ['peligro', 'ojo', 'truco'].includes(at.tipo) ? at.tipo : 'ojo'
        out.push(`<div class="av av-${esc(t)}">${dentro}</div>`)
      } else {
        fallo(rel, ln, `bloque desconocido: ::: ${tipo}`)
      }
      continue
    }

    const h = l.match(/^(#{1,6})\s+(.*)$/)
    if (h) {
      const n = h[1].length
      if (n === 1) { fallo(rel, ln, 'el # de nivel 1 lo pone el generador desde el frontmatter'); i++; continue }
      if (n > 3) { fallo(rel, ln, `encabezado de nivel ${n} no permitido (maximo ###)`); i++; continue }
      const id = `${slug(meta.titulo)}-${slug(h[2])}`
      if (n === 2) indice.push({ id, txt: h[2].replace(/[*`]/g, '') })
      out.push(`<h${n} id="${esc(id)}">${inline(h[2], rel, ln)}</h${n}>`)
      busca.push(plano(h[2]))
      i++; continue
    }

    if (l.startsWith('```')) {
      const buf = []; i++
      while (i < lineas.length && !lineas[i].startsWith('```')) buf.push(lineas[i++])
      i++
      out.push(`<pre><code>${esc(buf.join('\n'))}</code></pre>`)
      continue
    }

    if (l.trim().startsWith('|')) {
      const filas = []
      while (i < lineas.length && lineas[i].trim().startsWith('|')) filas.push(lineas[i++])
      if (filas.length < 2 || !/^\s*\|[\s:|-]+\|\s*$/.test(filas[1])) { fallo(rel, ln, 'tabla sin fila separadora'); continue }
      const celdas = (f) => f.trim().replace(/^\||\|$/g, '').split('|').map((c) => c.trim())
      busca.push(plano(filas.join(' ').replace(/\|/g, ' ')))
      out.push('<div class="tw"><table><thead><tr>' + celdas(filas[0]).map((c) => `<th>${inline(c, rel, ln)}</th>`).join('') +
        '</tr></thead><tbody>' + filas.slice(2).map((f) => '<tr>' + celdas(f).map((c) => `<td>${inline(c, rel, ln)}</td>`).join('') + '</tr>').join('') +
        '</tbody></table></div>')
      continue
    }

    const li = l.match(/^(\s*)([-*]|\d+\.)\s+(.*)$/)
    if (li) {
      const ord = /\d/.test(li[2])
      const items = []
      while (i < lineas.length) {
        const m = lineas[i].match(/^(\s*)([-*]|\d+\.)\s+(.*)$/)
        if (!m) break
        items.push(m[3]); i++
      }
      busca.push(plano(items.join(' ')))
      out.push(`<${ord ? 'ol' : 'ul'}>` + items.map((x) => `<li>${inline(x, rel, ln)}</li>`).join('') + `</${ord ? 'ol' : 'ul'}>`)
      continue
    }

    const buf = []
    while (i < lineas.length && lineas[i].trim() && !/^(#{1,6}\s|:::|```|\s*\||\s*([-*]|\d+\.)\s)/.test(lineas[i])) buf.push(lineas[i++])
    const parrafo = buf.join(' ')
    // Gate de cifras. Alcance deliberadamente acotado, y conviene saber por qué:
    // exigir un bloque de evidencia para "Acto 4" o "del 1 al 70" genera tanto ruido que
    // los autores acaban envolviendo trivialidades y el marcado deja de significar nada.
    // Lo que engaña de verdad son las MAGNITUDES: porcentajes y multiplicadores
    // ("50% de sus espinas", "275% de daño", "60%[x]"). Esas no pueden ir sueltas.
    // Limitación asumida y declarada: un entero pelado en prosa SÍ pasa el gate.
    const desnudo = parrafo.replace(/`[^`]*`/g, '').replace(/\[[^\]]*\]\([^)]*\)/g, '')
    cifrasFuera += (desnudo.match(/\d+(?:[.,]\d+)?\s*%|\d+\s*\[?x\]?(?![\w])/gi) || []).length
    busca.push(plano(parrafo))
    out.push(`<p>${inline(parrafo, rel, ln)}</p>`)
  }
  return { html: out.join('\n'), indice, texto: busca.join(' '), cifrasFuera }
}

// ------------------------------------------------------------------- main

const manifiesto = existsSync(join(RAIZ, 'manifiesto.json'))
  ? JSON.parse(readFileSync(join(RAIZ, 'manifiesto.json'), 'utf8'))
  : { parche_actual: '3.1.3', temporada_actual: 14 }

const docs = []
for (const f of ficheros(DIR)) {
  const rel = relative(DIR, f).split(sep).join('/')
  const fm = frontmatter(readFileSync(f, 'utf8'), rel)
  if (!fm) continue
  if (fm.meta.estado === 'ptr' || fm.meta.estado === 'archivado') continue
  docs.push({ rel, meta: fm.meta, id: slug(fm.meta.titulo), ...render(fm.cuerpo, rel, fm.meta) })
}

for (const d of docs) {
  for (const m of d.html.matchAll(/href="([^"]+)"/g)) {
    const u = m[1]
    if (u.startsWith('#') || /^https?:/.test(u)) continue
    if (d.meta.capa === 'nucleo' && u.includes('temporada/')) fallo(d.rel, 0, 'nucleo/ no puede enlazar a temporada/')
    if (u.includes('archivo/')) fallo(d.rel, 0, 'contenido vivo no puede enlazar a archivo/')
  }
  if (d.meta.capa === 'nucleo' && d.meta.temporada !== 'todas') fallo(d.rel, 0, `capa nucleo con temporada=${d.meta.temporada}: el nucleo debe ser temporada=todas`)
  if (d.cifrasFuera > 0) fallo(d.rel, 0, `${d.cifrasFuera} cifra(s) en parrafo fuera de un bloque ::: evidencia :::`)
}

const soloAvisar = process.argv.includes('--laxo')
if (errores.length && !soloAvisar) {
  console.error(`\n  BUILD ROTA - ${errores.length} problema(s):\n`)
  for (const e of errores.slice(0, 50)) console.error('   x ' + e)
  if (errores.length > 50) console.error(`   ... y ${errores.length - 50} mas`)
  console.error('\n  (usa --laxo para generar igualmente durante el desarrollo)\n')
  process.exit(1)
}
if (errores.length) console.error(`  ! ${errores.length} problema(s) ignorados por --laxo`)

const ORDEN = { nucleo: 0, version: 1, temporada: 2 }
docs.sort((a, b) => (ORDEN[a.meta.capa] - ORDEN[b.meta.capa]) || a.rel.localeCompare(b.rel))
const NOMBRE = { nucleo: 'Fundamentos', version: `Parche ${manifiesto.parche_actual}`, temporada: `Temporada ${manifiesto.temporada_actual}` }

// Alias español<->inglés extraídos del glosario, para que el buscador funcione en los dos
// idiomas: el juego está en español y los planners en inglés. Sin esto, buscar "minions"
// no encuentra el capítulo de esbirros y la guía se vuelve inútil a mitad de partida.
const alias = {}
const glosario = docs.find((d) => /glosario/i.test(d.meta.titulo))
if (glosario) {
  const filas = readFileSync(join(DIR, glosario.rel), 'utf8').split('\n').filter((l) => l.trim().startsWith('|'))
  for (const f of filas) {
    const c = f.trim().replace(/^\||\|$/g, '').split('|').map((x) => x.trim().replace(/[*`]/g, ''))
    if (c.length < 2) continue
    const es = sinTildes(c[0]), en = sinTildes(c[1])
    if (!es || !en || es === en || /^-+$/.test(es) || es === 'espanol') continue
    for (const [a, b] of [[es, en], [en, es]]) {
      if (a.split(' ').length > 3) continue
      ;(alias[a] ||= new Set()).add(b)
    }
  }
}
const ALIAS = Object.fromEntries(Object.entries(alias).map(([k, v]) => [k, [...v].sort()]))

const idx = docs.map((d) => ({
  id: d.id, t: d.meta.titulo, c: d.meta.capa,
  s: d.indice.map((x) => ({ id: x.id, t: x.txt })),
  x: sinTildes(d.texto).replace(/\s+/g, ' ').trim(),
}))

const nav = Object.keys(ORDEN).map((capa) => {
  const ds = docs.filter((d) => d.meta.capa === capa)
  if (!ds.length) return ''
  return `<div class="ng"><div class="nt">${esc(NOMBRE[capa])}</div>` +
    ds.map((d) => `<a class="nl" href="#${esc(d.id)}">${esc(d.meta.titulo)}</a>`).join('') + '</div>'
}).join('')

const secciones = docs.map((d) => {
  const [ic, tt] = ENT_ETIQ[d.meta.entitlement] || ENT_ETIQ.base
  return `<section id="${esc(d.id)}" data-rev="${esc(d.meta.revisar_despues)}">
<h1>${esc(d.meta.titulo)}</h1>
<div class="meta"><span class="chip c-${esc(d.meta.capa)}">${esc(NOMBRE[d.meta.capa])}</span><span class="chip">parche ${esc(d.meta.parche)}</span><span class="chip">verificado ${esc(d.meta.verificado)}</span><span class="chip">${ic} ${esc(tt)}</span><span class="cad" hidden>\u26a0 sin revisar desde ${esc(d.meta.revisar_despues)}</span></div>
${d.html}</section>`
}).join('\n')

const CSS = `
:root{--bg:#faf8f5;--fg:#1a1714;--mut:#6b625a;--bd:#e0d9d0;--pa:#8b1a1a;--pa2:#a83232;--sur:#fff;--sur2:#f2ede7;--ok:#1f6b3a;--lk:#7a1f1f;--az:#2f6690;--am:#8a6512;--na:#b3541e}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#141210;--fg:#e8e2da;--mut:#9a9088;--bd:#2e2926;--pa:#c14a4a;--pa2:#d96a6a;--sur:#1c1917;--sur2:#232019;--ok:#4a9d68;--lk:#e39c9c;--az:#7aa8cc;--am:#d0a63c;--na:#e08a4a}}
:root[data-theme=dark]{--bg:#141210;--fg:#e8e2da;--mut:#9a9088;--bd:#2e2926;--pa:#c14a4a;--pa2:#d96a6a;--sur:#1c1917;--sur2:#232019;--ok:#4a9d68;--lk:#e39c9c;--az:#7aa8cc;--am:#d0a63c;--na:#e08a4a}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 ui-serif,Georgia,"Times New Roman",serif;overflow-x:hidden}
a{color:var(--lk)}
.top{position:sticky;top:0;z-index:20;background:var(--sur);border-bottom:1px solid var(--bd);display:flex;gap:.5rem;align-items:center;padding:.5rem .8rem}
.top h2{margin:0;font:600 .82rem/1 ui-sans-serif,system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:var(--pa);white-space:nowrap}
#q{flex:1;min-width:0;padding:.45rem .7rem;border:1px solid var(--bd);border-radius:6px;background:var(--bg);color:var(--fg);font:inherit;font-size:.9rem}
.btn{background:var(--sur2);border:1px solid var(--bd);color:var(--fg);border-radius:6px;padding:.4rem .55rem;cursor:pointer;font:inherit;font-size:.85rem;line-height:1}
.wrap{display:flex;max-width:1180px;margin:0 auto;gap:1.6rem;padding:0 .8rem}
nav{width:232px;flex:none;position:sticky;top:3rem;height:calc(100vh - 3rem);overflow-y:auto;padding:1rem 0 3rem;font-family:ui-sans-serif,system-ui,sans-serif}
.ng{margin-bottom:1.1rem}
.nt{font-size:.66rem;text-transform:uppercase;letter-spacing:.11em;color:var(--mut);padding:0 .5rem .35rem}
.nl{display:block;padding:.3rem .55rem;border-radius:5px;color:var(--fg);text-decoration:none;font-size:.85rem;border-left:2px solid transparent}
.nl:hover{background:var(--sur2)}
.nl.on{border-left-color:var(--pa);color:var(--pa);background:var(--sur2)}
main{flex:1;min-width:0;padding:1.4rem 0 6rem}
section{margin-bottom:3.5rem;scroll-margin-top:3.8rem}
h1{font-size:1.8rem;margin:0 0 .5rem;color:var(--pa);line-height:1.2}
h2{font-size:1.28rem;margin:2.1rem 0 .7rem;padding-bottom:.25rem;border-bottom:1px solid var(--bd);scroll-margin-top:3.8rem}
h3{font-size:1.04rem;margin:1.5rem 0 .5rem;color:var(--pa2)}
.meta{display:flex;flex-wrap:wrap;gap:.3rem;margin-bottom:1.4rem;font-family:ui-sans-serif,system-ui,sans-serif}
.chip{font-size:.68rem;padding:.15rem .5rem;border-radius:99px;background:var(--sur2);border:1px solid var(--bd);color:var(--mut)}
.c-nucleo{border-color:var(--ok);color:var(--ok)}
.cad{font-size:.68rem;padding:.15rem .5rem;border-radius:99px;border:1px solid var(--pa);color:var(--pa)}
.tw{overflow-x:auto;margin:1rem 0;border:1px solid var(--bd);border-radius:7px}
table{border-collapse:collapse;width:100%;font:.86rem/1.5 ui-sans-serif,system-ui,sans-serif}
th,td{padding:.5rem .65rem;text-align:left;border-bottom:1px solid var(--bd);vertical-align:top}
th{background:var(--sur2);font-weight:600;white-space:nowrap}
tr:last-child td{border-bottom:0}
code{background:var(--sur2);padding:.1rem .3rem;border-radius:3px;font:.85em ui-monospace,Menlo,monospace}
pre{background:var(--sur2);padding:.8rem;border-radius:7px;overflow-x:auto;border:1px solid var(--bd)}
pre code{background:none;padding:0}
.ev{margin:1rem 0;border-left:3px solid var(--bd);background:var(--sur);border-radius:0 7px 7px 0;padding:.6rem .85rem}
.ev-h{display:flex;flex-wrap:wrap;gap:.5rem;align-items:center;margin-bottom:.3rem;font-family:ui-sans-serif,system-ui,sans-serif}
.ev-b{font-size:.63rem;text-transform:uppercase;letter-spacing:.08em;font-weight:700;padding:.12rem .45rem;border-radius:3px;background:var(--sur2)}
.ev-f{font:.66rem ui-monospace,monospace;color:var(--mut)}
.ev-oficial{border-left-color:var(--ok)}.ev-oficial .ev-b{color:var(--ok)}
.ev-corroborado{border-left-color:var(--az)}.ev-corroborado .ev-b{color:var(--az)}
.ev-unica{border-left-color:var(--am)}.ev-unica .ev-b{color:var(--am)}
.ev-disputa{border-left-color:var(--na)}.ev-disputa .ev-b{color:var(--na)}
.ev-sinconfirmar{border-left-color:var(--pa)}.ev-sinconfirmar .ev-b{color:var(--pa)}
.bd{margin:1.1rem 0;border:1px solid var(--bd);border-radius:8px;overflow:hidden}
.bd-h{display:flex;flex-wrap:wrap;gap:.5rem;align-items:center;padding:.5rem .8rem;background:var(--sur2);border-bottom:1px solid var(--bd);font-family:ui-sans-serif,system-ui,sans-serif}
.bd-n{font-weight:700;color:var(--pa)}
.bd-e{font-size:.66rem;text-transform:uppercase;letter-spacing:.07em;padding:.1rem .45rem;border-radius:3px;background:var(--bg);border:1px solid var(--bd);color:var(--mut)}
.bd-c{padding:.7rem .8rem}
.ent{font:.68rem ui-sans-serif,system-ui,sans-serif;color:var(--mut);margin-left:auto}
.ps{display:flex;gap:.7rem;margin:.55rem 0;align-items:flex-start}
.ps-n{flex:none;width:1.7rem;height:1.7rem;border-radius:50%;background:var(--pa);color:#fff;display:flex;align-items:center;justify-content:center;font:700 .76rem ui-sans-serif,system-ui,sans-serif}
.ps-opt .ps-n{background:var(--sur2);color:var(--mut);border:1px solid var(--bd)}
.ps-c{padding-top:.1rem}
.ps-o{font-size:.66rem;color:var(--mut);border:1px solid var(--bd);border-radius:3px;padding:.05rem .35rem}
.av{margin:1rem 0;padding:.65rem .85rem;border-radius:7px;border-left:3px solid var(--mut);background:var(--sur)}
.av-peligro{border-left-color:var(--pa)}
.av-truco{border-left-color:var(--ok)}
#res{display:none;padding:1rem 0}
.r{display:block;padding:.55rem .75rem;margin-bottom:.4rem;border:1px solid var(--bd);border-radius:7px;text-decoration:none;color:var(--fg);background:var(--sur)}
.r:hover{border-color:var(--pa)}
.r-c{font:.66rem ui-sans-serif,system-ui,sans-serif;color:var(--mut);text-transform:uppercase;letter-spacing:.07em}
.r-t{font-weight:600;color:var(--pa);font-size:.95rem}
.r-x{font-size:.84rem;color:var(--mut);margin-top:.15rem}
mark{background:#d9a62288;color:inherit;padding:0 .1em;border-radius:2px}
.nada{color:var(--mut);padding:1.5rem 0}
@media(max-width:860px){
nav{display:none;position:fixed;top:3rem;left:0;right:0;width:100%;height:auto;max-height:72vh;background:var(--sur);border-bottom:1px solid var(--bd);padding:.8rem;z-index:15}
nav.open{display:block}
.wrap{padding:0 .7rem}h1{font-size:1.5rem}body{font-size:15px}}
@media(min-width:861px){#menu{display:none}}`

const JS = `
const IDX=__IDX__;
const ALIAS=__ALIAS__;
const CAPA={nucleo:'Fundamentos',version:'Parche',temporada:'Temporada'};
const ND=s=>s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();
const RX=s=>s.replace(/[.*+?^\${}()|[\\]\\\\]/g,'\\\\$&');
const VAR=w=>{const v=[w];for(const a of(ALIAS[w]||[]))v.push(a);
 if(w.length>4){for(const k in ALIAS)if(k.startsWith(w)){v.push(k);for(const a of ALIAS[k])v.push(a)}}
 return [...new Set(v)]};
const q=document.getElementById('q'),res=document.getElementById('res'),doc=document.getElementById('doc');
function buscar(){
 const t=ND(q.value.trim());
 if(t.length<2){res.style.display='none';doc.style.display='';return}
 const ts=t.split(/\\s+/),vs=ts.map(VAR),out=[];
 for(const d of IDX){
  const tit=ND(d.t);
  if(!vs.every(g=>g.some(w=>d.x.includes(w)||tit.includes(w))))continue;
  let p=-1;for(const w of vs[0]){p=d.x.indexOf(w);if(p>=0)break}
  out.push({d,frag:p<0?'':d.x.slice(Math.max(0,p-60),p+120)});
  for(const s of d.s)if(vs.some(g=>g.some(w=>ND(s.t).includes(w))))out.push({d,sub:s});
 }
 if(!out.length){res.innerHTML='<p class="nada">Nada para \\u00ab'+q.value.replace(/[<>&]/g,'')+'\\u00bb.</p>'}
 else{const re=new RegExp('('+vs.flat().map(RX).join('|')+')','gi');
  res.innerHTML=out.slice(0,40).map(o=>'<a class="r" href="#'+(o.sub?o.sub.id:o.d.id)+'">'+
   '<span class="r-c">'+(CAPA[o.d.c]||'')+' \\u00b7 '+o.d.t+'</span>'+
   '<div class="r-t">'+(o.sub?o.sub.t:o.d.t)+'</div>'+
   (o.frag?'<div class="r-x">\\u2026'+o.frag.replace(re,'<mark>$1</mark>')+'\\u2026</div>':'')+'</a>').join('')}
 res.style.display='';doc.style.display='none';
}
q.addEventListener('input',buscar);
res.addEventListener('click',e=>{if(e.target.closest('.r')){q.value='';buscar()}});
const nv=document.getElementById('nav');
document.getElementById('menu').onclick=()=>nv.classList.toggle('open');
nv.addEventListener('click',e=>{if(e.target.closest('.nl'))nv.classList.remove('open')});
document.getElementById('tema').onclick=()=>{const r=document.documentElement;
 const oscuro=r.getAttribute('data-theme')==='dark'||(!r.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme:dark)').matches);
 r.setAttribute('data-theme',oscuro?'light':'dark')};
const HOY=(window.__RELOJ__?new Date(window.__RELOJ__):new Date()).toISOString().slice(0,10);
document.querySelectorAll('section[data-rev]').forEach(s=>{
 const c=s.querySelector('.cad');if(c&&s.dataset.rev&&s.dataset.rev<HOY)c.hidden=false});
const links=[...document.querySelectorAll('.nl')];
const io=new IntersectionObserver(es=>{for(const e of es)if(e.isIntersecting)
 links.forEach(l=>l.classList.toggle('on',l.getAttribute('href')==='#'+e.target.id))},{rootMargin:'-8% 0px -82% 0px'});
document.querySelectorAll('section').forEach(s=>io.observe(s));`

const html = `<title>C\u00f3dice del Nigromante</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Gu\u00eda de Diablo IV para nigromante sin expansiones, en d\u00fao. Parche ${esc(manifiesto.parche_actual)}.">
<style>${CSS}</style>
<div class="top"><button class="btn" id="menu" aria-label="Menu">\u2630</button><h2>C\u00f3dice</h2><input id="q" type="search" placeholder="Buscar\u2026 esbirros, glifo, Tormento" autocomplete="off"><button class="btn" id="tema" aria-label="Tema">\u25d0</button></div>
<div class="wrap"><nav id="nav">${nav}</nav><main><div id="res"></div><div id="doc">${secciones}</div></main></div>
<script>${JS.replace('__IDX__', JSON.stringify(idx)).replace('__ALIAS__', JSON.stringify(ALIAS))}</script>`

writeFileSync(SALIDA, html)
console.log(`  ok  ${docs.length} capitulos -> index.html (${(Buffer.byteLength(html) / 1024).toFixed(0)} KB)`)
for (const c of Object.keys(ORDEN)) {
  const n = docs.filter((d) => d.meta.capa === c).length
  if (n) console.log(`      ${c.padEnd(10)} ${n}`)
}
