# Glosario, tanda 1: NRBQ, Trabajos en altura, Electricidad, Protección civil, Procedimiento administrativo.
# Definiciones sacadas de las explicaciones ya comprobadas del banco (y de los manuales del proyecto).
# t = término, a = formas que se buscan en el texto, d = definición corta, tema, f = fuente, solo = buscar solo en preguntas de su tema
import json, os
G = [
 # NRBQ
 ('Rango de inflamabilidad', ['rango de inflamabilidad','rango inflamable'], 'Concentraciones de gas o vapor en aire, entre el LII y el LSI, en las que la mezcla puede arder.', 'NRBQ', 'Manual NRBQ'),
 ('LII', ['LII','límite inferior de inflamabilidad'], 'Límite inferior de inflamabilidad: concentración mínima de vapor en el aire para que pueda arder. Por debajo, la mezcla es pobre.', 'NRBQ', 'Manual NRBQ'),
 ('LSI', ['LSI','límite superior de inflamabilidad'], 'Límite superior de inflamabilidad: concentración máxima. Por encima no hay aire suficiente para arder (mezcla rica).', 'NRBQ', 'Manual NRBQ'),
 ('Mezcla rica', ['mezcla rica'], 'Mezcla por encima del LSI. No arde mientras siga así, pero si entra aire atraviesa el rango inflamable.', 'NRBQ', 'Manual NRBQ'),
 ('Panel naranja', ['panel naranja'], 'Placa de 40 × 30 cm que indica que un vehículo transporta mercancías peligrosas: arriba, el número de peligro; abajo, el número ONU.', 'NRBQ', 'Manual NRBQ'),
 ('Número de peligro', ['número de peligro','código Kemler'], 'Cifras de la parte superior del panel naranja (código Kemler). La X indica que reacciona peligrosamente con el agua y una cifra repetida, que el peligro se intensifica.', 'NRBQ', 'Manual NRBQ'),
 ('Número ONU', ['número ONU'], 'Número de la parte inferior del panel naranja que identifica la materia transportada.', 'NRBQ', 'Manual NRBQ'),
 ('DL50', ['DL50','dosis letal 50'], 'Dosis que causa la muerte del 50 % de una población animal de prueba. Cuanto más baja, más tóxica es la sustancia.', 'NRBQ', 'Manual NRBQ'),
 ('TLV', ['TLV'], 'Valores límite de exposición a sustancias en el trabajo.', 'NRBQ', 'Manual NRBQ'),
 ('TLV/STEL', ['STEL'], 'Límite de exposición para periodos cortos, de no más de 15 minutos.', 'NRBQ', 'Manual NRBQ'),
 ('TLV/TWA', ['TWA'], 'Límite de exposición como media ponderada de una jornada laboral.', 'NRBQ', 'Manual NRBQ'),
 ('IPVS (IDLH)', ['IPVS','IDLH'], 'Concentración de peligro inmediato para la vida o la salud.', 'NRBQ', 'Manual NRBQ'),
 ('Explosímetro', ['explosímetro'], 'Aparato que mide la concentración de gases y vapores inflamables. Detecta su presencia, pero no distingue unas sustancias de otras.', 'NRBQ', 'Manual NRBQ'),
 ('Factor de corrección', ['factor de corrección'], 'Número por el que se multiplica la lectura del explosímetro cuando se mide un gas distinto del de calibración (normalmente metano).', 'NRBQ', 'Manual NRBQ'),
 ('Tubo colorimétrico', ['tubo colorimétrico','tubos colorimétricos'], 'Vial con un reactivo que cambia de color con la sustancia; la longitud de la mancha indica la concentración. Se lee inmediatamente.', 'NRBQ', 'Manual NRBQ'),
 ('Ojiva', ['ojiva'], 'Parte superior de la botella de gas. Según la norma actual, su color identifica el riesgo principal del gas.', 'NRBQ', 'Manual NRBQ'),
 ('Rombo NFPA 704', ['NFPA'], '«Diamante de peligro» de EE. UU.: azul, salud; rojo, inflamabilidad; amarillo, reactividad; blanco, riesgos especiales. Cada uno, de 0 a 4.', 'NRBQ', 'Manual NRBQ'),
 ('Código Hazchem', ['Hazchem'], 'Código de mercancías peligrosas de Reino Unido, Australia y Nueva Zelanda. Empieza por el código de acción de emergencia.', 'NRBQ', 'Manual NRBQ'),
 ('Reglamento CLP', ['CLP'], 'Reglamento CE 1272/2008 de clasificación, etiquetado y envasado: pictogramas en rombo con borde rojo.', 'NRBQ', 'Manual NRBQ'),
 # Trabajos en altura
 ('Factor de caída', ['factor de caída'], 'Distancia de caída ÷ longitud de cuerda activa. No tiene unidades. En ascenso por cuerda se parte de un factor 2 teórico.', 'Trabajos en altura', 'Manual ANETVA'),
 ('Fuerza de choque', ['fuerza de choque'], 'Golpe que recibe el cuerpo cuando el sistema detiene la caída. El sistema debe absorber la mayor energía posible.', 'Trabajos en altura', 'Manual ANETVA'),
 ('Absorbedor de energía', ['absorbedor'], 'Elemento que se rasga o estira para «gastar» energía de la caída. Limita la fuerza de choque a 6 kN con 100 kg (UNE-EN 355).', 'Trabajos en altura', 'Manual de trabajos en altura'),
 ('Punto de anclaje', ['punto de anclaje','anclaje'], 'Punto fijo del que cuelga todo el sistema. Debe garantizar al menos 12 kN (UNE-EN 795).', 'Trabajos en altura', 'Manual de trabajos en altura'),
 ('Conector', ['conector'], 'Pieza que une los elementos del sistema (arnés, cuerda, anclaje…). Más de 15 kN en su eje mayor (EN 362).', 'Trabajos en altura', 'Manual de trabajos en altura'),
 ('Bloqueador', ['bloqueador','puño'], 'Aparato que se desliza por la cuerda en un sentido y se bloquea en el otro al cargar peso. Sirve para progresar, no para detener caídas.', 'Trabajos en altura', 'Manual de trabajos en altura'),
 ('Cuerda semiestática', ['cuerda semiestática','cuerdas semiestáticas'], 'Cuerda que estira poco (UNE-EN 1891). Clase A: 22 kN; clase B: 18 kN.', 'Trabajos en altura', 'Manual de trabajos en altura'),
 ('Cuerda de seguridad', ['cuerda de seguridad'], 'La que hace de anticaídas. Va con anclaje independiente de la de trabajo y es de otro color.', 'Trabajos en altura', 'Manual de trabajos en altura'),
 ('Cuerda de trabajo', ['cuerda de trabajo'], 'La que se usa para acceder al punto de trabajo y apoyarse.', 'Trabajos en altura', 'Manual de trabajos en altura'),
 ('Síndrome del arnés', ['síndrome del arnés','trauma por suspensión'], 'Daño por estar mucho tiempo colgado del arnés. En suspensiones largas es imprescindible el asiento de trabajo.', 'Trabajos en altura', 'NTP de trabajos verticales'),
 ('Protocolo P.A.S.', ['P.A.S.'], 'Principios ante cualquier accidente, en este orden: Proteger, Alertar y Socorrer.', 'Trabajos en altura', 'Manual de trabajos en altura'),
 # Electricidad
 ('Interruptor diferencial', ['diferencial'], 'Corta la corriente al detectar diferencia entre la que entra y la que sale (una fuga). En viviendas, 30 mA.', 'Electricidad', 'Manual de instalaciones eléctricas'),
 ('Tetanización', ['tetanización'], 'Contracción muscular por el paso de la corriente que impide soltar el conductor.', 'Electricidad', 'Conceptos básicos de electricidad'),
 ('Baja tensión', ['baja tensión'], 'Hasta 1.000 V en alterna y 1.500 V en continua.', 'Electricidad', 'Manual de instalaciones eléctricas'),
 ('MBTS', ['MBTS','muy baja tensión de seguridad'], 'Muy baja tensión de seguridad: tan baja que no se considera peligrosa. En piscinas, 12 V.', 'Electricidad', 'Manual de instalaciones eléctricas'),
 ('Corriente trifásica', ['trifásica'], 'Tres corrientes alternas de la misma frecuencia y valor eficaz, desfasadas 120°.', 'Electricidad', 'Manual de instalaciones eléctricas'),
 ('Centro de transformación', ['centro de transformación','centros de transformación'], 'Última etapa antes del usuario: recibe normalmente 20 kV y entrega baja tensión de 400/230 V.', 'Electricidad', 'Manual de instalaciones eléctricas'),
 ('Red de transporte eléctrico', ['red de transporte'], 'Lleva la electricidad a muy alta tensión (220 a 400 kV) para perder menos energía.', 'Electricidad', 'Manual de instalaciones eléctricas', True),
 # Protección civil
 ('Peligro', ['peligro'], 'Ley 17/2015: potencial de ocasionar daño.', 'Protección civil', 'Ley 17/2015, art. 2', True),
 ('Amenaza', ['amenaza'], 'Ley 17/2015: situación en la que personas y bienes están expuestos a un peligro inminente o latente.', 'Protección civil', 'Ley 17/2015, art. 2', True),
 ('Vulnerabilidad', ['vulnerabilidad'], 'Ley 17/2015: lo susceptible que es una colectividad de ser afectada por un peligro.', 'Protección civil', 'Ley 17/2015, art. 2', True),
 ('Riesgo', ['riesgo'], 'Ley 17/2015: posibilidad de que una amenaza llegue a afectar a personas o bienes.', 'Protección civil', 'Ley 17/2015, art. 2', True),
 ('Catástrofe', ['catástrofe'], 'Nivel más grave: situación que supera los medios de la propia comunidad.', 'Protección civil', 'Ley 17/2015, art. 2', True),
 ('Emergencia de protección civil', ['emergencia de protección civil','emergencia ordinaria'], 'Situación de riesgo colectivo que exige una gestión rápida de los poderes públicos. La ordinaria no tiene afectación colectiva.', 'Protección civil', 'Ley 17/2015, art. 2'),
 ('Deber de colaboración', ['deber de colaboración'], 'Obligación de colaborar personal o materialmente cuando lo pide la autoridad. Solo se indemnizan los daños en los bienes.', 'Protección civil', 'Ley 17/2015, art. 7 bis'),
 ('Estrategia del Sistema Nacional', ['Estrategia'], 'Analiza los riesgos futuros y fija líneas de acción. Se revisa al menos cada 4 años.', 'Protección civil', 'Ley 17/2015', True),
 # Procedimiento administrativo
 ('Silencio administrativo', ['silencio administrativo','silencio'], 'Lo que se entiende que ha decidido la Administración cuando no contesta en plazo. Puede ser estimatorio o desestimatorio.', 'Procedimiento administrativo', 'Ley 39/2015, art. 24', True),
 ('Certificado de silencio', ['certificado de silencio'], 'Acredita que se ha producido el silencio. Se expide de oficio en 15 días desde que vence el plazo para resolver.', 'Procedimiento administrativo', 'Ley 39/2015, art. 24.4'),
 ('Trámite de audiencia', ['trámite de audiencia'], 'Antes de la propuesta de resolución, la Administración enseña el expediente al interesado para que alegue. Entre 10 y 15 días.', 'Procedimiento administrativo', 'Ley 39/2015, art. 82'),
 ('Medidas provisionales', ['medidas provisionales','medida provisional'], 'Aseguran que la resolución final pueda cumplirse. Si se toman antes de abrir el procedimiento, hay que iniciarlo en 15 días.', 'Procedimiento administrativo', 'Ley 39/2015, art. 56'),
 ('Caducidad', ['caducidad'], 'Terminación del procedimiento cuando se paraliza por culpa del interesado.', 'Procedimiento administrativo', 'Ley 39/2015, art. 95'),
 ('Capacidad de obrar', ['capacidad de obrar'], 'Aptitud para actuar por uno mismo ante la Administración. Los menores la tienen donde la ley no exige a sus padres o tutores.', 'Procedimiento administrativo', 'Ley 39/2015, art. 3'),
 ('Informe', ['informe','informes'], 'Opinión técnica o jurídica de un órgano. Por defecto, facultativo y no vinculante; plazo general de 10 días.', 'Procedimiento administrativo', 'Ley 39/2015, art. 80', True),
 ('Información pública', ['información pública'], 'Trámite para que cualquier persona examine el expediente. Mínimo 20 días.', 'Procedimiento administrativo', 'Ley 39/2015, art. 83'),
 ('Período de prueba', ['período de prueba'], 'Se abre cuando la Administración no da por ciertos los hechos alegados. Entre 10 y 30 días.', 'Procedimiento administrativo', 'Ley 39/2015, art. 77'),
 ('Ejecución subsidiaria', ['ejecución subsidiaria'], 'La Administración hace lo que el obligado no hace, a costa de este. Solo si otro puede hacerlo.', 'Procedimiento administrativo', 'Ley 39/2015, art. 102'),
 ('Multa coercitiva', ['multa coercitiva'], 'Medio de ejecución forzosa para obligar a cumplir. No es una sanción y es compatible con ellas.', 'Procedimiento administrativo', 'Ley 39/2015, art. 103'),
 ('Compulsión directa', ['compulsión'], 'Medio de ejecución más intenso: actúa sobre la propia persona. Solo para obligaciones de no hacer o soportar, si la ley lo autoriza.', 'Procedimiento administrativo', 'Ley 39/2015, art. 104'),
]
out = []
for e in G:
    t, a, d, tema, f = e[:5]
    x = {'t': t, 'a': a, 'd': d, 'tema': tema, 'f': f}
    if len(e) > 5 and e[5]: x['solo'] = 1
    out.append(x)
p = os.path.join(os.path.dirname(__file__), '..', 'glosario.json')
old = []
if os.path.exists(p):
    old = [g for g in json.load(open(p, encoding='utf-8')) if g['t'] not in {o['t'] for o in out}]
json.dump(old + out, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(old + out), 'términos')
