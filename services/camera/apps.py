from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CameraConfig(AppConfig):
    name = "services.camera"
    verbose_name = _("Camera")
