import recommendations


def test_ability_to_give_a_recommendation_a_ranking():
    rank = recommendation.ranking("good")
    assert rank == 1
