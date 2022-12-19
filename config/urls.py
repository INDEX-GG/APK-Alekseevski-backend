from django.contrib import admin
from django.urls import path, include
from apps.base.yasg import urlpatterns as doc_urls
from django.conf.urls.static import static
from django.conf import settings
from apps.base.routers import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('apps.catalog.urls')),
    path('api/v1/', include('apps.news.urls')),
    path('api/v1/', include('apps.vacancies.urls')),
]

urlpatterns += doc_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)