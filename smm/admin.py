from django.contrib import admin
from .models import SmmConfiguration


class SmmConfigurationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SmmConfiguration._meta.fields]

    class Meta:
        model = SmmConfiguration

admin.site.register(SmmConfiguration, SmmConfigurationAdmin)