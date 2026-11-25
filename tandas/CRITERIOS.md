# Tandas nocturnas de preguntas: criterios y método

Este fichero es la referencia para las tareas programadas que generan preguntas cada noche
(y para cualquier conversación que haga una tanda). Copia de los criterios de las notas del
proyecto (`claude/entrenamiento-tests.md`); si hay contradicción, mandan las notas del proyecto.

## Visto bueno diario (regla del usuario, 25/11/2026)
- Cada noche se hace **un lote**: unas `por_noche` preguntas (tandas/estado.json), repartidas en
  varias tareas de unas `por_tarea` cada una.
- El lote se guarda en `tandas/pendientes/AAAA-MM-DD.json` (`{"preguntas": [...], "glosario": [...]}`).
  **No entra en `preguntas.json` ni en la web** hasta que el usuario da el visto bueno.
- Al terminar el lote: `python3 scripts/reglas.py` sin errores → `python3 scripts/revision.py AAAA-MM-DD`
  → commit y push → aviso al usuario con el enlace a `tandas/revision/AAAA-MM-DD.md`.
- **Si `esperando_visto_bueno` tiene la fecha de una noche anterior, la tarea NO hace nada**
  (como mucho, un recordatorio en la primera tarea de la noche).
- Cuando el usuario da el visto bueno (en una conversación): `python3 scripts/aprobar.py AAAA-MM-DD`
  (opcional `--quitar id1,id2`), luego `scripts/version.sh`, commit y push. Si pide cambios en
  preguntas concretas, se corrigen en el lote antes de aprobar y se apunta el criterio aprendido aquí
  y en las notas del proyecto.
- Si `parado` no es null (p. ej. «temario agotado»), la tarea no genera nada.

## Qué es un dato bueno (pendiente de completar con el usuario)
- Está en un manual subido al proyecto y se comprueba en su página.
- No se ha preguntado ya (scripts/similares.py, que también usa scripts/reglas.py).
- Es de los que pregunta el tribunal: cifras, plazos, distancias, definiciones, pasos de un
  procedimiento, diferencias entre conceptos, quién hace qué.
- Tiene respuesta clara, con distractores creíbles, sin depender de interpretaciones.
- Si no quedan datos buenos, **no se rellena**: se para y se avisa al usuario (poner `parado`).

## Criterios de estilo
- Estilo del examen real de las 152 plazas (2026): 3 opciones, una correcta (+ `o4`, la 4.ª del Chulito).
- Respuestas CORTAS, de una línea; enunciado conciso; sin faltas ni palabras omitidas.
- Distractores verosímiles: un número o una palabra cambiada, cifras reales de otro apartado,
  absolutos («siempre», «nunca»), detalles técnicos inventados. Las 3 opciones con forma y longitud parecidas.
- Mezclar tipos: literal, en negativo («NO es…»), supuesto práctico, cálculo, ordenación.
- Comprobar siempre la respuesta en el manual. Nada de memoria.
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

## Calidad (cada tarea)
1. Leer el manual del tema en el proyecto y comprobar cada respuesta en su página.
2. `python3 scripts/reglas.py tandas/pendientes/AAAA-MM-DD.json`: corregir todos los errores y mirar
   los avisos uno a uno.
3. Revisión independiente: un agente que no ha escrito las preguntas las responde sin ver la solución
   y busca cada dato en el manual. Si falla una o no encuentra el dato, se corrige o se quita.
