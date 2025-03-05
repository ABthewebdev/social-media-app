from django.db import models
from register.models import CustomUser

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    text = models.TextField()
    comments = models.BigIntegerField(default=0)
    likes = models.BigIntegerField(default=0)

    def __str__(self):
        return self.headline
