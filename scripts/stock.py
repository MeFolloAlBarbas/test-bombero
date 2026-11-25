"""Cuántas preguntas SIN USAR (que aún no están en plan.json) quedan de cada tema, sumando el lote de hoy.
Las tareas nocturnas eligen el tema con MENOS (y su manual en tandas/cobertura.json).
Uso: python3 scripts/stock.py [AAAA-MM-DD]   (fecha del lote de hoy; por defecto, hoy en Madrid)
"""
import json, os, sys, collections, datetime
from zoneinfo import ZoneInfo
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
hoy = sys.argv[1] if len(sys.argv) > 1 else datetime.datetime.now(ZoneInfo('Europe/Madrid')).strftime('%Y-%m-%d')
P = json.load(open(os.path.join(ROOT, 'preguntas.json'), encoding='utf-8'))
F = json.load(open(os.path.join(ROOT, 'plan.json'), encoding='utf-8'))
usadas = {i for v in F.values() for i in v}
lote_f = os.path.join(ROOT, 'tandas', 'pendientes', hoy + '.json')
lote = json.load(open(lote_f, encoding='utf-8'))['preguntas'] if os.path.exists(lote_f) else []
libres = collections.Counter(q['t'] for q in P if q['id'] not in usadas)
enlote = collections.Counter(q['t'] for q in lote)
cob = json.load(open(os.path.join(ROOT, 'tandas', 'cobertura.json'), encoding='utf-8'))['manuales']
temas = set(q['t'] for q in P) | set(enlote)
ALIAS = {'Síntomas clínicos': ['DOC-20240402-WA0043..pdf'], 'Patología cardiovascular': ['DOC-20240402-WA0043..pdf'],
         'Electricidad': ['2.18. Conceptos básicos de electricidad 1.pdf'],
         'Ascensores': ['(manual NO está en el proyecto: no se pueden hacer más)'],
         'Arbolado urbano': ['(PDF solo en el chat, no en el proyecto: las tareas nocturnas lo saltan)']}
def manuales(t):
    if t in ALIAS: return ALIAS[t]
    return [m for m, v in cob.items() if t.lower().split(' (')[0] in v['tema'].lower()]
print(f'Calendario hasta {max(F)}. Lote de hoy ({hoy}): {len(lote)} preguntas.')
print('sin usar + lote hoy = total · tema · manuales con ese tema en cobertura.json')
for t in sorted(temas, key=lambda t: (libres[t] + enlote[t], t)):
    man = manuales(t)
    print(f'{libres[t]:3} + {enlote[t]:3} = {libres[t] + enlote[t]:3} · {t} · {" | ".join(man) or "?"}')
con = {m for t in temas for m in manuales(t)}
sin = [m for m in cob if m not in con]
if sin: print('Manuales sin ninguna pregunta todavía (prioridad máxima):', ' | '.join(sin))
