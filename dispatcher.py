from events.event import Event
from event_handlers.event_handler import EventHandler


class Dispatcher:
    """Class that registers and dispatches events over event handlers"""

    handlers = list()

    def register(self, handler: EventHandler):
        self.handlers.append(handler)

    def dispatch(self, event: Event):
        for handler in self.handlers:
            if handler.accepts(event):
                handler.handle(event)
                break
