import sys
from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

import requests


class Command(ABC):
    pass

@dataclass
class AddRecommendationCommand(Command):
    """
    This command is a dataclass that encapsulates a Recommendation
    This uses type hints: https://docs.python.org/3/library/typing.html
    """
    itemID: int
    date: str
    findItem: str
    uniqueUserMatchID: str



# @dataclass
# class ListRecommendationsCommand(Command):
#     order_by: str
#     order: str


# @dataclass
# class DeleteBookmarkCommand(Command):
#     id: int


# @dataclass
# class EditBookmarkCommand(Command):
#     id: int
#     title: str
#     url: str
#     # data["date_added"] = datetime.utcnow().isoformat()
#     date_added: str
#     date_edited: str
#     notes: Optional[str] = None