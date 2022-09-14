from rest_framework import serializers
from . import models


class BiddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bidding
        fields = '__all__'


class ApplicationBiddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApplicationBidding
        fields = '__all__'
