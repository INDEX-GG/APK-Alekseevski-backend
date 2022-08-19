from rest_framework import viewsets
from rest_framework.decorators import action
from .models import *
from .permissions import IsAdminOrReadOnly
from .serializers import *
from rest_framework.response import Response


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'

    @action(methods=['get'], detail=False)
    def category(self, request):
        category = Category.objects.all()
        return Response({'category': [c.title for c in category]})
