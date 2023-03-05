import datetime
import uuid

from django.db import models

from context.models.object_instance_types import ObjectInstanceTypes
from context.models.resource_types import ResourceTypes
from context.models.size_units import SizeUnits
from general.models.organisations import Organisations
from mdm.models.data_object.data_objects import DataObjects
from users.models.users import Users


class ObjectInstances(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, db_index=True, default=uuid.uuid4)
    object_id = models.ForeignKey(DataObjects, on_delete=models.CASCADE, db_column='object_id',
                                  related_name='object_instances_object_id')
    instance_type = models.ForeignKey(ObjectInstanceTypes, on_delete=models.CASCADE, db_index=True,
                                      related_name='object_instances_instance_type_id')
    repository_org = models.ForeignKey(Organisations, on_delete=models.CASCADE, db_index=True,
                                       related_name='object_instances_repository_org_id')
    url = models.URLField(max_length=2000, null=True, blank=True)
    url_last_checked = models.DateTimeField(null=True, blank=True)
    resource_type = models.ForeignKey(ResourceTypes, on_delete=models.CASCADE, db_index=True,
                                      related_name='object_instances_resource_type_id')
    resource_size = models.BigIntegerField(null=True, blank=True)
    resource_size_unit = models.ForeignKey(SizeUnits, on_delete=models.CASCADE, db_index=True,
                                           related_name='object_instances_resource_size_unit_id')
    resource_comments = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, on_delete=models.CASCADE, db_index=True,
                                       related_name='object_instances_last_edited_by')

    class Meta:
        db_table = 'object_instances'
        ordering = ['created_on']
