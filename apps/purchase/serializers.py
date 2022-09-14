from rest_framework import serializers
from . import models


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Purchase
        fields = '__all__'


class ApplicationPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApplicationPurchase
        fields = '__all__'
