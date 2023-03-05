import datetime
import uuid

from django.db import models

from context.models.topic_types import TopicTypes
from mdm.models.data_object.data_objects import DataObjects
from users.models.users import Users


class ObjectTopics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    object_id = models.ForeignKey(DataObjects, on_delete=models.CASCADE, db_column='object_id',
                                  related_name='object_topics_object_id')
    topic_type = models.ForeignKey(TopicTypes, on_delete=models.CASCADE, db_column='topic_type_id',
                                   related_name='object_topics_topic_type_id')
    mesh_coded = models.BooleanField(default=False)
    mesh_code = models.CharField(max_length=255, blank=True, null=True)
    mesh_value = models.CharField(max_length=255, blank=True, null=True)
    original_value = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='last_edited_by',
                                       related_name='object_topics_last_edited_by')

    class Meta:
        db_table = 'object_topics'
        ordering = ['created_on']
