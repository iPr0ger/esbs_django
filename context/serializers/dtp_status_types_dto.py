from rest_framework import serializers

from context.models.dtp_status_types import DtpStatusTypes


class DtpStatusTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DtpStatusTypes
        fields = '__all__'
