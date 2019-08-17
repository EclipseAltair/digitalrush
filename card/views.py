from django.shortcuts import render
from .models import CardConfiguration


def card(request):
    config_true = CardConfiguration.objects.filter(bool=True)
    config_false = CardConfiguration.objects.filter(bool=False)
    total = 0
    for i in CardConfiguration.objects.filter(bool=True):
        total += i.price
    return render(request, 'card/card.html', locals())
