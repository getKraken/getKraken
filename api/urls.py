from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import (
  UserListCreateView,
  UserRetrieveUpdateDestroyView,
  SeriesListCreateView,
  SeriesRetrieveUpdateDestroyView,
  EventListCreateView,
  EventRetrieveUpdateDestroyView,
  GenerateDraftOrderView,
  ClaimEventAsHostView,
  GetSelfView,
)

urlpatterns = [
  path('user/', UserListCreateView.as_view(), name='user_api'),
  path('user/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='single_user_api'),
  
  path('self/', GetSelfView.as_view(), name="get_self_api"),

  path('series/', SeriesListCreateView.as_view(), name='series_api'),
  path('series/<int:pk>/', SeriesRetrieveUpdateDestroyView.as_view(), name='single_series_api'),
  path('series/<int:pk>/generate-draft-order/', GenerateDraftOrderView, name='generate_draft_order_for_single_series_api'),

  path('event/', EventListCreateView.as_view(), name='event_api'),
  path('event/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='single_event_api'),
  path('event/<int:pk>/host/', ClaimEventAsHostView, name='claim_event_as_host_api'),

  path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]