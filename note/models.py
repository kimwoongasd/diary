from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_numbers, validate_score, validate_no_special_characters

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        validators=[validate_no_special_characters],
        error_messages={"unique": "이미 사용중인 닉네임입니다."},
        )
    
    profile_pic = models.ImageField(default="default_profile_pic.jpg", upload_to="profile_pics")
    intro = models.TextField(blank=True)
    
    def __str__(self):
        return self.email
    
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    feeling = models.CharField(max_length=50, validators=[validate_no_numbers, validate_no_special_characters])
    score = models.IntegerField(validators=[validate_score, validate_no_special_characters])
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    