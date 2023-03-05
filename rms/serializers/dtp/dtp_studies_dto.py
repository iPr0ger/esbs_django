from rest_framework import serializers

from context.serializers.check_status_types_dto import CheckStatusTypesSerializer
from rms.models.dtp.dtp_studies import DtpStudies
from users.serializers.users_dto import UsersSerializer


class DtpStudiesSerializer(serializers.ModelSerializer):
    md_check_status = CheckStatusTypesSerializer(many=False, read_only=True)
    md_check_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = DtpStudies
        fields = '__all__'
