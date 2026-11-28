"""Repaso de las explicaciones ya hechas (pedido del usuario, 28/11/2026).

El «Por qué» debe explicar la CAUSA REAL (mecanismo, finalidad), no repetir la norma. Este script lleva la cola
de preguntas del banco que hay que revisar y aplica los cambios con seguridad.

  python3 scripts/repaso_explicaciones.py estado
  python3 scripts/repaso_explicaciones.py ver N            → JSON con las N siguientes preguntas sin revisar
  python3 scripts/repaso_explicaciones.py aplicar cambios.json

cambios.json = lista de objetos:
  {"id": 118, "ok": true}                                   → revisada, la explicación ya está bien
  {"id": 118, "que": "...", "porque": "...", "ojo": "...", "rec": "...", "motivo": "por qué se cambia"}
  Solo si la pregunta NO ha salido nunca se pueden cambiar también "q", "o", "c", "o4", "tq", "ta"
  (p. ej. un «¿por qué…?» cuya respuesta es «porque lo dice la norma»).
  {"id": 118, "revisar": "motivo"}                           → no se toca; se aparta para verla con el usuario

Escribe el registro antes/después en tandas/repaso_explicaciones/AAAA-MM-DD.json.
"""
import json, os, re, sys, datetime as dt
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'tandas', 'repaso_explicaciones')
COLA = os.path.join(D, 'cola.json')
PB = os.path.join(ROOT, 'preguntas.json')
LEGALES = {'Constitución', 'Igualdad', 'Régimen local', 'Haciendas locales', 'Reglamento Bomberos',
           'Procedimiento administrativo', 'EBEP', 'Estatuto CAM', 'Protección civil'}
EXPL = ('que', 'porque', 'ojo', 'rec')
ENUN = ('q', 'o', 'c', 'o4', 'tq', 'ta')
hoy = dt.datetime.now(ZoneInfo('Europe/Madrid')).date().isoformat()


def banco():
    return json.load(open(PB, encoding='utf-8'))


def usadas():
    plan = json.load(open(os.path.join(ROOT, 'plan.json'), encoding='utf-8'))
    t = open(os.path.join(ROOT, 'scripts', 'plan.py'), encoding='utf-8').read()
    antes = {int(x) for x in re.findall(r'\d+', re.sub(r'#.*', '', re.search(r'YA_USADAS_ANTES = \{([^}]*)\}', t, re.S).group(1)))}
    return antes | {i for d, ids in plan.items() if d <= hoy for i in ids}


def cola():
    if os.path.exists(COLA):
        return json.load(open(COLA, encoding='utf-8'))
    B = banco()
    orden = sorted(B, key=lambda q: (q['t'] in LEGALES, q['id']))  # técnicas primero, legales al final
    c = {'creada': hoy, 'pendientes': [q['id'] for q in orden], 'ok': [], 'cambiadas': [], 'revisar': []}
    os.makedirs(D, exist_ok=True)
    guardar_cola(c)
    return c


def guardar_cola(c):
    json.dump(c, open(COLA, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    cmd = sys.argv[1]
    c = cola()
    if cmd == 'estado':
        print(f"pendientes {len(c['pendientes'])} · bien {len(c['ok'])} · cambiadas {len(c['cambiadas'])} · para revisar {len(c['revisar'])}")
        return
    if cmd == 'ver':
        n = int(sys.argv[2]); B = {q['id']: q for q in banco()}; U = usadas()
        out = []
        for i in c['pendientes']:
            if i not in B: continue
            q = B[i]
            out.append({k: q.get(k) for k in ('id', 't', 'd', 'q', 'o', 'c', 'o4', 'que', 'porque', 'ojo', 'rec', 'f', 'src', 'tq', 'ta')} | {'ya_salio': i in U, 'legal': q['t'] in LEGALES})
            if len(out) >= n: break
        print(json.dumps(out, ensure_ascii=False, indent=1))
        return
    if cmd == 'aplicar':
        cambios = json.load(open(sys.argv[2], encoding='utf-8'))
        B = banco(); idx = {q['id']: q for q in B}; U = usadas()
        log_p = os.path.join(D, hoy + '.json')
        log = json.load(open(log_p, encoding='utf-8')) if os.path.exists(log_p) else []
        errores = []
        for ch in cambios:
            i = ch.get('id'); q = idx.get(i)
            if q is None: errores.append(f'{i}: no existe'); continue
            campos = set(ch) - {'id', 'ok', 'motivo', 'revisar'}
            if ch.get('ok') and campos: errores.append(f'{i}: «ok» no puede llevar cambios'); continue
            mal = campos - set(EXPL) - set(ENUN)
            if mal: errores.append(f'{i}: campos no permitidos {sorted(mal)}'); continue
            if campos & set(ENUN) and i in U: errores.append(f'{i}: ya ha salido, no se puede cambiar el enunciado ni las opciones'); continue
            for k in campos & set(EXPL):
                if re.search(r'\b(opción|respuesta)\s+[ABC]\b|(?:^|\s)[ABC]\)', re.sub('<[^>]+>', '', ch[k])):
                    errores.append(f'{i}: «{k}» nombra una opción por su letra')
            if 'o' in ch and (not isinstance(ch['o'], list) or len(ch['o']) != 3): errores.append(f'{i}: «o» debe tener 3 opciones')
            if 'c' in ch and ch['c'] not in (0, 1, 2): errores.append(f'{i}: «c» debe ser 0, 1 o 2')
        if errores:
            print('ERRORES, no se ha aplicado nada:'); print('\n'.join(errores)); sys.exit(1)
        n_ok = n_ch = n_rev = 0
        for ch in cambios:
            i = ch['id']; q = idx[i]
            if i in c['pendientes']: c['pendientes'].remove(i)
            if ch.get('revisar'):
                c['revisar'].append({'id': i, 'motivo': ch['revisar'], 'fecha': hoy}); n_rev += 1; continue
            if ch.get('ok'):
                c['ok'].append(i); n_ok += 1; continue
            antes = {k: q.get(k) for k in ch if k not in ('id', 'motivo')}
            for k, v in ch.items():
                if k not in ('id', 'motivo'): q[k] = v
            log.append({'id': i, 't': q['t'], 'motivo': ch.get('motivo', ''), 'antes': antes, 'despues': {k: q[k] for k in antes}})
            c['cambiadas'].append(i); n_ch += 1
        json.dump(B, open(PB, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        guardar_cola(c)
        json.dump(log, open(log_p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f'Aplicado: {n_ch} cambiadas · {n_ok} ya estaban bien · {n_rev} apartadas para revisar · quedan {len(c["pendientes"])}')
        return
    print(__doc__); sys.exit(1)


if __name__ == '__main__':
    main()
