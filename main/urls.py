# -*- coding: utf-8 -*-
from django.urls import path, include
from . import views
from .decorators import check_recaptcha


urlpatterns = [
    path('', views.main, name='main'),
    path('development', views.development, name='development'),
    path('development/', include('landing.urls')),
    path('development/', include('card.urls')),
    path('development/', include('catalog.urls')),
    path('development/', include('online_store.urls')),
    path('promotion', views.promotion, name='promotion'),
    path('promotion/', include('seo.urls')),
    path('promotion/', include('smm.urls')),
    path('promotion/', include('context.urls')),
    path('prices', views.prices, name='prices'),
    path('contacts', views.contacts, name='contacts'),
    path('feedback', check_recaptcha(views.feedback), name='feedback')
]