# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import SmmConfiguration


def smm(request):
    config_true = SmmConfiguration.objects.filter(bool=True)
    config_false = SmmConfiguration.objects.filter(bool=False)
    total = 0
    for i in SmmConfiguration.objects.filter(bool=True):
        total += i.price
    return render(request, 'smm/smm.html', locals())