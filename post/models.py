from django.db import models
from user.models import User

class Label(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    label = models.ForeignKey(Label, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
