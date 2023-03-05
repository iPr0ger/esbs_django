from rest_framework import serializers

from context.models.size_units import SizeUnits


class SizeUnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeUnits
        fields = '__all__'
