from .models import Series, User, Event

all_users = User.objects.all
# print(all_users)

# this filtering part will be like Mark's filtering for printing

# which users are listed in this series
# Series.participants => turn foreign key into names
series_of_interest = 1

# users_of_this_series = User.objects.filter(?)
# users_of_this_series = Series.objects.filter(?)


# which events are a part of this series

#how get series id?
series_of_interest = 1
events_of_series_of_interest = Event.objects.filter(series=series_of_interest)

#return an array of arrays of draft order, ex. [ [ 1, 2, 3, 4], [4, 3, 2, 1], [2, 3, 4, 1,],[1, 4, 3, 2]]