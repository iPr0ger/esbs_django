import datetime
import uuid

from django.db import models

from context.models.identifier_types import IdentifierTypes
from general.models.organisations import Organisations
from mdm.models.data_object.data_objects import DataObjects
from users.models.users import Users


class ObjectIdentifiers(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4, db_index=True)
    object_id = models.ForeignKey(DataObjects, on_delete=models.CASCADE, db_column='object_id',
                                  related_name='object_identifiers_object_id')
    identifier_type = models.ForeignKey(IdentifierTypes, on_delete=models.CASCADE, db_index=True,
                                        related_name='object_identifiers_identifier_type_id')
    identifier_org = models.ForeignKey(Organisations, on_delete=models.CASCADE, db_index=True,
                                       related_name='object_identifiers_identifier_org_id')
    identifier_value = models.CharField(max_length=255, db_index=True)
    identifier_date = models.DateTimeField(db_index=True, null=True)
    created_on = models.DateTimeField(db_index=True, default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, on_delete=models.CASCADE, db_index=True,
                                       related_name='object_identifiers_last_edited_by')

    class Meta:
        db_table = 'object_identifiers'
        ordering = ['created_on']
