# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('promotion/smm/', views.smm, name='smm'),
]