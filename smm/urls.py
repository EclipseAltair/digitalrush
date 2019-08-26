# -*- coding: utf-8 -*-
from django.urls import path
from . import views


urlpatterns = [
    path('smm', views.smm, name='smm'),
]