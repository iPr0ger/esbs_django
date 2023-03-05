from rest_framework import serializers

from context.models.gender_eligibility_types import GenderEligibilityTypes


class GenderEligibilityTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenderEligibilityTypes
        fields = '__all__'
