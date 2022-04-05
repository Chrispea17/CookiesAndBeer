from numbers import Real


class Recommendation:
    def __init__(self, id: int, matchid: int, itemID: int, url: str):

        self.recommendationID = id
        self.uniqueUserMatchID = matchid
        self.itemID = itemID
        self.findItem = url
        self._recommendationRating: int = None

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

    def setRank(self, sumratings: int, recommendationCount: int) -> float:
        self._rank = sumratings / recommendationCount


class MatchUsers:
    def __init__(self, id: int, RequesterID: int, RecommenderID: int):
        self.id = id
        self.requester = str(RequesterID)
        self.recommender = str(RecommenderID)
        self.seq: str = self.requester + "-" + self.recommender

    def getRecommender(self):
        return int(self.recommender)

    def getRequester(self):
        return int(self.requester)


###NOTE need unranked people to show somewhere###
# counts the number of recommendations from one user to another using the uniqueUserMatchID this is the first time we are looking for a psuedo repository
# def counter(ID):
#     countRecs = []
#     for (self.recommendationID = ID)
