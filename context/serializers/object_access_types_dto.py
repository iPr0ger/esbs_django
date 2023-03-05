from rest_framework import serializers

from context.models.object_access_types import ObjectAccessTypes


class ObjectAccessTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectAccessTypes
        fields = '__all__'
