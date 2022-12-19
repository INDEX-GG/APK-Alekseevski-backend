from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from apps.catalog.serializers import CategorySerializer, ProductsSerializer
from apps.catalog.models import Category


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class CategoryItemAPIView(views.APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)

    def get(self, requests, slug_category):
        try:
            current_category = Category.objects.get(slug=slug_category)
            products = current_category.category_products.all()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductAPIView(views.APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)

    def get(self, requests, slug_category, slug_product):
        try:
            current_category = Category.objects.get(slug=slug_category)
            product = current_category.category_products.filter(slug=slug_product)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductsSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
