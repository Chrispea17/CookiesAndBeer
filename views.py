 
from services import unit_of_work


def recommendations_view(recommendation: str, uow: unit_of_work.SqlAlchemyUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT uniqueUserMatchID, url FROM bookmars WHERE title = :title
            """,
            dict(uniqueUserMatchID=uniqueUserMatchID),
        )
    return [dict(r) for r in results]