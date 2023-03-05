from rest_framework import serializers

from context.models.legal_status_types import LegalStatusTypes


class LegalStatusTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalStatusTypes
        fields = '__all__'
