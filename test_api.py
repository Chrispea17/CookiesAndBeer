# import time
# from pathlib import Path
# from datetime import date
# import pytest
# import requests
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, clear_mappers
# from tenacity import retry, stop_after_delay
# from recommendations import Recommendation

# from orm import metadata, start_mappers
import config
# import flaskapi
from recommendations import Recommendation

# def post_to_add_recommendation(itemID, uniqueUserMatchID, findItem, date):
#     url = config.get_api_url()
#     r = requests.post(
#         f"{url}/recommendation", json={"itemID": itemID, "uniqueUserMatchID": uniqueUserMatchID, "findItem": findItem, "date": date}
#     )
    
import pytest
import requests
import flaskapi

LOCALHOST = "http://127.0.0.1:5000/"

@pytest.mark.usefixtures('restart_api')
def test_api_can_connect():
    res = requests.get(LOCALHOST)
    assert res != None

@pytest.mark.usefixtures('restart_api')
def test_happy_path_returns_200_or_201_and_recommendation(add_stock):


# @pytest.mark.usefixtures('in_memory_sqlite_db')
# def test_api_runs():
#     recommendation = Recommendation(4,4,"url.com",date=date(2020,7git s,25))
#     post_to_add_recommendation(4,4,"url.com", "7-25-2020")
#     data = {"itemID": 4, "uniqueUserMatchID": 4, "findItem": 'url.com', "date": 7-25-2020}
#     url = config.get_api_url()
#     r = requests.post(f"{url}", json=data)
#     assert r.status_code == 201