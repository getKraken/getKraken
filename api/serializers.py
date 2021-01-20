from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User, Series, Event

class UserSerializer(serializers.ModelSerializer):
  # https://stackoverflow.com/questions/16857450/how-to-register-users-in-django-rest-framework
  password = serializers.CharField(write_only=True)

  def create(self, validated_data):
      user = get_user_model().objects.create_user(
          username=validated_data['username'],
          password=validated_data['password'],
          email=validated_data['email'],
      )
      return user

  class Meta:
    model = User
    fields = 'email','password','username'

class SeriesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Series
    fields = 'title','organizer','participants'

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = 'series','description','host' 

