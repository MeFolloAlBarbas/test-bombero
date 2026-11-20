import json
P='/home/claude/test-bombero/preguntas.json'
Q=json.load(open(P,encoding='utf-8'))
nid=max(q['id'] for q in Q)+1
def q(t,d,enun,ops,c,que,porque,ojo,rec,f):
    global nid
    Q.append(dict(id=nid,t=t,d=d,q=enun,o=ops,c=c,que=que,porque=porque,ojo=ojo,rec=rec,f=f)); nid+=1

# ---------------- DIFÍCILES (para las 20:00) ----------------
q("Trabajos en altura","difícil",
 "Un operario con 1 m de cuerda activa sufre una caída de 2 m hasta que el sistema la detiene. ¿Cuál es el factor de caída?",
 ["0,5.","1.","2."],2,
 "El <mark>factor de caída</mark> mide la gravedad de una caída: distancia de caída entre longitud de cuerda activa. No tiene unidades.",
 "FC = <mark>2 m ÷ 1 m = 2</mark>. Con poca cuerda activa, la cuerda casi no puede estirarse para absorber la energía, así que casi toda llega al cuerpo como <mark>fuerza de choque</mark>.",
 "0,5 es hacer la división al revés. Una caída corta con poca cuerda puede ser más grave que una larga con mucha cuerda.",
 "<mark>FC = caída ÷ cuerda activa</mark>, y cuanto más bajo, mejor. Por eso el anclaje debe ir por encima y con la conexión lo más corta posible.","Manual de trabajos en altura, Factor de caída")

q("Trabajos en altura","difícil",
 "Para la cuerda de seguridad (línea de anclaje flexible) en trabajos verticales, ¿sirve una cuerda semiestática de clase B?",
 ["Sí, porque toda cuerda semiestática cumple la UNE-EN 1891.","No, porque la cuerda de seguridad debe garantizar 22 kN y la clase B solo garantiza 18 kN.","Sí, siempre que se use con absorbedor de energía."],1,
 "La UNE-EN 1891 distingue dos clases de cuerda semiestática: <mark>A (22 kN)</mark> y <mark>B (18 kN)</mark>, esta última de duración más limitada.",
 "La cuerda de seguridad en trabajos verticales tiene que dar una resistencia de <mark>22 kN</mark>. Eso solo lo garantiza la <mark>clase A</mark>, que es la más usada en trabajo vertical.",
 "Que las dos sean «UNE-EN 1891» no las hace intercambiables. El absorbedor reduce la fuerza de choque, pero no sube la resistencia de la cuerda.",
 "<mark>Clase A = 22 kN</mark> (la de trabajo) · <mark>Clase B = 18 kN</mark>.","Manual de trabajos en altura, Cuerdas")

q("PRL","difícil",
 "Bomberos actuando en una catástrofe con grave riesgo. Según el art. 3.2 de la Ley 31/1995, en esa actuación concreta:",
 ["La Ley de Prevención se aplica íntegramente.","La Ley no se aplica, aunque inspira su normativa específica.","La Ley no se aplica nunca a los bomberos."],1,
 "La Ley de Prevención de Riesgos Laborales se aplica también a los funcionarios, pero excluye algunas actividades cuyas particularidades lo impiden.",
 "Entre las exclusiones están los <mark>servicios operativos de protección civil en casos de grave riesgo, catástrofe y calamidad pública</mark>. Aun así, la Ley <mark>inspirará</mark> la normativa específica de esas actividades.",
 "La exclusión no es «para los bomberos», sino <mark>para esas situaciones</mark>. En el día a día, la Ley sí se aplica.",
 "Excluidos: policía y aduanas · <mark>protección civil en catástrofe</mark> · Fuerzas Armadas y actividades militares de la Guardia Civil.","Ley 31/1995, art. 3.2")

q("Protección civil","difícil",
 "En una emergencia, la autoridad obliga a un vecino a ayudar personalmente y además requisa su furgoneta, que acaba dañada. Según la Ley 17/2015:",
 ["Tiene derecho a indemnización por los dos conceptos.","No tiene derecho a indemnización por ninguno.","Solo tiene derecho a indemnización por los daños en la furgoneta."],2,
 "El <mark>deber de colaboración</mark> obliga a ciudadanos y empresas a colaborar personal o materialmente cuando lo requiera la autoridad de protección civil.",
 "Las <mark>prestaciones personales</mark> (a partir de la mayoría de edad) se hacen <mark>sin derecho a indemnización</mark>. Pero quien sufre perjuicios en sus bienes por una <mark>requisa</mark> u ocupación <mark>sí</mark> tiene derecho a ser indemnizado.",
 "Las opciones «todo» o «nada» son la trampa: la ley trata distinto a la persona y a los bienes.",
 "<mark>Ayuda personal: gratis</mark> · <mark>Bienes requisados o dañados: se indemnizan</mark>. Las medidas duran solo el tiempo estrictamente necesario.","Ley 17/2015, art. 7 bis")

q("Procedimiento administrativo","difícil",
 "Un ciudadano pide una indemnización por responsabilidad patrimonial y vence el plazo sin resolución notificada. Según el art. 24 de la Ley 39/2015, se entiende:",
 ["Estimada por silencio administrativo.","Desestimada por silencio administrativo.","Caducado el procedimiento."],1,
 "El <mark>silencio administrativo</mark> es lo que se entiende que ha decidido la Administración cuando no contesta a tiempo.",
 "La regla general en lo iniciado a solicitud del interesado es el <mark>silencio estimatorio</mark>. Pero hay excepciones con <mark>silencio desestimatorio</mark>, y una de ellas es la <mark>responsabilidad patrimonial</mark>: si no, bastaría con esperar para cobrar.",
 "La caducidad es para procedimientos iniciados de oficio, no para una solicitud. Otras excepciones desestimatorias: derecho de petición, dominio o servicio público, daño al medio ambiente, impugnación de actos.",
 "Regla: <mark>a solicitud = estimatorio</mark>, salvo excepciones. <mark>Dinero o dominio público = desestimatorio</mark>.","Ley 39/2015, art. 24")

q("Atención sanitaria","difícil",
 "Tras un traumatismo craneal, un herido obtiene 9 puntos en la Escala de Coma de Glasgow. Según el manual, el TCE es:",
 ["Leve.","Moderado.","Grave."],1,
 "La <mark>Escala de Glasgow</mark> valora el nivel de conciencia sumando la respuesta ocular, verbal y motora. Máximo 15 (normal) y mínimo 3.",
 "Clasificación del manual: <mark>14-15 leve</mark> · <mark>9-13 moderado</mark> · <mark>menos de 9 grave</mark>. El 9 es el límite inferior del moderado.",
 "La trampa es el límite: «por debajo de 9» es grave, pero <mark>9 justo es moderado</mark>.",
 "<mark>15-14 / 13-9 / 8-3</mark> = leve / moderado / grave. La escala rápida para el primer interviniente es la AVDN.","Manual de atención inicial al paciente")

q("Agua fría","difícil",
 "Se quiere instalar un hidrante en una conducción de 200 mm que forma parte de la red de transporte (arteria). ¿Es correcto?",
 ["Sí, porque supera los 150 mm.","No, porque en la red de transporte se deben evitar acometidas e hidrantes.","Sí, siempre que tenga acometida independiente."],1,
 "La red de distribución tiene tres subredes: <mark>transporte (arterias)</mark>, <mark>distribución principal</mark> y <mark>secundaria (ramales)</mark>.",
 "Las arterias (más de 150 mm) conectan la aducción con las zonas de presión y en ellas <mark>se evitan acometidas e hidrantes</mark>. Los hidrantes van en la <mark>distribución principal</mark> (150 mm o más).",
 "El diámetro solo no basta: hay que saber a qué red pertenece la tubería. Los ramales (menos de 150 mm) admiten solo acometidas.",
 "Arterias: <mark>nada</mark> · Principal: <mark>acometidas + hidrantes</mark> · Ramales: <mark>solo acometidas</mark>.","Manual de agua fría para consumo humano")

q("Apícola","difícil",
 "Un enjambre lleva 24 horas en un balcón y su apicultor sigue buscándolo. Según el Código Civil, ese enjambre:",
 ["Es res nullius y puede quedárselo el dueño del balcón.","Sigue siendo del apicultor mientras lo persiga.","Pasa a ser del Ayuntamiento."],1,
 "Las <mark>abejas domésticas</mark> se consideran ganado (semovientes) mientras están en la colmena y también cuando el enjambre sale y su dueño lo <mark>persigue</mark>.",
 "Mientras dura la persecución, la propiedad es del apicultor. Solo si <mark>abandona la persecución y pasan 48 horas</mark> se convierte en <mark>res nullius</mark> (animal salvaje).",
 "El plazo de 48 h cuenta desde que el dueño deja de perseguirlo, no desde que el enjambre llega.",
 "Persecución = <mark>sigue siendo suyo</mark> · Abandono + <mark>48 h</mark> = de quien lo recoja o del dueño del lugar (art. 612 del Código Civil).","Manual de rescate apícola")

q("Electricidad","difícil",
 "En una piscina se instala un equipo a 24 V en corriente alterna. ¿Se considera muy baja tensión de seguridad (MBTS)?",
 ["Sí, porque no supera los 50 V en alterna.","Sí, porque no supera los 75 V.","No, porque en piscinas el límite es de 12 V."],2,
 "La <mark>MBTS</mark> es una tensión tan baja que no se considera peligrosa para las personas.",
 "Con carácter general, el REBT (ITC-BT-36) la fija en <mark>50 V en alterna</mark> y <mark>75 V en continua</mark>. Pero hay instrucciones más restrictivas: en <mark>piscinas</mark> (ITC-BT-31) el límite es <mark>12 V</mark>, porque el agua reduce mucho la resistencia del cuerpo.",
 "La A sería correcta fuera de una piscina; la B confunde el límite de continua.",
 "MBTS: <mark>50 V CA · 75 V CC · 12 V en piscinas</mark>.","Conceptos básicos de electricidad")

# ---------------- NORMALES ----------------
q("Trabajos en altura","normal",
 "Según la UNE-EN 355, un absorbedor de energía debe conseguir que la fuerza de choque de una caída sea inferior a:",
 ["6 kN para una masa de 100 kg.","12 kN para una masa de 100 kg.","4 kN para una masa de 80 kg."],0,
 "La <mark>fuerza de choque</mark> es el golpe que recibe el cuerpo cuando el sistema detiene la caída. El absorbedor se rasga o estira para «gastar» parte de esa energía.",
 "La norma fija que el cuerpo no reciba más de <mark>6 kN</mark> (con una masa de <mark>100 kg</mark>), el límite que marca la norma para proteger al usuario.",
 "12 kN es la resistencia mínima de un <mark>anclaje</mark> (UNE-EN 795), no la fuerza de choque.",
 "Absorbedor: <mark>menos de 6 kN</mark> · Anclaje: <mark>12 kN</mark> · Conector: <mark>más de 15 kN</mark>.","Manual de trabajos en altura")

q("Trabajos en altura","normal",
 "Según la UNE-EN 795, el punto de anclaje de un sistema de sujeción debe garantizar una resistencia mínima de:",
 ["6 kN.","12 kN.","22 kN."],1,
 "El <mark>anclaje</mark> es el punto fijo del que cuelga todo el sistema. Si falla, falla todo.",
 "Debe ser suficientemente sólido y garantizar al menos <mark>12 kN</mark>. El anclaje de la cuerda de seguridad es independiente del de la cuerda de trabajo y también es de 12 kN.",
 "22 kN es la resistencia de la cuerda semiestática de <mark>clase A</mark>, no del anclaje.",
 "<mark>Anclaje 12 kN</mark>, y dos anclajes independientes: uno para trabajo y otro para seguridad.","Manual de trabajos en altura")

q("Trabajos en altura","normal",
 "Según la EN 362, la resistencia estática de un conector (mosquetón) en su eje longitudinal debe ser superior a:",
 ["15 kN.","6 kN.","10 kN."],0,
 "El <mark>conector</mark> une los elementos del sistema: arnés, cuerda, anclaje…",
 "La norma exige <mark>más de 15 kN</mark> sin deformarse ni romperse. En la práctica, casi todos los fabricantes superan los <mark>20 kN</mark>. Deben tener cierre de seguridad para evitar aperturas involuntarias.",
 "La resistencia es en el <mark>eje longitudinal</mark>. Cargado de lado o con el gatillo abierto, resiste mucho menos.",
 "Conector: <mark>más de 15 kN</mark> (normalmente más de 20).","Manual de trabajos en altura")

q("Trabajos en altura","normal",
 "Según el manual, ¿por qué no deben usarse bloqueadores tipo puño como dispositivo anticaídas?",
 ["Porque solo funcionan con cuerdas dinámicas.","Porque un puño puede partir la cuerda con una caída de tan solo 4 kN.","Porque no se pueden conectar al arnés."],1,
 "El <mark>puño</mark> es un bloqueador para progresar por la cuerda, no para detener caídas.",
 "Ante un tirón brusco muerde la cuerda y puede <mark>partirla con solo 4 kN</mark>. Como anticaídas solo deben usarse dispositivos certificados para ello.",
 "Pasa lo mismo con otros bloqueadores (ventral, tibloc, gri-gri…): no son anticaídas.",
 "Bloqueador ≠ anticaídas. <mark>4 kN</mark> pueden bastar para romper la cuerda.","Manual de trabajos en altura")

q("Accesos forzados","normal",
 "Según el manual, la norma UNE 1627 de 2011 clasifica las puertas según su resistencia en:",
 ["3 clases.","4 clases.","6 clases."],2,
 "Las puertas se clasifican por el tiempo que resisten un ataque, el tipo de ladrón y la herramienta necesaria.",
 "La norma establece <mark>6 clases</mark>. Pero incluso una de clase 6 se puede abrir: invertir en una puerta mejor es <mark>«comprar tiempo»</mark>.",
 "Por eso en bomberos casi siempre hay un <mark>plan B</mark>: ventanas, balcones, vecinos…",
 "<mark>6 clases</mark>, y todas las puertas se pueden abrir.","Manual de accesos forzados")

q("Accesos forzados","normal",
 "En una cerradura, la cara biselada (achaflanada) del resbalón tiene que estar orientada hacia:",
 ["El cerradero.","El interior de la vivienda.","Las bisagras."],0,
 "El <mark>resbalón</mark> es la pieza que cierra la puerta al tirar de ella sin echar la llave.",
 "La cara <mark>biselada hacia el cerradero</mark> permite que se retraiga al cerrar. La <mark>cara plana</mark> impide que la puerta se abra hasta accionar la manilla.",
 "Como con el resbalón solo es fácil abrir con una mica, existen <mark>resbalones antitarjeta</mark> con varias caras planas.",
 "Bisel → <mark>cerradero</mark>; plana → bloquea.","Manual de accesos forzados")

q("Accesos forzados","normal",
 "Según el manual, una puerta estándar de madera se caracteriza por:",
 ["Cerradura multipunto y bisagras con bulón antipalanca.","Cerradura monopunto y bisagras sin refuerzo antipalanca.","Cerco metálico reforzado y tres cierres."],1,
 "Las puertas van de menos a más resistencia: <mark>estándar</mark>, <mark>blindada</mark> y <mark>acorazada</mark>.",
 "La estándar es un tablero de madera sin refuerzo, con tres bisagras <mark>sin refuerzo antipalanca</mark>, cerradura <mark>monopunto</mark> (resbalón y un cierre) y cerco sin refuerzos, recibido con grapas y espuma.",
 "Los bulones antipalanca en las bisagras y los cierres múltiples son de las blindadas y acorazadas.",
 "Estándar = <mark>monopunto y sin antipalanca</mark>.","Manual de accesos forzados")

q("Agua fría","normal",
 "Las llaves de paso anteriores al contador (de toma, de corte en acera y de corte general) solo deben manipularlas:",
 ["El propietario del edificio.","Los agentes del Canal y la autoridad competente en emergencia, dando cuenta al Canal.","Cualquier vecino en caso de fuga."],1,
 "La red de distribución y las acometidas son <mark>propiedad del Canal de Isabel II</mark>.",
 "Por eso esas llaves son del Canal. En una emergencia, la <mark>autoridad competente</mark> (por ejemplo, bomberos) puede manipularlas, pero <mark>dando cuenta inmediata</mark> de la maniobra y sus razones al Canal.",
 "La acometida contra incendios debe ser siempre <mark>independiente</mark>.",
 "Antes del contador: <mark>Canal</mark> (o bomberos en emergencia, avisando).","Manual de agua fría para consumo humano")

q("Sanitario (SVB)","normal",
 "Para desfibrilar a un niño de 5 años con un DEA, según el manual se deben utilizar:",
 ["Los parches estándar de adulto.","Parches pediátricos con atenuador, o el modo pediátrico si lo hay.","Ningún DEA: está contraindicado en menores de 8 años."],1,
 "El <mark>DEA</mark> analiza el ritmo del corazón y, si es desfibrilable, da una descarga.",
 "Los DEA estándar valen para <mark>mayores de 8 años</mark>. De <mark>1 a 8 años</mark> se usan <mark>parches pediátricos con atenuador</mark> (o el modo pediátrico), que reducen la energía.",
 "No está contraindicado: hay que adaptarlo a la edad.",
 "<mark>Más de 8 años: estándar</mark> · <mark>De 1 a 8: pediátrico</mark>.","Manual de SVB")

q("Sanitario (SVB)","normal",
 "Según el manual, la desfibrilación en los primeros 3-5 minutos tras la parada puede conseguir una supervivencia de hasta:",
 ["El 10-20 %.","El 50-70 %.","El 90-100 %."],1,
 "La <mark>desfibrilación precoz</mark> es uno de los eslabones de la cadena de supervivencia.",
 "En los primeros <mark>3-5 minutos</mark> se alcanzan tasas de supervivencia de hasta el <mark>50-70 %</mark>. Por eso es tan importante el <mark>acceso público</mark> a los DEA.",
 "Cada minuto sin desfibrilar baja mucho la supervivencia: no se debe retrasar por seguir con la RCP si ya hay un DEA.",
 "<mark>3-5 minutos → 50-70 %</mark>.","Manual de SVB")

q("Sanitario (SVB)","normal",
 "Un adulto atragantado tose con fuerza y puede respirar. Según el manual, hay que:",
 ["Darle 5 golpes interescapulares.","Hacerle la maniobra de Heimlich.","Animarle a toser, sin golpes ni darle de beber."],2,
 "La <mark>obstrucción incompleta</mark> deja pasar aire: la persona puede hablar, respirar y toser.",
 "Toser genera presión en la vía aérea y es lo más eficaz para expulsar el objeto. Solo se <mark>anima a toser</mark>: <mark>nada de golpes, ni de comer o beber</mark>.",
 "Golpes y Heimlich son para la <mark>obstrucción completa</mark>: no tose, no habla, signos de asfixia.",
 "Tose → <mark>que siga tosiendo</mark>. No tose → <mark>5 golpes + 5 compresiones</mark>.","Manual de SVB")

q("Sanitario (SVB)","normal",
 "En una obstrucción completa de la vía aérea en un adulto consciente, el manual indica:",
 ["Alternar 5 golpes interescapulares con 5 compresiones abdominales.","Hacer 30 compresiones torácicas y 2 insuflaciones.","Dar 10 golpes interescapulares seguidos."],0,
 "En la <mark>obstrucción completa</mark> el aire no pasa: hay que sacar el objeto con fuerza externa.",
 "Primero <mark>5 golpes interescapulares</mark> con la víctima inclinada hacia delante y después <mark>5 compresiones abdominales</mark> (Heimlich), alternando hasta que expulse el objeto o quede inconsciente.",
 "La RCP (30:2) es si pierde la conciencia, no mientras está consciente.",
 "<mark>5 + 5</mark> en bucle. Heimlich: puño en la boca del estómago, hacia dentro y hacia arriba.","Manual de SVB")

q("Atención sanitaria","normal",
 "Según el manual de atención inicial, el relleno capilar es normal cuando el lecho ungueal recupera su color en:",
 ["Menos de 3 segundos.","Menos de 6 segundos.","Entre 5 y 10 segundos."],0,
 "El <mark>relleno capilar</mark> se mide apretando la uña y soltando: indica si la sangre llega bien a la periferia.",
 "Si recupera el tono rosado en <mark>menos de 3 segundos</mark> es normal. Si tarda más, indica <mark>alteración hemodinámica</mark>, como un shock.",
 "Con frío se alarga aunque el paciente esté bien: es una referencia, no una prueba definitiva.",
 "Relleno capilar <mark>menor de 3 s</mark> · pulso normal <mark>60-100 lpm</mark>.","Manual de atención inicial al paciente")

q("Atención sanitaria","normal",
 "Según el manual de atención inicial, el torniquete se emplea:",
 ["Siempre que haya una herida sangrante en una extremidad.","En amputaciones y cuando no se puede controlar la hemorragia por compresión.","Solo en heridas de la cabeza."],1,
 "El <mark>torniquete</mark> corta toda la circulación de una extremidad: para la hemorragia, pero puede causar daños.",
 "Lo primero es la <mark>compresión directa</mark>. El torniquete se reserva para <mark>amputaciones</mark> y <mark>hemorragias incontrolables</mark>, o con muchos heridos y poca gente para atenderlos.",
 "No se usa para cualquier sangrado, y nunca en la cabeza.",
 "Primero <mark>compresión</mark>; torniquete solo si no basta.","Manual de atención inicial al paciente")

q("Atención sanitaria","normal",
 "En la escala AVDN de valoración neurológica, la letra D significa:",
 ["Desorientado.","Respuesta al dolor.","Disminución de pupilas."],1,
 "La <mark>AVDN</mark> es una forma rápida de valorar el nivel de conciencia, más sencilla que la de Glasgow.",
 "<mark>A</mark>: alerta · <mark>V</mark>: responde a estímulo verbal · <mark>D</mark>: responde al dolor · <mark>N</mark>: no responde.",
 "No confundir «D» con desorientado: un paciente desorientado está en A o V.",
 "<mark>Alerta, Verbal, Dolor, No responde</mark>.","Manual de atención inicial al paciente")

q("Patología cardiovascular","normal",
 "Dolor torácico opresivo de 25 minutos que no mejora con reposo ni con nitroglicerina. Según el manual, orienta a:",
 ["Angina de pecho (ángor).","Infarto agudo de miocardio.","Crisis de ansiedad."],1,
 "<mark>Ángor</mark> e <mark>infarto (IAM)</mark> son síndromes coronarios agudos. En el ángor la arteria se estrecha; en el infarto se obstruye del todo.",
 "<mark>Ángor</mark>: dolor intermitente, con el esfuerzo, de <mark>menos de 10-15 min</mark>, que mejora con reposo y nitroglicerina. <mark>IAM</mark>: dolor continuo, de <mark>más de 15 min</mark>, que <mark>no mejora</mark> con reposo ni con medicación.",
 "Los síntomas son parecidos: lo que los distingue es la <mark>duración</mark> y la <mark>respuesta</mark> al reposo y a la nitroglicerina.",
 "<mark>Más de 15 min y no cede = IAM</mark>.","Manual de patología cardiovascular")

q("Patología cardiovascular","normal",
 "¿Qué diferencia una emergencia hipertensiva de una urgencia hipertensiva?",
 ["En la emergencia hay lesión de órganos diana y riesgo vital.","En la emergencia la tensión es más baja.","La urgencia siempre requiere reanimación."],0,
 "Una <mark>crisis hipertensiva</mark> es una subida brusca de la tensión que puede dañar los <mark>órganos diana</mark>: cerebro, corazón y riñones.",
 "<mark>Urgencia</mark>: más leve, sin lesión de órganos ni síntomas. <mark>Emergencia</mark>: grave, con <mark>lesión de órganos diana</mark> (cefalea intensa, baja conciencia, signos coronarios…) y <mark>riesgo vital</mark>.",
 "Lo que las distingue es si hay lesión de órganos, no la cifra de tensión.",
 "<mark>Emergencia = órganos dañados</mark>.","Manual de patología cardiovascular")

q("Patología cardiovascular","normal",
 "Según el manual, una crisis convulsiva se considera emergencia neurológica grave cuando dura más de:",
 ["1 minuto.","5 minutos.","15 minutos."],1,
 "Las <mark>convulsiones</mark> son descargas eléctricas anormales del cerebro que producen movimientos involuntarios.",
 "Si una crisis dura <mark>más de 5 minutos</mark>, o hay <mark>crisis repetidas</mark>, es una emergencia neurológica grave.",
 "Durante la crisis no se mete nada en la boca: se protege la cabeza y se apartan objetos.",
 "Convulsión: <mark>más de 5 min o repetida = emergencia</mark>.","Manual de patología cardiovascular y otras urgencias")

q("Protección civil","normal",
 "Según el art. 2 de la Ley 17/2015, la posibilidad de que una amenaza llegue a afectar a personas o bienes es:",
 ["El peligro.","La vulnerabilidad.","El riesgo."],2,
 "La Ley define una cadena de conceptos que conviene no mezclar.",
 "<mark>Peligro</mark>: potencial de causar daño. <mark>Vulnerabilidad</mark>: lo susceptible que es una colectividad. <mark>Amenaza</mark>: estar expuesto a un peligro. <mark>Riesgo</mark>: <mark>posibilidad</mark> de que la amenaza llegue a afectar.",
 "Si la definición habla de «posibilidad», es el riesgo.",
 "<mark>Peligro → amenaza → riesgo → emergencia → catástrofe</mark>.","Ley 17/2015, art. 2")

q("Protección civil","normal",
 "La Estrategia del Sistema Nacional de Protección Civil se revisará, al menos, cada:",
 ["Dos años.","Cuatro años.","Cinco años."],1,
 "La <mark>Estrategia</mark> analiza los riesgos futuros y fija líneas de acción para responder a las emergencias.",
 "Se revisa <mark>al menos cada cuatro años</mark>. Sus líneas básicas las aprueba el <mark>Consejo Nacional de Protección Civil</mark>, y la Estrategia Nacional, el <mark>Consejo de Seguridad Nacional</mark> a propuesta del Ministro del Interior.",
 "No confundir los dos consejos: el Nacional de Protección Civil y el de Seguridad Nacional.",
 "Estrategia: <mark>cada 4 años</mark>.","Ley 17/2015, art. 4")

q("PRL","normal",
 "Según el art. 38 de la Ley 31/1995, el Comité de Seguridad y Salud se constituye en empresas o centros con:",
 ["50 o más trabajadores, y se reúne trimestralmente.","30 o más trabajadores, y se reúne mensualmente.","100 o más trabajadores, y se reúne anualmente."],0,
 "El <mark>Comité de Seguridad y Salud</mark> es un órgano <mark>paritario</mark> y colegiado: Delegados de Prevención por un lado, y empresario o representantes en igual número por el otro.",
 "Se crea con <mark>50 o más trabajadores</mark> y se reúne <mark>trimestralmente</mark>, y siempre que lo pida alguna de las partes.",
 "Los delegados sindicales y los técnicos de prevención participan <mark>con voz pero sin voto</mark>.",
 "Comité: <mark>50 trabajadores, cada 3 meses, paritario</mark>.","Ley 31/1995, art. 38")

q("PRL","normal",
 "Según el art. 19 de la Ley 31/1995, la formación en prevención de los trabajadores:",
 ["La paga el trabajador y se hace fuera de la jornada.","Se imparte, si es posible, dentro de la jornada, y su coste nunca recae en el trabajador.","Solo es obligatoria al incorporarse a la empresa."],1,
 "El empresario debe dar formación <mark>teórica y práctica</mark>, suficiente y adecuada, centrada en el puesto.",
 "Se da al contratar, al cambiar de funciones y al introducir nuevas tecnologías o equipos. Se imparte <mark>dentro de la jornada</mark> o, si no, descontando ese tiempo, y su coste <mark>no recae nunca en el trabajador</mark>.",
 "No es solo al entrar: se repite cuando cambian los riesgos.",
 "Formación: <mark>en jornada y gratis</mark>.","Ley 31/1995, art. 19")

q("EBEP","normal",
 "Según el art. 56 del TREBEP, para participar en un proceso selectivo hay que tener cumplidos:",
 ["16 años.","18 años.","21 años."],0,
 "El art. 56 recoge los requisitos generales para acceder al empleo público.",
 "Hace falta tener <mark>16 años</mark> y no superar la edad de jubilación forzosa. <mark>Solo por ley</mark> se puede fijar otra edad máxima.",
 "Mucha gente piensa en 18 por la mayoría de edad, pero el EBEP dice 16.",
 "Requisitos: nacionalidad, capacidad funcional, <mark>16 años</mark>, no estar separado ni inhabilitado y titulación.","TREBEP, art. 56")

q("EBEP","normal",
 "Según el art. 76 del TREBEP, para el subgrupo C1 se exige el título de:",
 ["Graduado en ESO.","Bachiller o Técnico.","Técnico Superior."],1,
 "Los cuerpos se clasifican en grupos según la <mark>titulación</mark> exigida para entrar.",
 "<mark>A1 y A2</mark>: grado universitario · <mark>B</mark>: Técnico Superior · <mark>C1</mark>: <mark>Bachiller o Técnico</mark> · <mark>C2</mark>: ESO.",
 "Técnico Superior es del grupo B, no del C1.",
 "<mark>Grado / Técnico Superior / Bachiller-Técnico / ESO</mark> = A / B / C1 / C2.","TREBEP, art. 76")

q("EBEP","normal",
 "Según el art. 50 del TREBEP, las vacaciones anuales retribuidas de los funcionarios son de:",
 ["22 días hábiles, sin contar los sábados como hábiles.","30 días naturales.","25 días hábiles."],0,
 "Se disfrutan <mark>en cada año natural</mark> o, si se trabajó menos tiempo, de forma proporcional.",
 "Son <mark>22 días hábiles</mark>, y a estos efectos <mark>los sábados no son hábiles</mark> (salvo horarios especiales).",
 "30 días naturales es el mínimo del Estatuto de los Trabajadores, no la regla del EBEP.",
 "Vacaciones: <mark>22 días hábiles</mark>.","TREBEP, art. 50")

q("Constitución","normal",
 "Según el art. 17.2 CE, la detención preventiva no puede durar más del tiempo necesario y, en todo caso, el plazo máximo es de:",
 ["24 horas.","48 horas.","72 horas."],2,
 "La <mark>detención preventiva</mark> sirve para hacer las averiguaciones necesarias para aclarar los hechos.",
 "Dura lo estrictamente necesario y, como máximo, <mark>72 horas</mark>. Después, el detenido queda en libertad o a disposición judicial.",
 "El «habeas corpus» (art. 17.4) es el procedimiento para poner de inmediato ante el juez a quien está detenido ilegalmente.",
 "Detención: <mark>máximo 72 h</mark>, con derecho a abogado y a no declarar.","CE, art. 17")

q("Constitución","normal",
 "Según el art. 140 CE, los alcaldes serán elegidos:",
 ["Por los concejales o por los vecinos.","Solo por los vecinos.","Por el Pleno a propuesta del Gobierno autonómico."],0,
 "El art. 140 garantiza la <mark>autonomía de los municipios</mark>, que tienen personalidad jurídica plena.",
 "Los <mark>concejales</mark> se eligen por sufragio universal de los vecinos. Los <mark>alcaldes</mark>, <mark>por los concejales o por los vecinos</mark>.",
 "La ley regula también el <mark>concejo abierto</mark>, en el que gobierna la asamblea de vecinos.",
 "Concejales: <mark>los vecinos</mark> · Alcalde: <mark>los concejales o los vecinos</mark>.","CE, art. 140")

q("Estatuto CAM","normal",
 "Según el Estatuto de Autonomía de Madrid, para ser Vicepresidente o Consejero del Gobierno de la Comunidad:",
 ["Hay que ser Diputado de la Asamblea.","No es necesaria la condición de Diputado.","Hay que haber sido alcalde."],1,
 "Las instituciones de autogobierno son la <mark>Asamblea</mark>, el <mark>Gobierno</mark> y el <mark>Presidente</mark>.",
 "El Gobierno lo forman el Presidente, los Vicepresidentes y los Consejeros, que el Presidente <mark>nombra y cesa</mark>. Para ser Vicepresidente o Consejero <mark>no hace falta ser Diputado</mark>.",
 "La potestad legislativa es de la Asamblea; la reglamentaria y ejecutiva, del Gobierno.",
 "<mark>Asamblea legisla, Gobierno ejecuta</mark>; los Consejeros no tienen por qué ser Diputados.","Estatuto de Autonomía de la CAM, arts. 8, 22 y 34")

q("Procedimiento administrativo","normal",
 "Según el art. 103 de la Ley 39/2015, la multa coercitiva:",
 ["Es una sanción y sustituye a las demás.","Es independiente de las sanciones y compatible con ellas.","Solo se puede imponer una vez."],1,
 "La <mark>multa coercitiva</mark> no castiga: es un <mark>medio de ejecución forzosa</mark> para obligar a cumplir lo ordenado.",
 "Se puede <mark>reiterar</mark> cada cierto tiempo hasta que se cumpla. Por eso es <mark>independiente</mark> de las sanciones y <mark>compatible</mark> con ellas.",
 "Solo cabe cuando una ley lo autoriza: actos personalísimos, actos en los que la compulsión no conviene o actos que puede hacer otra persona.",
 "Medios de ejecución forzosa: <mark>apremio, ejecución subsidiaria, multa coercitiva, compulsión</mark>.","Ley 39/2015, arts. 100 y 103")

q("Igualdad","normal",
 "Según la LO 3/2007, la situación en que una norma aparentemente neutra pone a personas de un sexo en desventaja particular es:",
 ["Discriminación directa.","Discriminación indirecta.","Acoso por razón de sexo."],1,
 "La ley distingue dos formas de discriminación.",
 "<mark>Directa</mark>: tratar peor a alguien por su sexo. <mark>Indirecta</mark>: una regla <mark>aparentemente neutra</mark> que perjudica más a un sexo, salvo que esté justificada objetivamente con medios necesarios y adecuados.",
 "Toda <mark>orden de discriminar</mark> también se considera discriminación.",
 "«Aparentemente neutro» = <mark>indirecta</mark>.","LO 3/2007, art. 6")

q("Igualdad","normal",
 "El III Plan de Igualdad del Ayuntamiento de Madrid estructura sus actuaciones en tres líneas de intervención:",
 ["La institución, la comunicación y las personas.","El empleo, la salud y la conciliación.","La formación, la violencia de género y el lenguaje."],0,
 "El plan persigue avanzar en la igualdad entre mujeres y hombres en el Ayuntamiento y sus organismos autónomos.",
 "Se organiza en <mark>tres líneas</mark>: <mark>1. La institución</mark>, <mark>2. La comunicación</mark> y <mark>3. Las personas</mark>, con objetivos, medidas e indicadores.",
 "Antecedentes: I Plan (2017-2019) y II Plan (2022-2024).",
 "<mark>Institución · Comunicación · Personas</mark>.","III Plan de Igualdad del Ayuntamiento de Madrid")

q("Corte y soldadura","normal",
 "Al encender el soplete de oxicorte con Chemtane, el orden correcto es:",
 ["Abrir primero el oxígeno, encender y abrir después el Chemtane.","Abrir el Chemtane (rojo) unos 3/4 de vuelta, encender y abrir después lentamente el oxígeno (azul).","Abrir las dos válvulas a la vez y encender."],1,
 "El soplete tiene dos válvulas: <mark>combustible (Chemtane, rojo)</mark> y <mark>oxígeno (azul)</mark>.",
 "Primero se abre el <mark>Chemtane</mark> unos <mark>3/4 de vuelta</mark>, se enciende con el chisquero y después se abre <mark>lentamente el oxígeno</mark> hasta formar la llama de calentamiento.",
 "Hay que tener cuidado de no cerrar el Chemtane al abrir el oxígeno: con guantes se pierde precisión.",
 "<mark>Rojo, chispa, azul</mark>. Presiones: oxígeno 2-5 bar · Chemtane 0,5 bar.","Manual de corte térmico")

q("Corte y soldadura","normal",
 "Según el manual, durante el oxicorte se abre el chorro de oxígeno de corte cuando la pieza alcanza:",
 ["Un color blanco brillante.","Un color rojo cereza, inclinando el soplete unos 45°.","Un color negro mate."],1,
 "El oxicorte no funde el metal con la llama: lo <mark>calienta</mark> y luego lo <mark>quema</mark> con un chorro de oxígeno puro.",
 "Se calienta hasta <mark>rojo cereza</mark> (cerca de la fusión) y se abre el oxígeno con el soplete a <mark>45°</mark> en la dirección del corte, a unos <mark>2-5 mm</mark> de la pieza.",
 "Con más espesor, el dardo se coloca más perpendicular. El espesor máximo suele estar entre 0,3 y 6 cm.",
 "<mark>Rojo cereza → oxígeno → 45°</mark>.","Manual de corte térmico")

q("Electricidad","normal",
 "Según el manual, la tetanización producida por el paso de la corriente es:",
 ["La contracción involuntaria de los músculos, que impide soltarse del punto de contacto.","Una infección de las quemaduras eléctricas.","La parada de la respiración por falta de oxígeno."],0,
 "Al pasar corriente por el cuerpo, los músculos reciben la señal eléctrica como si fuera una orden de contraerse.",
 "La <mark>tetanización</mark> es la <mark>contracción involuntaria</mark> o intermitente que deja sin capacidad de reacción e <mark>impide separarse</mark> del contacto. Si afecta al tórax, puede causar asfixia.",
 "No tiene que ver con el tétanos infeccioso, aunque se llame igual.",
 "Efectos de la corriente: <mark>fibrilación, paro, asfixia, tetanización y quemaduras</mark>.","Conceptos básicos de electricidad")

q("CTE DB-SI","normal",
 "Según el DB-SI 1, con carácter general la superficie construida de un sector de incendio no debe exceder de:",
 ["1.000 m².","2.500 m².","5.000 m²."],1,
 "Un <mark>sector de incendio</mark> es una zona cerrada con elementos resistentes al fuego para que el incendio no pase al resto del edificio durante un tiempo.",
 "La regla general es <mark>2.500 m²</mark>. Limitar el tamaño limita lo que puede arder de una vez.",
 "Hay excepciones: con instalación automática de extinción, algunos usos pueden ampliarlo.",
 "Sector: <mark>2.500 m²</mark> en general.","CTE DB-SI 1")

q("Ascensores","normal",
 "En el rescate en un ascensor hidráulico, tras cortar la corriente y asegurar las puertas, para bajar la cabina hasta planta se acciona:",
 ["El volante de giro manual.","El botón o tirador rojo de descenso.","El freno del motor."],1,
 "En los ascensores hidráulicos la cabina sube empujada por aceite a presión; para bajarla basta con dejar salir ese aceite.",
 "Se acciona el <mark>botón o tirador rojo</mark> de descenso hasta dejar la cabina en posición de rescate. Los fabricantes incorporan avisos visuales o acústicos para saber cuándo está en planta. Si hay que subirla, se usa la <mark>palanca de accionamiento hidráulico</mark>.",
 "El volante y el freno son de los ascensores eléctricos de tracción.",
 "Hidráulico: <mark>botón rojo para bajar, palanca para subir</mark>.","Manual de rescate en ascensores")

q("Vehículos","normal",
 "Según la información de vehículos del SEI, la autoescala articulada de 32 m (Riffaud) tiene:",
 ["Un paquete de 5 tramos, con el último articulado y telescópico.","Un paquete de 4 tramos, todos fijos.","Un brazo articulado sin tramos telescópicos."],0,
 "El Servicio tiene autoescalas convencionales y articuladas.",
 "La <mark>articulada de 32 m</mark> (Riffaud, 4x2) lleva un paquete de <mark>5 tramos</mark>, con el <mark>último articulado y telescópico</mark> para salvar obstáculos. La convencional es de <mark>27 m</mark> (Metz).",
 "No mezclar: 27 m es la Metz y 32 m la articulada Riffaud.",
 "<mark>Metz 27 m</mark> · <mark>Riffaud articulada 32 m, 5 tramos</mark>.","Información de vehículos del SEI")

json.dump(Q,open(P,'w',encoding='utf-8'),ensure_ascii=False)
# reescribir con una pregunta por línea
open(P,'w',encoding='utf-8').write('[\n'+',\n'.join(json.dumps(x,ensure_ascii=False) for x in Q)+'\n]\n')
print(len(Q), sum(1 for x in Q if x['d']=='difícil'))
