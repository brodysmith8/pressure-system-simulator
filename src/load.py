from system import System
from decimal import Decimal


class Load(System):
    def __init__(self) -> None:
        super().__init__()
        self.required_volume = Decimal(345)  # L
        self.required_rate = Decimal(0)  # L/min, pretend this is a ventilator
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
