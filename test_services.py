from recommendations import Recommendation
from services import setRating

def test_set_rating_on_particular_recommendation():
    recommendation1 = Recommendation("1234", "pizza", "getpizza.com", "7-12-1987", reference = 4)
    recommendation45 = Recommendation("1234", "icecream", "geticecream.com", "7-12-1997", reference = 45)
    rating=setRating("good", [recommendation1,recommendation45], 45)
    assert rating == 1
    rating2=setRating("bad", [recommendation1,recommendation45], 4)
    assert rating2 == 0

def test_calculate_recommendation_count():
    rec1 = Recommendation(5, 6, "garbageinput.com","8-2-2022", reference = 1)
    rec1.setRating("good")
    rec2 = Recommendation(6, 6, "garbageinput.com","8-2-2022", reference = 2)
    rec3 = Recommendation(5, 6, "garbageinput.com","8-2-2022", reference = 3)
    rec3.setRating("bad")
    rec4 = Recommendation(5, 6, "garbageinput.com","8-2-2022", reference = 4)
    rec4.setRating("good")
    rec5 = Recommendation(5, 6, "garbageinput.com","8-2-2022", reference = 5)
    ratings = [rec1, rec2, rec3, rec4, rec5]

    counter = Rank()
    counter.countforRank(ratings, 5)
    assert counter._count == 3
    counter.countforRank(ratings, 6)
    assert counter._count == None
    counter.countforRank(ratings, 10)
    assert counter._count == None