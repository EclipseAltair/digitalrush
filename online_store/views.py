# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import OnlineStoreConfiguration


def online_store(request):
    config_true = OnlineStoreConfiguration.objects.filter(bool=True)
    config_false = OnlineStoreConfiguration.objects.filter(bool=False)
    total = 0
    for i in OnlineStoreConfiguration.objects.filter(bool=True):
        total += i.price
    return render(request, 'online_store/online_store.html', locals())
