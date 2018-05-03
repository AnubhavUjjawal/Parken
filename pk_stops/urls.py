from django.urls import path
from django.conf.urls import include, url
from .views import BookSpot, ExitSpot

app_name='pk_stops'

urlpatterns = [
    path('bookings/', BookSpot.as_view(), name='main_page'),
    url(r'^ExitSpot', ExitSpot, name='ExitSpot'),
]
