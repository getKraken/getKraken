from django.contrib.auth import get_user
from django.http.response import JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import AnonymousUser
from .models import User, Series, Event
from .serializers import UserSerializer, SeriesSerializer, EventSerializer
from rest_framework.permissions import IsAdminUser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import random
import copy
import json

# Naming convention: OBJECT(List) + CRUD-options + View

# Users
class UserMixin:
  def get_queryset(self):
    user = self.request.user
    # give all admin permissions to see everything
    if user.is_staff:
      return User.objects.all()
    # give logged-in users the ability to see themselves as a user
    if not isinstance(user, AnonymousUser):
      return User.objects.filter(username=user.username)
    # not admin or logged in, you get nothing
    return None

@method_decorator(csrf_exempt, name='dispatch')
class UserListCreateView(UserMixin, ListCreateAPIView):
  serializer_class = UserSerializer

@method_decorator(csrf_exempt, name='dispatch')
class UserRetrieveUpdateDestroyView(UserMixin, RetrieveUpdateDestroyAPIView):
  serializer_class = UserSerializer

@method_decorator(csrf_exempt, name='dispatch')
class GetSelfView(ListCreateAPIView):
  serializer_class = UserSerializer

  def get_queryset(self):
    user = self.request.user
      
    return User.objects.filter(username=user.username)


# Series
class SeriesMixin:
  def get_queryset(self):
    user = self.request.user
    # give all admin permissions to see everything
    if user.is_staff:
      return Series.objects.all()
    # give logged-in users the ability to see what they are an organizer or particpant of
    if not isinstance(user, AnonymousUser):
      series_organizer = Series.objects.filter(organizer__username=user.username)
      series_participant = Series.objects.filter(participants__username=user.username)
      return series_organizer.union(series_participant)
    # not admin or logged in, you get nothing
    return None

@method_decorator(csrf_exempt, name='dispatch')
class SeriesListCreateView(SeriesMixin, ListCreateAPIView):
  serializer_class = SeriesSerializer

@method_decorator(csrf_exempt, name='dispatch')
class SeriesRetrieveUpdateDestroyView(SeriesMixin, RetrieveUpdateDestroyAPIView):
  serializer_class = SeriesSerializer


# Events
class EventMixin:
  def get_queryset(self):
    user = self.request.user
    # give all admin permissions to see everything
    if user.is_staff:
      return Event.objects.all()
    # give logged-in users the ability to see what events they in if:
    # 1) are a host
    # or
    # 2) participant of a series the events is in
    if not isinstance(user, AnonymousUser):
      event_host = Event.objects.filter(host__username=user.username)
      event_in_series = Event.objects.filter(series__participants__username=user.username)
      return event_host.union(event_in_series)
    # not admin or logged in, you get nothing
    return None

@method_decorator(csrf_exempt, name='dispatch')
class EventListCreateView(EventMixin, ListCreateAPIView):
  serializer_class = EventSerializer

@method_decorator(csrf_exempt, name='dispatch')
class EventRetrieveUpdateDestroyView(EventMixin, RetrieveUpdateDestroyAPIView):
  serializer_class = EventSerializer


def GenerateDraftOrderView(request, pk):

  series_of_interest = Series.objects.get(id=pk)
  participants_of_series = series_of_interest.participants
  number_of_participants = participants_of_series.count()

  events_in_this_series = Event.objects.filter(series=pk)
  number_of_events_in_this_series = events_in_this_series.count()

  user_IDs = [user.id for user in participants_of_series.iterator()]

  full_draft = []
  max_rounds = (number_of_events_in_this_series//number_of_participants)
  remainder = number_of_events_in_this_series % number_of_participants

  while len(full_draft) < max_rounds:
    current_order = copy.copy(user_IDs)
    random.shuffle(current_order)
    full_draft += [current_order]

    if len(full_draft) < max_rounds:
      reverse_order = []
      for i in range(len(current_order)):
        reverse_index = len(current_order) - 1 -i
        reverse_order += [current_order[reverse_index]]
      full_draft += [reverse_order]

  # Jsondumps encode look up stringify store as text field
  # https://www.w3schools.com/python/python_json.asp

  # draft_order_as_json = 'pending write to json'
  draft_order_as_json = json.dumps({"draft_order": full_draft})
  series_of_interest.draft_order = draft_order_as_json
  # to parse the json in python, use:  y = json.loads(x)
  # to parse the json in javascript, use: const obj = JSON.parse(json)
  series_of_interest.round = 1
  series_of_interest.pick = 1
  series_of_interest.remainder = remainder
  series_of_interest.draft_generation_complete = True
  # series_of_interest.total_rounds = max_rounds
  # series_of_interest.total_picks = number_of_participants
  series_of_interest.save()


  '''
  POSSIBLE HELPFUL INFO AND SOURCES:
  django docs about views:  https://docs.djangoproject.com/en/3.1/topics/http/views/
  Helpful terms and hints:
    - object relational mapper (ORM)  --so that we don't have to write SQL
    - Object Manager:  <ourObject>.objects

  example pseudo code:
  # target_series = Series.objects.all().filter(title="Season 2021")
  # request.params.pk = pk ?
  # target_series.round += 1
  # target_series.save()
  '''


  message_to_return = "The draft order has been calculated.  There will be " + str(remainder) + " game(s) not included in the draft.  Visit the individual Series page to view the draft order... The draft order array of array: " + str(full_draft)
  response = {"message": message_to_return, "status_code": 200}
  return JsonResponse(response)



def ClaimEventAsHostView(request, pk):
  # confirm the event is currently available
  event_of_interest = Event.objects.get(id=pk)
  if event_of_interest.host:
    message_to_return = "This event already has a host or has already been claimed.  Please select a different event."
    response = {"message": message_to_return, "status_code": 200}
    return JsonResponse(response)
  
  # confirm it is the user's turn to claim an event
  part_of_series_pk = event_of_interest.series
  series_of_interest = Series.objects.get(id=part_of_series_pk)
  y = json.loads(series_of_interest.draft_order)
  draft_order_as_array = y.draft_order

  # how can we figure out which user requested this?
  user = get_user()

  if draft_order_as_array[series_of_interest.round][series_of_interest.pick] != user.id:
    message_to_return = "It is not your turn to claim to host or attend an event.  Please be patient and wait your turn."
    response = {"message": message_to_return, "status_code": 200}
    return JsonResponse(response)

  # update the Event in the database to assign the current user as the Host of the Event
  event_of_interest.host = user.id
  event_of_interest.save()

  # increment the Pick counter by 1. If the Pick count is higher than the number of Participants, reset it to 1 and increment the Round count by 1
  pick = series_of_interest.pick

  participants_of_series = series_of_interest.participants
  number_of_participants = participants_of_series.count()

  if pick+1 <= number_of_participants:
    series_of_interest.pick += 1
    series_of_interest.save()
  else:
    series_of_interest.round += 1
    series_of_interest.pick = 1
    series_of_interest.save()

  # if Round count is higher than the number of draft rounds, mark the draft as complete in database
  events_in_this_series = Event.objects.filter(series=part_of_series_pk)
  number_of_events_in_this_series = events_in_this_series.count()

  max_rounds = (number_of_events_in_this_series//number_of_participants)

  if series_of_interest.round > max_rounds:
    series_of_interest.draft_complete = True
    series_of_interest.save()

    message_to_return = "This was the final pick of the draft.  Enjoy the events!"
    response = {"message": message_to_return, "status_code": 200}
    return JsonResponse(response)


  # response for a typical pick
  message_to_return = "Congrats!  " + str(user.username) + " has successfully claimed " + str(event_of_interest.description) + ".  It is now the next person's turn in the draft.  We are at Pick number " + str(series_of_interest.pick) + " of Round " + str(series_of_interest.round) + "."
  response = {"message": message_to_return, "status_code": 200}
  return JsonResponse(response)
