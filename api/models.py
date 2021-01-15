from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class User(models.Model):
  username = models.CharField(max_length=64)

  def __str__(self):
    return self.username

  def get_absolute_url(self):
    return reverse("user_detail", args=[str(self.id)])


class Series(models.Model):
  title = models.CharField(max_length=64)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("series_details", args=[str(self.id)])