from rest_framework import serializers

from rms.models.dup.duas import DataUseAccesses


class DataUseAccessesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataUseAccesses
        fields = '__all__'
