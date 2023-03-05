from rest_framework import serializers

from context.models.dataset_recordkey_types import DatasetRecordkeyTypes


class DatasetRecordkeyTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetRecordkeyTypes
        fields = '__all__'
