from rest_framework import serializers

from context.models.access_prereq_types import AccessPrereqTypes


class AccessPrereqTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessPrereqTypes
        fields = '__all__'
