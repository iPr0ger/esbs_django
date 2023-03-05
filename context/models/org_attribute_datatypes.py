import uuid

from django.db import models


class OrgAttributeDatatypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=255, db_index=True, unique=True)
    list_order = models.IntegerField(default=0)

    class Meta:
        db_table = "org_attribute_datatypes"
        ordering = ["list_order"]
