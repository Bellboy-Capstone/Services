from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import Serializer


class CameraSerializer(Serializer):
    """Processes incoming API data for the Heartbeat endpoint"""

    bellboy_id = IntegerField(required=True)
    status = CharField(required=True, allow_blank=False, max_length=50)
