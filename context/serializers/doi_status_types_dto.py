from rest_framework import serializers

from context.models.doi_status_types import DoiStatusTypes


class DoiStatusTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoiStatusTypes
        fields = '__all__'
