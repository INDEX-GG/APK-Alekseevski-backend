from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.base.permissions import IsAdminOrReadOnly, IsOwnerProfileOrReadOnly
from .serializers import BiddingSerializer, ApplicationBiddingSerializer
from .models import Bidding, ApplicationBidding


class BiddingViewSet(viewsets.ModelViewSet):
    queryset = Bidding.objects.all()
    serializer_class = BiddingSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ApplicationBiddingViewSet(viewsets.ModelViewSet):
    queryset = ApplicationBidding.objects.all()
    serializer_class = ApplicationBiddingSerializer
    # TODO Написать доступы для заявки
    # permission_classes = (IsAuthenticated, IsOwnerProfileOrReadOnly)
