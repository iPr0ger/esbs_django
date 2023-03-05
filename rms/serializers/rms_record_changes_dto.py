from rest_framework import serializers

from rms.models.rms_record_changes import RmsRecordChanges


class RmsRecordChangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RmsRecordChanges
        fields = '__all__'
