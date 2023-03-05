from rest_framework import serializers

from context.models.role_types import RoleTypes
from context.serializers.role_classes_dto import RoleClassesSerializer


class RoleTypesSerializer(serializers.ModelSerializer):
    role_class = RoleClassesSerializer(many=False, read_only=True)

    class Meta:
        model = RoleTypes
        fields = '__all__'
