if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/sw.js').then(function(registration) {
            console.log('ServiceWorker registration successful with scope: ', registration.scope);
        }).catch(function(err) {
            console.log('ServiceWorker registration failed: ', err);
        });
    });
}
var CACHE_NAME = 'digitalrush-cache-v1';
var urlsToCache = [
  '/',
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

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        // ресурс есть в кеше
        if (response) {
          return response;
        }
        /* Клонируем запрос. Запрос - это поток, может быть обработан только раз.
           Если мы хотим использовать объект request несколько раз, его нужно клонировать */
        var fetchRequest = event.request.clone();

        return fetch(fetchRequest).then(
          function(response) {
            // проверяем, что получен корректный ответ
            if(!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }
            // Клонируем ответ. Объект response также является потоком.
            var responseToCache = response.clone();
            caches.open(CACHE_NAME)
              .then(function(cache) {
                cache.put(event.request, responseToCache);
              });
            return response;
          }
        );
      })
    );
});