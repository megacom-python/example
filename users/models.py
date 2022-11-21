from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    email = models.EmailField("Почта", max_length=254, unique=True)

    USERNAME_FIELD = "email"
