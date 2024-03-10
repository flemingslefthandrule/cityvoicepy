from rest_framework import serializers
from .models import Post

class NewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body', 'author']