#The orm sets the stage for seding the data to the db tables


from xmlrpc.client import DateTime
from sqlalchemy import Column, ForeignKey, Integer, String, Table, MetaData, Float, Date
from sqlalchemy.orm import relationship, mapper 
from abc import *
from recommendations import *

metadata = MetaData()

recommendations = Table(
    "recommendations", metadata,
    Column("reference", Integer, primary_key=True, autoincrement=True),
    Column("date", Date),
    Column("uniqueUserMatchID", String(255)),
    Column("itemID", String(255)),
    Column("findItem", String(255)),
    Column("_recommendationRating", Integer),
    Column("_rank", Float)
)

match_users = Table(
    "match_users", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("RequesterID", String(255)),
    Column("RecommenderID", String(255)),
    Column("_rank", Float),
)

items = Table(
    "items", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("Name", String(255)),
)

users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("userName", String(255)),
)


def start_mappers():
    match_mapper = mapper(MatchUsers, match_users)
    user_mapper = mapper(User, users)
    item_mapper = mapper(Item, items)
    recommendation_mapper = mapper(Recommendation, recommendations)

