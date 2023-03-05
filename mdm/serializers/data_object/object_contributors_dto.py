from rest_framework import serializers

from context.serializers.contributor_types_dto import ContributorTypesSerializer
from general.serializers.organisations_dto import OrganisationsSerializer
from mdm.models.data_object.object_contributors import ObjectContributors
from users.serializers.users_dto import UsersSerializer


class ObjectContributorsSerializer(serializers.ModelSerializer):
    contributor_type = ContributorTypesSerializer(many=False, read_only=True)
    person = UsersSerializer(many=False, read_only=True)
    organisation = OrganisationsSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectContributors
        fields = '__all__'
