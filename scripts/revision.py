"""Crea tandas/revision/AAAA-MM-DD.md para que el usuario supervise el lote antes de darle el visto bueno.

- Muestra: unas 10 preguntas completas, de temas y tipos distintos (cifras, concepto, examen, intervención,
  dibujo, difícil), con la correcta marcada y toda la explicación.
- Aparte, TODAS las de Edificaciones y Técnicas de estabilización: necesitan el visto bueno una a una.
- Al final, la lista completa en forma de tarjeta (pregunta corta → respuesta corta).
Uso: python3 scripts/revision.py 2026-11-25 [--muestra 10]
"""
import json, os, re, sys, random
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fecha = sys.argv[1]
N = int(sys.argv[sys.argv.index('--muestra') + 1]) if '--muestra' in sys.argv else 10
lote = json.load(open(os.path.join(ROOT, 'tandas', 'pendientes', fecha + '.json'), encoding='utf-8'))
Q = lote['preguntas']
DELICADOS = ('edificaci', 'estabiliza')
delicada = lambda q: any(k in q['t'].lower() for k in DELICADOS)

def tipo(q):
    if q.get('d') == 'difícil': return 'difícil'
    for k, n in (('int', 'intervención'), ('ex', 'estilo examen'), ('dib', 'dibujo'), ('cifra', 'cifra')):
        if q.get(k): return n
    return 'concepto'

def md(t): return re.sub(r'</?mark>', '**', re.sub(r'<(?!/?mark)[^>]+>', '', t or ''))

def ficha(q):
    L = [f'### #{q["id"]} · {q["t"]} · {tipo(q)}', '', md(q['q']), '']
    for k, o in enumerate(q['o']):
        L.append(f'- {"✅" if k == q["c"] else "▫️"} {md(o)}')
    L.append(f'- ▫️ *(4.ª opción, solo con Chulito)* {md(q.get("o4", ""))}')
    L += ['', f'**Qué es:** {md(q["que"])}', '', f'**Por qué:** {md(q["porque"])}', '',
          f'**Ojo:** {md(q["ojo"])}', '', f'**Para recordar:** {md(q["rec"])}', '', f'*Fuente: {q["f"]}*', '']
    return L

normales = [q for q in Q if not delicada(q)]
rnd = random.Random(fecha)
grupos = {}
for q in normales: grupos.setdefault(tipo(q), []).append(q)
for g in grupos.values(): rnd.shuffle(g)
muestra, temas = [], set()
while len(muestra) < min(N, len(normales)):
    avanzo = False
    for g in grupos.values():
        for q in g:
            if q in muestra or (q['t'] in temas and len(temas) < len({x['t'] for x in normales})): continue
            muestra.append(q); temas.add(q['t']); avanzo = True; break
        if len(muestra) >= N: break
    if not avanzo:
        resto = [q for q in normales if q not in muestra]
        if not resto: break
        muestra.append(resto[0])

L = [f'# Revisión del lote del {fecha}', '',
     f'{len(Q)} preguntas nuevas, ids {min(q["id"] for q in Q)}-{max(q["id"] for q in Q)}. '
     'No están en la web: entran cuando des el visto bueno, y hasta entonces no se hace el lote siguiente.', '',
     'Para responder, abre una conversación en el proyecto y di: «visto bueno al lote del ' + fecha + '», '
     'o di qué preguntas quitar o cambiar y por qué.', '', f'## Muestra ({len(muestra)} preguntas)', '']
for q in muestra: L += ficha(q)
dl = [q for q in Q if delicada(q)]
if dl:
    L += ['## Edificaciones y Técnicas de estabilización (revisar una a una)', '',
          'Estos manuales tienen datos mal: cada una explica cómo es realmente y cómo lo pone el temario.', '']
    for q in dl: L += ficha(q)
L += ['## Lote completo (tarjetas)', '']
for q in Q: L.append(f'- **#{q["id"]}** {q["t"]} · {tipo(q)} — {md(q["tq"])} → {md(q["ta"])}')
out = os.path.join(ROOT, 'tandas', 'revision', fecha + '.md')
open(out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print(out)
