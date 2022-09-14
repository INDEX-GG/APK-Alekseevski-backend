from rest_framework import viewsets
from apps.base.permissions import IsAdminOrReadOnly
from . import serializers
from . import models


class NewsViewSet(viewsets.ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'
