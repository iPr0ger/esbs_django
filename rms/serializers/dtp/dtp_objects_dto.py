from rest_framework import serializers

from context.serializers.check_status_types_dto import CheckStatusTypesSerializer
from context.serializers.object_access_types_dto import ObjectAccessTypesSerializer
from rms.models.dtp.dtp_objects import DtpObjects
from users.serializers.users_dto import UsersSerializer


class DtpObjectsSerializer(serializers.ModelSerializer):
    access_type = ObjectAccessTypesSerializer(many=False, read_only=True)
    access_check_status = CheckStatusTypesSerializer(many=False, read_only=True)
    access_check_by = UsersSerializer(many=False, read_only=True)
    md_check_status = CheckStatusTypesSerializer(many=False, read_only=True)
    md_check_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = DtpObjects
        fields = '__all__'
