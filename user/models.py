from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager

class User(AbstractUser):
    username = models.CharField(max_length=300, unique=True)
    phone = models.CharField(max_length=12, unique=True,blank=True)
    is_expert = models.BooleanField(default=False)
    following = models.ManyToManyField("self", blank=True, symmetrical=False, related_name="followed")
    
    objects = UserManager()
        
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    @property
    def get_followers(self):
        count = self.followed.all().count()
        if not count or count == 0:
            return {"no followers yet"}
        else:
            return self.followed.all()

    @property
    def get_following(self):
        count = self.following.all().count()
        if not count or count == 0:
            return {"not following anyone yet"}
        else:
            return self.following.all()