from rest_framework import serializers

from context.serializers.access_prereq_types_dto import AccessPrereqTypesSerializer
from rms.models.dup.dup_prereqs import DupPrereqs


class DupPrereqsSerializer(serializers.ModelSerializer):
    prereq_type = AccessPrereqTypesSerializer(many=False, read_only=True)

    class Meta:
        model = DupPrereqs
        fields = '__all__'
