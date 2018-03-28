from django.db import models
from django.contrib.auth.models import User

class Organisation(models.Model):
	org_user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	rate = models.FloatField(default=10)	#rate 10 RS per hour
	address = models.CharField(max_length=1000)


class Spot(models.Model):
	org = models.ForeignKey(Organisation, on_delete=models.CASCADE)
	is_booked = models.BooleanField(default=False)
	booked_from = models.DateTimeField()
	booked_till = models.DateTimeField()

class Booking(models.Model):	
	booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
	license_plate = models.CharField(max_length=20)
	spot = models.ForeignKey(Spot, on_delete=models.CASCADE)