import inspect
from typing import Callable
from orm import start_mappers, metadata
import handlers, unitofwork, messagebus


def bootstrap(
    start_orm: bool = True,
    uow: unitofwork.AbstractUnitOfWork = unitofwork.SqlAlchemyUnitOfWork(),
    # notifications: AbstractNotifications = None,
    # publish: Callable = redis_eventpublisher.publish,
) -> messagebus.MessageBus:

    # if notifications is None:
    #     notifications = EmailNotifications()

    if start_orm:
        start_mappers()

    # dependencies = {"uow": uow, "notifications": notifications, "publish": publish}
    dependencies = {"uow": uow}
    injected_event_handlers = {
        event_type: [
            inject_dependencies(handler, dependencies) for handler in event_handlers
        ]
        for event_type, event_handlers in handlers.EVENT_HANDLERS.items()
    }
    injected_command_handlers = {
        command_type: inject_dependencies(handler, dependencies)
        for command_type, handler in handlers.COMMAND_HANDLERS.items()
    }

    return messagebus.MessageBus(
        uow=uow,
        event_handlers=injected_event_handlers,
        command_handlers=injected_command_handlers,
    )


def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency for name, dependency in dependencies.items() if name in params
    }
    return lambda message: handler(message, **deps)