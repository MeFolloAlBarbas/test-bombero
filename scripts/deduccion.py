"""Pone la pregunta EXTRA de deducir de las 20:00 (13.ª del día) en los días futuros del calendario.
- Solo días posteriores a hoy (Madrid) que tengan 12 preguntas; nunca toca hoy ni días pasados.
- Usa preguntas aprobadas con `ded: 1` que no hayan salido nunca (ni en YA_USADAS_ANTES), con un tema que no esté ya ese día.
- Si no quedan, esos días se quedan con 12 (la web solo enseña la extra cuando existe).
"""
import json, os, re, datetime as dt
from zoneinfo import ZoneInfo
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Interruptor del usuario (28/11): la extra de las 20:00 NO se activa hasta que él lo diga → tandas/estado.json "extra_20h": true
if not json.load(open(os.path.join(ROOT, 'tandas', 'estado.json'), encoding='utf-8')).get('extra_20h'):
    print('Pregunta extra de las 20:00 desactivada (extra_20h = false en tandas/estado.json): no se añade ninguna.')
    raise SystemExit(0)
P = os.path.join(ROOT, 'plan.json')
plan = json.load(open(P, encoding='utf-8')); B = {q['id']: q for q in json.load(open(os.path.join(ROOT, 'preguntas.json'), encoding='utf-8'))}
t = open(os.path.join(ROOT, 'scripts', 'plan.py'), encoding='utf-8').read()
antes = {int(x) for x in re.findall(r'\d+', re.sub(r'#.*', '', re.search(r'YA_USADAS_ANTES = \{([^}]*)\}', t, re.S).group(1)))}
usadas = {i for ids in plan.values() for i in ids} | antes
libres = [q for q in sorted(B.values(), key=lambda q: q['id']) if q.get('ded') and q['id'] not in usadas]
hoy = dt.datetime.now(ZoneInfo('Europe/Madrid')).date().isoformat()
n = 0
for d in sorted(plan):
    if d <= hoy or len(plan[d]) != 12: continue
    temas = {B[i]['t'] for i in plan[d] if i in B}
    q = next((q for q in libres if q['t'] not in temas), None)
    if not q: continue
    plan[d].append(q['id']); libres.remove(q); n += 1
open(P, 'w', encoding='utf-8').write(json.dumps(plan, ensure_ascii=False, indent=0) + '\n')
print(f'Preguntas de deducir (20:00 extra) añadidas: {n} · quedan sin usar: {len(libres)}')
