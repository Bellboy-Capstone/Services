from rest_framework.response import Response
from rest_framework.views import APIView

from services.heartbeat.serializers import HeartbeatSerializer


class HeartbeatView(APIView):
    """Deploys a simple POST endpoint for Bellboy devices"""

    def post(self, request, format=None):
        """Allows a bellboy to ensure the Services are up and responding"""
        serializer = HeartbeatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        return Response({"status": "OK", "received": data})
