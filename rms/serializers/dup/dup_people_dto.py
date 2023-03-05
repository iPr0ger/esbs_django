from rest_framework import serializers

from rms.models.dup.dup_people import DupPeople
from users.serializers.users_dto import UsersSerializer


class DupPeopleSerializer(serializers.ModelSerializer):
    person = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = DupPeople
        fields = '__all__'
