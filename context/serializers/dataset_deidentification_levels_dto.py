from rest_framework import serializers

from context.models.dataset_deidentification_levels import DatasetDeidentificationLevels


class DatasetDeidentificationLevelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetDeidentificationLevels
        fields = '__all__'
