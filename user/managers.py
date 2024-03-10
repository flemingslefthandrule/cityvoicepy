from django.contrib.auth.base_user import BaseUserManager
from django.db import router

class UserManager(BaseUserManager):
    def create_user(self, username, aadhaar, password=None, **extra_fields):
        user = self.model(username=username,aadhaar=aadhaar, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, aadhaar, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True.')

        user = self.create_user(username, aadhaar, password, **extra_fields)
       
        return user