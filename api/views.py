from django.http.response import JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import AnonymousUser
from .models import User, Series, Event
from .serializers import UserSerializer, SeriesSerializer, EventSerializer
from rest_framework.permissions import IsAdminUser
from django.http.response import JsonResponse
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

class UserListCreateView(UserMixin, ListCreateAPIView):
  serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(UserMixin, RetrieveUpdateDestroyAPIView):
  serializer_class = UserSerializer


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

class SeriesListCreateView(SeriesMixin, ListCreateAPIView):
  serializer_class = SeriesSerializer

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

class EventListCreateView(EventMixin, ListCreateAPIView):
  serializer_class = EventSerializer
  
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
    random.shuffle(user_IDs)
    full_draft += [user_IDs]

    if len(full_draft) < max_rounds:
      # full_draft += [user_IDs.reverse()]
      # using the reverse method does not work, needs long version
      reverse_order = []
      for i in range(len(user_IDs)):
        reverse_index = len(user_IDs) - 1 -i
        reverse_order += [user_IDs[reverse_index]]
      full_draft += [reverse_order]

    # based on behavior seen when the conditional if statement is max_rounds-1, I think the odd rounds will always be the same.  We may need to do the copy thing Yoni has below.

  # full_draft = []
  # max_rounds = (len(event_IDs)//len(user_IDs))
  # while len(full_draft) < max_rounds:
  #   current_order = copy.copy(user_IDs)
  #   shuffle = random.shuffle(current_order)
  #   if current_order not in full_draft:
  #     full_draft += [current_order]
  #     if len(full_draft) < max_rounds:
  #       reverse_order = []
  #       for i in range(len(current_order)):
  #         reverse_index = len(current_order) - 1 -i
  #         reverse_order += [current_order[reverse_index]]
  #       full_draft += [reverse_order]
    # return full_draft


  # Jsondumps encode look up stringify store as text field
  # https://www.w3schools.com/python/python_json.asp

  # draft_order_as_json = 'pending write to json'
  # draft_order_as_json = json.dumps({"draft_order": full_draft})
  # series_of_interest.draft_order = draft_order_as_json
  # to parse the json later, use:  y = json.loads(x)
  series_of_interest.round = 1
  series_of_interest.pick = 1
  series_of_interest.remainder = remainder
  series_of_interest.draft_generation_complete = True
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
    response = {"message": "This event already has a host or has already been claimed.  Please select a different event."}
    return JsonResponse(response)
  
  # confirm it is the user's turn to claim an event
  part_of_series_pk = event_of_interest.series
  


  # update the Event in the database to assign the current user as the Host of the Event

  # increment the Pick counter by 1
  
  # if the Pick count is higher than the number of Participants, reset it to 1 and increment the Round count by 1

  # if Round count is higher than the number of draft rounds, somehow mark the draft as complete in database

  # create a response message
  figure_out_user = "USERNAME"
  figure_out_event = "EVENT-DESCRIPTION"
  round_holder = 22
  pick_holder = 22
  message_to_return = "Congrats!  " + figure_out_user + " has successfully claimed " + figure_out_event + ".  It is now the next person's turn in the draft.  We are at Pick number " + pick_holder + " of Round " + round_holder + "."
  return {"message": message_to_return}
