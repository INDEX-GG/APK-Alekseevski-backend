from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProfileDetailView, ProfileListCreateView

urlpatterns = [
    # gets all user profiles and create a new profile
    path('profiles/', ProfileListCreateView.as_view(), name="profiles"),
    # retrieves profile details of the currently logged-in user
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name="profile"),
]
