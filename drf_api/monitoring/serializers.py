from rest_framework import serializers
from . import Health

STATUSES = (
    'Healthy',
    'Degraded',
    'Unstable',
)


class HealthSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.ChoiceField(choices=STATUSES, default='Healthy')

    def create(self, validated_data):
        return Health(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
