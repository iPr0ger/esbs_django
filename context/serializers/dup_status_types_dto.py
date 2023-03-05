from rest_framework import serializers

from context.models.dup_status_types import DupStatusTypes


class DupStatusTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DupStatusTypes
        fields = '__all__'
