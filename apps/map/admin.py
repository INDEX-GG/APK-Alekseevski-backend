from django.contrib import admin

from apps.map.models import Addresses


@admin.register(Addresses)
class AddressesAdmin(admin.ModelAdmin):
    list_display = ['title']
