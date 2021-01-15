from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CustomUser

class User(CustomUser):
  username = models.CharField(max_length=64)

  def __str__(self):
    return self.username

class Series(models.Model):
  title = models.CharField(max_length=64)

  def __str__(self):
    return self.title

class Event(models.Model):
  description = models.CharField(max_length=64)
  # TODO: unsure about the SET_NULL, could possibly use RESTRICT
  series = models.ForeignKey('Series', on_delete=models.CASCADE)
  # TODO = 
  owner = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return f"The event {self.description} is a part of the {self.series} and has been claimed by {self.owner}"

class Subscription(models.Model):

  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  series = models.ForeignKey('Series', on_delete=models.CASCADE)

  def __str__(self):
    return f"User {self.user} has been subscribed to the series {self.series}."