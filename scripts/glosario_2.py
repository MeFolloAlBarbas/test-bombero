# Glosario, tanda 2: el resto de temas. Definiciones a partir de las explicaciones ya comprobadas del banco.
import json, os
S = True
G = [
 # Gas y GLP
 ('Densidad relativa', ['densidad relativa'], 'Compara el peso de un gas con el del aire (aire = 1). Si es menor que 1, sube; si es mayor, se acumula abajo.', 'Gas y GLP', 'Manual de gas natural'),
 ('Tensión de vapor', ['tensión de vapor'], 'Equilibrio entre el líquido y el gas dentro de la bombona de GLP. Por eso no se llena del todo (máximo 85 %).', 'Gas y GLP', 'Manual de gas natural'),
 ('Válvula de seguridad', ['válvula de seguridad'], 'Válvula contra sobrepresiones en la parte superior de la bombona de GLP. Abre a 26 bar.', 'Gas y GLP', 'Manual de gas natural'),
 ('THT', ['THT','odorizante'], 'Odorizante que se añade al gas natural, que no huele, para poder detectar las fugas.', 'Gas y GLP', 'Manual de gas natural'),
 ('Llama higiénica', ['llama higiénica'], 'Llama azul, dura y estable, que no produce CO ni hollín. Una llama amarilla indica mala combustión.', 'Gas y GLP', 'Manual de gas natural'),
 ('Índice de Wobbe', ['Wobbe'], 'Relaciona el poder calorífico con la densidad del gas y agrupa los gases en familias. Gases de distinta familia no son intercambiables.', 'Gas y GLP', 'Manual de gas natural'),
 ('GLP', ['GLP'], 'Gases licuados del petróleo (propano y butano). Se guardan licuados: ocupan unas 240 veces menos que en gas.', 'Gas y GLP', 'Manual de gas natural'),
 ('Gas natural', ['gas natural'], 'Mezcla de hidrocarburos ligeros, sobre todo metano (≈80 %). No es tóxico, pero desplaza el oxígeno.', 'Gas y GLP', 'Manual de gas natural', S),
 ('GNL', ['GNL'], 'Gas natural licuado: se licúa a unos −160 °C.', 'Gas y GLP', 'Manual de gas natural'),
 ('Acometida de gas', ['acometida'], 'Tramo que une la red con el edificio. En Madrid hay de baja presión (sobre todo en la almendra central) y de media presión en el resto.', 'Gas y GLP', 'Manual de gas natural', S),
 # CTE DB-SI
 ('Recorrido de evacuación', ['recorrido de evacuación','recorridos de evacuación'], 'Distancia que hay que andar hasta una salida. Se limita porque el humo avanza más rápido que la gente.', 'CTE DB-SI', 'CTE DB-SI 3'),
 ('Sector de incendio', ['sector de incendio'], 'Zona cerrada con elementos resistentes al fuego para que el incendio no pase al resto del edificio durante un tiempo. En general, máximo 2.500 m².', 'CTE DB-SI', 'CTE DB-SI 1'),
 ('Altura de evacuación', ['altura de evacuación'], 'Diferencia de cota entre la planta más alejada y la de salida del edificio. De ella dependen muchas exigencias del DB-SI.', 'CTE DB-SI', 'CTE DB-SI, Anejo A'),
 ('Espacio de maniobra', ['espacio de maniobra'], 'Zona junto a la fachada para los vehículos de bomberos, sobre todo las autoescalas. Obligatorio con más de 9 m de altura de evacuación.', 'CTE DB-SI', 'CTE DB-SI 5'),
 ('Vial de aproximación', ['vial de aproximación','viales de aproximación','viales'], 'Camino que lleva a los vehículos de bomberos hasta el espacio de maniobra. Gálibo mínimo de 4,5 m.', 'CTE DB-SI', 'CTE DB-SI 5', S),
 ('Columna seca', ['columna seca'], 'Tubería vacía que los bomberos conectan desde la calle. En viviendas, obligatoria con más de 24 m de altura de evacuación.', 'CTE DB-SI', 'CTE DB-SI 4'),
 ('BIE', ['BIE'], 'Boca de incendio equipada: manguera fija conectada a una red de agua para la primera intervención. 45 mm en general; 25 mm en viviendas.', 'CTE DB-SI', 'CTE DB-SI 4'),
 ('Hidrante exterior', ['hidrante','hidrantes'], 'Toma de agua en la calle para abastecer a los vehículos de bomberos. Cuentan los que están a menos de 100 m de la fachada.', 'CTE DB-SI', 'CTE DB-SI 4', S),
 ('Extinción automática', ['extinción automática','rociadores'], 'Instalación que apaga el fuego sin intervención humana, como los rociadores.', 'CTE DB-SI', 'CTE DB-SI 4'),
 ('Escalera protegida', ['escalera protegida'], 'Recinto donde los ocupantes pueden permanecer un tiempo con seguridad. Se protege del humo con ventilación, conductos o presión diferencial.', 'CTE DB-SI', 'CTE DB-SI 3'),
 ('Interfaz urbano-forestal', ['interfaz urbano-forestal','zona forestal'], 'Zona donde los edificios lindan con terreno forestal, de especial riesgo de incendio. Exige una franja libre de 25 m.', 'CTE DB-SI', 'CTE DB-SI 5'),
 ('Hueco de acceso para bomberos', ['hueco de acceso','huecos'], 'Hueco en fachada que permite a los bomberos entrar en cada planta desde fuera. Mínimo 0,80 × 1,20 m.', 'CTE DB-SI', 'CTE DB-SI 5', S),
 # Tráfico (APRAT)
 ('Zona caliente', ['zona caliente'], 'Zona de acción alrededor del vehículo accidentado (en general, de 2 a 5 m). Solo entra personal con EPI y formación.', 'Tráfico (APRAT)', 'APRAT'),
 ('Condensador', ['condensador','condensadores'], 'Almacena carga y la retiene tras desconectar la fuente. Por eso un airbag puede dispararse con la batería desembornada.', 'Tráfico (APRAT)', 'APRAT I'),
 ('Airbag de dos etapas', ['dos etapas'], 'Airbag con dos disparos según la violencia del choque: que haya saltado no significa que esté desactivado.', 'Tráfico (APRAT)', 'APRAT I'),
 ('Pretensor', ['pretensor','pretensores'], 'Tensa el cinturón en un choque frontal. Los hay mecánicos (sensor mecánico, sin electricidad) y pirotécnicos.', 'Tráfico (APRAT)', 'APRAT I'),
 ('Niveles de atrapamiento', ['atrapamiento'], 'Clasificación del APRAT para decidir el rescate. Físico 1: no puede salir por sus lesiones, pero el vehículo no le atrapa. Físico 2: el vehículo le atrapa.', 'Tráfico (APRAT)', 'APRAT II', S),
 ('Vía de extracción', ['vía de extracción','salida de extracción'], 'Salida por la que se saca a la víctima. Se elige la que menos gira la columna: 0º por el portón; 25º por la puerta trasera del mismo lado.', 'Tráfico (APRAT)', 'APRAT II'),
 ('Estabilización', ['estabilización'], 'Evitar movimientos del vehículo que agraven las lesiones y crear un lugar de trabajo seguro. Sobre ruedas: cuñas a ambos lados de una o dos ruedas.', 'Tráfico (APRAT)', 'APRAT', S),
 ('Acceso sanitario', ['acceso sanitario'], 'Espacio que se crea como prioridad para que el sanitario llegue al herido y lo valore.', 'Tráfico (APRAT)', 'APRAT'),
 # Ascensores
 ('Paracaídas', ['paracaídas'], 'Frena la cabina clavando cuñas contra las guías cuando baja demasiado rápido. Para soltarlo, la cabina se mueve hacia arriba.', 'Ascensores', 'Manual de ascensores'),
 ('Foso', ['foso'], 'Parte del hueco por debajo de la última parada. Tiene mandos (seta de emergencia, finales de carrera, limitador) que pueden quedar con tensión.', 'Ascensores', 'Manual de ascensores'),
 ('Ascensor hidráulico', ['hidráulico','hidráulicos'], 'La cabina sube empujada por aceite a presión; para bajarla basta con dejar salir el aceite (botón o tirador rojo).', 'Ascensores', 'Manual de ascensores', S),
 ('Ascensor de emergencia', ['ascensor de emergencia'], 'Ascensor de uso prioritario para bomberos en un incendio. Carga mínima de 630 kg (bomberos con equipo o camilla).', 'Ascensores', 'Manual de ascensores · CTE DB-SI'),
 ('Faldón', ['faldón'], 'Chapa bajo la puerta de la cabina que tapa el hueco del foso cuando la cabina se para entre dos pisos. Mínimo 750 mm.', 'Ascensores', 'Manual de ascensores'),
 ('Ascensor sin cuarto de máquinas', ['sin cuarto de máquinas'], 'El protocolo añade un paso propio: mover la cabina con el sistema eléctrico de emergencia.', 'Ascensores', 'Manual de ascensores'),
 # Apícola
 ('Enjambrazón', ['enjambrazón'], 'División natural de la colonia: se va la reina vieja con parte de las abejas; en la colmena nacen reinas nuevas.', 'Apícola', 'Manual de rescate apícola'),
 ('Ahumador', ['humo'], 'El humo hace que las abejas llenen el buche de miel y les cueste picar. Es la herramienta clásica para trabajar sin ataques masivos.', 'Apícola', 'Manual de rescate apícola', S),
 ('Aspirado del enjambre', ['aspirado','aspirar'], 'Forma de retirar las abejas: se ahúma hacia una zona limpia y se aspira a la potencia mínima.', 'Apícola', 'Manual de rescate apícola', S),
 ('Lagarto ocelado', ['lagarto ocelado'], 'Reptil grande y verdoso con manchas azules (50-60 cm, hasta 90). Su peligro es el mordisco: cierra fuerte la mandíbula.', 'Apícola', 'Manual de rescate apícola'),
 ('Eslingas', ['eslingas'], 'Cintas para izar animales grandes, como caballos o vacas. Un animal grande no debe estar suspendido más de 15 minutos.', 'Apícola', 'Manual de rescate apícola'),
 # Atención sanitaria y SVB
 ('Pulsioxímetro', ['pulsioxímetro'], 'Mide la proporción de hemoglobina saturada de oxígeno. El convencional no distingue la carboxihemoglobina.', 'Atención sanitaria', 'Manual de Soporte Vital Básico'),
 ('Carboxihemoglobina', ['carboxihemoglobina'], 'Unión del CO con la hemoglobina (240 veces más afín que el oxígeno). Produce hipoxia; se trata con oxígeno al 100 %.', 'Atención sanitaria', 'Atención inicial al politraumatizado'),
 ('Relleno capilar', ['relleno capilar'], 'Se aprieta la uña y se suelta: indica si la sangre llega bien a la periferia. Normal, menos de 3 segundos.', 'Atención sanitaria', 'Atención inicial al politraumatizado'),
 ('Torniquete', ['torniquete'], 'Corta toda la circulación de una extremidad. Detiene la hemorragia, pero puede causar daños: solo para amputaciones o hemorragias que no paran con presión.', 'Atención sanitaria', 'Atención inicial al politraumatizado'),
 ('AVDN', ['AVDN'], 'Valoración rápida del nivel de conciencia: Alerta, responde a la Voz, al Dolor o No responde.', 'Atención sanitaria', 'Atención inicial al politraumatizado'),
 ('Escala de Glasgow', ['Glasgow'], 'Valora el nivel de conciencia sumando respuesta ocular, verbal y motora: de 3 a 15. TCE leve 14-15 · moderado 9-13 · grave menos de 9.', 'Atención sanitaria', 'Atención inicial al politraumatizado'),
 ('Collarín cervical', ['collarín'], 'Protege el cuello ante sospecha de traumatismo. Se pone entre dos personas, en posición neutra y sin traccionar. No limita los movimientos laterales: no se suelta la cabeza.', 'Atención sanitaria', 'Atención inicial al politraumatizado'),
 ('SIEVE', ['SIEVE'], 'Triaje del Reino Unido con esquema C-ABC: camina · vía aérea · respiración · circulación. No valora el estado mental.', 'Atención sanitaria', 'Patologías e IMV'),
 ('DEA', ['DEA'], 'Desfibrilador externo automático: analiza el ritmo y, si es desfibrilable, da una descarga. En niños, con atenuador o modo pediátrico.', 'Sanitario (SVB)', 'Manual de Soporte Vital Básico'),
 ('Cadena de supervivencia', ['cadena de supervivencia'], 'Eslabones que salvan vidas en una parada; uno de ellos es la desfibrilación precoz.', 'Sanitario (SVB)', 'Manual de Soporte Vital Básico'),
 ('Obstrucción de la vía aérea', ['obstrucción'], 'Incompleta: pasa aire, se anima a toser. Completa: 5 golpes en la espalda y 5 compresiones abdominales.', 'Sanitario (SVB)', 'Manual de Soporte Vital Básico', S),
 ('RCP', ['RCP','compresiones'], 'Reanimación cardiopulmonar. Compresiones de 5-6 cm a 110-120 por minuto. En niños se empieza con 5 ventilaciones.', 'Sanitario (SVB)', 'Manual de Soporte Vital Básico', S),
 ('Síndrome coronario agudo', ['síndrome coronario','ángor','infarto'], 'Ángor: la arteria coronaria se estrecha. Infarto (IAM): se obstruye del todo.', 'Patología cardiovascular', 'Manual de patologías'),
 ('Crisis hipertensiva', ['crisis hipertensiva'], 'Subida brusca de la tensión. Es emergencia si daña órganos diana (cerebro, corazón, riñones).', 'Patología cardiovascular', 'Manual de patologías'),
 ('Insuficiencia respiratoria', ['insuficiencia respiratoria'], 'Fallo del aparato respiratorio para oxigenar la sangre: saturación por debajo del 90 %.', 'Síntomas clínicos', 'Manual de patologías'),
 # Corte y soldadura
 ('Oxicorte', ['oxicorte'], 'Corta el metal calentándolo al rojo cereza y quemándolo después con un chorro de oxígeno puro.', 'Corte y soldadura', 'Manual de corte térmico'),
 ('Chemtane', ['Chemtane'], 'Combustible del oxicorte que sustituye al acetileno: 99 % propano, unos 3.300 °C. Válvula y manguera rojas.', 'Corte y soldadura', 'Manual de corte térmico'),
 ('Regulador', ['regulador'], 'Baja la presión de la botella a la de trabajo. Oxígeno 2-5 bar; Chemtane 0,5 bar.', 'Corte y soldadura', 'Manual de corte térmico', S),
 ('Lanza térmica', ['lanza térmica'], 'Herramienta de corte que alcanza 4.000-5.000 °C en la punta y funciona incluso sumergida.', 'Corte y soldadura', 'Manual de corte térmico'),
 # ACS y agua fría
 ('Aparatos de gas tipo A, B y C', ['tipo A','tipo B','tipo C'], 'A: vierte el humo al local. B: coge aire del local y saca el humo por un conducto. C: estanco, aire de fuera y humo fuera.', 'ACS', 'Manual de ACS', S),
 ('Legionela', ['legionela'], 'Bacteria que se multiplica en el agua tibia estancada y puede causar neumonías graves. Se elimina a 70 °C.', 'ACS', 'Manual de ACS'),
 ('Acometida de agua', ['acometida'], 'Une la red pública con la instalación del edificio. Normalmente una; los edificios especiales pueden tener dos en anillo; la de incendios, siempre independiente.', 'Agua fría', 'Manual de agua fría', S),
 ('Arteria', ['arteria','arterias'], 'Tubería de la red de transporte de agua. En ella no se ponen acometidas ni hidrantes.', 'Agua fría', 'Manual de agua fría', S),
 ('Red de distribución', ['red de distribución'], 'Tiene tres subredes: transporte (arterias), distribución principal y secundaria (ramales). Es propiedad del Canal de Isabel II.', 'Agua fría', 'Manual de agua fría'),
 # Vehículos, accesos, EPI
 ('Nomenclatura de bombas', ['FPN'], 'Indica presión y caudal: FPN 10/3500 es una bomba de baja presión que a 10 bar da 3.500 l/min.', 'Vehículos', 'Información básica de vehículos'),
 ('Cabrestante', ['cabrestante'], 'Torno para arrastrar o sujetar cargas.', 'Vehículos', 'Información básica de vehículos'),
 ('Autoescala', ['autoescala','autoescalas'], 'Vehículo con escalera extensible. El Servicio tiene convencionales y articuladas.', 'Vehículos', 'Información básica de vehículos'),
 ('Resbalón', ['resbalón'], 'Pieza que cierra la puerta al tirar de ella sin echar la llave. Su cara inclinada mira hacia el cerradero.', 'Accesos forzados', 'Manual de accesos forzados'),
 ('Picaporte con condena', ['condena'], 'Cerradura sencilla que se bloquea desde dentro, típica del baño.', 'Accesos forzados', 'Manual de accesos forzados'),
 ('Puerta blindada', ['blindada'], 'Más resistente que la estándar, menos que la acorazada. Las puertas se ordenan: estándar, blindada, acorazada.', 'Accesos forzados', 'Manual de accesos forzados'),
 ('Puerta acorazada', ['acorazada'], 'La más resistente: bisagras robustas y varios cierres antipalanca.', 'Accesos forzados', 'Manual de accesos forzados'),
 ('Autonomía del ERA', ['aire disponible'], 'Aire disponible = (presión inicial − presión final) × volumen de la botella; dividido por el consumo da los minutos.', 'EPI', 'Manual de EPI'),
 ('Alarma de baja presión', ['alarma'], 'Aviso acústico del manorreductor del ERA: suena a 55 bar y sigue hasta quedar 10 bar.', 'EPI', 'Manual de EPI', S),
 # EBEP
 ('Prescripción', ['prescripción','prescriben'], 'Plazo tras el cual ya no se puede sancionar una falta si la Administración no ha actuado. Faltas graves: 2 años.', 'EBEP', 'TREBEP, art. 97', S),
 ('Funcionario interino', ['interino','interinos'], 'Nombrado temporalmente, por necesidad y urgencia, para funciones de funcionario de carrera (vacante: máximo 3 años).', 'EBEP', 'TREBEP, art. 10'),
 ('Situaciones administrativas', ['situaciones administrativas'], 'Posición en que se encuentra un funcionario respecto a su puesto: servicio activo, excedencia, suspensión…', 'EBEP', 'TREBEP, art. 85'),
 ('Excedencia', ['excedencia'], 'Situación en la que el funcionario deja de prestar servicio durante un tiempo.', 'EBEP', 'TREBEP, art. 89'),
 ('Suspensión firme', ['suspensión firme'], 'Sanción que aparta al funcionario de sus funciones (máximo 6 años).', 'EBEP', 'TREBEP, art. 90'),
 ('Separación del servicio', ['separación del servicio'], 'Sanción más grave: pérdida de la condición de funcionario. Solo por falta muy grave.', 'EBEP', 'TREBEP, art. 96'),
 ('Grupos de clasificación', ['grupo','grupos'], 'Los cuerpos se clasifican en grupos según la titulación exigida para entrar.', 'EBEP', 'TREBEP, art. 76', S),
 # Régimen local
 ('Junta de Gobierno Local', ['Junta de Gobierno Local','Junta de Gobierno'], 'Órgano que ayuda al Alcalde a dirigir el ayuntamiento. Obligatoria con más de 5.000 habitantes; como máximo, un tercio de los concejales.', 'Régimen local', 'Ley 7/1985, arts. 20 y 23'),
 ('Servicios mínimos obligatorios', ['servicios mínimos'], 'Servicios que cada municipio debe prestar según su población (art. 26). Extinción de incendios, desde 20.000; transporte urbano, desde 50.000.', 'Régimen local', 'Ley 7/1985, art. 26'),
 ('Distrito', ['Distrito','Distritos'], 'División territorial con órganos de gestión desconcentrada. En Madrid lo preside siempre un Concejal.', 'Régimen local', 'Ley 22/2006', S),
 ('Moción de censura', ['moción de censura'], 'Permite al Pleno destituir al Alcalde. Votación pública y por llamamiento nominal.', 'Régimen local', 'Ley 7/1985'),
 ('Bando', ['bando','bandos'], 'Aviso o mandato del Alcalde dirigido a los vecinos.', 'Régimen local', 'Ley 7/1985, art. 21'),
 ('Voto de calidad', ['voto de calidad'], 'Voto que sirve para desempatar. Lo tiene el Alcalde.', 'Régimen local', 'Ley 7/1985'),
 ('Competencias propias', ['competencias propias','competencia propia'], 'Las que el municipio ejerce en su propio nombre, como la prevención y extinción de incendios.', 'Régimen local', 'Ley 7/1985, art. 25'),
 ('Padrón', ['padrón'], 'Registro de los vecinos del municipio. No prueba la residencia legal de un extranjero.', 'Régimen local', 'Ley 7/1985, art. 16'),
 # Constitución y Estatuto
 ('Inviolabilidad del domicilio', ['inviolabilidad del domicilio','domicilio'], 'Derecho fundamental (art. 18): no se entra sin consentimiento, resolución judicial o en caso de flagrante delito.', 'Constitución', 'CE, art. 18', S),
 ('Detención preventiva', ['detención preventiva'], 'Sirve para hacer las averiguaciones necesarias; máximo 72 horas antes de pasar al juez.', 'Constitución', 'CE, art. 17'),
 ('Tutela judicial efectiva', ['tutela judicial efectiva'], 'Derecho a acudir a los tribunales y obtener una respuesta fundada, sin indefensión.', 'Constitución', 'CE, art. 24'),
 ('Irretroactividad', ['irretroactividad'], 'Una norma no se aplica a hechos anteriores a su entrada en vigor. Garantizada para las sancionadoras desfavorables.', 'Constitución', 'CE, art. 9.3'),
 ('Valores superiores', ['valores superiores'], 'Libertad, justicia, igualdad y pluralismo político (art. 1.1).', 'Constitución', 'CE, art. 1'),
 ('Autonomía municipal', ['autonomía de los municipios','autonomía municipal'], 'Los municipios gozan de personalidad jurídica plena; su gobierno corresponde a alcaldes y concejales.', 'Constitución', 'CE, art. 140'),
 ('Instituciones de autogobierno', ['instituciones de autogobierno'], 'De la Comunidad de Madrid: la Asamblea, el Gobierno y el Presidente.', 'Estatuto CAM', 'Estatuto de Autonomía de la CAM'),
 # Reglamento de Bomberos
 ('Unidad de mando', ['unidad de mando'], 'Todo servicio con dos o más miembros se hace bajo el mando de una sola persona.', 'Reglamento Bomberos', 'Reglamento del Cuerpo de Bomberos'),
 ('Mandos naturales', ['mandos naturales'], 'Los únicos que dan órdenes en el Cuerpo: sus mandos internos, por jerarquía y especialización.', 'Reglamento Bomberos', 'Reglamento del Cuerpo de Bomberos'),
 ('Servicio de Apoyo Técnico', ['Servicio de Apoyo Técnico'], 'Personal con incapacidad física parcial para la atención directa (por edad, enfermedad o accidente). Pase por edad: bombero 55; conductor y mando 60.', 'Reglamento Bomberos', 'Reglamento del Cuerpo de Bomberos'),
 ('Promoción interna', ['promoción interna'], 'En la Escala Ejecutiva: concurso-oposición y curso selectivo. A Cabo, 6 años; a Sargento, 10 (o 4 desde Cabo).', 'Reglamento Bomberos', 'Reglamento del Cuerpo de Bomberos'),
 # PRL
 ('Delegados de Prevención', ['Delegados de Prevención','Delegado de Prevención'], 'Representantes de los trabajadores en seguridad y salud. De 101 a 500 trabajadores, 3.', 'PRL', 'Ley 31/1995, art. 35'),
 ('Comité de Seguridad y Salud', ['Comité de Seguridad y Salud'], 'Órgano paritario de consulta en empresas de 50 o más trabajadores. Se reúne cada trimestre.', 'PRL', 'Ley 31/1995, art. 38'),
 ('Vigilancia de la salud', ['vigilancia de la salud'], 'Reconocimientos médicos según los riesgos del puesto. Requiere consentimiento, salvo excepciones.', 'PRL', 'Ley 31/1995, art. 22'),
 ('Riesgo grave e inminente', ['riesgo grave e inminente','peligro grave e inminente'], 'El trabajador puede interrumpir su actividad y no se le exige volver mientras dure.', 'PRL', 'Ley 31/1995, art. 21'),
 ('Principios de la acción preventiva', ['acción preventiva'], 'Nueve principios del art. 15. El primero: evitar los riesgos.', 'PRL', 'Ley 31/1995, art. 15'),
 # Igualdad
 ('Acoso sexual', ['acoso sexual'], 'Comportamiento de naturaleza sexual que atenta contra la dignidad. Siempre es discriminatorio.', 'Igualdad', 'LO 3/2007, art. 7'),
 ('Acoso por razón de sexo', ['acoso por razón de sexo'], 'Comportamiento motivado por el sexo de la persona que atenta contra su dignidad. Siempre es discriminatorio.', 'Igualdad', 'LO 3/2007, art. 7'),
 ('Discriminación directa', ['discriminación directa'], 'Trato menos favorable por razón de sexo. Lo es todo trato desfavorable por embarazo o maternidad.', 'Igualdad', 'LO 3/2007, arts. 6 y 8'),
 ('Discriminación indirecta', ['discriminación indirecta'], 'Una norma o práctica aparentemente neutra que perjudica a las personas de un sexo.', 'Igualdad', 'LO 3/2007, art. 6'),
 ('Acciones positivas', ['acciones positivas'], 'Medidas específicas para corregir desigualdades de hecho, mientras duren y si son razonables y proporcionadas.', 'Igualdad', 'LO 3/2007, art. 11'),
 ('Indemnidad frente a represalias', ['indemnidad'], 'Trato adverso por reclamar la igualdad: es discriminación por razón de sexo.', 'Igualdad', 'LO 3/2007, art. 9'),
 ('Discriminación por error', ['discriminación por error'], 'Ley 4/2023: la que se basa en una apreciación equivocada de las características de la persona.', 'Igualdad', 'Ley 4/2023, art. 3'),
 # Haciendas locales
 ('Tasa', ['tasa'], 'Se paga por un servicio concreto que se te presta a ti. Algunos servicios, como la protección civil, nunca pueden cobrarse con tasa.', 'Haciendas locales', 'TRLRHL, arts. 20-21', S),
 ('Contribución especial', ['contribución especial','contribuciones especiales'], 'La pagan quienes se benefician especialmente de una obra o de la ampliación de un servicio. Solo se destina a esa obra.', 'Haciendas locales', 'TRLRHL, art. 28'),
 ('Precio público', ['precio público','precios públicos'], 'Se cobra por servicios que no son obligatorios para el ciudadano. Debe cubrir al menos el coste.', 'Haciendas locales', 'TRLRHL, art. 41'),
 ('Sustituto del contribuyente', ['sustituto del contribuyente','sustituta del contribuyente'], 'Quien paga en lugar del contribuyente. En la tasa de extinción de incendios, la aseguradora.', 'Haciendas locales', 'TRLRHL, art. 23'),
 ('Impuestos potestativos', ['potestativo','potestativos'], 'Los que el ayuntamiento «podrá establecer»: el ICIO y la plusvalía (IIVTNU). Obligatorios: IBI, IAE e IVTM.', 'Haciendas locales', 'TRLRHL, art. 59'),
]
out = []
for e in G:
    t, a, d, tema, f = e[:5]
    x = {'t': t, 'a': a, 'd': d, 'tema': tema, 'f': f}
    if len(e) > 5 and e[5]: x['solo'] = 1
    out.append(x)
p = os.path.join(os.path.dirname(__file__), '..', 'glosario.json')
old = [g for g in json.load(open(p, encoding='utf-8')) if g['t'] not in {o['t'] for o in out}]
json.dump(old + out, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(old + out), 'términos')
