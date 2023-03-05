from rest_framework import serializers

from context.models.object_types import ObjectTypes
from context.serializers.object_classes_dto import ObjectClassesSerializer
from context.serializers.object_filter_types_dto import ObjectFilterTypesSerializer


class ObjectTypesSerializer(serializers.ModelSerializer):
    filter_as = ObjectFilterTypesSerializer(many=False, read_only=True)
    object_class = ObjectClassesSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectTypes
        fields = '__all__'
