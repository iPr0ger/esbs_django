from rest_framework import serializers

from context.models.rms_user_types import RmsUserTypes


class RmsUserTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RmsUserTypes
        fields = '__all__'
