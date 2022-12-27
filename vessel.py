import time

SIMULATION_FREQUENCY_SECONDS = 1.0

# assume flow rate needs to stay constant 
class Vessel:
    # flow_rate and leak_rate in m3/s, volume in m3 
    def __init__(self, flow_rate, volume, is_leaking = False, leak_rate = 0) -> None:
        self.flow_rate = flow_rate
        self.volume = volume
        self.is_leaking = is_leaking
        self.leak_rate = leak_rate

    # called every frame like unity lol
    def update(self) -> None:
        self.volume -= self.leak_rate # sensor frequency is 1 hz assuming this class is simulated at once a second

    def __str__(self) -> str:
        return f'Flow Rate: {self.flow_rate}, Volume: {self.volume}, Leaking?: {self.is_leaking}'


v = Vessel(1.0, 10.0, True, 0.1)

while(True):
    v.update()
    print(v)
    time.sleep(SIMULATION_FREQUENCY_SECONDS) 