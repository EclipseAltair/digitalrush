from django.contrib import admin
from .models import OnlineStoreConfiguration


class OnlineStoreConfigurationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OnlineStoreConfiguration._meta.fields]

    class Meta:
        model = OnlineStoreConfiguration

admin.site.register(OnlineStoreConfiguration, OnlineStoreConfigurationAdmin)
