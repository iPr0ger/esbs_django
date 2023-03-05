import uuid
from datetime import datetime

from django.db import models


class TopicVocabularies(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=75, unique=True, db_index=True)
    source = models.CharField(max_length=75, db_index=True)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(default=datetime.utcnow)
    list_order = models.IntegerField(default=0)
    use_in_data_entry = models.BooleanField(default=True)
    url = models.URLField(blank=True, null=True)

    class Meta:
        db_table = "topic_vocabularies"
        ordering = ["list_order"]
