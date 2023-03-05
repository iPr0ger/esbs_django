from rest_framework import viewsets, permissions

from users.models.profiles import UserProfiles
from users.models.users import Users
from users.serializers.profiles_dto import UserProfilesSerializer
from users.serializers.users_dto import UsersSerializer


class UsersList(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserProfilesList(viewsets.ModelViewSet):
    queryset = UserProfiles.objects.all()
    serializer_class = UserProfilesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(user=self.kwargs['userId'])
        )
