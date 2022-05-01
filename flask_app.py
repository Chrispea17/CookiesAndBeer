 
from datetime import datetime
from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from allocation.domain import model
from allocation.adapters import orm
import services, unitofwork

app = Flask(__name__)
orm.start_mappers()

app.route("/submit_recommendation", methods=["POST"])
def add_recommendation():
    date = request.json["date"]
    if date is not None:
        date = datetime.fromisoformat(date).date()
    services.add_recommendation(
        request.json["uniqueUserMatchID"],
        request.json["itemID"],
        request.json["findItem"],
        date,
        unitofwork.SqlAlchemyUnitOfWork(),
    )
    return "OK", 201

if (__name__)==("__main__"):
    app.run()