class Recommendation:
    def __init__(self, id, matchid, itemID, url):

        self.recommendationID = id
        self.uniqueUserMatchID = matchid
        self.itemID = itemID
        self.findItem = url
        # self._recommendationRating = None
        self._recommendationRating: int = None
        
    ###NOTE SHOULD PROBABLY DECOUPLE RATING AND RECOMMENDATION IN UPDATE###
    # allows a recommendation to be rated
    def setRating(self, response) -> int:
        ratings = {"good": 1, "bad": 0}
        # return ratings[response]
        self._recommendationRating = ratings[response]
        return self._recommendationRating

    # counts the number of recommendations from one user to another using the uniqueUserMatchID this is the first time we are looking for a psuedo repository
    # def counter(ID):
    #     countRecs = []
    #     for (self.recommendationID = ID)
