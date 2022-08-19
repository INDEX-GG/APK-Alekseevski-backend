from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.news.views import NewsViewSet
from apps.catalog.views import ProductsViewSet, CategoryViewSet
from .yasg import urlpatterns as doc_urls
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'news', NewsViewSet)   # http://127.0.0.1:8000/api/v1/news/

router.register(r'products', ProductsViewSet)   # http://127.0.0.1:8000/api/v1/products/
router.register(r'category', CategoryViewSet)   # http://127.0.0.1:8000/api/v1/category/


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]

urlpatterns += doc_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
