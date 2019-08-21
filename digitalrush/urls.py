# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
    }

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('landing.urls')),
    path('', include('card.urls')),
    path('', include('catalog.urls')),
    path('', include('online_store.urls')),
    path('', include('seo.urls')),
    path('', include('smm.urls')),
    path('', include('context.urls')),
    path('robots.txt', lambda r: HttpResponse("User-agent: *\nDisallow: /admin\nSitemap: http://digitalrush.ru/sitemap.xml", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('manifest.json', lambda r: HttpResponse('{"name": "DigitalRush","short_name": "DigitalRush","start_url": "/",' '"display": "standalone","theme_color": "#000", "background_color": "#fff"}', content_type="application/json"))

] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)