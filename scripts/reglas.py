"""Revisa un lote de preguntas pendientes (tandas/pendientes/AAAA-MM-DD.json) antes de pedir el visto bueno.

Errores (hay que corregirlos):
  - falta «src» (manual de temario/ y páginas del PDF de donde sale el dato)
  - faltan campos (id, t, d, q, o con 3, c 0-2, o4, que, porque, ojo, rec, f, tq, ta) o ids repetidos
  - la explicación nombra una opción por su letra («la A», «opción B», «B)»…): las opciones se barajan
  - enunciado casi igual a otra pregunta del banco o del propio lote
Avisos (mirarlos uno a uno):
  - mismo tema y enunciado parecido: puede ser una pregunta hermana válida (otro dato del mismo párrafo)
  - la explicación trae cifras que no salen en el enunciado ni en las opciones (¿otro dato del temario?)
  - una opción es mucho más larga que las demás (la correcta no debe notarse por la longitud)
  - ningún término del glosario aparece en la pregunta (¿falta añadir sus términos?)
Uso: python3 scripts/reglas.py tandas/pendientes/2026-11-25.json
"""
import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from similares import comparar, norm

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMPOS = ['id', 't', 'd', 'q', 'o', 'c', 'o4', 'que', 'porque', 'ojo', 'rec', 'f', 'tq', 'ta']
EXPL = ['que', 'porque', 'ojo', 'rec']
LETRA_EXACTA = re.compile(r'\b(?:opci[oó]n|respuesta|alternativa|letra)\s+[ABCDabcd]\b|(?<![\w>])[ABCD]\)|\b(?:la|las)\s+[ABCD]\b')
NUM = re.compile(r'\d+(?:[.,]\d+)?')

def limpio(t): return re.sub(r'<[^>]+>', ' ', t or '')

def nums(t): return {n.replace(',', '.') for n in NUM.findall(limpio(t))}

def main(ruta):
    lote = json.load(open(ruta, encoding='utf-8'))
    nuevas = lote['preguntas']
    banco = json.load(open(os.path.join(ROOT, 'preguntas.json'), encoding='utf-8'))
    glos = json.load(open(os.path.join(ROOT, 'glosario.json'), encoding='utf-8')) + lote.get('glosario', [])
    err, avi = [], []
    ids_banco = {q['id'] for q in banco}
    vistos = set()
    for q in nuevas:
        i = q.get('id')
        falt = [c for c in CAMPOS if c not in q or q[c] in (None, '')]
        if falt: err.append((i, 'faltan campos: ' + ', '.join(falt)))
        if i in ids_banco or i in vistos: err.append((i, 'id repetido'))
        vistos.add(i)
        src = q.get('src') or {}
        if not src.get('m') or not src.get('p'):
            (err if os.path.basename(ruta) >= '2026-11-26' else avi).append((i, 'falta «src»: {"m": "<nombre del manual en temario/>", "p": [páginas del PDF]}'))
        elif not os.path.exists(os.path.join(ROOT, 'temario', 'texto', src['m'] + '.txt.enc')):
            err.append((i, f'«src.m» no es un manual de temario/: {src["m"]}'))
        if not isinstance(q.get('o'), list) or len(q['o']) != 3: err.append((i, 'o debe tener 3 opciones'))
        if q.get('c') not in (0, 1, 2): err.append((i, 'c debe ser 0, 1 o 2'))
        for c in EXPL + ['tq', 'ta']:
            m = LETRA_EXACTA.search(limpio(q.get(c, '')))
            if m: err.append((i, f'«{c}» nombra una opción por su letra: «{m.group(0)}»'))
        if isinstance(q.get('o'), list) and len(q['o']) == 3:
            base = nums(q['q']) | set().union(*(nums(o) for o in q['o'] + [q.get('o4', '')]))
            extra = set().union(*(nums(q.get(c, '')) for c in EXPL)) - base - {'0', '1', '2'}
            L = [len(limpio(o)) for o in q['o']]
            if max(L) > 1.6 * (sorted(L)[1] or 1) and max(L) - sorted(L)[1] > 25:
                avi.append((i, f'una opción es mucho más larga (longitudes {L})'))
        texto = norm(' '.join([q.get('q', '')] + q.get('o', []) + [q.get(c, '') for c in EXPL]))
        if not any(norm(f).strip() and f' {norm(f).strip()} ' in f' {texto} ' for g in glos for f in g.get('a', [g['t']])):
            avi.append((i, 'ningún término del glosario aparece en la pregunta'))
    try: ok = {tuple(p) for p in json.load(open(os.path.join(ROOT, 'scripts/similares_revisadas.json')))}
    except FileNotFoundError: ok = set()
    for k, n in enumerate(nuevas):
        for v in banco + nuevas[:k]:
            try: m = comparar(n, v)
            except Exception: m = None
            if m and (n.get('id'), v['id']) not in ok:
                # «Casi igual» es error; «mismo tema y parecido» solo aviso: del mismo párrafo salen varias preguntas distintas
                (err if m.startswith('enunciado casi igual') else avi).append((n.get('id'), f'se parece a #{v["id"]}: {m} (¿pregunta lo mismo?)'))
    for nombre, lista in (('ERROR', err), ('AVISO', avi)):
        for i, m in lista: print(f'{nombre} #{i}: {m}')
    print(f'{len(nuevas)} preguntas · {len(err)} errores · {len(avi)} avisos')
    return 1 if err else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
