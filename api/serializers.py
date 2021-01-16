from rest_framework import serializers
from .models import User, Series, Event, Subscription

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = 'id','username'

class SeriesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Series
    fields = 'id','title','organizer' 

#  NOTE: this is used to take the foreign keys in the table and convert them to usernames, series names, or event-series relations (or other relationships)

# class EventField(serializers.RelatedField):

#     def to_representation(self, obj):
#         return {
#             'id': obj.id,
#             'name': obj.name,
#         }

#     def to_internal_value(self, data):
#         try:
#             try:
#                 obj_id = data['id']
#                 return Obj.objects.get(id=obj_id)
#             except KeyError:
#                 raise serializers.ValidationError(
#                     'id is required'
#                 )
#         except Obj.DoesNotExist:
#             raise serializers.ValidationError(
#                 'Obj does not exist'
#                 )

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = 'id','series','description','host' 

class SubscriptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Subscription
    fields = 'id','user','series'
