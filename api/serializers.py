from rest_framework import serializers
from .models import User, Series, Event, Subscription

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = 'id','username'

class SeriesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Series
    fields = 'id','title' 

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = 'id','series','description','owner' 

class SubscriptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Subscription
    fields = 'id','user','series'