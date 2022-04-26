from datetime import datetime
import json
import commands

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return f'APIS'

@app.route('/submit')
def submit_recommendation():
    return f'submit your recommendation'

# @app.route('/view_item_recommendations/<id>', methods=['GET'])
# def list_recommendations_by_itemID():

@app.route('/add_recommendation', methods=['POST'])
def add_confirm_and_remove_bookmark():
    itemID: str
    uniqueUserMatchID: str
    findItem: str
    date: str


#     # title, url, notes, date_added, date_edited
#     data = request.get_json()
#     id = data["id"]
#     title = data["title"]
#     url = data["url"]
#     date = data["date_added"]


    cmd = commands.AddRecommendationCommand(
            itemID, uniqueUserMatchID, findItem, date
    )
    # bus.handle(cmd)
    # return "OK", 201


# @app.route("/bookmarks/<title>", methods=['GET'])
# def get_bookmark_by_title(title):
#     result = views.bookmarks_view(title, bus.uow)
#     if not result:
#          return "not found", 404
#     return jsonify(result), 200

# def get_bookmark_by_id( title):
#     pass

# def delete(bookmark):
#     pass

# def update(bookmark):
#     pass

if __name__ == "__main__":
    app.run()