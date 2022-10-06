from dataclasses import field, fields
from django import forms
from .models import Post, ReComment, User, Comment
        
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname"]
        
    def signup(self, request, user):
        user.nickname = self.cleaned_data["nickname"]
        user.save()
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title",
    "content",
    "feeling",
    "score"]
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "nickname",
            "profile_pic",
            "intro",
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
        
        widget = {
            'content': forms.Textarea,
        }

class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = [
            "content",
        ]
        
        