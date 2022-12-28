class System:
    def __init__(self) -> None:
        self._components = [] 

    def add_subsystem(self, subsystem) -> None:
        self._components.append(subsystem)

    # process for advancing to the next discrete state
    def advance(self) -> None:
        pass