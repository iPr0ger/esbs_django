import uuid
from datetime import datetime

from django.db import models


class CheckStatusTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    name = models.CharField(max_length=75, null=False, unique=True, db_index=True)
    description = models.TextField(null=True)
    created_on = models.DateTimeField(null=False, default=datetime.utcnow)
    list_order = models.IntegerField(default=0, null=False)

    class Meta:
        db_table = "check_status_types"
        ordering = ["list_order"]
