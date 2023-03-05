from rest_framework import serializers

from context.models.date_types import DateTypes


class DateTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateTypes
        fields = '__all__'
