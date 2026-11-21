"""Tanda 4: preguntas de intervención (campo int=1), basadas solo en los manuales."""
import json, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F=os.path.join(ROOT,'preguntas.json');B=json.load(open(F,encoding='utf-8'))
def q(id,t,enun,ops,c,o4,que,porque,ojo,rec,f,d='normal'):
    return {"id":id,"t":t,"d":d,"q":enun,"o":ops,"c":c,"o4":o4,"que":que,"porque":porque,"ojo":ojo,"rec":rec,"f":f,"int":1}
N=[
q(230,"Ascensores","Llegáis a un ascensor parado entre plantas con dos personas dentro. No es seguro ponerlo en marcha, pero se las puede sacar sin mover la cabina. ¿Qué hacéis?",
 ["Cortar el suministro eléctrico, comprobar que no hay tensión y rescatarlas.","Mover la cabina con el sistema eléctrico de emergencia hasta dejarla a nivel.","Sacarlas sin cortar la corriente, para que la cabina no se quede a oscuras."],0,
 "Esperar a la empresa mantenedora sin hacer nada más.",
 "El manual sigue un <mark>protocolo de preguntas en orden</mark> tras comunicarse con las víctimas, valorar la situación e identificar los riesgos.",
 "1.º ¿Es posible y segura la puesta en marcha normal? <mark>No</mark>. 2.º ¿Se puede rescatar sin mover la cabina? <mark>Sí</mark> → <mark>cortar y comprobar la ausencia de suministro eléctrico y rescatar</mark>.",
 "Nunca se rescata con tensión: hay que evitar el riesgo de <mark>electrocución, caídas y atrapamientos</mark>. Avisa a las víctimas de que puede apagarse la luz.",
 "Si no hace falta mover la cabina: <mark>cortar, comprobar y rescatar</mark>.",
 "Manual de rescate en ascensores, procedimiento táctico"),
q(231,"Ascensores","Ascensor sin cuarto de máquinas: no es seguro ponerlo en marcha y no se puede rescatar sin mover la cabina. El sistema eléctrico de emergencia funciona. ¿Qué hacéis?",
 ["Mover la cabina con el sistema eléctrico de emergencia hasta un punto que permita el rescate.","Cortar la corriente y mover la cabina sin electricidad hasta la planta más cercana.","Tratarlo como un rescate no ordinario, porque la cabina no se puede mover."],0,
 "Abrir la trampilla del techo y sacarlas por el hueco.",
 "En los ascensores <mark>sin cuarto de máquinas</mark>, el protocolo incluye un paso propio: usar el <mark>sistema eléctrico de emergencia</mark>.",
 "Orden: puesta en marcha normal (no) → rescate sin mover la cabina (no) → <mark>¿se puede mover con el sistema eléctrico de emergencia? Sí</mark> → moverla así hasta un punto de rescate. Solo si no se puede, se corta la corriente y se mueve sin electricidad.",
 "El <mark>rescate no ordinario</mark> es para cuando la cabina está bloqueada: acuñada, fuera de sus guías o con el mecanismo de elevación dañado.",
 "Sin cuarto de máquinas: <mark>primero el sistema de emergencia</mark>, después a mano.",
 "Manual de rescate en ascensores, procedimiento táctico"),
q(232,"NRBQ","Mides con el explosímetro los vapores de un producto distinto del gas con el que está calibrado y marca un 8 %. ¿Qué haces con esa lectura?",
 ["Multiplicarla por el factor de corrección que da el fabricante para ese producto.","Darla por buena, porque el explosímetro mide cualquier vapor inflamable.","Descartarla y medir con un tubo colorimétrico, porque el explosímetro no sirve para ese producto."],0,
 "Dividirla entre dos, porque los vapores pesan más que el aire.",
 "El <mark>explosímetro</mark> mide la concentración de gases y vapores inflamables. Detecta su presencia, pero <mark>no distingue</mark> unas sustancias de otras.",
 "Se calibra con un <mark>gas patrón</mark>. Con vapores de otros productos la lectura <mark>puede no ser precisa</mark>, y para obtener la medida correcta hay que <mark>multiplicarla por el factor de corrección</mark> del fabricante.",
 "Conviene elegir bien el gas de calibración para tener factores de corrección <mark>cercanos a 1</mark>.",
 "Otro producto = <mark>lectura × factor de corrección</mark>.",
 "Manual NRBQ, Aparatos de detección y medida"),
q(233,"Tráfico (APRAT)","Un turismo está volcado de lado con las ventanillas intactas y hay que romper una luna para el acceso sanitario. ¿Cuál se elige?",
 ["La más retirada del herido y que menos restos y cristales genere.","El parabrisas, porque da el acceso más amplio.","La más cercana al herido, para poder valorarlo cuanto antes."],0,
 "La luna trasera, porque siempre es la más fácil de romper.",
 "Si el acceso no está creado, el mando ordena como <mark>prioridad</mark> crear un espacio para que el sanitario llegue al herido.",
 "Se busca la maniobra más sencilla. Si hay que romper lunas, se elige la <mark>más retirada del herido</mark>, la que <mark>menos restos le pueda arrojar</mark> y la que <mark>menos cristales genere</mark>, para no contaminar el escenario.",
 "El parabrisas es <mark>laminado</mark>: cortarlo genera un polvo de vidrio muy dañino si se inhala. Debe evitarse hasta poder proteger a los heridos.",
 "Luna: <mark>lejos del herido, pocos restos</mark>. Parabrisas, solo con los heridos protegidos.",
 "APRAT I, Acceso sanitario"),
q(234,"Tráfico (APRAT)","Un turismo accidentado está sobre sus ruedas con el herido dentro. ¿Qué se hace primero al estabilizarlo?",
 ["Colocar cuñas a ambos lados de una o dos ruedas.","Colocar calzos bajo los pilares A y C.","Mover el vehículo a una zona llana y segura."],0,
 "Desinflar los neumáticos para que apoye la carrocería.",
 "La estabilización evita movimientos que agraven las lesiones y crea un lugar de trabajo seguro. Sobre las ruedas ya hay <mark>cuatro apoyos</mark>, por eso es de las más sencillas.",
 "1.º <mark>Cuñas a ambos lados de una o dos ruedas</mark> (movimiento longitudinal); en cuanto se pueda, quitar el contacto y echar el freno de estacionamiento. 2.º <mark>Calzos lo más cerca de la amortiguación</mark>, bajo los pilares A y C (movimientos verticales).",
 "<mark>Nunca se mueve un vehículo con víctimas dentro</mark>, salvo ante un gran riesgo que no se pueda controlar (atropello, incendio…).",
 "Sobre ruedas: <mark>primero cuñas, después calzos</mark>.",
 "APRAT I, Estabilizaciones básicas"),
q(235,"Trabajos en altura","Vas a hacer un trabajo vertical en el que prevés estar suspendido unos 45 minutos. ¿Qué elemento es imprescindible y por qué?",
 ["El asiento de trabajo, para evitar el síndrome del arnés.","El estribo o pedal, para no cansar los brazos al ascender.","Un segundo arnés de pecho, para repartir el peso."],0,
 "Un casco con barboquejo, para no perderlo en la suspensión.",
 "Estar mucho tiempo colgado del arnés puede causar el <mark>trauma por suspensión o síndrome del arnés</mark>.",
 "El <mark>asiento (silla) de trabajo</mark> permite estar suspendido liberando la presión de las cintas del arnés. Es <mark>imprescindible si se prevé estar suspendido más de 30 minutos</mark> (NTP 789).",
 "El asiento es un <mark>equipo auxiliar</mark>, no un EPI. El estribo también es auxiliar: sirve para ascender cargando el peso en las piernas.",
 "Más de <mark>30 minutos</mark> suspendido → <mark>asiento</mark>.",
 "NTP, Seguridad en trabajos verticales"),
]
ids={x['id'] for x in B}
B+=[x for x in N if x['id'] not in ids]
open(F,'w',encoding='utf-8').write('[\n'+',\n'.join(json.dumps(x,ensure_ascii=False) for x in B)+'\n]\n')
print(len(B))
