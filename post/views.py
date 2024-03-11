from rest_framework.generics import GenericAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Post, Reply, Label
from .serializers import PostSerializer, ReplySerializer
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def getlabels(request):  
    labels = Label.objects.all()

    label_data = [{
        "name" : label.name,
    } for label in labels]

    return JsonResponse(label_data, safe=False)

class CreateNewPostView(CreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostDetailView(RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'postid'

class PostUpdateView(UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'postid'

class PostDeleteView(DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'postid'

class ReplyListView(RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ReplySerializer
    lookup_field = 'postid'

    def get_queryset(self):
        postid = self.kwargs.get('postid')
        post = get_object_or_404(Post, postid=postid)
        return post.replies.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class CreateReplyView(CreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ReplySerializer

    def perform_create(self, serializer):
        postid = self.kwargs.get('postid')
        post = Post.objects.get(postid=postid)
        serializer.save(post=post)

class ReplyDetailView(RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ReplySerializer
    queryset = Reply.objects.all()
    lookup_field = 'replyid'

class ReplyUpdateView(UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ReplySerializer
    queryset = Reply.objects.all()
    lookup_field = 'replyid'

class ReplyDeleteView(DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ReplySerializer
    queryset = Reply.objects.all()
    lookup_field = 'replyid'