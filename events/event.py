import datetime
from abc import ABC, abstractmethod

import app
from state_manager import StateManager


class Event(ABC):
    """Base class for events"""

    time = datetime.time()

    """Timeout for scheduling in seconds"""
    @property
    @abstractmethod
    def timeout(self):
        pass

    """Schedules an event in the event queue"""
    def schedule(self):
        self.time = StateManager.currentTime + datetime.timedelta(seconds=self.timeout)
        app.event_queue.put(self, self.time)
