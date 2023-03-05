from rest_framework import serializers

from context.models.description_types import DescriptionTypes


class DescriptionTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionTypes
        fields = '__all__'
