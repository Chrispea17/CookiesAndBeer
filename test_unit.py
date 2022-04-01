from pyparsing import null_debug_action
from recommendations import Rank, Recommendation
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


def test_calculate_recommendation_count():
    recList = [
        Recommendation(1, 5, 6, "garbageinput.com"),
        Recommendation(2, 6, 6, "garbageinput.com"),
        Recommendation(3, 5, 6, "garbageinput.com"),
        Recommendation(4, 5, 6, "garbageinput.com"),
        Recommendation(5, 5, 6, "garbageinput.com")
    ]
    setrating = [
        "good","bad", None, None, "good","good"
    ]
    for item in range(0,len(recList)-1):
        recList[item].setRating(setRating[item])
    counter = Rank()
    counter.countforRank(recList, 5)
    assert counter._count == 0
    counter.countforRank(recList, 6)
    assert counter._count == None
    counter.countforRank(recList, 10)
    assert counter._count == None

# def test_calculate_recommendation_sum():
#     recList = [
#         Recommendation(1, 5, 6, "garbageinput.com").setRating("good"),
#         Recommendation(2, 6, 6, "garbageinput.com").setRating("good"),
#         Recommendation(3, 5, 6, "garbageinput.com").setRating("bad"),
#         Recommendation(4, 5, 6, "garbageinput.com").setRating("good"),
#         Recommendation(5, 5, 6, "garbageinput.com").setRating("bad")

#     ]
#     counter = Rank()
#     counter.countforRank(recList, 5)
#     assert counter._count == 4
#     counter.countforRank(recList, 6)
#     assert counter._count == 1
#     counter.countforRank(recList, 10)
#     assert counter._count == 0

#     def test_calculate_unranked_sum():
#         recList = [
#         Recommendation(1, 5, 6, "garbageinput.com").setRating("good"),
#         Recommendation(2, 6, 6, "garbageinput.com").setRating("good"),
#         Recommendation(3, 5, 6, "garbageinput.com").setRating("bad"),
#         Recommendation(4, 5, 6, "garbageinput.com").setRating("good"),
#         Recommendation(5, 5, 6, "garbageinput.com")

#     ]
#         counter = Rank()
#         counter.countforRank(recList, 5)
#         assert counter._count == 4
#         counter.countforRank(recList, 6)
#         assert counter._count == 1
#         counter.countforRank(recList, 10)
#         assert counter._count == 0

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
