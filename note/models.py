from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    feeling = models.CharField(max_length=50)
    score = models.IntegerField()
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title