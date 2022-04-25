import uuid
import pytest
import requests
from recommendations import Recommendation
import config
from datetime import date

    
def post_to_add_recommendation(date, uniqueUserMatchID, itemID, findItem):
    url = config.get_api_url()
    r = requests.post(
        f"{url}/add_batch", json={"date": date, "uniqueUserMatchID": uniqueUserMatchID, "itemID": itemID, "findItem": findItem}
    )
    assert r.status_code == 201

@pytest.mark.usefixtures("in_memory_sqlite_db")
@pytest.mark.usefixtures('restart_api')
def test_api_returns_recommendations(add_recommendation):
    post_to_add_recommendation(4,4,"url",date=date(2020,7,25))
    data = {"uniqueUserMatchID": 4,"itemID":4, "findItem":findItem, "date":date}
    url = config.get_sqlite_memory_uri()
    r=requests.post(f"https://127.0.0.0.0:5000/recommendation",json=data)
    print(url)
    assert r.status_code == 201
    assert r.json()["batchref"] == 0


# @pytest.mark.usefixtures("postgres_db")
# @pytest.mark.usefixtures("restart_api")

# def test_unhappy_path_returns_400_and_error_message():
#     unknown_sku, orderid = random_sku(), random_orderid()
#     data = {"orderid": orderid, "sku": unknown_sku, "qty": 20}
#     url = config.get_api_url()
#     r = requests.post(f"{url}/allocate", json=data)
#     assert r.status_code == 400
#     assert r.json()["message"] == f"Invalid sku {unknown_sku}"
