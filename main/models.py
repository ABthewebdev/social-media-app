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

class Follower(models.Model):
    follower = models.ForeignKey(CustomUser, related_name="following_relations", on_delete=models.CASCADE)
    followed = models.ForeignKey(CustomUser, related_name="follower_relations", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'followed')

    def __str__(self):
        return f"{self.follower} follows {self.followed}"
