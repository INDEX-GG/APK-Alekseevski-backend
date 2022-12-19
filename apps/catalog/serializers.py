from rest_framework.serializers import ModelSerializer
from apps.catalog.models import Products, Category, Images


class ImagesSerializer(ModelSerializer):
    class Meta:
        model = Images
        fields = ['id', 'products', 'src']


class ProductsSerializer(ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        fields = ['id', 'category', 'title', 'slug', 'description', 'price', 'images']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'src']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
