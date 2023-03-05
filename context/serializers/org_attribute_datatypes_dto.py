from rest_framework import serializers

from context.models.org_attribute_datatypes import OrgAttributeDatatypes


class OrgAttributeDatatypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgAttributeDatatypes
        fields = '__all__'
