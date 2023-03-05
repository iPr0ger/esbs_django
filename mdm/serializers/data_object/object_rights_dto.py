from rest_framework import serializers

from mdm.models.data_object.object_rights import ObjectRights
from users.serializers.users_dto import UsersSerializer


class ObjectRightsSerializer(serializers.ModelSerializer):
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectRights
        fields = '__all__'
