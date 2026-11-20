# Test Bombero Madrid

App de entrenamiento tipo test para la oposición de Bombero Especialista del Ayuntamiento de Madrid.

- `index.html`: la app.
- `preguntas.json`: el banco de preguntas (se amplía con el tiempo).
- `firebase-config.js`: la configuración del proyecto de Firebase (no es secreta).
- `firestore.rules`: las reglas de seguridad que hay que pegar en Firestore.

## Cómo funciona

- Cada persona entra escribiendo su nombre. Por detrás, Firebase le asigna una sesión anónima en ese navegador.
- Preguntas de hoy: 12 al día (de 9:00 a 20:00, hora de Madrid), de lunes a sábado. Solo se pueden responder ese día; después quedan para revisar.
- Puntuación: acierto +1, fallo −0,33, en blanco 0.
- Ranking semanal: se publica el domingo. Nota máxima, 72 netas; el corte está en más del 70 %.

## Puesta en marcha (una sola vez)

1. Firebase → crear proyecto → añadir app web → copiar la configuración en `firebase-config.js`.
2. Authentication → Método de acceso → activar **Anónimo**. En Configuración → Dominios autorizados, añadir `mefolloalbarbas.github.io`.
3. Firestore Database → crear base de datos (región europe-west) → pestaña Reglas → pegar `firestore.rules` → Publicar.
4. GitHub → Settings → Pages → Deploy from a branch → `main` / root.

Nota: el progreso está ligado al navegador en el que se entra. Si alguien cambia de móvil, empieza de cero (aunque su nombre en el ranking se mantiene en las semanas ya cerradas).
