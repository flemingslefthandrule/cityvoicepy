from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager

class User(AbstractUser):
    aadhaar = models.CharField(max_length=12, unique=True)
    is_expert = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'aadhaar'
    REQUIRED_FIELDS = []