from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.catalog.models import Products, Category, Images


class ImageInline(admin.TabularInline):
    model = Images
    extra = 0
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')

    preview.short_description = "Картинки"


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ImageInline, ]
    exclude = ('slug',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    exclude = ('slug',)
