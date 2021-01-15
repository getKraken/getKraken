from django.contrib import admin
from .models import User, Series, Event, Subscription

# Register your models here.

admin.site.register(User)
admin.site.register(Series)
admin.site.register(Event)
admin.site.register(Subscription)
