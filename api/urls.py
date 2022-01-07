from django.urls import path, include

from drf_spectacular.views import SpectacularJSONAPIView, SpectacularRedocView
from core.registries import plugin_registry, application_type_registry

from .user import urls as user_urls
from .user_files import urls as user_files_urls
from api.employee.views import StaffAll
from api.seat.views import SeatAll, SeatDetailView, AssignSeat
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
        path('seat/', SeatAll.as_view(), name="seat_all"),
        path('seat/<int:pk>/', SeatDetailView.as_view(), name='seat_detail'),
        path('assign/<int:pk>/', AssignSeat.as_view(), name='assign_seat')
    ]
)
