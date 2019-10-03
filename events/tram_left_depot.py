import app
from .event import Event


class TramLeftDepotEvent(Event):
    """Class for scheduling the TramLeftDepot event"""

    name = "TramLeftDepot"

    def __init__(self, frequency):
        self.frequency = frequency

    def timeout(self):
        return self.frequency
