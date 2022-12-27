from decimal import Decimal, getcontext
getcontext().prec = 12
from time import sleep
import configparser

class Simulation:
    def __init__(self) -> None:
        self._cfg = configparser.ConfigParser()
        self._cfg.read('config.ini')

        # time config
        self._cfg_simulation = self._cfg['Simulation Settings']
        self._SIMULATION_TIME_SCALE_FACTOR = Decimal(self._cfg_simulation['SIMULATION_TIME_SCALE_FACTOR'])

        if self._SIMULATION_TIME_SCALE_FACTOR == 1.0:
            self._SIMULATION_IS_REALTIME = True
        else:
            self._SIMULATION_IS_REALTIME = False

        self.SIMULATION_TIMESTEP_LENGTH_SECONDS = Decimal(self._cfg_simulation['SIMULATION_TIMESTEP_LENGTH_SECONDS']) # represents the sim time elapsed
        self._SIMULATION_TIMESTEP_REAL_LENGTH_SECONDS = float(self.SIMULATION_TIMESTEP_LENGTH_SECONDS / self._SIMULATION_TIME_SCALE_FACTOR) # represents the real time

        # meta stuff 
        self._time_elapsed = Decimal(0.0)
        self._time_step_id = 0
        self._is_running = False 

        #
        #self.


    def run(self) -> None:
        self._is_running = True

        # can implement parallelism here for faster performance if i want to
        while(self._is_running):
            print(f'Timestep: {self._time_step_id}, Time Elapsed: {self._time_elapsed} s')
            
            #for item in self._prioritized_simulation_objects:
            #    item.update()

            # Meta Updates
            self._time_step_id += 1
            self._time_elapsed += self.SIMULATION_TIMESTEP_LENGTH_SECONDS;
            sleep(self._SIMULATION_TIMESTEP_REAL_LENGTH_SECONDS) 