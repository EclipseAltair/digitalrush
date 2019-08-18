# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import CatalogConfiguration


class CatalogConfigurationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CatalogConfiguration._meta.fields]

    class Meta:
        model = CatalogConfiguration

admin.site.register(CatalogConfiguration, CatalogConfigurationAdmin)
