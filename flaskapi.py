from datetime import datetime
import json
import commands
import bootstrap
from flask import Flask, jsonify, request

app = Flask(__name__)
bus = bootstrap.bootstrap()

@app.route('/')
def index():
    return f'Barky API'



@app.route('/make_recommendation', methods=['POST'])
def add_confirm_and_remove_recommendation():


    date : str
    matchID : str
    itemID : str
    url : str
    # _recommendationRating: int = None
    # _rank = 0

#     # title, url, notes, date_added, date_edited
    data = request.get_json()
#     id = data["id"]
    date = data["date"]
    url = data["findItem"]
    itemID = data["itemID"]
    matchID = data["matchID"]

    cmd = commands.AddRecommendation(
            date, url, itemID, matchID,
    )
    bus.handle(cmd)
    return "OK", 201


@app.route("/recommendations/<itemID>", methods=['GET'])
def get_bookmark_by_item(itemID):
   result = views.bookmarks_view(title, bus.uow)
#     if not result:
#          return "not found", 404
#     return jsonify(result), 200

# def get_bookmark_by_id( title):
#     pass

# def delete(bookmark):
#     pass

# def update(bookmark):
#     pass

# if __name__ == "__main__":
#     app.run()