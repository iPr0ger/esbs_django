from rest_framework import serializers

from context.models.dataset_consent_types import DatasetConsentTypes


class DatasetConsentTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetConsentTypes
        fields = '__all__'
