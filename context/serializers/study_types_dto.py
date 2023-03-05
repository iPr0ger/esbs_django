from rest_framework import serializers

from context.models.study_types import StudyTypes


class StudyTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyTypes
        fields = '__all__'
