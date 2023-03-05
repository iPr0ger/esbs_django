from rest_framework import serializers

from context.serializers.gender_eligibility_types_dto import GenderEligibilityTypesSerializer
from context.serializers.study_statuses_dto import StudyStatusesSerializer
from context.serializers.study_types_dto import StudyTypesSerializer
from context.serializers.time_units_dto import TimeUnitsSerializer
from general.serializers.language_codes_dto import LanguageCodesSerializer
from mdm.models.study.studies import Studies
from users.serializers.users_dto import UsersSerializer


class StudiesSerializer(serializers.ModelSerializer):
    title_lang_code = LanguageCodesSerializer(many=False, read_only=True)
    study_type = StudyTypesSerializer(many=False, read_only=True)
    study_status = StudyStatusesSerializer(many=False, read_only=True)
    study_gender_elig = GenderEligibilityTypesSerializer(many=False, read_only=True)
    min_age_unit = TimeUnitsSerializer(many=False, read_only=True)
    max_age_unit = TimeUnitsSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = Studies
        fields = '__all__'
