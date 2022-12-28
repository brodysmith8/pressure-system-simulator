from decimal import Decimal, getcontext
from system import System
# right now, this is using its own import to emulate the precision of a sensor,
#  but will make a sensor class in the future that outsources this
getcontext().prec = 6


class Vessel(System):
    OXYGEN_DENSITY_AT_STP_G_PER_L = Decimal(1.429)  # g/L

    # flow_rate and leak_rate in L/min, volume in L
    def __init__(self, volume: float) -> None:
        # could add children if there are subsystems that compose this,
        # but no need here
        super().__init__()
        self.volume = Decimal(volume)
        self.oxygen_mass = self.volume * self.OXYGEN_DENSITY_AT_STP_G_PER_L

    # called every timestep
    def update(self) -> None:
        print(f'[Vessel] {self}')
        self.volume -= Decimal(0.1)
        self.oxygen_mass = self.volume * self.OXYGEN_DENSITY_AT_STP_G_PER_L

    def __str__(self) -> str:
        return f'Volume: {self.volume} L, Mass of Oxygen: {self.oxygen_mass} g'
