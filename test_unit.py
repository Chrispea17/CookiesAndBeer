from pyparsing import null_debug_action
from recommendations import Recommendation
import pytest


def test_ability_to_give_a_recommendation_a_positive_rating():
    rank = Recommendation.rating("good")
    assert rank == 1


def test_ability_to_give_a_recommendation_a_negative_rating():
    rank = Recommendation.rating("bad")
    assert rank == 0


def test_null_rating_not_possible():
    with pytest.raises(Exception):
        Recommendation.rating() == 1


def test_this_is_a_recommendation_with_correct_data_types():
    recommendation = Recommendation(25, 14, 4, "www.findyouritem.com")
    assert type(recommendation.recommendationID) == int
    assert type(recommendation.uniqueUserMatchID) == int
    assert type(recommendation.itemID) == int
    assert type(recommendation.findItem) == str


def test_this_is_a_recommendation_with_correct_data():
    recommendation = Recommendation(25, 14, 4, "www.findyouritem.com")
    assert recommendation.recommendationID == 25
    assert recommendation.uniqueUserMatchID == 14
    assert recommendation.itemID == 4
    assert recommendation.findItem == "www.findyouritem.com"


def test_this_is_a_recommendation_with_no_rating():
    recommendation = Recommendation(25, 14, 4, "www.findyouritem.com")
    assert recommendation.recommendationID == 25
    assert recommendation.uniqueUserMatchID == 14
    assert recommendation.itemID == 4
    assert recommendation.findItem == "www.findyouritem.com"
