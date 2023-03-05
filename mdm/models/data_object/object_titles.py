import datetime
import uuid

from django.db import models

from context.models.language_usage_types import LanguageUsageTypes
from context.models.title_types import TitleTypes
from general.models.language_codes import LanguageCodes
from mdm.models.data_object.data_objects import DataObjects
from users.models.users import Users


class ObjectTitles(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, db_index=True, default=uuid.uuid4)
    object_id = models.ForeignKey(DataObjects, on_delete=models.CASCADE, db_column='object_id',
                                  related_name='object_titles_object_id')
    title_type = models.ForeignKey(TitleTypes, on_delete=models.CASCADE, db_index=True,
                                   related_name='object_titles_title_type_id')
    title_text = models.CharField(max_length=255, db_index=True)
    lang_code = models.ForeignKey(LanguageCodes, on_delete=models.CASCADE, db_index=True,
                                  related_name='object_titles_lang_code_id')
    lang_usage = models.ForeignKey(LanguageUsageTypes, on_delete=models.CASCADE, db_index=True,
                                   related_name='object_titles_lang_usage_id')
    is_default = models.BooleanField(default=False, db_index=True)
    comments = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, on_delete=models.CASCADE,
                                       related_name='object_titles_last_edited_by')

    class Meta:
        db_table = 'object_titles'
        ordering = ['created_on']
