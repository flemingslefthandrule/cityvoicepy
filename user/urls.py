from django.urls import path
from .views import RegisterView, LoginView, LogoutView, userinfo, userposts, follow , unfollow, usertagged
from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name ='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('<str:username>/', userinfo , name='userinfo'),
    path('<str:username>/posts', userposts , name='userposts'), 
    path('<str:username>/follow', follow , name='follow_user'),
    path('<str:username>/unfollow', unfollow , name='unfollow_user'),
    path('<str:username>/tagged', usertagged , name='usertagged'),
]
