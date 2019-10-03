from abc import ABC, abstractmethod

from events.event import Event


class EventHandler(ABC):
    """Base class for event handlers"""

    @abstractmethod
    def handle(self, event: Event):
        pass

    @abstractmethod
    def accept(self, event: Event) -> bool:
        pass
