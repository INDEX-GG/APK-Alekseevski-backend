from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
from .serializers import PurchaseSerializer, ApplicationPurchaseSerializer
from .models import Purchase, ApplicationPurchase


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ApplicationPurchaseViewSet(viewsets.ModelViewSet):
    queryset = ApplicationPurchase.objects.all()
    serializer_class = ApplicationPurchaseSerializer
    permission_classes = (IsAdminOrReadOnly,)
