from rest_framework.serializers import ModelSerializer

from apps.map.models import Addresses


class AddressesSerializer(ModelSerializer):
    class Meta:
        model = Addresses
        fields = ['id', 'title', 'geotag']
