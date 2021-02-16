from account.api.serializers import (
    UserDetailSerializer,
    CreateUserSerializer
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model

User = get_user_model()

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        serializer = UserDetailSerializer(user, context={'request': request})
        return Response(serializer.data, HTTP_200_OK)

        

class UserRegisterAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer