from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import IntegerField
from accounts.models import CustomUser
from django.contrib.postgres.fields.array import ArrayField

class User(CustomUser):
  # username = models.CharField(max_length=64)

  def __str__(self):
    return self.username

class Series(models.Model):
  title = models.CharField(max_length=64)
  organizer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

  draft_order = ArrayField(
    ArrayField(
      models.IntegerField(blank=True, null=True)
    )
    )
  round = models.IntegerField(blank=True, null=True)
  pick = models.IntegerField(blank=True, null=True)
  remainder = models.IntegerField(blank=True, null=True)
  draft_generation_complete = models.BooleanField(default=False)
  draft_complete = models.BooleanField(default=False)


  def __str__(self):
    return f"The Series {self.title} is organized by {self.organizer}."

class Event(models.Model):
  description = models.CharField(max_length=64)
  # TODO: unsure about the SET_NULL, could possibly use RESTRICT
  series = models.ForeignKey('Series', on_delete=models.CASCADE)
  # TODO = 
  host = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return f"The event {self.description} is a part of the {self.series} and has been claimed by {self.host}"

class Subscription(models.Model):

  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  series = models.ForeignKey('Series', on_delete=models.CASCADE)

  def __str__(self):
    return f"User {self.user} has been subscribed to the series {self.series}."
