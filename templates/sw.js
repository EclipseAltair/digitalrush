if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/sw.js').then(function(registration) {
            // Регистрация успешна
            console.log('ServiceWorker registration successful with scope: ', registration.scope);
        }).catch(function(err) {
            // Регистрация не успешна
            console.log('ServiceWorker registration failed: ', err);
        });
    });
}
var CACHE_NAME = 'digitalrush-cache-v1';
var urlsToCache = [
  '/',
  'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.2/css/all.min.css',
  '/static/css/style.min.css',
  '/static/js/scripts.min.js',
  '/static/js/parallax.min.js'
];

self.addEventListener('install', function(event) {
  // установка
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});