from rest_framework import serializers
from .models import Bidding, ApplicationBidding


class BiddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bidding
        fields = '__all__'


class ApplicationBiddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationBidding
        fields = '__all__'
