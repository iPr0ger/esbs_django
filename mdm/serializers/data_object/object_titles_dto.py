from rest_framework import serializers

from context.serializers.language_usage_types_dto import LanguageUsageTypesSerializer
from context.serializers.title_types_dto import TitleTypesSerializer
from general.serializers.language_codes_dto import LanguageCodesSerializer
from mdm.models.data_object.object_titles import ObjectTitles
from users.serializers.users_dto import UsersSerializer


class ObjectTitlesSerializer(serializers.ModelSerializer):
    title_type = TitleTypesSerializer(many=False, read_only=True)
    lang_code = LanguageCodesSerializer(many=False, read_only=True)
    lang_usage = LanguageUsageTypesSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectTitles
        fields = '__all__'
