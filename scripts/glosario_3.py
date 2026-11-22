# Glosario, tanda 3: términos del manual de Rescate en ascensores (preguntas 279-290).
import json, os
F = 'Manual de rescate en ascensores'
G = [
 ('Contrapeso', ['contrapeso'], 'Peso que equilibra la cabina para reducir la potencia del motor: la cabina más un 45 %. Con poca gente dentro, la cabina tiende a subir.', 'Ascensores', F),
 ('Limitador de velocidad', ['limitador de velocidad','limitador'], 'Detiene la cabina con el paracaídas si va demasiado rápida y corta el motor. Tiene dos poleas y un cable propio, independiente de los de tracción.', 'Ascensores', F, True),
 ('Pulsador de bomberos', ['pulsador de bomberos'], 'Al romper su cristal, el ascensor de emergencia queda para los bomberos: si sube, para en el piso siguiente; si baja, sigue a la planta principal; luego solo atiende llamadas interiores.', 'Ascensores', F),
 ('Amortiguadores', ['amortiguadores'], 'Frenan la cabina en el foso si fallan las paradas automáticas. Comprimidos del todo, deben dejar al menos medio metro libre.', 'Ascensores', F),
 ('Impulsión directa', ['impulsión directa'], 'Ascensor hidráulico 1:1: la cabina se mueve lo mismo que el pistón. Necesita un foso profundo.', 'Ascensores', F),
 ('Impulsión diferencial', ['impulsión diferencial'], 'Ascensor hidráulico 2:1: por cada centímetro del pistón la cabina se mueve dos. El pistón va en el lateral y no necesita foso profundo.', 'Ascensores', F),
 ('Cuarto de máquinas', ['cuarto de máquinas'], 'Lugar del mecanismo de tracción (motor, polea, volante, freno, limitador y cuadro de maniobras). Los ascensores más modernos no lo tienen.', 'Ascensores', F),
 ('RAEM', ['RAEM','Reglamento de Aparatos de Elevación'], 'Reglamento de Aparatos de Elevación y Manutención (RD 2291/1985). Un defecto grave se corrige en 6 meses o el ascensor queda fuera de servicio.', 'Ascensores', F),
 ('Ascensor sin engranajes', ['sin engranajes'], 'Ascensor eléctrico con el motor unido directamente a una polea grande. Rápido: 2-10 m/s, para edificios de gran altura.', 'Ascensores', F),
]
out = []
for e in G:
    x = {'t': e[0], 'a': e[1], 'd': e[2], 'tema': e[3], 'f': e[4]}
    if len(e) > 5 and e[5]: x['solo'] = 1
    out.append(x)
p = os.path.join(os.path.dirname(__file__), '..', 'glosario.json')
old = [g for g in json.load(open(p, encoding='utf-8')) if g['t'] not in {o['t'] for o in out}]
json.dump(old + out, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(old + out), 'términos')
