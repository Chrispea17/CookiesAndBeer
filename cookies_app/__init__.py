import os
from pickle import TRUE
from flask import Flask, jsonify, request

from datetime import datetime
import json
import commands

app = Flask(__name__)

def create_app(test_config=None):
    #create and configure my app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev', DATABASE = os.path.join(app.instance_path, 'recommendations.sqlite'))

    if test_config is None:
        app.config.from_pyfile('config.py', silent=TRUE)
    else:
        app.config.from_mapping(test_config)

    try: 
        os.makedirs(app.instance_path)
    except OSError:
        pass


@app.route('/')
def index():
    return f'APIS'

@app.route('/submit')
def submit_recommendation():
    return f'submit your recommendation'

# @app.route('/view_item_recommendations/<id>', methods=['GET'])
# def list_recommendations_by_itemID():


one_item_for_test = [{"itemID": "item-str",
    "uniqueUserMatchID": "match-str",
    "findItem": "url.str",
    "date": "date-str"}] 

@app.route('/add_recommendation', methods=['POST'])
def add_recommendation():
    return jsonify({"Recommendation": one_item_for_test})
    # itemID: str
    # uniqueUserMatchID: str
    # findItem: str
    # date: str

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
    app.run(debug=False,host='0.0.0.0')