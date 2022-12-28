from decimal import Decimal, getcontext
from system import System
# right now, this is using its own import to emulate the precision of a sensor,
#  but will make a sensor class in the future that outsources this
getcontext().prec = 9


class Vessel(System):
    OXYGEN_DENSITY_AT_STP_G_PER_L = Decimal(1.429)  # g/L

    # flow_rate and leak_rate in L/min, volume in L
    def __init__(self, volume: float) -> None:
        print(f'context: {getcontext()}')
        # could add children if there are subsystems that compose this,
        # but no need here
        super().__init__()
        self.volume = Decimal(volume)
        self.oxygen_mass = Decimal(self.volume
                                   * self.OXYGEN_DENSITY_AT_STP_G_PER_L)
        self.load_volume = Decimal(0)  # L
        self.output_volume = Decimal(0)  # L

    # called every timestep after pipe updates
    def update(self) -> None:
        print(f'[Vessel] {self}')

        # volume changes
        self.output_volume = self.send()

        self.oxygen_mass = self.volume * self.OXYGEN_DENSITY_AT_STP_G_PER_L

    # send requested gas
    def send(self) -> Decimal:
        if self.volume >= self.load_volume:
            self.volume -= self.load_volume
            return self.load_volume
        else:
            less_volume_than_required = self.volume
            self.volume -= self.volume  # should take us to 0 L
            return less_volume_than_required

    def __str__(self) -> str:
        vol_str = f'Volume: {self.volume} L'
        mass_str = f'Mass of Oxygen: {self.oxygen_mass.normalize()} g'
        return f'{vol_str}, {mass_str}'
