from .location import Location
from .character import Character

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

        # Travel stuff
        self.travel_origin = "Kliron"
        self.travel_destination = None
        self.travel_progress = 0

        # Travel costs more one way because uphill.
        self.distances = {("Kliron", "Brine"): 4, ("Brine", "Kliron"): 2}

        self.prompt = "You find yourselves in a sprawling city. Would you like to go get the MacGuffin?"
        self.party = []

    def advance_travel(self):
        speed = min(i.travel_speed for i in party)