from rest_framework import serializers

from context.serializers.org_names_qualifier_types_dto import OrgNameQualifierTypesSerializer
from general.models.org_names import OrgNames
from general.serializers.language_codes_dto import LanguageCodesSerializer
from general.serializers.organisations_dto import OrganisationsSerializer


class OrgNamesSerializer(serializers.ModelSerializer):
    organisation = OrganisationsSerializer(many=False, read_only=True)
    qualifier = OrgNameQualifierTypesSerializer(many=False, read_only=True)
    lang_code = LanguageCodesSerializer(many=False, read_only=True)
    changes_language = LanguageCodesSerializer(many=False, read_only=True)

    class Meta:
        model = OrgNames
        fields = '__all__'
