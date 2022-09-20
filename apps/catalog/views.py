from rest_framework import viewsets, generics, views
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny
from .serializers import CategorySerializer, ProductsSerializer
from rest_framework.response import Response
from .models import Category, Products


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'slug'


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Products.objects.all()
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset


class CatalogAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class CatalogCategoryAPIView(views.APIView):
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
