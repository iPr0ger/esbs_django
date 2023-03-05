import datetime
import uuid

from django.db import models

from context.models.check_status_types import CheckStatusTypes
from context.models.object_access_types import ObjectAccessTypes
from mdm.models.data_object.data_objects import DataObjects
from rms.models.dtp.dtps import DataTransferProcesses
from users.models.users import Users


class DtpObjects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    dtp_id = models.ForeignKey(DataTransferProcesses, on_delete=models.CASCADE, db_column='dtp_id', blank=True,
                               null=True, related_name='dtp_objects_dtp_id')
    object_id = models.ForeignKey(DataObjects, on_delete=models.CASCADE, db_column='object_id', blank=True,
                                  null=True, related_name='dtp_objects_object_id')
    is_dataset = models.BooleanField(default=False)
    access_type = models.ForeignKey(ObjectAccessTypes, on_delete=models.CASCADE, db_column='access_type_id',
                                    blank=True, null=True, related_name='dtp_objects_access_type_id')
    download_allowed = models.BooleanField(default=False)
    access_details = models.TextField(blank=True, null=True)
    embargo_requested = models.BooleanField(default=False)
    embargo_regime = models.TextField(blank=True, null=True)
    embargo_still_applies = models.BooleanField(default=False)
    access_check_status = models.ForeignKey(CheckStatusTypes, on_delete=models.CASCADE,
                                            db_column='access_check_status_id', blank=True, null=True,
                                            related_name='dtp_objects_access_check_status_id')
    access_check_date = models.DateTimeField(blank=True, null=True)
    access_check_by = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='access_check_by', blank=True,
                                        null=True, related_name='dtp_objects_access_check_by')
    md_check_status = models.ForeignKey(CheckStatusTypes, on_delete=models.CASCADE, db_column='md_check_status_id',
                                        blank=True, null=True, related_name='dtp_objects_md_check_status_id')
    md_check_date = models.DateTimeField(blank=True, null=True)
    md_check_by = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='md_check_by', blank=True, null=True,
                                    related_name='dtp_objects_md_check_by')
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'dtp_objects'
        ordering = ['created_on']
