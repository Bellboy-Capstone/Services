from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from services.bellboy.models import BellboyDevice, StatusUpdate
from services.bellboy.serializers import BellboyDeviceSerializer, StatusUpdateSerializer


class BellboyDeviceViewSet(ModelViewSet):
    """Generic CRUD endpoints for BellboyDevice."""

    serializer_class = BellboyDeviceSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = BellboyDevice.objects.all()


class StatusUpdateViewSet(ModelViewSet):
    """Generic CRUD endpoints for StatusUpdate."""

    serializer_class = StatusUpdateSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = StatusUpdate.objects.all()


class BellboyRegistrationView(APIView):

    """Deploys a simple POST endpoint for Bellboy devices."""

    permission_classes = [AllowAny]

    def get(self, request=None):
        """Creates a new Bellboy device and returns an identifier."""
        new_bellboy = BellboyDevice()
        new_bellboy.save()
        return Response(
            {
                "status": "OK",
                "message": "New Bellboy device created.",
                "identifier": new_bellboy.identifier,
            }
        )


class PublicStatusUpdateViewSet(
    GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin
):
    """Generic CRUD endpoints for StatusUpdate."""

    serializer_class = StatusUpdateSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [AllowAny]
    queryset = StatusUpdate.objects.order_by("-created")
