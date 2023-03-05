from rest_framework import serializers

from context.models.link_types import LinkTypes


class LinkTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkTypes
        fields = '__all__'
