import graphene

import pk_stops.schema

class Query(pk_stops.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(pk_stops.schema.Mutation, graphene.ObjectType):
	pass 

schema = graphene.Schema(query=Query, mutation=Mutation)