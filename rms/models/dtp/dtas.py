import datetime
import uuid

from django.db import models

from rms.models.dtp.dtps import DataTransferProcesses


class DataTransferAccesses(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4, db_index=True)
    dtp_id = models.ForeignKey(DataTransferProcesses, on_delete=models.CASCADE, db_column='dtp_id',
                               related_name='dta_dtp_id', default=None, null=True, blank=True)
    conforms_to_default = models.BooleanField(default=False)
    variations = models.TextField(blank=True, null=True)
    dta_file_path = models.TextField(blank=True, null=True)
    repo_signature_1 = models.IntegerField(default=0)
    repo_signature_2 = models.IntegerField(default=0)
    provider_signature_1 = models.IntegerField(default=0)
    provider_signature_2 = models.IntegerField(default=0)
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'data_transfer_accesses'
        ordering = ['created_on']
