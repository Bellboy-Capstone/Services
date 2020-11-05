from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BellboyConfig(AppConfig):
    name = "services.bellboy"
    verbose_name = _("Bellboy")
