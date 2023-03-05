from rest_framework import serializers

from context.serializers.dataset_consent_types_dto import DatasetConsentTypesSerializer
from context.serializers.dataset_deidentification_levels_dto import DatasetDeidentificationLevelsSerializer
from context.serializers.dataset_recordkey_types_dto import DatasetRecordkeyTypesSerializer
from mdm.models.data_object.object_datasets import ObjectDatasets
from users.serializers.users_dto import UsersSerializer


class ObjectDatasetsSerializer(serializers.ModelSerializer):
    recordkey_type = DatasetRecordkeyTypesSerializer(many=False, read_only=True)
    deident_type = DatasetDeidentificationLevelsSerializer(many=False, read_only=True)
    consent_type = DatasetConsentTypesSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectDatasets
        fields = '__all__'
