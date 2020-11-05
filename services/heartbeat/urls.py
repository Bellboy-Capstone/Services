from django.urls import path

from services.heartbeat.views import HeartbeatView

app_name = "heartbeat"
urlpatterns = [path("", view=HeartbeatView.as_view(), name="update")]
