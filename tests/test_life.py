import unittest
from typing import List
from life import ClosedUniverse, live, originate_from


def neibours(count: int, cell = True) -> List[bool]:
    return [True] * count + [None] * (8 - count)


class LifeTestCase(unittest.TestCase):
    def test_live_cell_remains_dead(self):
        for alive in range(3):
            next_cell = live(None, neibours(alive), lambda: True)
            self.assertIsNone(next_cell)

        for neiboirs_exist in range(4, 8):
            next_cell = live(None, neibours(alive), lambda: True)
            self.assertIsNone(next_cell)

    def test_live_cell_survives(self):
        for alive in range(2, 3):
            next_cell = live(1, neibours(alive, 1), lambda: 2)
            self.assertEqual(next_cell, 1)

    def test_live_cell_dies(self):
        for alive in range(2):
            next_cell = live(True, neibours(alive), lambda: True)
            self.assertIsNone(next_cell)

        for alive in range(4, 9):
            next_cell = live(True, neibours(alive), lambda: True)
            self.assertIsNone(next_cell)

    def test_live_cell_regenerates(self):
        next_cell = live(None, neibours(3), lambda: True)
        self.assertTrue(next_cell)

    def test_originate_from_loaf(self):
        original_universe = ClosedUniverse.from_data(
            [None, True, True, None],
            [True, None, None, True],
            [None, True, None, True],
            [None, None, True, None]
        )

        generation = originate_from(original_universe, lambda: True)
        actual_universe = next(generation)

        self.assertEqual(actual_universe, original_universe)

    def test_originate_from_block(self):
        original_universe = ClosedUniverse.from_data(
            [None, None, None, None],
            [None, True, True, None],
            [None, True, True, None],
            [None, None, None, None]
        )

        generation = originate_from(original_universe, lambda: True)
        actual_universe = next(generation)

        self.assertEqual(actual_universe, original_universe)

    def test_originate_from_blinker(self):
        original_universe = ClosedUniverse.from_data(
            [None, True, None],
            [None, True, None],
            [None, True, None]
        )

        expected_universe = ClosedUniverse.from_data(
            [None, None, None],
            [True, True, True],
            [None, None, None]
        )

        generation = originate_from(original_universe, lambda: True)
        actual_universe = next(generation)

        self.assertEqual(actual_universe, expected_universe)

    def test_originate_from_toad(self):
        original_universe = ClosedUniverse.from_data(
            [None, None, None, None],
            [None, True, True, True],
            [True, True, True, None],
            [None, None, None, None]
        )

        expected_universe = ClosedUniverse.from_data(
            [None, None, True, None],
            [True, None, None, True],
            [True, None, None, True],
            [None, True, None, None]
        )

        generation = originate_from(original_universe, lambda: True)
        actual_universe = next(generation)

        self.assertEqual(actual_universe, expected_universe)


if __name__ == '__main__':
    unittest.main()
