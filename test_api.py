# # import time
# # from pathlib import Path
# # from datetime import date
# # import pytest
# # import requests
# # from sqlalchemy import create_engine
# # from sqlalchemy.orm import sessionmaker, clear_mappers
# # from tenacity import retry, stop_after_delay
# # from recommendations import Recommendation

# # from orm import metadata, start_mappers
# from ntpath import join
# import config
# # import flaskapi
# from recommendations import Recommendation

# # def post_to_add_recommendation(itemID, uniqueUserMatchID, findItem, date):
# #     url = config.get_api_url()
# #     r = requests.post(
# #         f"{url}/recommendation", json={"itemID": itemID, "uniqueUserMatchID": uniqueUserMatchID, "findItem": findItem, "date": date}
# #     )
    
# import pytest
# import requests
# import flaskapi
# from config import get_api_url
# import uuid
# import pytest
# import requests
# import random
# import config


def random_suffix():
    return uuid.uuid4().hex[:6]

def random_number(seed):
    return random.seed(seed)

def random_reference(name=""):
    name=int(name)
    return int(f'{name}{random.randint(0,11145)}')


def random_userMatch(name=""):
    return f"sku-{name}-{random_suffix()}"


def random_itemID(name=""):
    return f"batch-{name}-{random_suffix()}"


def random_url(name=""):
    return f"order-{name}-{random_suffix()}-.com"

def random_rank():
    return random.randint(0,1)

# LOCALHOST = "http://127.0.0.1:5000/"

# @pytest.mark.usefixtures('restart_api')
# def test_api_can_connect():
#     res = requests.get(LOCALHOST)
#     assert res != None

# @pytest.mark.usefixtures('restart_api')
# def test_happy_path_returns_200_or_201_and_recommendation(add_stock):
# @pytest.mark.usefixtures('restart_api')
# def test_api_returns_first_ranking(add_ranking):
#     add_ranking(
#         [
#             ("sku", random_userMatch("betty"), random_url(), "2011-01-02"),
#             ("sku", random_userMatch("bob"), random_url(), "2011-01-01"),
#             ("othersku", random_userMatch("barry"), random_url(), "2022-01-01"),
#         ])
#     data = {"_rank":random_rank(), "itemID":"othersku"}
#     url = config.get_api_url()
#     r = requests.post(f'{url}/ranked_users', json = data)
#     assert r.status_code==201
#     assert r.json()['recref'] == first_recommendation

# @pytest.mark.usefixtures('in_memory_sqlite_db')
# def test_api_runs():
#     recommendation = Recommendation(4,4,"url.com",date=date(2020,7git s,25))
#     post_to_add_recommendation(4,4,"url.com", "7-25-2020")
#     data = {"itemID": 4, "uniqueUserMatchID": 4, "findItem": 'url.com', "date": 7-25-2020}
#     url = config.get_api_url()
#     r = requests.post(f"{url}", json=data)
#     assert r.status_code == 201