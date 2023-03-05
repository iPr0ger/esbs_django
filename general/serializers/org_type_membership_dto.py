from rest_framework import serializers

from context.serializers.org_types_dto import OrgTypesSerializer
from general.models.org_type_membership import OrgTypeMembership
from general.serializers.organisations_dto import OrganisationsSerializer


class OrgTypeMembershipSerializer(serializers.ModelSerializer):
    organisation = OrganisationsSerializer(many=False, read_only=True)
    org_type = OrgTypesSerializer(many=False, read_only=True)

    class Meta:
        model = OrgTypeMembership
        fields = '__all__'
