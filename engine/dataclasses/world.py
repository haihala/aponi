from .location import Location

from enum import Enum, auto

class GAME_STATE(Enum):
    TRAVEL = auto()
    COMBAT = auto()
    SOCIAL = auto()
    CAMP = auto()

class World:
    """
    The world is a graph with values for distances between nodes.
    """
    def __init__(self, name):
        self.name = name
        # For demo, simplify the graph to two nodes
        self.locations = {i: Location(i) for i in ["Kliron", "Brine"]}
        self.locations["Kliron"].population = 1
        self.locations["Kliron"].technology = 0.7
        self.locations["Kliron"].wilderness = 0

        self.locations["Brine"].population = 0.1
        self.locations["Brine"].population = 0.1
        self.locations["Brine"].population = 1

        self.situation = GAME_STATE.SOCIAL

        # Travel stuff
        self.party_location = "Kliron"
        self.party_destination = None
        self.party_progress = 0

        # Travel costs more one way because uphill.
        self.distances = {("Kliron", "Brine"): 4, ("Brine", "Kliron"): 2}

        self.setting = "You find yourselves in a sprawling city."

