from rest_framework import serializers

from context.models.object_filter_types import ObjectFilterTypes


class ObjectFilterTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectFilterTypes
        fields = '__all__'
