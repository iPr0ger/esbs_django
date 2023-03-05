from rest_framework import serializers

from context.serializers.access_prereq_types_dto import AccessPrereqTypesSerializer
from rms.models.dtp.dtp_prereqs import DtpPrereqs


class DtpPrereqsSerializer(serializers.ModelSerializer):
    prereq_type = AccessPrereqTypesSerializer(many=False, read_only=True)

    class Meta:
        model = DtpPrereqs
        fields = '__all__'
