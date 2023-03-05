from rest_framework import serializers

from context.models.study_statuses import StudyStatuses


class StudyStatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyStatuses
        fields = '__all__'
