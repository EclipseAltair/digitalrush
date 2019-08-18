# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import CatalogConfiguration


def catalog(request):
    config_true = CatalogConfiguration.objects.filter(bool=True)
    config_false = CatalogConfiguration.objects.filter(bool=False)
    total = 0
    for i in CatalogConfiguration.objects.filter(bool=True):
        total += i.price
    return render(request, 'catalog/catalog.html', locals())
