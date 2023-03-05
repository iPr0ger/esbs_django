from rest_framework import serializers

from context.models.org_relationship_types import OrgRelationshipTypes


class OrgRelationshipTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgRelationshipTypes
        fields = '__all__'
