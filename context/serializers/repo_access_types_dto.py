from rest_framework import serializers

from context.models.repo_access_types import RepoAccessTypes


class RepoAccessTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepoAccessTypes
        fields = '__all__'
