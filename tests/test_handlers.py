from __future__ import annotations
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from typing import Dict, List
import pytest
import bootstrap
import commands
import handlers, unitofwork
import repository
import messagebus

from orm import start_mappers
from unitofwork import FakeUnitOfWork


def boostrap_test_app():
    return bootstrap.bootstrap(start_orm=False, uow=FakeUnitOfWork())


def test_add_single_recommendation():

    #arrange
    bus = boostrap_test_app()
    nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)

    # add one = act
    bus.handle(
        commands.AddRecommendationCommand(
            f"pizza",  # itemid
            f"http://example.com",  # url
            f"unique-andsteve",#uniqieusermatch
            nu.isoformat(),  # date

        )
    )

    print(bus.uow.recommendations.get_by_title(f"Test"))

    # assert
    assert bus.uow.recommendations.get_by_title(f"Test") is not None
    assert bus.uow.committed


# def test_get_recommendation_by_id():
#     bus = boostrap_test_app()

#     nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)

#     # add one
#     bus.handle(
#         commands.AddRecommendationCommand(
#             f"pizza",  # itemid
#             f"http://example.com",  # url
#             f"unique-andsteve",#uniqieusermatch
#             nu.isoformat(),  # date
#         )
#     )

#     assert bus.uow.recommendations.get_by_id(99) is not None
#     assert bus.uow.committed


# def test_get_recommendation_by_url():
#     bus = boostrap_test_app()

#     nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)

#     # add one
#     bus.handle(
#         commands.AddRecommendationCommand(
#             f"pizza",  # itemid
#             f"http://example.com",  # url
#             f"unique-andsteve",#uniqieusermatch
#             nu.isoformat(),  # date
#         )
#     )

#     assert bus.uow.recommendations.get_by_url(f"http://example.com") is not None
#     assert bus.uow.committed


# def test_get_all_recommendations():
#     bus = boostrap_test_app()

#     nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)
#     bus.handle(
#         commands.AddRecommendationCommand(
#             f"pizza",  # itemid
#             f"http://example.com",  # url
#             f"unique-andsteve",#uniqieusermatch
#             nu.isoformat(),  # date
#         )
#     )

#     nuto = nu + timedelta(days=2, hours=12)

#     bus.handle(
#         commands.AddRecommendationCommand(
#             f"pizza",  # itemid
#             f"http://example.com",  # url
#             f"unique-andsteve",#uniqieusermatch
#             nu.isoformat(),  # date
#         )
#     )

#     records = bus.uow.recommendations.get_all()
#     assert len(records) == 2