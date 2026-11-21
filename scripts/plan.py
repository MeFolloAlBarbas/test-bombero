"""Genera / amplía plan.json: qué pregunta sale cada día y hora.

Reglas:
- Una pregunta NUNCA se repite (ni en el plan ni con las ya usadas el 20/11/2026).
- 12 preguntas por día (9:00-20:00), de lunes a sábado; los domingos no hay.
- En un mismo día no se repite tema.
- La de las 20:00 es siempre "difícil".
- Los días ya planificados no se tocan; solo se añaden días nuevos al final.
- Si no quedan preguntas suficientes para un día completo, el plan se detiene ahí.
- Las preguntas de intervención (int=1) no se usan aquí: las coloca scripts/intervencion.py
  (una al día, a hora aleatoria). Ejecutar después: python3 scripts/intervencion.py
Uso: python3 scripts/plan.py
"""
import json, random, datetime as dt, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANK = json.load(open(os.path.join(ROOT, 'preguntas.json'), encoding='utf-8'))
PLAN_F = os.path.join(ROOT, 'plan.json')
INICIO = dt.date(2026, 11, 21)
YA_USADAS_ANTES = {1, 7, 11, 12, 13, 15, 16, 20, 22, 26, 33, 34, 36, 38, 39}  # preguntas del 20/11/2026

plan = json.load(open(PLAN_F, encoding='utf-8')) if os.path.exists(PLAN_F) else {}
usadas = set(YA_USADAS_ANTES) | {i for ids in plan.values() for i in ids}
libres = [q for q in sorted(BANK, key=lambda q: q['id']) if q['id'] not in usadas]

dia = max([dt.date.fromisoformat(k) for k in plan] + [INICIO - dt.timedelta(days=1)]) + dt.timedelta(days=1)
nuevos = 0
while True:
    if dia.weekday() == 6:  # domingo
        dia += dt.timedelta(days=1); continue
    dificiles = [q for q in libres if q['d'] == 'difícil']
    if not dificiles:
        break
    dura = dificiles[0]
    normales = [q for q in libres if q['d'] != 'difícil' and not q.get('int') and q['t'] != dura['t']]
    por_tema = {}
    for q in normales:
        por_tema.setdefault(q['t'], []).append(q)
    if len(por_tema) < 11:
        break
    rnd = random.Random(dia.isoformat())
    temas = sorted(por_tema, key=lambda t: (-len(por_tema[t]), rnd.random()))[:11]
    elegidas = [por_tema[t][0] for t in temas]
    rnd.shuffle(elegidas)
    ids = [q['id'] for q in elegidas] + [dura['id']]
    plan[dia.isoformat()] = ids
    usadas |= set(ids)
    libres = [q for q in libres if q['id'] not in usadas]
    nuevos += 1
    dia += dt.timedelta(days=1)

open(PLAN_F, 'w', encoding='utf-8').write(json.dumps(dict(sorted(plan.items())), ensure_ascii=False, indent=0))
ultimo = max(plan) if plan else '—'
print(f'Días añadidos: {nuevos} · plan hasta: {ultimo} · preguntas sin usar: {len(libres)} '
      f'(difíciles: {sum(1 for q in libres if q["d"]=="difícil")})')
