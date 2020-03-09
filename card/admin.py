# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import CardConfiguration


class CardConfigurationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CardConfiguration._meta.fields]


admin.site.register(CardConfiguration, CardConfigurationAdmin)
