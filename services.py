# There are two services that the app takes care of, one is applying a rating given be the requester to the recommendation itself
# The next is using all previous recommendations to calculate the rank of each new person giving a recommendation and including those who have never given a recommendation before


from difflib import Match
from gettext import find

from recommendations import Recommendation, MatchUsers, User
from unitofwork import AbstractUnitOfWork


#uow service
def add_recommendation(
    uniqueUserMatchID:str, itemID:str, findItem:str, date : str, uow: AbstractUnitOfWork, recommendationRating : int =None, rank : float = 0,
    ):

    with uow:
        uow.repo.add(Recommendation(uniqueUserMatchID,itemID,findItem,date,uow,recommendationRating,rank))
        uow.commit()

def add_userMatch(
    RequesterID : str, RecommenderID : str,
    uow: AbstractUnitOfWork):

    with uow:
        uow.repo.add_match(MatchUsers(RequesterID=RequesterID,RecommenderID=RecommenderID))
        uow.commit()

def setRating(response: str, recommendations, reference) -> int:
    for recs in recommendations:
        if recs.reference == reference:
            recs.setRating(response)
            return recs._recommendationRating

# uow service 
"""
TODO:this is very wrong, need to save to match first then apply to rating"""
def uow_setRating(response: str, reference, uow: AbstractUnitOfWork) -> int:
    with uow:
        rated_recommend = uow.repo.select_for_update(reference)
        rated_recommend.setRating(response)
        uow.commit()
        return rated_recommend._recommendationRating


        

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


def sumRatings(data, uniqueusermatch):
    sum = 0
    for item in data:
        print(item._recommendationRating)
        print(sum)
        if (
            item.uniqueUserMatchID == uniqueusermatch
            and item._recommendationRating != None
            and item._recommendationRating == 1
        ):
            sum += 1
    if sum == 0:
        sum = None
    return sum

#uow service
def sumRatings(data, uniqueusermatch):
    sum = 0
    for item in data:
        print(item._recommendationRating)
        print(sum)
        if (
            item.uniqueUserMatchID == uniqueusermatch
            and item._recommendationRating != None
            and item._recommendationRating == 1
        ):
            sum += 1
    if sum == 0:
        sum = None
    return sum


def setRank(data: list[Recommendation], matchid, uow : AbstractUnitOfWork):
    with uow:
        sum = sumRatings(data, matchid)
        count = countRecommendationsForMatch(data, matchid)
        rank = sum / count
        uow.commit()
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
