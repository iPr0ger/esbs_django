import uuid
from datetime import datetime

from django.db import models


class DupStatusTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=255, db_index=True, unique=True)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.utcnow)
    list_order = models.IntegerField(default=0)

    class Meta:
        db_table = "dup_status_types"
        ordering = ["list_order"]
