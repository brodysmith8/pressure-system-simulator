from simulation import Decimal

class Vessel:
    # flow_rate and leak_rate in L/min, volume in L 
    def __init__(self, volume : Decimal) -> None:
        self.volume = volume

    # called every frame like unity lol
    def update(self) -> None:
        pass

    def __str__(self) -> str:
        return f'Volume: {self.volume} L'
