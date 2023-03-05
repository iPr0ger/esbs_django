import uuid
from datetime import datetime

from django.db import models
from context.models.object_classes import ObjectClasses
from context.models.object_filter_types import ObjectFilterTypes


class ObjectTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=75, unique=True, db_index=True)
    object_class = models.ForeignKey(ObjectClasses, on_delete=models.CASCADE, db_index=True,
                                     related_name='object_types_object_class_id')
    filter_as = models.ForeignKey(ObjectFilterTypes, on_delete=models.CASCADE, db_index=True,
                                  related_name="object_types_filter_as_id")
    source = models.CharField(max_length=75, db_index=True)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(default=datetime.utcnow)
    list_order = models.IntegerField(default=0)
    use_in_data_entry = models.BooleanField(default=True)

    class Meta:
        db_table = "object_types"
        ordering = ["list_order"]
