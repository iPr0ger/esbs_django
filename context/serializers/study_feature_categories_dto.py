from rest_framework import serializers

from context.models.study_feature_categories import StudyFeatureCategories
from context.serializers.study_feature_types_dto import StudyFeatureTypesSerializer


class StudyFeatureCategoriesSerializer(serializers.ModelSerializer):
    feature_type = StudyFeatureTypesSerializer(many=False, read_only=True)

    class Meta:
        model = StudyFeatureCategories
        fields = '__all__'
