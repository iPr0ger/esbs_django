import uuid
from datetime import datetime

from django.db import models


class OrgLinkTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=75, db_index=True, unique=True)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.utcnow)
    list_order = models.IntegerField(default=0)

    class Meta:
        db_table = "org_link_types"
        ordering = ["list_order"]
