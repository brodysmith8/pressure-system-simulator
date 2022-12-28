from system import System
from vessel import Vessel
from load import Load
from decimal import Decimal


# currently it connects a vessel to a Load
# but this should be changed in the future with a
# connector object
#
# what happens if multiple pipes are attached? i guess
# that update on the children would be called multiple times
#
# this should actually have a length and diameter so we
# can calculate its internal volume for equilibrium if
# the output is not accepting
class Pipe(System):
    def __init__(self, input: Vessel, output: Load) -> None:
        super().__init__()

        # order matters here
        self.add_subsystem(input)
        self.add_subsystem(output)

        self.input = input
        self.output = output

        # this should be a Gas object but we don't
        # have a physics system yet so its a decimal
        # that represents the amount of gas in L
        self._buffer_content = Decimal(0)  # L

        self._diameter = Decimal(7.415)  # m
        self._length = Decimal(2)  # m
        self._internal_volume = (Decimal(3.14159)
                                 * self._diameter
                                 * self._diameter
                                 * self._length)
        print(f'[Pipe] Internal Volume: {self._internal_volume} L')
        self.input.load_volume = min(self.output.required_volume, self._internal_volume)

    # right now, pipe also acts as a regulator and as a distributor.
    # Changing in future
    def update(self) -> None:
        # input
        if self._buffer_content + self.input.output_volume <= self._internal_volume:
            self._buffer_content += self.input.output_volume
        else:
            self.input.load_volume = self._internal_volume
            self._buffer_content = self._internal_volume

        print(f'[Pipe] Buffer size: {self._buffer_content} L')

        # output
        if self._buffer_content >= self.output.required_volume:
            self._buffer_content -= self.output.required_volume
            self.output.intake_volume = self.output.required_volume
        else:
            less_volume_than_required = self._buffer_content
            self._buffer_content -= self._buffer_content
            self.output.intake_volume = less_volume_than_required

        # ready to update children
