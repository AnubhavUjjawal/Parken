import graphene
from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Organisation, Spot, Booking, User


class UserType(DjangoObjectType):
	class Meta:
		model = User
		filter_fields = ['username', 'email', 'organisation__name', 'organisation__id', 'organisation__rate']
		interfaces = (relay.Node, )


class OrganisationType(DjangoObjectType):
	class Meta:
		model = Organisation
		filter_fields = ['org_user__username', 'name', 'rate', 'address']
		interfaces = (relay.Node, )

class SpotType(DjangoObjectType):
	class Meta:
		model = Spot
		filter_fields = ['is_booked', 'booked_from', 'booked_till', 'spot_name', 'org__name', 'org__rate', 'org__address']
		interfaces = (relay.Node, )

class BookingType(DjangoObjectType):
	class Meta:
		model = Booking
		# filter_fields = ['is_booked', 'booked_from', 'booked_till', 'spot_name', 'org__name', 'org__rate', 'org__address']
		# interfaces = (relay.Node, )

class Query(object):
	user = relay.Node.Field(UserType)
	all_users = DjangoFilterConnectionField(UserType)

	organisation = relay.Node.Field(OrganisationType)
	all_organisations = DjangoFilterConnectionField(OrganisationType)

	spot = relay.Node.Field(SpotType)
	all_spots = DjangoFilterConnectionField(SpotType)
	# all_organisations = graphene.List(OrganisationType)
	# all_spots = graphene.List(SpotType)
	# all_users = graphene.List(UserType)
		
	# def resolve_all_users(self, info, **kwargs):
	# 	return User.objects.all()

	# def resolve_all_organisations(self, info, **kwargs):
	# 	return Organisation.objects.all()

	# def resolve_all_spots(self, info, **kwargs):
	# 	return Spot.objects.select_related('org').all()
