import datetime
import uuid

from django.db import models

from context.models.org_relationship_types import OrgRelationshipTypes
from general.models.organisations import Organisations


class OrgRelationships(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4, db_index=True)
    organisation = models.ForeignKey(Organisations, on_delete=models.CASCADE, db_index=True,
                                     related_name='org_relationships_org_id')
    relationship_type = models.ForeignKey(OrgRelationshipTypes, on_delete=models.CASCADE, db_index=True,
                                          related_name='org_relationships_relationship_type_id')
    target_org = models.ForeignKey(Organisations, on_delete=models.CASCADE, db_index=True,
                                   related_name='org_relationships_target_org_id')
    is_current = models.BooleanField(default=True, db_index=True)
    year_established = models.IntegerField(blank=True, null=True, db_index=True)
    year_ceased = models.IntegerField(blank=True, null=True, db_index=True)
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'org_relationships'
