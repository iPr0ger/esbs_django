from rest_framework import serializers

from context.models.org_attribute_types import OrgAttributeTypes
from context.serializers.org_attribute_datatypes_dto import OrgAttributeDatatypesSerializer


class OrgAttributeTypesSerializer(serializers.ModelSerializer):
    org_attribute_datatype = OrgAttributeDatatypesSerializer(many=False, read_only=True)

    class Meta:
        model = OrgAttributeTypes
        fields = '__all__'
