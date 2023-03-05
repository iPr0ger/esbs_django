from rest_framework import serializers

from general.models.language_codes import LanguageCodes


class LanguageCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageCodes
        fields = '__all__'
