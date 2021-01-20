from django.urls import path
from .views import (
  UserListView,
  UserCreateView,
  UserRetrieveUpdateDestroyView,
  SeriesListCreateView,
  SeriesRetrieveUpdateDestroyView,
  EventListCreateView,
  EventRetrieveUpdateDestroyView,
)

urlpatterns = [
  path('user/', UserListView.as_view(), name='user_api'),
  path('user/create/', UserCreateView.as_view(), name='user_create_api'),
  path('user/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='single_user_api'),

  path('series/', SeriesListCreateView.as_view(), name='series_api'),
  path('series/<int:pk>/', SeriesRetrieveUpdateDestroyView.as_view(), name='single_series_api'),

  path('event/', EventListCreateView.as_view(), name='event_api'),
  path('event/<int:pk>', EventRetrieveUpdateDestroyView.as_view(), name='single_event_api'),
]