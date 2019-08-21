# -*- coding: utf-8 -*-
from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('development/', views.development, name='development'),
    path('promotion/', views.promotion, name='promotion'),
    path('prices/', views.prices, name='prices'),
    path('contacts/', views.contacts, name='contacts'),
    path('feedback/', views.feedback, name='feedback')
]