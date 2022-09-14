from rest_framework import viewsets, generics, views
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from .serializers import *
from rest_framework.response import Response
from . import models


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'slug'


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = models.Products.objects.all()
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset


class CatalogAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer


class CatalogCategoryAPIView(views.APIView):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, requests, slug_category):
        try:
            # TODO: Add get_or_404
            current_category = models.Category.objects.get(slug=slug_category)
            products = current_category.category_products.all()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductAPIView(views.APIView):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, requests, slug_category, slug_product):
        try:
            # TODO: Add get_or_404
            current_category = models.Category.objects.get(slug=slug_category)
            product = current_category.category_products.filter(slug=slug_product)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductsSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
