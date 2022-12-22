from rest_framework import generics

from apps.map.serializers import AddressesSerializer, VideoSerializer
from apps.map.models import Addresses, Video


class AddressesAPIView(generics.ListAPIView):
    queryset = Addresses.objects.all().order_by('-pk')
    serializer_class = AddressesSerializer


class VideoAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
