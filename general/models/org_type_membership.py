import datetime
import uuid

from django.db import models

from context.models.org_types import OrgTypes
from general.models.organisations import Organisations


class OrgTypeMembership(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    organisation = models.ForeignKey(Organisations, on_delete=models.CASCADE, db_index=True,
                                     related_name="org_type_membership_org_id")
    org_type = models.ForeignKey(OrgTypes, on_delete=models.CASCADE, db_index=True,
                                 related_name="org_type_membership_org_type_id")
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'org_type_membership'
        ordering = ["created_on"]
