from rest_framework import status, viewsets
from rest_framework.response import Response

from . import Health
from . import serializers

checks = {
    1: Health(id=1, status='Healthy'),
}


class HealthCheckViewSet(viewsets.ViewSet):
    serializer_class = serializers.HealthSerializer

    def list(self, request):
        serializer = serializers.HealthSerializer(
            instance=checks.values(), many=True)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     try:
    #         check = checks[int(pk)]
    #     except KeyError:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     except ValueError:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    #     serializer = serializers.HealthSerializer(instance=check)
    #     return Response(serializer.data)
