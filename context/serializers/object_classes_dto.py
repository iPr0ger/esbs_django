from rest_framework import serializers

from context.models.object_classes import ObjectClasses


class ObjectClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectClasses
        fields = '__all__'
