from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from services.bellboy.models import BellboyDevice, StatusUpdate
from services.bellboy.serializers import BellboyDeviceSerializer, StatusUpdateSerializer


class IsAuthenticatedOrReadonly(object):
    pass


class BellboyDeviceViewSet(ModelViewSet):
    """Generic CRUD endpoints for BellboyDevice."""

    serializer_class = BellboyDeviceSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadonly]
    queryset = BellboyDevice.objects.all()


class StatusUpdateViewSet(ModelViewSet):
    """Generic CRUD endpoints for StatusUpdate."""

    serializer_class = StatusUpdateSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadonly]
    queryset = StatusUpdate.objects.all()
