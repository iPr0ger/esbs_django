from rest_framework import serializers

from context.serializers.contributor_types_dto import ContributorTypesSerializer
from general.serializers.organisations_dto import OrganisationsSerializer
from mdm.models.study.study_contributors import StudyContributors
from users.serializers.users_dto import UsersSerializer


class StudyContributorsSerializer(serializers.ModelSerializer):
    contributor_type = ContributorTypesSerializer(many=False, read_only=True)
    person = UsersSerializer(many=False, read_only=True)
    organisation = OrganisationsSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = StudyContributors
        fields = '__all__'
