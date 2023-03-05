from rest_framework import viewsets, permissions

from mdm.models.data_object.data_objects import DataObjects
from mdm.models.data_object.object_contributors import ObjectContributors
from mdm.models.data_object.object_datasets import ObjectDatasets
from mdm.models.data_object.object_dates import ObjectDates
from mdm.models.data_object.object_descriptions import ObjectDescriptions
from mdm.models.data_object.object_identifiers import ObjectIdentifiers
from mdm.models.data_object.object_instances import ObjectInstances
from mdm.models.data_object.object_relationships import ObjectRelationships
from mdm.models.data_object.object_rights import ObjectRights
from mdm.models.data_object.object_titles import ObjectTitles
from mdm.models.data_object.object_topics import ObjectTopics
from mdm.serializers.data_object.data_objects_dto import DataObjectsSerializer
from mdm.serializers.data_object.object_contributors_dto import ObjectContributorsSerializer
from mdm.serializers.data_object.object_datasets_dto import ObjectDatasetsSerializer
from mdm.serializers.data_object.object_dates_dto import ObjectDatesSerializer
from mdm.serializers.data_object.object_descriptions_dto import ObjectDescriptionsSerializer
from mdm.serializers.data_object.object_identifiers_dto import ObjectIdentifiersSerializer
from mdm.serializers.data_object.object_instances_dto import ObjectInstancesSerializer
from mdm.serializers.data_object.object_relationships_dto import ObjectRelationshipsSerializer
from mdm.serializers.data_object.object_rights_dto import ObjectRightsSerializer
from mdm.serializers.data_object.object_titles_dto import ObjectTitlesSerializer
from mdm.serializers.data_object.object_topics_dto import ObjectTopicsSerializer


class DataObjectsList(viewsets.ModelViewSet):
    queryset = DataObjects.objects.all()
    serializer_class = DataObjectsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ObjectContributorsList(viewsets.ModelViewSet):
    queryset = ObjectContributors.objects.all()
    serializer_class = ObjectContributorsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectContributors.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )


class ObjectDatasetsList(viewsets.ModelViewSet):
    queryset = ObjectDatasets.objects.all()
    serializer_class = ObjectDatasetsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectDatasets.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )


class ObjectDatesList(viewsets.ModelViewSet):
    queryset = ObjectDates.objects.all()
    serializer_class = ObjectDatesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectDates.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )


class ObjectDescriptionsList(viewsets.ModelViewSet):
    queryset = ObjectDescriptions.objects.all()
    serializer_class = ObjectDescriptionsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectDescriptions.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )


class ObjectIdentifiersList(viewsets.ModelViewSet):
    queryset = ObjectIdentifiers.objects.all()
    serializer_class = ObjectIdentifiersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectIdentifiers.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )


class ObjectInstancesList(viewsets.ModelViewSet):
    queryset = ObjectInstances.objects.all()
    serializer_class = ObjectInstancesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectInstances.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )


class ObjectRelationshipsList(viewsets.ModelViewSet):
    queryset = ObjectRelationships.objects.all()
    serializer_class = ObjectRelationshipsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectRelationships.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )


class ObjectRightsList(viewsets.ModelViewSet):
    queryset = ObjectRights.objects.all()
    serializer_class = ObjectRightsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectRights.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )


class ObjectTitlesList(viewsets.ModelViewSet):
    queryset = ObjectTitles.objects.all()
    serializer_class = ObjectTitlesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectTitles.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )


class ObjectTopicsList(viewsets.ModelViewSet):
    queryset = ObjectTopics.objects.all()
    serializer_class = ObjectTopicsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return ObjectTopics.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(object_id=self.kwargs['objectId'])
        )
