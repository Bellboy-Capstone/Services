from django.urls import include, path
from rest_framework.routers import DefaultRouter

from services.bellboy.views import BellboyDeviceViewSet, StatusUpdateViewSet

app_name = "bellboy"

router = DefaultRouter()
router.register(r"device", BellboyDeviceViewSet, basename="device")
router.register(r"status-update", StatusUpdateViewSet, basename="status-update")

urlpatterns = [path("", include(router.urls))]
