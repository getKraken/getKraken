from rest_framework import serializers
from .models import User, Series, Event

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = 'id','email','password','username'

class SeriesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Series
    fields = 'id','title','organizer','participants'

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = 'id','series','description','host' 

