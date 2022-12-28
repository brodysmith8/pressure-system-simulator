from simulation import Simulation
from system import System
from vessel import Vessel

# assemble System as per the system diagram detailed in the readme
root_system = System()

# tank test (probably won't stay like this, but
# im testing subsystem nesting right now)
compressed_pressure_vessel = Vessel(10.0)

root_system.add_subsystem(compressed_pressure_vessel)

# initiate the Simulation of the System
# can substitute system for compressed_pressure_vessel here and it still
# works (inheritance was right choice)
simulation = Simulation(root_system)

simulation.run()
