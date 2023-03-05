from rest_framework import serializers

from general.models.org_locations import OrgLocations
from general.serializers.geog_entities_dto import GeogEntitiesSerializer
from general.serializers.organisations_dto import OrganisationsSerializer


class OrgLocationsSerializer(serializers.ModelSerializer):
    organisation = OrganisationsSerializer(many=False, read_only=True)
    city = GeogEntitiesSerializer(many=False, read_only=True)
    country = GeogEntitiesSerializer(many=False, read_only=True)

    class Meta:
        model = OrgLocations
        fields = '__all__'
