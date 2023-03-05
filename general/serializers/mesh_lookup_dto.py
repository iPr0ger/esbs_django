from rest_framework import serializers

from general.models.mesh_lookup import MeshLookup


class MeshLookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeshLookup
        fields = '__all__'
