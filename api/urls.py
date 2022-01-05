from django.urls import path, include

from drf_spectacular.views import SpectacularJSONAPIView, SpectacularRedocView

from core.registries import plugin_registry, application_type_registry

from .user import urls as user_urls
from .user_files import urls as user_files_urls

app_name = "api"

urlpatterns = (
    [
        # path("schema.json", SpectacularJSONAPIView.as_view(), name="json_schema"),
        # path(
        #     "redoc/",
        #     SpectacularRedocView.as_view(url_name="api:json_schema"),
        #     name="redoc",
        # ),
        # path("user/", include(user_urls, namespace="user")),
        # path("user-files/", include(user_files_urls, namespace="user_files")),
    ]
)
