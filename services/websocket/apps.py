from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WebsocketConfig(AppConfig):
    name = "services.websocket"
    verbose_name = _("Websocket")

    def ready(self):
        import services.websocket.signals  # noqa
