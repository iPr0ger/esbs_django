from rest_framework import serializers

from rms.models.dtp.dtas import DataTransferAccesses


class DataTransferAccessesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTransferAccesses
        fields = '__all__'


class DataTransferAccessesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTransferAccesses
        fields = '__all__'
