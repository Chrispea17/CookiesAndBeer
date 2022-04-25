from pickle import TRUE
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqla_repository import *
from baseapi import AbstractRecommendationAPI

# init from dotenv file
# from dotenv import load_dotenv
# load_dotenv()

app = Flask(__name__)

class FlaskRecommendationAPI(AbstractRecommendationAPI):
    """
    Flask 
    """
    def __init__(self) -> None:
        super().__init__()
    
    @app.route('/')
    def index(self):
        return f'MyRecommendation'

    # @app.route('/api/one/<id>')
    # def one(self, id):
    #     return f'The provided id is {id}'

    # @app.route('/api/all')
    # def all(self):
    #     return f'all records'

    # @app.route('/api/first/<property>/<value>/<sort>')
    # def first(self, filter, value, sort):
    #     return f'the first '
    #     pass
    
    # def many(self, filter, value, sort):
    #     pass
    
    # def add(recommendation):
    #     pass

    # def delete(recommendation):
    #     pass

    # def update(recommendation):
    #     pass


if __name__=="__main__":
    app.run(debug=TRUE)