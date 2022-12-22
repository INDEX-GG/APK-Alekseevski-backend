from rest_framework.serializers import ModelSerializer
from apps.map.models import Addresses, Video


class AddressesSerializer(ModelSerializer):
    class Meta:
        model = Addresses
        fields = ['id', 'title', 'geotag']


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ['src']
