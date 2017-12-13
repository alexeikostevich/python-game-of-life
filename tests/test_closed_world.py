import unittest
from life import ClosedWorld


class ClosedWorldTestCase(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            ClosedWorld(0, 1)

        with self.assertRaises(ValueError):
            ClosedWorld(1, 0)

        with self.assertRaises(ValueError):
            ClosedWorld(-1, 1)

        with self.assertRaises(ValueError):
            ClosedWorld(1, -1)

        self.assertIsInstance(ClosedWorld(1, 1), ClosedWorld)

    def test_width(self):
        world = ClosedWorld(2, 1)

        self.assertEqual(world.width, 2)

    def test_height(self):
        world = ClosedWorld(1, 2)

        self.assertEqual(world.height, 2)

    def test_get_positions(self):
        world = ClosedWorld(2, 2)

        self.assertEqual(list(world.get_positions()), [(0, 0), (1, 0), (0, 1), (1, 1)])

    def test_get_neighbours_of(self):
        world = ClosedWorld.from_data(
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        )

        neighbours = world.get_neighbours_of(0, 0)
        self.assertEqual(list(neighbours), [9, 7, 8, 2, 5, 4, 6, 3])

        neighbours = world.get_neighbours_of(2, 2)
        self.assertEqual(list(neighbours), [5, 6, 4, 7, 1, 3, 2, 8])

        neighbours = world.get_neighbours_of(1, 1)
        self.assertEqual(list(neighbours), [1, 2, 3, 6, 9, 8, 7, 4])

    def test_adjust_position(self):
        world = ClosedWorld(2, 2)

        self.assertEqual(world.adjust_position(-1, -1), (1, 1))
        self.assertEqual(world.adjust_position(2, 2), (0, 0))
        self.assertEqual(world.adjust_position(0, 0), (0, 0))

    def test_is_position_in_range(self):
        world = ClosedWorld(2, 2)

        self.assertTrue(world.is_position_in_range(-1, 0))
        self.assertTrue(world.is_position_in_range(2, 0))
        self.assertTrue(world.is_position_in_range(0, -1))
        self.assertTrue(world.is_position_in_range(0, 2))
        self.assertTrue(world.is_position_in_range(0, 0))

    def test_get_item(self):
        world = ClosedWorld.from_data(
            [1, 3],
            [2, None]
        )

        self.assertEqual(world[0, 0], 1)
        self.assertEqual(world[1, 1], None)
        self.assertEqual(world[-1, 0], 3)
        self.assertEqual(world[2, 0], 1)
        self.assertEqual(world[0, -1], 2)
        self.assertEqual(world[0, 2], 1)

    def test_set_item(self):
        world = ClosedWorld(2, 2)

        world[0, 0] = 1
        self.assertEqual(world[0, 0], 1)

        world[1, 1] = 2
        self.assertEqual(world[1, 1], 2)

        world[-1, 0] = 3
        self.assertEqual(world[1, 0], 3)

        world[2, 0] = 4
        self.assertEqual(world[0, 0], 4)

        world[0, -1] = 5
        self.assertEqual(world[0, 1], 5)

        world[0, 2] = 6
        self.assertEqual(world[0, 0], 6)

    def test_str(self):
        world = ClosedWorld.from_data(
            [None, 3],
            [2, None]
        )

        self.assertMultiLineEqual(str(world), '  3\n2  ')

    def test_empty_from(self):
        world = ClosedWorld.from_data(
            [1, 2],
            [3, None, 5]
        )

        empty_world = ClosedWorld.empty_from(world)

        self.assertEqual(empty_world.width, world.width)
        self.assertEqual(empty_world.height, world.height)

        all_empty = all(empty_world[position] is None for position in empty_world.get_positions())

        self.assertTrue(all_empty)

    def test_from_data(self):
        world = ClosedWorld.from_data(
            [1, 2],
            [3, None, 5]
        )

        self.assertEqual(world[0, 0], 1)
        self.assertEqual(world[1, 0], 2)
        self.assertEqual(world[0, 1], 3)
        self.assertEqual(world[1, 1], None)
        self.assertEqual(world[2, 1], 3)

    def test_random(self):
        world = ClosedWorld.random(2, 2, lambda: 1)

        self.assertEqual(world.width, 2)
        self.assertEqual(world.height, 2)
        self.assertEqual(world[0, 0], 1)
        self.assertEqual(world[1, 0], 1)
        self.assertEqual(world[0, 1], 1)
        self.assertEqual(world[1, 1], 1)


if __name__ == '__main__':
    unittest.main()
