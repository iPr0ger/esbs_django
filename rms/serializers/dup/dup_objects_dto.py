from rest_framework import serializers

from context.serializers.access_prereq_types_dto import AccessPrereqTypesSerializer
from rms.models.dup.dup_objects import DupObjects


class DupObjectsSerializer(serializers.ModelSerializer):
    access_type = AccessPrereqTypesSerializer(many=False, read_only=True)

    class Meta:
        model = DupObjects
        fields = '__all__'
