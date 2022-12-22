from django.contrib import admin

from apps.map.models import Addresses, Video

admin.site.register(Video)


@admin.register(Addresses)
class AddressesAdmin(admin.ModelAdmin):
    list_display = ['title']
