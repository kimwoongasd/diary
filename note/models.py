from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_hash, validate_no_numbers, validate_score

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, validators=[validate_no_hash])
    content = models.TextField(validators=[validate_no_hash])
    feeling = models.CharField(max_length=50, validators=[validate_no_hash, validate_no_numbers])
    score = models.IntegerField(validators=[validate_score])
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class User(AbstractUser):
    nickname = models.CharField(max_length=20, unique=True, null=True)
    
    def __str__(self):
        return self.email