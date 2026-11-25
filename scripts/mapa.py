"""Mapa de cobertura del temario: qué página de qué manual ha dado cada pregunta, y qué páginas faltan.

Necesita el temario descifrado (TEMARIO_CLAVE=... sh scripts/temario.sh texto /tmp/temario).
- Si una pregunta trae `src` ({"m": "<nombre del manual en temario/>", "p": [páginas del PDF]}), se usa tal cual.
- Si no (preguntas antiguas), se localiza su página buscando en el manual de su tema las palabras más
  características de la respuesta y la explicación (confianza alta / media / baja).
Escribe (solo números de página e ids, nunca texto de los manuales):
- tandas/mapa_preguntas.json  → {id: {"m", "p", "conf"}}
- tandas/mapa_paginas.json    → {manual: {"paginas": N, "con_preguntas": {pág: [ids]}, "sin_preguntas": [págs]}}
Uso: python3 scripts/mapa.py [/tmp/temario]   ·   python3 scripts/mapa.py --resumen   (tabla por manual)
"""
import json, os, re, sys, glob, math, unicodedata, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = next((a for a in sys.argv[1:] if not a.startswith('--')), '/tmp/temario')

# Etiqueta del campo t de las preguntas → manuales del temario donde puede estar el dato (prefijos de nombre)
TEMAS = {
 'Constitución': ['Bloque I - Tema 01'], 'Régimen local': ['Bloque I - Tema 02'], 'Haciendas locales': ['Bloque I - Tema 03'],
 'EBEP': ['Bloque I - Temas 04 y 05'], 'Procedimiento administrativo': ['Bloque I - Tema 06'], 'Igualdad': ['Bloque I - Tema 07'],
 'PRL': ['Bloque I - Tema 08'], 'Incendios de vegetación': ['Bloque II - Tema 05'],
 'Trabajos en altura': ['Bloque II - Temas 06 y 07', 'Bloque II - Tema 23'], 'Tráfico (APRAT)': ['Bloque II - Tema 08', 'Bloque II - Tema 09'],
 'Apícola': ['Bloque II - Tema 10'], 'Edificaciones': ['Bloque II - Tema 11', 'Bloque II - Tema 12', 'Bloque II - Tema 13'],
 'Técnicas de estabilización': ['Bloque II - Tema 14'], 'Accesos forzados': ['Bloque II - Tema 15'], 'Arbolado urbano': ['Bloque II - Tema 16'],
 'NRBQ': ['Bloque II - Tema 17'], 'Electricidad': ['Bloque II - Tema 18'], 'Instalaciones eléctricas': ['Bloque II - Tema 19'],
 'ACS': ['Bloque II - Tema 20'], 'Gas y GLP': ['Bloque II - Tema 21'], 'Agua fría': ['Bloque II - Tema 22'],
 'EPI': ['Bloque II - Tema 24'], 'Estatuto CAM': ['Bloque I - Tema 01'], 'Ascensores': ['Extra - Rescate en ascensores'], 'Corte y soldadura': ['Bloque II - Tema 25'], 'Sanitario (SVB)': ['Bloque II - Tema 26'],
 'Atención sanitaria': ['Bloque II - Tema 27', 'Bloque II - Tema 26', 'Bloque II - Tema 28'],
 'Patología cardiovascular': ['Bloque II - Tema 28'], 'Síntomas clínicos': ['Bloque II - Tema 28'],
 'Reglamento Bomberos': ['Bloque II - Tema 29 - Reglamento'], 'Protección civil': ['Bloque II - Tema 29 - Ley 17'],
 'CTE DB-SI': ['Bloque II - Tema 30', 'Bloque II - Tema 31'], 'Vehículos': ['Bloque II - Tema 32'],
 # Ascensores no está en las bases: su manual va como «Extra»
}
VACIAS = set('''a al algo ante como con contra cual cuando de del desde donde el ella en entre es esa ese esta este
esto fue ha han hasta hay la las le les lo los mas muy no o otra otro para pero por que quien se segun ser si sin
sobre son su sus tambien tiene un una uno unos y ya debe deben puede pueden cada solo porque cuanto mas menos
siempre nunca todo todos toda todas tanto hace hacer queda esto eso asi bien'''.split())

def norm(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    t = unicodedata.normalize('NFKD', t.lower())
    t = ''.join(c for c in t if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', ' ', t)

def toks(t): return [w for w in norm(t).split() if (len(w) > 3 and w not in VACIAS) or (w.isdigit() and len(w) > 1)]

def cargar():
    man = {}
    for f in sorted(glob.glob(os.path.join(DIR, '*.txt'))):
        n = os.path.basename(f)[:-4]
        partes = re.split(r'\n=== Página (\d+) del PDF ===\n', open(f, encoding='utf-8').read())
        pags = {int(partes[i]): partes[i + 1] for i in range(1, len(partes) - 1, 2)}
        man[n] = {p: collections.Counter(toks(t)) for p, t in pags.items()}
    return man

def preguntas():
    Q = json.load(open(os.path.join(ROOT, 'preguntas.json'), encoding='utf-8'))
    for f in sorted(glob.glob(os.path.join(ROOT, 'tandas', 'pendientes', '*.json'))):
        Q += [dict(q, _pend=1) for q in json.load(open(f, encoding='utf-8'))['preguntas']]
    return Q

def localizar(q, man, df, npag):
    cands = [m for m in man for pre in TEMAS.get(q['t'], []) if m.startswith(pre)]
    if not cands: return None
    clave = toks(q['o'][q['c']]) * 3 + toks(q.get('que', '')) * 2 + toks(q.get('porque', '')) + toks(q.get('rec', '')) + toks(q['q'])
    pesos = collections.Counter(clave)
    mejor = (0, None, None); seg = 0
    for m in cands:
        for p, cnt in man[m].items():
            s = sum(w * math.log(npag / (1 + df[t])) for t, w in pesos.items() if t in cnt)
            if s > mejor[0]: seg = mejor[0]; mejor = (s, m, p)
            elif s > seg: seg = s
    if not mejor[1]: return None
    conf = 'alta' if mejor[0] > 25 and mejor[0] > 1.3 * seg else 'media' if mejor[0] > 12 else 'baja'
    return {'m': mejor[1], 'p': [mejor[2]], 'conf': conf}

def main():
    man = cargar()
    if not man: sys.exit(f'No hay temario descifrado en {DIR}')
    df = collections.Counter(t for m in man.values() for cnt in m.values() for t in cnt)
    npag = sum(len(m) for m in man.values())
    mapa = {}
    for q in preguntas():
        if q.get('src') and q['src'].get('m') in man:
            r = {'m': q['src']['m'], 'p': q['src'].get('p') or [], 'conf': 'src'}
        else:
            r = localizar(q, man, df, npag) or {'m': None, 'p': [], 'conf': 'sin manual'}
        if q.get('_pend'): r['pendiente'] = 1
        mapa[str(q['id'])] = r
    pags = {}
    for m, ps in man.items():
        con = collections.defaultdict(list)
        for i, r in mapa.items():
            if r['m'] == m and r['conf'] != 'baja':
                for p in r['p']: con[p].append(int(i))
        vacias = [p for p in sorted(ps) if p not in con and sum(ps[p].values()) > 40]  # ignora portadas/páginas casi vacías
        pags[m] = {'paginas': len(ps), 'con_preguntas': {str(p): v for p, v in sorted(con.items())}, 'sin_preguntas': vacias}
    json.dump(mapa, open(os.path.join(ROOT, 'tandas', 'mapa_preguntas.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    json.dump(pags, open(os.path.join(ROOT, 'tandas', 'mapa_paginas.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    c = collections.Counter(r['conf'] for r in mapa.values())
    print(f'{len(mapa)} preguntas localizadas: ' + ', '.join(f'{k} {v}' for k, v in c.most_common()))
    if '--resumen' in sys.argv or True:
        print(f'{"manual":70} págs  con  sin')
        for m, d in pags.items():
            print(f'{m[:70]:70} {d["paginas"]:4} {len(d["con_preguntas"]):4} {len(d["sin_preguntas"]):4}')

if __name__ == '__main__':
    main()
