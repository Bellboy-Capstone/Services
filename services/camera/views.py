from rest_framework.response import Response
from rest_framework.views import APIView


from services.camera.serializers import CameraSerializer


class CameraView(APIView):
    """Deploys a simple POST endpoint for Bellboy devices"""

    def post(self, request, format=None):
        """Allows a bellboy to ensure the Services are up and responding"""
        serializer = CameraSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        return Response({"status": "OK", "received": data})



