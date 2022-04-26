from __future__ import annotations
from dataclasses import asdict
from typing import List, Dict, Callable, Type, TYPE_CHECKING

import commands, events, recommendations, unitofwork

if TYPE_CHECKING:
    from . import unit_of_work

def add_recommendation(
    cmd: commands.AddRecommendationCommand,
    uow: unitofwork.AbstractUnitOfWork,
):
    with uow:

        recommendation = None

        # look to see if we already have this Recommendation as the title is set as unique
        try:
            # we place this in a try block in case we are using SQLAlchemy
            Recommendation = uow.recommendations.get(recommendation)

            # checks to see if the list is empty
            if not Recommendation:
                Recommendation = recommendations.Recommendation(
                    cmd.itemID, cmd.uniqueUserMatchID, cmd.findItem, cmd.date,
                )
                uow.recommendations.add(recommendation)            
        except:
            Recommendation = recommendations.Recommendation(
                cmd.itemID, cmd.uniqueUserMatchID, cmd.findItem, cmd.date,
            )
            uow.recommendations.add(recommendation)

        uow.commit()

# ListRecommendationsCommand: order_by: str order: str
def list_recommendations(
    cmd: commands.ListRecommendationsCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    Recommendations = None
    with uow:
        Recommendations = uow.Recommendations.all()
        
    return Recommendations


# DeleteRecommendationCommand: id: int
def delete_recommendation(
    cmd: commands.DeleteRecommendationCommand,
    uow: unitofwork.AbstractUnitOfWork,
):
    with uow:
        pass


# EditRecommendationCommand(Command):
def edit_recommendation(
    cmd: commands.EditRecommendationCommand,
    uow: unitofwork.AbstractUnitOfWork,
):
    with uow:
        pass


EVENT_HANDLERS = {
    events.RecommendationAdded: [add_recommendation],
    events.RecommendationsListed: [list_recommendations],
    events.RecommendationDeleted: [delete_recommendation],
    events.RecommendationEdited: [edit_recommendation],
}  # type: Dict[Type[events.Event], List[Callable]]

COMMAND_HANDLERS = {
    commands.AddRecommendationCommand: add_recommendation,
    commands.ListRecommendationsCommand: list_recommendations,
    commands.DeleteRecommendationCommand: delete_recommendation,
    commands.EditRecommendationCommand: edit_recommendation,
}  # type: Dict[Type[commands.Command], Callable]

