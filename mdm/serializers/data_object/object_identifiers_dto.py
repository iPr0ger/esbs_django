from rest_framework import serializers

from context.serializers.identifier_types_dto import IdentifierTypesSerializer
from general.serializers.organisations_dto import OrganisationsSerializer
from mdm.models.data_object.object_identifiers import ObjectIdentifiers
from users.serializers.users_dto import UsersSerializer


class ObjectIdentifiersSerializer(serializers.ModelSerializer):
    identifier_type = IdentifierTypesSerializer(many=False, read_only=True)
    identifier_org = OrganisationsSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectIdentifiers
        fields = '__all__'
