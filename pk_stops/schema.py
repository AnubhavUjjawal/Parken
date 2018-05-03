import graphene
from graphene import relay, ObjectType, InputObjectType, ClientIDMutation
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Organisation, Spot, Booking, User, Client
from .helper import update_create_instance


class UserNode(DjangoObjectType):
	class Meta:
		model = User
		filter_fields = ['username', 'email', 'organisation__name', 'organisation__id', 'organisation__rate']
		interfaces = (relay.Node, )


class OrganisationNode(DjangoObjectType):
	class Meta:
		model = Organisation
		filter_fields = ['org_user__username', 'name', 'rate', 'address', 'org_user__email', 'lat', 'lon']
		interfaces = (relay.Node, )


class SpotNode(DjangoObjectType):
	class Meta:
		model = Spot
		# filter_fields = [ 'spot_name', 'org__name', 'org__rate', 'org__address', 'booking__booked_till', 'booking__booked_from']
		filter_fields = {
			'spot_name' : ['exact'],
			'org__name' : ['exact'],
			'org__rate' : ['exact'],
			'org__address': ['exact', 'icontains'],
			'booking__booked_till': ['lte', 'gte'],
			'booking__booked_from': ['gte', 'lte'],
			# 'booking__booked_till_time': ['lte', 'gte'],
			# 'booking__booked_from_time': ['gte', 'lte'],
		}
		interfaces = (relay.Node, )


class BookingNode(DjangoObjectType):
	class Meta:
		model = Booking
		filter_fields = ['booked_by__username', 'booked_by__id', 'booked_from', 'booked_till', 'spot__org__name', 'spot__org__address', 'license_plate', 'spot__spot_name']
		interfaces = (relay.Node, )


class ClientNode(DjangoObjectType):
	class Meta:
		model = Client
		filter_fields = ['name', 'age']
		interfaces = (relay.Node, )


class Query(object):
	user = relay.Node.Field(UserNode)
	all_users = DjangoFilterConnectionField(UserNode)

	organisation = relay.Node.Field(OrganisationNode)
	all_organisations = DjangoFilterConnectionField(OrganisationNode)

	spot = relay.Node.Field(SpotNode)
	all_spots = DjangoFilterConnectionField(SpotNode)

	booking = relay.Node.Field(BookingNode)
	all_bookings = DjangoFilterConnectionField(BookingNode)

	client = relay.Node.Field(ClientNode)
	all_clients = DjangoFilterConnectionField(ClientNode)


class CreateOrganisation(ClientIDMutation):
	organisation = graphene.Field(OrganisationNode)
	class Input:
		name = graphene.String()
		username = graphene.String()
		rate = graphene.Float()
		address = graphene.String()

	@classmethod
	def mutate_and_get_payload(cls, context, info, **input):
		temp = Organisation(
			name = input.get('name'),
			org_user = User.objects.get(username = input.get('username')),
			rate = input.get('rate'),
			address = input.get('address'),
			lat = input.get('lat'),
			lon = input.get('lon')
		)
		temp.save()
		return CreateOrganisation(organisation=temp)


class CreateSpot(ClientIDMutation):
	spot = graphene.Field(SpotNode)
	class Input:
		spot_name = graphene.String()
		username = graphene.String()

	@classmethod
	def mutate_and_get_payload(cls, context, info, **input):
		# print(**input)
		temp = Spot(
					spot_name = input.get('spot_name'),
					org = Organisation.objects.get(
					org_user = User.objects.get(username=input.get('username'))
				)
		)
		temp.save()
		return CreateSpot(spot=temp)	


class CreateBooking(ClientIDMutation):
	booking = graphene.Field(BookingNode)
	class Input:
		license_plate = graphene.String()
		spot_name = graphene.String()
		booked_from = graphene.DateTime()
		booked_till = graphene.DateTime()
		phone_no = graphene.String()
		username = graphene.String()
		name = graphene.String()

	@classmethod
	def mutate_and_get_payload(cls, context, info, **input):
		temp = Booking(
					license_plate = input.get('license_plate'),
					spot = Spot.objects.get(spot_name=input.get('spot_name'),	
								org = Organisation.objects.get(name=input.get('name'))
							),
					booked_from = input.get('booked_from'),
					booked_till = input.get('booked_till'),
					phone_no = input.get('phone_no'),
					booked_by = User.objects.get(username=input.get('username')),
				)
		temp.save()
		return CreateBooking(booking=temp)			

class Mutation(graphene.ObjectType):
	# create_client = CreateClient.Field()
	create_organisation = CreateOrganisation.Field()
	create_spot = CreateSpot.Field()
	create_booking = CreateBooking.Field()	

