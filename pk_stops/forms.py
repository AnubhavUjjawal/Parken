from django.forms import ModelForm

from .models import Booking

class BookingForm(ModelForm):
	class Meta:
		model = Booking
		fields = '__all__'
		# exclude = ['booked_by']