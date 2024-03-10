from django.urls import path
from .views import CreateNewPostView

urlpatterns = [
    path('new/', CreateNewPostView.as_view(), name='create_post'),
]