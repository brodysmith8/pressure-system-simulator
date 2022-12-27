from simulation import Simulation

simulation = Simulation()
print(f'Is the sim operating in real time?: {simulation._SIMULATION_IS_REALTIME}')

simulation.run()