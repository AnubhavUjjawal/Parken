from django.shortcuts import render, get_list_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.urls import reverse

from .models import Spot, Booking, Organisation
from .forms import BookingForm

# Create your views here.

class BookSpot(View):
	template_name = 'pk_spots/book_spot.html'
	form_class = BookingForm

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		prev_bookings = Booking.objects.filter(booked_by=request.user).order_by('pk')
		open_spots = Spot.objects.filter(is_booked=False)
		return render(request, self.template_name, context={ 'open_spots':open_spots, 'previous_bookings': prev_bookings })

	@method_decorator(login_required)
	def post(self):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('pk_stops:main_page'))	#redirect to this page	


class Login(View):
	template_name = "auth/login.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, context=None)

	def post(self, request, *args, **kwargs):
		print(request.POST)
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return JsonResponse({"logged_in": 1})
		
		return JsonResponse({"logged_in": 0})
		# return render(request, self.template_name, context={ err: 'Invalid Username or  Password' })	


def ExitSpot(request):
	# print(request.GET)
	license_plate = str(request.GET.get("license_plate"))
	print(license_plate)
	bookings = get_list_or_404(Booking, license_plate=license_plate)
	for booking in bookings:
		booking.delete()
	return HttpResponse("success") 

