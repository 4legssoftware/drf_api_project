from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response


class HealthCheckViewSet(viewsets.GenericViewSet):

    @list_route(methods=['get'], permission_classes=[])
    def check(self, _request):
        data = {
            'health': 'healthy'
        }
        return Response(data)
