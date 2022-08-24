from rest_framework import serializers
from .models import Purchase, ApplicationPurchase


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class ApplicationPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationPurchase
        fields = '__all__'
