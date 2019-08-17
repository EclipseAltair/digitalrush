from django.shortcuts import render
from .models import ContextConfiguration


def context(request):
    config_true = ContextConfiguration.objects.filter(bool=True)
    config_false = ContextConfiguration.objects.filter(bool=False)
    total = 0
    for i in ContextConfiguration.objects.filter(bool=True):
        total += i.price
    return render(request, 'context/context.html', locals())