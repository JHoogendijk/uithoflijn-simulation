import math
from queue import Queue

from event_queue import EventQueue
from events.tram_left_depot import TramLeftDepotEvent
from dispatcher import Dispatcher

event_queue = EventQueue()


class App:

    time_interval = 5
    turn_around_time = 3

    def __init__(self):
        self.initialise_queue()
        self.run_simulation()
        self.calculate_performance_measures()

    def initialise_queue(self):
        # Schedule tram leaves from depot events using the given interval for as many as are required
        for i in range(0, math.ceil((17 + self.turn_around_time)/5)):
            TramLeftDepotEvent(self.time_interval * i).schedule()
        # Schedule a first passenger arrival at each station
        # TODO Schedule a first passenger arrival at each station
        pass

    def run_simulation(self):
        dispatcher = Dispatcher()
        while not event_queue.empty():
            event = event_queue.get()
            dispatcher.dispatch(event)

    def calculate_performance_measures(self):
        pass
