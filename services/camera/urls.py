from django.urls import path

from services.camera.views import CameraView

app_name = "camera"
urlpatterns = [
    path("", view=CameraView.as_view(), name="update"),
]
