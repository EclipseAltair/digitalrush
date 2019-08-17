from django.contrib import admin
from .models import CardConfiguration


class CardConfigurationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CardConfiguration._meta.fields]

    class Meta:
        model = CardConfiguration

admin.site.register(CardConfiguration, CardConfigurationAdmin)
