from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.base.permissions import IsAdminOrReadOnly, IsOwnerProfileOrReadOnly
from . import serializers
from . import models


class BiddingViewSet(viewsets.ModelViewSet):
    queryset = models.Bidding.objects.all()
    serializer_class = serializers.BiddingSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ApplicationBiddingViewSet(viewsets.ModelViewSet):
    queryset = models.ApplicationBidding.objects.all()
    serializer_class = serializers.ApplicationBiddingSerializer
    permission_classes = (IsAuthenticated, IsOwnerProfileOrReadOnly)
