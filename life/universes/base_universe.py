from abc import ABCMeta, abstractmethod
from typing import Callable, Iterable, List, TypeVar, Tuple
from life.universe import Universe


T = TypeVar('T')


class BaseUniverse(Universe[T]):
    """
    Represents a base class for universes for 'The Game of Life'.
    The base universe is memory-efficient since it represents a sparse grid.
    So, it holds memory only for occuppied cells.
    """

    __metaclass__ = ABCMeta

    def __init__(self, width: int, height: int):
        if width <= 0:
            raise ValueError('width is zero or a negative number.')

        if height <= 0:
            raise ValueError('height is zero or a negative number.')

        self._width = width
        self._height = height
        self._data = dict()

    @property
    def width(self) -> int:
        """Returns universe width."""
        return self._width

    @property
    def height(self) -> int:
        """Returns universe height."""
        return self._height

    @abstractmethod
    def adjust_position(self, x: int, y: int) -> Tuple[int, int]:
        """Returns the universe position."""
        pass

    @abstractmethod
    def is_position_in_range(self, x: int, y: int) -> bool:
        """Indicates whether the specified position is within the universe boundaries."""
        pass

    @abstractmethod
    def empty(self) -> 'Universe[T]':
        """Returns an empty universe of the same dimensions."""
        pass

    def through(self) -> Tuple[int, int]:
        """Returns a new iterator that can iterate over universe positions."""
        return ((x, y) for y in range(self.height)
                       for x in range(self.width))

    def neighbours_of(self, x: int, y: int) -> Iterable[T]:
        """Returns a new iterator that can iterate over neighbours around the specified position."""
        positions = [
            (x - 1, y - 1),  # NE
            (x, y - 1),      # N
            (x + 1, y - 1),  # NW
            (x + 1, y),      # W
            (x + 1, y + 1),  # SW
            (x, y + 1),      # S
            (x - 1, y + 1),  # SE
            (x - 1, y)       # E
        ]

        return (self[position] for position in positions if self.is_position_in_range(*position))

    def __getitem__(self, position: Tuple[int, int]) -> T:
        """Returns a value for the specified position using self[x, y]."""
        adjusted_position = self.adjust_position(*position)
        item = self._data.get(adjusted_position, None)

        return item

    def __setitem__(self, position: Tuple[int, int], value: T):
        """Sets the value for the specified position using self[x, y]."""
        adjusted_position = self.adjust_position(*position)

        if value is None:
            return

        self._data[adjusted_position] = value

    def __str__(self) -> str:
        """Returns a string representation of the universe."""
        def to_str(i): return str(i or ' ')

        rows = ((to_str(self[x, y]) for x in range(self.width))
                                    for y in range(self.height))

        result = '\n'.join((''.join(row) for row in rows))

        return result

    def __eq__(self, other: 'BaseUniverse[T]') -> bool:
        """Indicates whether the universe equals to another universe."""
        eq = self._data.items() == other._data.items()

        return eq

    @classmethod
    def from_data(cls, *kargs: List[T]) -> 'Universe[T]':
        """Creates a universe from a 2-deminsiomal list."""
        universe = cls(len(kargs[0]), len(kargs))

        for x, y in universe.through():
            universe[x, y] = kargs[y][x] if x < len(kargs[y]) else None

        return universe

    @classmethod
    def random(cls, width: int, height: int, get_random: Callable[[], T]) -> 'Universe[T]':
        """Creates a random universe of the specified dimensions."""
        universe = cls(width, height)

        for x, y in universe.through():
            universe[x, y] = get_random()

        return universe