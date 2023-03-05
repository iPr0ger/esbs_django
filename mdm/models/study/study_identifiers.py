import datetime
import uuid

from django.db import models

from context.models.identifier_types import IdentifierTypes
from general.models.organisations import Organisations
from mdm.models.study.studies import Studies
from users.models.users import Users


class StudyIdentifiers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    study_id = models.ForeignKey(Studies, on_delete=models.CASCADE, db_column='study_id',
                                 related_name='study_identifiers_study_id')
    identifier_type = models.ForeignKey(IdentifierTypes, on_delete=models.CASCADE, db_column='identifier_type_id',
                                        related_name='study_identifiers_identifier_type_id')
    identifier_value = models.CharField(max_length=255, blank=True, null=True)
    identifier_org = models.ForeignKey(Organisations, on_delete=models.CASCADE, db_column='identifier_org_id',
                                       related_name='study_identifiers_identifier_org_id')
    identifier_date = models.DateTimeField(blank=True, null=True)
    identifier_link = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, null=True, blank=True, on_delete=models.CASCADE,
                                       related_name='study_identifiers_last_edited_by')

    class Meta:
        db_table = 'study_identifiers'
        ordering = ['created_on']
