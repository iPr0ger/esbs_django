import datetime
import uuid

from django.db import models

from context.models.date_types import DateTypes
from mdm.models.data_object.data_objects import DataObjects
from users.models.users import Users


class ObjectDates(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, db_index=True, default=uuid.uuid4)
    object_id = models.ForeignKey(DataObjects, on_delete=models.CASCADE, db_column='object_id',
                                  related_name='object_dates_object_id')
    date_type = models.ForeignKey(DateTypes, on_delete=models.CASCADE, db_index=True,
                                  related_name="object_dates_date_type_id")
    date_is_range = models.BooleanField(default=False)
    date_as_string = models.CharField(max_length=255, blank=True, null=True)
    start_year = models.IntegerField(blank=True, null=True)
    start_month = models.IntegerField(blank=True, null=True)
    start_day = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)
    end_month = models.IntegerField(blank=True, null=True)
    end_day = models.IntegerField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True,
                                       related_name="object_dates_last_edited_by")

    class Meta:
        db_table = 'object_dates'
        ordering = ['created_on']
