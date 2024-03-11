from rest_framework.generics import GenericAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Post, Reply
from .serializers import PostSerializer, ReplySerializer

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

    def get_queryset(self):
        postid = self.kwargs.get('postid')
        post = Post.objects.get(postid=postid)
        return post.replies.all()

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