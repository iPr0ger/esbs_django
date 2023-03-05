from rest_framework import serializers

from context.models.org_types import OrgTypes
from context.serializers.org_classes_dto import OrgClassesSerializer


class OrgTypesSerializer(serializers.ModelSerializer):
    org_class = OrgClassesSerializer(many=False, read_only=True)

    class Meta:
        model = OrgTypes
        fields = '__all__'
