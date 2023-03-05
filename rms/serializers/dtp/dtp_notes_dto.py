from rest_framework import serializers

from rms.models.dtp.dtp_notes import DtpNotes
from users.serializers.users_dto import UsersSerializer


class DtpNotesSerializer(serializers.ModelSerializer):
    author = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = DtpNotes
        fields = '__all__'
