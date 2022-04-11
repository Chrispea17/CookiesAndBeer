from numbers import Real
from dataclasses import dataclass
from abc import ABC, abstractmethod, abstractproperty


@dataclass
class Item:
    def __init__(self, id: str, item: str):
        self.itemID: str = id  # for now, I'm not sure why this wouldn't end up being an iterated iteger?
        self.itemName: str = item

    def get_item_from_id(self, id):
        if self.itemID == id:
            return self.itemName


@dataclass
class User:
    def __init__(self, id: str, Name: str):
        self.userID: str = id
        self.userName: str = Name  # if username is changes we expect userid to change too i.e."cannot change username, please make new account"

    def get_user_from_id(self, id):
        if self.userID == id:
            return self.userName


class Recommendation:
    def __init__(self, id: int, matchid: int, itemID: int, url: str):

        self.recommendationID = id
        self.uniqueUserMatchID = matchid
        self.itemID = itemID
        self.findItem = url
        self._recommendationRating: int = None
        self._rank: int = None

    # Note SHOULD PROBABLY DECOUPLE RATING AND RECOMMENDATION IN UPDATE#
    # allows a recommendation to be rated
    def setRating(self, response: str) -> int:
        ratings = {"good": 1, "bad": 0}
        self._recommendationRating = ratings[response]


class Rank:
    def __init__(self):
        self._rank: float = None
        self._count: int = None
        self._sum: int = None

    # Note SHOULD PROBABLY DECOUPLE COUNT AND RANK IN UPDATE#
    # counts # of Recommendations
    def countforRank(self, data, uniqueusermatch):
        self._count = 0
        for item in data:
            if (
                item.uniqueUserMatchID == uniqueusermatch
                and item._recommendationRating != None
            ):
                self._count += 1
        if self._count == 0:
            self._count = None

    def sumforRank(self, data, uniqueusermatch):
        self._sum = 0
        for item in data:
            if (
                item.uniqueUserMatchID == uniqueusermatch
                and item._recommendationRating != None
                and item._recommendationRating == 1
            ):
                self._sum += 1
            if self._sum == 0:
                self._sum = None

    def setRank(self, data, uniqueusermatch) -> float:
        self.sumforRank(data, uniqueusermatch)
        self.countforRank(data, uniqueusermatch)
        self._rank = self._sum / self._count


class MatchUsers:
    def __init__(self, id: int, RequesterID: int, RecommenderID: int):
        self.id = id
        self.requester = str(RequesterID)
        self.recommender = str(RecommenderID)

    def getRecommender(self, id):
        if self.id == id:
            return int(self.recommender)

    def getRequester(self, id):
        return int(self.requester)


class Outputs:
    def __init__(self) -> None:
        self._recommendersList = []
        self._rankedList = []

    def get_recommenders_with_itemID(self, recommendations, matches, ID):
        for recommendation in recommendations:
            if recommendation.itemID == ID:
                for match in matches:
                    if match.id == recommendation.uniqueUserMatchID:
                        self._recommendersList.append(match.getRecommender(match.id))
        self._recommendersList = set(self._recommendersList)

    def get_ranked_recommendations(self, recommenders, recommendations, matches, ID):
        rankedList = []
        for recommendation in recommendations:
            if recommendation.itemID == ID:
                for match in matches:
                    if match.id == recommendation.uniqueUserMatchID:
                        recommendation._rank = match._rank
                        for recommender in recommenders:
                            if recommender.userID == match.getRecommender(match.id):
                                rankedList.append(
                                    (
                                        [
                                            recommender.get_user_from_id(recommender.userID),
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
