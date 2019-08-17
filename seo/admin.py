from django.contrib import admin
from .models import SeoConfiguration


class SeoConfigurationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SeoConfiguration._meta.fields]

    class Meta:
        model = SeoConfiguration

admin.site.register(SeoConfiguration, SeoConfigurationAdmin)
