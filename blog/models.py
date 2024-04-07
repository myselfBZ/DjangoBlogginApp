from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    