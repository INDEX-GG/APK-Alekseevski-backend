from django.urls import path
from apps.map.views import AddressesAPIView


urlpatterns = [
    path('map/', AddressesAPIView.as_view()),
]
