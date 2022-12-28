from decimal import Decimal, getcontext
getcontext().prec = 12
from time import sleep
import configparser
from system import System

class Simulation:
    def __init__(self, system: System) -> None:
        self._cfg = configparser.ConfigParser()
        self._cfg.read('config.ini')

        # time config
        self._cfg_simulation = self._cfg['Simulation Settings']
        self._SIMULATION_TIME_SCALE_FACTOR = Decimal(self._cfg_simulation['SIMULATION_TIME_SCALE_FACTOR'])
        self.SIMULATION_TIMESTEP_LENGTH_SECONDS = Decimal(self._cfg_simulation['SIMULATION_TIMESTEP_LENGTH_SECONDS']) # represents the sim time elapsed

        if self.SIMULATION_TIMESTEP_LENGTH_SECONDS * self._SIMULATION_TIME_SCALE_FACTOR == 1.0:
            self._SIMULATION_IS_REALTIME = True
        else:
            self._SIMULATION_IS_REALTIME = False

        self._SIMULATION_TIMESTEP_REAL_LENGTH_SECONDS = float(self.SIMULATION_TIMESTEP_LENGTH_SECONDS / self._SIMULATION_TIME_SCALE_FACTOR) # represents the real time

        # meta stuff 
        self._time_elapsed = Decimal(0.0)
        self._time_step_id = 0
        self._is_running = False 

        # topology of simulation objects
        self._simulation_system = system

        # print the simulation configuration
        self.print_settings()

    # dumb
    def print_settings(self) -> None:
        print('----- [SIM INIT] Simulation Settings -----')
        print(f'_SIMULATION_TIME_SCALE_FACTOR: \t\t\t{self._SIMULATION_TIME_SCALE_FACTOR}')
        print(f'SIMULATION_TIMESTEP_LENGTH_SECONDS: \t\t{self.SIMULATION_TIMESTEP_LENGTH_SECONDS}')
        print(f'_SIMULATION_IS_REALTIME: \t\t\t{self._SIMULATION_IS_REALTIME}')
        print(f'_SIMULATION_TIMESTEP_REAL_LENGTH_SECONDS: \t{self._SIMULATION_TIMESTEP_REAL_LENGTH_SECONDS}')
        print(f'root _simulation_system address: \t\t{self._simulation_system}')
        print('------------- [END SIM INIT] -------------\n')


    def run(self) -> None:
        self._is_running = True

        # can implement parallelism here for faster performance if i want to
        while(self._is_running):
            print(f'[SIM META] TIMESTEP {self._time_step_id} START')
            
            self._simulation_system.advance()

            # Meta Updates
            print(f'[SIM META] TIMESTEP {self._time_step_id} END, elapsed: {self._time_elapsed} s\n')
            self._time_step_id += 1
            self._time_elapsed += self.SIMULATION_TIMESTEP_LENGTH_SECONDS
            sleep(self._SIMULATION_TIMESTEP_REAL_LENGTH_SECONDS) 