from rest_framework import serializers

from general.models.published_journals import PublishedJournals


class PublishedJournalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublishedJournals
        fields = '__all__'
