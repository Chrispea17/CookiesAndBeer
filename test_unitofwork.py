from datetime import datetime, timezone
import pytest
from unitofwork import SqlAlchemyUnitOfWork
from services import setRank_uow
from conftest import sqlite_session_factory
# from services import setRating, setRank, uow_setRating, add_recommendation, add_userMatch, getRankedRecommendations, getRecommendersForItem
# from CookiesAndBeer.unitofwork import FakeUnitOfWork

from recommendations import Recommendation, MatchUsers, setRank 
import unitofwork
import services


def insert_recommendation(session, itemID, uniqueUserMatchID, date, findItem, _recommendationRating = None, _rank = 0):
    session.execute(
        """
        INSERT INTO recommendations (date, uniqueUserMatchID, itemID, findItem, _recommendationRating, _rank)
        VALUES(:date,:uniqueUserMatchID,:itemID,:findItem,:_recommendationRating, :_rank)
        """,
            dict(
            date=date, 
            findItem=findItem,
            uniqueUserMatchID=uniqueUserMatchID,
            itemID=itemID,
            _recommendationRating=_recommendationRating,
            _rank=_rank,
        ),
    )

def insert_userMatch(session, RequesterID, RecommenderID):
    session.execute(
        """
        INSERT INTO match_users (reference, RequesterID, RecommenderID)
        VALUES(:reference,:RequesterID,:RecommenderID)
        """,
            dict(reference = RequesterID + RecommenderID,
            RequesterID=RequesterID, 
            RecommenderID=RecommenderID,
        ),
    )


def get_rating(session, reference):
    [[recommendationrating]]=session.execute(
        'SELECT _recommendationRating FROM recommendations WHERE reference=:reference',
        dict(reference=reference),
    )
    return recommendationrating

def setRating(session,response):
    uow = SqlAlchemyUnitOfWork(sqlite_session_factory)
    insert_recommendation(session, f"pizza", f"Betty-George", nu.isoformat(), f"http://example.com")
    uow.commit()
    uow = unitofwork.SqlAlchemyUnitOfWork(sqlite_session_factory)
    with uow:
        rec = uow.repo.get(0)
        rec.setRating(response)



#this is messed up because i need to persist the rank for the user match instad of the recommendation. The rank doesn't change for every recommendation so it should not be given more reasons to change than it needs
def get_ranking(session, uniqueUserMatchID):
    [[recommendationrating]]=session.execute(
        'SELECT Avg(_recommendationRating) FROM recommendations WHERE uniqueUserMatchID=:uniqueUserMatchID',
        dict(uniqueUserMatchID=uniqueUserMatchID),
    )
    return recommendationrating


def test_can_retrieve_recommendation(sqlite_session_factory):
    session = sqlite_session_factory()
    nu: datetime = datetime(2022, 4, 24, 0,0, 0, 0, tzinfo=timezone.utc)
    insert_recommendation(session, f"pizza", f"Betty-George", nu.isoformat(), f"http://example.com")
    session.commit()

    recommendation: Recommendation = None
    uow = unitofwork.SqlAlchemyUnitOfWork(sqlite_session_factory)

    with uow: 
        recommendation = uow.repo.list_recommendations()[0]
        assert recommendation.itemID=="pizza"

def test_can_retrieve_userMatch(sqlite_session_factory):
    session = sqlite_session_factory()
    insert_userMatch(session, f"Betty", f"George")
    session.commit()

    matches: MatchUsers = None
    uow = unitofwork.SqlAlchemyUnitOfWork(sqlite_session_factory)

    with uow: 
        match = uow.repo.list_matches()[0]
        print(match.reference)
        assert match.reference=="BettyGeorge"

    
def get_recommendation(session, reference):
    [[itemID]] = session.execute(
        "SELECT itemID FROM recommendations WHERE reference=:reference",
        dict(reference=reference)
    )
    return itemID

def test_set_ranking_for_usermatch(sqlite_session_factory):
    session = sqlite_session_factory()
    nu: datetime = datetime(2022, 4, 24, 0,0, 0, 0, tzinfo=timezone.utc)
    insert_userMatch(session,"betty","george")
    insert_userMatch(session, "betty","john")
    insert_recommendation(session, f"pizza",f"bettygeorge", nu.isoformat() ,f"getpizza.com", _recommendationRating=1) #because we have a passing set rating test() &we assume data has already been set
    insert_recommendation(session,f"icecream",f"bettygeorge", nu.isoformat(), "geticecream.com",_recommendationRating=0)
    insert_recommendation(session,"jello","bettygeorge", nu.isoformat(), f"getjello.com",  _recommendationRating=0)
    insert_recommendation(session, "beer","bettyjohn", nu.isoformat(), f"getbeer.com",_recommendationRating=0)
    session.commit()

    matches: MatchUsers = None
    uow = unitofwork.SqlAlchemyUnitOfWork(sqlite_session_factory)

    with uow:
        match = uow.repo.get_match("bettygeorge")
        recs = uow.repo.list_rated_recommendations()
        rank = setRank(recs,"bettygeorge")
        match.setRank(rank,"bettygeorge")
        uow.commit()
        rank_sql = uow.repo.get_match("bettygeorge")
        assert rank_sql._rank == 1/3
        


def test_uow_can_retrieve_a_user_match_from_recommendation_(sqlite_session_factory):
    session = sqlite_session_factory()
    nu: datetime = datetime(2022, 4, 24, 0,0, 0, 0, tzinfo=timezone.utc)
    nu2: datetime = datetime(2022, 4, 24, 0,0, 0, 0, tzinfo=timezone.utc)
    insert_recommendation(session, f"pizza", f"Betty-George", nu.isoformat(), f"http://example.com")
    insert_recommendation(session, f"pizza", f"Betty-John", nu2.isoformat(), f"http://examplepizza.com")    
    session.commit()
    uow = unitofwork.SqlAlchemyUnitOfWork(sqlite_session_factory)
    with uow:
        recommendation = uow.repo.list_recommendations()
        for rec in recommendation:
            if rec.reference==2:
                rec_user = rec.uniqueUserMatchID

    assert rec_user == "Betty-John"

def test_select_for_update(sqlite_session_factory):
    session = sqlite_session_factory()
    nu: datetime = datetime(2022, 4, 24, 0,0, 0, 0, tzinfo=timezone.utc)
    nu2: datetime = datetime(2022, 4, 25, 0,0, 0, 0, tzinfo=timezone.utc)
    insert_recommendation(session, f"pizza", f"Betty-George", nu.isoformat(), f"http://example.com")
    insert_recommendation(session, f"pizza", f"Betty-John", nu2.isoformat(), f"http://examplepizza.com")
    session.commit()

    uow = unitofwork.SqlAlchemyUnitOfWork(sqlite_session_factory)

    with uow:
        retrieved = uow.repo.select_for_update(reference=1)
        retrieved.setRating("bad")
        uow.commit()
    rate = get_rating(session, 1)
    assert rate==0

def test_get_rank(sqlite_session_factory):
    session = sqlite_session_factory()
    nu: datetime = datetime(2022, 4, 24, 0,0, 0, 0, tzinfo=timezone.utc)
    nu2: datetime = datetime(2022, 4, 25, 0,0, 0, 0, tzinfo=timezone.utc)
    nu3: datetime = datetime(2022, 4, 26, 0,0, 0, 0, tzinfo=timezone.utc)
    nu4: datetime = datetime(2022, 4, 27, 0,0, 0, 0, tzinfo=timezone.utc)
    insert_userMatch(session,"betty","george")
    insert_recommendation(session, f"ice cream", f"bettygeorge", nu.isoformat(), f"http://example.com")
    insert_recommendation(session, f"pizza", f"bettygeorge", nu2.isoformat(), f"http://examplepizza.com")
    insert_recommendation(session, f"cookies", f"bettygeorge", nu3.isoformat(), f"http://examplepizza.com")
    insert_recommendation(session, f"beer", f"bettygeorge", nu4.isoformat(), f"http://examplepizza.com")

    session.commit()

    uow = unitofwork.SqlAlchemyUnitOfWork(sqlite_session_factory)

    with uow:
        retrieved = uow.repo.list_recommendations()
        retrieved[0].setRating("bad")
        retrieved[1].setRating("good")
        retrieved[2].setRating("good")
        retrieved[3].setRating("good")
        rank = setRank(retrieved,"bettygeorge")
        uow.commit()
        final_rank = get_ranking(session,f'bettygeorge')
        retrieved_rating = get_rating(session, 1)

        assert final_rank==0.75


def return_list_by_rank(sqlite_session_factory):
    session = sqlite_session_factory()
    nu: datetime = datetime(2022, 4, 24, 0,0, 0, 0, tzinfo=timezone.utc)
    nu2: datetime = datetime(2022, 4, 25, 0,0, 0, 0, tzinfo=timezone.utc)
    nu3: datetime = datetime(2022, 4, 26, 0,0, 0, 0, tzinfo=timezone.utc)
    nu4: datetime = datetime(2022, 4, 27, 0,0, 0, 0, tzinfo=timezone.utc)
    insert_recommendation(session, f"ice cream", f"BettyGeorge", nu.isoformat(), f"http://example.com")
    insert_recommendation(session, f"pizza", f"BettyGeorge", nu2.isoformat(), f"http://examplepizza.com")
    insert_recommendation(session, f"cookies", f"BettyJohn", nu3.isoformat(), f"http://examplepizza.com")
    insert_recommendation(session, f"beer", f"BettyGeorge", nu4.isoformat(), f"http://examplepizza.com")
    session.commit()

    uow = unitofwork.SqlAlchemyUnitOfWork(sqlite_session_factory)

    with uow:
        retrieved = uow.repo.list_recommendations()
        retrieved[0].setRating("bad")
        retrieved[1].setRating("good")
        retrieved[2].setRating("good")
        retrieved[3].setRating("good")
        rank = setRank(retrieved,"BettyGeorge")
        rate_George = uow.repo.get_match("BettyGeorge")
        rate_George.setRank(rank,rate_George.uniqueUserMatchID)
        rate_John = uow.repo.get_match("BettyJohn")
        rate_John.setRank(rank,rate_John.uniqueUserMatchID)
        uow.commit()
        assert rate_George._rank==0.75
        assert rate_John._rank==1

