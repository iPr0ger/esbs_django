from rest_framework import serializers

from rms.models.dtp.dtas import DataTransferAccesses


class DataTransferAccessesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTransferAccesses
        fields = '__all__'
