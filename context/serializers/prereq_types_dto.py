from rest_framework import serializers

from context.models.prereq_types import PrereqTypes


class PrereqTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrereqTypes
        fields = '__all__'
