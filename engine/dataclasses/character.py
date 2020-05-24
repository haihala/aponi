from dataclasses import dataclass

@dataclass
class Character:
    name: str
    travel_speed: float

    def travel_verbs(self):
        pass