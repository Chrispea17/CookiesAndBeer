from abc import ABC, abstractmethod
import abc
from recommendations import MatchUsers, Recommendation
# import recommendations
import orm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
    def list_recommendations(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def list_rated_recommendations(self):
        raise NotImplementedError

    @abc.abstractmethod
    def select_for_update(self, reference)->Recommendation:
        raise NotImplementedError

    @abc.abstractmethod
    def add_match(self, match:MatchUsers):
        raise NotImplementedError

    @abc.abstractmethod
    def get_match(self,matchid):
        raise NotImplementedError
        
    @abc.abstractmethod
    def list_matches(self):
        raise NotImplementedError
         
    @abc.abstractmethod   
    def select_for_update_match(self, reference) -> MatchUsers:
        return self.session.query(MatchUsers).filter(reference==reference).with_for_update().one()

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session
    
    def add(self, recommendation):
        self.session.add(recommendation)
        self.session.commit()
    
    def get(self,reference):
        return self.session.query(Recommendation).filter(Recommendation.reference==reference)

    def list_recommendations(self):
        return self.session.query(Recommendation).all()
    
    def list_rated_recommendations(self):
        return self.session.query(Recommendation).filter(Recommendation._recommendationRating!=None).all()
    
    def select_for_update(self, reference) -> Recommendation:
        return self.session.query(Recommendation).filter(Recommendation.reference==reference).one()
    
    def filtered_item_list(self, itemID):
        return self.session.query(Recommendation).filter(Recommendation.itemID==itemID).all()

    def filtered_recommendation_list(self, uniqueUserMatch):
        return self.session.query(Recommendation).filter(Recommendation.uniqueUserMatchID==uniqueUserMatch).all()

    def add_match(self, match):
        self.session.add(match)
        self.session.commit()

    def get_match(self,matchid):
        return next(b for b in self.session.query(MatchUsers) if b.reference==matchid)

    def list_matches(self):
        return self.session.query(MatchUsers).all()

    def select_for_update_match(self, reference) -> MatchUsers:
        return self.session.query(MatchUsers).filter(reference==reference).with_for_update().one()

# class AbstractMatchRepository(ABC):
#     # @abc.abstractmethod
    # def add(self, match: MatchUsers):
    #     raise NotImplementedError

    # @abc.abstractmethod
    # def get(self, reference) -> MatchUsers:
    #     raise NotImplementedError
    
    # @abc.abstractmethod
    # def select_for_update(self, reference)->MatchUsers:
    #     raise NotImplementedError


# class SqlAlchemyMatchRepository(AbstractMatchRepository):
#     def __init__(self, session):
#         self.session = session
    
#     def add(self, match):
#         self.session.add(match)
#         self.session.commit()
    
#     def get(self,reference):
#         return self.session.query(MatchUsers).filter(MatchUsers.reference==reference)

#     def list(self):
#         return self.session.query(MatchUsers).all()
    
#     def select_for_update(self, reference) -> MatchUsers:
#         return self.session.query(MatchUsers).filter(MatchUsers.reference==reference).one()
    
