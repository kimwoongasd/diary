from django import forms
from .models import Post

class PostForm(forms.ModelFoem):
    class Meta:
        model = Post
        fields = '__all__'