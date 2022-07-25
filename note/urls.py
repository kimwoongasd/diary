from django.urls import path
from . import views

urlpatterns = [
    # post
    path('', views.index, name="index"),
    path('info/', views.info, name="info"),
    path('post/list/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    
    # profile
    path('profile/<int:user_id>/', views.ProfileView.as_view(), name="profile"),
    path('profile/<int:user_id>/post/', views.UserPostListView.as_view(), name="user-post-list"),
    path('update-profile/', views.ProfileUpdateForm.as_view(), name="profile-update"),
    
    # comment
    path('post/<int:pk>/comments/create/', views.CommentCreateView.as_view(), name="comment-create"),
    path('post/<int:comment_id>/comments/update/', views.CommentUpdateView.as_view(), name="comment-update"),
    path('post/<int:comment_id>/comments/delete/', views.CommentDeleteView.as_view(), name="comment-delete"),
    
    # like
    path('post/like/<int:content_type_id>/<int:object_id>/', views.ProcessLikeView.as_view(), name="process-like"),
    
    # follow
    path('post/users/<int:user_id>/follow/', views.ProcessFollowView.as_view(), name="process-follow"),
    path('post/users/<int:user_id>/following/', views.FollowingListView.as_view(), name="following-list"),
    path('post/users/<int:user_id>/followers/', views.FollowerListView.as_view(), name="followers-list"),
]