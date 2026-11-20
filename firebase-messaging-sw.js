// Service worker de avisos (notificaciones push).
importScripts('https://www.gstatic.com/firebasejs/10.12.2/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.12.2/firebase-messaging-compat.js');
importScripts('firebase-config.js');
firebase.initializeApp(self.FIREBASE_CONFIG);
const messaging = firebase.messaging();
messaging.onBackgroundMessage(p => {
  const d = p.data || {};
  if (p.notification) return; // el navegador ya la muestra
  self.registration.showNotification(d.title || 'Nueva pregunta', { body: d.body || '', data: { link: d.link } });
});
self.addEventListener('notificationclick', e => {
  e.notification.close();
  const link = (e.notification.data && (e.notification.data.link || (e.notification.data.FCM_MSG && e.notification.data.FCM_MSG.notification && e.notification.data.FCM_MSG.notification.click_action))) || './#inicio';
  e.waitUntil(clients.matchAll({ type: 'window', includeUncontrolled: true }).then(ws => {
    for (const w of ws) if (w.url.includes('/test-bombero/')) { w.focus(); return w.navigate ? w.navigate(link) : null; }
    return clients.openWindow(link);
  }));
});
