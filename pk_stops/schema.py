import graphene

from graphene_django.types import DjangoObjectType
from .models import Organisation, Spot, Booking, User


class UserType(DjangoObjectType):
	class Meta:
		model = User


class OrganisationType(DjangoObjectType):
	class Meta:
		model = Organisation


class SpotType(DjangoObjectType):
	class Meta:
		model = Spot


class BookingType(DjangoObjectType):
	class Meta:
		model = Booking


class Query(object):
	all_organisations = graphene.List(OrganisationType)
	all_spots = graphene.List(SpotType)
	all_users = graphene.List(UserType)

	def resolve_all_users(self, info, **kwargs):
		return User.objects.all()

	def resolve_all_organisations(self, info, **kwargs):
		return Organisation.objects.all()

	def resolve_all_spots(self, info, **kwargs):
		return Spot.objects.select_related('org').all()
