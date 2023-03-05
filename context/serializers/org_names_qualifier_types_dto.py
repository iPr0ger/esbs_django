from rest_framework import serializers

from context.models.org_names_qualifier_types import OrgNameQualifierTypes


class OrgNameQualifierTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgNameQualifierTypes
        fields = '__all__'
