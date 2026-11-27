"""Mete 2 preguntas «estilo examen» (ex=1) por día en los días futuros de plan.json.

- Solo días posteriores a hoy (Madrid) que aún no tengan ninguna. Nunca sustituye a la de las 20:00,
  ni a la de intervención (int) ni a la del dibujo (dib).
- «No repetir tema en el día»: si el tema ya está como normal, la sustituye; si está en una de las
  protegidas, prueba con la siguiente pregunta libre. Las dos del día son de temas distintos.
- La pregunta sustituida vuelve a quedar sin usar. Uso: python3 scripts/examen.py
"""
import json, os, random, datetime as dt
from zoneinfo import ZoneInfo
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B={q['id']:q for q in json.load(open(os.path.join(ROOT,'preguntas.json'),encoding='utf-8'))}
PF=os.path.join(ROOT,'plan.json');plan=json.load(open(PF,encoding='utf-8'))
hoy=dt.datetime.now(ZoneInfo('Europe/Madrid')).date().isoformat()
POR_DIA=2
usadas={i for ids in plan.values() for i in ids}
import os as _os,re as _re  # también las ya vistas antes del calendario (YA_USADAS_ANTES de plan.py)
_t=open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),'plan.py'),encoding='utf-8').read()
usadas|={int(x) for x in _re.findall(r'\d+',_re.sub(r'#.*','',_re.search(r'YA_USADAS_ANTES = \{([^}]*)\}',_t,_re.S).group(1)))}
libres=[q for q in sorted(B.values(),key=lambda q:q['id']) if q.get('ex') and q['id'] not in usadas and not q.get('ded')]
prot=lambda q:q.get('int') or q.get('dib')
n=0
for d in sorted(plan):
    ids=plan[d]
    if d<=hoy or any(B[i].get('ex') for i in ids): continue
    puestas=0
    for nq in list(libres):
        if puestas==POR_DIA: break
        temas={B[i]['t']:j for j,i in enumerate(ids)}
        j=temas.get(nq['t'])
        if j is not None and (j==11 or prot(B[ids[j]]) or B[ids[j]].get('ex')): continue
        if j is None:
            cand=[k for k in range(11) if not prot(B[ids[k]]) and not B[ids[k]].get('ex')]
            j=random.Random(f'ex-{d}-{puestas}').choice(cand)
        ids[j]=nq['id'];libres.remove(nq);puestas+=1;n+=1;print(d,f'{9+j}:00',nq['id'],nq['t'])
    if not libres: break
open(PF,'w',encoding='utf-8').write(json.dumps(dict(sorted(plan.items())),ensure_ascii=False,indent=0)+'\n')
print(f'Preguntas estilo examen añadidas: {n} · quedan sin usar: {len(libres)}')
