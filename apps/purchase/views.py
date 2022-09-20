from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.base.permissions import IsAdminOrReadOnly, IsOwnerProfileOrReadOnly
from .serializers import PurchaseSerializer, ApplicationPurchaseSerializer
from .models import Purchase, ApplicationPurchase


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ApplicationPurchaseViewSet(viewsets.ModelViewSet):
    queryset = ApplicationPurchase.objects.all()
    serializer_class = ApplicationPurchaseSerializer
    permission_classes = (IsAuthenticated, IsOwnerProfileOrReadOnly)

