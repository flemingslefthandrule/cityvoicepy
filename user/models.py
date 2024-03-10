from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager

class User(AbstractUser):
    username = models.CharField(max_length=300, unique=True)
    phone = models.CharField(max_length=12, unique=True,blank=True)
    is_expert = models.BooleanField(default=False)
    followers = models.ManyToManyField('self', related_name='users_who_are_following_me')
    followering = models.ManyToManyField('self', related_name='the_people_i_am_currently_following')
    
    objects = UserManager()
        
    REQUIRED_FIELDS = []