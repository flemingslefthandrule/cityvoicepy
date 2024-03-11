from rest_framework.generics import GenericAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Post, Reply, Label, Poll
from .serializers import PostSerializer, ReplySerializer, PollSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from django.db.models import Q

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

class PostUpvote(APIView):
    def post(self, request, postid):
        post = get_object_or_404(Post, postid=postid)
        user = request.user
        

        if user in post.user_votes.all():
            post.upvotes -= 1
            post.user_votes.remove(user)
            return Response({'message': 'post upvote removed successfully'})

        if user in post.user_votes.all():
            post.downvotes -= 1
            post.user_votes.remove(user)


        post.upvotes += 1
        post.user_votes.add(user)
        post.save()

        return Response({'message': 'post upvoted successfully'})

class PostDownvote(APIView):
    def post(self, request, postid):
        post = get_object_or_404(Post, postid=postid)
        user = request.user

        if user in post.user_votes.all():
            post.downvotes -= 1
            post.user_votes.remove(user)
            return Response({'message': 'post upvote removed successfully'})

        if user in post.user_votes.all():
            post.upvotes -= 1
            post.user_votes.remove(user)


        post.downvotes += 1
        post.user_votes.add(user)
        post.save()

        return Response({'message': 'post downvoted successfully'})

# todo : poll

class AddPoll(APIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = PollSerializer

    def post(self, request, postid):
        post = get_object_or_404(Post, postid=postid)

        question = request.data.get('question')
        options = request.data.get('options')

        if question and options:
            poll = Poll.objects.create(question=question, post=post)
            for option_text in options:
                poll.options.create(text=option_text)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        return Response({'error': 'missing question or options'}, status=400)

class VotePoll(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, postid, option_text):
        user = request.user

        post = get_object_or_404(Post, postid=postid)
        poll = get_object_or_404(Poll, post=post)
        has_voted = poll.has_voted(poll, request.user)
        option = get_object_or_404(poll.options.all(), text=option_text)

        if not poll.has_voted(poll, user): 
            vote = PollVote.objects.create(option=option, voter=user)
            option.vote_count += 1
            option.save()

        serializer = PostSerializer(post)
        return Response(serializer.data)

class PollResults(APIView):
    def get(self, request, postid):
        post = get_object_or_404(Post, postid=postid)
        poll = get_object_or_404(Poll, post=post)

        total_votes = sum(option.vote_count for option in poll.options.all())

        serializer = PollSerializer(poll)
        data = serializer.data

        data['total_votes'] = total_votes
        for option in data['options']:
            option['vote_percentage'] = (option['vote_count'] / total_votes) * 100 if total_votes > 0 else 0

        return Response(data)

# endtodo : poll


def findpost(request, whoispost):
    posts = Post.objects.all()

    titleorbody = whoispost

    if titleorbody:
        posts = posts.filter(Q(title__icontains=titleorbody) | Q(body__icontains=titleorbody))

    post_data = [
        {
            'title': post.title,
            'body': post.body,
            'author': post.author.username,
        }
        for post in posts
    ]

    if post_data == [] :
        post_data = [
            {
                'err' : 'not found'
            }
        ] 

    return JsonResponse(post_data, safe=False)
