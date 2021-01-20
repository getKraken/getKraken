from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import AnonymousUser
from .models import User, Series, Event
from .serializers import UserSerializer, SeriesSerializer, EventSerializer
from rest_framework.permissions import IsAdminUser

# Naming convention: OBJECT(List) + CRUD-options + View

# Users
class UserMixin:
  def get_queryset(self):
    user = self.request.user
    # give all admin permissions to see everything
    if user.is_staff:
      return Series.objects.all()
    # give logged-in users the ability to see themselves as a user
    if not isinstance(user, AnonymousUser):
      return Series.objects.filter(username=user)
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
      return Series.objects.filter(organizer=user, participants__username=user)
    # not admin or logged in, you get nothing
    return None

class SeriesListCreateView(SeriesMixin, ListCreateAPIView):
  serializer_class = SeriesSerializer

class SeriesRetrieveUpdateDestroyView(SeriesMixin, RetrieveUpdateDestroyAPIView):
  serializer_class = SeriesSerializer


# Events
class EventsMixin:
  def get_queryset(self):
    user = self.request.user
    # give all admin permissions to see everything
    if user.is_staff:
      return Events.objects.all()
    # give logged-in users the ability to see what events they in if:
    # 1) are a host
    # or
    # 2) participant of a series the events is in
    if not isinstance(user, AnonymousUser):
      return Events.objects.filter(host=user, series__participants__username=user)
    # not admin or logged in, you get nothing
    return None

class EventListCreateView(ListCreateAPIView):
  serializer_class = EventSerializer

class EventRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
  serializer_class = EventSerializer
