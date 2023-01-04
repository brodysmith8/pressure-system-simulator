# structure would be a bundle of connections
class Structure:
    def __init__(self, internal_volume: float, name: str) -> None:
        self.name = name
        self.internal_volume: float = internal_volume
        self.internal_pressure: float = 0.0
        self.max_output_pressure: float = float("inf")
        self.inputs: list[Structure] = []  # circular only if we initialize Connection objects
        self.outputs: list[Structure] = []  # circular only if we initialize Connection objects

    def add_input(self, component) -> None:
        self.inputs.append(component)
        component.add_output(self)

    def add_output(self, component) -> None:
        self.outputs.append(component)

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name
