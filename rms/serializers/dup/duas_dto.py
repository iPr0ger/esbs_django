from rest_framework import serializers

from rms.models.dup.duas import DataUseAccesses


class DataUseAccessesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataUseAccesses
        fields = '__all__'


class DataUseAccessesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataUseAccesses
        fields = '__all__'
