from datetime import datetime, timezone
import pytest
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

def get_recommendation(session, itemID):
    [[recommendationID]]=session.execute(
        'SELECT id FROM recommendations WHERE itemID=:itemID',
        dict(itemID=itemID)
    )
    return recommendationID


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
        "SELECT itemID FROM recommendation WHERE reference=:reference",
        dict(reference=reference)
    )
    return itemID


def test_uow_can_retrieve_a_user_match_from_recommendation_(sqlite_session_factory):
    session = sqlite_session_factory()
    nu: datetime = datetime(2022, 4, 24, 0,0, 0, 0, tzinfo=timezone.utc)
    insert_recommendation(session, f"pizza", f"Betty-George", nu.isoformat(), f"http://example.com")
    insert_recommendation(session, f"pizza", f"Betty-John", nu.isoformat(), f"http://examplepizza.com")
    session.commit()

    uow = unitofwork.SqlAlchemyUnitOfWork(sqlite_session_factory)
    with uow:
        recommendation = uow.recommendations.list()

        for rec in recommendation:
            if rec.reference==2:
                rec_user = rec.uniqueUserMatchID

    assert rec_user == "Betty-John"