from rest_framework import serializers

from context.serializers.study_relationship_types_dto import StudyRelationshipTypesSerializer
from mdm.models.study.study_relationships import StudyRelationships
from users.serializers.users_dto import UsersSerializer


class StudyRelationshipsSerializer(serializers.ModelSerializer):
    relationship_type = StudyRelationshipTypesSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = StudyRelationships
        fields = '__all__'
