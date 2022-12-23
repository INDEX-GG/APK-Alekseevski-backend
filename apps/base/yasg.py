from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from config.settings import SWAGGER_URL

schema_view = get_schema_view(
    openapi.Info(
        title="APK Alekseevski",
        default_version='v1',
        description="Docs for api APK Alekseevski",
    ),
    public=True,
    url=SWAGGER_URL
)

urlpatterns = [
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
