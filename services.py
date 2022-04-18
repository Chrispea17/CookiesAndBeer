#There are two services that the app takes care of, one is applying a rating given be the requester to the recommendation itself
#The next is using all previous recommendations to calculate the rank of each new person giving a recommendation and including those who have never given a recommendation before


from recommendations import Recommendation


def setRating(response: str, recommendations: list[Recommendation], reference) -> int:
        for recs in recommendations:
            if recs.reference==reference:
                recs.setRating(response)
                return recs._recommendationRating

# class Rank:
#     def __init__(self):
#         self._rank: float = None
#         self._count: int = None
#         self._sum: int = None

    # counts # of Recommendations
# def countRecommendations(data: list(Recommendation), uniqueusermatch):


#     def sumforRank(self, data, uniqueusermatch):
#         self._sum = 0
#         for item in data:
#             if (
#                 item.uniqueUserMatchID == uniqueusermatch
#                 and item._recommendationRating != None
#                 and item._recommendationRating == 1
#             ):
#                 self._sum += 1
#             if self._sum == 0:
#                 self._sum = None

#     def setRank(self, data, uniqueusermatch) -> float:
#         self.sumforRank(data, uniqueusermatch)
#         self.countforRank(data, uniqueusermatch)
#         self._rank = self._sum / self._count




# # def rank():
# #     #get a list of recommendations from with a particular uniqueUserMatchID and calculate the rank of all rated recommendations
# #     #step 1

    