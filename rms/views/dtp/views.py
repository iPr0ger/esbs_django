from rest_framework import viewsets, permissions

from rms.models.dtp.dtas import DataTransferAccesses
from rms.models.dtp.dtp_datasets import DtpDatasets
from rms.models.dtp.dtp_notes import DtpNotes
from rms.models.dtp.dtp_objects import DtpObjects
from rms.models.dtp.dtp_people import DtpPeople
from rms.models.dtp.dtp_prereqs import DtpPrereqs
from rms.models.dtp.dtp_studies import DtpStudies
from rms.models.dtp.dtps import DataTransferProcesses
from rms.serializers.dtp.dtas_dto import DataTransferAccessesOutputSerializer
from rms.serializers.dtp.dtp_datasets_dto import DtpDatasetsOutputSerializer
from rms.serializers.dtp.dtp_notes_dto import DtpNotesOutputSerializer
from rms.serializers.dtp.dtp_objects_dto import DtpObjectsOutputSerializer
from rms.serializers.dtp.dtp_people_dto import DtpPeopleOutputSerializer
from rms.serializers.dtp.dtp_prereqs_dto import DtpPrereqsOutputSerializer
from rms.serializers.dtp.dtp_studies_dto import DtpStudiesOutputSerializer
from rms.serializers.dtp.dtps_dto import DataTransferProcessesOutputSerializer, \
    DataTransferProcessesDetailsOutputSerializer


class DataTransferAccessesList(viewsets.ModelViewSet):
    queryset = DataTransferAccesses.objects.all()
    serializer_class = DataTransferAccessesOutputSerializer
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
    serializer_class = DtpDatasetsOutputSerializer
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
    serializer_class = DtpNotesOutputSerializer
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
    serializer_class = DtpObjectsOutputSerializer
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
    serializer_class = DtpPeopleOutputSerializer
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
    serializer_class = DtpPrereqsOutputSerializer
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
    serializer_class = DtpStudiesOutputSerializer
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
    serializer_class = DataTransferProcessesOutputSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

