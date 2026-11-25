"""Comprueba que ninguna pregunta sale dos veces en el calendario (plan.json), ni las ya usadas
antes del plan (YA_USADAS_ANTES de plan.py). Termina con error si encuentra alguna.
Lo ejecuta scripts/calendario.sh al final. Uso: python3 scripts/sin_repetir.py"""
import json, os, re, sys, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
plan = json.load(open(os.path.join(ROOT, 'plan.json'), encoding='utf-8'))
txt = open(os.path.join(ROOT, 'scripts', 'plan.py'), encoding='utf-8').read()
m = re.search(r'YA_USADAS_ANTES = \{([^}]*)\}', txt, re.S)
antes = {int(x) for x in re.findall(r'\d+', re.sub(r'#.*', '', m.group(1)))} if m else set()
c = collections.Counter(i for ids in plan.values() for i in ids)
despues = {i for d, ids in plan.items() if d > '2026-11-20' for i in ids}  # el 20/11 está en el plan y en YA_USADAS_ANTES
rep = sorted(i for i, n in c.items() if n > 1) + sorted(antes & despues)
if rep:
    sys.exit(f'¡PREGUNTAS REPETIDAS en el calendario!: {rep}')
print(f'Sin repeticiones: {len(c)} preguntas en {len(plan)} días.')
