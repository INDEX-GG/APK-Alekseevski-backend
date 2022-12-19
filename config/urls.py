from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.base.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.catalog.urls')),
    path('api/v1/', include('apps.news.urls')),
    path('api/v1/', include('apps.vacancies.urls')),
    path('api/v1/', include('apps.map.urls')),
]

urlpatterns += doc_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
