from rest_framework import serializers

from context.serializers.description_types_dto import DescriptionTypesSerializer
from general.serializers.language_codes_dto import LanguageCodesSerializer
from mdm.models.data_object.object_descriptions import ObjectDescriptions
from users.serializers.users_dto import UsersSerializer


class ObjectDescriptionsSerializer(serializers.ModelSerializer):
    description_type = DescriptionTypesSerializer(many=False, read_only=True)
    lang_code = LanguageCodesSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectDescriptions
        fields = '__all__'
