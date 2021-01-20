from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, SeriesSerializer, EventSerializer, SubscriptionSerializer
from .models import User, Series, Event, Subscription
from django.http import HttpResponse
# TODO: from .permissions import ??? isAuthorOrReadOnly ??? and then add stuff to particular views

# Naming convention: (Single)OBJECT(List) + CRUD-options + View

class UserListCreateView(ListCreateAPIView):
  serializer_class = UserSerializer
  queryset = User.objects.all()

# TODO: User RUD

class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
  serializer_class = UserSerializer
  queryset = User.objects.all()

class SeriesListCreateView(ListCreateAPIView):
  serializer_class = SeriesSerializer
  queryset = Series.objects.all()

class SingleSeriesRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
  serializer_class = SeriesSerializer
  queryset = Series.objects.all()


class EventListCreateView(ListCreateAPIView):
  serializer_class = EventSerializer
  queryset = Event.objects.all()

class SingleEventRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
  serializer_class = EventSerializer
  queryset = Event.objects.all()


class SubscriptionListCreateView(ListCreateAPIView):
  serializer_class = SubscriptionSerializer
  queryset = Subscription.objects.all()

class SingleSubscriptionRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
  serializer_class = SubscriptionSerializer
  queryset = Subscription.objects.all()



def GenerateDraftOrderView(request):
  '''
  Overall Steps:
  When viewing a single series with all of the events and participant users added, the series organizer can click a one-time button to generate a "draft order".
  When clicked, the url is sent to the API to call a "function based view".
  The function based view retrieves the user/participants for this series using a database call and filter.
  The function based view retrieves the events for this series using a database call and filter.
  The function calls the drafting helper function (or just living inside of it as a part of this function) with the user/participant and event info.  (Event info could just be number of events... aka length.)
  The function based view calculates the draft order as an array of arrays.
    - The randomizer draft function (contained within the function based view) was created by Yoni.  Conducts only full rounds, randomizes odd rounds of draft, reverses odd rounds as the next even rounds, tries to add fairness with attempts to not repeat identical rounds, may or may not return random numbers for the leftover/remainder rounds.
    - Each inner array represents a "round" in the "draft".  Each element in an inner array represents a "pick" in that "round".
  The function stores the resulting array in the database as an attribute of the "series".
  The function sets the "round" and "pick" attributes of the "series" to 1.
  The "remainder" attribute of the "series" should be set to the value calculated by total_events-participants*rounds.
  The function based view then redirects the page to be a view that shows the overall draft order.
  The view for the overall draft order, then sends the draft order and current draft round and pick numbers to React for rendering.
    - Could possibly instead just send it to the single series review screen.
    - A test case will be done first to just show simple html message showing the function based view is being called.

  django docs about views:  https://docs.djangoproject.com/en/3.1/topics/http/views/
  Helpful terms and hints:
    - object relational mapper (ORM)  --so that we don't have to write SQL
    - Object Manager:  <ourObject>.objects

  # target_series = Series.objects.all().filter(title="Season 2021")

  # request.params.pk = pk ?
  # target_series.round += 1
  
  # target_series.save()

  '''

# Yoni's code for figuring out the draft order; will be put in here once we know the routes are connected and his inputs are available.
# import random
# import copy
# user_IDs = [1,2,3,4,5]
# event_IDs = [6,7,8,9,10]

# def random_draft(user_IDs, event_IDs):

#   full_draft = []
#   max_rounds = (len(event_IDs)//len(user_IDs))
#   while len(full_draft) < max_rounds:
#     current_order = copy.copy(user_IDs)
#     shuffle = random.shuffle(current_order)
#     if current_order not in full_draft:
#       full_draft += [current_order]
#       if len(full_draft) < max_rounds:
#         reverse_order = []
#         for i in range(len(current_order)):
#           reverse_index = len(current_order) - 1 -i
#           reverse_order += [current_order[reverse_index]]
#         full_draft += [reverse_order]
#   return full_draft

# print('one round:',random_draft(user_IDs, event_IDs))
# print('more rounds:',random_draft(user_IDs, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
# print('uneven rounds:',random_draft([1,2], [1,2,3,4,5,6,7,8,9,10,11,12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))



  html = "<html><body>The view to generate a draft order has been reached.</body></html>"
  return HttpResponse(html)