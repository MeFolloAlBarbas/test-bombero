"""Comprueba que ninguna pregunta sale dos veces en el calendario (plan.json), ni las ya usadas
antes del plan (YA_USADAS_ANTES de plan.py), y que NO se ha cambiado ningún día de hoy o anterior
(alguien ya pudo ver esas preguntas: lo que pasó el 23/11 con la 71). Termina con error si falla algo.
Lo ejecuta scripts/calendario.sh al final. Uso: python3 scripts/sin_repetir.py"""
import json, os, re, sys, collections, subprocess, datetime as dt
from zoneinfo import ZoneInfo
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
plan = json.load(open(os.path.join(ROOT, 'plan.json'), encoding='utf-8'))
txt = open(os.path.join(ROOT, 'scripts', 'plan.py'), encoding='utf-8').read()
m = re.search(r'YA_USADAS_ANTES = \{([^}]*)\}', txt, re.S)
antes = {int(x) for x in re.findall(r'\d+', re.sub(r'#.*', '', m.group(1)))} if m else set()
c = collections.Counter(i for ids in plan.values() for i in ids)
despues = {i for d, ids in plan.items() if d > '2026-11-20' for i in ids}  # el 20/11 está en el plan y en YA_USADAS_ANTES
rep = sorted(i for i, n in c.items() if n > 1) + sorted(antes & despues)
hoy = dt.datetime.now(ZoneInfo('Europe/Madrid')).date().isoformat()
try:
    viejo = json.loads(subprocess.run(['git', '-C', ROOT, 'show', 'HEAD:plan.json'], capture_output=True, text=True, check=True).stdout)
except Exception:
    viejo = {}
tocados = [d for d in viejo if d <= hoy and viejo[d] != plan.get(d)]
if tocados:
    sys.exit(f'¡Se han cambiado días que ya pudieron verse (hoy o antes)!: {tocados}. Deshaz el cambio en plan.json.')
if rep:
    sys.exit(f'¡PREGUNTAS REPETIDAS en el calendario!: {rep}')
print(f'Sin repeticiones: {len(c)} preguntas en {len(plan)} días.')
