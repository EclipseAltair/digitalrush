# -*- coding: utf-8 -*-
from django.urls import path
from . import views


urlpatterns = [
    path('context', views.context, name='context'),
]