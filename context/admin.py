# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import ContextConfiguration


class ContextConfigurationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ContextConfiguration._meta.fields]


admin.site.register(ContextConfiguration, ContextConfigurationAdmin)