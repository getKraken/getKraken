from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from .models import User, Series, Event
from django.contrib.auth.models import AnonymousUser
from .views import (
    SeriesListCreateView,
    SeriesRetrieveUpdateDestroyView,
    EventListCreateView,
    EventRetrieveUpdateDestroyView,
    


)

class SeriesListCreateViewTest(TestCase):

    def test_allowed(self):
        user = User.objects.create_user(username='jb', password='jb', email='jb@jb.jb')
        series = Series.objects.create(title='Spamming',organizer=user)
        series.participants.add(user)

        factory = APIRequestFactory()
        view = SeriesListCreateView.as_view()

        request = factory.get('/api/v1/series/')

        force_authenticate(request, user=user)
        response = view(request)
        data = response.data[0]

        self.assertEqual(data['title'],'Spamming')

    def test_not_allowed(self):

        user = User.objects.create_user(username='jb', password='jb', email='jb@jb.jb')
        series = Series.objects.create(title='Spamming',organizer=user)
        series.participants.add(user)

        factory = APIRequestFactory()
        view = SeriesListCreateView.as_view()

        request = factory.get('/api/v1/series/')

        force_authenticate(request, user=AnonymousUser())
        data = view(request).data

        self.assertEqual(data, [])


class SeriesRetrieveUpdateDestroyViewTest(TestCase):

    def test_retrieve(self):
        user = User.objects.create_user(username='mark', password='mark', email='mark@mark.mark')
        series = Series.objects.create(title='series1',organizer=user)

        factory = APIRequestFactory()
        view = SeriesRetrieveUpdateDestroyView.as_view()

        request = factory.get(f'/api/v1/series/{series.id}')
        force_authenticate(request, user=user)
        data = view(request, pk=series.id).data

        self.assertEqual(data['title'],'series1')
        self.assertEqual(data['participants'],[])

        series.participants.add(user)

        request = factory.get(f'/api/v1/series/{series.id}')
        force_authenticate(request, user=user)
        data = view(request, pk=series.id).data

        self.assertEqual(data['participants'][0]['username'], user.username)

    def test_update(self):
        user1 = User.objects.create_user(username='mark', password='mark', email='mark@mark.mark')
        user2 = User.objects.create_user(username='paul', password='paul', email='paul@paul.paul')
        series = Series.objects.create(title='series1',organizer=user1)
        series.participants.add(user2)

        factory = APIRequestFactory()
        view = SeriesRetrieveUpdateDestroyView.as_view()

        request = factory.put('/api/v1/series/1', {'title':'series2'})
        force_authenticate(request, user=user2)
        data = view(request, pk=series.id).data

        self.assertEqual(data['title'], 'series2')
        self.assertEqual(data['participants'][0]['username'], 'paul')

    def test_delete(self):
        user = User.objects.create_user(username='mark', password='mark', email='mark@mark.mark')
        series = Series.objects.create(title='series1',organizer=user)
        series.participants.add(user)

        factory = APIRequestFactory()
        view = SeriesRetrieveUpdateDestroyView.as_view()

        request = factory.delete('/api/v1/series/1')
        force_authenticate(request, user=user)
        data = view(request, pk=series.id).data

        self.assertEqual(data, None)


class EventListCreateViewTest(TestCase):

    def test_allowed(self):
        user = User.objects.create_user(username='mark', password='mark', email='mark@mark.mark')
        series = Series.objects.create(title='series1',organizer=user)
        series.participants.add(user)

        event = Event.objects.create(series=series, description='event1')

        factory = APIRequestFactory()
        view = EventListCreateView.as_view()

        request = factory.get('/api/v1/event/')

        force_authenticate(request, user=user)
        response = view(request)
        event = response.data[0]

        self.assertEqual(event['description'], 'event1')

    def test_not_allowed(self):

        user = User.objects.create_user(username='mark', password='mark', email='mark@mark.mark')
        series = Series.objects.create(title='series1',organizer=user)
        series.participants.add(user)

        event = Event.objects.create(series=series, description='event1')

        factory = APIRequestFactory()
        view = SeriesListCreateView.as_view()
        
        request = factory.get('/api/v1/event/')

        force_authenticate(request, user=AnonymousUser())
        response = view(request)

        self.assertEqual(response.data, [])


class EventRetrieveUpdateDestroyViewTest(TestCase):

    def test_retrieve(self):
        user = User.objects.create_user(username='mark', password='mark', email='mark@mark.mark')
        series = Series.objects.create(title='series1',organizer=user)
        series.participants.add(user)

        event = Event.objects.create(series=series, description='event1')

        factory = APIRequestFactory()
        view = EventRetrieveUpdateDestroyView.as_view()

        request = factory.get(f'/api/v1/event/{event.id}')
        force_authenticate(request, user=user)
        data = view(request, pk=event.id).data

        self.assertEqual(data['description'],'event1')
        self.assertEqual(data['series']['title'],'series1')

    def test_update(self):
        user = User.objects.create_user(username='mark', password='mark', email='mark@mark.mark')
        series = Series.objects.create(title='series1',organizer=user)
        series.participants.add(user)

        event = Event.objects.create(series=series, description='event1')

        factory = APIRequestFactory()
        view = EventRetrieveUpdateDestroyView.as_view()

        request = factory.put(f'/api/v1/event/{event.id}', { 'description':'new description'})
        force_authenticate(request, user=user)
        data = view(request, pk=event.id).data

        self.assertEqual(data['description'], 'new description')

    def test_delete(self):
        user = User.objects.create_user(username='mark', password='mark', email='mark@mark.mark')
        series = Series.objects.create(title='series1',organizer=user)
        series.participants.add(user)

        event = Event.objects.create(series=series, description='event1')

        factory = APIRequestFactory()
        view = EventRetrieveUpdateDestroyView.as_view()

        request = factory.delete(f'/api/v1/event/{event.id}')
        force_authenticate(request, user=user)
        data = view(request, pk=event.id).data

        self.assertEqual(data, None)

class 