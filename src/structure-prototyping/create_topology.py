from structure import Structure

# volumes are in m3
# pressure in bar (100 kPa)


class Topology:
    def __init__(self) -> None:
        self.root_node = Structure(0, "root")
        self.root_node.is_root = True

        # if there's only one input and it has 0 volume we know this is storage, or at
        # least we know it's the first level
        bottle = Structure(100.0, "bottle")
        bottle.internal_pressure = 100.0
        bottle.add_input(self.root_node)

        regulator_bottle = Structure(0.02, "regulator_bottle")
        regulator_bottle.max_output_pressure = 6.0
        regulator_bottle.add_input(bottle)

        pipe1 = Structure(0.16, "pipe1")
        pipe1.add_input(regulator_bottle)

        splitter = Structure(0.03, "splitter")
        splitter.add_input(pipe1)

        pipe2 = Structure(0.09, "pipe2")
        pipe2.add_input(splitter)
        regulator_pipe2 = Structure(0.02, "regulator_pipe2")
        regulator_pipe2.max_output_pressure = 1.5
        regulator_pipe2.add_input(pipe2)
        empty_box_pipe2 = Structure(100, "empty_box_pipe2")
        empty_box_pipe2.add_input(regulator_pipe2)

        pipe3 = Structure(0.09, "pipe3")
        pipe3.add_input(splitter)
        empty_box_pipe3 = Structure(100, "empty_box_pipe3")
        empty_box_pipe3.add_input(pipe3)

        pipe4 = Structure(0.09, "pipe4")
        pipe4.add_input(splitter)
        regulator_pipe4 = Structure(0.02, "regulator_pipe4")
        regulator_pipe4.max_output_pressure = 0.75
        regulator_pipe4.add_input(pipe4)

        pipe4_splitter = Structure(0.03, "pipe4_splitter")
        pipe4_splitter.add_input(regulator_pipe4)

        pipe41 = Structure(0.09, "pipe41")
        pipe41.add_input(pipe4_splitter)
        regulator_pipe41 = Structure(0.02, "regulator_pipe41")
        regulator_pipe41.add_input(pipe41)
        empty_box_pipe_41 = Structure(100, "empty_box_pipe41")
        empty_box_pipe_41.add_input(regulator_pipe41)

        pipe42 = Structure(0.09, "pipe42")
        pipe42.add_input(pipe4_splitter)
        empty_box_pipe_42 = Structure(100, "empty_box_pipe42")
        empty_box_pipe_42.add_input(pipe42)

        self.final_leaf = Structure(0, "final_leaf")
        self.final_leaf.add_input(empty_box_pipe2)
        self.final_leaf.add_input(empty_box_pipe3)
        self.final_leaf.add_input(empty_box_pipe_41)
        self.final_leaf.add_input(empty_box_pipe_42)
        self.final_leaf.is_root = True

    def get_root(self) -> Structure:
        return self.root_node

    def get_last_leaf(self) -> Structure:
        return self.final_leaf
