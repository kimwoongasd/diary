from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('info/', views.info, name="info"),
    path('post/list/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete')
]