"""Comprueba que los metodos nuevos no invocan nombres inexistentes.
Es el fallo que dejo el capturador muerto (T.Image): compila, revienta al correr.
"""
import ast, sys, builtins
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import tracker as T, valorar as V

src = open(Path(__file__).resolve().parent.parent / 'tracker.py', encoding='utf-8').read()
arbol = ast.parse(src)
globales = set(dir(T)) | set(dir(builtins))
malos = []
for nodo in ast.walk(arbol):
    if not isinstance(nodo, ast.FunctionDef):
        continue
    if nodo.name not in ("leer_ficha", "_bucle_ficha", "_fin_ficha", "reflujo",
                         "_captura_limpia", "_vigilar_geometria", "monitor_activo",
                         "capturar", "pantalla", "agrupar", "identificar"):
        continue
    locales = {a.arg for a in nodo.args.args}
    for n in ast.walk(nodo):
        if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store):
            locales.add(n.id)
        if isinstance(n, ast.ExceptHandler) and n.name:
            locales.add(n.name)
        if isinstance(n, ast.comprehension):
            for t in ast.walk(n.target):
                if isinstance(t, ast.Name):
                    locales.add(t.id)
        if isinstance(n, (ast.Lambda, ast.FunctionDef)):
            for a in n.args.args:
                locales.add(a.arg)
        if isinstance(n, (ast.Import, ast.ImportFrom)):
            for a in n.names:
                locales.add((a.asname or a.name).split('.')[0])
    for n in ast.walk(nodo):
        if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load):
            if n.id not in locales and n.id not in globales:
                malos.append(f"{nodo.name}: nombre suelto '{n.id}'")
        if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name):
            base = n.value.id
            if base == 'V' and not hasattr(V, n.attr):
                malos.append(f"{nodo.name}: V.{n.attr} NO existe")
            if base == 'T' and not hasattr(T, n.attr):
                malos.append(f"{nodo.name}: T.{n.attr} NO existe")
for m in sorted(set(malos)):
    print("  MAL ", m)
print(f"  {'PASA' if not malos else 'FALLA'}  ({len(set(malos))} problemas)")
sys.exit(1 if malos else 0)
