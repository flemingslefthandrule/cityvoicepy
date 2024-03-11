from rest_framework import serializers
from .models import Post, Reply, Label

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['postid', 'author', 'title', 'body', 'label', 'created_at']
        read_only_fields = ['postid', 'created_at']

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['replyid', 'post', 'author', 'body', 'upvote', 'downvote', 'created_at', 'parent']
        read_only_fields = ['replyid', 'created_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.parent:
            representation['parent'] = ReplySerializer(instance.parent).data
        return representation

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['name']