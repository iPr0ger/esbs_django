from rest_framework import serializers

from context.serializers.org_link_types_dto import OrgLinkTypesSerializer
from general.models.org_links import OrgLinks
from general.serializers.organisations_dto import OrganisationsSerializer


class OrgLinksSerializer(serializers.ModelSerializer):
    organisation = OrganisationsSerializer(many=False, read_only=True)
    org_link_type = OrgLinkTypesSerializer(many=False, read_only=True)

    class Meta:
        model = OrgLinks
        fields = '__all__'
