from rest_framework import serializers

from context.models.language_usage_types import LanguageUsageTypes


class LanguageUsageTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageUsageTypes
        fields = '__all__'
