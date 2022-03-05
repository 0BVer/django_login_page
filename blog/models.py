from datetime import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models


class BlogUsers(models.Model):
    username = models.CharField(max_length=32)
    password = models.TextField()
    email = models.EmailField()
    date_joined = models.DateTimeField(auto_now=True)


class Users(AbstractUser):
    user = models.ForeignKey(BlogUsers, on_delete=models.CASCADE, null=True, blank=True)
