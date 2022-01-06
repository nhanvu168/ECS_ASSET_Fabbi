from django.urls import path, include

from drf_spectacular.views import SpectacularJSONAPIView, SpectacularRedocView

from core.registries import plugin_registry, application_type_registry

from .user import urls as user_urls
from .user_files import urls as user_files_urls
from api.employee.views import StaffAll
from api.seat.views import SeatAssigned, SeatAll, SeatDetail, AssignSeat
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
        path('test', StaffAll.as_view(), name="test"),
        path('test1', SeatAll.as_view(), name="test1"),
        path('test2', SeatAssigned.as_view(), name='test2'),
        # path('test3', EmployeeNotAssigned.as_view(), name="test3")
        path('test2/<int:pk>/', SeatDetail.as_view(), name='test4'),
        path('test3', AssignSeat.as_view(), name='test3')
    ]
)
