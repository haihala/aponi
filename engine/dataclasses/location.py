from dataclasses import dataclass

@dataclass
class Location:
    name: str

    # Following properties try to describe the location
    # This is mostly for rolling events
    population: float = 0.5
    technology: float = 0.5
    wilderness: float = 0.5