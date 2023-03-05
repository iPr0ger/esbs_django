from rest_framework import serializers

from context.serializers.object_instance_types_dto import ObjectInstanceTypesSerializer
from context.serializers.resource_types_dto import ResourceTypesSerializer
from context.serializers.size_units_dto import SizeUnitsSerializer
from general.serializers.organisations_dto import OrganisationsSerializer
from mdm.models.data_object.object_instances import ObjectInstances
from users.serializers.users_dto import UsersSerializer


class ObjectInstancesSerializer(serializers.ModelSerializer):
    instance_type = ObjectInstanceTypesSerializer(many=False, read_only=True)
    repository_org = OrganisationsSerializer(many=False, read_only=True)
    resource_type = ResourceTypesSerializer(many=False, read_only=True)
    resource_size_unit = SizeUnitsSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectInstances
        fields = '__all__'
