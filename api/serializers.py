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
    fields = 'id','email','password','username'

class SeriesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Series
    fields = 'id','title','organizer','participants','round','pick','remainder','draft_generation_complete','draft_complete'
    depth = 1
    # fields = 'id','title','organizer','participants','draft_order','round','pick','remainder','draft_generation_complete','draft_complete','total_rounds','total_picks'

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
    depth = 1


