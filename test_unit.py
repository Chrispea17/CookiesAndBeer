from pyparsing import null_debug_action
from recommendations import Recommendation
import pytest

# def test_ability_to_give_a_recommendation_a_positive_rating():
#     rank = Recommendation.rating("bad")
#     assert rank == 1
# changed to a more accurate name for the test
# def test_ability_to_give_a_recommendation_a_positive_rating():

def test_positive_rating_equals_one():
    recommendation = Recommendation(1, 25, 1, "howdy.com")
    recommendation._recommendationRating = recommendation.setRating("good")
    assert recommendation._recommendationRating == 1


# def test_ability_to_give_recommendation_a_positive_rating():
#     rant = Recommendation.


def test_ability_to_give_a_recommendation_a_negative_rating():
    rank = Recommendation.rating("bad")
    assert rank == 0


def test_null_rating_not_possible():
    with pytest.raises(Exception):
        Recommendation.rating() == 1


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


# didn't like the way this worked so took rating out of the initializer
# def test_this_is_a_recommendation_with_no_rating():
#     recommendation = Recommendation(25, 14, 4, "www.findyouritem.com")
#     assert recommendation.recommendationID == 25
#     assert recommendation.uniqueUserMatchID == 14
#     assert recommendation.itemID == 4
#     assert recommendation.findItem == "www.findyouritem.com"

# this is the first time we are testing a repository
def test_count_all_recommendations_given_by_User2_to_User1():
    recommendation1 = Recommendation(25, 14, 1, "www.findyourfirstitem.com")
    recommendation2 = Recommendation(26, 14, 2, "www.findyourseconditem.com")
    recommendation3 = Recommendation(27, 14, 3, "www.findyourthirditem.com")
    recommendation4 = Recommendation(28, 14, 4, "www.findyourfourthitem.com")
    recommendation5 = Recommendation(29, 14, 5, "www.findyourfifthitem.com")
    countRecommendations = Recommendation.counter(14)
    assert countRecommendations == 5
