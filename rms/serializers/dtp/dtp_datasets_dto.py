from rest_framework import serializers

from context.serializers.check_status_types_dto import CheckStatusTypesSerializer
from context.serializers.legal_status_types_dto import LegalStatusTypesSerializer
from rms.models.dtp.dtp_datasets import DtpDatasets
from users.serializers.users_dto import UsersSerializer


class DtpDatasetsSerializer(serializers.ModelSerializer):
    legal_status = LegalStatusTypesSerializer(many=False, read_only=True)
    desc_md_check_status = CheckStatusTypesSerializer(many=False, read_only=True)
    desc_md_check_by = UsersSerializer(many=False, read_only=True)
    deident_check_status = CheckStatusTypesSerializer(many=False, read_only=True)
    deident_check_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = DtpDatasets
        fields = '__all__'
