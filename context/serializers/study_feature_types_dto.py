from rest_framework import serializers

from context.models.study_feature_types import StudyFeatureTypes


class StudyFeatureTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyFeatureTypes
        fields = '__all__'
