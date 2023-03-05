import uuid

from django.db import models

from context.models.rms_user_types import RmsUserTypes
from context.models.role_classes import RoleClasses
from context.models.role_types import RoleTypes
from general.models.organisations import Organisations
from users.models.users import Users


class UserProfiles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='user_profiles_user_id')
    ls_aai_id = models.CharField(max_length=255, null=True, blank=True)
    role = models.ForeignKey(RoleTypes, on_delete=models.CASCADE, db_column='role_id',
                             related_name='users_role_id')
    role_class = models.ForeignKey(RoleClasses, on_delete=models.CASCADE, db_column='role_class',
                                   related_name='users_role_class')
    user_type = models.ForeignKey(RmsUserTypes, on_delete=models.CASCADE, db_column='user_role',
                                  related_name='users_user_type')
    organisation = models.ForeignKey(Organisations, on_delete=models.CASCADE, db_column='organisation_id',
                                     related_name='users_organisation_id')

    class Meta:
        db_table = 'user_profiles'
