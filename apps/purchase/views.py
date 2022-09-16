from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.base.permissions import IsAdminOrReadOnly, IsOwnerProfileOrReadOnly
from . import serializers
from . import models


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = models.Purchase.objects.all()
    serializer_class = serializers.PurchaseSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ApplicationPurchaseViewSet(viewsets.ModelViewSet):
    queryset = models.ApplicationPurchase.objects.all()
    serializer_class = serializers.ApplicationPurchaseSerializer
    permission_classes = (IsAuthenticated, IsOwnerProfileOrReadOnly)

