import abc
import recommendations


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, recommendations: recommendations.Recommendation):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> recommendations.Recommendation:
        raise NotImplementedError
    
    @abc.abstractmethod
    def add(self, match_users: recommendations.MatchUsers):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id) -> recommendations.MatchUsers:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, recommendations):
        self.session.add(recommendations)

    def get(self, reference):
        return self.session.query(recommendations.Recommendation).filter_by(reference=reference).one()

    def list(self, recommendations):
        return self.session.query(recommendations.Recommendation).all()

    def add(self, match_users):
        self.session.add(match_users)

    def get(self, id):
        return self.session.query(recommendations.MatchUsers).filter_by(reference=id).one()

    def list(self, match_users):
        return self.session.query(recommendations.MatchUsers).all()