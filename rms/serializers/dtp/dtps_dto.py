from rest_framework import serializers

from context.serializers.dtp_status_types_dto import DtpStatusTypesSerializer
from general.serializers.organisations_dto import OrganisationsSerializer
from rms.models.dtp.dtps import DataTransferProcesses


class DataTransferProcessesSerializer(serializers.ModelSerializer):
    organisation = OrganisationsSerializer(many=False, read_only=True)
    status = DtpStatusTypesSerializer(many=False, read_only=True)

    class Meta:
        model = DataTransferProcesses
        fields = '__all__'
