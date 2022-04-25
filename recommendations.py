from dataclasses import dataclass
from abc import ABC, abstractmethod, abstractproperty
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

@dataclass
class Item:
    Name: str
# this will eventually have data added like a photo


@dataclass
class User:
    userName: str
# this will eventually have data added, like first name, last name, possibly a hashed password, profile information, photo, etc

@dataclass
class Recommendation:
    def __init__(self, matchid : str, itemID: str, url: str, date: str, rating = None, reference = 0):
        self.reference = reference
        self.date = date
        self.uniqueUserMatchID = matchid
        self.itemID = itemID
        self.findItem = url
        self._recommendationRating: int = None
        self._rank = 0

    # Note SHOULD PROBABLY DECOUPLE RATING AND RECOMMENDATION IN UPDATE#
    # allows a recommendation to be rated
    def setRating(self, response: str) -> int:
        ratings = {"good": 1, "bad": 0}
        self._recommendationRating = ratings[response]


class MatchUsers:
    def __init__(self, RequesterID: str, RecommenderID: str, rank=0):
        self.reference = RequesterID + RecommenderID
        self.requester = RequesterID
        self.recommender = RecommenderID
        self._rank = 0

    def getRecommender(self, id):
        if self.reference == id:
            return self.recommender

    def getRequester(self, id):
        if self.reference == id:
            return self.requester
    
    def setRank(self, rank, id):
        if self.reference == id: 
            self._rank = rank
    






