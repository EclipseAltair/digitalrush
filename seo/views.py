from django.shortcuts import render
from .models import SeoConfiguration


def seo(request):
    config_true = SeoConfiguration.objects.filter(bool=True)
    config_false = SeoConfiguration.objects.filter(bool=False)
    total = 0
    for i in SeoConfiguration.objects.filter(bool=True):
        total += i.price
    return render(request, 'seo/seo.html', locals())