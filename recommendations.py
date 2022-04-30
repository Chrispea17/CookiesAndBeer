from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod, abstractproperty
from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()


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
    def __init__(self, matchid : str, itemID: str, url: str, date: str, rating = None, reference = 0 , rank = 0):
        self.reference = reference
        self.date = date
        self.uniqueUserMatchID = matchid
        self.itemID = itemID
        self.findItem = url
        self._recommendationRating: int = rating
        self._rank = rank

    def __repr__(self):
        return f"Recommendation {self.reference}"

    def __eq__(self, other):
        if not isinstance(other,Recommendation):
            return False
        return other.reference == self.reference

    def __hash__(self):
        return hash(self.reference)

    def __gt__(self, other):
        if self._rank is None:
            return False
        if other._rank is None:
            return True
        return self._rank > other._rank

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
        self._rank = rank

    def getRecommender(self, id):
        if self.reference == id:
            return self.recommender

    def getRequester(self, id):
        if self.reference == id:
            return self.requester
    
    def setRank(self, rank, id):
        if self.reference == id: 
            self._rank = rank
    






