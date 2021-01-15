from rest_framework.generics import ListCreateAPIView,CreateAPIView
from .serializers import UserSerializer

class CreateUserView(CreateAPIView):
  serializer_class = UserSerializer

  