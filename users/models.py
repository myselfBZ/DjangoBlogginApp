from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')
    bio = models.CharField(max_length=255, null=True)
    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"

