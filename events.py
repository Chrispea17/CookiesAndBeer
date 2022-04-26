from abc import ABC
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

from recommendations import Recommendation



class Event(ABC):
    pass


@dataclass
class RecommendationAdded(Event):
    id: int
    title: str
    url: str
    date_added: str
    Recommendation_notes: Optional[str] = None


@dataclass
class RecommendationEdited(Event):
    id: int
    title: str
    url: str
    date_edited: str
    Recommendation_notes: Optional[str] = None


@dataclass
class RecommendationsListed(Event):
    Recommendations: list[Recommendation]


@dataclass
class RecommendationDeleted(Event):
    Recommendation: Recommendation