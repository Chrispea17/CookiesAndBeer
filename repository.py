from abc import ABC, abstractmethod
import abc
from recommendations import MatchUsers, Recommendation
# import recommendations
import orm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# class AbstractRepository(ABC):
#     def __init__(self):
#         self.seen = set()

#     def add(self, recommendation: Recommendation):
#         self._add(recommendation)

#     def get_by_item(self, itemID: str) -> list[Recommendation]:
#         recommendations = self._get(itemID)
#         if recommendations:
#             self.seen.add(recommendations)
#         return recommendations

#     @abstractmethod
#     def _add(self, recommendation: Recommendation):
#         raise(NotImplementedError)

#     @abstractmethod
#     def _get(self, itemID) -> list[Recommendation]:
#         raise NotImplementedError

#     @abstractmethod
#     def _edit(self, recommendation: Recommendation):
#         found = self.get(recommendation.reference)
#         if found:
#             pass

# class SqlAlchemyRepository(AbstractRepository):
#     def __init__(self, url=None) -> None:
#         super().__init__()

#         self.engine = None

#         # create db connection
#         if url != None:
#             self.engine = create_engine(url)
#         else:
#             # let's default to in-memory for now
#             self.engine = create_engine("sqlite:///:memory:", echo=True)

#         # ensure tables are there
#         Base.metadata.create_all(self.engine)

#         # obtain session
#         # the session is used for all transactions
#         self.Session = sessionmaker(bind=self.engine)


#     def _add(self, recommendation: Recommendation):
#         pass
#         # raise(NotImplementedError)

#     def _get(self, itemID) -> list[Recommendation]:
#         pass
#         # raise NotImplementedError

#     def _edit(self, recommendation: Recommendation):
#         found = self.get(recommendation.reference)
#         if found:
#             pass

#     def add_one(self, recommendation: Recommendation) -> int:
#         self.Session.add(recommendation)
#         self.Session.commit()
#         pass

#     def add_many(self, recommendation: list[Recommendation]) -> int:
#         self.Session.add(recommendation)
#         pass

#     def delete_one(self, recommendation) -> int:
#         pass

#     def delete_many(self, recommendation) -> int:
#         pass

#     def update(self, recommendation) -> int:
#         pass

#     def update_many(self, recommendation) -> int:
#         pass

#     def find_first(self, query) -> Recommendation:
#         pass

#     def find_all(self, query) -> list[Recommendation]:
#         pass


# class RecommendationRepository(AbstractRepository):
#     def __init__(self, session):
#         self.session = session

#     def add(self, recommendation):
#             self.session.add(recommendation)

#     def get(self, reference):
#         return self.session.query(recommendations.Recommendation).filter_by(reference=reference)

#     def getlist(self):
#         return list(self.session.query(recommendations.Recommendation).all())

#     def matchlist(self, recommendations, matchid):
#         return self.session.query(recommendations.Recommendation).all().filter_by(matchid)

"""
With Chapter 06 instead of Barky
"""
class AbstractRepository(ABC):
    @abc.abstractmethod
    def add(self, recommendation: Recommendation):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> Recommendation:
        raise NotImplementedError
    
    @abc.abstractmethod
    def select_for_update(self, reference)->Recommendation:
        raise NotImplementedError

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session
    
    def add(self, recommendation):
        self.session.add(recommendation)
        self.session.commit()
    
    def get(self,reference):
        return self.session.query(Recommendation).filter(Recommendation.reference==reference)

    def list(self):
        return self.session.query(Recommendation).all()
    
    def select_for_update(self, reference) -> Recommendation:
        return self.session.query(Recommendation).filter(Recommendation.reference==reference).one()
    
    def filtered_list(self, itemID):
        return self.session.query(Recommendation).filter(Recommendation.itemID==itemID).all()