from django.contrib import admin
from .models import ContextConfiguration


class ContextConfigurationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ContextConfiguration._meta.fields]

    class Meta:
        model = ContextConfiguration

admin.site.register(ContextConfiguration, ContextConfigurationAdmin)