from decimal import Decimal, getcontext
from system import System
from gas_container import GasContainer
from gas import Gas
# right now, this is using its own import to emulate the precision of a sensor,
#  but will make a sensor class in the future that outsources this
getcontext().prec = 9


class Vessel(System, GasContainer):
    # flow_rate and leak_rate in L/min, volume in L
    def __init__(self, volume: Decimal) -> None:
        print('ves')
        super().__init__()
        self.volume = Decimal(volume)
        self.gas = Gas(volume)
        self.gas.volume = self.volume

    # called every timestep after pipe updates
    def update(self) -> None:
        self.gas.update()

    def __repr__(self) -> str:
        return f'Vessel({self.volume})'

    def __str__(self) -> str:
        vol_str = f'Volume: {self.volume} L'
        # mass_str = f'Mass of Oxygen: {self.oxygen_mass.normalize()} g'
        return f'Vessel with volume: {vol_str} L'
