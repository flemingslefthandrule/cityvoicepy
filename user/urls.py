from django.urls import path
from .views import RegisterView, LoginView, userinfo, userposts
from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('<str:username>/', userinfo , name='userinfo'),
    path('<str:username>/posts', userposts , name='userposts')
]
