from recommendations import Outputs, Rank, Recommendation, MatchUsers, User, Item, Outputs

# from sqlalchemy.orm import mapper, relationship
import pytest


def test_this_is_a_recommendation_with_correct_data_types():
    recommendation = Recommendation(
        "7-15-2022", "Jean-Joe", "cookies", "www.findyouritem.com")
    assert type(recommendation.date) == str
    assert type(recommendation.uniqueUserMatchID) == str
    assert type(recommendation.itemID) == str
    assert type(recommendation.findItem) == str


def test_this_is_a_recommendation_with_correct_data():
    recommendation = Recommendation(
        "Shell-Silver", "cookies", "www.findyouritem.com", "7-25-2020")
    assert recommendation.date == "7-25-2020"
    assert recommendation.uniqueUserMatchID == "Shell-Silver"
    assert recommendation.itemID == "cookies"
    assert recommendation.findItem == "www.findyouritem.com"
    assert isinstance(recommendation, Recommendation)


# def test_calculate_rank():
#     recommendationCount = 20
#     sumofratings = 15
#     score = Rank()
#     score.setRank(sumofratings, recommendationCount)
#     assert score._rank == 0.75
# refactored


def test_calculate_rank():
    rec1 = Recommendation(5, 6, "garbageinput.com","8-2-2022", reference = 1)
    rec1.setRating("good")
    rec2 = Recommendation(6, 7, "garbageinput.com","8-2-2022", reference = 2)
    rec3 = Recommendation(5, 8, "g2.com","8-2-2022", reference = 3)
    rec3.setRating("bad")
    rec4 = Recommendation(5, 9, "garbageinput.com","8-2-2022", reference = 4)
    rec4.setRating("good")
    rec5 = Recommendation(5, 10, "garbageinput.com","8-2-2022", reference = 5)
    ratings = [rec1, rec2, rec3, rec4, rec5]

    counter = Rank()
    counter.setRank(ratings, 5)
    assert counter._rank == 2 / 3
    # counter.countforRank(ratings, 6)
    # assert counter._count == None
    # counter.countforRank(ratings, 10)
    # assert counter._count == None


# I've got no where to put this because I don't have UniqueUserMatchIDs to assign the Count to



def test_calculate_recommendation_sum():
    rec1 = Recommendation(5, 6, "garbageinput.com","8-2-2022", reference = 1)
    rec1.setRating("good")
    rec2 = Recommendation(6, 6, "garbageinput.com","8-2-2022", reference = 2)
    rec3 = Recommendation(5, 4, "garbageinput.com","8-2-2022", reference = 3)
    rec3.setRating("bad")
    rec4 = Recommendation(5, 3, "garbageinput.com","8-2-2022", reference = 4)
    rec4.setRating("good")
    rec5 = Recommendation(5, 2, "garbageinput.com","8-2-2022", reference = 5)
    ratings = [rec1, rec2, rec3, rec4, rec5]

    counter = Rank()
    counter.sumforRank(ratings, 5)
    assert counter._sum == 2
    counter.sumforRank(ratings, 6)
    assert counter._sum == None
    counter.sumforRank(ratings, 10)
    assert counter._sum == None


def test_get_recommender_or_requester_user_id_from_recommendation():
    requestID = "ImaRequester"
    recommendID = "GinaeatsGarbagePlates"
    item = Item("coffee")
    matchID = MatchUsers(requestID, recommendID)
    recommendation = Recommendation(
        1, matchID.reference, item, "garbageinput.com", reference = 1)
    recommender = matchID.getRecommender(matchID.reference)
    assert recommender == "GinaeatsGarbagePlates"
    requester = matchID.getRequester(matchID.reference)
    assert requester == "ImaRequester"


def test_list_recommender_users():
    """
    if a bunch of people send a recommendation, list them, by their UserIDs
    """
    item1 = Item("pizza")
    pizza = item1.Name
    item2 = Item('marshmallow')
    mm = item2.Name
    requester1 = User("ImaRequester")
    requester2 = User("OtherRequester")
    recommender1 = User("AbbyEats")
    recommender2 = User("JoeHatesPizza")
    recommender3 = User("YinaEatsBeanas")
    recommender4 = User("MyNameSucks")
    recommender5 = User("AnOldUser")
    match1 = MatchUsers(requester1.userName, recommender1.userName)
    match2 = MatchUsers(requester1.userName, recommender2.userName)
    match3 = MatchUsers(requester2.userName, recommender3.userName)
    match4 = MatchUsers(requester1.userName, recommender4.userName)
    match5 = MatchUsers(requester1.userName, recommender5.userName)
    rec1 = Recommendation(match1.reference,
                          pizza, "garbageinput1.com","7-16-2022", reference = 1)
    rec2 = Recommendation(match2.reference,
                          pizza, "garbageinput2.com","7-16-2022", reference = 2)
    rec3 = Recommendation(match3.reference,
                          pizza, "garbageinput3.com","7-16-2022", reference = 3)
    rec4 = Recommendation(match4.reference,
                          pizza, "garbageinput4.com","7-16-2022", reference = 4)
    rec5 = Recommendation(match5.reference,
                          mm, "garbageinput5.com","7-16-2022", reference = 5)
    recommendations = [rec1, rec2, rec3, rec4, rec5]
    matches = [match1, match2, match3, match4, match5]
    listRecommenders = Outputs()
    listRecommenders.get_recommenders_with_same_item(
        recommendations, matches, pizza)
    assert listRecommenders._recommendersList == {
        "AbbyEats", "JoeHatesPizza", "YinaEatsBeanas", "MyNameSucks"}


def test_order_recommender_list_by_Rank():
    """
    TODO:refactor to set this as a data set for all tests and call
    the complexity of the test is due to the calculation of the rank which needs more than one recommendation
    the factory pattern design patterns gang of four "factory boy package"
    """
    item1 = Item("pizza")
    item2 = Item("marshmallows")
    requester1 = User("ImaRequester")
    requester2 = User("OtherRequester")
    recommender1 = User("AbbyEats")
    recommender2 = User("JoeHatesPizza")
    recommender3 = User("YinaEatsBeanas")
    recommender4 = User("MyNameSucks")
    recommender5 = User("AnOldUser") 
    match1 = MatchUsers(requester1.userName, recommender1.userName)
    match2 = MatchUsers(requester1.userName, recommender2.userName)
    match3 = MatchUsers(requester2.userName, recommender3.userName)
    match4 = MatchUsers(requester1.userName, recommender4.userName)
    match5 = MatchUsers(requester1.userName, recommender5.userName)
    rec1 = Recommendation(match1.reference,
                          item1.Name, "placetogetpizza.com","8-2-2022", reference = 1)
    match1._rank = 0.5
    rec2 = Recommendation(match2.reference, item1.Name, "yourmom.com","7-25-2020", reference = 2)
    match2._rank = 0.4
    rec3 = Recommendation(match3.reference, item1.Name, "mymom.com","7-25-2020", reference = 3)
    match3._rank = 0.77
    rec4 = Recommendation(match4.reference,
                          item1.Name, "homemade.com","7-25-2020", reference=4)
    match4._rank = 0.25
    rec5 = Recommendation(match5.reference,
                          item2.Name, "notpizza.com","7-25-2020",reference=5)
    match5._rank = 0
    recommenders = [
        recommender1,
        recommender2,
        recommender3,
        recommender4,
        recommender5,
    ]
    recommendations = [rec1, rec2, rec3, rec4, rec5]
    matches = [match1, match2, match3, match4, match5]
    list = Outputs()
    list.get_ranked_recommendations(
        recommenders, recommendations, matches, item1.Name, requester1.userName)
    assert list._rankedList == [
        ["AbbyEats", 'pizza', "placetogetpizza.com"],
        ["JoeHatesPizza", 'pizza', "yourmom.com"],
        ["MyNameSucks", 'pizza', "homemade.com"],
    ]

def test_get_user_from_input():
    user = User("BettyRec")
    assert isinstance(user, User)


def test_item_user_from_input():
    item = Item("Cookies")
    assert isinstance(item, Item)
