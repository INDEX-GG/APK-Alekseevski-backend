from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
from .serializers import NewsSerializer
from .models import News


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'
