from rest_framework import serializers

from context.serializers.org_relationship_types_dto import OrgRelationshipTypesSerializer
from general.models.org_relationships import OrgRelationships
from general.serializers.organisations_dto import OrganisationsSerializer


class OrgRelationshipsSerializer(serializers.ModelSerializer):
    organisation = OrganisationsSerializer(many=False, read_only=True)
    relationship_type = OrgRelationshipTypesSerializer(many=False, read_only=True)
    target_org = OrganisationsSerializer(many=False, read_only=True)

    class Meta:
        model = OrgRelationships
        fields = '__all__'
