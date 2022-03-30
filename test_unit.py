from recommendations import Recommendation
import pytest


def test_ability_to_give_a_recommendation_a_positive_rating():
    rank = Recommendation.rating("good")
    assert rank == 1


def test_ability_to_give_a_recommendation_a_negative_rating():
    rank = Recommendation.rating("bad")
    assert rank == 0


def test_other_rating_not_possible():
    with pytest.raises(Exception):
        Recommendation.rating() == 1
