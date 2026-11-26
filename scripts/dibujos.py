"""Mete una pregunta con dibujo (dib=1) cada dos días de preguntas en los días futuros de plan.json.

- Solo días posteriores a hoy (Madrid). Sustituye a una normal (nunca a la de intervención ni a la de las 20:00).
- Respeta «no repetir tema en el día»: si el tema ya está como normal, la sustituye; si está en la de
  intervención o en la de las 20:00, pasa al día siguiente.
- La pregunta sustituida vuelve a quedar sin usar. Uso: python3 scripts/dibujos.py
"""
import json, os, random, datetime as dt
from zoneinfo import ZoneInfo
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B={q['id']:q for q in json.load(open(os.path.join(ROOT,'preguntas.json'),encoding='utf-8'))}
PF=os.path.join(ROOT,'plan.json');plan=json.load(open(PF,encoding='utf-8'))
hoy=dt.datetime.now(ZoneInfo('Europe/Madrid')).date().isoformat()
usadas={i for ids in plan.values() for i in ids}
import os as _os,re as _re  # también las ya vistas antes del calendario (YA_USADAS_ANTES de plan.py)
_t=open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),'plan.py'),encoding='utf-8').read()
usadas|={int(x) for x in _re.findall(r'\d+',_re.sub(r'#.*','',_re.search(r'YA_USADAS_ANTES = \{([^}]*)\}',_t,_re.S).group(1)))}
libres=[q for q in sorted(B.values(),key=lambda q:q['id']) if q.get('dib') and q['id'] not in usadas]
dias=sorted(plan);ult=max([d for d in dias if any(B[i].get('dib') for i in plan[d])],default=None)
espera=0 if ult is None or ult<=hoy else None
n=0
for d in dias:
    if d<=hoy: continue
    ids=plan[d]
    if any(B[i].get('dib') for i in ids): espera=1; continue
    if espera is None: espera=0
    if espera>0: espera-=1; continue
    if not libres: break
    nq=libres[0];k=None
    for j in range(11):
        if B[ids[j]]['t']==nq['t']: k=j
    if B[ids[11]]['t']==nq['t'] or (k is not None and B[ids[k]].get('int')): continue
    if k is None:
        cand=[j for j in range(11) if not B[ids[j]].get('int')];k=random.Random('dib-'+d).choice(cand)
    ids[k]=nq['id'];libres.pop(0);n+=1;espera=1;print(d,f'{9+k}:00',nq['id'])
open(PF,'w',encoding='utf-8').write(json.dumps(dict(sorted(plan.items())),ensure_ascii=False,indent=0)+'\n')
print(f'Preguntas con dibujo añadidas: {n} · quedan sin usar: {len(libres)}')
