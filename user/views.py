from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserSerializer, TokenRefreshSerializer
from .models import User
from post.models import Post

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if username is None or password is None:
            return Response({'error': 'please provide both username and password.'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'invalid phone number or password.'},
                            status=status.HTTP_401_UNAUTHORIZED)

# class ProfileView():
 

def userinfo(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({'error': 'user not found'}, status=404)

    followers = [{'username': follower.username, 'is_expert': follower.is_expert} for follower in user.get_followers]
    following = [{'username': following_user.username, 'is_expert': following_user.is_expert} for following_user in user.get_following]



    user_data = {
        'username': user.username,
        'is_expert': user.is_expert,
        'followers': followers,
        'following': following
    }

    return JsonResponse(user_data, safe=False)


def userposts(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({'error': 'user not found'}, status=404)
    
    posts = Post.objects.filter(author=user)

    post_data = [{
        "title" : post.title,
        "body" : post.body,
        "label" : post.label,
        "created_at" : post.created_at,
    } for post in posts]

    return JsonResponse(post_data, safe=False)

@login_required
def follow(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    user = request.user
    if user in user_to_follow.followers.all():
        return JsonResponse({"follow":"already following"})
    else:
        user.following.add(user_to_follow)

    return JsonResponse({"follow":"sucessful"})