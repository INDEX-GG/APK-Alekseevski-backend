from rest_framework import serializers
from apps.purchase.models import (
    Purchase, ApplicationPurchase, DocsSamples, Docs, Images)


class DocsSamplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocsSamples
        fields = ['id', 'purchase_docs_samples', 'src_docs']


class DocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docs
        fields = ['id', 'purchase_docs', 'src_docs']


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['id', 'purchase_images', 'src_image']


class PurchaseSerializer(serializers.ModelSerializer):
    purchase_docs_samples = DocsSamplesSerializer(many=True, read_only=True)
    purchase_docs = DocsSerializer(many=True, read_only=True)
    purchase_images = ImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Purchase
        fields = ['id', 'title', 'description', 'text', 'purchase_docs_samples', 'purchase_docs', 'purchase_images']


class ApplicationPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationPurchase
        fields = '__all__'
