import json, subprocess, sys
P='/home/claude/test-bombero/preguntas.json'
Q=json.load(open(P,encoding='utf-8'))
nid=max(q['id'] for q in Q)+1
desde=nid
def q(t,d,enun,ops,c,o4,que,porque,ojo,rec,f):
    global nid
    assert len(ops)==3 and o4 not in ops
    Q.append(dict(id=nid,t=t,d=d,q=enun,o=ops,c=c,que=que,porque=porque,ojo=ojo,rec=rec,f=f,o4=o4)); nid+=1

# ======================= DIFÍCILES =======================
q("CTE DB-SI","difícil",
 "Un edificio de viviendas tiene una altura de evacuación de 30 m. Según el DB-SI 4, ¿cuál de estas instalaciones debe tener obligatoriamente?",
 ["Columna seca.","Sistema de detección y alarma de incendio.","Instalación automática de extinción."],0,
 "Detección y alarma, pero no columna seca.",
 "El DB-SI 4 fija qué <mark>instalaciones de protección contra incendios</mark> necesita cada edificio según su uso y su altura.",
 "En uso Residencial Vivienda: <mark>columna seca</mark> si la altura de evacuación supera los <mark>24 m</mark>; <mark>detección y alarma</mark> si supera los <mark>50 m</mark>; y, en general, <mark>extinción automática</mark> si supera los <mark>80 m</mark>. Con 30 m solo se cumple el primer umbral.",
 "Con 30 m también hace falta ascensor de emergencia (más de 28 m), aunque no estaba entre las opciones.",
 "Vivienda: <mark>24 m columna seca</mark> · <mark>50 m detección</mark> · <mark>80 m extinción automática</mark>.","CTE DB-SI 4, tabla 1.1")

q("Procedimiento administrativo","difícil",
 "En un procedimiento iniciado a su solicitud, el interesado no realiza un trámite que no es indispensable para dictar la resolución. Según el art. 95 de la Ley 39/2015, ¿qué ocurre?",
 ["Pierde su derecho a ese trámite, pero el procedimiento sigue.","Se le advierte y, a los tres meses, se produce la caducidad.","Se archiva el procedimiento de inmediato."],0,
 "Se entiende que ha desistido de su solicitud.",
 "La <mark>caducidad</mark> es la terminación del procedimiento cuando se paraliza por culpa del interesado.",
 "Solo se aplica si el trámite pendiente es <mark>indispensable</mark>: entonces se le advierte y, pasados <mark>tres meses</mark>, se archiva. Si el trámite <mark>no es indispensable</mark>, su inactividad solo supone la <mark>pérdida de su derecho a ese trámite</mark>.",
 "La caducidad no produce por sí sola la prescripción de las acciones, pero los procedimientos caducados no la interrumpen.",
 "Trámite indispensable → <mark>caducidad a los 3 meses</mark> · No indispensable → <mark>pierde el trámite</mark>.","Ley 39/2015, art. 95")

q("Corte y soldadura","difícil",
 "Según el manual, la lanza térmica atraviesa unos 25 mm de acero en 5 segundos. A ese ritmo, ¿cuánto tardaría en atravesar 50 mm de acero?",
 ["Unos 10 segundos.","Unos 5 segundos.","Unos 2,5 minutos."],0,
 "Alrededor de 1 minuto.",
 "La <mark>lanza térmica</mark> es una herramienta de corte que alcanza en la punta entre <mark>4.000 y 5.000 °C</mark> y funciona incluso sumergida.",
 "Como referencia, atraviesa unos <mark>25 mm de acero en 5 s</mark>. El doble de espesor (50 mm) necesita, más o menos, el <mark>doble de tiempo</mark>: unos 10 s.",
 "Los 2,5 minutos son la referencia para atravesar unos 250 mm de hormigón, no el acero.",
 "Lanza térmica: <mark>25 mm de acero en 5 s</mark> · <mark>250 mm de hormigón en 2,5 min</mark>.","Manual de corte térmico y soldadura")

q("Trabajos en altura","difícil",
 "Una cuerda para trabajos verticales debe garantizar una resistencia de 22 kN. Según el manual, ¿de qué clase es y qué alargamiento aproximado tiene?",
 ["Semiestática de clase A, con un alargamiento de un 5 %.","Semiestática de clase B, con un alargamiento de un 5 %.","Dinámica, con un alargamiento cercano al 8 %."],0,
 "Semiestática de clase B, con un alargamiento cercano al 8 %.",
 "La UNE-EN 1891 regula las <mark>cuerdas semiestáticas</mark>, las más usadas en trabajos verticales porque estiran poco.",
 "Tienen un alargamiento de un <mark>5 %</mark> y hay dos clases: la <mark>A</mark>, que garantiza <mark>22 kN</mark>, y la <mark>B</mark>, que garantiza <mark>18 kN</mark>. Las <mark>dinámicas</mark> (EN 892) estiran mucho más y se usan sobre todo en escalada.",
 "Para trabajos verticales se usan las de clase A, de 10,5 u 11 mm de diámetro.",
 "Semiestática: <mark>5 %</mark> · Clase A <mark>22 kN</mark> · Clase B <mark>18 kN</mark>.","Manual de trabajos en altura, EN 1891")

q("EBEP","difícil",
 "Fallece el abuelo de una funcionaria y el fallecimiento se produce en otra localidad. Según el art. 48 del TREBEP, ¿cuántos días de permiso le corresponden?",
 ["Cuatro días hábiles.","Dos días hábiles.","Cinco días hábiles."],0,
 "Tres días naturales.",
 "El permiso por fallecimiento depende del <mark>grado de parentesco</mark> y de si el suceso ocurre en la <mark>misma localidad</mark>.",
 "El abuelo es familiar de <mark>segundo grado</mark>: corresponden <mark>dos días hábiles</mark> en la misma localidad y <mark>cuatro</mark> en distinta localidad. Para el primer grado son tres y cinco días hábiles.",
 "Los días son hábiles, no naturales.",
 "Fallecimiento: 1.er grado <mark>3/5</mark> · 2.º grado <mark>2/4</mark> días hábiles (misma/distinta localidad).","TREBEP, art. 48.a")

q("Régimen local","difícil",
 "Un ayuntamiento quiere concertar una operación de crédito prevista en el presupuesto cuyo importe acumulado en el ejercicio llega al 12 % de sus recursos ordinarios. Según la Ley 7/1985, ¿quién es competente?",
 ["El Pleno, porque supera el 10 % de los recursos ordinarios.","El Alcalde, porque la operación está prevista en el presupuesto.","La Junta de Gobierno Local."],0,
 "El Alcalde, porque no supera el 15 %.",
 "El art. 21 reparte las atribuciones económicas entre el <mark>Alcalde</mark> y el <mark>Pleno</mark>.",
 "El Alcalde puede concertar operaciones de crédito previstas en el presupuesto siempre que su importe acumulado en el ejercicio <mark>no supere el 10 %</mark> de los recursos ordinarios. Por encima, la competencia es del <mark>Pleno</mark>.",
 "El 15 % es el límite para las operaciones de tesorería, que es otro supuesto distinto.",
 "Crédito: Alcalde <mark>hasta el 10 %</mark> · Tesorería <mark>hasta el 15 %</mark>.","Ley 7/1985, art. 21.1.f")

# ======================= NORMALES =======================
q("Constitución","normal","Según el art. 1.3 CE, la forma política del Estado español es:",
 ["La Monarquía parlamentaria.","La República parlamentaria.","El Estado federal."],0,"La Monarquía presidencialista.",
 "El art. 1 recoge los principios básicos del Estado.",
 "España es un <mark>Estado social y democrático de Derecho</mark>, la soberanía reside en el <mark>pueblo español</mark> y la forma política es la <mark>Monarquía parlamentaria</mark>.",
 "El Rey no gobierna: el poder ejecutivo corresponde al Gobierno, que responde ante las Cortes.",
 "Art. 1.3: <mark>Monarquía parlamentaria</mark>.","CE, art. 1.3")

q("Constitución","normal","Según el art. 1.1 CE, los valores superiores del ordenamiento jurídico son:",
 ["La libertad, la justicia, la igualdad y el pluralismo político.","La libertad, la seguridad, la igualdad y la solidaridad.","La dignidad, la justicia, la igualdad y la unidad."],0,
 "La libertad, la justicia, la legalidad y el pluralismo político.",
 "Los <mark>valores superiores</mark> orientan todo el ordenamiento jurídico.",
 "Son cuatro: <mark>libertad</mark>, <mark>justicia</mark>, <mark>igualdad</mark> y <mark>pluralismo político</mark>.",
 "La seguridad jurídica y la legalidad son principios del art. 9.3, no valores superiores.",
 "Valores superiores: <mark>libertad, justicia, igualdad y pluralismo político</mark>.","CE, art. 1.1")

q("Constitución","normal","Según el art. 9.3 CE, la Constitución garantiza la irretroactividad de:",
 ["Las disposiciones sancionadoras no favorables o restrictivas de derechos individuales.","Todas las leyes, sin excepción.","Las normas tributarias."],0,
 "Las disposiciones favorables al ciudadano.",
 "La <mark>irretroactividad</mark> significa que una norma no se aplica a hechos anteriores a su entrada en vigor.",
 "La CE la garantiza para las disposiciones <mark>sancionadoras no favorables</mark> o <mark>restrictivas de derechos individuales</mark>: nadie puede ser castigado por una norma posterior a sus actos.",
 "Las normas favorables sí pueden aplicarse con efecto retroactivo.",
 "Irretroactivas: <mark>sanciones desfavorables y restricciones de derechos</mark>.","CE, art. 9.3")

q("Constitución","normal","Según el art. 20.5 CE, el secuestro de publicaciones, grabaciones y otros medios de información solo puede acordarse:",
 ["En virtud de resolución judicial.","Por orden del Ministerio del Interior.","Por acuerdo del Consejo de Ministros."],0,
 "Por decisión del director del medio.",
 "El art. 20 protege la libertad de expresión y de información.",
 "Estas libertades no pueden restringirse con <mark>censura previa</mark>, y el <mark>secuestro</mark> de publicaciones solo cabe por <mark>resolución judicial</mark>.",
 "Su límite está en el derecho al honor, a la intimidad, a la propia imagen y en la protección de la juventud y la infancia.",
 "Secuestro de publicaciones: <mark>solo un juez</mark>.","CE, art. 20")

q("Constitución","normal","Según el art. 137 CE, el Estado se organiza territorialmente en:",
 ["Municipios, provincias y Comunidades Autónomas.","Municipios, comarcas y Comunidades Autónomas.","Provincias, regiones y nacionalidades."],0,
 "Distritos, municipios y provincias.",
 "El Título VIII de la CE regula la <mark>organización territorial</mark> del Estado.",
 "El Estado se organiza en <mark>municipios</mark>, <mark>provincias</mark> y <mark>Comunidades Autónomas</mark>, y todas gozan de <mark>autonomía</mark> para gestionar sus intereses.",
 "Las comarcas pueden existir como agrupaciones de municipios, pero no están en esta lista.",
 "Art. 137: <mark>municipios, provincias y CCAA</mark>.","CE, art. 137")

q("Constitución","normal","Según el art. 33.3 CE, nadie puede ser privado de sus bienes y derechos sino:",
 ["Por causa justificada de utilidad pública o interés social, con la correspondiente indemnización.","Por decisión del Pleno municipal, sin indemnización.","Cuando lo pida un vecino afectado."],0,
 "Por una sanción administrativa leve.",
 "El art. 33 reconoce el derecho a la <mark>propiedad privada</mark> y a la herencia.",
 "Solo se puede expropiar por <mark>utilidad pública o interés social</mark>, con la <mark>indemnización</mark> correspondiente y según las leyes.",
 "La función social de la propiedad delimita su contenido.",
 "Expropiar: <mark>causa justificada + indemnización</mark>.","CE, art. 33")

q("Constitución","normal","Según el art. 143.3 CE, si la iniciativa para constituir una Comunidad Autónoma no prospera, solo puede reiterarse pasados:",
 ["Cinco años.","Dos años.","Seis meses."],0,"Diez años.",
 "El art. 143 regula cómo se accede a la autonomía.",
 "La iniciativa corresponde a las Diputaciones y a dos tercios de los municipios; si <mark>no prospera</mark>, solo puede repetirse pasados <mark>cinco años</mark>.",
 "Los seis meses son el plazo para cumplir los requisitos de la iniciativa desde el primer acuerdo.",
 "Iniciativa fallida: <mark>5 años</mark> de espera.","CE, art. 143")

q("Estatuto CAM","normal","Según el art. 8 del Estatuto de Autonomía de Madrid, los poderes de la Comunidad se ejercen a través de:",
 ["La Asamblea, el Gobierno y el Presidente.","La Asamblea, el Senado y el Presidente.","El Gobierno, el Tribunal Superior de Justicia y el Alcalde de Madrid."],0,
 "El Consejo de Gobierno y la Delegación del Gobierno.",
 "Las <mark>instituciones de autogobierno</mark> son los órganos propios de la Comunidad.",
 "Son tres: la <mark>Asamblea</mark>, el <mark>Gobierno</mark> y el <mark>Presidente</mark> de la Comunidad.",
 "La Delegación del Gobierno es un órgano del Estado, no de la Comunidad.",
 "CAM: <mark>Asamblea, Gobierno y Presidente</mark>.","Estatuto de Autonomía de Madrid, art. 8")

q("Estatuto CAM","normal","Según el art. 9 del Estatuto de Autonomía de Madrid, ¿quién aprueba y controla el Presupuesto de la Comunidad?",
 ["La Asamblea de Madrid.","El Gobierno de la Comunidad.","El Presidente de la Comunidad."],0,"La Delegación del Gobierno en Madrid.",
 "La <mark>Asamblea</mark> representa al pueblo de Madrid.",
 "Ejerce la <mark>potestad legislativa</mark>, <mark>aprueba y controla el Presupuesto</mark> e impulsa y controla la acción del Gobierno.",
 "La potestad reglamentaria y la función ejecutiva corresponden al Gobierno.",
 "Asamblea: <mark>leyes y Presupuesto</mark>.","Estatuto de Autonomía de Madrid, art. 9")

q("Régimen local","normal","Según el art. 21 de la Ley 7/1985, dictar bandos es una atribución:",
 ["Del Alcalde.","Del Pleno.","De la Junta de Gobierno Local."],0,"Del Secretario del Ayuntamiento.",
 "Un <mark>bando</mark> es un aviso o mandato del Alcalde dirigido a los vecinos.",
 "Entre las atribuciones del <mark>Alcalde</mark> está <mark>dictar bandos</mark>, además de dirigir el gobierno municipal y representar al ayuntamiento.",
 "Las ordenanzas, en cambio, las aprueba el Pleno.",
 "Bandos: <mark>Alcalde</mark> · Ordenanzas: <mark>Pleno</mark>.","Ley 7/1985, art. 21.1.e")

q("Régimen local","normal","Según el art. 21 de la Ley 7/1985, ¿quién decide los empates con voto de calidad en las sesiones que preside?",
 ["El Alcalde.","El concejal de más edad.","El Secretario de la corporación."],0,"El Teniente de Alcalde.",
 "El <mark>voto de calidad</mark> es el voto que sirve para desempatar.",
 "El <mark>Alcalde</mark> convoca y preside las sesiones del Pleno y de la Junta de Gobierno Local y <mark>decide los empates con voto de calidad</mark>.",
 "El Secretario da fe de los acuerdos, pero no vota.",
 "Empate: <mark>decide el Alcalde</mark>.","Ley 7/1985, art. 21.1.c")

q("Régimen local","normal","Según el art. 21 de la Ley 7/1985, la jefatura de la Policía Municipal corresponde:",
 ["Al Alcalde.","Al Pleno.","Al Delegado del Gobierno."],0,"Al Jefe de Bomberos.",
 "El Alcalde tiene la <mark>jefatura superior de todo el personal</mark> municipal.",
 "Además, ejerce expresamente la <mark>jefatura de la Policía Municipal</mark>.",
 "Puede delegar algunas atribuciones, pero la jefatura le corresponde a él.",
 "Policía Municipal: <mark>jefe, el Alcalde</mark>.","Ley 7/1985, art. 21.1.i")

q("Régimen local","normal","Según el art. 25 de la Ley 7/1985, la prevención y extinción de incendios es, para el municipio:",
 ["Una competencia propia.","Una competencia exclusiva del Estado.","Una competencia delegada por la Comunidad Autónoma."],0,
 "Una competencia de las Diputaciones en todo caso.",
 "Las <mark>competencias propias</mark> son las que el municipio ejerce en su propio nombre.",
 "El art. 25 incluye entre ellas la <mark>policía local</mark>, la <mark>protección civil</mark> y la <mark>prevención y extinción de incendios</mark>.",
 "Otra cosa es que sea un servicio obligatorio: según el art. 26, solo lo es en municipios de más de 20.000 habitantes.",
 "Incendios: <mark>competencia propia</mark> del municipio.","Ley 7/1985, art. 25.2.f")

q("Régimen local","normal","Según el art. 18 de la Ley 7/1985, la inscripción de un extranjero en el padrón municipal:",
 ["No prueba su residencia legal en España ni le da derechos que no le reconozca la ley.","Le concede automáticamente el permiso de residencia.","Solo es posible si tiene nacionalidad europea."],0,
 "Le da derecho a votar en todas las elecciones.",
 "El <mark>padrón</mark> es el registro de los vecinos del municipio.",
 "Inscribirse en él <mark>no constituye prueba de residencia legal</mark> en España ni atribuye derechos distintos de los que reconoce la legislación de extranjería.",
 "El padrón refleja dónde vive alguien, no su situación administrativa.",
 "Padrón ≠ <mark>residencia legal</mark>.","Ley 7/1985, art. 18.2")

q("EBEP","normal","Según el art. 89 del TREBEP, ¿cuál de estas NO es una modalidad de excedencia de los funcionarios de carrera?",
 ["La excedencia por estudios.","La excedencia por razón de violencia de género.","La excedencia voluntaria por agrupación familiar."],0,
 "La excedencia por cuidado de familiares.",
 "La <mark>excedencia</mark> es una situación en la que el funcionario deja de prestar servicio durante un tiempo.",
 "Las modalidades son: <mark>interés particular</mark>, <mark>agrupación familiar</mark>, <mark>cuidado de familiares</mark>, <mark>violencia de género</mark> y <mark>violencia terrorista</mark>.",
 "La excedencia por estudios no aparece en el art. 89.",
 "Excedencias: <mark>interés particular, agrupación familiar, cuidado de familiares, violencia de género y terrorista</mark>.","TREBEP, art. 89")

q("EBEP","normal","Según el art. 96 del TREBEP, la sanción de suspensión firme de funciones tiene una duración máxima de:",
 ["6 años.","3 años.","1 año."],0,"10 años.",
 "La <mark>suspensión firme</mark> aparta al funcionario de sus funciones como sanción disciplinaria.",
 "Puede durar como máximo <mark>6 años</mark>.",
 "La separación del servicio, que es más grave, solo puede imponerse por faltas muy graves.",
 "Suspensión firme: <mark>máximo 6 años</mark>.","TREBEP, art. 96.1.c")

q("EBEP","normal","Según el art. 96 del TREBEP, la separación del servicio de un funcionario solo puede imponerse por:",
 ["Faltas muy graves.","Faltas graves.","Cualquier falta, si hay reincidencia."],0,"Una condena penal leve.",
 "La <mark>separación del servicio</mark> es la sanción más grave: supone perder la condición de funcionario.",
 "Solo puede sancionar la comisión de <mark>faltas muy graves</mark>. En los interinos supone la revocación del nombramiento.",
 "Otras sanciones son el traslado forzoso, el demérito y el apercibimiento.",
 "Separación del servicio: <mark>solo faltas muy graves</mark>.","TREBEP, art. 96.1.a")

q("EBEP","normal","Según el art. 48 del TREBEP, el permiso por traslado de domicilio sin cambio de residencia es de:",
 ["Un día.","Dos días.","Tres días hábiles."],0,"No existe ese permiso.",
 "El art. 48 recoge los <mark>permisos</mark> de los funcionarios.",
 "Por <mark>traslado de domicilio sin cambio de residencia</mark> corresponde <mark>un día</mark>.",
 "Para exámenes finales, el permiso dura los días de su celebración.",
 "Mudanza en la misma localidad: <mark>1 día</mark>.","TREBEP, art. 48.b")

q("EBEP","normal","Según el art. 14 del TREBEP, ¿cuál de estos es un derecho individual de los empleados públicos?",
 ["La inamovilidad en la condición de funcionario de carrera.","Elegir libremente su puesto de trabajo.","No ser trasladado nunca de localidad."],0,
 "Cobrar horas extraordinarias en todo caso.",
 "El art. 14 enumera los <mark>derechos individuales</mark> de los empleados públicos.",
 "El primero es la <mark>inamovilidad</mark> en la condición de funcionario de carrera; también la progresión en la carrera, las retribuciones y la defensa jurídica, entre otros.",
 "La inamovilidad protege la condición de funcionario, no un puesto o una localidad concretos.",
 "Art. 14.a: <mark>inamovilidad</mark>.","TREBEP, art. 14")

q("Procedimiento administrativo","normal","Según el art. 77 de la Ley 39/2015, el período de prueba ordinario tiene una duración:",
 ["No superior a treinta días ni inferior a diez.","No superior a quince días ni inferior a cinco.","De dos meses como máximo."],0,
 "No superior a cuarenta días ni inferior a veinte.",
 "El <mark>período de prueba</mark> se abre cuando la Administración no da por ciertos los hechos alegados.",
 "Dura <mark>entre 10 y 30 días</mark>. A petición de los interesados puede abrirse uno <mark>extraordinario</mark> de hasta <mark>10 días</mark>.",
 "Las pruebas solo pueden rechazarse si son manifiestamente improcedentes o innecesarias, mediante resolución motivada.",
 "Prueba: <mark>10 a 30 días</mark> · extraordinaria: <mark>hasta 10</mark>.","Ley 39/2015, art. 77")

q("Procedimiento administrativo","normal","Según el art. 80 de la Ley 39/2015, salvo disposición expresa en contrario, los informes son:",
 ["Facultativos y no vinculantes.","Preceptivos y vinculantes.","Preceptivos y no vinculantes."],0,"Facultativos y vinculantes.",
 "Un <mark>informe</mark> es la opinión técnica o jurídica de un órgano dentro del procedimiento.",
 "Por regla general son <mark>facultativos</mark> (no es obligatorio pedirlos) y <mark>no vinculantes</mark> (no obligan a resolver en su sentido).",
 "Si una norma dice lo contrario, pueden ser preceptivos o vinculantes.",
 "Informes: <mark>facultativos y no vinculantes</mark>.","Ley 39/2015, art. 80.1")

q("Procedimiento administrativo","normal","Según el art. 80 de la Ley 39/2015, salvo que se disponga otro plazo, los informes se emiten en:",
 ["Diez días.","Quince días.","Un mes."],0,"Tres días.",
 "Los informes deben emitirse por <mark>medios electrónicos</mark>.",
 "El plazo general es de <mark>diez días</mark>. Si no se emite, se puede seguir el procedimiento, salvo que el informe sea <mark>preceptivo</mark>.",
 "Si el informe es preceptivo y se retrasa, puede suspenderse el plazo máximo para resolver.",
 "Informe: <mark>10 días</mark>.","Ley 39/2015, art. 80.2")

q("Procedimiento administrativo","normal","Según el art. 83 de la Ley 39/2015, en el trámite de información pública el plazo para formular alegaciones no puede ser inferior a:",
 ["Veinte días.","Diez días.","Quince días."],0,"Cinco días.",
 "La <mark>información pública</mark> permite que cualquier persona examine el expediente.",
 "Se publica un anuncio en el diario oficial y el plazo para alegar <mark>nunca puede ser inferior a veinte días</mark>.",
 "No comparecer en este trámite no impide recurrir después la resolución.",
 "Información pública: <mark>mínimo 20 días</mark>.","Ley 39/2015, art. 83")

q("Procedimiento administrativo","normal","Según el art. 24 de la Ley 39/2015, en los procedimientos relativos al derecho de petición del art. 29 CE, el silencio administrativo tiene efecto:",
 ["Desestimatorio.","Estimatorio.","Estimatorio, salvo que una ley diga lo contrario."],0,"No existe silencio en ese procedimiento.",
 "El <mark>silencio administrativo</mark> es el efecto que se da a la falta de resolución en plazo.",
 "La regla general es el silencio <mark>estimatorio</mark>, pero es <mark>desestimatorio</mark>, entre otros, en el <mark>derecho de petición</mark>, en la responsabilidad patrimonial y en los que afectan al dominio público.",
 "La desestimación por silencio solo sirve para poder recurrir.",
 "Derecho de petición: <mark>silencio negativo</mark>.","Ley 39/2015, art. 24.1")

q("Procedimiento administrativo","normal","Según el art. 24 de la Ley 39/2015, el certificado acreditativo del silencio se expide de oficio en el plazo de:",
 ["Quince días desde que expira el plazo máximo para resolver.","Un mes desde la solicitud.","Diez días desde la petición del interesado."],0,"Tres meses desde que se inició el procedimiento.",
 "El <mark>certificado de silencio</mark> sirve para acreditar que se ha producido.",
 "Lo expide de oficio el órgano competente en <mark>quince días</mark> desde que vence el plazo para resolver. El interesado puede pedirlo en cualquier momento.",
 "El silencio también puede acreditarse por cualquier otro medio de prueba.",
 "Certificado de silencio: <mark>15 días</mark>.","Ley 39/2015, art. 24.4")

q("Procedimiento administrativo","normal","Según el art. 102 de la Ley 39/2015, la ejecución subsidiaria procede cuando:",
 ["El acto no es personalísimo y puede realizarlo otra persona a costa del obligado.","El obligado tiene que cumplir personalmente una obligación de no hacer.","Hay que cobrar una deuda en dinero."],0,
 "La Administración impone una multa reiterada.",
 "La <mark>ejecución subsidiaria</mark> es un medio de ejecución forzosa.",
 "La Administración realiza el acto, por sí o por otros, <mark>a costa del obligado</mark>, cuando el acto <mark>no es personalísimo</mark>. El importe puede liquidarse provisionalmente antes de ejecutar.",
 "Para cobrar dinero se usa el apremio sobre el patrimonio.",
 "Ejecución subsidiaria: <mark>lo hace otro y paga el obligado</mark>.","Ley 39/2015, art. 102")

q("Procedimiento administrativo","normal","Según el art. 104 de la Ley 39/2015, la compulsión sobre las personas puede usarse para obligaciones personalísimas:",
 ["De no hacer o soportar, cuando la ley lo autorice expresamente.","De pagar una cantidad de dinero.","De hacer, en todo caso y sin límites."],0,
 "De cualquier tipo, si lo decide el instructor.",
 "La <mark>compulsión directa</mark> es el medio de ejecución más intenso: actúa sobre la propia persona.",
 "Solo cabe en obligaciones personalísimas de <mark>no hacer o soportar</mark>, si la <mark>ley lo autoriza expresamente</mark> y respetando su dignidad y derechos.",
 "Si una obligación personalísima de hacer no se cumple, el obligado debe resarcir los daños y perjuicios.",
 "Compulsión: <mark>no hacer o soportar + ley expresa</mark>.","Ley 39/2015, art. 104")

q("PRL","normal","Según el art. 15 de la Ley 31/1995, el primer principio general de la acción preventiva es:",
 ["Evitar los riesgos.","Facilitar equipos de protección individual.","Formar a los trabajadores."],0,"Investigar los accidentes.",
 "El art. 15 ordena los <mark>principios de la acción preventiva</mark>.",
 "Empieza por <mark>evitar los riesgos</mark>; después, <mark>evaluar</mark> los que no se puedan evitar y <mark>combatirlos en su origen</mark>, entre otros.",
 "La protección colectiva tiene prioridad sobre la individual.",
 "Prevención: <mark>evitar → evaluar → combatir en origen</mark>.","Ley 31/1995, art. 15")

q("PRL","normal","Según el art. 22 de la Ley 31/1995, con carácter general, la vigilancia de la salud de los trabajadores:",
 ["Solo puede hacerse si el trabajador da su consentimiento.","Es obligatoria en todos los casos.","La decide el Comité de Seguridad y Salud."],0,"Solo se hace a los mayores de 50 años.",
 "La <mark>vigilancia de la salud</mark> son los reconocimientos médicos en función de los riesgos del puesto.",
 "La garantiza el empresario, pero es <mark>voluntaria</mark>: requiere el <mark>consentimiento</mark> del trabajador, salvo excepciones como las actividades de especial peligrosidad.",
 "Las excepciones requieren informe previo de los representantes de los trabajadores.",
 "Vigilancia de la salud: <mark>voluntaria, salvo excepciones</mark>.","Ley 31/1995, art. 22")

q("PRL","normal","Según el art. 21 de la Ley 31/1995, ante un peligro grave, inminente e inevitable:",
 ["Los trabajadores pueden interrumpir su actividad y no se les puede exigir que la reanuden mientras persista el peligro.","Los trabajadores deben seguir trabajando hasta que llegue un superior.","Solo el Comité de Seguridad y Salud puede ordenar la evacuación."],0,
 "Los trabajadores pierden el sueldo de las horas que no trabajen.",
 "El art. 21 regula el <mark>riesgo grave e inminente</mark>.",
 "El empresario debe informar lo antes posible y permitir que los trabajadores <mark>interrumpan su actividad</mark> y abandonen el lugar. <mark>No puede exigirse reanudarla</mark> mientras siga el peligro, salvo excepción justificada.",
 "Los trabajadores no pueden sufrir perjuicio por esa decisión, salvo que hayan actuado de mala fe o con negligencia grave.",
 "Riesgo grave e inminente: <mark>se puede parar y salir</mark>.","Ley 31/1995, art. 21")

q("Igualdad","normal","Según el art. 8 de la LO 3/2007, el trato desfavorable a una mujer relacionado con el embarazo o la maternidad es:",
 ["Discriminación directa por razón de sexo.","Discriminación indirecta por razón de sexo.","Una acción positiva."],0,"Una infracción leve sin relación con el sexo.",
 "La ley protege especialmente el <mark>embarazo y la maternidad</mark>.",
 "Todo trato desfavorable relacionado con ellos constituye <mark>discriminación directa</mark> por razón de sexo.",
 "La indirecta es la que nace de una norma aparentemente neutra que perjudica a un sexo.",
 "Embarazo o maternidad: <mark>discriminación directa</mark>.","LO 3/2007, art. 8")

q("Igualdad","normal","Según el art. 11 de la LO 3/2007, las acciones positivas a favor de las mujeres:",
 ["Se aplican mientras subsistan las situaciones de desigualdad y deben ser razonables y proporcionadas.","Son permanentes y no pueden retirarse.","Solo pueden adoptarlas los poderes públicos."],0,
 "Solo se aplican en el sector privado.",
 "Las <mark>acciones positivas</mark> son medidas específicas para corregir desigualdades de hecho.",
 "Se aplican <mark>en tanto subsistan</mark> esas situaciones y deben ser <mark>razonables y proporcionadas</mark>. También pueden adoptarlas las personas físicas y jurídicas privadas.",
 "No son un privilegio permanente: desaparecen cuando se corrige la desigualdad.",
 "Acción positiva: <mark>temporal, razonable y proporcionada</mark>.","LO 3/2007, art. 11")

q("Igualdad","normal","Según el art. 9 de la LO 3/2007, un trato adverso a una persona por haber presentado una reclamación para exigir la igualdad de trato se considera:",
 ["Discriminación por razón de sexo.","Una medida disciplinaria legítima.","Una acción positiva."],0,"Un conflicto laboral ordinario.",
 "El art. 9 recoge la <mark>indemnidad frente a represalias</mark>.",
 "Cualquier trato adverso o efecto negativo por presentar una <mark>queja, reclamación o denuncia</mark> para exigir la igualdad se considera <mark>discriminación por razón de sexo</mark>.",
 "Así se protege a quien reclama sus derechos.",
 "Represalia por reclamar = <mark>discriminación</mark>.","LO 3/2007, art. 9")

q("Protección civil","normal","Según el art. 2 de la Ley 17/2015, el «potencial de ocasionar daño» a personas o bienes que la protección civil debe preservar se denomina:",
 ["Peligro.","Vulnerabilidad.","Catástrofe."],0,"Servicio esencial.",
 "La Ley 17/2015 define los conceptos básicos de la protección civil.",
 "El <mark>peligro</mark> es el potencial de causar daño; la <mark>amenaza</mark>, la exposición a un peligro inminente o latente; y la <mark>vulnerabilidad</mark>, la característica que hace a personas o bienes susceptibles de ser afectados.",
 "No hay que confundir el peligro con el riesgo, que es la posibilidad de que la amenaza llegue a afectar.",
 "Peligro = <mark>potencial de daño</mark>.","Ley 17/2015, art. 2")

q("Protección civil","normal","Según el art. 2 de la Ley 17/2015, una catástrofe se caracteriza porque:",
 ["Su atención supera los medios disponibles de la propia comunidad.","Afecta como mínimo a dos Comunidades Autónomas.","Solo puede tener origen natural."],0,"Siempre causa más de cien víctimas.",
 "La <mark>catástrofe</mark> es el nivel más grave de situación de protección civil.",
 "Altera o interrumpe sustancialmente el funcionamiento de una comunidad, con gran cantidad de víctimas y daños, y su atención <mark>supera los medios de la propia comunidad</mark>.",
 "La ley no fija un número mínimo de víctimas.",
 "Catástrofe: <mark>supera los medios propios</mark>.","Ley 17/2015, art. 2.6")

q("Protección civil","normal","Según el art. 2 de la Ley 17/2015, la emergencia ordinaria se diferencia de la emergencia de protección civil en que:",
 ["No tiene afectación colectiva.","Siempre es más grave.","La gestiona el Estado."],0,"Solo ocurre de noche.",
 "La <mark>emergencia de protección civil</mark> (o extraordinaria) es una situación de riesgo colectivo que exige una gestión rápida de los poderes públicos.",
 "La <mark>emergencia ordinaria</mark>, en cambio, <mark>no tiene afectación colectiva</mark>: por ejemplo, un incendio en una sola vivienda.",
 "Si una emergencia de protección civil no se controla, puede convertirse en catástrofe.",
 "Ordinaria: <mark>sin afectación colectiva</mark>.","Ley 17/2015, art. 2.5")

q("Reglamento Bomberos","normal","Según el art. 4 del Reglamento del Cuerpo de Bomberos, el Cuerpo actúa bajo la superior autoridad y dependencia directa:",
 ["Del Alcalde, que puede delegar en el Concejal del Área de Seguridad u otro miembro de la Corporación.","Del Delegado del Gobierno en Madrid.","Del Presidente de la Comunidad de Madrid."],0,
 "Del Jefe del Cuerpo, sin posibilidad de delegación.",
 "El art. 4 fija de quién depende el Cuerpo de Bomberos.",
 "Depende directamente del <mark>Alcalde</mark>, que puede <mark>delegar</mark> sus funciones en el <mark>Concejal del Área de Seguridad</mark> o en otro miembro de la Corporación.",
 "La competencia es municipal, no autonómica ni estatal.",
 "Bomberos de Madrid: <mark>dependen del Alcalde</mark>.","Reglamento del Cuerpo de Bomberos, art. 4")

q("Reglamento Bomberos","normal","Según el art. 2 del Reglamento, cuando el Cuerpo de Bomberos de Madrid se envía a una catástrofe fuera del municipio, sus dotaciones actúan:",
 ["Bajo la dirección inmediata de sus mandos naturales.","A las órdenes directas del alcalde del municipio afectado.","Sin mandos propios."],0,"Bajo el mando del primer vecino que pida ayuda.",
 "El Alcalde de Madrid puede enviar efectivos a cualquier lugar del territorio nacional ante una <mark>catástrofe o calamidad pública</mark>.",
 "Se hace a petición urgente del Gobierno, de la autoridad de protección civil autonómica o del alcalde afectado, y las dotaciones actúan bajo la <mark>dirección inmediata de sus mandos naturales</mark>.",
 "La petición puede hacerse sin formalidad alguna, por la urgencia.",
 "Fuera de Madrid: <mark>con sus propios mandos</mark>.","Reglamento del Cuerpo de Bomberos, art. 2.4")

q("Reglamento Bomberos","normal","Según el Reglamento del Cuerpo de Bomberos, los Bomberos de actuación directa realizan en los parques guardias de:",
 ["Veinticuatro horas.","Doce horas.","Ocho horas."],0,"Cuarenta y ocho horas.",
 "El Reglamento describe las funciones de cada categoría.",
 "Bomberos, Cabos y Cabos conductores realizan <mark>guardias de veinticuatro horas</mark> en los parques, turnándose entre los de su categoría, y asisten a los siniestros que se les ordenen.",
 "El Cabo, como primero de la dotación, además pasa revista al terminar el siniestro.",
 "Guardias: <mark>24 horas</mark>.","Reglamento del Cuerpo de Bomberos, arts. 21-23")

q("Reglamento Bomberos","normal","Según el art. 29 del Reglamento, en todos los actos del servicio el personal con mando:",
 ["Asume siempre el puesto de mayor responsabilidad.","Permanece siempre en el vehículo de mando.","Delega el riesgo en el bombero más antiguo."],0,"Se retira cuando el siniestro es grave.",
 "El art. 29 refleja el <mark>espíritu de mando</mark> del Cuerpo.",
 "El mando asume siempre el <mark>puesto de mayor responsabilidad</mark> y busca el lugar desde el que pueda controlar y asumir el riesgo que corren sus subordinados.",
 "Mandar implica estar donde se controla la situación.",
 "Mando: <mark>el puesto de mayor responsabilidad</mark>.","Reglamento del Cuerpo de Bomberos, art. 29")

q("CTE DB-SI","normal","Según el DB-SI 4, con carácter general debe haber un extintor de eficacia 21A-113B a una distancia de recorrido máxima, desde todo origen de evacuación, de:",
 ["15 m.","25 m.","10 m."],0,"50 m.",
 "Los <mark>extintores portátiles</mark> son la instalación de protección más básica.",
 "Con carácter general debe haber uno de eficacia <mark>21A-113B</mark> a <mark>15 m de recorrido</mark> como máximo en cada planta, y en las zonas de riesgo especial.",
 "21A indica la eficacia frente a fuegos de sólidos y 113B, frente a líquidos.",
 "Extintores: <mark>21A-113B cada 15 m</mark>.","CTE DB-SI 4, tabla 1.1")

q("CTE DB-SI","normal","Según el DB-SI 5, la altura mínima libre o gálibo de los viales de aproximación de los vehículos de bomberos es de:",
 ["4,5 m.","3,5 m.","4 m."],0,"5,5 m.",
 "Los <mark>viales de aproximación</mark> llevan a los vehículos de bomberos hasta el espacio de maniobra.",
 "Deben tener una <mark>anchura mínima libre de 3,5 m</mark>, una <mark>altura libre o gálibo de 4,5 m</mark> y una capacidad portante de 20 kN/m².",
 "Los 3,5 m son la anchura, no la altura.",
 "Viales: <mark>3,5 m de ancho · 4,5 m de gálibo · 20 kN/m²</mark>.","CTE DB-SI 5, apartado 1.1")

q("CTE DB-SI","normal","Según el DB-SI 5, en zonas edificadas junto a áreas forestales debe haber una franja libre de vegetación que pueda propagar el incendio de una anchura de:",
 ["25 m.","10 m.","50 m."],0,"5 m.",
 "La <mark>interfaz urbano-forestal</mark> es una zona de especial riesgo de incendio.",
 "Debe haber una <mark>franja de 25 m</mark> que separe lo edificado de lo forestal y un <mark>camino perimetral de 5 m</mark>, que puede estar incluido en la franja.",
 "Si solo hay un acceso, debe terminar en un fondo de saco circular de 12,50 m de radio.",
 "Interfaz forestal: <mark>franja de 25 m + camino de 5 m</mark>.","CTE DB-SI 5, apartado 1.2")

q("CTE DB-SI","normal","Según el DB-SI 4, para calcular la dotación de hidrantes de un edificio pueden tenerse en cuenta los hidrantes de la vía pública situados a menos de:",
 ["100 m de la fachada accesible.","50 m de la fachada accesible.","250 m de cualquier fachada."],0,"500 m del edificio.",
 "Los <mark>hidrantes exteriores</mark> abastecen de agua a los vehículos de bomberos.",
 "Se exige <mark>al menos uno hasta 10.000 m²</mark> construidos y uno más por cada 10.000 m² adicionales. Computan los de la vía pública a <mark>menos de 100 m</mark> de la fachada accesible.",
 "Los hidrantes que se instalen pueden estar conectados a la red pública de abastecimiento.",
 "Hidrantes: <mark>1 por cada 10.000 m²</mark> · públicos a <mark>menos de 100 m</mark>.","CTE DB-SI 4, tabla 1.1")

q("CTE DB-SI","normal","Según el DB-SI 4, las bocas de incendio equipadas serán de tipo 45 mm, excepto en uso Residencial Vivienda, donde serán de:",
 ["25 mm.","45 mm también.","70 mm."],0,"52 mm.",
 "Las <mark>BIE</mark> son mangueras fijas conectadas a una red de agua para la primera intervención.",
 "En general son de <mark>45 mm</mark>, pero en <mark>Residencial Vivienda</mark> son de <mark>25 mm</mark>, más manejables para personas sin formación.",
 "En las zonas de riesgo especial alto deben instalarse BIE cuando el riesgo se deba a materias combustibles sólidas.",
 "BIE: <mark>45 mm</mark> · viviendas <mark>25 mm</mark>.","CTE DB-SI 4")

q("CTE DB-SI","normal","Según el DB-SI 4, con carácter general, un edificio debe tener instalación automática de extinción si su altura de evacuación excede de:",
 ["80 m.","50 m.","28 m."],0,"120 m.",
 "La <mark>extinción automática</mark> (por ejemplo, rociadores) actúa sin intervención humana.",
 "Salvo otra indicación según el uso, es obligatoria en todo edificio con una altura de evacuación de <mark>más de 80 m</mark>, y también en algunas cocinas industriales y centros de transformación.",
 "28 m es el umbral del ascensor de emergencia y 50 m, el de detección y alarma en viviendas.",
 "Extinción automática: <mark>más de 80 m</mark>.","CTE DB-SI 4, tabla 1.1")

q("Gas y GLP","normal","Según el manual, el componente principal del gas natural, en torno al 80 % de su volumen, es:",
 ["El metano.","El propano.","El butano."],0,"El etano.",
 "El <mark>gas natural</mark> es una mezcla de hidrocarburos ligeros.",
 "Está formado en un <mark>80 %</mark> aproximadamente por <mark>metano</mark>; el resto lo componen etano, propano, butano y otros gases.",
 "Propano y butano son los gases licuados del petróleo (GLP).",
 "Gas natural = <mark>sobre todo metano</mark>.","Manual de gas natural")

q("Gas y GLP","normal","Según el manual, para transportarlo en buques metaneros, el gas natural se licúa enfriándolo hasta unos:",
 ["−160 °C.","−42 °C.","0 °C."],0,"−273 °C.",
 "El <mark>GNL</mark> es gas natural licuado.",
 "En las plantas de licuefacción se enfría a <mark>−160 °C</mark> para transportarlo en <mark>buques metaneros</mark> hasta las plantas de regasificación.",
 "Al licuarse ocupa muchísimo menos volumen, lo que hace rentable su transporte por mar.",
 "GNL: <mark>−160 °C</mark>.","Manual de gas natural")

q("Gas y GLP","normal","Según el manual, las redes de distribución de gas natural trabajan con una presión máxima:",
 ["Igual o inferior a 16 bar.","Igual o superior a 60 bar.","Entre 60 y 16 bar."],0,"Igual o inferior a 0,05 bar.",
 "El gas natural llega a los consumidores a través de redes con distintas presiones.",
 "<mark>Transporte primario</mark>: <mark>60 bar o más</mark>. <mark>Transporte secundario</mark>: <mark>entre 60 y 16 bar</mark>. <mark>Distribución</mark>: <mark>16 bar o menos</mark>.",
 "Las presiones bajan en las estaciones de regulación y medida (ERM).",
 "Gas: <mark>≥60</mark> · <mark>60-16</mark> · <mark>≤16 bar</mark>.","Manual de gas natural")

q("Gas y GLP","normal","Según el manual, en una intervención en un edificio, ver un armario de regulación en la fachada y montantes de sección pequeña indica que la acometida es de:",
 ["Media presión.","Baja presión.","Alta presión."],0,"Transporte secundario.",
 "En Madrid conviven acometidas de <mark>baja presión</mark>, sobre todo en la almendra central, y de <mark>media presión</mark> en el resto.",
 "En <mark>media presión</mark> los montantes son más pequeños (1\" o 1½\") y hay <mark>armario de regulación en la fachada</mark>. En <mark>baja presión</mark> los montantes son grandes y no hay armario.",
 "Identificar la presión ayuda a prever cuánto gas puede salir en una fuga.",
 "Armario de regulación en fachada → <mark>media presión</mark>.","Manual de gas natural")

q("Gas y GLP","normal","Según el manual, una fuga de gas natural puede producir asfixia porque desplaza el aire y la concentración de oxígeno baja de:",
 ["19,5 %.","50 %.","5 %."],0,"30 %.",
 "El gas natural no es tóxico, pero <mark>desplaza el oxígeno</mark>.",
 "Por debajo del <mark>19,5 % de oxígeno</mark> aparecen mareo, aumento del ritmo cardiaco y respiratorio y dolor de cabeza, y puede llegar a producirse <mark>asfixia</mark>.",
 "El aire normal tiene en torno a un 21 % de oxígeno.",
 "Asfixia: <mark>O₂ por debajo del 19,5 %</mark>.","Manual de gas natural")

q("Gas y GLP","normal","Según el manual, en las redes de gas se usan mayoritariamente tuberías de polietileno enterradas para presiones:",
 ["Hasta 10 bar; por encima se usa acero.","De más de 60 bar.","Solo dentro de las viviendas."],0,"Por encima de 16 bar.",
 "El material de la tubería depende de la <mark>presión</mark> que tiene que soportar.",
 "Hasta <mark>10 bar</mark> se usa sobre todo <mark>polietileno</mark> enterrado; para presiones mayores, <mark>acero</mark>.",
 "La red de transporte en alta presión va enterrada a mayor profundidad.",
 "Polietileno <mark>hasta 10 bar</mark> · acero <mark>por encima</mark>.","Manual de gas natural")

q("Electricidad","normal","Según el manual, un centro de transformación convierte la alta tensión, normalmente de 20 kV, en baja tensión de:",
 ["400/230 V.","230/125 V.","66 kV."],0,"1.000/500 V.",
 "Los <mark>centros de transformación</mark> son la última etapa antes de llegar a los usuarios.",
 "Reciben normalmente <mark>20 kV</mark> y entregan <mark>baja tensión de 400/230 V</mark>.",
 "El antiguo sistema B1 trabajaba a 230/125 V.",
 "CT: <mark>20 kV → 400/230 V</mark>.","Manual de instalaciones eléctricas")

q("Electricidad","normal","Según el manual, en las centrales eléctricas la energía se genera a una tensión de entre:",
 ["3 y 36 kV.","220 y 400 kV.","230 y 400 V."],0,"1 y 2 V.",
 "La electricidad se produce en las <mark>centrales</mark> y se eleva para transportarla.",
 "Se genera entre <mark>3 y 36 kV</mark> y las estaciones elevadoras la suben a unos <mark>220 kV</mark>, pudiendo llegar a <mark>400 kV</mark>.",
 "Transportar a muy alta tensión reduce las pérdidas.",
 "Generación: <mark>3-36 kV</mark> · Transporte: <mark>220-400 kV</mark>.","Manual de instalaciones eléctricas")

q("Electricidad","normal","Según el manual, el antiguo sistema B1 de distribución en baja tensión, de 3 conductores, trabajaba a:",
 ["230/125 V.","400/230 V.","20 kV."],0,"380/220 V con 5 conductores.",
 "En baja tensión hay dos sistemas de distribución.",
 "El antiguo <mark>B1</mark>, de 3 conductores, trabajaba a <mark>230/125 V</mark>. El actual <mark>B2</mark> trabaja a <mark>400/230 V</mark>.",
 "Todavía pueden encontrarse instalaciones antiguas en algunos edificios.",
 "B1: <mark>230/125 V</mark> · B2: <mark>400/230 V</mark>.","Manual de instalaciones eléctricas")

q("ACS","normal","Según el manual de ACS, los contadores de agua caliente son los preparados para temperaturas de:",
 ["Entre 30 y 90 °C.","Menos de 30 °C.","Más de 100 °C."],0,"Entre 0 y 15 °C.",
 "Los contadores se clasifican por la <mark>temperatura del agua</mark> que miden.",
 "Los de <mark>agua fría</mark> trabajan por debajo de <mark>30 °C</mark> y los de <mark>agua caliente</mark>, entre <mark>30 y 90 °C</mark>.",
 "En un edificio comunitario debe haber un contador de ACS por cada usuario si la producción es centralizada.",
 "Contador frío <mark>&lt;30 °C</mark> · caliente <mark>30-90 °C</mark>.","Manual de ACS")

q("ACS","normal","Según el manual de ACS, como regla general, la contribución mínima de energías renovables a la demanda energética anual de ACS debe ser de al menos:",
 ["El 70 % de la demanda anual de ACS.","El 20 % de la demanda anual de ACS.","El 100 % de la demanda anual de ACS."],0,"El 5 % de la demanda anual de ACS.",
 "El CTE obliga a cubrir parte de la demanda de ACS con <mark>energías renovables</mark>.",
 "Como regla general, al menos el <mark>70 %</mark> de la demanda anual. Puede bajar al <mark>60 %</mark> si la demanda es inferior a 5.000 l/día.",
 "La misma exigencia se aplica a la climatización de piscinas.",
 "Renovables en ACS: <mark>70 %</mark> (60 % si &lt;5.000 l/día).","Manual de ACS")

q("Agua fría","normal","Según el manual, la presión mínima que necesitan los fluxores y los calentadores es de:",
 ["1,5 bar (150 kPa).","0,5 bar (50 kPa).","5 bar (500 kPa)."],0,"10 bar (1.000 kPa).",
 "Algunos aparatos necesitan más presión que un grifo normal para funcionar.",
 "Los <mark>fluxores y calentadores</mark> requieren como mínimo <mark>150 kPa</mark>, es decir, <mark>1,5 bar</mark> o 15 m de columna de agua.",
 "La presión máxima en las instalaciones interiores es de 500 kPa (5 bar).",
 "Fluxores y calentadores: <mark>mínimo 1,5 bar</mark>.","Manual de agua fría para consumo humano")

q("Ascensores","normal","Según el manual de rescate en ascensores, para rescatar a las personas por el piso superior, el hueco libre entre la cabina y la planta debe ser mayor de:",
 ["80 cm.","40 cm.","1,5 m."],0,"20 cm.",
 "Cuando la cabina queda entre dos plantas, hay que decidir por dónde sacar a los ocupantes.",
 "El rescate por el <mark>piso superior</mark> sin mover la cabina solo se hace si el hueco libre es <mark>mayor de 80 cm</mark>. Antes hay que cortar la corriente y asegurar el cierre de todas las puertas.",
 "Si el hueco es menor, primero hay que desplazar la cabina hasta una planta.",
 "Rescate por arriba: <mark>hueco de más de 80 cm</mark>.","Manual de rescate en ascensores")

q("Ascensores","normal","Según el manual, para atender a las personas atrapadas en un ascensor, los fabricantes deben disponer de:",
 ["Un servicio de asistencia 24 horas.","Un técnico en cada edificio.","Un bombero de guardia en su empresa."],0,"Un servicio que solo atiende en horario laboral.",
 "Las personas atrapadas pueden pedir ayuda desde la cabina.",
 "Los fabricantes y mantenedores tienen un <mark>servicio de asistencia 24 horas</mark> para atender estas incidencias.",
 "Los bomberos intervienen cuando hay urgencia o el servicio de asistencia no puede actuar a tiempo.",
 "Ascensores: <mark>asistencia 24 horas</mark>.","Manual de rescate en ascensores")

q("Apícola","normal","Según el manual de rescate apícola y de otras especies, el peligro del lagarto ocelado está en:",
 ["El firme cierre de su mandíbula.","Su veneno, muy potente.","Su velocidad para atacar."],0,"Las espinas venenosas de su cola.",
 "El <mark>lagarto ocelado</mark> es un reptil grande y verdoso, con manchas azules, de 50-60 cm que puede llegar a 90 cm.",
 "Su peligro es el <mark>firme cierre de su mandíbula</mark>: muerde con fuerza y luego apenas tiene fuerza para abrirla. Al ser de sangre fría, el <mark>frío lo deja inactivo</mark>.",
 "No es venenoso.",
 "Lagarto ocelado: <mark>mordisco firme, sin veneno</mark>.","Manual de rescate apícola y de otras especies")

q("Apícola","normal","Según el manual, cuando se iza con eslingas a un animal grande, no conviene mantenerlo suspendido más de:",
 ["15 minutos.","1 hora.","2 minutos."],0,"3 horas.",
 "Rescatar animales grandes, como caballos o vacas, a veces exige <mark>izarlos</mark> con eslingas.",
 "Una vez izado, no debe estar suspendido <mark>más de 15 minutos</mark> para evitar <mark>lesiones en los órganos internos</mark>.",
 "Las eslingas se colocan de forma que no se junten delante ni detrás, para no dañar al animal.",
 "Animal izado: <mark>máximo 15 minutos</mark>.","Manual de rescate apícola y de otras especies")

q("Apícola","normal","Según el manual, cuando el servicio municipal se hace cargo de un animal recogido, lo cuida durante un máximo de:",
 ["20 días.","2 días.","6 meses."],0,"1 año.",
 "Los animales recogidos en una intervención pasan a cargo del servicio municipal competente.",
 "Este les proporciona alimento y cuidados sanitarios durante un <mark>máximo de 20 días</mark>. El propietario tiene entre <mark>5 y 20 días</mark>, según la comunidad autónoma, para retirarlo pagando los gastos.",
 "Pasado ese tiempo, el servicio decide qué hacer con el animal, por ejemplo darlo en adopción.",
 "Animal recogido: <mark>hasta 20 días</mark>.","Manual de rescate apícola y de otras especies")

q("Corte y soldadura","normal","Según el manual, el oxicorte es apto para cortar elementos metálicos oxidables de hasta:",
 ["60 mm de espesor.","6 mm de espesor.","600 mm de espesor."],0,"2 mm de espesor.",
 "El <mark>oxicorte</mark> corta el metal quemándolo con un chorro de oxígeno tras precalentarlo.",
 "Es apto para metales <mark>oxidables</mark> de hasta <mark>60 mm</mark> de espesor, sobre todo los de hierro y acero.",
 "No es recomendable en metales que no se oxidan con facilidad, como el aluminio o el acero inoxidable.",
 "Oxicorte: <mark>hasta 60 mm</mark>.","Manual de corte térmico y soldadura")

q("Corte y soldadura","normal","Según el manual de corte térmico, la boquilla número 2 del soplete se usa para espesores de entre:",
 ["15 y 25 mm.","1 y 3 mm.","50 y 60 mm."],0,"100 y 150 mm.",
 "Las <mark>boquillas</mark> se eligen según el espesor que se va a cortar.",
 "La <mark>número 2</mark> sirve para espesores de <mark>15 a 25 mm</mark>. Algunos vehículos llevan boquillas hasta la número 5, para espesores mayores.",
 "Cuanto mayor es el número, mayor es el espesor que permite cortar.",
 "Boquilla n.º 2: <mark>15-25 mm</mark>.","Manual de corte térmico y soldadura")

q("Trabajos en altura","normal","Según el manual de trabajos verticales, es muy recomendable que la cuerda de seguridad:",
 ["Sea de un color distinto al de la cuerda de trabajo.","Sea dinámica.","Tenga menos de 8 mm de diámetro."],0,"Esté atada al mismo anclaje que la de trabajo.",
 "En trabajos verticales se usan dos cuerdas: la de <mark>trabajo</mark> y la de <mark>seguridad</mark>.",
 "Conviene que la de seguridad sea de un <mark>color distinto</mark>, para no confundirlas. Para la seguridad de las personas solo deben usarse cuerdas de <mark>10 mm o más</mark>.",
 "Cada cuerda debe tener su propio anclaje.",
 "Cuerda de seguridad: <mark>otro color</mark> y <mark>≥10 mm</mark>.","Manual de trabajos en altura")

q("Trabajos en altura","normal","Según el manual, los bloqueadores tienen una resistencia superior a 15 kN, pero están pensados para soportar cargas de, como máximo:",
 ["Unos 400 kg.","Unos 40 kg.","Unos 4.000 kg."],0,"Unos 15 kg.",
 "Los <mark>bloqueadores</mark> se deslizan en un sentido y se bloquean en el otro al cargar peso.",
 "Aunque resisten más de <mark>15 kN</mark>, están pensados para cargas moderadas de <mark>unos 400 kg</mark>: suficiente para una persona y su equipo. Por encima, pueden dañar la cuerda.",
 "Cuanto más se carga, más fuerte presionan la cuerda.",
 "Bloqueador: <mark>hasta unos 400 kg</mark>.","Manual de trabajos en altura")

q("Tráfico (APRAT)","normal","Según el APRAT, en una vía de doble sentido los triángulos de señalización de un accidente se colocan:",
 ["A 50 metros en ambos sentidos.","A 10 metros en ambos sentidos.","A 150 metros solo en el sentido del accidente."],0,"Junto al vehículo accidentado.",
 "Señalizar bien el accidente evita que se produzcan otros.",
 "En <mark>doble sentido</mark>, a <mark>50 m en ambos sentidos</mark>. En vías de un solo sentido, como las autovías, el primero a <mark>50 m</mark> y otro, si hace falta, a <mark>150 m como mínimo</mark>.",
 "Antes de salir del vehículo hay que ponerse el chaleco reflectante.",
 "Triángulos: <mark>50 m</mark> (y 150 m en autovía si hace falta).","APRAT I")

q("Tráfico (APRAT)","normal","Según el APRAT, en un atrapamiento Físico 1, la inmovilización y extracción de la víctima normalmente se hace:",
 ["Sin necesidad de que estén presentes los bomberos.","Siempre con cizalla y separador.","Cortando el techo del vehículo."],0,"Esperando a que llegue una grúa.",
 "En el <mark>Físico 1</mark>, la víctima no puede salir por sus lesiones, pero el vehículo no la atrapa.",
 "Por norma general la <mark>inmovilización y extracción</mark> se hace <mark>sin la presencia de bomberos</mark>. En el <mark>Físico 2</mark>, en cambio, no se recomienda liberar a la víctima sin ellos.",
 "En el Físico 2 la deformación del vehículo atrapa a la persona.",
 "Físico 1: <mark>sin bomberos</mark> · Físico 2: <mark>con bomberos</mark>.","APRAT II")

q("NRBQ","normal","Según el manual NRBQ, la densidad de referencia para líquidos y sólidos es la del agua a 1 atm y 4 °C, que es de:",
 ["1.000 kg/m³.","100 kg/m³.","8.700 kg/m³."],0,"19.300 kg/m³.",
 "La <mark>densidad</mark> indica si una sustancia flota o se hunde en el agua.",
 "La referencia es el <mark>agua a 4 °C</mark> y 1 atm: <mark>1.000 kg/m³</mark>, es decir, 1 kg/dm³. Como comparación, el hierro tiene 8.700 kg/m³ y el oro, 19.300 kg/m³.",
 "Un líquido menos denso que el agua flota sobre ella.",
 "Agua: <mark>1.000 kg/m³</mark> a 4 °C.","Manual NRBQ")

q("NRBQ","normal","Según el manual NRBQ, el límite inferior de inflamabilidad de la gasolina es de un:",
 ["1,4 %.","14 %.","50 %."],0,"0,1 %.",
 "El <mark>límite inferior de inflamabilidad</mark> (LII) es la concentración mínima de vapor en el aire para que pueda arder.",
 "Para la <mark>gasolina</mark> es el <mark>1,4 %</mark>: por debajo de esa concentración de vapor en el aire, la mezcla es demasiado pobre para arder.",
 "Por encima del límite superior, la mezcla es demasiado rica y tampoco arde.",
 "Gasolina: <mark>LII 1,4 %</mark>.","Manual NRBQ")

q("Vehículos","normal","Según la información de vehículos del SEI, una bomba de baja presión FPN 10/2000 proporciona:",
 ["2.000 litros por minuto a 10 bar.","10 litros por minuto a 2.000 bar.","1.000 litros por minuto a 20 bar."],0,"2.000 litros por hora a 1 bar.",
 "La denominación de las <mark>bombas</mark> indica su presión y su caudal.",
 "<mark>FPN 10/2000</mark> significa que a <mark>10 bar</mark> da <mark>2.000 l/min</mark>. Del mismo modo, una FPH 40/500 da 500 l/min a 40 bar.",
 "FPN es baja presión y FPH, alta presión.",
 "FPN 10/2000: <mark>10 bar · 2.000 l/min</mark>.","Información de vehículos del SEI")

q("Vehículos","normal","Según la información de vehículos del SEI, el cabrestante eléctrico de los vehículos tiene una tracción máxima en su primera capa de aproximadamente:",
 ["5.400 kg.","540 kg.","54.000 kg."],0,"150 kg.",
 "El <mark>cabrestante</mark> es un torno para arrastrar o sujetar cargas.",
 "Su tracción máxima, en la primera capa de cable, es de <mark>unos 5.400 kg</mark>. Según el vehículo, lleva cable metálico de 38 m o sintético de 25 m.",
 "La tracción disminuye en las capas exteriores del tambor.",
 "Cabrestante: <mark>unos 5.400 kg</mark>.","Información de vehículos del SEI")

q("Atención sanitaria","normal","Según el manual de atención inicial, ¿a qué se refiere la expresión «10 minutos platino»?",
 ["Al tiempo inicial en el que una atención correcta en el lugar del accidente aumenta mucho la supervivencia.","Al tiempo máximo para trasladar a un herido al hospital.","Al tiempo que tarda en hacer efecto la medicación."],0,
 "Al descanso obligatorio del equipo tras cada rescate.",
 "La atención <mark>prehospitalaria</mark> es decisiva en los traumatismos graves.",
 "Se habla de los <mark>«10 minutos platino»</mark> y de la <mark>«hora de oro»</mark>: tiempos en los que actuar correctamente aumenta la supervivencia de lesiones potencialmente graves.",
 "La hemorragia es una de las principales causas de muerte evitable en los traumatismos.",
 "<mark>10 minutos platino</mark> · <mark>hora de oro</mark>.","Manual de atención inicial al paciente")

q("Sanitario (SVB)","normal","Según el manual de SVB, si la RCP empieza en los primeros 4 minutos, la probabilidad de reanimación ronda el 80 %. Por cada minuto extra de retraso, esa probabilidad disminuye un:",
 ["10 %.","1 %.","50 %."],0,"25 %.",
 "El tiempo es el factor clave en una <mark>parada cardiaca</mark>.",
 "Si la RCP empieza en los <mark>primeros 4 minutos</mark>, la probabilidad de reanimación ronda el <mark>80 %</mark>, y baja un <mark>10 %</mark> por cada minuto más que se tarde.",
 "Por eso cualquier testigo debe empezar la RCP sin esperar a los servicios de emergencia.",
 "RCP: <mark>−10 % por minuto</mark> de retraso.","Manual de soporte vital básico")

q("Sanitario (SVB)","normal","Según el manual de SVB, para comprobar si la víctima respira con normalidad no se deben emplear más de:",
 ["10 segundos.","1 minuto.","30 segundos."],0,"3 segundos.",
 "Tras abrir la vía aérea hay que valorar la <mark>respiración</mark>.",
 "No se deben emplear <mark>más de 10 segundos</mark>. Si hay dudas sobre si respira con normalidad, se actúa como si no respirara.",
 "Las respiraciones agónicas no son una respiración normal.",
 "Valorar respiración: <mark>máximo 10 segundos</mark>.","Manual de soporte vital básico")

q("Síntomas clínicos","normal","Según el manual, el signo principal de la insuficiencia respiratoria es la hipoxemia, que se da cuando la saturación de oxígeno baja de:",
 ["90 %.","99 %.","50 %."],0,"70 %.",
 "La <mark>insuficiencia respiratoria</mark> es el fallo del aparato respiratorio para oxigenar la sangre.",
 "Su signo principal es la <mark>hipoxemia</mark>: <mark>SO₂ por debajo del 90 %</mark>. A veces se añade <mark>hipercapnia</mark>, que es el aumento del CO₂.",
 "Taquipnea con piel pálida o cianosis también son signos de alarma.",
 "Hipoxemia: <mark>SO₂ &lt;90 %</mark>.","Manual de síntomas y signos clínicos")

q("Síntomas clínicos","normal","Según el manual, en el síndrome de abstinencia alcohólica, el delirium tremens aparece a partir de las:",
 ["72 horas desde el último consumo.","2 horas desde el último consumo.","8 horas desde el último consumo."],0,"Dos semanas desde el último consumo.",
 "El <mark>síndrome de abstinencia alcohólica</mark> evoluciona por fases.",
 "La primera aparece a las <mark>8-12 horas</mark>, la segunda a las <mark>24 horas</mark> y el <mark>delirium tremens</mark>, a partir de las <mark>72 horas</mark>, con alucinaciones visuales muy vívidas.",
 "Se maneja como una agitación psicomotriz o un cuadro confusional.",
 "Delirium tremens: <mark>desde las 72 horas</mark>.","Manual de síntomas y signos clínicos")

open(P,'w',encoding='utf-8').write('[\n'+',\n'.join(json.dumps(x,ensure_ascii=False) for x in Q)+'\n]\n')
print('añadidas',nid-desde,'desde',desde,'total',len(Q),'difíciles nuevas',sum(1 for x in Q[desde-1:] if x['d']=='difícil'))
r=subprocess.run([sys.executable,'scripts/similares.py','--desde',str(desde)],capture_output=True,text=True)
print(r.stdout[-3000:])
