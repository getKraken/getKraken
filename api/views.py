from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, SeriesSerializer, EventSerializer, SubscriptionSerializer
from .models import User, Series, Event, Subscription
from .permissions import IsSelfUser
from rest_framework.permissions import IsAdminUser

# Naming convention: (Single)OBJECT(List) + CRUD-options + View

class UserListCreateView(ListCreateAPIView):
  permission_classes = (IsAdminUser, IsSelfUser)
  serializer_class = UserSerializer
  queryset = User.objects.all()

class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAdminUser, IsSelfUser)
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
