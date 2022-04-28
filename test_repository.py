
# from sqlalchemy import Column, ForeignKey, Integer, String, Table, MetaData
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, mapper
import pytest
from datetime import date
from recommendations import Recommendation
import recommendations
from sqlalchemy import insert, update
from repository import SqlAlchemyRepository
from services import setRating, setRank
from sqlalchemy.orm import Session
# pytestmark = pytest.mark.usefixtures('mappers')

def test_repo_can_save_a_recommendation(session):
    recommendation = recommendations.Recommendation(4,4,"url",date=date(2020,7,25))
    repo = SqlAlchemyRepository(session)
    repo.add(recommendation)
    session.commit()

    rows = list(session.execute(
        'SELECT uniqueUserMatchID, itemID, findItem FROM recommendations'
    ))
    assert list(rows) == [('4','4',"url")]

def insert_recommendation(session):
    session.execute(
        "INSERT INTO recommendations (itemID, uniqueUserMatchID, findItem, date)"
        'VALUES ("pizza", "Betty-John","pizza.com","2022-04-27")'
    )
    [[recommendation_id]] = session.execute(
            "Select itemID FROM recommendations WHERE uniqueUserMatchID=:uniqueUserMatchID",
            dict (uniqueUserMatchID= "Betty-John")
        )
    return recommendation_id



def test_repository_can_save_rating(session):
    recommendation = recommendations.Recommendation(4,4,"url",date=date(2020,7,25))
    repo = SqlAlchemyRepository(session)
    repo.add(recommendation)
    session.commit()
    reference=0
    x = repo.list()
    x[0]._recommendationRating = setRating("good",x,reference)
    session.commit()
    rows = list(session.execute(
        'SELECT uniqueUserMatchID, itemID, findItem, _recommendationRating FROM recommendations'
    ))
    assert list(rows) == [('4','4',"url", 1)]

def test_repository_can_save_rank(session):
    recommendation = recommendations.Recommendation(4,4,"url",date=date(2020,7,25))
    repo = SqlAlchemyRepository(session)
    repo.add(recommendation)
    session.commit()
    reference=0
    x = repo.list()
    x[0]._recommendationRating = setRating("good",x,reference)
    session.commit()
    x[0]._rank = setRank(x,recommendation.uniqueUserMatchID)
    rows = list(session.execute(
        'SELECT uniqueUserMatchID, itemID, findItem, _recommendationRating FROM recommendations'
    ))
    assert list(rows) == [('4','4',"url", 1)]



