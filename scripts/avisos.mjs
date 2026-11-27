// Envía el aviso de la pregunta de la hora a todos los dispositivos suscritos.
// Lo lanza GitHub Actions (.github/workflows/avisos.yml). Necesita el secreto FIREBASE_SA.
import admin from 'firebase-admin';

// Hora de la pregunta a avisar: si se ejecuta en los últimos 10 minutos de una hora
// (lo normal, a las :58), avisa de la que se abre a la hora siguiente. Si GitHub lo
// lanza con retraso (pasada la hora), avisa de la que ya está abierta, no de la siguiente.
const madrid = d => Object.fromEntries(new Intl.DateTimeFormat('en-CA', { timeZone: 'Europe/Madrid', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', weekday: 'short', hourCycle: 'h23' })
  .formatToParts(d).map(x => [x.type, x.value]));
const ahora = madrid(new Date());
const p = +ahora.minute >= 50 ? madrid(new Date(Date.now() + 15 * 60 * 1000)) : ahora;
const hour = +p.hour, day = `${p.year}-${p.month}-${p.day}`;
const force = process.env.FORZAR === 'si';
if (!force && (p.weekday === 'Sun' || hour < 9 || hour > 20)) { console.log('Fuera de horario:', day, hour); process.exit(0); }

import { readFileSync } from 'node:fs';
const plan = JSON.parse(readFileSync(new URL('../plan.json', import.meta.url)));
if (!force && !plan[day]) { console.log('No hay preguntas publicadas para', day); process.exit(0); }

admin.initializeApp({ credential: admin.credential.cert(JSON.parse(process.env.FIREBASE_SA)) });
const db = admin.firestore();
const marca = `${day}-${hour}`, est = db.doc('avisos/estado');
if (!force && (await est.get()).data()?.ultimo === marca) { console.log('Ya enviado:', marca); process.exit(0); }

const snap = await db.collection('tokens').get();
const tokens = snap.docs.map(d => d.id);
console.log('Dispositivos:', tokens.length);
// A las 20:00, si el día tiene la extra de deducir (13.º id), se manda UN solo aviso para las dos
const extra = hour === 20 && (plan[day] || []).length > 12;
const link = 'https://mefolloalbarbas.github.io/test-bombero/#inicio';
let ok = 0, borrados = 0;
for (let i = 0; i < tokens.length; i += 500) {
  const lote = tokens.slice(i, i + 500);
  const r = await admin.messaging().sendEachForMulticast({
    tokens: lote,
    data: extra
      ? { title: '🚒 Preguntas de las 20:00', body: 'Hoy son dos: la de siempre y la extra de deducir. Respóndelas hoy: mañana solo se podrán revisar.', link }
      : { title: `🚒 Pregunta de las ${hour}:00`, body: 'Ya tienes una pregunta nueva. Respóndela hoy: mañana solo se podrá revisar.', link },
    webpush: { headers: { Urgency: 'high', TTL: '3600' } }
  });
  ok += r.successCount;
  await Promise.all(r.responses.map((x, j) => {
    const c = x.error && x.error.code;
    if (c === 'messaging/registration-token-not-registered' || c === 'messaging/invalid-registration-token') { borrados++; return db.doc('tokens/' + lote[j]).delete(); }
  }));
}
await est.set({ ultimo: marca, enviados: ok, fecha: Date.now() });
console.log(`Enviados: ${ok} · tokens caducados borrados: ${borrados}`);
