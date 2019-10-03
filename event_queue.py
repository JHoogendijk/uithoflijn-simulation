import datetime


class EventQueue:
    """"Class that maintains a queue of events and returns the event happening soonest"""

    events = list()

    """"Adds event to the list"""
    def put(self, item, time: datetime.time):
        self.events.append((item, (time.hour * 60 + time.minute) * 60 + time.second))

    """"Returns the earliest next event"""
    def get(self):
        return min(self.events, key=lambda t: t[1])[0]

    """Returns true if the event list is empty"""
    def empty(self) -> bool:
        return not len(self.events) > 0
