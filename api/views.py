from rest_framework.generics import ListCreateAPIView,CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, SeriesSerializer, EventSerializer, SubscriptionSerializer
from .models import User, Series, Event, Subscription
# TODO: from .permissions import ??? isAuthorOrReadOnly ??? and then add stuff to particular views

# Naming convention: (Single)OBJECT(List) + CRUD-options + View

class UserCreateView(CreateAPIView):
  serializer_class = UserSerializer
  queryset = User.objects.all()

# TODO: User RUD



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
