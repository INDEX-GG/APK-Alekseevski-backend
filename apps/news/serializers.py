from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    # TODO: fix default on date
    date = serializers.DateField(format="%d-%m-%Y", default='01-01-2000')
    image = serializers.ImageField(required=True)
    slug = serializers.SlugField(required=False)

    class Meta:
        model = News
        fields = ('title', 'slug', 'small_text', 'big_text', 'image', 'date', 'publish')
        # lookup_field = 'slug'
