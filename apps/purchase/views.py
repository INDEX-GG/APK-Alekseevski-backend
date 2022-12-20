from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.base.permissions import IsAdminOrReadOnly, IsOwnerProfileOrReadOnly
from .serializers import PurchaseSerializer, ApplicationPurchaseSerializer
from .models import Purchase, ApplicationPurchase


class PurchaseAPIView(generics.ListAPIView):
    queryset = Purchase.objects.all().order_by('-pk')
    serializer_class = PurchaseSerializer


class PurchaseItemAPIView(generics.RetrieveAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

# class ApplicationPurchaseViewSet(viewsets.ModelViewSet):
#     queryset = ApplicationPurchase.objects.all()
#     serializer_class = ApplicationPurchaseSerializer
#     permission_classes = (IsAuthenticated, IsOwnerProfileOrReadOnly)
