from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager

class User(AbstractUser):
    username = models.CharField(max_length=300, unique=True)
    aadhaar = models.CharField(max_length=12, unique=True)
    is_expert = models.BooleanField(default=False)
    objects = UserManager()

    REQUIRED_FIELDS = []