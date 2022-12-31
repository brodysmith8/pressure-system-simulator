from decimal import Decimal, getcontext
getcontext().prec = 8


class Gas:
    # will have pressure calculation
    def __init__(self,
                 occupiable_volume: Decimal = Decimal(0.0),
                 amount_of_substance_mols: Decimal = Decimal(0.0)) -> None:
        self.volume = Decimal(occupiable_volume)  # i think gas just occupies whatever volume is available
        self.n = Decimal(amount_of_substance_mols)
        self.R = Decimal(8.314)  # J/(mol K)
        self.T = Decimal(25) + Decimal(273.15)
        self.volume_in_litres = True
        self.pressure = self.calcute_pressure()

    def update(self) -> None:
        if self.volume == Decimal(0.0) and self.n > 0:
            raise Exception("A gas cannot be present if there is no occupiable volume.")

        self.pressure = self.calcute_pressure()

    # PV = nRT
    def calcute_pressure(self) -> Decimal:
        if self.volume == Decimal(0.0):
            return Decimal(0)

        litres_to_cubic_metres_multiplier = Decimal(1)
        if self.volume_in_litres:
            litres_to_cubic_metres_multiplier = Decimal(1) / Decimal(1000)

        return (self.n * self.R * self.T) / (litres_to_cubic_metres_multiplier * self.volume)

    def add_gas_moles(self, moles_to_add: Decimal) -> None:
        self.n += moles_to_add
        self.pressure = self.calcute_pressure()

    def remove_gas_moles(self, moles_to_remove: Decimal) -> None:
        if moles_to_remove > self.n:
            self.n = Decimal(0)
            self.pressure = Decimal(0)
            return

        self.n -= moles_to_remove
        self.pressure = self.calcute_pressure()
