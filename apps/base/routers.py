from apps.catalog.views import *
from apps.bidding.views import *
from apps.purchase.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'bidding', BiddingViewSet)
router.register(r'application-bidding', ApplicationBiddingViewSet)
router.register(r'purchase', PurchaseViewSet)
router.register(r'application-purchase', ApplicationPurchaseViewSet)
