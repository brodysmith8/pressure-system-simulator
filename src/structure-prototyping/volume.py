class Volume:
    def __init__(self, static_volume: float, dynamic_volume: float = 0.0) -> None:
        self.static_volume = static_volume
        self.dynamic_volume = dynamic_volume

    def total(self) -> float:
        return self.static_volume + self.dynamic_volume

    # allows volumes to be added
    def __add__(self, other: "Volume") -> "Volume":
        static_sum = self.static_volume + other.static_volume
        dynamic_sum = self.dynamic_volume + other.dynamic_volume
        return Volume(static_sum, dynamic_sum)

    def __radd__(self, other: "Volume") -> "Volume":
        static_sum = self.static_volume + other.static_volume
        dynamic_sum = self.dynamic_volume + other.dynamic_volume
        return Volume(static_sum, dynamic_sum)

    def __str__(self) -> str:
        return f'Static Volume: {self.static_volume} m3, Dynamic Volume: {self.dynamic_volume} m3'
