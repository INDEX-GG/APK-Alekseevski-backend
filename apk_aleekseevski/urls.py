from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('api/news/', include('apps.news.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += doc_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
