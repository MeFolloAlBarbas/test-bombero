# Tandas nocturnas de preguntas: criterios y método

Este fichero es la referencia para las tareas programadas que generan preguntas cada noche
(y para cualquier conversación que haga una tanda). Copia de los criterios de las notas del
proyecto (`claude/entrenamiento-tests.md`); si hay contradicción, mandan las notas del proyecto.

## Regla de oro (usuario, 25/11/2026)
- **Una pregunta que ya le ha salido a alguien no vuelve a salir nunca.** No se borra (se guarda para un futuro
  apartado de repaso de pasadas), pero el calendario no la vuelve a usar. Tampoco se cambia nunca un día de hoy o
  anterior en plan.json. `scripts/sin_repetir.py` lo comprueba al ampliar el calendario.

## Aprobación automática (desde el 27/11/2026, el usuario ya no da visto bueno a cada lote)
- «Me han gustado las preguntas que has ido haciendo»: las preguntas entran solas en la web cada noche.
- **Excepción: marca con `"revisar": "<motivo>"` cualquier pregunta rara o distinta en su forma de redacción**
  (formato nuevo, enunciado poco habitual, duda sobre si se entiende, dato discutible o contradictorio) y las de
  Edificaciones I-III / Técnicas de estabilización donde el manual y la realidad no coinciden, y **SIEMPRE las
  preguntas basadas en una errata del temario** (y su ficha para laboratorio.json): el usuario quiere verlas antes. Esas NO entran: se
  apartan en `tandas/revisar/AAAA-MM-DD.json` y se ven con el usuario una a una. Ante la duda, marcarla.
- La tarea 5, al terminar, ejecuta `python3 scripts/aprobar.py <hoy> --separar-revisar`, luego `scripts/version.sh`,
  commit y push, y avisa al usuario: cuántas han entrado y cuáles quedan para revisar juntos (con su motivo).
- Si la aprobación falla (reglas.py con errores o sin_repetir.py), no se sube nada a la web: queda pendiente y se avisa.
- Las revisadas que el usuario acepte: `python3 scripts/aceptar_revisadas.py AAAA-MM-DD --ok id1,id2 [--quitar id3]`.
- `esperando_visto_bueno` solo queda puesto si la aprobación automática falló; entonces la noche siguiente no genera.

## Temario oficial
- **Los manuales están en el repo, cifrados**, en `temario/` (nombres según las bases). Al empezar:
  `TEMARIO_CLAVE='<clave de las instrucciones de la tarea>' sh scripts/temario.sh texto /tmp/temario` y trabaja
  con esos .txt (grep para buscar datos, leer solo las páginas necesarias; marcas «=== Página N del PDF ===»).
  Es más barato que project_read. Si falta la clave o falla, usa el proyecto como antes. NUNCA subas al repo
  nada descifrado ni copies texto de los manuales en ficheros sin cifrar (el repo es público).
- `tandas/TEMARIO_BASES.md`: títulos y contenido exacto de cada tema según las bases, y qué archivo corresponde a cada uno. **Solo se pregunta lo que entra en el tema** (p. ej. en leyes, solo los artículos indicados).

## Mapa de cobertura (saber con seguridad qué está preguntado y qué falta)
- **Cada pregunta nueva lleva `src`**: `{"m": "<nombre exacto del manual en temario/, sin .txt.enc>", "p": [páginas del PDF]}`
  (las páginas son las marcas «=== Página N del PDF ===»). reglas.py da error si falta.
- `python3 scripts/mapa.py /tmp/temario` (con el temario descifrado) genera `tandas/mapa_preguntas.json` (id → manual,
  página, confianza) y `tandas/mapa_paginas.json` (por manual: páginas con preguntas y **páginas sin preguntas**).
  Las preguntas antiguas sin `src` se localizan buscando su dato en el manual (confianza alta/media/baja).
- **Qué cuenta como «ya preguntado»: SOLO el dato que es el objeto de una pregunta** (lo que se pregunta y su respuesta
  correcta, resumido en `tq` → `ta`). Lo que aparece en la explicación, en los distractores o en el contexto NO cuenta.
  Ejemplo (pregunta 75, art. 140 CE, alcaldes elegidos por concejales o vecinos): siguen libres el concejo abierto o la
  personalidad jurídica plena de los municipios, aunque salgan en su explicación.
- Por eso una página «con preguntas» **no está terminada**: casi siempre le quedan datos. Orden de trabajo: primero las
  páginas de `sin_preguntas`; después, las páginas con preguntas, leyendo sus `tq`/`ta` para saber qué dato está
  cogido y sacando pregunta de todos los demás datos de la página. Al terminar, volver a ejecutarlo
  y subir los dos mapas (solo contienen ids y números de página).

## Lo que pregunta el examen real (152 plazas, 2026: 90 + 5 de reserva; en temario/ como «Extra - Examen teórico…», cifrado)
Reparto aproximado de las 90 (para priorizar temas; nunca copiar sus preguntas):
- Bloque I: 17 (Constitución 2 · Régimen local 1 · Haciendas 3 · EBEP 4 · Ley 39/2015 2 · Igualdad, incl. Ley 4/2023, 3 · PRL 2).
- Teoría del fuego, incendios de interior/ventilación (VPP), hidráulica y meteorología: ~10 (manuales II.1-II.4 aún sin subir).
- **Edificaciones (II.11-13): 8** · APRAT: 7 · ANETVA/NTP trabajos verticales: 6 · Sanitario (SVB, politrauma, urgencias): 5 ·
  ACS/calefacción/climatización: 5 · CTE DB-SI: 4-5 · Electricidad + instalaciones eléctricas: 6 · Agua fría y saneamiento: 4 ·
  Gas: 3 · NRBQ: 3 · Arbolado (motosierra): 2 · Vehículos: 2 · EPI: 2 · Corte y soldadura: 2 · Incendios de vegetación: 2 ·
  Apícola + ascensores: 2 · Accesos forzados: 1 · Reglamento del Cuerpo: 1 · Protección civil: 1.
- Rasgos: enunciados que citan la ley y el artículo («Según el artículo 18 del RDL 5/2015…») pero preguntan el contenido, no el
  número; opciones casi idénticas que cambian una palabra o cifra; muchos **supuestos de intervención** con datos concretos
  (corte de suministro en un local, caldera que echa humo blanco, colector con atmósfera peligrosa, rescatado tras 35 s de
  electrización); **cálculos con tablas del CTE** (dotación de BIE, extintores, hospital, uso administrativo con m² y altura);
  lectura de tablas del manual (solubilidad NRBQ «tabla 9»); ordenación de pasos (Rautek); «señale la incorrecta / es falso que»;
  definiciones del glosario de la NTP o de la Ley 17/2015; designaciones normalizadas (GL 28 h, electrodos, UNE-EN 437, UNE-EN 1891).
- Consecuencia: dar prioridad a Edificaciones (hoy casi sin preguntas), instalaciones (ACS, agua, gas, electricidad), APRAT,
  trabajos verticales, sanitario y CTE con supuestos numéricos.

## Qué es un dato bueno (acordado con el usuario el 25/11/2026)
- **Cada dato concreto del manual es una pregunta**: cada definición, cada componente, cada cifra,
  cada rango, cada prohibición, cada «por qué», cada función. De una sola página salen 10 o más.
  El ejemplo de abajo (una página de ACS que propuso el usuario) es un **esqueleto de la idea, no una
  plantilla**: muestra el nivel de detalle y la variedad de enfoques (qué NO forma parte, rangos, dónde va,
  por qué, función de cada parte, permitido/prohibido, supuesto de intervención). No hay que copiar esas
  preguntas tal cual; cada tarea decide las suyas con ese espíritu y su propio criterio.
  Ejemplo, página de ACS (contadores, conducciones, depósito de expansión):
  - componentes del contador (medidor + indicador) → «¿cuál NO forma parte?» con uno inventado creíble;
  - contador de agua fría (< 30 °C) y de caliente (30-90 °C) → rangos;
  - todo contador lleva válvula de corte a la entrada; los de ACS, además, antirretorno → ¿cuál lleva
    antirretorno? / ¿cuáles llevan válvula de corte? / ¿dónde va la válvula de corte? (3 preguntas);
  - intervención: fuga sin apariencia → se detecta por el movimiento de la palomilla de la mariposa de registro;
  - depósito de expansión: sus dos zonas, la función de cada una, por qué la membrana es elástica e
    impermeable, gas = aire o nitrógeno (varias preguntas);
  - conducciones compatibles con el fluido (no alterar su composición ni reaccionar);
  - 50 °C trabajo normal / 70 °C tratamiento periódico (dos preguntas, cada una con su porqué);
  - galvanizado prohibido > 60 °C / qué materiales sí se permiten (dos preguntas);
  - cómo se comportan los termoplásticos con la temperatura;
  - presión en ACS (no en agua fría): mínimo 1 bar, máximo 5 bar.
- Un mismo párrafo puede dar varias preguntas siempre que cada una pregunte **algo distinto**.
- **Reglas mnemotécnicas** en «Para recordar» cuando haya una buena (al usuario le gustó «cuerdas A:
  la A es de Aguantan más»).
- Requisitos: está en un manual subido y se comprueba en su página; no se ha preguntado ya; tiene
  respuesta clara y distractores creíbles.
- No se rellena con relleno (introducciones, títulos de figuras, obviedades). Si de verdad no quedan
  datos, se para y se avisa (poner `parado`).

## Criterios de estilo
- Estilo del examen real de las 152 plazas (2026): 3 opciones, una correcta (+ `o4`, la 4.ª del Chulito).
- Respuestas CORTAS, de una línea; enunciado conciso; sin faltas ni palabras omitidas.
- Distractores verosímiles: un número o una palabra cambiada, cifras reales de otro apartado,
  absolutos («siempre», «nunca»), detalles técnicos inventados. Las 3 opciones con forma y longitud parecidas.
- Mezclar tipos: literal, en negativo («NO es…»), supuesto práctico, cálculo, ordenación.
- Comprobar siempre la respuesta en el manual. Nada de memoria.
- **No preguntar por números de anexo o de artículo** (regla del usuario, 25/11/2026): nada de «¿qué contiene el
  anexo II?» o «¿qué artículo regula…?». Saberse qué número tiene cada anexo o artículo no enseña nada. Se pregunta el
  contenido; la referencia puede ir en el enunciado como contexto («Según el art. 7.2…, ¿de qué depende…?»), nunca
  como respuesta. **Excepción: en la CONSTITUCIÓN sí se pregunta el número de artículo y apartado** (en los dos sentidos: ¿qué artículo dice X? / ¿qué dice el art. N.M?), pedido por el usuario el 25/11/2026.
  **Excepción: los números de las normas UNE / EN SÍ se preguntan** (el usuario dice que hace falta
  sabérselos), p. ej. «¿qué norma lleva el guante de protección química?» → UNE-EN 374-1.
- Cada pregunta enseña algo NUEVO.
- Explicación en bloques `que` / `porque` / `ojo` / `rec` (Qué es / Por qué / Ojo / Para recordar),
  lenguaje sencillo, `<mark>` en los datos clave.
- **Nunca nombrar una opción por su letra** (se barajan): referirse a su contenido.
- **La explicación puede contar otros datos del temario** (contexto, datos relacionados): al usuario le parece bien
  (26/11, sustituye a la regla del 25/11). **Pero esos datos NO cuentan como ya preguntados**: siguen libres para
  futuras preguntas.
- **Preguntas de solo cifras** (campo `cifra: 1`): un tipo más entre las normales cortas, junto a las
  de concepto. Explicación sencilla: un truco para recordar la cifra o la comparación con el dato con
  el que se suele confundir.
- Cada pregunta lleva `tq` y `ta` (tarjeta, lo más cortas posible) y añade sus términos al glosario
  (en el lote, campo `glosario`, formato de glosario.json: t, a, d, tema, f, solo).
- Campos: `id, t, d (normal|difícil), q, o (3), c (0-2), o4, que, porque, ojo, rec, f, tq, ta`
  y, según el tipo, `cifra`, `ex`, `int`, `dib` + `img` (SVG propio, nunca imágenes de los manuales).
- Ids: a partir del mayor id de preguntas.json y del lote pendiente.

## Preguntas de APLICACIÓN (campo `apl: 1`) — PRIORIDAD (usuario, 27/11/2026: «son las que más tenemos que trabajar»)
Patrón del examen real (preguntas 20, 21, 26, 77 y 88): no preguntan un dato, sino **aplicar un concepto a una situación
concreta**, y la opción que suena bien es la equivocada. Variantes:
- **Concepto descrito en un caso**: no se pide la definición, sino reconocerla en una escena (p. ej. qué pasa con el flujo
  de gases en una ventilación defensiva).
- **Límite físico**: el caso choca con una ley física y la opción «reforzada» es la trampa (p. ej. aspirar agua de un pozo
  de 20 m: ninguna bomba en superficie aspira más de ~10 m, tampoco dos en serie; la correcta es la bomba sumergida).
- **Principio + trampa de unidades**: aplicar una ley con datos en unidades mezcladas (p. ej. empuje = peso del barco
  que flota, con N, kg·m/s² y kg).
- **Escenario de un tema, respuesta en otro**: intervención (colector con gases) cuya respuesta está en la instalación
  (cierres hidráulicos del saneamiento); a menudo doble («¿qué… y qué…?»).
- **«No se exige nada»**: la correcta es que la norma no pide nada en ese caso; los distractores son exigencias reales de
  otros apartados (EI 60, EI2 30-C5…).
**LAS FAVORITAS DEL USUARIO: las que hay que DEDUCIR** (como la del pozo y la de las paredes entre habitaciones). La
respuesta **no aparece tal cual en el temario**: se deduce en el momento a partir de lo que sí dice. En la del pozo, el
manual explica la aspiración y su límite (presión atmosférica, ~10 m) pero no habla de un pozo de 20 m; en la de las paredes,
el CTE dice qué elementos deben compartimentar (sectores, locales de riesgo…) y, como entre habitaciones de una vivienda no
pide nada, la respuesta es «no se exige». Al hacerlas: partir de un principio, límite o ámbito de aplicación que SÍ está en el
manual (citarlo en `src` y en la explicación) y construir un caso que el temario no menciona literalmente. La explicación
muestra el razonamiento paso a paso: qué dice el manual → por qué de ahí se deduce la correcta → por qué falla la tentadora.
Dar prioridad a este tipo dentro de las de aplicación (y para la difícil de las 20:00).
Reglas: enunciado con un caso concreto y verosímil; el dato o principio tiene que estar en el temario (con `src`); los
distractores son errores de razonamiento típicos, no datos inventados; la explicación dice qué principio se aplica y por
qué la opción tentadora falla. Pueden ser normales o difíciles (las de las 20:00 de este estilo son ideales).
**Cantidad: 10-15 por lote**, priorizando hidráulica (cuando haya manual), ventilación, electricidad, instalaciones (ACS,
agua, gas, saneamiento), CTE DB-SI, edificaciones, APRAT y trabajos verticales. Si una sale rara o con formato nuevo,
marcarla con `revisar`.

## Proporción orientativa por lote de 100
- ~70 normales cortas (mitad cifras, mitad concepto) · **10-15 de aplicación (`apl: 1`)** · ~9 difíciles (las de las 20:00) ·
  ~5 estilo examen · ~4 intervención · ~2 dibujo. Temas variados; priorizar los menos usados.

## Difíciles (las de las 20:00)
- Saberse un dato NO es difícil: la opción tentadora debe ser la equivocada. Tipos: al revés (solo el
  dato y a qué corresponde, con «Ambas»), doble dato, supuesto doble, **concepto en un caso raro**
  (el favorito del usuario: la del diferencial que no salta en un contacto fase-neutro), definiciones
  intercambiadas. Siempre con la frase del manual que lo respalde.

## Temas delicados
- **Edificaciones I, II, III y Técnicas de estabilización tienen datos mal.** Contrastar cada dato con
  fuentes fiables; la explicación dice cómo es realmente y cómo lo pone el temario. Van en el lote
  marcadas y el usuario las revisa una a una (revision.py las pone aparte).
- **Preguntas sobre una errata** (aprobado por el usuario, 26/11/2026, preguntas 703, 717 y 723): la respuesta correcta
  es el dato real; el valor del manual puede ir como opción incorrecta, y el bloque «Ojo» empieza por «Errata del temario:»,
  dice qué pone el manual, por qué está mal y avisa de que el tribunal podría copiar la frase literal. Si poner el valor del
  manual como opción deja dos respuestas defendibles, se deja fuera (como en la 717).

## Ahorro de uso (25/11/2026, pedido del usuario)
- **No leer enteras las notas del proyecto**: este fichero basta. Solo `project_search` en las notas si hay
  una duda concreta.
- **`tandas/cobertura.json`**: qué páginas de cada manual ya se han convertido en preguntas. Cada tarea
  sigue donde lo dejó la anterior y, al terminar, actualiza `hechas` (solo números de página, nunca texto).
- **5 tareas por noche** (desde el 25/11/2026, pedido del usuario: tener pronto preguntas de TODOS los temas).
- **Un manual por tarea** (dos si son cortos), leído de corrido. Se elige con `python3 scripts/stock.py`: el tema con
  **menos preguntas sin usar** (no están en plan.json) sumando el lote de hoy; primero los manuales sin ninguna pregunta.
  Saltar los manuales que no se pueden leer como texto (escaneados) y apuntarlo en cobertura.json.
- **Manual terminado** (todas sus páginas convertidas en preguntas): poner en su nota de cobertura.json «TERMINADO (<fecha>)… El usuario puede quitarlo del proyecto» y decirlo en el aviso de la última tarea de la noche. El proyecto está lleno (límite de texto superado) y el usuario va quitando los manuales terminados para hacer sitio.
- Leer con `project_read` el manual y avanzar por páginas; `project_search` solo para comprobar datos sueltos.

## Calidad (cada tarea)
1. Comprobar cada respuesta en su página del manual mientras se escribe.
2. `python3 scripts/reglas.py tandas/pendientes/AAAA-MM-DD.json`: corregir todos los errores y mirar
   los avisos uno a uno.
3. Revisión independiente con un agente en **modelo Sonnet** (herramienta Agent, `model: "sonnet"`), que no
   ha escrito las preguntas: recibe enunciados y opciones barajadas, responde y da la página del dato.
   Revisa **todas** las difíciles, de concepto, estilo examen, intervención, dibujo y las de Edificaciones /
   Estabilización; de las de **cifras**, una de cada tres (al azar). Si falla una o no encuentra el dato,
   se corrige o se quita (y si falla una de cifras, se revisan todas las de cifras de esa tarea).
