from rest_framework import serializers

from context.models.contributor_types import ContributorTypes


class ContributorTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributorTypes
        fields = '__all__'
