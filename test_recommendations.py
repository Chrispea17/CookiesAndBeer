from recommendations import recommendation


def test_ability_to_give_a_recommendation_a_ranking():
    rank = recommendation.ranking("good")
    print(rank)
    assert rank == 1
