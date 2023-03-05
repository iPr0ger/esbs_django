from rest_framework import viewsets, permissions

from general.models.geog_entities import GeogEntities
from general.models.language_codes import LanguageCodes
from general.models.mesh_lookup import MeshLookup
from general.models.org_attributes import OrgAttributes
from general.models.org_links import OrgLinks
from general.models.org_locations import OrgLocations
from general.models.org_names import OrgNames
from general.models.org_relationships import OrgRelationships
from general.models.org_type_membership import OrgTypeMembership
from general.models.organisations import Organisations
from general.models.published_journals import PublishedJournals
from general.serializers.geog_entities_dto import GeogEntitiesSerializer
from general.serializers.language_codes_dto import LanguageCodesSerializer
from general.serializers.mesh_lookup_dto import MeshLookupSerializer
from general.serializers.org_attributes_dto import OrgAttributesSerializer
from general.serializers.org_links_dto import OrgLinksSerializer
from general.serializers.org_locations_dto import OrgLocationsSerializer
from general.serializers.org_names_dto import OrgNamesSerializer
from general.serializers.org_relationships_dto import OrgRelationshipsSerializer
from general.serializers.org_type_membership_dto import OrgTypeMembershipSerializer
from general.serializers.organisations_dto import OrganisationsSerializer
from general.serializers.published_journals_dto import PublishedJournalsSerializer


# Create your views here.
class GeogEntitiesList(viewsets.ReadOnlyModelViewSet):
    queryset = GeogEntities.objects.all()
    serializer_class = GeogEntitiesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MeshLookupList(viewsets.ReadOnlyModelViewSet):
    queryset = MeshLookup.objects.all()
    serializer_class = MeshLookupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrgAttributesList(viewsets.ReadOnlyModelViewSet):
    queryset = OrgAttributes.objects.all()
    serializer_class = OrgAttributesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return OrgAttributes.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(organisation=self.kwargs['orgId'])
        )


class OrgLinksList(viewsets.ReadOnlyModelViewSet):
    queryset = OrgLinks.objects.all()
    serializer_class = OrgLinksSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return OrgLinks.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(organisation=self.kwargs['orgId'])
        )


class OrgLocationsList(viewsets.ReadOnlyModelViewSet):
    queryset = OrgLocations.objects.all()
    serializer_class = OrgLocationsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return OrgLocations.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(organisation=self.kwargs['orgId'])
        )


class OrgNamesList(viewsets.ReadOnlyModelViewSet):
    queryset = OrgNames.objects.all()
    serializer_class = OrgNamesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return OrgNames.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(organisation=self.kwargs['orgId'])
        )


class OrgRelationshipsList(viewsets.ReadOnlyModelViewSet):
    queryset = OrgRelationships.objects.all()
    serializer_class = OrgRelationshipsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return OrgRelationships.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(organisation=self.kwargs['orgId'])
        )


class OrgTypeMembershipList(viewsets.ReadOnlyModelViewSet):
    queryset = OrgTypeMembership.objects.all()
    serializer_class = OrgTypeMembershipSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return OrgTypeMembership.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(organisation=self.kwargs['orgId'])
        )


class PublishedJournalsList(viewsets.ReadOnlyModelViewSet):
    queryset = PublishedJournals.objects.all()
    serializer_class = PublishedJournalsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LanguageCodesList(viewsets.ReadOnlyModelViewSet):
    queryset = LanguageCodes.objects.all()
    serializer_class = LanguageCodesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrganisationsList(viewsets.ModelViewSet):
    queryset = Organisations.objects.all()
    serializer_class = OrganisationsSerializer
    permission_classes = [permissions.IsAuthenticated]
