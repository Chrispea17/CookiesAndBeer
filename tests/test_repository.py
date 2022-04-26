
# from sqlalchemy import Column, ForeignKey, Integer, String, Table, MetaData
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, mapper
import pytest
from datetime import date
import recommendations
from sqlalchemy import update
from repository import RecommendationRepository
from services import setRating, setRank

# pytestmark = pytest.mark.usefixtures('mappers')

def test_repo_can_save_a_recommendation(session):
    recommendation = recommendations.Recommendation(4,4,"url",date=date(2020,7,25))
    repo = RecommendationRepository(session)
    repo.add(recommendation)
    session.commit()

    rows = list(session.execute(
        'SELECT uniqueUserMatchID, itemID, findItem FROM recommendations'
    ))
    assert list(rows) == [('4','4',"url")]

# def insert_rating(session,reference,_recommendationRating):
#     dict(_recommendationRating=_recommendationRating, reference = reference)
#     session.execute(
#         "UPDATE recommendations"
#         "SET _recommendationRating := _recommendationRating"
#         'WHERE recommendation.reference :=reference',
#     )

#     [[rank]] = session.execute(
#         'SELECT id FROM items WHERE reference=:reference AND _recommendationRating=:_recommendationRating',
#         dict(reference=1, _recommendationRating=0),
#     )
#     return rank
    

def test_repository_can_save_rating(session):
    recommendation = recommendations.Recommendation(4,4,"url",date=date(2020,7,25))
    repo = RecommendationRepository(session)
    repo.add(recommendation)
    session.commit()
    reference=0
    x = repo.get(recommendation)
    print(x)
    x._recommendationRating = setRating("good",x,reference)
    session.commit()
    rows = list(session.execute(
        'SELECT uniqueUserMatchID, itemID, findItem, _recommendationRating FROM recommendations'
    ))
    assert list(rows) == [('4','4',"url", 1)]

def test_repository_can_save_rank(session):
    recommendation = recommendations.Recommendation(4,4,"url",date=date(2020,7,25))
    repo = RecommendationRepository(session)
    repo.add(recommendation)
    session.commit()
    reference=0
    x = repo.get(recommendation)
    print(x)
    x._recommendationRating = setRating("good",x,reference)
    session.commit()
    x._rank = setRank(x,recommendation.uniqueUserMatchID)
    rows = list(session.execute(
        'SELECT uniqueUserMatchID, itemID, findItem, _recommendationRating FROM recommendations'
    ))
    assert list(rows) == [('4','4',"url", 1)]



