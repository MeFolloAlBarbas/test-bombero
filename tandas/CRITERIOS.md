# Tandas nocturnas de preguntas: criterios y método

Este fichero es la referencia para las tareas programadas que generan preguntas cada noche
(y para cualquier conversación que haga una tanda). Copia de los criterios de las notas del
proyecto (`claude/entrenamiento-tests.md`); si hay contradicción, mandan las notas del proyecto.

## Visto bueno diario (regla del usuario, 25/11/2026)
- Cada noche se hace **un lote**: unas `por_noche` preguntas (tandas/estado.json), repartidas en
  varias tareas de unas `por_tarea` cada una.
- El lote se guarda en `tandas/pendientes/AAAA-MM-DD.json` (`{"preguntas": [...], "glosario": [...]}`).
  **No entra en `preguntas.json` ni en la web** hasta que el usuario da el visto bueno.
- Al terminar el lote: `python3 scripts/reglas.py` sin errores → `python3 scripts/revision.py AAAA-MM-DD` (pone todas las preguntas completas)
  → commit y push → aviso al usuario con el enlace a `tandas/revision/AAAA-MM-DD.md`.
- **Si `esperando_visto_bueno` tiene la fecha de una noche anterior, la tarea NO hace nada**
  (como mucho, un recordatorio en la primera tarea de la noche).
- Normas UNE/EN: la web las detecta solas (Laboratorio → Normas) en cualquier parte del texto de una pregunta (enunciado, opciones o explicación) y la muestran solo después de que el usuario responda esa pregunta: código, qué regula y tema. Al citar una norma, escribir siempre su código completo (p. ej. «UNE-EN 374-1»). La web SOLO muestra las que están en `laboratorio.json` → `nor` (lista de normas que aparecen en el temario). Al aprobar un lote, si sale una norma nueva, comprobar con project_search que está en algún manual y solo entonces añadirla ahí con su descripción; las que solo vengan de fuentes externas (contrastes, erratas) no se añaden.
- Cuando el usuario da el visto bueno (en una conversación): `python3 scripts/aprobar.py AAAA-MM-DD`
  (opcional `--quitar id1,id2`), luego `scripts/version.sh`, commit y push. Si pide cambios en
  preguntas concretas, se corrigen en el lote antes de aprobar y se apunta el criterio aprendido aquí
  y en las notas del proyecto.
- Si `parado` no es null (p. ej. «temario agotado»), la tarea no genera nada.

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
  como respuesta. **Excepción: los números de las normas UNE / EN SÍ se preguntan** (el usuario dice que hace falta
  sabérselos), p. ej. «¿qué norma lleva el guante de protección química?» → UNE-EN 374-1.
- Cada pregunta enseña algo NUEVO.
- Explicación en bloques `que` / `porque` / `ojo` / `rec` (Qué es / Por qué / Ojo / Para recordar),
  lenguaje sencillo, `<mark>` en los datos clave.
- **Nunca nombrar una opción por su letra** (se barajan): referirse a su contenido.
- **La explicación solo usa el dato que se pregunta**: nada de otros datos del temario que puedan ser
  futuras preguntas; como mucho, el de la opción tentadora.
- **Preguntas de solo cifras** (campo `cifra: 1`): un tipo más entre las normales cortas, junto a las
  de concepto. Explicación sencilla: un truco para recordar la cifra o la comparación con el dato con
  el que se suele confundir.
- Cada pregunta lleva `tq` y `ta` (tarjeta, lo más cortas posible) y añade sus términos al glosario
  (en el lote, campo `glosario`, formato de glosario.json: t, a, d, tema, f, solo).
- Campos: `id, t, d (normal|difícil), q, o (3), c (0-2), o4, que, porque, ojo, rec, f, tq, ta`
  y, según el tipo, `cifra`, `ex`, `int`, `dib` + `img` (SVG propio, nunca imágenes de los manuales).
- Ids: a partir del mayor id de preguntas.json y del lote pendiente.

## Proporción orientativa por lote de 100
- ~80 normales cortas (mitad cifras, mitad concepto) · ~9 difíciles (las de las 20:00) ·
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

## Ahorro de uso (25/11/2026, pedido del usuario)
- **No leer enteras las notas del proyecto**: este fichero basta. Solo `project_search` en las notas si hay
  una duda concreta.
- **`tandas/cobertura.json`**: qué páginas de cada manual ya se han convertido en preguntas. Cada tarea
  sigue donde lo dejó la anterior y, al terminar, actualiza `hechas` (solo números de página, nunca texto).
- **5 tareas por noche** (desde el 25/11/2026, pedido del usuario: tener pronto preguntas de TODOS los temas).
- **Un manual por tarea** (dos si son cortos), leído de corrido. Se elige con `python3 scripts/stock.py`: el tema con
  **menos preguntas sin usar** (no están en plan.json) sumando el lote de hoy; primero los manuales sin ninguna pregunta.
  Saltar los manuales que no se pueden leer como texto (escaneados) y apuntarlo en cobertura.json.
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
