from rest_framework import serializers

from context.serializers.topic_types_dto import TopicTypesSerializer
from mdm.models.study.study_topics import StudyTopics
from users.serializers.users_dto import UsersSerializer


class StudyTopicsSerializer(serializers.ModelSerializer):
    topic_type = TopicTypesSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = StudyTopics
        fields = '__all__'
