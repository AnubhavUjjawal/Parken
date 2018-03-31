from django.db import models
from django.contrib.auth.models import User

class Organisation(models.Model):
	org_user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	rate = models.FloatField(default=10)	#rate 10 RS per hour
	address = models.CharField(max_length=1000)

	def __str__(self):
		return self.name


class Spot(models.Model):
	org = models.ForeignKey(Organisation, on_delete=models.CASCADE)
	spot_name = models.CharField(max_length=10)
	is_booked = models.BooleanField(default=False)
	booked_from = models.DateTimeField(blank=True, null=True)
	booked_till = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.org.name + " => " + self.spot_name


class Booking(models.Model):	
	booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
	license_plate = models.CharField(max_length=20)
	spot = models.ForeignKey(Spot, on_delete=models.CASCADE)