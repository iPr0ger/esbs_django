import datetime
import uuid

from django.db import models

from context.models.contributor_types import ContributorTypes
from general.models.organisations import Organisations
from mdm.models.study.studies import Studies
from users.models.users import Users


class StudyContributors(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    study_id = models.ForeignKey(Studies, on_delete=models.CASCADE, db_column='study_id',
                                 related_name='study_contributors_study_id')
    contributor_type = models.ForeignKey(ContributorTypes, on_delete=models.CASCADE, db_column='contributor_type_id',
                                         related_name='study_contributors_contributor_type_id')
    is_individual = models.BooleanField(default=False)
    person = models.ForeignKey(Users, null=True, blank=True, on_delete=models.CASCADE, db_column='person_id',
                               related_name='study_contributors_person_id')
    organisation = models.ForeignKey(Organisations, null=True, blank=True, on_delete=models.CASCADE,
                                     db_column='organisation_id',
                                     related_name='study_contributors_organisation_id')
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, null=True, blank=True, on_delete=models.CASCADE,
                                       db_column='last_edited_by',
                                       related_name='study_contributors_last_edited_by')

    class Meta:
        db_table = 'study_contributors'
        ordering = ['created_on']
