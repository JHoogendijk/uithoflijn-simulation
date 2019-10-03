from .event import Event


class TramDepartedEvent(Event):
    """Class for scheduling the TramDeparted event"""

    name = "TramDeparted"

    def __init__(self, current, to):
        self.current = current
        self.to = to

    def timeout(self):
        return 0
