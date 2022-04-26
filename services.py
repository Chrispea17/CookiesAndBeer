# There are two services that the app takes care of, one is applying a rating given be the requester to the recommendation itself
# The next is using all previous recommendations to calculate the rank of each new person giving a recommendation and including those who have never given a recommendation before


from difflib import Match
from recommendations import Recommendation, MatchUsers, User
import unitofwork

def setRating(response: str, data: list[Recommendation], reference) -> int:
    for recs in data:
        if (recs.reference == reference):
            recs.setRating(response)
            return recs._recommendationRating


def countRecommendationsForMatch(data: list[Recommendation], uniqueUserMatch):
    count = 0
    for item in data:
        if (
            item.uniqueUserMatchID == uniqueUserMatch
            and item._recommendationRating != None
        ):
            count += 1
    if count == 0:
        count = None
    return count


def sumRatings(data: list[Recommendation], uniqueusermatch):
    sum = 0
    for item in data:
        if (
            item.uniqueUserMatchID == uniqueusermatch
            and item._recommendationRating != None
            and item._recommendationRating == 1
        ):
            sum += 1
        if sum == 0:
            sum = None
    return sum


def setRank(data: list[Recommendation], id):
    sum = sumRatings(data, id)
    count = countRecommendationsForMatch(data, id)
    rank = sum / count
    return rank

def getRecommendersForItem(recs : list[Recommendation], matches : list[MatchUsers], ItemId):
    recommendersList = []
    for recommendation in recs:
        if recommendation.itemID == ItemId:
            for match in matches:
                if match.reference == recommendation.uniqueUserMatchID:
                    recommendersList.append(
                        match.getRecommender(match.reference))
    recommendersList = set(recommendersList)
    return recommendersList


def getRankedRecommendations(recommenders: list[User], recommendations: list[Recommendation], matches: list[Match], item, requesterID):
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
    rankedList = [y[0] for y in rankedList]
    return rankedList

# def printRankedRecommendations(rankedList):
#     for items in rankedList:
#         print(items)

def add_recommendation(
    itemID: str, uniqueUserMatchID: str, findItem: int, date: str,
    uow: unitofwork.AbstractUnitOfWork):

    with uow:
        uow.recommendations.add(Recommendation(itemID,uniqueUserMatchID, findItem, date))
        uow.commit()