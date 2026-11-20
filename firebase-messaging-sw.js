// Service worker de avisos (notificaciones push).
const URL_APP = 'https://mefolloalbarbas.github.io/test-bombero/#inicio';

// Al pulsar el aviso: abrir la web (o traerla al frente si ya está abierta).
self.addEventListener('notificationclick', e => {
  e.stopImmediatePropagation();
  e.notification.close();
  const d = e.notification.data || {};
  const link = d.link || (d.FCM_MSG && d.FCM_MSG.data && d.FCM_MSG.data.link) || URL_APP;
  e.waitUntil((async () => {
    const ws = await clients.matchAll({ type: 'window', includeUncontrolled: true });
    for (const w of ws) {
      if (w.url.includes('/test-bombero/')) {
        try { await w.focus(); } catch (x) {}
        try { if (w.navigate) await w.navigate(link); } catch (x) {}
        return;
      }
    }
    await clients.openWindow(link);
  })());
});

importScripts('https://www.gstatic.com/firebasejs/10.12.2/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.12.2/firebase-messaging-compat.js');
importScripts('firebase-config.js');
firebase.initializeApp(self.FIREBASE_CONFIG);
const messaging = firebase.messaging();

// Los avisos llegan como datos y los muestra este service worker.
messaging.onBackgroundMessage(p => {
  if (p.notification) return;
  const d = p.data || {};
  return self.registration.showNotification(d.title || 'Nueva pregunta', {
    body: d.body || '', tag: 'pregunta', renotify: true, data: { link: d.link || URL_APP }
  });
});
