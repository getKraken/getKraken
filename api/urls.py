from django.urls import path
from .views import (
  UserCreateView,
  SeriesListCreateView,
  SingleSeriesRetrieveUpdateDestroyView,
  EventListCreateView,
  SingleEventRetrieveUpdateDestroyView,
  SubscriptionListCreateView,
  SingleSubscriptionRetrieveUpdateDestroyView,
)

urlpatterns = [
  path('user/', UserCreateView.as_view(), name='user_api'),
  path('series/', SeriesListCreateView.as_view(), name='series_api'),
  path('series/<int:pk>/', SingleSeriesRetrieveUpdateDestroyView.as_view(), name='single_series_api'),
  path('event/', EventListCreateView.as_view(), name='event_api'),
  path('event/<int:pk>', SingleEventRetrieveUpdateDestroyView.as_view(), name='single_event_api'),
  path('subscription/', SubscriptionListCreateView.as_view(), name='subscription_api'),
  path('subscription/<int:pk>', SingleSubscriptionRetrieveUpdateDestroyView.as_view(), name='single_subscription_api'),
]