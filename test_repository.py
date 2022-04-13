
# from sqlalchemy import Column, ForeignKey, Integer, String, Table, MetaData
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, mapper
import pytest
import recommendations

pytestmark = pytest.mark.usefixtures('mappers')

# def test_repo_can_save_a_recommendation(session):
#     recommendation = recommendations.Recommendation(4,4,"url")
#     repo = repository.SQlalchemyRepository(session)
#     repo.add(recommendation)
#     session.commit()

#     rows = list(session.execute(
#         'SELECT id, matchid, itemID, findItem FROM recommendations'
#     ))
#     assert rows == [[1,4,4,"url"]]