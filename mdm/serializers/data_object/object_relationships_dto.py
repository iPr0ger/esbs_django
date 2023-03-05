from rest_framework import serializers

from context.serializers.object_relationship_types_dto import ObjectRelationshipTypesSerializer
from mdm.models.data_object.object_relationships import ObjectRelationships
from users.serializers.users_dto import UsersSerializer


class ObjectRelationshipsSerializer(serializers.ModelSerializer):
    relationship_type = ObjectRelationshipTypesSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectRelationships
        fields = '__all__'
