import abc
from abc import abstractmethod
import orm
from recommendations import Recommendation, Base
import recommendations



class AbstractRepository(abc.ABC):
    def __init__(self):
        self.bookmarks = set()

    @abc.abstractmethod
    def add(self, recommendation: Recommendation):
        raise NotImplementedError

    @abc.abstractmethod
    def get(recommendation:Recommendation, query) -> list[Recommendation]:
        raise NotImplementedError
    

class RecommendationRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, recommendation):
            self.session.add(recommendation)

    def get(self, recommendation: Recommendation) ->list[Recommendation]:
        return self.session.query(Recommendation)

    def getlist(self):
        return list(self.session.query(Recommendation).all())

    def matchlist(self, recommendations, matchid):
        return self.session.query(recommendations.Recommendation).all().filter_by(matchid)