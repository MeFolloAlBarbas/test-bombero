"""Comprueba que una pregunta nueva no repite otra del banco.

Compara el enunciado y la respuesta correcta de cada pregunta nueva con todas
las anteriores. Avisa si:
  - los enunciados se parecen mucho (mismas palabras clave), o
  - preguntan lo mismo con otras palabras: misma respuesta correcta, mismo
    tema y enunciados parecidos.

Las parejas ya revisadas a mano (parecidas pero distintas) se apuntan en
scripts/similares_revisadas.json como [nueva, vieja].

Uso:
  python3 scripts/similares.py            # revisa todo el banco
  python3 scripts/similares.py --desde 145  # solo las preguntas con id >= 145
"""
import json, re, sys, unicodedata
from difflib import SequenceMatcher

VACIAS = set("""a al algo ante bajo como con contra cual cuales cuando de del desde donde
dos el ella ellos en entre era es esa ese esta este esto estos fue ha han hasta hay la
las le les lo los mas me mi muy no o otra otro para pero por que quien se segun ser si
sin sobre son su sus tambien te tiene tienen todo todos tu un una uno unos y ya cual
cuál debe deben puede pueden siguiente siguientes art articulo ley manual segun
correcta incorrecta verdadera falsa afirmacion""".split())

def norm(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    t = unicodedata.normalize('NFKD', t.lower())
    t = ''.join(c for c in t if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9 ]+', ' ', t)

def claves(t):
    return {w for w in norm(t).split() if w not in VACIAS and len(w) > 2 or w.isdigit()}

def jaccard(a, b):
    return len(a & b) / len(a | b) if a and b else 0.0

def comparar(n, v):
    """Devuelve el motivo si n (nueva) repite v (vieja); None si no."""
    qa, qb = claves(n['q']), claves(v['q'])
    j = jaccard(qa, qb)
    r = SequenceMatcher(None, norm(n['q']), norm(v['q'])).ratio()
    if j >= 0.6 or r >= 0.8:
        return f'enunciado casi igual (palabras {j:.0%}, texto {r:.0%})'
    ca, cb = norm(n['o'][n['c']]).strip(), norm(v['o'][v['c']]).strip()
    mismo_tema = n.get('t') == v.get('t')
    if mismo_tema and ca == cb and len(ca) > 3 and j >= 0.3:
        return f'misma respuesta y mismo tema con enunciado parecido ({j:.0%})'
    if mismo_tema and j >= 0.45:
        return f'mismo tema y enunciado muy parecido ({j:.0%})'
    return None

def revisar(nuevas, banco):
    fallos = []
    for n in nuevas:
        for v in banco:
            if v['id'] >= n['id']:
                continue
            m = comparar(n, v)
            if m:
                fallos.append((n['id'], v['id'], m))
    return fallos

if __name__ == '__main__':
    Q = json.load(open('preguntas.json', encoding='utf-8'))
    desde = int(sys.argv[sys.argv.index('--desde') + 1]) if '--desde' in sys.argv else 0
    nuevas = [q for q in Q if q['id'] >= desde]
    try: ok = {tuple(p) for p in json.load(open('scripts/similares_revisadas.json'))}
    except FileNotFoundError: ok = set()
    f = [x for x in revisar(nuevas, Q) if (x[0], x[1]) not in ok]
    byid = {q['id']: q for q in Q}
    for a, b, m in f:
        print(f'#{a} se parece a #{b}: {m}\n   NUEVA: {byid[a]["q"]}\n   VIEJA: {byid[b]["q"]}')
    print(f'{len(nuevas)} revisadas, {len(f)} posibles repeticiones')
    sys.exit(1 if f else 0)
