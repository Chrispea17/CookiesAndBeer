from recommendations import Rank, Recommendation, MatchUsers, User, Item, Lists

# from sqlalchemy.orm import mapper, relationship
import pytest


def test_positive_rating_equals_one():
    recommendation = Recommendation(1, 25, 1, "howdy.com")
    recommendation.setRating("good")
    assert recommendation._recommendationRating == 1


def test_negative_rating_equals_zero():
    recommendation = Recommendation(1, 16, 5, "fifth.com")
    recommendation.setRating("bad")
    assert recommendation._recommendationRating == 0


def test_other_rating_not_possible():
    with pytest.raises(Exception):
        recommendation = Recommendation(1, 6, 6, "garbageinput.com")
        recommendation.setRating("garbage-in")
        assert recommendation._recommendationRating == 1
        assert recommendation._recommendationRating == 0


def test_this_is_a_recommendation_with_correct_data_types():
    recommendation = Recommendation(25, 14, 1, "www.findyouritem.com")
    assert type(recommendation.recommendationID) == int
    assert type(recommendation.uniqueUserMatchID) == int
    assert type(recommendation.itemID) == int
    assert type(recommendation.findItem) == str


def test_this_is_a_recommendation_with_correct_data():
    recommendation = Recommendation(25, 14, 1, "www.findyouritem.com")
    assert recommendation.recommendationID == 25
    assert recommendation.uniqueUserMatchID == 14
    assert recommendation.itemID == 1
    assert recommendation.findItem == "www.findyouritem.com"


# def test_calculate_rank():
#     recommendationCount = 20
#     sumofratings = 15
#     score = Rank()
#     score.setRank(sumofratings, recommendationCount)
#     assert score._rank == 0.75
# refactored


def test_calculate_rank():
    rec1 = Recommendation(1, 5, 6, "garbageinput.com")
    rec1.setRating("good")
    rec2 = Recommendation(2, 6, 6, "garbageinput.com")
    rec3 = Recommendation(3, 5, 6, "garbageinput.com")
    rec3.setRating("bad")
    rec4 = Recommendation(4, 5, 6, "garbageinput.com")
    rec4.setRating("good")
    rec5 = Recommendation(5, 5, 6, "garbageinput.com")
    ratings = [rec1, rec2, rec3, rec4, rec5]

    counter = Rank()
    counter.setRank(ratings, 5)
    assert counter._rank == 2 / 3
    # counter.countforRank(ratings, 6)
    # assert counter._count == None
    # counter.countforRank(ratings, 10)
    # assert counter._count == None


# I've got no where to put this because I don't have UniqueUserMatchIDs to assign the Count to
def test_calculate_recommendation_count():
    rec1 = Recommendation(1, 5, 6, "garbageinput.com")
    rec1.setRating("good")
    rec2 = Recommendation(2, 6, 6, "garbageinput.com")
    print(rec2._recommendationRating)
    rec3 = Recommendation(3, 5, 6, "garbageinput.com")
    rec3.setRating("bad")
    rec4 = Recommendation(4, 5, 6, "garbageinput.com")
    rec4.setRating("good")
    rec5 = Recommendation(5, 5, 6, "garbageinput.com")
    ratings = [rec1, rec2, rec3, rec4, rec5]

    counter = Rank()
    counter.countforRank(ratings, 5)
    assert counter._count == 3
    counter.countforRank(ratings, 6)
    assert counter._count == None
    counter.countforRank(ratings, 10)
    assert counter._count == None


def test_calculate_recommendation_sum():
    rec1 = Recommendation(1, 5, 6, "garbageinput.com")
    rec1.setRating("good")
    rec2 = Recommendation(2, 6, 6, "garbageinput.com")
    rec3 = Recommendation(3, 5, 4, "garbageinput.com")
    rec3.setRating("bad")
    rec4 = Recommendation(4, 5, 3, "garbageinput.com")
    rec4.setRating("good")
    rec5 = Recommendation(5, 5, 2, "garbageinput.com")
    ratings = [rec1, rec2, rec3, rec4, rec5]

    counter = Rank()
    counter.sumforRank(ratings, 5)
    assert counter._sum == 2
    counter.sumforRank(ratings, 6)
    assert counter._sum == None
    counter.sumforRank(ratings, 10)
    assert counter._sum == None


def test_get_recommender_or_requester_user_id_from_recommendation():
    recommendation = Recommendation(5, 2, 6, "garbageinput.com")
    matchID = MatchUsers(recommendation.uniqueUserMatchID, 13, 14)
    recommender = matchID.getRecommender(2)
    assert recommender == 14
    requester = matchID.getRequester(2)
    assert requester == 13


def test_list_recommender_users():
    """
    if a bunch of people send a recommendation, list them, by their UserIDs
    """
    rec1 = Recommendation(1, 5, 6, "garbageinput1.com")
    match1 = MatchUsers(rec1.uniqueUserMatchID, 1, 12)
    rec2 = Recommendation(2, 6, 6, "garbageinput2.com")
    match2 = MatchUsers(rec2.uniqueUserMatchID, 1, 13)
    rec3 = Recommendation(3, 7, 6, "garbageinput3.com")
    match3 = MatchUsers(rec3.uniqueUserMatchID, 1, 14)
    rec4 = Recommendation(4, 10, 6, "garbageinput4.com")
    match4 = MatchUsers(rec4.uniqueUserMatchID, 1, 15)
    rec5 = Recommendation(5, 1, 7, "garbageinput5.com")
    match5 = MatchUsers(rec5.uniqueUserMatchID, 1, 16)
    recommendations = [rec1, rec2, rec3, rec4, rec5]
    matches = [match1, match2, match3, match4, match5]
    listRecommenders = Lists()
    listRecommenders.get_recommenders_with_itemID(recommendations, matches, 6)
    assert listRecommenders._recommendersList == {12, 13, 14, 15}


"""
User tests

"""


def test_get_user_from_input():
    user = User("5", "BettyRec")
    assert user.userID == "5"
    assert isinstance(user, User)


def test_item_user_from_input():
    item = Item("1", "Cookies")
    assert item.itemID == "1"
    assert isinstance(item, Item)


def test_get_user_from_id():
    user = User("5", "BettyRec")
    user.get_user_from_id("5") == "BettyRec"


def test_get_item_from_id():
    user = Item("1", "Cookies")
    user.get_item_from_id("1") == "Cookies"
