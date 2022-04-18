from numbers import Real
from dataclasses import dataclass
from abc import ABC, abstractmethod, abstractproperty


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
    def __init__(self, matchid : str, itemID: str, url: str, date: str, rating = None, rank =0, reference = 0):
        self.reference = reference
        self.date = date
        self.uniqueUserMatchID = matchid
        self.itemID = itemID
        self.findItem = url
        self._recommendationRating: int = None
        self._rank: int = 0  # new users get initialized to zero so for now go to the bottom of the list, but future would like to keep them separate
        #I am realizing now that rank doesn't belong with the ratings (otherwise you will get repeated data in the database, so)
        #we want to refactor to the matched users but that also couples Matched users and recommendations. 

    # Note SHOULD PROBABLY DECOUPLE RATING AND RECOMMENDATION IN UPDATE#
    # allows a recommendation to be rated
    def setRating(self, response: str) -> int:
        ratings = {"good": 1, "bad": 0}
        self._recommendationRating = ratings[response]


class MatchUsers:
    def __init__(self, RequesterID: str, RecommenderID: str):
        self.reference = RequesterID + RecommenderID
        self.requester = RequesterID
        self.recommender = RecommenderID

    def getRecommender(self, id):
        if self.reference == id:
            return self.recommender

    def getRequester(self, id):
        if self.reference == id:
            return self.requester


class Outputs:
    def __init__(self) -> None:
        self._recommendersList = []
        self._rankedList = []

    def get_recommenders_with_same_item(self, recommendations, matches, ID):
        for recommendation in recommendations:
            if recommendation.itemID == ID:
                for match in matches:
                    if match.reference == recommendation.uniqueUserMatchID:
                        self._recommendersList.append(
                            match.getRecommender(match.reference))
        self._recommendersList = set(self._recommendersList)

    def get_ranked_recommendations(self, recommenders, recommendations, matches, item, requesterID):
        rankedList = []
        for recommendation in recommendations:
            if recommendation.itemID == item: #i should switch searching for user match before item for processing, but later
                for match in matches:
                    if match.reference == recommendation.uniqueUserMatchID and match.requester == requesterID:
                        recommendation._rank = match._rank
                        for recommender in recommenders:
                            if recommender.userName == match.getRecommender(match.reference):
                                rankedList.append(
                                    (
                                        [
                                            recommender.userName,
                                            recommendation.itemID,
                                            recommendation.findItem,
                                        ],
                                        recommendation._rank,
                                    )
                                )
        rankedList.sort(key=lambda y: y[1], reverse=True)
        self._rankedList = [y[0] for y in rankedList]
        print(self._rankedList)

    def print_ranked_recommendations(self):
        for items in self._rankedList:
            print(items)


