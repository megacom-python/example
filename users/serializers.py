from typing import Any, Dict, Mapping
from rest_framework import serializers
from users.models import User
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate(self, attrs: Dict[str, Any]):
        attrs["password"] = make_password(attrs["password"], "213123123")
        return attrs


class ObtainTokenSerializer(serializers.ModelSerializer):
    token = serializers.ReadOnlyField()
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "password", "token")

    def create(self, validated_data: Mapping[str, Any]):
        email = validated_data.get("email")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist as e:
            raise AuthenticationFailed() from e
        is_valid = check_password(
            validated_data.get("password"), user.password
        )
        if not is_valid:
            raise AuthenticationFailed()

        token, _ = Token.objects.get_or_create(user=user)
        return {"token": token.key}
