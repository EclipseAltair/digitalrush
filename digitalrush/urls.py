# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

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
] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)