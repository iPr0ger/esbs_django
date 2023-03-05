from rest_framework import serializers

from context.models.topic_types import TopicTypes


class TopicTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicTypes
        fields = '__all__'
