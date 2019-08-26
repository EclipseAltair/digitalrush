# -*- coding: utf-8 -*-
from django.urls import path
from . import views


urlpatterns = [
    path('promotion/context', views.context, name='context'),
]