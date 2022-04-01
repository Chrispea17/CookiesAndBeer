class Recommendation:
    def __init__(self, id: int, matchid: int, itemID: int, url: str):

        self.recommendationID = id
        self.uniqueUserMatchID = matchid
        self.itemID = itemID
        self.findItem = url


class Rating:
    def rateObject(ID, response):
        ratings = {"good": 1, "bad": 0}
        return ratings[response]
