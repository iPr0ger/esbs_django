from rest_framework import serializers

from context.models.user_types import UserTypes


class UserTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTypes
        fields = '__all__'
