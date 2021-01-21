from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from .models import User, Series
from .views import SeriesListCreateView
from django.contrib.auth.models import AnonymousUser

class SeriesListCreateViewTest(TestCase):

    def test_allowed(self):
        user = User.objects.create_user(username="jb", password="jb", email="jb@jb.jb")
        series = Series.objects.create(title="Spamming",organizer=user)
        series.participants.add(user)

        factory = APIRequestFactory()
        view = SeriesListCreateView.as_view()

        request = factory.get('/api/v1/series/')

        force_authenticate(request, user=user)
        response = view(request)
        series = response.data[0]

        self.assertEqual(series["title"],"Spamming")

    def test_not_allowed(self):

        user = User.objects.create_user(username="jb", password="jb", email="jb@jb.jb")
        series = Series.objects.create(title="Spamming",organizer=user)
        series.participants.add(user)

        factory = APIRequestFactory()
        view = SeriesListCreateView.as_view()

        request = factory.get('/api/v1/series/')

        force_authenticate(request, user=AnonymousUser())
        response = view(request)

        self.assertEqual(response.data, [])


# class EventListCreateViewTest(TestCase):

#     def test_allowed(self):
#         user = User.objects.create_user(username="jb", password="jb", email="jb@jb.jb")
#         series = Series.objects.create(title="Spamming",organizer=user)
#         series.participants.add(user)

#         factory = APIRequestFactory()
#         view = SeriesListCreateView.as_view()

#         request = factory.get('/api/v1/series/')

#         force_authenticate(request, user=user)
#         response = view(request)
#         series = response.data[0]

#         self.assertEqual(series["title"],"Spamming")

#     def test_not_allowed(self):

#         user = User.objects.create_user(username="jb", password="jb", email="jb@jb.jb")
#         series = Series.objects.create(title="Spamming",organizer=user)
#         series.participants.add(user)

#         factory = APIRequestFactory()
#         view = SeriesListCreateView.as_view()
        
#         request = factory.get('/api/v1/series/')

#         force_authenticate(request, user=AnonymousUser())
#         response = view(request)

#         self.assertEqual(response.data, [])