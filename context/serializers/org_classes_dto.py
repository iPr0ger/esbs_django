from rest_framework import serializers

from context.models.org_classes import OrgClasses


class OrgClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgClasses
        fields = '__all__'
