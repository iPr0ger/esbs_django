import uuid
from datetime import datetime

from django.db import models


class CompositeHashTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=75, db_index=True, unique=True, null=False)
    applies_to = models.CharField(max_length=75, db_index=True, null=True)
    source = models.CharField(max_length=75, db_index=True, null=True)
    description = models.TextField(null=True)
    date_added = models.DateTimeField(default=datetime.now, null=False)
    list_order = models.IntegerField(default=0, null=False)

    class Meta:
        db_table = "composite_hash_types"
        ordering = ["list_order"]
