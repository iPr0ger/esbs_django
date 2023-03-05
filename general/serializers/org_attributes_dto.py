from rest_framework import serializers

from context.serializers.org_attribute_types_dto import OrgAttributeTypesSerializer
from general.models.org_attributes import OrgAttributes
from general.serializers.organisations_dto import OrganisationsSerializer


class OrgAttributesSerializer(serializers.ModelSerializer):
    organisation = OrganisationsSerializer(many=False, read_only=True)
    attribute_type = OrgAttributeTypesSerializer(many=False, read_only=True)

    class Meta:
        model = OrgAttributes
        fields = '__all__'
