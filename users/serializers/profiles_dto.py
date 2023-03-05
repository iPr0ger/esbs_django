from rest_framework import serializers

from context.serializers.rms_user_types_dto import RmsUserTypesSerializer
from context.serializers.role_classes_dto import RoleClassesSerializer
from context.serializers.role_types_dto import RoleTypesSerializer
from general.serializers.organisations_dto import OrganisationsSerializer
from users.models.profiles import UserProfiles
from users.serializers.users_dto import UsersSerializer


class UserProfilesSerializer(serializers.ModelSerializer):
    user = UsersSerializer(many=False, read_only=True)
    role = RoleTypesSerializer(many=False, read_only=True)
    role_class = RoleClassesSerializer(many=False, read_only=True)
    user_type = RmsUserTypesSerializer(many=False, read_only=True)
    organisation = OrganisationsSerializer(many=False, read_only=True)

    class Meta:
        model = UserProfiles
        fields = '__all__'
