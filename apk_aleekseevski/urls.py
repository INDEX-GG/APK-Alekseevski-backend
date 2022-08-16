from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('api/', include('apps.api.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += doc_urls