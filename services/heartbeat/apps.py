from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HeartbeatConfig(AppConfig):
    name = "services.heartbeat"
    verbose_name = _("Heartbeat")
