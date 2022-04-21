import abc
from recommendations import MatchUsers, Recommendation
import recommendations



class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, recommendation: recommendations.Recommendation):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> recommendations.Recommendation:
        raise NotImplementedError
    

class RecommendationRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, recommendation):
            self.session.add(recommendation)

    def get(self, reference):
        return self.session.query(recommendations.Recommendation).filter_by(reference=reference).one()

    def getlist(self):
        return list(self.session.query(recommendations.Recommendation).all())

    def matchlist(self, recommendations, matchid):
        return self.session.query(recommendations.Recommendation).all().filter_by(matchid)



class FakeRecommendationRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, recommendation):
            self.session.add(recommendation)

    def get(self, reference):
        return self.session.query(recommendations.Recommendation).filter_by(reference=reference).one()

    def getlist(self):
        return list(self.session.query(recommendations.Recommendation).all())

    def matchlist(self, recommendations, matchid):
        return self.session.query(recommendations.Recommendation).all().filter_by(matchid)