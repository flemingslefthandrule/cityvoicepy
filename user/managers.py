from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, aadhar, password=None, **extra_fields):
        if not aadhar:
            raise ValueError('aadhar required')
        user = self.model(aadhar=aadhar, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, aadhar, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True.')

        return self.create_user(aadhar, password, **extra_fields)