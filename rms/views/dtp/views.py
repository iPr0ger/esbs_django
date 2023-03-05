from rest_framework import viewsets, permissions

from rms.models.dtp.dtas import DataTransferAccesses
from rms.models.dtp.dtp_datasets import DtpDatasets
from rms.models.dtp.dtp_notes import DtpNotes
from rms.models.dtp.dtp_objects import DtpObjects
from rms.models.dtp.dtp_people import DtpPeople
from rms.models.dtp.dtp_prereqs import DtpPrereqs
from rms.models.dtp.dtp_studies import DtpStudies
from rms.models.dtp.dtps import DataTransferProcesses
from rms.serializers.dtp.dtas_dto import DataTransferAccessesSerializer
from rms.serializers.dtp.dtp_datasets_dto import DtpDatasetsSerializer
from rms.serializers.dtp.dtp_notes_dto import DtpNotesSerializer
from rms.serializers.dtp.dtp_objects_dto import DtpObjectsSerializer
from rms.serializers.dtp.dtp_people_dto import DtpPeopleSerializer
from rms.serializers.dtp.dtp_prereqs_dto import DtpPrereqsSerializer
from rms.serializers.dtp.dtp_studies_dto import DtpStudiesSerializer
from rms.serializers.dtp.dtps_dto import DataTransferProcessesSerializer


class DataTransferAccessesList(viewsets.ModelViewSet):
    queryset = DataTransferAccesses.objects.all()
    serializer_class = DataTransferAccessesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DataTransferAccesses.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dtp_id=self.kwargs['dtpId'])
        )


class DtpDatasetsList(viewsets.ModelViewSet):
    queryset = DtpDatasets.objects.all()
    serializer_class = DtpDatasetsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DtpDatasets.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dtp_id=self.kwargs['dtpId'])
        )


class DtpNotesList(viewsets.ModelViewSet):
    queryset = DtpNotes.objects.all()
    serializer_class = DtpNotesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DtpNotes.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dtp_id=self.kwargs['dtpId'])
        )


class DtpObjectsList(viewsets.ModelViewSet):
    queryset = DtpObjects.objects.all()
    serializer_class = DtpObjectsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DtpObjects.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dtp_id=self.kwargs['dtpId'])
        )


class DtpPeopleList(viewsets.ModelViewSet):
    queryset = DtpPeople.objects.all()
    serializer_class = DtpPeopleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DtpPeople.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dtp_id=self.kwargs['dtpId'])
        )


class DtpPrereqsList(viewsets.ModelViewSet):
    queryset = DtpPrereqs.objects.all()
    serializer_class = DtpPrereqsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DtpPrereqs.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dtp_id=self.kwargs['dtpId'])
        )


class DtpStudiesList(viewsets.ModelViewSet):
    queryset = DtpStudies.objects.all()
    serializer_class = DtpStudiesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return DtpStudies.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dtp_id=self.kwargs['dtpId'])
        )


class DataTransferProcessesList(viewsets.ModelViewSet):
    queryset = DataTransferProcesses.objects.all()
    serializer_class = DataTransferProcessesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
