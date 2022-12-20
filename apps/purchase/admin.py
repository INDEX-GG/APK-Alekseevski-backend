from django.contrib import admin
from apps.purchase.models import (
    Purchase, ApplicationPurchase, DocsSamples, Docs, Images)

admin.site.register(ApplicationPurchase)


class ImageInline(admin.TabularInline):
    model = Images
    extra = 0


class DocsSamplesInline(admin.TabularInline):
    model = DocsSamples
    extra = 0


class DocsInline(admin.TabularInline):
    model = Docs
    extra = 0


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ImageInline, DocsSamplesInline, DocsInline]
