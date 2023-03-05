from rest_framework import serializers

from context.serializers.date_types_dto import DateTypesSerializer
from mdm.models.data_object.object_dates import ObjectDates
from users.serializers.users_dto import UsersSerializer


class ObjectDatesSerializer(serializers.ModelSerializer):
    date_type = DateTypesSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectDates
        fields = '__all__'
