from rest_framework import serializers

from context.models.role_classes import RoleClasses


class RoleClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleClasses
        fields = '__all__'
