from urllib import request
from recommendations import Rank, Recommendation, MatchUsers
import pytest


def test_positive_rating_equals_one():
    recommendation = Recommendation(1, 25, 1, "howdy.com")
    recommendation.setRating("good")
    assert recommendation._recommendationRating == 1


def test_negative_rating_equals_zero():
    recommendation = Recommendation(1, 16, 5, "fifth.com")
    recommendation.setRating("bad")
    assert recommendation._recommendationRating == 0


def test_null_rating_not_possible():
    with pytest.raises(Exception):
        recommendation = Recommendation(1, 6, 6, "garbageinput.com")
        recommendation.setRating("garbage-in")
        assert recommendation._recommendationRating == 1


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


def test_calculate_rank():
    recommendationCount = 20
    sumofratings = 15
    score = Rank()
    score.setRank(sumofratings, recommendationCount)
    assert score._rank == 0.75


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
    counter.sumforRank(ratings, 5)
    assert counter._sum == 2
    counter.sumforRank(ratings, 6)
    assert counter._sum == None
    counter.sumforRank(ratings, 10)
    assert counter._sum == None


def test_calculate_unique_user_match_seq():
    UserID1 = 11
    UserID2 = 12
    matchSequence = MatchUsers(1,UserID1, UserID2)
    assert matchSequence.seq == "11-12"
    matchSequence2 = MatchUsers(2,UserID2, UserID1)
    assert matchSequence2.seq == "12-11"

def test_get_recommender_user_id_from_recommendation():
    recommendation = Recommendation(5, 2, 6, "garbageinput.com")
    matchID = MatchUsers(recommendation.uniqueUserMatchID, 13, 14)
    recommender = matchID.getRecommender()
    assert recommender == 14
    requester = matchID.getRequester()
    assert requester == 13
# didn't like the way this worked so took rating out of the initializer
# def test_this_is_a_recommendation_with_no_rating():
#     recommendation = Recommendation(25, 14, 4, "www.findyouritem.com")
#     assert recommendation.recommendationID == 25
#     assert recommendation.uniqueUserMatchID == 14
#     assert recommendation.itemID == 4
#     assert recommendation.findItem == "www.findyouritem.com"

# this is the first time we are testing a repository
# def test_store_recommendations():
# def test_count_all_recommendations_given_by_User2_to_User1():
#     recommendation1 = Recommendation(25, 14, 1, "www.findyourfirstitem.com")
#     recommendation2 = Recommendation(26, 14, 2, "www.findyourseconditem.com")
#     recommendation3 = Recommendation(27, 14, 3, "www.findyourthirditem.com")
#     recommendation4 = Recommendation(28, 14, 4, "www.findyourfourthitem.com")
#     recommendation5 = Recommendation(29, 14, 5, "www.findyourfifthitem.com")
#     countRecommendations = Recommendation.counter(14)
#     assert countRecommendations == 5
