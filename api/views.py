from rest_framework.generics import ListCreateAPIView,CreateAPIView
from .serializers import UserSerializer

from .models import User, Series
from django.urls import reverse_lazy


class CreateUserView(CreateAPIView):
  serializer_class = UserSerializer

class CreateSeriesView(CreateAPIView):
    serializer_class = 
  