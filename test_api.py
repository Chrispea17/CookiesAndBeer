from datetime import datetime, timezone
from random import *

from api_client import *
import pytest

import config


@pytest.mark.usefixtures("file_sqlite_db")
@pytest.mark.usefixtures("client")
def test_path_correct_returns_201_and_recommendation_added(client):
    nu: datetime = datetime(2022, 4, 20, 0, 0, 0, 0, tzinfo=timezone.utc)
    reference = 0
    url = f"http://myownexample.com"
    itemID = f"pizza"
    matchID = f"brianna-benny"
    date = nu.isoformat()

    url = config.get_api_url()

    r=client.post(
        "/make_recommendation",
        json={
            "date" : date,
            "matchID": matchID,
            "itemID": itemID,
            "findItem": url,
        },
    )
    assert r.status_code ==201