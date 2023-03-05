from rest_framework import serializers

from context.serializers.topic_types_dto import TopicTypesSerializer
from mdm.models.data_object.object_topics import ObjectTopics
from users.serializers.users_dto import UsersSerializer


class ObjectTopicsSerializer(serializers.ModelSerializer):
    topic_type = TopicTypesSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectTopics
        fields = '__all__'
