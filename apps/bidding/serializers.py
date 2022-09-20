from rest_framework.serializers import ModelSerializer
from .models import Bidding, ApplicationBidding


class BiddingSerializer(ModelSerializer):
    class Meta:
        model = Bidding
        fields = '__all__'


class ApplicationBiddingSerializer(ModelSerializer):
    class Meta:
        model = ApplicationBidding
        fields = '__all__'
