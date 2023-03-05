from rest_framework import viewsets, permissions

from mdm.models.study.studies import Studies
from mdm.models.study.study_contributors import StudyContributors
from mdm.models.study.study_features import StudyFeatures
from mdm.models.study.study_identifiers import StudyIdentifiers
from mdm.models.study.study_relationships import StudyRelationships
from mdm.models.study.study_titles import StudyTitles
from mdm.models.study.study_topics import StudyTopics
from mdm.serializers.study.studies_dto import StudiesSerializer
from mdm.serializers.study.study_contributors_dto import StudyContributorsSerializer
from mdm.serializers.study.study_features_dto import StudyFeaturesSerializer
from mdm.serializers.study.study_identifiers_dto import StudyIdentifiersSerializer
from mdm.serializers.study.study_relationships_dto import StudyRelationshipsSerializer
from mdm.serializers.study.study_titles_dto import StudyTitlesSerializer
from mdm.serializers.study.study_topics_dto import StudyTopicsSerializer


class StudiesList(viewsets.ModelViewSet):
    queryset = Studies.objects.all()
    serializer_class = StudiesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StudyContributorsList(viewsets.ModelViewSet):
    queryset = StudyContributors.objects.all()
    serializer_class = StudyContributorsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return StudyContributors.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(study_id=self.kwargs['studyId'])
        )


class StudyFeaturesList(viewsets.ModelViewSet):
    queryset = StudyFeatures.objects.all()
    serializer_class = StudyFeaturesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return StudyFeatures.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(study_id=self.kwargs['studyId'])
        )


class StudyIdentifiersList(viewsets.ModelViewSet):
    queryset = StudyIdentifiers.objects.all()
    serializer_class = StudyIdentifiersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return StudyIdentifiers.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(study_id=self.kwargs['studyId'])
        )


class StudyRelationshipsList(viewsets.ModelViewSet):
    queryset = StudyRelationships.objects.all()
    serializer_class = StudyRelationshipsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return StudyRelationships.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(study_id=self.kwargs['studyId'])
        )


class StudyTitlesList(viewsets.ModelViewSet):
    queryset = StudyTitles.objects.all()
    serializer_class = StudyTitlesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return StudyTitles.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(study_id=self.kwargs['studyId'])
        )


class StudyTopicsList(viewsets.ModelViewSet):
    queryset = StudyTopics.objects.all()
    serializer_class = StudyTopicsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return StudyTopics.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(study_id=self.kwargs['studyId'])
        )
