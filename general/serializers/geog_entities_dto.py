from rest_framework import serializers

from context.serializers.geog_entity_types_dto import GeogEntityTypesSerializer
from general.models.geog_entities import GeogEntities


class GeogEntitiesSerializer(serializers.ModelSerializer):
    geog_entity_type = GeogEntityTypesSerializer(many=False, read_only=True)

    class Meta:
        model = GeogEntities
        fields = '__all__'
