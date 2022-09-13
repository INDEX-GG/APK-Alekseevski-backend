from django.contrib import admin
from django.urls import path, include
from apps.news.views import NewsViewSet
from apps.catalog.views import ProductsViewSet, CategoryViewSet
from apps.bidding.views import BiddingViewSet, ApplicationBiddingViewSet
from apps.purchase.views import PurchaseViewSet, ApplicationPurchaseViewSet
from .yasg import urlpatterns as doc_urls
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'news', NewsViewSet)  # /api/v1/news/
router.register(r'products', ProductsViewSet)  # /api/v1/products/
router.register(r'categories', CategoryViewSet)  # /api/v1/category/
router.register(r'bidding', BiddingViewSet)  # /api/v1/bidding/
router.register(r'application-bidding', ApplicationBiddingViewSet)  # /api/v1/application-bidding/
router.register(r'purchase', PurchaseViewSet)  # /api/v1/purchase/
router.register(r'application-purchase', ApplicationPurchaseViewSet)  # /api/v1/application-purchase/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('apps.catalog.urls')),  # /api/v1/catalog/slug/slug/
    path('api/v1/', include('apps.profile.urls')),
    # path to djoser endpoints
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
]

urlpatterns += doc_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
