from rest_framework import generics

from apps.map.serializers import AddressesSerializer
from apps.map.models import Addresses


class AddressesAPIView(generics.ListAPIView):
    queryset = Addresses.objects.all().order_by('-pk')
    serializer_class = AddressesSerializer
