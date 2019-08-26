# -*- coding: utf-8 -*-
from django.urls import path
from . import views


urlpatterns = [
    path('seo', views.seo, name='seo'),
]