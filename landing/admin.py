# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import LandingConfiguration


class LandingConfigurationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LandingConfiguration._meta.fields]


admin.site.register(LandingConfiguration, LandingConfigurationAdmin)
