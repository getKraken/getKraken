from django.urls import path
from .views import (
  UserListCreateView,
  UserRetrieveUpdateDestroyView,
  SeriesListCreateView,
  SingleSeriesRetrieveUpdateDestroyView,
  EventListCreateView,
  SingleEventRetrieveUpdateDestroyView,
  SubscriptionListCreateView,
  SingleSubscriptionRetrieveUpdateDestroyView,
  GenerateDraftOrderView,
  ClaimEventAsHostView,
)

urlpatterns = [
  path('user/', UserListCreateView.as_view(), name='user_api'),
  path('user/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='single_user_api'),

  path('series/', SeriesListCreateView.as_view(), name='series_api'),
  path('series/<int:pk>/', SingleSeriesRetrieveUpdateDestroyView.as_view(), name='single_series_api'),

  path('series/<int:pk>/generate-draft-order/', GenerateDraftOrderView, name='generate_draft_order_for_single_series_api'),
  # path('series/showdraftorder/<int:pk>/', MYSTERY, name='show_draft_order_for_single_series_api'),

  path('event/', EventListCreateView.as_view(), name='event_api'),
  path('event/<int:pk>', SingleEventRetrieveUpdateDestroyView.as_view(), name='single_event_api'),

  path('event/<int:pk>/host/', ClaimEventAsHostView, name='claim_event_as_host_api'),

  path('subscription/', SubscriptionListCreateView.as_view(), name='subscription_api'),
  path('subscription/<int:pk>', SingleSubscriptionRetrieveUpdateDestroyView.as_view(), name='single_subscription_api'),

  # path('redirect/', SingleSeriesRetrieveUpdateDestroyView),
]