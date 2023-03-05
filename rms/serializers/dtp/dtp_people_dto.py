from rest_framework import serializers

from rms.models.dtp.dtp_people import DtpPeople
from users.serializers.users_dto import UsersSerializer


class DtpPeopleSerializer(serializers.ModelSerializer):
    person = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = DtpPeople
        fields = '__all__'
