from rest_framework import viewsets
from rest_framework.response import Response

from . import Health
from . import serializers

checks = {
    1: Health(id=1, status=serializers.HEALTH_STATUS_HEALTHY),
}


class HealthCheckViewSet(viewsets.ViewSet):
    serializer_class = serializers.HealthSerializer

    def list(self, _request):
        serializer = serializers.HealthSerializer(
            instance=checks.values(), many=True)
        return Response(serializer.data)
