from recommendations import Recommendation
import pytest


def test_ability_to_give_a_recommendation_a_positive_ranking():
    rank = Recommendation.ranking("good")
    assert rank == 1


def test_ability_to_give_a_recommendation_a_negative_ranking():
    rank = Recommendation.ranking("bad")
    assert rank == 0


def test_other_ranking_not_possible():
    with pytest.raises(Exception):
        Recommendation.ranking() == 1
