"""
I needed to define some pseudocode for my model kind of like P&G did in APP
# Skipping the request being set out from the initial user
#1. Recommendations are made and are copied into the database
#2. The rankings for those recommendations are calculated and stored as well (this points to a refactor i need to do)
# at that point so when the initial user looks at the recommendations they should be in rank order
# The initial user will then review them and pick one to go explore (the picking of one is on the action of the user and 
#is not recorded or stored, they can review any number of them without limitation)
#3. The user will then rank the recommendation that they chose and that will be ready for the next time they ask for
#a recommendation from other users
#So in the way that I can develop the pseudocode in a similar way as the APP book
@flask.route.gubbins***
def recommendation_list_endpoint():
    #store recommendations in database as they come in
    recommendations(request.parameters)
    #load relavent recommendations from the database by their rank which can be stored at the time of recommendation (needs to be refactored)
    #list them to user via some UI
    Outputs.get_ranked_recommendations()
    #User than chooses one and rates it 0 or 1
    Recommendation.set(rating)
    #Rating gets stored and is used to calculate ranking for future set of recommendations
"""
from xmlrpc.client import DateTime
from sqlalchemy import Column, ForeignKey, Integer, String, Table, MetaData, Float, Date
from sqlalchemy.orm import relationship, mapper
from abc import *
from recommendations import Recommendation, User, Item, MatchUsers

metadata = MetaData()

recommendations = Table(
    'recommendations', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('date', Date),
    Column('matchID', String(255)),
    Column('itemID', Integer, nullable=False),
    Column('url', String(255)),  # I realize this could be larger
    Column('rating', Integer),
    Column('rank', Float),
)

items = Table(
    'items', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('Name', String(255)),
)

users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('userName', String(255)),
)

match_users = Table(
    'match_users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('RequesterID', String(255)),
    Column('RecommenderID', String(255)),
)


def start_mappers():
    match_mapper = mapper(MatchUsers, match_users)
    user_mapper = mapper(User, users)
    item_mapper = mapper(Item, items)
    recommendation_mapper = mapper(Recommendation, recommendations)
