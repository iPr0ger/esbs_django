from rest_framework import serializers

from context.serializers.identifier_types_dto import IdentifierTypesSerializer
from general.serializers.organisations_dto import OrganisationsSerializer
from mdm.models.study.study_identifiers import StudyIdentifiers
from users.serializers.users_dto import UsersSerializer


class StudyIdentifiersSerializer(serializers.ModelSerializer):
    identifier_type = IdentifierTypesSerializer(many=False, read_only=True)
    identifier_org = OrganisationsSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = StudyIdentifiers
        fields = '__all__'
