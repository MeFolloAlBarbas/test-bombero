// Envía el aviso de la pregunta de la hora a todos los dispositivos suscritos.
// Lo lanza GitHub Actions (.github/workflows/avisos.yml). Necesita el secreto FIREBASE_SA.
import admin from 'firebase-admin';

const p = Object.fromEntries(new Intl.DateTimeFormat('en-CA', { timeZone: 'Europe/Madrid', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', weekday: 'short', hourCycle: 'h23' })
  .formatToParts(new Date(Date.now() + 30 * 60 * 1000)).map(x => [x.type, x.value]));
const hour = +p.hour, day = `${p.year}-${p.month}-${p.day}`;
const force = process.env.FORZAR === 'si';
if (!force && (p.weekday === 'Sun' || hour < 9 || hour > 20)) { console.log('Fuera de horario:', day, hour); process.exit(0); }

admin.initializeApp({ credential: admin.credential.cert(JSON.parse(process.env.FIREBASE_SA)) });
const db = admin.firestore();
const marca = `${day}-${hour}`, est = db.doc('avisos/estado');
if (!force && (await est.get()).data()?.ultimo === marca) { console.log('Ya enviado:', marca); process.exit(0); }

const snap = await db.collection('tokens').get();
const tokens = snap.docs.map(d => d.id);
console.log('Dispositivos:', tokens.length);
const link = 'https://pedroireneo-cpu.github.io/test-bombero/#inicio';
let ok = 0, borrados = 0;
for (let i = 0; i < tokens.length; i += 500) {
  const lote = tokens.slice(i, i + 500);
  const r = await admin.messaging().sendEachForMulticast({
    tokens: lote,
    webpush: {
      notification: { title: `🚒 Pregunta de las ${hour}:00`, body: 'Ya tienes una pregunta nueva. Respóndela hoy: mañana solo se podrá revisar.', tag: 'pregunta', renotify: true },
      fcmOptions: { link }
    }
  });
  ok += r.successCount;
  await Promise.all(r.responses.map((x, j) => {
    const c = x.error && x.error.code;
    if (c === 'messaging/registration-token-not-registered' || c === 'messaging/invalid-registration-token') { borrados++; return db.doc('tokens/' + lote[j]).delete(); }
  }));
}
await est.set({ ultimo: marca, enviados: ok, fecha: Date.now() });
console.log(`Enviados: ${ok} · tokens caducados borrados: ${borrados}`);
