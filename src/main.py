from simulation import Simulation
from system import System
from vessel import Vessel
from load import Load
from pipe import Pipe

# assemble System as per the system diagram detailed in the readme
root_system = System()

# gas vessel
compressed_pressure_vessel = Vessel(10000.0)

# test load
load = Load()

# pipe
vessel_to_load = Pipe(compressed_pressure_vessel, load)

root_system.add_subsystem(vessel_to_load)

# initiate the Simulation of the System
simulation = Simulation(root_system)

simulation.run()
