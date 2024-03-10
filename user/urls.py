from django.urls import path
from .views import RegisterView, LoginView, TokenRefreshView, userinfo

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<str:username>/', userinfo , name='followers_and_following')
]
