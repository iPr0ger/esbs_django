from rest_framework import serializers

from general.models.organisations import Organisations


class OrganisationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisations
        fields = '__all__'
