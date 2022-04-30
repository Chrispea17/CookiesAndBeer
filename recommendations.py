from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod, abstractproperty
from sqlalchemy.ext.declarative import declarative_base
from typing import List
# Base = declarative_base()


def setRank(recommendations: List[Recommendation], matchid):
    count = 0
    sum = 0
    for recs in recommendations:
        if recs.uniqueUserMatchID==matchid and recs._recommendationRating is not None :
            count +=1
            sum+= recs._recommendationRating
    for recs in recommendations:
        recs._rank = sum/count
    return sum/count

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

    def setRank(self, rank, id):
        if self.reference == id: 
            self._rank = rank

    # Note SHOULD PROBABLY DECOUPLE RATING AND RECOMMENDATION IN UPDATE#
    # allows a recommendation to be rated
    def setRating(self, response: str) -> int:
        ratings = {"good": 1, "bad": 0}
        self._recommendationRating = ratings[response]


class MatchUsers:
    def __init__(self, RequesterID: str, RecommenderID: str, rank=0):
        self.reference = RequesterID + RecommenderID
        self.RequesterID = RequesterID
        self.RecommenderID = RecommenderID
        self._rank = rank

    def getRecommender(self, id):
        if self.reference == id:
            return self.RecommenderID

    def getRequester(self, id):
        if self.reference == id:
            return self.RequesterID
    
    def setRank(self, rank, id):
        if self.reference == id: 
            self._rank = rank
    






