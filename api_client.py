import requests
import config

def post_to_add_recommendation(
    date : str,
    matchID : str,
    itemID: str,
    url: str,
):
    url = config.get_api_url()
    r=requests.post(
        f"{url}/make_recommendation",
        json = {
            "date" : date,
            "matchID": matchID,
            "itemID": itemID,
            "findItem": url,
        },
    )
    assert r.status_code ==201

def see_recommendations_for_item(itemID: str):
    url = config.get_api_url()
    return requests.get(f"{url}/recommendations/{itemID}")

def see_ranking(userMatch:str):
    url = config.get_api_url()
    return requests.get(f"{url}/rank/{userMatch}")
