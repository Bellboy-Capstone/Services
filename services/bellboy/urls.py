from django.urls import include, path
from rest_framework.routers import DefaultRouter

from services.bellboy.views import (
    BellboyDeviceViewSet,
    BellboyRegistrationView,
    StatusUpdateViewSet,
)

app_name = "bellboy"

router = DefaultRouter()
router.register(r"devices", BellboyDeviceViewSet, basename="device")
router.register(r"status-updates", StatusUpdateViewSet, basename="status-update")

urlpatterns = [
    path("admin/", include(router.urls)),
    path("register-device/", view=BellboyRegistrationView.as_view(), name="register"),
]
