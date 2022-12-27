from decimal import Decimal, getcontext
from time import sleep
import configparser

class Simulation:
    def __init__(self) -> None:
        self._cfg = configparser.ConfigParser()
        self._cfg.read('config.ini')
        self._cfg_simulation = self._cfg['Simulation Settings']
        self._SIMULATION_IS_REALTIME = self._cfg_simulation.getboolean('SIMULATION_IS_REALTIME')
        self._SIMULATION_TIME_SCALE_FACTOR = Decimal(self._cfg_simulation['SIMULATION_TIME_SCALE_FACTOR'])

        if self._SIMULATION_IS_REALTIME and self._SIMULATION_TIME_SCALE_FACTOR != 1.0:
            raise InvalidTimeScaleCombinationError

        if not self._SIMULATION_IS_REALTIME and self._SIMULATION_TIME_SCALE_FACTOR == 1.0:
            self._SIMULATION_IS_REALTIME = True

        self.SIMULATION_TIMESTEP_LENGTH_SECONDS = Decimal(self._cfg_simulation['SIMULATION_TIMESTEP_LENGTH_SECONDS']) # known in unity as "time delta" or something
        self._SIMULATION_TIMESTEP_LENGTH_SECONDS_FLOAT = float(self.SIMULATION_TIMESTEP_LENGTH_SECONDS / self._SIMULATION_TIME_SCALE_FACTOR)
        getcontext().prec = 12 
        self._time_elapsed = Decimal(0.0)
        self._time_step_id = 0
        self._is_running = False 

    def run(self) -> None:
        self._is_running = True

        while(self._is_running):
            print(f'Timestep: {self._time_step_id}, Time Elapsed: {self._time_elapsed} s')

            # Meta Updates
            self._time_step_id += 1
            self._time_elapsed += self.SIMULATION_TIMESTEP_LENGTH_SECONDS;
            sleep(self._SIMULATION_TIMESTEP_LENGTH_SECONDS_FLOAT) 


class InvalidTimeScaleCombinationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    
    def __str__(self) -> str:
        return "Real-time simulation requires a Time Scale Factor of 1.0. Change config.ini"