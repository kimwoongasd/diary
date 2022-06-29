from django import forms
from .models import Post, User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname"]
        
    def signup(self, request, user):
        user.nickname = self.cleaned_data["nickname"]
        user.save()