"""Mete una pregunta de intervención (int=1) por día en los días futuros de plan.json.

- Solo toca días posteriores a hoy (hora de Madrid) que aún no tengan una.
- Va a una hora aleatoria de 9:00 a 19:00 (nunca a las 20:00, que es la difícil).
- Mantiene la regla de no repetir tema en el día: si su tema ya está ese día, sustituye a esa pregunta.
- La pregunta sustituida vuelve a quedar sin usar.
Uso: python3 scripts/intervencion.py
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
libres=[q for q in sorted(B.values(),key=lambda q:q['id']) if q.get('int') and q['id'] not in usadas]
n=0
for dia in sorted(plan):
    if dia<=hoy or any(B[i].get('int') for i in plan[dia]): continue
    if not libres: break
    nq=libres.pop(0);ids=plan[dia]
    rnd=random.Random('int-'+dia);hora=rnd.randrange(0,11)
    mismo=[k for k in range(11) if B[ids[k]]['t']==nq['t']]
    if B[ids[11]]['t']==nq['t']: libres.insert(0,nq);continue
    k=mismo[0] if mismo else hora
    ids[k]=nq['id'];ids[k],ids[hora]=ids[hora],ids[k]
    n+=1;print(dia,f"{9+hora}:00",nq['id'],nq['t'])
open(PF,'w',encoding='utf-8').write(json.dumps(dict(sorted(plan.items())),ensure_ascii=False,indent=0)+'\n')
print(f'Días con pregunta de intervención añadida: {n} · quedan sin usar: {len(libres)}')
