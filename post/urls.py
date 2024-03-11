from django.urls import path
from . import views

urlpatterns = [
    path('labels/', views.getlabels , name='get_labels'), 
    path('', views.CreateNewPostView.as_view(), name='create_post'),
    path('<str:postid>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<str:postid>/upvote/', views.PostUpvote.as_view(), name='post_upvote'),
    path('<str:postid>/downvote/', views.PostDownvote.as_view(), name='post_downvote'),
    path('<str:postid>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<str:postid>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('<str:postid>/replies/', views.ReplyListView.as_view(), name='reply_list'),
    path('<str:postid>/replies/create/', views.CreateReplyView.as_view(), name='create_reply'),
    path('replies/<str:replyid>/', views.ReplyDetailView.as_view(), name='reply_detail'),
    path('replies/<str:replyid>/update/', views.ReplyUpdateView.as_view(), name='reply_update'),
    path('replies/<str:replyid>/delete/', views.ReplyDeleteView.as_view(), name='reply_delete'),
    path('whois/<str:whoispost>/', views.findpost, name='who_is_post')
]