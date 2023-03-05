from rest_framework import serializers

from context.models.time_units import TimeUnits


class TimeUnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeUnits
        fields = '__all__'
