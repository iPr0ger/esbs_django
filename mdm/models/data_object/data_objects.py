import datetime
import uuid

from django.db import models

from context.models.doi_status_types import DoiStatusTypes
from context.models.object_access_types import ObjectAccessTypes
from context.models.object_classes import ObjectClasses
from context.models.object_types import ObjectTypes
from general.models.language_codes import LanguageCodes
from general.models.organisations import Organisations
from users.models.users import Users


class DataObjects(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4, db_index=True)
    sd_oid = models.CharField(max_length=255, blank=True, null=True)
    display_title = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    doi = models.CharField(max_length=255, blank=True, null=True)
    doi_status = models.ForeignKey(DoiStatusTypes, on_delete=models.CASCADE, db_column='doi_status_id',
                                   blank=True, null=True, related_name='data_objects_doi_status_id')
    publication_year = models.IntegerField(blank=True, null=True)
    object_class = models.ForeignKey(ObjectClasses, on_delete=models.CASCADE, db_column='object_class_id',
                                     blank=True, null=True, related_name='data_objects_object_class_id')
    object_type = models.ForeignKey(ObjectTypes, on_delete=models.CASCADE, db_column='object_type_id',
                                    blank=True, null=True, related_name='data_objects_object_type_id')
    managing_org = models.ForeignKey(Organisations, on_delete=models.CASCADE, db_column='managing_org_id',
                                     blank=True, null=True, related_name='data_objects_managing_org_id')
    lang_code = models.ForeignKey(LanguageCodes, on_delete=models.CASCADE, db_column='lang_code_id',
                                  blank=True, null=True, related_name='data_objects_lang_code_id')
    access_type = models.ForeignKey(ObjectAccessTypes, on_delete=models.CASCADE, db_column='access_type_id',
                                    blank=True, null=True, related_name='data_objects_access_type_id')
    access_details = models.CharField(max_length=255, blank=True, null=True)
    access_details_url = models.URLField(max_length=255, blank=True, null=True)
    url_last_checked = models.DateTimeField(blank=True, null=True)
    add_study_contributors = models.BooleanField(blank=True, null=True)
    add_study_topics = models.BooleanField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True, default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='last_edited_by',
                                       blank=True, null=True, related_name='data_objects_last_edited_by')

    class Meta:
        db_table = 'data_objects'
        ordering = ['created_on']
