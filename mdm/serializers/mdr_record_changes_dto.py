from rest_framework import serializers

from mdm.models.mdr_record_changes import MdrRecordChanges


class MdrRecordChangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MdrRecordChanges
        fields = '__all__'
