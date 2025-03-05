from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    following = models.BigIntegerField(default=0)
    followers = models.BigIntegerField(default=0)
    posts = models.BigIntegerField(default=0)

    def __str__(self):
        return self.username