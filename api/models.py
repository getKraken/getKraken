from django.db import models
from django.contrib.auth import get_user_model

class User(models.Model):
  username = models.CharField(max_length=64)

  def __str__(self):
    return self.username

class Series ()