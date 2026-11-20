import json
P='/home/claude/test-bombero/preguntas.json'
Q=json.load(open(P,encoding='utf-8'))
nid=max(q['id'] for q in Q)+1
def q(t,d,enun,ops,c,que,porque,ojo,rec,f):
    global nid
    Q.append(dict(id=nid,t=t,d=d,q=enun,o=ops,c=c,que=que,porque=porque,ojo=ojo,rec=rec,f=f)); nid+=1

# ---------------- DIFÍCILES ----------------
q("Régimen local","difícil",
 "Un municipio tiene 15.000 habitantes. Según el art. 26 de la Ley 7/1985, ¿está obligado a prestar por sí mismo el servicio de prevención y extinción de incendios?",
 ["Sí, porque es un servicio obligatorio en todos los municipios.","No, porque solo es obligatorio en los de más de 20.000 habitantes.","Sí, porque supera los 5.000 habitantes."],1,
 "El art. 26 fija los <mark>servicios mínimos</mark> que cada municipio debe prestar según su población.",
 "La prevención y extinción de incendios es obligatoria en los municipios de <mark>más de 20.000 habitantes</mark>. En los de menos, es la <mark>Diputación provincial</mark> (o entidad equivalente) la que coordina la prestación de algunos servicios.",
 "Con más de 5.000 se añaden parque público, biblioteca y tratamiento de residuos, pero no los bomberos.",
 "Escalones: <mark>todos</mark> · <mark>más de 5.000</mark> · <mark>más de 20.000 (bomberos y protección civil)</mark> · <mark>más de 50.000 (transporte urbano y medio ambiente)</mark>.","Ley 7/1985, art. 26")

q("Tráfico (APRAT)","difícil",
 "Hay que extraer al conductor de un turismo y no es posible hacerlo por el portón trasero. Según el APRAT, ¿cuál es la siguiente vía de extracción?",
 ["La puerta trasera del mismo lado (ángulo de 25º).","La puerta trasera contralateral (ángulo de 60º).","La puerta delantera (ángulo de 90º)."],0,
 "Se elige la salida que menos gire el <mark>eje espinal</mark> de la víctima, para no agravar una posible lesión de columna.",
 "Orden para el conductor: <mark>portón trasero (0º)</mark> → <mark>puerta trasera del mismo lado (25º)</mark> → puerta trasera contralateral (60º) → puertas delanteras (90º).",
 "La puerta delantera es la última opción: obliga a girar 90º y además estorban el volante y el salpicadero.",
 "Cuanto <mark>menor sea el ángulo</mark>, mejor: <mark>0 → 25 → 60 → 90</mark>.","APRAT II, Salidas de extracción")

q("NRBQ","difícil",
 "En un panel naranja, el número de identificación de peligro va precedido de una «X» y tiene una cifra repetida. ¿Qué indica cada cosa?",
 ["La X, que la materia es explosiva; la cifra repetida, que hay dos materias.","La X, que reacciona peligrosamente con el agua; la cifra repetida, que ese peligro se intensifica.","La X, que es un residuo; la cifra repetida, que la cisterna tiene doble pared."],1,
 "El número de la parte superior del panel (código Kemler) resume los peligros principales de la materia.",
 "La <mark>X</mark> indica que la materia <mark>reacciona peligrosamente con el agua</mark>: solo pueden usar agua los expertos. La <mark>duplicación de una cifra</mark> indica que <mark>se intensifica</mark> ese peligro.",
 "Si basta una sola cifra para indicar el peligro, el número se completa con un <mark>0</mark>.",
 "<mark>X = cuidado con el agua</mark> · <mark>cifra doble = peligro más intenso</mark> · <mark>0 = relleno</mark>.","Manual NRBQ, Número de identificación de peligro")

q("CTE DB-SI","difícil",
 "Un edificio tiene una altura de evacuación de 18 m. Según el DB-SI 5, ¿cuál es la separación máxima entre el vehículo de bomberos y la fachada en el espacio de maniobra?",
 ["23 m.","18 m.","10 m."],1,
 "Los edificios con una altura de evacuación descendente de <mark>más de 9 m</mark> deben tener un <mark>espacio de maniobra</mark> para los vehículos de bomberos.",
 "La separación máxima depende de la altura: <mark>hasta 15 m → 23 m</mark> · <mark>de más de 15 hasta 20 m → 18 m</mark> · <mark>más de 20 m → 10 m</mark>. Con 18 m se aplica el tramo intermedio.",
 "Cuanto más alto es el edificio, más cerca tiene que poder ponerse el vehículo, porque la escala debe llegar más arriba.",
 "<mark>23 / 18 / 10 m</mark> para edificios de hasta 15, de 15 a 20 y de más de 20 m.","CTE DB-SI 5")

q("Haciendas locales","difícil",
 "Según el art. 59 del TRLRHL, ¿cuál de estos impuestos puede el ayuntamiento decidir no exigir?",
 ["El Impuesto sobre Bienes Inmuebles (IBI).","El Impuesto sobre Vehículos de Tracción Mecánica (IVTM).","El Impuesto sobre Construcciones, Instalaciones y Obras (ICIO)."],2,
 "Los impuestos municipales se dividen en <mark>obligatorios</mark> («exigirán») y <mark>potestativos</mark> («podrán establecer»).",
 "Obligatorios: <mark>IBI, IAE e IVTM</mark>. Potestativos: <mark>ICIO</mark> y el impuesto sobre el incremento de valor de los terrenos urbanos (<mark>plusvalía</mark>).",
 "Fíjate en el verbo de la ley: «exigirán» frente a «podrán establecer y exigir».",
 "Obligatorios: <mark>IBI, IAE, IVTM</mark> · Potestativos: <mark>ICIO y plusvalía</mark>.","TRLRHL, art. 59")

q("EBEP","difícil",
 "Se nombra a un funcionario interino por exceso o acumulación de tareas. Según el art. 10 del TREBEP, su nombramiento puede durar como máximo:",
 ["9 meses dentro de un periodo de 18 meses.","3 años.","6 meses dentro de un periodo de 12 meses."],0,
 "Los <mark>interinos</mark> se nombran temporalmente, por necesidad y urgencia, para funciones propias de funcionarios de carrera.",
 "Hay cuatro supuestos: <mark>plaza vacante</mark> (máximo 3 años), <mark>sustitución</mark> (el tiempo necesario), <mark>programa temporal</mark> (máximo 3 años, ampliable 12 meses) y <mark>acumulación de tareas</mark> (<mark>máximo 9 meses en 18</mark>).",
 "Los 3 años son de la plaza vacante y de los programas temporales, no de la acumulación de tareas.",
 "Interinos: vacante <mark>3 años</mark> · programa <mark>3 años + 12 meses</mark> · acumulación <mark>9 en 18 meses</mark>.","TREBEP, art. 10")

# ---------------- NORMALES ----------------
q("NRBQ","normal",
 "Según el manual NRBQ, el panel naranja de un vehículo de mercancías peligrosas mide normalmente:",
 ["40 cm de base y 30 cm de altura.","30 cm de base y 30 cm de altura.","50 cm de base y 40 cm de altura."],0,
 "El <mark>panel naranja</mark> señala que un vehículo transporta mercancías peligrosas.",
 "Es <mark>retrorreflectante</mark>, rectangular, de <mark>40 cm de base y 30 cm de altura</mark>, con un ribete negro de 1,5 cm, y debe resistir la intemperie y un incendio sin desprenderse.",
 "Si el vehículo no tiene sitio suficiente, se admiten dimensiones reducidas, pero la medida normal es 40 × 30.",
 "Panel: <mark>40 × 30 cm</mark>; arriba el peligro y abajo el número ONU.","Manual NRBQ")

q("NRBQ","normal",
 "Según el ADR, en la clase 1 (explosivos), ¿cuál es la división más peligrosa?",
 ["La 1.4.","La 1.1.","La 1.6."],1,
 "La <mark>clase 1</mark> agrupa las materias y objetos explosivos, divididos según su grado de peligro.",
 "De mayor a menor peligro el orden es <mark>1.1, 1.5, 1.2, 1.3, 1.6 y 1.4</mark>. La <mark>1.1</mark> es la más peligrosa y la <mark>1.4</mark>, la menos.",
 "El orden no es numérico: la 1.5 va justo detrás de la 1.1.",
 "Más peligrosa: <mark>1.1</mark> · Menos peligrosa: <mark>1.4</mark>.","Manual NRBQ, Clase 1")

q("NRBQ","normal",
 "Según el manual NRBQ, una sustancia con una DL50 baja es:",
 ["Poco tóxica.","Muy tóxica.","No tóxica por inhalación."],1,
 "La <mark>DL50</mark> (dosis letal 50) es la dosis que causa la muerte del 50 % de una población animal de prueba.",
 "Si hace falta <mark>poca cantidad</mark> para matar a la mitad, la sustancia es <mark>muy tóxica</mark>. Por eso, cuanto <mark>más baja</mark> es la DL50, más potente es el tóxico.",
 "Es una relación inversa: al aumentar la DL50, baja la toxicidad.",
 "<mark>DL50 baja = muy tóxica</mark>. Para gases se usa la CL50 (concentración letal).","Manual NRBQ, Toxicología")

q("NRBQ","normal",
 "Según el manual NRBQ, el IPVS (o IDLH) es:",
 ["La concentración que supone un peligro inmediato para la vida o la salud.","La concentración a la que se percibe el olor de una sustancia.","La concentración máxima para trabajar 8 horas al día."],0,
 "Los detectores de gases usan varios <mark>valores límite</mark> de exposición.",
 "El <mark>IPVS/IDLH</mark> es el nivel que representa un <mark>peligro inmediato para la vida o la salud</mark>: alcanzarlo, aunque sea unos instantes, puede causar la muerte o un daño irreversible.",
 "Si una sustancia no tiene IDLH determinado, se recomienda aplicar <mark>10 veces</mark> su valor TLV/TWA.",
 "<mark>IPVS = peligro inmediato</mark>. Cuidado si el umbral de olor es mayor que el IPVS: no da tiempo a notarlo.","Manual NRBQ")

q("NRBQ","normal",
 "Según el manual NRBQ, el límite TLV/STEL se refiere a exposiciones de una duración no superior a:",
 ["15 minutos.","1 hora.","8 horas."],0,
 "Los <mark>TLV</mark> son valores límite de exposición a sustancias en el trabajo.",
 "El <mark>TLV/STEL</mark> es la concentración que permite trabajar en periodos de <mark>no más de 15 minutos</mark>. El TLV/TWA es la media ponderada para una jornada.",
 "No confundir STEL (exposición corta) con TWA (jornada completa).",
 "<mark>STEL = 15 minutos</mark> · TWA = jornada · C = valor techo que no se puede superar nunca.","Manual NRBQ")

q("NRBQ","normal",
 "Según las normas del número de identificación de peligro, cuando basta una sola cifra para indicar el peligro de una materia:",
 ["El número se completa con un cero.","Se repite la cifra.","Se añade la letra X."],0,
 "El número de peligro siempre tiene, al menos, <mark>dos cifras</mark>.",
 "Si con una cifra basta para describir el peligro, se completa con un <mark>0</mark>. Por ejemplo, un 30 indica solo el peligro que representa el 3.",
 "Repetir la cifra no es «rellenar»: significa que ese peligro se <mark>intensifica</mark>.",
 "<mark>0 = relleno</mark> · <mark>cifra doble = más peligro</mark> · <mark>X = reacciona con el agua</mark>.","Manual NRBQ")

q("Tráfico (APRAT)","normal",
 "Según el APRAT, cuando la deformación del vehículo atrapa a la víctima por algún miembro (pies, piernas, brazos), el nivel de atrapamiento es:",
 ["Mecánico.","Físico 1.","Físico 2."],2,
 "El APRAT define <mark>tres niveles de atrapamiento</mark> para decidir cómo será el rescate.",
 "<mark>Mecánico</mark>: la estructura del vehículo bloquea las salidas. <mark>Físico 1</mark>: las lesiones le impiden salir por su propio pie. <mark>Físico 2</mark>: la deformación del vehículo le <mark>atrapa algún miembro</mark>.",
 "El atrapamiento exterior también se considera Físico 2.",
 "<mark>Mecánico = puertas</mark> · <mark>Físico 1 = lesiones</mark> · <mark>Físico 2 = miembros atrapados</mark>.","APRAT II, Niveles de atrapamiento")

q("Tráfico (APRAT)","normal",
 "Según el APRAT, la vía de extracción del conductor que respeta un ángulo de 0º del eje espinal es:",
 ["La puerta del conductor.","El portón o la zona trasera del vehículo.","El hueco del techo retirado."],1,
 "Siempre se busca la salida que <mark>menos gire la columna</mark> de la víctima.",
 "Para el conductor, la vía que respeta los <mark>0º</mark> es el <mark>portón trasero</mark>: la víctima sale en línea recta, tumbada sobre la tabla, sin giros.",
 "Por la puerta del conductor habría que girarla 90º.",
 "<mark>0º = portón trasero</mark>.","APRAT II, Salidas de extracción")

q("CTE DB-SI","normal",
 "Según el DB-SI 5, los huecos de fachada para el acceso de los bomberos deben tener unas dimensiones mínimas de:",
 ["0,80 m de anchura y 1,20 m de altura.","0,60 m de anchura y 1,00 m de altura.","1,00 m de anchura y 2,00 m de altura."],0,
 "Las fachadas deben tener <mark>huecos</mark> que permitan a los bomberos entrar en cada planta desde el exterior.",
 "Deben medir al menos <mark>0,80 m en horizontal</mark> y <mark>1,20 m en vertical</mark>, con el alféizar a <mark>no más de 1,20 m</mark> del suelo de la planta, y separados como máximo <mark>25 m</mark> entre ejes.",
 "El 1,20 m aparece dos veces: es la altura mínima del hueco y la altura máxima del alféizar.",
 "Huecos: <mark>0,80 × 1,20 m</mark> · alféizar <mark>≤ 1,20 m</mark> · cada <mark>25 m</mark> como máximo.","CTE DB-SI 5")

q("CTE DB-SI","normal",
 "Según el DB-SI 5, ¿a partir de qué altura de evacuación descendente debe tener un edificio un espacio de maniobra para los bomberos?",
 ["Más de 9 m.","Más de 15 m.","Más de 28 m."],0,
 "El <mark>espacio de maniobra</mark> es la zona junto a la fachada donde se colocan los vehículos de bomberos, sobre todo las autoescalas.",
 "Lo necesitan los edificios con una altura de evacuación descendente de <mark>más de 9 m</mark>, a lo largo de las fachadas donde están los accesos.",
 "28 m es la altura a partir de la cual hace falta un ascensor de emergencia.",
 "Espacio de maniobra: <mark>más de 9 m</mark> · Ascensor de emergencia: <mark>más de 28 m</mark>.","CTE DB-SI 5")

q("CTE DB-SI","normal",
 "Según el DB-SI 4, un hospital debe contar con comunicación telefónica directa con el servicio de bomberos si dispone de:",
 ["Más de 100 camas.","Más de 50 camas.","Más de 500 camas."],0,
 "El DB-SI 4 fija qué instalaciones de protección contra incendios necesita cada uso.",
 "En uso hospitalario, si el edificio tiene <mark>más de 100 camas</mark>, debe tener <mark>comunicación telefónica directa</mark> con los bomberos.",
 "Es una exigencia propia del uso hospitalario, donde la evacuación es más lenta y compleja.",
 "Hospital: <mark>más de 100 camas → línea directa con bomberos</mark>.","CTE DB-SI 4")

q("Ascensores","normal",
 "Según el manual de rescate en ascensores, un ascensor de emergencia es obligatorio en edificios con una altura de evacuación superior a:",
 ["15 m, en todos los usos.","28 m (15 m en uso hospitalario).","50 m."],1,
 "El <mark>ascensor de emergencia</mark> es de uso prioritario para los bomberos en caso de incendio.",
 "Es obligatorio por encima de <mark>28 m</mark> de altura de evacuación, y por encima de <mark>15 m</mark> en uso <mark>hospitalario</mark> y de tratamiento intensivo.",
 "Debe tener dos fuentes de alimentación independientes; la segunda tiene que garantizar <mark>al menos una hora</mark> de funcionamiento a plena carga.",
 "Ascensor de emergencia: <mark>más de 28 m</mark> (hospitales, <mark>más de 15 m</mark>).","Manual de rescate en ascensores")

q("Ascensores","normal",
 "Según el CTE, un ascensor de emergencia debe tener, como mínimo, una capacidad de carga de:",
 ["450 kg.","630 kg.","1.000 kg."],1,
 "El ascensor de emergencia tiene que poder llevar a bomberos con su equipo o a una persona en camilla.",
 "Mínimos: carga de <mark>630 kg</mark>, cabina de <mark>1,10 × 1,40 m</mark>, paso de <mark>1,00 m</mark> y una velocidad que le permita hacer todo su recorrido en <mark>menos de 60 s</mark>.",
 "Los 60 segundos son para todo el recorrido, no por planta.",
 "<mark>630 kg · 1,10 × 1,40 m · menos de 60 s</mark>.","CTE DB-SI 5")

q("Ascensores","normal",
 "Según el manual, los faldones de la cabina de un ascensor, ya sean fijos o telescópicos, deben tener una longitud total de:",
 ["500 mm.","750 mm.","1.000 mm."],1,
 "El <mark>faldón</mark> es una chapa bajo la puerta de la cabina que tapa el hueco del foso cuando la cabina se para entre dos pisos.",
 "Fijo o telescópico, debe medir <mark>750 mm</mark> en total. El telescópico tiene una parte fija de al menos <mark>200 mm</mark>.",
 "Su función es evitar que alguien caiga al foso al salir de una cabina parada entre plantas.",
 "Faldón: <mark>750 mm</mark>.","Manual de rescate en ascensores")

q("Régimen local","normal",
 "Según el art. 26 de la Ley 7/1985, el transporte colectivo urbano de viajeros es un servicio obligatorio en los municipios de más de:",
 ["5.000 habitantes.","20.000 habitantes.","50.000 habitantes."],2,
 "Los servicios mínimos obligatorios aumentan con la población del municipio.",
 "Por encima de <mark>50.000 habitantes</mark> se añaden el <mark>transporte colectivo urbano</mark> y el <mark>medio ambiente urbano</mark>.",
 "Con más de 20.000 entran la protección civil y la extinción de incendios.",
 "<mark>50.000 → transporte urbano y medio ambiente</mark>.","Ley 7/1985, art. 26")

q("Régimen local","normal",
 "Según la Ley 22/2006, de Capitalidad y de Régimen Especial de Madrid, la presidencia de cada Distrito corresponde:",
 ["A un vecino elegido por la Junta de Distrito.","En todo caso, a un Concejal.","Al funcionario de mayor categoría del Distrito."],1,
 "Los <mark>Distritos</mark> son divisiones territoriales con órganos de gestión desconcentrada, para acercar la gestión municipal y fomentar la participación ciudadana.",
 "El Pleno debe crearlos, y su presidencia corresponde <mark>en todo caso a un Concejal</mark>.",
 "La participación vecinal se canaliza a través del Distrito, pero la presidencia siempre es de un Concejal.",
 "Distrito: <mark>lo crea el Pleno, lo preside un Concejal</mark>.","Ley 22/2006, art. 22")

q("Régimen local","normal",
 "Según el art. 22 de la Ley 7/1985, la votación de la moción de censura al Alcalde en el Pleno es:",
 ["Secreta.","Pública y por llamamiento nominal.","A mano alzada y anónima."],1,
 "La <mark>moción de censura</mark> permite al Pleno destituir al Alcalde.",
 "La votación de la moción de censura y la de la cuestión de confianza son <mark>públicas</mark> y se hacen <mark>por llamamiento nominal</mark> en todo caso: cada concejal vota en voz alta cuando se le nombra.",
 "Se rigen por la legislación electoral general.",
 "Censura y confianza: <mark>públicas y nominales</mark>.","Ley 7/1985, art. 22.3")

q("Haciendas locales","normal",
 "Según el TRLRHL, lo recaudado por contribuciones especiales solo puede destinarse a:",
 ["Cualquier gasto del presupuesto municipal.","Los gastos de la obra o del servicio por el que se exigieron.","Reducir la deuda municipal."],1,
 "Las <mark>contribuciones especiales</mark> las pagan quienes se benefician especialmente de una obra o de la ampliación de un servicio.",
 "Por eso el dinero es <mark>finalista</mark>: solo puede usarse para <mark>sufragar esa obra o ese servicio</mark>.",
 "No se pueden destinar a otros gastos municipales.",
 "Contribución especial: <mark>solo para la obra que la origina</mark>.","TRLRHL, art. 29")

q("Haciendas locales","normal",
 "Según el TRLRHL, el importe de los precios públicos debe cubrir, como mínimo:",
 ["El coste del servicio prestado o de la actividad realizada.","La mitad del coste del servicio.","El coste más un 10 % de beneficio."],0,
 "Los <mark>precios públicos</mark> se cobran por servicios o actividades que no son obligatorios para el ciudadano.",
 "Como regla general deben cubrir <mark>como mínimo el coste</mark> del servicio o actividad.",
 "Por razones sociales, benéficas, culturales o de interés público, pueden fijarse <mark>por debajo</mark> de ese coste.",
 "Precio público: <mark>al menos el coste</mark>, salvo razones de interés público.","TRLRHL, art. 44")

q("Reglamento Bomberos","normal",
 "Según el Reglamento del Cuerpo de Bomberos, su personal tiene la consideración de:",
 ["Personal laboral fijo.","Funcionario de carrera de Servicios Especiales.","Funcionario interino de Administración General."],1,
 "El Reglamento define la naturaleza del personal y del Cuerpo.",
 "El personal es <mark>funcionario de carrera de Servicios Especiales</mark>. El Cuerpo está jerarquizado y tiene <mark>carácter civil</mark>.",
 "Que esté jerarquizado no lo convierte en un cuerpo militar.",
 "Bomberos: <mark>funcionarios de carrera de Servicios Especiales</mark>, cuerpo <mark>civil</mark> y jerarquizado.","Reglamento del Cuerpo de Bomberos, art. 5")

q("Reglamento Bomberos","normal",
 "Según el Reglamento del Cuerpo de Bomberos, ¿qué categorías forman la escala Ejecutiva u Operativa?",
 ["Jefe de Departamento, Jefe de Sección y Oficiales.","Suboficiales, Sargentos, Cabos, Bombero y Bombero conductor.","Oficiales, Suboficiales y Sargentos."],1,
 "Todo el personal forma una sola línea jerárquica con <mark>dos escalas</mark>.",
 "<mark>Escala Técnica o de Mando</mark>: Jefe de Departamento (Inspector Jefe), Jefe de Sección (Subinspector) y Oficiales. <mark>Escala Ejecutiva u Operativa</mark>: <mark>Suboficiales, Sargentos, Cabos, Bombero y Bombero conductor</mark>.",
 "Los Oficiales son de la escala de Mando; los Suboficiales ya son de la Operativa.",
 "Mando: <mark>hasta Oficiales</mark> · Operativa: <mark>desde Suboficiales</mark>.","Reglamento del Cuerpo de Bomberos, art. 6")

q("Reglamento Bomberos","normal",
 "Según el Reglamento del Cuerpo de Bomberos, ¿quién tiene derecho a pedir la actuación del Servicio en una situación de siniestro?",
 ["Solo los mayores de edad.","Toda persona, incluso un menor de edad.","Solo el propietario del inmueble afectado."],1,
 "El Servicio de Extinción de Incendios es un servicio esencial para la protección civil.",
 "<mark>Toda persona, incluso el menor de edad</mark>, tiene derecho a pedir su actuación en una situación de siniestro o calamidad. El Ayuntamiento <mark>denunciará las falsas alarmas</mark>.",
 "Además, la recepción y el uso del Servicio por parte de los ciudadanos se declaran <mark>obligatorios</mark>.",
 "Pedir ayuda: <mark>cualquiera, también un menor</mark>.","Reglamento del Cuerpo de Bomberos, art. 1")

q("Electricidad","normal",
 "Según el manual, se considera baja tensión la de las instalaciones con una tensión nominal igual o inferior a:",
 ["1.000 V en alterna y 1.500 V en continua.","400 V en alterna y 600 V en continua.","50 V en alterna y 75 V en continua."],0,
 "Las instalaciones se clasifican según su tensión, y cada tipo tiene su reglamento.",
 "<mark>Baja tensión</mark>: hasta <mark>1.000 V en alterna</mark> y <mark>1.500 V en continua</mark>. Por encima, alta tensión.",
 "50 V en alterna y 75 V en continua son los límites de la <mark>muy baja tensión de seguridad</mark>.",
 "BT: <mark>1.000 V CA · 1.500 V CC</mark>.","Instalaciones eléctricas")

q("Electricidad","normal",
 "Según el manual, la red de transporte de energía eléctrica trabaja con tensiones de:",
 ["220 a 400 kV.","20 a 30 kV.","230 a 400 V."],0,
 "La electricidad se transporta a <mark>muy alta tensión</mark> para perder menos energía en el camino.",
 "La red de transporte trabaja entre <mark>220 y 400 kV</mark>. Después, las subestaciones la bajan para distribuirla.",
 "230/400 V es la tensión que llega a las viviendas, no la de transporte.",
 "Transporte: <mark>220-400 kV</mark> · Vivienda: <mark>230/400 V</mark>.","Instalaciones eléctricas")

q("Electricidad","normal",
 "En un sistema trifásico, las tres tensiones están desfasadas entre sí:",
 ["90°.","120°.","180°."],1,
 "La corriente <mark>trifásica</mark> son tres corrientes alternas de la misma frecuencia y el mismo valor eficaz.",
 "Las tres están desfasadas <mark>120°</mark>, es decir, un tercio de vuelta: así se reparten de forma equilibrada.",
 "120° × 3 = 360°, una vuelta completa.",
 "Trifásica: <mark>3 fases a 120°</mark>.","Instalaciones eléctricas")

q("ACS","normal",
 "Según el CTE (HS4), en cada punto de consumo de agua caliente sanitaria la presión debe estar entre:",
 ["1 y 5 bar.","0,5 y 2 bar.","5 y 10 bar."],0,
 "La presión en los grifos debe ser suficiente para usarlos y no tan alta que dañe la instalación.",
 "El HS4 exige en cada punto de consumo un <mark>mínimo de 1 bar</mark> y un <mark>máximo de 5 bar</mark>.",
 "Los depósitos de acumulación trabajan a más presión (mínimo 6 bar), pero eso no es la presión en el grifo.",
 "Grifo: <mark>1-5 bar</mark>.","Manual de ACS")

q("ACS","normal",
 "Según el manual de ACS, ¿por qué el acero galvanizado no debe usarse para agua a más de 60 °C?",
 ["Porque lo prohíbe expresamente el CTE (HS4).","Porque se funde a esa temperatura.","Porque es más caro que el cobre."],0,
 "El material de las tuberías debe soportar la temperatura y la presión del agua.",
 "El CTE <mark>prohíbe expresamente</mark> el acero galvanizado para temperaturas de <mark>más de 60 °C</mark>.",
 "Los termoplásticos aguantan menos presión cuanto más caliente está el agua; por eso hay que elegir bien su tipo y categoría.",
 "Galvanizado: <mark>nunca por encima de 60 °C</mark>.","Manual de ACS")

q("ACS","normal",
 "Según el manual de ACS, para prevenir la legionelosis, la temperatura de trabajo de los depósitos de acumulación no debe ser inferior a:",
 ["40 °C.","55 °C.","70 °C."],2,
 "La <mark>legionela</mark> es una bacteria que se multiplica en el agua tibia estancada y puede causar neumonías graves.",
 "Los depósitos de acumulación deben trabajar a <mark>70 °C o más</mark> y a una presión mínima de <mark>6 bar</mark> (recomendable 8).",
 "Los <mark>interacumuladores</mark> producen el agua caliente ellos mismos; los <mark>acumuladores</mark> solo la almacenan.",
 "Acumulación: <mark>al menos 70 °C</mark>, por la legionela.","Manual de ACS")

q("Trabajos en altura","normal",
 "Según la NTP de trabajos verticales, cuando se trabaja cerca de líneas eléctricas hay que solicitar su desconexión si la distancia es o puede ser menor de:",
 ["1 m.","3 m.","5 m."],2,
 "Trabajar cerca de líneas eléctricas tiene riesgo de <mark>electrocución</mark>, incluso sin llegar a tocarlas.",
 "Hay que pedir la <mark>desconexión</mark> mientras duren los trabajos si la distancia es o puede ser <mark>menor de 5 m</mark>.",
 "Si en líneas aéreas no es posible desconectar, hay que adoptar otras medidas de protección.",
 "Líneas eléctricas: <mark>menos de 5 m → pedir desconexión</mark>.","NTP sobre trabajos verticales")

q("Trabajos en altura","normal",
 "En los trabajos verticales, ¿qué función tiene cada cuerda?",
 ["La de trabajo sirve para acceder, descender y apoyarse; la de seguridad, como anticaídas.","Las dos sirven para descender a la vez.","La de seguridad sirve para subir material."],0,
 "En los trabajos verticales el operario está suspendido de <mark>dos cuerdas</mark> independientes.",
 "La <mark>cuerda de trabajo</mark> es el medio de acceso, descenso y apoyo. La <mark>cuerda de seguridad</mark> es el sistema <mark>anticaídas</mark> por si falla la de trabajo.",
 "Cada cuerda tiene su propio anclaje: si los dos dependieran del mismo punto, no habría seguridad real.",
 "<mark>Trabajo = moverse</mark> · <mark>Seguridad = no caer</mark>.","NTP sobre trabajos verticales")

q("EBEP","normal",
 "Según el art. 85 del TREBEP, ¿cuál de estas NO es una situación administrativa de los funcionarios de carrera?",
 ["Servicios especiales.","Excedencia.","Jubilación."],2,
 "Las <mark>situaciones administrativas</mark> describen en qué posición se encuentra un funcionario respecto a su puesto.",
 "Son cinco: <mark>servicio activo</mark>, <mark>servicios especiales</mark>, <mark>servicio en otras Administraciones Públicas</mark>, <mark>excedencia</mark> y <mark>suspensión de funciones</mark>.",
 "La <mark>jubilación</mark> no es una situación: es una causa de <mark>pérdida</mark> de la condición de funcionario.",
 "Situaciones: <mark>activo, especiales, otras Administraciones, excedencia, suspensión</mark>.","TREBEP, art. 85")

q("EBEP","normal",
 "Según el art. 10 del TREBEP, un funcionario interino nombrado para cubrir una plaza vacante puede ocuparla como máximo:",
 ["1 año.","3 años.","5 años."],1,
 "Se nombra un interino para una vacante cuando no es posible cubrirla con un funcionario de carrera.",
 "En ese caso el límite es de <mark>tres años</mark>.",
 "El de la acumulación de tareas es distinto: 9 meses dentro de 18.",
 "Vacante: <mark>máximo 3 años</mark>.","TREBEP, art. 10")

q("EBEP","normal",
 "Según el art. 67 del TREBEP, la jubilación forzosa se declara de oficio al cumplir el funcionario:",
 ["60 años.","65 años.","70 años."],1,
 "La jubilación puede ser <mark>voluntaria</mark>, <mark>forzosa</mark> o por <mark>incapacidad permanente</mark>.",
 "La <mark>forzosa</mark> se declara de oficio a los <mark>65 años</mark>. Las leyes de Función Pública pueden permitir solicitar la prolongación en el servicio activo.",
 "La voluntaria depende de los requisitos del régimen de Seguridad Social que corresponda.",
 "Jubilación forzosa: <mark>65 años</mark>.","TREBEP, art. 67")

q("Procedimiento administrativo","normal",
 "Según el art. 56 de la Ley 39/2015, las medidas provisionales adoptadas antes de iniciar el procedimiento deben confirmarse, modificarse o levantarse en el acuerdo de iniciación, que debe dictarse en un plazo de:",
 ["10 días.","15 días.","1 mes."],1,
 "Las <mark>medidas provisionales</mark> aseguran que la resolución final pueda cumplirse; en casos de urgencia se pueden tomar incluso antes de abrir el procedimiento.",
 "Si se adoptan antes, el procedimiento debe iniciarse en los <mark>15 días siguientes</mark>, y el acuerdo de iniciación debe pronunciarse sobre ellas.",
 "Si no se inicia en ese plazo, o el acuerdo no dice nada de ellas, las medidas <mark>quedan sin efecto</mark>.",
 "Medidas previas: <mark>15 días</mark> para iniciar o decaen.","Ley 39/2015, art. 56")

q("Procedimiento administrativo","normal",
 "Según el art. 56 de la Ley 39/2015, las medidas provisionales deben respetar los principios de:",
 ["Proporcionalidad, efectividad y menor onerosidad.","Celeridad, economía y eficacia.","Publicidad, igualdad y mérito."],0,
 "Una medida provisional limita derechos antes de que haya una resolución final.",
 "Por eso debe ser <mark>proporcionada</mark>, <mark>efectiva</mark> y la <mark>menos gravosa</mark> posible (menor onerosidad), y estar motivada.",
 "Mérito y capacidad son principios del acceso al empleo público, no de las medidas provisionales.",
 "Medidas provisionales: <mark>proporcionalidad, efectividad y menor onerosidad</mark>.","Ley 39/2015, art. 56")

q("Procedimiento administrativo","normal",
 "Según el art. 3 de la Ley 39/2015, los menores de edad tienen capacidad de obrar ante las Administraciones Públicas:",
 ["Nunca.","Para los derechos e intereses cuya actuación permite la ley sin la asistencia de quien ejerce la patria potestad, tutela o curatela.","Solo a partir de los 16 años y para cualquier trámite."],1,
 "La <mark>capacidad de obrar</mark> es la aptitud para actuar por uno mismo ante la Administración.",
 "La tienen las personas con capacidad según las normas civiles y también los <mark>menores</mark>, para los derechos e intereses que la ley les permite ejercer <mark>sin asistencia</mark> de padres o tutores.",
 "Se exceptúan los menores incapacitados cuando la incapacitación afecte a ese derecho.",
 "Menores: <mark>sí, cuando la ley les deja actuar solos</mark>.","Ley 39/2015, art. 3")

q("Constitución","normal",
 "Según el art. 25.3 CE, la Administración civil:",
 ["Puede imponer sanciones de arresto de hasta 48 horas.","No puede imponer sanciones que impliquen privación de libertad.","Puede privar de libertad si lo autoriza un reglamento."],1,
 "El art. 25 recoge el principio de legalidad en materia penal y sancionadora.",
 "La Administración civil <mark>no puede imponer sanciones</mark> que, directa o subsidiariamente, impliquen <mark>privación de libertad</mark>. Eso queda reservado a los jueces.",
 "Además, nadie puede ser sancionado por algo que no era infracción cuando lo hizo.",
 "Administración civil: <mark>multas sí, cárcel nunca</mark>.","CE, art. 25")

q("Constitución","normal",
 "Según el art. 24.1 CE, todas las personas tienen derecho a la tutela efectiva de jueces y tribunales sin que, en ningún caso, pueda producirse:",
 ["Indefensión.","Una sentencia desfavorable.","Un recurso de la otra parte."],0,
 "La <mark>tutela judicial efectiva</mark> es el derecho a acudir a los tribunales y obtener una respuesta fundada.",
 "Su núcleo es que nunca se produzca <mark>indefensión</mark>: no se puede quedar sin posibilidad de defenderse.",
 "El art. 24.2 añade el juez predeterminado por la ley, la defensa, la presunción de inocencia y el derecho a no declarar contra sí mismo.",
 "Art. 24: <mark>tutela efectiva sin indefensión</mark>.","CE, art. 24")

q("Constitución","normal",
 "Según el art. 28.1 CE, sobre la libertad sindical:",
 ["Todos los funcionarios están obligados a afiliarse a un sindicato.","Nadie puede ser obligado a afiliarse a un sindicato.","Solo pueden sindicarse los trabajadores del sector privado."],1,
 "La <mark>libertad sindical</mark> incluye fundar sindicatos y afiliarse al que se elija.",
 "También tiene una vertiente negativa: <mark>nadie puede ser obligado a afiliarse</mark>. La ley puede limitar este derecho en las Fuerzas o Institutos armados y regular sus peculiaridades para los funcionarios.",
 "Los funcionarios sí pueden sindicarse, con las peculiaridades que fije la ley.",
 "Libertad sindical: <mark>afiliarse o no, libremente</mark>.","CE, art. 28")

q("PRL","normal",
 "Según el art. 3 de la Ley 31/1995, ¿se aplica la Ley de Prevención al personal funcionario de las Administraciones Públicas?",
 ["No, solo a los trabajadores con contrato laboral.","Sí, con las peculiaridades que recoge la propia Ley o sus normas de desarrollo.","Solo si lo acuerda cada Administración."],1,
 "La Ley de Prevención no es solo para las empresas privadas.",
 "Se aplica a las relaciones laborales y también a las de <mark>carácter administrativo o estatutario</mark> del personal de las Administraciones Públicas, <mark>con sus peculiaridades</mark>.",
 "Solo quedan fuera actividades concretas, como los servicios operativos de protección civil en catástrofes.",
 "LPRL: <mark>también para funcionarios</mark>, con peculiaridades.","Ley 31/1995, art. 3.1")

q("Protección civil","normal",
 "Según el art. 1 de la Ley 17/2015, la protección civil se define como:",
 ["Un instrumento de la política de seguridad pública.","Un servicio de voluntariado privado.","Una competencia exclusiva de los ayuntamientos."],0,
 "La Ley crea el <mark>Sistema Nacional de Protección Civil</mark>.",
 "La protección civil es un <mark>instrumento de la política de seguridad pública</mark>: el servicio público que protege a personas y bienes ante emergencias y catástrofes de origen natural o humano, accidental o intencionado.",
 "Participan todas las Administraciones; el voluntariado colabora, pero no la define.",
 "Protección civil: <mark>servicio público de seguridad pública</mark>.","Ley 17/2015, art. 1")

q("Protección civil","normal",
 "Según el art. 6 de la Ley 17/2015, la información a los ciudadanos sobre los riesgos colectivos debe darse:",
 ["Solo cuando se produce la emergencia.","Tanto en caso de emergencia como preventivamente.","Solo si los ciudadanos la solicitan."],1,
 "Todos tienen <mark>derecho a ser informados</mark> de los riesgos colectivos importantes que les afecten y de cómo actuar.",
 "La información se da <mark>en la emergencia</mark> y también <mark>preventivamente</mark>, antes de que el peligro esté presente.",
 "Prevenir es parte de la protección civil: informar después ya es tarde.",
 "Información: <mark>antes y durante</mark>.","Ley 17/2015, art. 6")

q("Protección civil","normal",
 "Según el art. 7 bis de la Ley 17/2015, cuando una emergencia exige entrar en un domicilio y evacuar a personas en peligro, se aplica lo dispuesto en:",
 ["El art. 15.2 de la Ley Orgánica 4/2015, de protección de la seguridad ciudadana.","El art. 18.2 del Código Penal.","El Reglamento de cada Cuerpo de Bomberos."],0,
 "Entrar en un domicilio sin permiso afecta a un derecho fundamental, así que debe estar cubierto por una ley.",
 "La Ley de Protección Civil remite al <mark>art. 15.2 de la LO 4/2015</mark> de seguridad ciudadana, que permite la entrada para <mark>evitar daños inminentes y graves</mark> a personas y cosas en catástrofe, calamidad, ruina inminente o casos de extrema y urgente necesidad.",
 "El art. 18.2 que protege el domicilio es de la Constitución, no del Código Penal.",
 "Entrada por emergencia: <mark>LO 4/2015, art. 15.2</mark>.","Ley 17/2015, art. 7 bis")

q("Atención sanitaria","normal",
 "Según el manual de atención inicial, el pulso normal de un adulto está entre:",
 ["40 y 60 latidos por minuto.","60 y 100 latidos por minuto.","100 y 140 latidos por minuto."],1,
 "El <mark>pulso</mark> indica cuántas veces late el corazón por minuto.",
 "En un adulto lo normal es entre <mark>60 y 100 lpm</mark>. Por debajo es bradicardia y por encima, taquicardia.",
 "Un pulso rápido y débil, con relleno capilar lento, puede indicar shock.",
 "Pulso: <mark>60-100 lpm</mark>.","Manual de atención inicial al paciente")

q("Agua fría","normal",
 "Según el Canal de Isabel II, la acometida contra incendios de un edificio debe ser:",
 ["La misma que la de agua potable.","Siempre independiente.","Opcional en edificios de viviendas."],1,
 "La <mark>acometida</mark> une la red de distribución con la instalación del edificio.",
 "Como regla, cada instalación tiene <mark>una sola acometida</mark>, pero la <mark>de incendios debe ser siempre independiente</mark>, para que el agua para extinción no dependa del consumo doméstico.",
 "Edificios especiales como los hospitales pueden tener dos acometidas en anillo.",
 "Incendios: <mark>acometida independiente siempre</mark>.","Manual de agua fría para consumo humano")

q("Agua fría","normal",
 "Según el manual, ¿qué edificios pueden abastecerse mediante dos acometidas en una distribución en anillo?",
 ["Cualquier edificio de viviendas.","Edificios especiales como los hospitales.","Solo los edificios industriales."],1,
 "Lo normal es que cada instalación de agua potable tenga <mark>una sola acometida</mark>.",
 "Los <mark>edificios especiales</mark>, como los <mark>hospitales</mark>, pueden tener <mark>dos acometidas en anillo</mark>, para no quedarse sin agua si falla una.",
 "No confundir con la acometida de incendios, que siempre es independiente en todos los edificios.",
 "Dos acometidas: <mark>hospitales y edificios especiales</mark>.","Manual de agua fría para consumo humano")

q("Accesos forzados","normal",
 "Según el manual de accesos forzados, ¿dónde se instala el picaporte con condena?",
 ["En puertas exteriores de vivienda.","En puertas de baño, en el interior de las viviendas.","En puertas cortafuegos."],1,
 "El <mark>picaporte con condena</mark> es una cerradura sencilla que se bloquea desde dentro.",
 "No se instala en puertas exteriores, sino en <mark>puertas de baño</mark> dentro de la vivienda. La intervención típica es la de un <mark>niño que se encierra</mark> en el baño y no sabe abrir.",
 "La manilla actúa sobre el resbalón mediante un cuadradillo de 8 mm.",
 "Condena: <mark>puerta de baño</mark>, caso típico de un niño encerrado.","Manual de accesos forzados")

q("Accesos forzados","normal",
 "Según el manual, ¿qué diferencia a una puerta acorazada de una blindada?",
 ["La acorazada tiene bisagras mucho más robustas y una cerradura con varios cierres antiapalancamiento.","La acorazada es de madera sin refuerzo.","No hay diferencia: son dos nombres para la misma puerta."],0,
 "Las puertas se ordenan de menos a más resistencia: <mark>estándar</mark>, <mark>blindada</mark> y <mark>acorazada</mark>.",
 "La blindada ya tiene más bisagras y refuerzo antipalanca. La <mark>acorazada</mark> tiene <mark>bisagras mucho más robustas</mark> y una cerradura con <mark>varios cierres antiapalancamiento</mark>.",
 "La puerta de madera sin refuerzo es la estándar.",
 "Estándar → blindada → <mark>acorazada (la más resistente)</mark>.","Manual de accesos forzados")

q("Gas y GLP","normal",
 "Según el manual, al licuar los GLP a presión su volumen se reduce aproximadamente:",
 ["10 veces.","240 veces.","1.000 veces."],1,
 "Los <mark>GLP</mark> (propano y butano) se guardan licuados para poder transportar mucha cantidad en poco espacio.",
 "Al licuarlos a presión, su volumen se reduce unas <mark>240 veces</mark>. Por eso una fuga de líquido produce muchísimo gas.",
 "Dentro del envase conviven una fase líquida y otra gaseosa.",
 "GLP licuado: <mark>240 veces menos volumen</mark>.","Manual de GLP")

q("Corte y soldadura","normal",
 "Según el manual de corte térmico, ¿a qué presiones aproximadas se regulan el oxígeno y el Chemtane?",
 ["Oxígeno de 2 a 5 bar y Chemtane unos 0,5 bar.","Oxígeno a 0,5 bar y Chemtane de 2 a 5 bar.","Los dos a 10 bar."],0,
 "Cada gas tiene su <mark>regulador</mark>, que baja la presión de la botella a la de trabajo.",
 "El <mark>oxígeno</mark> se regula de <mark>2 a 5 bar</mark>, según el espesor que se vaya a cortar. El <mark>Chemtane</mark>, a unos <mark>0,5 bar</mark>.",
 "Invertirlas es la trampa: el oxígeno es el que va a más presión, porque es el que corta.",
 "<mark>Oxígeno 2-5 bar</mark> · <mark>Chemtane 0,5 bar</mark>.","Manual de corte térmico")

q("Apícola","normal",
 "Según el manual de rescate apícola, durante la enjambrazón, ¿quién abandona la colonia?",
 ["Las nuevas reinas recién nacidas.","La reina vieja, con parte de la colonia.","Solo los zánganos."],1,
 "La <mark>enjambrazón</mark> es la forma natural en la que una colonia de abejas se divide.",
 "Al sobrealimentar algunas larvas con jalea real, a los <mark>16 días</mark> nacen nuevas reinas. Unas horas antes, la <mark>reina vieja abandona la colonia</mark> con parte de las abejas y forma un enjambre.",
 "Muchos de esos enjambres buscan refugio en edificios, y de ahí vienen muchas intervenciones.",
 "Enjambre = <mark>reina vieja + parte de la colonia</mark>.","Manual de rescate apícola")

q("Igualdad","normal",
 "Según el art. 3 de la LO 3/2007, el principio de igualdad de trato entre mujeres y hombres supone:",
 ["La ausencia de toda discriminación, directa o indirecta, por razón de sexo.","La obligación de contratar el mismo número de mujeres y hombres.","Que hombres y mujeres cobren siempre lo mismo, sea cual sea el puesto."],0,
 "Es el principio básico sobre el que se construye toda la ley.",
 "Supone la <mark>ausencia de toda discriminación</mark>, <mark>directa o indirecta</mark>, por razón de sexo, y especialmente la derivada de la <mark>maternidad</mark>, las <mark>obligaciones familiares</mark> y el <mark>estado civil</mark>.",
 "La paridad numérica no es la definición de este principio.",
 "Igualdad de trato: <mark>sin discriminación directa ni indirecta</mark>.","LO 3/2007, art. 3")

q("Vehículos","normal",
 "Según la información de vehículos del SEI, la autoescala convencional de 27 m es de la marca:",
 ["Metz.","Riffaud.","Magirus."],0,
 "El Servicio dispone de autoescalas de distintas alturas y marcas.",
 "La autoescala de <mark>27 m</mark> es de la marca <mark>Metz</mark>. La <mark>articulada de 32 m</mark> es de <mark>Riffaud</mark>.",
 "No confundir las dos: cambian la altura, la marca y el tipo.",
 "<mark>Metz 27 m</mark> · <mark>Riffaud articulada 32 m</mark>.","Información de vehículos del SEI")

open(P,'w',encoding='utf-8').write('[\n'+',\n'.join(json.dumps(x,ensure_ascii=False) for x in Q)+'\n]\n')
print(len(Q), sum(1 for x in Q if x['d']=='difícil'))
