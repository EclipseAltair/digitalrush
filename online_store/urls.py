# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('development/onlinestore/', views.online_store, name='online_store'),
]