from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('info/', views.info, name="info"),
    path('list/', views.post_list, name='post-list'),
    path('post/<int:post_id>/', views.post_detail, name='post-detail'),
    path('post/edit/', views.post_create, name='post-create'),
]