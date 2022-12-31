from system import System
from gas_container import GasContainer
from decimal import Decimal, getcontext
getcontext().prec = 9


class Load(System, GasContainer):
    def __init__(self) -> None:
        super().__init__()
        self.required_rate = Decimal(25)  # L/min, pretend this is a ventilator 0.416667 L/s
        self.required_volume = Decimal(0.416667)  # L. Sim Frequency Hz * 60 s in 1 minute = 1 second
        self.intake_volume = Decimal(0)  # L

    def update(self) -> None:
        if self.intake_volume == self.required_volume:
            print('[Load] Required oxygen volume met.\n' +
                  f'\t\t-> Volume Required: {self.required_volume} L\n' +
                  f'\t\t-> Volume Received: {self.intake_volume} L')
        else:
            print('[Load][ALERT] Required oxygen volume NOT met!\n' +
                  f'\t\t-> Volume Required: {self.required_volume} L\n' +
                  f'\t\t-> Volume Received: {self.intake_volume} L\n' +
                  f'\t\t-> Volume Rec/Req: {Decimal(100) * self.intake_volume/self.required_volume}%')
