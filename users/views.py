from rest_framework import generics
from users.models import User
from users.serializers import (
    ObtainTokenSerializer,
    UserSerializer,
    RegisterUserSerializer,
)
from rest_framework.permissions import IsAuthenticated, AllowAny


class UsersListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]


class ObtainTokenAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ObtainTokenSerializer
    permission_classes = [AllowAny]
