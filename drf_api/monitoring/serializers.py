from rest_framework import serializers
from . import Health

HEALTH_STATUS_HEALTHY = 'healthy'
HEALTH_STATUS_DEGRADED = 'degraded'
HEALTH_STATUS_UNSTABLE = 'unstable'


class HealthSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=256, default=HEALTH_STATUS_UNSTABLE)

    def create(self, validated_data):
        return Health(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
