from rest_framework import serializers

from context.models.topic_vocabularies import TopicVocabularies


class TopicVocabulariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicVocabularies
        fields = '__all__'
