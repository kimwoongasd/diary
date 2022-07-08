from django import forms
from .models import Post, User
        
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
