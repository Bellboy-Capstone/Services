from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from services.heartbeat.serializers import HeartbeatSerializer


class HeartbeatView(APIView):

    """Deploys a simple POST endpoint for Bellboy devices."""

    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def post(self, request, format=None):
        """Allows a bellboy to ensure the Services are up and responding."""
        serializer = HeartbeatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        return Response({"status": "OK", "received": data})

    def get(self, request=None):
        return Response(
            {"status": "OK", "message": "Bellboy Services are up and ready to go!"}
        )
