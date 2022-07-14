from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
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
    
    following = models.ManyToManyField('self', symmetrical=False, blank=True, related_name="followers")
    
    def __str__(self):
        return self.email
    
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    feeling = models.CharField(max_length=50, validators=[validate_no_numbers, validate_no_special_characters])
    score = models.IntegerField(validators=[validate_score, validate_no_special_characters])
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    
    likes = GenericRelation("Like")
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField(max_length=500, blank=False)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    
    likes = GenericRelation("Like")
    
    def __str__(self):
        return self.content[:30]
    
class Like(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    
    object_id = models.PositiveBigIntegerField()
    
    liked_object = GenericForeignKey('content_type', 'object_id')
    
    def __str__(self):
        return f"{self.user}, {self.liked_object}"