from typing import TypeVar, Tuple
from ..universes.base_universe import BaseUniverse


T = TypeVar('T')


class ClosedUniverse(BaseUniverse[T]):
    """
    Represents the closed universe of 'The Game of Life'.
    The universe has edges beyond which no cells can exist.
    """

    def adjust_position(self, x: int, y: int) -> Tuple[int, int]:
        """Returns the universe position."""
        if (not self.is_position_in_range(x, y)):
            raise IndexError()

        return x, y

    def is_position_in_range(self, x: int, y: int) -> bool:
        """Indicates whether the specified position is within the universe boundaries."""
        is_in_range = 0 <= x < self.width and 0 <= y < self.height

        return is_in_range
