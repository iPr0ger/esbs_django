from rest_framework import serializers

from context.models.resource_types import ResourceTypes


class ResourceTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceTypes
        fields = '__all__'
