from django.db import models
from user.models import User
import uuid

class Label(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    postid = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    label = models.ManyToManyField("Label", blank=True, symmetrical=False, related_name="posts_with_label")
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        unique_string = f"{self.author.username}-{str(uuid.uuid4())}"
        self.postid = unique_string
        super().save(*args, **kwargs)

class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='nested_replies')
    replyid = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"reply to {self.post.title} by {self.author.username}"

    def save(self, *args, **kwargs):
        unique_string = f"{self.author.id}-{str(self.created_at)}"
        self.replyid = unique_string
        super().save(*args, **kwargs)