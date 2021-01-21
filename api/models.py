from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CustomUser

class User(CustomUser):
  def __str__(self):
    return self.username

class Series(models.Model):
  title = models.CharField(max_length=64)
  participants = models.ManyToManyField(get_user_model())
  organizer = models.ForeignKey(get_user_model(), related_name="organizer", on_delete=models.CASCADE)

  def __str__(self):
    return f"The Series {self.title} is organized by {self.organizer}."

class Event(models.Model):
  description = models.CharField(max_length=64)
  series = models.ForeignKey(Series, on_delete=models.CASCADE)
  # TODO: unsure about the SET_NULL, could possibly use RESTRICT
  host = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return f"The event {self.description} is a part of the {self.series} and has been claimed by {self.host}"
