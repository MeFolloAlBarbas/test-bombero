"""Genera / amplía plan.json: qué pregunta sale cada día y hora.

Reglas:
- Una pregunta NUNCA se repite (ni en el plan ni con las ya usadas el 20/11/2026).
- 12 preguntas por día (9:00-20:00), de lunes a sábado; los domingos no hay.
- En un mismo día no se repite tema.
- La de las 20:00 es siempre "difícil".
- La 13.ª (extra de deducir de las 20:00, `ded: 1`) la pone después scripts/deduccion.py.
- Los días ya planificados no se tocan; solo se añaden días nuevos al final.
- Si no quedan preguntas suficientes para un día completo, el plan se detiene ahí.
- Las preguntas de intervención (int=1) no se usan aquí: las coloca scripts/intervencion.py
  (una al día, a hora aleatoria). Ejecutar después: python3 scripts/intervencion.py
- Solo planifica hasta HORIZONTE días por delante de hoy (21 por defecto; --hasta AAAA-MM-DD para otro
  límite). Las preguntas que sobran se quedan en el banco, sin día, para cuando haya más por hora.
Uso: python3 scripts/plan.py [--hasta AAAA-MM-DD]
"""
import json, random, datetime as dt, os, sys
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANK = json.load(open(os.path.join(ROOT, 'preguntas.json'), encoding='utf-8'))
PLAN_F = os.path.join(ROOT, 'plan.json')
INICIO = dt.date(2026, 11, 21)
YA_USADAS_ANTES = {1, 7, 11, 12, 13, 15, 16, 20, 22, 26, 33, 34, 36, 38, 39,  # preguntas del 20/11/2026
                   71,  # 23/11 19:00: la vio casi todo el mundo (el plan se cambió a la 293)
                   # 26/11: salían en el 20/11 calculado con el banco (cambiaba al crecer) y alguien pudo verlas
                   17, 62, 70, 76, 85, 93, 94, 111, 136, 137, 158, 228, 265, 332}

HOY = dt.datetime.now(ZoneInfo('Europe/Madrid')).date()
HORIZONTE = 21
HASTA = dt.date.fromisoformat(sys.argv[sys.argv.index('--hasta') + 1]) if '--hasta' in sys.argv else HOY + dt.timedelta(days=HORIZONTE)

plan = json.load(open(PLAN_F, encoding='utf-8')) if os.path.exists(PLAN_F) else {}
usadas = set(YA_USADAS_ANTES) | {i for ids in plan.values() for i in ids}
libres = [q for q in sorted(BANK, key=lambda q: q['id']) if q['id'] not in usadas and not q.get('ded')]  # ded: hueco extra de las 20:00

dia = max([dt.date.fromisoformat(k) for k in plan] + [INICIO - dt.timedelta(days=1)]) + dt.timedelta(days=1)
nuevos = 0
while dia <= HASTA:
    if dia.weekday() == 6:  # domingo
        dia += dt.timedelta(days=1); continue
    dificiles = [q for q in libres if q['d'] == 'difícil']
    if not dificiles:
        break
    dura = dificiles[0]
    normales = [q for q in libres if q['d'] != 'difícil' and not q.get('int') and not q.get('ex') and q['t'] != dura['t']]
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
