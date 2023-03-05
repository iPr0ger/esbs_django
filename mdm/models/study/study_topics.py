import datetime
import uuid

from django.db import models

from context.models.topic_types import TopicTypes
from mdm.models.study.studies import Studies
from users.models.users import Users


class StudyTopics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    study_id = models.ForeignKey(Studies, on_delete=models.CASCADE, db_column='study_id',
                                 related_name='study_topics_study_id')
    topic_type = models.ForeignKey(TopicTypes, on_delete=models.CASCADE, db_column='topic_type_id',
                                   related_name='study_topics_topic_type_id')
    mesh_coded = models.BooleanField(default=False)
    mesh_code = models.CharField(max_length=255, blank=True, null=True)
    mesh_value = models.CharField(max_length=255, blank=True, null=True)
    original_value = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='last_edited_by',
                                       related_name='study_topics_last_edited_by')

    class Meta:
        db_table = 'study_topics'
        ordering = ['created_on']
