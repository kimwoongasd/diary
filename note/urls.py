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
    path('post/<int:pk>/comments/create/', views.CommentCreateView.as_view(),name="comment-create"),
]