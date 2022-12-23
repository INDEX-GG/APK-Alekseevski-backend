from django.contrib import admin
from django.contrib.auth.models import Group

from apps.map.models import Addresses, Video


@admin.register(Addresses)
class AddressesAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Video)
admin.site.unregister(Group)
