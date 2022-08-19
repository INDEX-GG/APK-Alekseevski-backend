from django.contrib import admin
from .models import Products


@admin.register(Products)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ["title"]
    prepopulated_fields = {'slug': ('title',)}
