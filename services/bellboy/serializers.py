from rest_framework.serializers import ModelSerializer

from services.bellboy.models import BellboyDevice, StatusUpdate


class BellboyDeviceSerializer(ModelSerializer):
    class Meta:
        model = BellboyDevice
        fields = "__all__"
        read_only_fields = ["id", "created", "identifier"]


class StatusUpdateSerializer(ModelSerializer):
    class Meta:
        model = StatusUpdate
        fields = "__all__"
        read_only_fields = ["id", "created"]
