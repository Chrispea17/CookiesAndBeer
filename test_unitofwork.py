from datetime import datetime, timezone
import pytest
from services import setRating, setRank, uow_setRating
# from CookiesAndBeer.unitofwork import FakeUnitOfWork

from recommendations import Recommendation
import unitofwork


def insert_recommendation(session, itemID, uniqueUserMatchID, date, findItem):
    session.execute(
        """
        INSERT INTO recommendations (date, uniqueUserMatchID, itemID, findItem)
        VALUES(:date,:uniqueUserMatchID,:itemID,:findItem)
        """,
            dict(
            date=date, 
            findItem=findItem,
            uniqueUserMatchID=uniqueUserMatchID,
            itemID=itemID,
        ),
    )

def get_rating(session, reference):
    [[recommendationrating]]=session.execute(
        'SELECT _recommendationRating FROM recommendations WHERE reference=:reference',
        dict(reference=reference),
    )
    return recommendationrating

def get_raking(session, uniqueUserMatchID):
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
        recommendation = uow.recommendations.list()[0]
        assert recommendation.itemID=="pizza"


def get_recommendation(session, reference):
    [[itemID]] = session.execute(
        "SELECT itemID FROM recommendations WHERE reference=:reference",
        dict(reference=reference)
    )
    return itemID


def test_uow_can_retrieve_a_user_match_from_recommendation_(sqlite_session_factory):
    session = sqlite_session_factory()
    nu: datetime = datetime(2022, 4, 24, 0,0, 0, 0, tzinfo=timezone.utc)
    nu2: datetime = datetime(2022, 4, 24, 0,0, 0, 0, tzinfo=timezone.utc)
    insert_recommendation(session, f"pizza", f"Betty-George", nu.isoformat(), f"http://example.com")
    insert_recommendation(session, f"pizza", f"Betty-John", nu2.isoformat(), f"http://examplepizza.com")    
    session.commit()
    uow = unitofwork.SqlAlchemyUnitOfWork(sqlite_session_factory)
    with uow:
        recommendation = uow.recommendations.list()
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
        retrieved = uow.recommendations.select_for_update(reference=1)
        retrieved._recommendationRating = setRating("bad",[retrieved],1)
        uow.commit()
    rate = get_rating(session, 1)
    assert rate==0

def test_select_for_update_uow_setRating(sqlite_session_factory):
    session = sqlite_session_factory()
    nu: datetime = datetime(2022, 4, 24, 0,0, 0, 0, tzinfo=timezone.utc)
    nu2: datetime = datetime(2022, 4, 25, 0,0, 0, 0, tzinfo=timezone.utc)
    nu3: datetime = datetime(2022, 4, 26, 0,0, 0, 0, tzinfo=timezone.utc)
    nu4: datetime = datetime(2022, 4, 27, 0,0, 0, 0, tzinfo=timezone.utc)

    insert_recommendation(session, f"ice cream", f"Betty-George", nu.isoformat(), f"http://example.com")
    insert_recommendation(session, f"pizza", f"Betty-John", nu2.isoformat(), f"http://examplepizza.com")
    session.commit()

    uow = unitofwork.SqlAlchemyUnitOfWork(sqlite_session_factory)
    with uow:
        rate = uow_setRating("bad", 1, uow)
        retrieved_rating = get_rating(session, 1)
        assert retrieved_rating==0

def test_get_rank(sqlite_session_factory):
    session = sqlite_session_factory()
    nu: datetime = datetime(2022, 4, 24, 0,0, 0, 0, tzinfo=timezone.utc)
    nu2: datetime = datetime(2022, 4, 25, 0,0, 0, 0, tzinfo=timezone.utc)
    nu3: datetime = datetime(2022, 4, 26, 0,0, 0, 0, tzinfo=timezone.utc)
    nu4: datetime = datetime(2022, 4, 27, 0,0, 0, 0, tzinfo=timezone.utc)
    insert_recommendation(session, f"ice cream", f"bettygeorge", nu.isoformat(), f"http://example.com")
    insert_recommendation(session, f"pizza", f"bettygeorge", nu2.isoformat(), f"http://examplepizza.com")
    insert_recommendation(session, f"cookies", f"bettygeorge", nu3.isoformat(), f"http://examplepizza.com")
    insert_recommendation(session, f"beer", f"bettygeorge", nu4.isoformat(), f"http://examplepizza.com")
    session.commit()

    uow = unitofwork.SqlAlchemyUnitOfWork(sqlite_session_factory)

    with uow:
        retrieved = uow.recommendations.list()
        retrieved1 = setRating("bad",retrieved,1)
        retrieved2 = setRating("good",retrieved,2)
        retrieved3 = setRating("good",retrieved,3)
        retrieved4 = setRating("good",retrieved,4)
        rank = setRank(retrieved,"bettygeorge")
        uow.commit()
        final_rank = get_raking(session,f'bettygeorge')
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
        retrieved = uow.recommendations.list()
        retrieved1 = setRating("bad",retrieved,1)
        retrieved2 = setRating("good",retrieved,2)
        retrieved3 = setRating("good",retrieved,3)
        retrieved4 = setRating("good",retrieved,4)
        rank = setRank(retrieved,"BettyGeorge")
        rate_George = get_rating(session, f"BettyGeorge")
        rate_John = get_rating(session,1)
        uow.commit()

    assert rank==0.75
