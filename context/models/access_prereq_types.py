import uuid
from datetime import datetime

from django.db import models


class AccessPrereqTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    name = models.CharField(max_length=75, unique=True, db_index=True, null=False)
    description = models.TextField(null=True)
    created_on = models.DateTimeField(default=datetime.utcnow, null=False)
    list_order = models.IntegerField(default=0, null=False)

    class Meta:
        db_table = "access_prereq_types"
        ordering = ["list_order"]
