from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from baserepository import BaseRepository
from recommendations import Recommendation, Base

class SQLARespository(BaseRepository):
    """
    Uses guidance from the basic SQLAlchemy 1.3 tutorial: https://docs.sqlalchemy.org/en/13/orm/tutorial.html
    """

    def __init__(self, url=None) -> None:
        super().__init__()

        self.engine = None

        # create db connection
        if url != None:
            self.engine = create_engine(url)
        else:
            # let's default to in-memory for now
            self.engine = create_engine('sqlite:///:memory:', echo=True)

        # ensure tables are there
        Base.metadata.create_all(self.engine)

        # obtain session
        # the session is used for all transactions
        self.Session = sessionmaker(bind=self.engine)

    def add_one(self, recommendation: Recommendation) -> int:
        self.Session.add(recommendation)
        self.Session.commit()
        pass

    def add_many(self, recommendations: list[Recommendation]) -> int:
        self.Session.add(recommendations)
        pass

    def delete_one(self, recommendation) -> int:
        pass

    def delete_many(self, recommendations) -> int:
        pass

    def update(self, recommendation) -> int:
        pass

    def update_many(self, recommendations) -> int:
        pass

    def find_first(self, query) -> Recommendation:
        pass

    def find_all(self, query) -> list[Recommendation]:
        pass