"""Tanda 6: preguntas con dibujo (campo img con SVG propio, dib=1). Todo comprobado en el manual NRBQ."""
import json, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F=os.path.join(ROOT,'preguntas.json');B=json.load(open(F,encoding='utf-8'))
def q(id,enun,img,ops,o4,que,porque,ojo,rec,f):
    return {"id":id,"t":"NRBQ","d":"normal","q":enun,"img":img,"o":ops,"c":0,"o4":o4,"que":que,"porque":porque,"ojo":ojo,"rec":rec,"f":f,"dib":1}
NFPA='<svg viewBox="0 0 24 24" role="img" aria-label="Rombo NFPA con un 2 en rojo, un 0 en amarillo y un 3 en azul" shape-rendering="crispEdges"><g transform="rotate(45 12 12)"><rect x="4" y="4" width="8" height="8" fill="#d62828"/><rect x="12" y="4" width="8" height="8" fill="#f2c80f"/><rect x="4" y="12" width="8" height="8" fill="#2a6fdb"/><rect x="12" y="12" width="8" height="8" fill="#ffffff"/><rect x="4" y="4" width="16" height="16" fill="none" stroke="#1a1a1a" stroke-width="0.5"/></g><g font-family="monospace" font-weight="bold" font-size="4" text-anchor="middle" fill="#1a1a1a"><text x="12" y="8.5">2</text><text x="17.6" y="13.5">0</text><text x="6.4" y="13.5" fill="#ffffff">3</text></g></svg>'
HAZ='<svg viewBox="0 0 30 20" role="img" aria-label="Placa naranja con el código 2W" shape-rendering="crispEdges"><rect width="30" height="20" fill="#1a1a1a"/><rect x="1" y="1" width="28" height="18" fill="#f28c1e"/><text x="15" y="14" text-anchor="middle" font-family="monospace" font-weight="bold" font-size="10" fill="#1a1a1a">2W</text></svg>'
RES_O='<svg viewBox="0 0 100 100" role="img" aria-label="Pictograma cuadrado naranja con una llama sobre un círculo"><rect x="4" y="4" width="92" height="92" fill="#f5a623" stroke="#1a1a1a" stroke-width="4"/><circle cx="50" cy="66" r="16" fill="none" stroke="#1a1a1a" stroke-width="7"/><path d="M50 14 C58 26 68 32 64 44 C62 50 56 52 50 52 C42 52 36 48 36 40 C36 32 42 30 44 22 C46 28 48 30 50 30 C52 26 50 20 50 14 Z" fill="#1a1a1a"/><rect x="20" y="86" width="60" height="5" fill="#1a1a1a"/></svg>'
RES_T='<svg viewBox="0 0 100 100" role="img" aria-label="Pictograma cuadrado naranja con una calavera sobre tibias cruzadas"><rect x="4" y="4" width="92" height="92" fill="#f5a623" stroke="#1a1a1a" stroke-width="4"/><g stroke="#1a1a1a" stroke-width="7" stroke-linecap="round"><line x1="24" y1="58" x2="76" y2="86"/><line x1="76" y1="58" x2="24" y2="86"/></g><path d="M50 14 C34 14 26 25 26 37 C26 45 30 50 36 52 L36 60 L64 60 L64 52 C70 50 74 45 74 37 C74 25 66 14 50 14 Z" fill="#1a1a1a"/><circle cx="41" cy="38" r="6" fill="#f5a623"/><circle cx="59" cy="38" r="6" fill="#f5a623"/><polygon points="50,44 46,51 54,51" fill="#f5a623"/></svg>'
CLP='<svg viewBox="0 0 100 100" role="img" aria-label="Rombo de borde rojo con una botella de gas"><polygon points="50,4 96,50 50,96 4,50" fill="#fff" stroke="#d62828" stroke-width="6"/><g transform="rotate(-35 50 52)"><rect x="40" y="30" width="20" height="44" rx="9" fill="#1a1a1a"/><rect x="45" y="22" width="10" height="9" fill="#1a1a1a"/><rect x="42" y="19" width="16" height="4" fill="#1a1a1a"/></g></svg>'
TUBO='<svg viewBox="0 0 220 70" role="img" aria-label="Tubo colorimétrico con una mancha morada hasta la marca de 300 ppm"><rect x="10" y="22" width="190" height="22" rx="11" fill="#eef4f7" stroke="#6b7c85" stroke-width="2"/><rect x="22" y="25" width="86" height="16" fill="#7b3fa0"/><rect x="108" y="25" width="80" height="16" fill="#f3e9b5"/><g stroke="#333" stroke-width="1.5"><line x1="40" y1="44" x2="40" y2="52"/><line x1="75" y1="44" x2="75" y2="52"/><line x1="110" y1="44" x2="110" y2="52"/><line x1="145" y1="44" x2="145" y2="52"/><line x1="180" y1="44" x2="180" y2="52"/></g><g font-family="monospace" font-size="10" fill="#333" text-anchor="middle"><text x="40" y="63">500</text><text x="75" y="63">400</text><text x="110" y="63">300</text><text x="145" y="63">200</text><text x="180" y="63">100</text></g><text x="105" y="15" font-family="monospace" font-size="10" fill="#333" text-anchor="middle">ppm</text></svg>'
def bot(oj,cu,lab): return f'<svg viewBox="0 0 60 130" role="img" aria-label="{lab}"><rect x="25" y="2" width="10" height="10" fill="#555"/><path d="M10 40 C10 22 20 14 30 14 C40 14 50 22 50 40 Z" fill="{oj}" stroke="#333" stroke-width="1.5"/><rect x="10" y="40" width="40" height="84" rx="4" fill="{cu}" stroke="#333" stroke-width="1.5"/></svg>'
N=[
q(247,"En este rombo NFPA 704, ¿qué indica el 3 del cuadro azul?",NFPA,
 ["Que la materia es muy peligrosa para la salud.","Que la materia es muy inflamable.","Que la materia es muy reactiva."],"Que la materia es radiactiva.",
 "El <mark>rombo NFPA 704</mark> («diamante de peligro») etiqueta mercancías peligrosas en EE. UU. y en algunos productos importados.",
 "Cada color es un peligro: <mark>azul = salud</mark> · <mark>rojo = inflamabilidad</mark> · <mark>amarillo = reactividad</mark> · blanco = riesgos especiales. Cada uno se puntúa de <mark>0 (sin riesgo) a 4 (máximo)</mark>: un 3 en azul es <mark>muy peligroso</mark> para la salud.",
 "El cuadro blanco no lleva número: lleva símbolos de riesgo específico, como OX (oxidante), W tachada (no usar agua) o el de radiactividad.",
 "<mark>Azul salud, rojo fuego, amarillo reacción</mark>; de 0 a 4.","Manual NRBQ, Rombo NFPA"),
q(248,"Acabas de hacer la aspiración con este tubo colorimétrico. ¿Cuándo debes leer el resultado?",TUBO,
 ["Inmediatamente, porque la mancha puede cambiar con el tiempo.","Tras esperar 10 minutos a que la mancha se estabilice.","Después de guardarlo refrigerado."],"Al día siguiente, en el parque.",
 "Los <mark>tubos colorimétricos</mark> contienen un reactivo que cambia de color con la sustancia que se mide; la <mark>longitud de la mancha</mark> indica la concentración.",
 "La lectura debe hacerse <mark>inmediatamente después de terminar el muestreo</mark>, porque la coloración y la extensión de la mancha <mark>pueden variar con el tiempo</mark>.",
 "Lo de refrigerar es para <mark>conservar</mark> los tubos sin usar, que además caducan. Y la mayoría <mark>no distinguen compuestos parecidos</mark>.",
 "Tubo: <mark>aspirar y leer al momento</mark>.","Manual NRBQ, Tubos colorimétricos"),
q(249,"Un recipiente lleva este pictograma. Según el reglamento CLP, ¿qué peligro indica?",CLP,
 ["Gas a presión, que puede explotar si se calienta.","Gas extremadamente tóxico, que puede ser mortal.","Gas inflamable en contacto con el agua."],"Gas corrosivo para la piel.",
 "El reglamento <mark>CLP</mark> (CE 1272/2008) usa pictogramas en forma de rombo con borde rojo para la clasificación, etiquetado y envasado de sustancias.",
 "La <mark>botella de gas</mark> indica <mark>gas bajo presión, que puede explotar cuando se calienta</mark>. También gases refrigerados (quemaduras criogénicas) y gases disueltos.",
 "La toxicidad mortal se indica con la <mark>calavera</mark>, y la inflamabilidad con la <mark>llama</mark>.",
 "Botella en el rombo = <mark>gas a presión</mark>.","Manual NRBQ, Tabla 34 (reglamento CLP)"),
q(250,"Una placa Hazchem empieza por este código. ¿Qué agente extintor NO se puede usar?",HAZ,
 ["Chorro pleno.","Espuma.","Agentes secos."],"Agua pulverizada.",
 "El código <mark>Hazchem</mark> identifica mercancías peligrosas en Reino Unido, Australia y Nueva Zelanda. Empieza por el <mark>código de acción de emergencia</mark>.",
 "El número indica el agente: <mark>1 chorro pleno · 2 niebla · 3 espuma · 4 agentes secos</mark>. Se puede usar uno de <mark>número mayor</mark>, pero <mark>nunca uno menor</mark>: con un 2 valen espuma y agentes secos, pero no el chorro pleno.",
 "La <mark>W</mark> pide contener el producto y evitar que llegue a alcantarillas o ríos, y obliga a usar protección completa (equipo de respiración y traje químico).",
 "Hazchem: <mark>hacia arriba sí, hacia abajo nunca</mark>.","Manual NRBQ, Código Hazchem"),
q(251,"Esta botella tiene la ojiva roja y el cuerpo azul. ¿Qué informa sobre el riesgo del gas?",bot('#d62828','#2a6fdb','Botella de gas con la ojiva roja y el cuerpo azul'),
 ["Solo la ojiva: el color del cuerpo lo elige el fabricante.","La combinación de los dos colores.","Solo el cuerpo: la ojiva indica el fabricante."],"Ninguno de los dos colores.",
 "La parte superior de la botella es la <mark>ojiva</mark>. Según la norma actual, su color identifica el riesgo principal del gas.",
 "El color del <mark>cuerpo es de libre aplicación</mark> (salvo en gases medicinales): <mark>no informa sobre riesgos</mark> y lo elige el fabricante. Aquí, la ojiva roja indica <mark>inflamable</mark>.",
 "La única información concreta del gas es la de la <mark>etiqueta</mark>; el color de la ojiva es información adicional. La norma no se aplica a extintores ni a GLP.",
 "Riesgo = <mark>ojiva</mark>; cuerpo = fabricante.","Manual NRBQ, Equipamiento y etiquetado de botellas"),
q(252,"En la etiqueta de un residuo peligroso aparece este pictograma. ¿Qué indica?",RES_O,
 ["Comburente.","Inflamable.","Explosivo."],"Corrosivo.",
 "Los residuos peligrosos se etiquetan con <mark>pictogramas negros sobre fondo amarillo anaranjado</mark>.",
 "Una <mark>llama encima de un círculo (O)</mark> indica <mark>comburente</mark>: favorece la combustión de otras materias.",
 "No confundir con la <mark>llama sola</mark>, que indica inflamable, ni con la <mark>bomba explotando</mark>, que indica explosivo.",
 "Llama <mark>con círculo = comburente</mark>; llama sola = inflamable.","Manual NRBQ, Etiquetado de residuos"),
q(253,"¿Qué tipo de gas indica la ojiva verde intenso de esta botella?",bot('#1f9a3a','#8a8f96','Botella de gas con la ojiva verde intenso y el cuerpo gris'),
 ["Un gas inerte, como el argón.","Un gas tóxico.","Un gas inflamable."],"Un gas oxidante.",
 "Según la norma actual, el color de la <mark>ojiva</mark> identifica el riesgo principal del gas.",
 "Los gases <mark>inertes</mark> (argón y mezclas) llevan la ojiva <mark>verde intenso o verde oscuro</mark>. Antes eran amarillos o de varios colores.",
 "El cambio confunde: el amarillo, que antes era de inertes, ahora es <mark>tóxico o corrosivo</mark>.",
 "Ojiva <mark>verde = inerte</mark>.","Manual NRBQ, Equipamiento y etiquetado de botellas"),
q(254,"¿Qué indica este pictograma en la etiqueta de un residuo peligroso?",RES_T,
 ["Tóxico.","Nocivo.","Corrosivo."],"Irritante.",
 "Los residuos peligrosos se etiquetan con <mark>pictogramas negros sobre fondo amarillo anaranjado</mark>.",
 "Una <mark>calavera sobre unas tibias cruzadas (T)</mark> indica <mark>tóxico</mark>.",
 "<mark>Nocivo (Xn)</mark> e <mark>irritante (Xi)</mark> se indican con una <mark>cruz de san Andrés</mark>, no con la calavera.",
 "Calavera = <mark>tóxico</mark>; cruz = nocivo o irritante.","Manual NRBQ, Etiquetado de residuos"),
q(255,"Una botella de gas medicinal tiene la ojiva blanca. ¿Qué gas contiene?",bot('#ffffff','#ffffff','Botella de gas medicinal blanca'),
 ["Oxígeno.","Nitrógeno.","Helio."],"Hidrógeno.",
 "En los <mark>gases medicinales y respirables</mark>, cada gas tiene un color específico de ojiva (salvo las mezclas).",
 "Colores que no han cambiado con la norma: <mark>oxígeno blanco</mark> · nitrógeno negro · dióxido de carbono gris · óxido nitroso azul · helio marrón · hidrógeno rojo.",
 "En los gases medicinales el color del cuerpo sí está regulado; en los industriales es libre.",
 "Ojiva <mark>blanca = oxígeno</mark>.","Manual NRBQ, Equipamiento y etiquetado de botellas"),
]
ids={x['id'] for x in B};B+=[x for x in N if x['id'] not in ids]
open(F,'w',encoding='utf-8').write('[\n'+',\n'.join(json.dumps(x,ensure_ascii=False) for x in B)+'\n]\n')
print(len(B))
