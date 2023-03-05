from rest_framework import serializers

from context.models.composite_hash_types import CompositeHashTypes


class CompositeHashTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompositeHashTypes
        fields = '__all__'
