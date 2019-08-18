# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import LandingConfiguration


def landing(request):
    config_true = LandingConfiguration.objects.filter(bool=True)
    config_false = LandingConfiguration.objects.filter(bool=False)
    total = 0
    for i in LandingConfiguration.objects.filter(bool=True):
        total += i.price
    return render(request, 'landing/landing.html', locals())
