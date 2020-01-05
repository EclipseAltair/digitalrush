# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import OnlineStoreConfiguration


class OnlineStoreConfigurationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OnlineStoreConfiguration._meta.fields]

admin.site.register(OnlineStoreConfiguration, OnlineStoreConfigurationAdmin)
