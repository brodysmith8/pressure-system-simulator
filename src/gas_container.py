from decimal import Decimal
from gas import Gas


class GasContainer():
    def __init__(self, volume: Decimal = Decimal(0.0)) -> None:
        print('[GasContainer] called')
        self.volume = Decimal(volume)
        self.gas = Gas(self.volume)
        self.gas.volume = self.volume

    def fill(self, mols_to_add: Decimal):
        self.gas.add_gas_moles(mols_to_add)

    def remove(self, mols_to_remove: Decimal):
        self.gas.remove_gas_moles(mols_to_remove)

    def __str__(self) -> str:
        internal_volume = f'\t-> Internal volume: {self.volume} L'
        gas = f'\n\t-> Gas volume: {self.gas.volume} L'
        internal_pressure = f'\n\t-> Gas pressure: {self.gas.pressure} kPa'
        gas_address = f'\n\t-> Gas instance at: {self.gas}'
        return f'[GasContainer] This container has:\n{internal_volume}{gas}{internal_pressure}{gas_address}'


# gas test
# gas_container = GasContainer()
# print(f'\n--- no volume, no gas:\n{gas_container}')

# gas_container = GasContainer(Decimal(10))
# print(f'\n--- 10 Litres, no gas:\n{gas_container}')

# gas_container = GasContainer(Decimal(10))
# gas_container.gas.add_gas_moles(Decimal(2))
# print(f'\n--- 10 Litres, 2 moles gas:\n{gas_container}')

# gas_container.fill(Decimal(2))
# print(f'\n--- 10 Litres, 4 moles gas (filled):\n{gas_container}\n')
