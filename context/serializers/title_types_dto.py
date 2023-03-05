from rest_framework import serializers

from context.models.title_types import TitleTypes


class TitleTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleTypes
        fields = '__all__'
