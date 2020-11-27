from django.urls import include, path
from rest_framework.routers import DefaultRouter

from services.bellboy.views import (
    BellboyDeviceViewSet,
    BellboyRegistrationView,
    PublicStatusUpdateViewSet,
    StatusUpdateViewSet,
)

app_name = "bellboy"

# For security APIs
router = DefaultRouter()
router.register(r"devices", BellboyDeviceViewSet, basename="device")
router.register(r"status-updates", StatusUpdateViewSet, basename="status-update")

# For public APIs
bellboy_router = DefaultRouter()
bellboy_router.register(
    r"status-updates", PublicStatusUpdateViewSet, basename="status-update"
)


urlpatterns = [
    path("", include(bellboy_router.urls)),
    path("admin/", include(router.urls)),
    path("register-device/", view=BellboyRegistrationView.as_view(), name="register"),
]
