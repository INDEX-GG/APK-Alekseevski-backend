from django.urls import path
from apps.map.views import AddressesAPIView, VideoAPIView


urlpatterns = [
    path('map/', AddressesAPIView.as_view()),
    path('video/', VideoAPIView.as_view()),
]
