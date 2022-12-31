from simulation import Simulation
from decimal import Decimal
from system import System
from vessel import Vessel
from pipe import Pipe

# assemble System as per the system diagram detailed in the readme
root_system = System()

# gas vessels will have the same volume. Equilibrium volume of both will be 5000 L
compressed_pressure_vessel_one = Vessel(Decimal(10000.0))
compressed_pressure_vessel_two = Vessel(Decimal(10000.0))

# pipe
vessel_one_to_vessel_two = Pipe(compressed_pressure_vessel_one, compressed_pressure_vessel_two)

root_system.add_subsystem(vessel_one_to_vessel_two)

# initiate the Simulation of the System
simulation = Simulation(root_system)

simulation.run()
