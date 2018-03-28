from django.contrib import admin
from pk_stops.models import Organisation, Spot

# Register your models here.
admin.site.register([ Organisation, Spot, ])
