from rest_framework import viewsets
from rest_framework.response import Response

from . import Health
from . import serializers


class HealthCheckViewSet(viewsets.ViewSet):
    serializer_class = serializers.HealthSerializer

    def list(self, _request):
        serializer = serializers.HealthSerializer(
            instance=self.health_check().values(), many=True)
        return Response(serializer.data)

    def health_check(self):
        checks = {
            1: Health(id=1, status=self.get_the_api_health_status()),
        }
        return checks

    def get_the_api_health_status(self):
        return serializers.HEALTH_STATUS_HEALTHY
