from rest_framework import serializers

from context.serializers.study_feature_categories_dto import StudyFeatureCategoriesSerializer
from context.serializers.study_feature_types_dto import StudyFeatureTypesSerializer
from mdm.models.study.study_features import StudyFeatures
from users.serializers.users_dto import UsersSerializer


class StudyFeaturesSerializer(serializers.ModelSerializer):
    feature_type = StudyFeatureTypesSerializer(many=False, read_only=True)
    feature_value = StudyFeatureCategoriesSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = StudyFeatures
        fields = '__all__'
