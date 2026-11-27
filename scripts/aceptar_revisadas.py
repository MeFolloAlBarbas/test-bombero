"""Pasa al banco preguntas apartadas en tandas/revisar/ cuando el usuario las ha visto.
Uso: python3 scripts/aceptar_revisadas.py 2026-11-27 --ok 901,905 [--quitar 903]
Las aceptadas se añaden como un lote pendiente de esa fecha y se aprueban con aprobar.py; las quitadas se descartan.
Las que no se nombran se quedan esperando en tandas/revisar/.
"""
import json, os, sys, subprocess
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fecha = sys.argv[1]
arg = lambda k: {int(x) for x in sys.argv[sys.argv.index(k) + 1].split(',')} if k in sys.argv else set()
ok, fuera = arg('--ok'), arg('--quitar')
rv = os.path.join(ROOT, 'tandas', 'revisar', fecha + '.json'); d = json.load(open(rv, encoding='utf-8'))
acept = [dict({k: v for k, v in q.items() if k != 'revisar'}) for q in d['preguntas'] if q['id'] in ok]
d['preguntas'] = [q for q in d['preguntas'] if q['id'] not in ok | fuera]
pend = os.path.join(ROOT, 'tandas', 'pendientes', fecha + '-revisadas.json')
json.dump({'preguntas': acept, 'glosario': d.get('glosario', [])}, open(pend, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if d['preguntas']: json.dump(d, open(rv, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
else: os.remove(rv)
sys.exit(subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'aprobar.py'), fecha + '-revisadas']).returncode)
