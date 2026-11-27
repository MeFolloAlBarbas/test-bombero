"""Pasa a la web un lote con visto bueno del usuario.

1. Comprueba el lote con scripts/reglas.py (si hay errores, no hace nada).
2. Mete sus preguntas en preguntas.json y sus términos en glosario.json.
3. Mueve el lote a tandas/aprobadas/ y deja tandas/estado.json sin lote esperando.
4. Amplía el calendario (scripts/calendario.sh).
Después: scripts/version.sh, commit y push.
Uso: python3 scripts/aprobar.py 2026-11-25   (o --quitar 401,407 para descartar antes esas preguntas)
     python3 scripts/aprobar.py 2026-11-27 --separar-revisar   (aprobación automática de la tarea 5: las preguntas
       marcadas con «revisar» no entran; se apartan en tandas/revisar/AAAA-MM-DD.json para verlas con el usuario)
"""
import json, os, sys, subprocess, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fecha = sys.argv[1]
quitar = {int(x) for x in sys.argv[sys.argv.index('--quitar') + 1].split(',')} if '--quitar' in sys.argv else set()
ruta = os.path.join(ROOT, 'tandas', 'pendientes', fecha + '.json')
lote = json.load(open(ruta, encoding='utf-8'))
if quitar:
    lote['preguntas'] = [q for q in lote['preguntas'] if q['id'] not in quitar]
    json.dump(lote, open(ruta, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if '--separar-revisar' in sys.argv:
    aparte = [q for q in lote['preguntas'] if q.get('revisar')]
    if aparte:
        rv = os.path.join(ROOT, 'tandas', 'revisar', fecha + '.json')
        prev = json.load(open(rv, encoding='utf-8')) if os.path.exists(rv) else {'preguntas': [], 'glosario': []}
        prev['preguntas'] += aparte; prev['glosario'] += lote.get('glosario', [])
        open(rv, 'w', encoding='utf-8').write(json.dumps(prev, ensure_ascii=False, indent=1))
        lote['preguntas'] = [q for q in lote['preguntas'] if not q.get('revisar')]
        json.dump(lote, open(ruta, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'Apartadas para revisar con el usuario: {len(aparte)}')
if subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'reglas.py'), ruta]).returncode:
    sys.exit('Hay errores: corrígelos antes de aprobar.')
PQ, GL = os.path.join(ROOT, 'preguntas.json'), os.path.join(ROOT, 'glosario.json')
banco = json.load(open(PQ, encoding='utf-8')); glos = json.load(open(GL, encoding='utf-8'))
banco += lote['preguntas']
ya = {g['t'].lower() for g in glos}
nuevos_t = [g for g in lote.get('glosario', []) if g['t'].lower() not in ya]
glos += nuevos_t
open(PQ, 'w', encoding='utf-8').write(json.dumps(banco, ensure_ascii=False, indent=0))
open(GL, 'w', encoding='utf-8').write(json.dumps(glos, ensure_ascii=False, indent=0))
n_nuevas = len(lote['preguntas'])
dest = os.path.join(ROOT, 'tandas', 'aprobadas', fecha + '.json')
if os.path.exists(dest):  # segundo lote del mismo día (p. ej. aprobado por la tarde y otro por la noche): se suman
    prev = json.load(open(dest, encoding='utf-8'))
    lote['preguntas'] = prev['preguntas'] + lote['preguntas']; lote['glosario'] = prev.get('glosario', []) + lote.get('glosario', [])
    open(dest, 'w', encoding='utf-8').write(json.dumps(lote, ensure_ascii=False, indent=1)); os.remove(ruta)
else:
    shutil.move(ruta, dest)
EF = os.path.join(ROOT, 'tandas', 'estado.json'); est = json.load(open(EF, encoding='utf-8'))
est['esperando_visto_bueno'] = None; est['ultimo_aprobado'] = fecha
open(EF, 'w', encoding='utf-8').write(json.dumps(est, ensure_ascii=False, indent=1) + '\n')
print(f'Aprobadas {n_nuevas} preguntas y {len(nuevos_t)} términos del glosario.')
subprocess.run(['sh', os.path.join(ROOT, 'scripts', 'calendario.sh')], check=True)
