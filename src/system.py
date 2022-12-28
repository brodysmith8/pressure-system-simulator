from copy import deepcopy

class System:
    def __init__(self) -> None:
        self._components: list[System] = []
        self.parent_system: System = self # if self.parent_system = self, we know we are at the root

    def add_subsystem(self, subsystem) -> None:
        subsystem.parent_system = self
        self._components.append(subsystem)

    # process for advancing to the next discrete state
    def advance(self) -> None:
        self.last_state = deepcopy(self) # captures our current state before calculating the next state
        self.update()
        for child in self._components:
            child.advance()
        del self.last_state # do this to stop compound copying (very slow) 

    # return None by default if this system only composes subsystems
    # has no function. update() will be implemented only for the
    # lowest level systems.  
    def update(self) -> None:
        print(f'System with ID {id(self)} updates, ID of parent system is {id(self.parent_system)}')
        return None