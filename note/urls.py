from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('info/', views.info, name="info"),
    path('list/', views.post_list, name='post-list'),
    path('post/<int:post_id>/', views.post_detail, name='post-detail'),
    path('post/new/', views.post_create, name='post-create'),
    path('post/<int:post_id>/update/', views.post_update, name='post-update'),
    path('post/<int:post_id>/delete/', views.post_delete, name='post-delete')
]