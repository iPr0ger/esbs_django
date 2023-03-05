from rest_framework import serializers

from context.serializers.doi_status_types_dto import DoiStatusTypesSerializer
from context.serializers.object_access_types_dto import ObjectAccessTypesSerializer
from context.serializers.object_classes_dto import ObjectClassesSerializer
from context.serializers.object_types_dto import ObjectTypesSerializer
from general.serializers.language_codes_dto import LanguageCodesSerializer
from general.serializers.organisations_dto import OrganisationsSerializer
from mdm.models.data_object.data_objects import DataObjects
from users.serializers.users_dto import UsersSerializer


class DataObjectsSerializer(serializers.ModelSerializer):
    doi_status = DoiStatusTypesSerializer(many=False, read_only=True)
    object_class = ObjectClassesSerializer(many=False, read_only=True)
    object_type = ObjectTypesSerializer(many=False, read_only=True)
    managing_org = OrganisationsSerializer(many=False, read_only=True)
    lang_code = LanguageCodesSerializer(many=False, read_only=True)
    access_type = ObjectAccessTypesSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = DataObjects
        fields = '__all__'
