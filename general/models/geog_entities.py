import uuid

from django.db import models
from context.models.geog_entity_types import GeogEntityTypes


class GeogEntities(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    geog_entity_type = models.ForeignKey(GeogEntityTypes, on_delete=models.CASCADE, db_column='type_id', null=False,
                                         db_index=True, related_name="geog_entities_type_id")
    name = models.CharField(max_length=75, unique=True, db_index=True, null=False)
    code = models.CharField(max_length=75, db_index=True, null=True)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, db_column='parent_id', null=True, db_index=True,
                                  related_name="geog_entities_parent_id")
    parent = models.CharField(max_length=75, db_index=True, null=True)
    old_id = models.IntegerField(null=True)

    class Meta:
        db_table = "geog_entities"
        ordering = ["name"]
