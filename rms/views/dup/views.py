from rest_framework import viewsets, permissions

from rms.models.dup.duas import DataUseAccesses
from rms.models.dup.dup_notes import DupNotes
from rms.models.dup.dup_objects import DupObjects
from rms.models.dup.dup_people import DupPeople
from rms.models.dup.dup_prereqs import DupPrereqs
from rms.models.dup.dup_secondary_use import DupSecondaryUse
from rms.models.dup.dup_studies import DupStudies
from rms.models.dup.dups import DataUseProcesses
from rms.serializers.dup.duas_dto import DataUseAccessesSerializer
from rms.serializers.dup.dup_notes_dto import DupNotesSerializer
from rms.serializers.dup.dup_objects_dto import DupObjectsSerializer
from rms.serializers.dup.dup_people_dto import DupPeopleSerializer
from rms.serializers.dup.dup_prereqs_dto import DupPrereqsSerializer
from rms.serializers.dup.dup_secondary_use_dto import DupSecondaryUseSerializer
from rms.serializers.dup.dup_studies_dto import DupStudiesSerializer
from rms.serializers.dup.dups_dto import DataUseProcessesSerializer


class DataUseAccessesList(viewsets.ReadOnlyModelViewSet):
    queryset = DataUseAccesses.objects.all()
    serializer_class = DataUseAccessesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DataUseAccesses.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupNotesList(viewsets.ReadOnlyModelViewSet):
    queryset = DupNotes.objects.all()
    serializer_class = DupNotesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DupNotes.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupObjectsList(viewsets.ReadOnlyModelViewSet):
    queryset = DupObjects.objects.all()
    serializer_class = DupObjectsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DupObjects.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupPeopleList(viewsets.ReadOnlyModelViewSet):
    queryset = DupPeople.objects.all()
    serializer_class = DupPeopleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DupPeople.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupPrereqsList(viewsets.ReadOnlyModelViewSet):
    queryset = DupPrereqs.objects.all()
    serializer_class = DupPrereqsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DupPrereqs.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupSecondaryUseList(viewsets.ReadOnlyModelViewSet):
    queryset = DupSecondaryUse.objects.all()
    serializer_class = DupSecondaryUseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DupSecondaryUse.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupStudiesList(viewsets.ReadOnlyModelViewSet):
    queryset = DupStudies.objects.all()
    serializer_class = DupStudiesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DupStudies.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DataUseProcessesList(viewsets.ReadOnlyModelViewSet):
    queryset = DataUseProcesses.objects.all()
    serializer_class = DataUseProcessesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
