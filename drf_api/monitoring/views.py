from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import Health
from . import serializers

checks = {
    1: Health(id=1, status='Healthy'),
}


class HealthCheckViewSet(viewsets.ViewSet):
    serializer_class = serializers.HealthSerializer

    def list(self, _request):
        serializer = serializers.HealthSerializer(
            instance=checks.values(), many=True)
        return Response(serializer.data)

    @action(detail=False)
    def check(self, _request):
        data = {
            'status': 'healthy'
        }
        return Response(data)
