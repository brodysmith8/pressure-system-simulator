# structure would be a bundle of connections
class Structure:
    def __init__(self, internal_volume: float, name: str) -> None:
        self.initial_name = name
        self.internal_volume: float = internal_volume
        self.internal_pressure: float = 0.0
        self.max_output_pressure: float = float("inf")
        self.inputs: list[Structure] = []  # circular only if we initialize Connection objects
        self.outputs: list[Structure] = []  # circular only if we initialize Connection objects
        self.times_counted = 0
        self.is_root: bool = False
        self.nodal_volume_requirement = self.internal_volume
        self.per_output_volume_requirement = []  # will have a 1:1 mapping with self.outputs -> new data structure
        self.name = self.initial_name
        # self.name = f'{self.initial_name} NV: {self.nodal_volume_requirement} m3'

    def add_input(self, component) -> None:
        self.inputs.append(component)
        component.add_output(self)

    def add_output(self, component) -> None:
        self.outputs.append(component)

    # need to start with the last element and move backwards.
    # do this in reverse BFS
    def calculate_nodal_volume_requirement(self) -> None:
        self.times_counted += 1
        string = f'{self.initial_name},'
        string += f'times counted: {self.times_counted},'
        string += f' current nodal vol: {self.nodal_volume_requirement}'
        print(string)
        if self.is_root:
            return
        self.per_output_volume_requirement = []
        self.nodal_volume_requirement = self.internal_volume
        for output in self.outputs:
            self.per_output_volume_requirement.append(output.nodal_volume_requirement)
        self.nodal_volume_requirement += sum(self.per_output_volume_requirement)
        self.name = f'{self.initial_name} NV: {self.nodal_volume_requirement:.2f} m3'

    def add_downstream_nodal_volume(self, downstream_structure) -> None:
        self.per_output_volume_requirement.append(downstream_structure)
        self.nodal_volume_requirement += downstream_structure.nodal_volume_requirement
        # self.name = f'{self.initial_name} NV: {self.nodal_volume_requirement} m3'

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name
