# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import SeoConfiguration


class SeoConfigurationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SeoConfiguration._meta.fields]

admin.site.register(SeoConfiguration, SeoConfigurationAdmin)
