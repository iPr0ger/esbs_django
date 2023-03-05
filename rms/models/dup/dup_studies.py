import datetime
import uuid

from django.db import models

from mdm.models.study.studies import Studies
from rms.models.dup.dups import DataUseProcesses


class DupStudies(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    dup_id = models.ForeignKey(DataUseProcesses, on_delete=models.CASCADE, db_column='dup_id',
                               related_name='dup_studies_dup_id')
    study_id = models.ForeignKey(Studies, on_delete=models.CASCADE, db_column='study_id',
                                 related_name='dup_studies_study_id')
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'dup_studies'
        ordering = ['created_on']
