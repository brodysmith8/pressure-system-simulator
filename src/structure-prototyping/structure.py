from volume import Volume


# structure would be a bundle of connections
class Structure:
    def __init__(self, internal_volume: float, name: str) -> None:
        self.initial_name = name
        self.internal_volume: Volume = Volume(internal_volume)  # can only ever have static volume
        self.internal_pressure: float = 0.0
        self.max_output_pressure: float = float("inf")
        self.inputs: list[Structure] = []
        self.outputs: list[Structure] = []
        self.times_counted = 0
        self.is_root: bool = False
        self.nodal_volume_requirement = Volume(internal_volume)  # important to make diff from internal_volume
        self.per_output_volume_requirement = []  # will have a 1:1 mapping with self.outputs -> new data structure
        self.name = self.initial_name
        # self.name = f'{self.initial_name} NV: {self.nodal_volume_requirement} m3'

    def add_input(self, component) -> None:
        self.inputs.append(component)
        if component.is_root:
            # because it's a storage structure
            self.nodal_volume_requirement.static_volume -= self.internal_volume.static_volume
        component.add_output(self)

    def add_output(self, component) -> None:
        self.outputs.append(component)

    def add_downstream_nodal_volume(self, downstream_structure) -> None:
        if self.is_root:
            return
        self.per_output_volume_requirement.append(downstream_structure)
        self.nodal_volume_requirement += downstream_structure.nodal_volume_requirement
        self.name = f'{self.initial_name} NV: {self.nodal_volume_requirement.total():.2f} m3'

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name
