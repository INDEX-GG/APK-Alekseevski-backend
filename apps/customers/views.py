# from rest_framework import viewsets
# from .models import *
# from .permissions import IsAdminOrReadOnly
# from .serializers import *
#
#
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = (IsAdminOrReadOnly,)
#     lookup_field = 'slug'
#
#
# class ProductsViewSet(viewsets.ModelViewSet):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer
#     permission_classes = (IsAdminOrReadOnly,)
#     lookup_field = 'slug'
#
