# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import Price
from .forms import ClientForm


def main(request):
    return render(request, 'main/index.html')

def development(request):
    return render(request, 'main/development.html')

def promotion(request):
    return render(request, 'main/promotion.html')

def repair(request):
    return render(request, 'main/repair.html')

def prices(request):
    landing, created = Price.objects.get_or_create(name='Лендинг')
    card, created = Price.objects.get_or_create(name='Сайт-визитка')
    catalog, created = Price.objects.get_or_create(name='Сайт-каталог')
    online_store, created = Price.objects.get_or_create(name='Интернет-магазин')
    seo, created = Price.objects.get_or_create(name='SEO')
    smm, created = Price.objects.get_or_create(name='SMM')
    context, created = Price.objects.get_or_create(name='Контекстная реклама')
    return render(request, 'main/prices.html', locals())

def contacts(request):
    return render(request, 'main/contacts.html')

def feedback(request):
    if request.POST:
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            name = request.POST['name']
            phone = request.POST['phone']
            subject = 'Новый клиент!'
            message = 'Имя: ' + name + ' | Номер телефона: ' + phone
            sender = 'digitalrushmailer@gmail.com'
            recipient = 'info@digitalrush.ru'
            send_mail(subject, message, sender, [recipient], fail_silently=False)
            return JsonResponse({})

def error_404(request, exception=None):
    return render(request, '404.html', status=404)

def error_500(request):
    return render(request, '500.html', status=500)
