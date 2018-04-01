from django.contrib import admin
from pk_stops.models import Organisation, Spot, Client, Booking

# Register your models here.
admin.site.register([ Organisation, Spot, Client, Booking ])
