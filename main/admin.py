# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Client, Price


class ClientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Client._meta.fields]


admin.site.register(Client, ClientAdmin)


class PriceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Price._meta.fields]


admin.site.register(Price, PriceAdmin)