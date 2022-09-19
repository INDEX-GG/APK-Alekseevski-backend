from apps.news.views import *
from apps.catalog.views import *
from apps.bidding.views import *
from apps.purchase.views import *
from apps.vacancies.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'products', ProductsViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'bidding', BiddingViewSet)
router.register(r'application-bidding', ApplicationBiddingViewSet)
router.register(r'purchase', PurchaseViewSet)
router.register(r'application-purchase', ApplicationPurchaseViewSet)
router.register(r'vacancies', VacancyViewSet)
router.register(r'application-vacancies', ApplicationVacancyViewSet)
